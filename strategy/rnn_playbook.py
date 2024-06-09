
import pandas as pd
import numpy as np

import lightning as pl
import os
import torch
import pickle
import torch.nn as nn
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split
from collections import OrderedDict
from lightning.pytorch.loggers.csv_logs import CSVLogger
from lightning.pytorch.callbacks import ModelCheckpoint, early_stopping
from lightning import Trainer
from datetime import datetime
from tqdm import tqdm

# global variables
log_path = '/Users/zehoo/Documents/Course/quant_playbook/logs'
model_name = 'RNN' # RNN LSTM GRU
version_name = datetime.now().strftime("%Y%m%d_%H%M%S")
max_epochs = 500
seq_len = 5
input_size = 37
batch_size = 512

def rolling_window(arr, window_size):
    if window_size < 1:
        # raise ValueError("Window size must be at least 1.")
        return None
    if window_size > arr.shape[0]:
        # raise ValueError("Window size is too big for the array.")
        return None
    shape = (arr.shape[0] - window_size + 1, window_size, arr.shape[1])
    strides = (arr.strides[0], arr.strides[0], arr.strides[1])
    return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)



class TimeseriesDataset(Dataset):   
    '''
    Custom Dataset subclass. 
    Serves as input to DataLoader to transform X 
      into sequence data using rolling window. 
    DataLoader using this dataset will output batches 
      of `(batch_size, seq_len, n_features)` shape.
    Suitable as an input to RNNs. 
    '''
    def __init__(self, X: np.ndarray, y: np.ndarray):
      self.X = X
      self.y = y
  

    def __len__(self):
        return self.X.__len__() 

    def __getitem__(self, index):
      # if np.any(np.isnan(self.y[index])) or np.any(np.isnan(self.X[index])):
      #   print(1)
      return (torch.from_numpy(self.X[index]).float(), torch.tensor([self.y[index]]).float())

from torch.utils.data import DataLoader

class DInterface(pl.LightningDataModule):
    '''
    PyTorch Lighting DataModule subclass:
    https://pytorch-lightning.readthedocs.io/en/latest/datamodules.html

    Serves the purpose of aggregating all data loading
      and processing work in one place.
    '''

    def __init__(self, data, seq_len, batch_size):
        super().__init__()
        self.data = data
        self.seq_len = seq_len
        self.batch_size = batch_size
        self.X_train = None
        self.y_train = None
        self.X_val = None
        self.y_val = None
       
        
    def sliding_data(self, data, seq_len):
        data_X_sliding, data_y_sliding = [], []
        for code,  data_code in data.groupby('ts_code'):
            data_code = data_code.sort_index()
            data_code_X = data_code.iloc[:, 1:-1]
            data_code_y = data_code.iloc[:, -1]
            data_code_X_sliding = rolling_window(data_code_X.values, seq_len)
            data_code_y_sliding = data_code_y.values[seq_len-1:]
            if not (data_code_X_sliding is None):
                data_X_sliding.extend(data_code_X_sliding.tolist())
                data_y_sliding.extend(data_code_y_sliding.tolist())
        
        data_X_sliding = np.array(data_X_sliding)
        data_y_sliding = np.array(data_y_sliding)
        return data_X_sliding, data_y_sliding
    
    
    def split_train_val(self, data):
        # uindex = np.unique(self.data[DATE_NAME].values)
        train_date, val_date = train_test_split(data.index.unique(), test_size=0.1)
        train_data = data.loc[train_date]
        val_data = data.loc[val_date]
        return train_data, val_data
        
        
    def setup(self, stage=None):
        if stage == 'fit' and self.X_train is not None:
            return
        if stage is None and self.X_train is not None:
            return
        train_data, val_data = self.split_train_val(self.data)
        self.X_train, self.y_train = self.sliding_data(train_data, self.seq_len)
        self.X_val, self.y_val = self.sliding_data(val_data, self.seq_len)
     
    def train_dataloader(self):
        train_dataset = TimeseriesDataset(self.X_train,
                                          self.y_train)
        train_loader = DataLoader(train_dataset,
                                  batch_size=self.batch_size,
                                  shuffle=True)

        return train_loader

    def val_dataloader(self):
        val_dataset = TimeseriesDataset(self.X_val,
                                        self.y_val)
        val_loader = DataLoader(val_dataset,
                                batch_size=self.batch_size,
                                shuffle=False)

        return val_loader
    

class CustomRNN(pl.LightningModule):
    def __init__(self, input_size, nn_type):
        super(CustomRNN, self).__init__()
        self.nn_type = nn_type
        self.rnn_layers = nn.ModuleDict({
            'RNN': nn.RNN(input_size=input_size, hidden_size=100, num_layers=2, dropout=0.2, batch_first=True),
            'LSTM': nn.LSTM(input_size=input_size,  hidden_size=100, num_layers=2,  dropout=0.2, batch_first=True),
            'GRU': nn.GRU(input_size=input_size, hidden_size=100,  num_layers=2, dropout=0.2, batch_first=True)
        })
      
        self.fc = nn.Linear(100, 1)  # 输出维度为 1
        

    def forward(self, x):
        # (batch_size, time_steps, input_size)
        rnn_out, _ = self.rnn_layers[self.nn_type](x)
        # 只取序列的最后一个时间步
        out = self.fc(rnn_out[:, -1, :])
        return out

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = nn.functional.mse_loss(y_hat, y)  # 损失函数
        self.log('train_loss', loss)
    
    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = nn.functional.mse_loss(y_hat, y)  # 损失函数
        self.log('val_loss', loss)

    def configure_optimizers(self):
        optimizer = torch.optim.RMSprop(self.parameters(), lr=0.001)  # RMSProp 优化器
        return optimizer
    
    
class PredTimeseriesDataset(Dataset):   
    def __init__(self, X: np.ndarray):
      self.X = X
    def __len__(self):
        return self.X.__len__() 
    def __getitem__(self, index):
        return torch.from_numpy(self.X[index]).float()

class PInterface:
    def __init__(self, model, filename, data, seq_len, input_size, nn_type, model_path) -> None:
        self.seq_len = seq_len
        self.model_path = model_path
        self.nn_type = nn_type
        self.data = data
        self.net = self._load_model(model, filename, input_size, nn_type)
        
    def _load_model(self, model, filename, input_size, nn_type):
        file_path = f'{self.model_path}/checkpoints/{filename}.ckpt'
        checkpoint = torch.load(file_path) 
        params = OrderedDict([(k, v) for (k, v) in checkpoint["state_dict"].items()  if k not in ["epoch", "global_step", "pytorch-lightning_version", "state_dict", "loops", "callbacks", "optimizer_states", "lr_schedulers"]])
        init_net = model(input_size, nn_type) 
        init_net.load_state_dict(params)
        return init_net
    
    def sliding_data(self, data, seq_len):
        data_X_sliding, index_sliding = [], []
        for code,  data_code in data.groupby('ts_code'):
            data_code = data_code.sort_index()
            data_code_X = data_code.iloc[:, 1:-1]
            data_code_X_sliding = rolling_window(data_code_X.values, seq_len)
            data_code_index_sliding = list(zip(data_code.index.values[seq_len-1:], [code]*(len(data_code)-seq_len+1)))
            if not (data_code_X_sliding is None):
                data_X_sliding.extend(data_code_X_sliding.tolist())
                index_sliding.extend(data_code_index_sliding)
        
        data_X_sliding = np.array(data_X_sliding)
        index_sliding = np.array(index_sliding)
        return data_X_sliding, index_sliding
    
    def _stepwise_pred(self, x:torch.tensor):
        self.net.eval()
        out = self.net(x)
        out = out.cpu().detach().numpy().ravel()
        return out
    
    
    def pred(self, batch_size:int =128):
        pred_X, pred_index = self.sliding_data(self.data.copy(), self.seq_len)
        Pred_Dataset = PredTimeseriesDataset(pred_X)
        Pred_Dataloader = DataLoader(Pred_Dataset, batch_size=batch_size, shuffle=False)
        predictions = []
        with torch.no_grad():
            progress_bar = tqdm(Pred_Dataloader)
            for idx, batch in enumerate(progress_bar):
                inputs = batch
                outputs = self._stepwise_pred(inputs)
                predictions.extend(outputs)
                
        res = pd.DataFrame(np.array([
            [item[0] for item in pred_index], 
            [item[1] for item in pred_index], 
            predictions]).T, columns=['date', 'ts_code', f'fac_{self.nn_type.lower()}'])
        print(res)
        return res
    

def main_train():
    version_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    insample_data = pd.read_parquet('./data/temp_insample_data.parquet')
    csv_logger = CSVLogger(log_path, name=model_name, version=version_name)
    checkpoint_callback = early_stopping.EarlyStopping(monitor='val_loss', min_delta=0.0, patience=10, verbose=False, mode='min', strict=True, check_on_train_epoch_end=False)
    trainer = Trainer(
        accelerator = 'cpu',
        max_epochs=max_epochs,
        logger=csv_logger,
        log_every_n_steps = 100,
        callbacks=[checkpoint_callback]
    )

    model = CustomRNN(input_size, model_name)
    data_module = DInterface(insample_data, seq_len, batch_size)
    trainer.fit(model=model, datamodule=data_module)
    
def main_pred(model_id):
    version_name = '20231217_093917'
    outsample_data = pd.read_parquet('./data/temp_outsample_data.parquet')
    model_path = f"{log_path}/{model_name}/{version_name}"
    pred_batch_size = 512
    rpd = PInterface(CustomRNN, model_id, outsample_data, seq_len, input_size, model_name, model_path)
    outsample_pred = rpd.pred(batch_size=pred_batch_size)
    fac_data = outsample_pred.reset_index().sort_values(['date', 'ts_code']).set_index('date')
    return fac_data


if __name__ == '__main__':
    
    # main_train()
    dates = pd.to_datetime(pickle.load(open('./fundmental/date.pkl', 'rb')))
    mask = (dates >= pd.Timestamp('2017-01-01')) & (dates <= pd.Timestamp('2021-12-31'))
    backtest_dates = dates[mask]
    fac_data = main_pred('epoch=10-step=484')
    fac_data = fac_data.drop(columns=['index'])
    
    fac_data_daily = pd.DataFrame()
    for code, fac_data_code in fac_data.groupby('ts_code'):
        fac_data_code_ = fac_data_code.reindex(backtest_dates).bfill()
        fac_data_daily = pd.concat([fac_data_daily, fac_data_code_])
    
    fac_data_daily = fac_data_daily.reset_index().rename(columns={'index': 'date', 'ts_code':'code'}).dropna()
    fac_data_daily = fac_data_daily.sort_values(['date', 'code'])   
    
    path = f'./feature/{model_name.lower()}_pred'
    if not os.path.exists(path):
        os.makedirs(path)

    for date, fac_data_date in fac_data_daily.groupby('date'):
        fac_data_daily_ = fac_data_date.drop(columns=['date'])
        fac_data_daily_[f'fac_{model_name.lower()}'] = fac_data_daily_[f'fac_{model_name.lower()}']
        date = date.strftime('%Y-%m-%d')
        fac_data_daily_.to_csv(f'./feature/{model_name.lower()}_pred/{date}.csv', index=False)