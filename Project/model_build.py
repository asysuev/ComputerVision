import numpy as np
from procrustes import procrustes

def preprocess_lm(lm_array):
    xs = []
    ys = []
    for i in lm_array.size:
        if i%2==1:
            xs.append(lm_array[i])
        else:
            ys.append(lm_array[i])
    x = np.array(xs)
    y = np.array(ys)
    original = np.array([x,y])
    #translating to origin
    mux = x.mean
    muy = y.mean
    center = np.array([mux, muy])
    x_tr = x - mux #translate x and y (below) to origin
    y_tr = y - muy
    #scaling part
    scaling = np.sqrt(sum(x_tr*x_tr)+sum(y_tr*y_tr)) #sum of squares
    x_res = x_tr/scaling
    y_res = y_tr/scaling
    result = np.array([x_res, y_res])
    return original, center, scaling, result
