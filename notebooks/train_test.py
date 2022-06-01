# train test split & scaler
def train_test(all_data, time_steps, for_periods):
    import numpy as np
    import pandas as pd

    # training & test set
    train = all_data[:'2019'].values
    test = all_data['2020':].values
    train_len = len(train)
    test_len = len(test)
    
    # min max scaler
    from sklearn.preprocessing import MinMaxScaler
    sc = MinMaxScaler()
    train = sc.fit_transform(train.reshape(-1,1))
    
    # train & test slicing with time steps and periods
    X_train = []
    y_train = []
    y_train_stacked = []
    for i in range(time_steps, train_len-for_periods+1):
        X_train.append(train[i-time_steps:i])
        y_train.append(train[i:i+for_periods])
    X_train, y_train = np.array(X_train), np.array(y_train)
    
    # reshape to 3-dimensional
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    # preparing to create X_test
    inputs = pd.concat((all_data[:'2019'], all_data['2020':]), axis=0).values
    inputs = inputs[len(inputs) - len(test) - time_steps:]
    inputs = sc.transform(inputs.reshape(-1,1))
    
    X_test = []
    for i in range(time_steps, test_len+time_steps-for_periods):
        X_test.append(inputs[i-time_steps:i])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    return X_train, y_train, X_test, sc