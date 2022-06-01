# GRU model
def GRU_model(X_train, y_train, X_test, sc, artist):
    # import
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, SimpleRNN, GRU
    from tensorflow.keras.optimizers import SGD
    from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
    
    # GRU architecture
    my_GRU_model = Sequential()
    my_GRU_model.add(GRU(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1), activation='tanh'))
    my_GRU_model.add(GRU(units=50, activation='tanh'))
    my_GRU_model.add(Dense(units=13))
    
    # Compile
    my_GRU_model.compile(optimizer=SGD(learning_rate=0.05, decay=1e-7, momentum=0.9, nesterov=False), 
                         loss='mean_squared_error')
    
    # Early Stop, Model Checkpoint
    es = EarlyStopping(patience=30)
    mc = ModelCheckpoint('../models/checkpoint/{}.h5'.format(artist), save_best_only=True, monitor='val_loss')
    
    # Fitting
    history = my_GRU_model.fit(X_train[:-26], y_train[:-26], epochs=150, batch_size=8, verbose=0, validation_data=(X_train[-26:], y_train[-26:]), callbacks=[es, mc])
    my_GRU_model.load_weights('../models/checkpoint/{}.h5'.format(artist))
                     
    GRU_prediction = my_GRU_model.predict(X_test)
    GRU_prediction = sc.inverse_transform(GRU_prediction)
    
    return my_GRU_model, GRU_prediction, history