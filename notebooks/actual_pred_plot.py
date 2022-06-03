# actual vs pred plot
def actual_pred_plot(actual, preds):
    import pandas as pd
    import numpy as np
    actual_pred = pd.DataFrame(columns=['Actual', 'Predict'])
    actual_pred['Actual'] = actual['2020':][0:len(preds)]
    actual_pred['Predict'] = preds
    
    from tensorflow.keras.metrics import MeanSquaredError
    m = MeanSquaredError()
    m.update_state(np.array(actual_pred['Actual']), np.array(actual_pred['Predict']))
    
    
    return m.result().numpy(), actual_pred
    