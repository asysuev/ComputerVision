import numpy as np
from procrustes import procrustes
from copy import deepcopy
import matplotlib as mp
from matplotlib.mlab import PCA
import matplotlib.pyplot as plt

def preprocess_lm(lm_array):
    xs = []
    ys = []
    for i in range(lm_array.size):
        if i%2==1:
            xs.append(lm_array[i])
        else:
            ys.append(lm_array[i])
    x = np.array(xs)
    y = np.array(ys)
    #translating to origin
    mux = x.mean()
    muy = y.mean()
    center = np.array([mux, muy])
    x_tr = x - mux #translate x and y (below) to origin
    y_tr = y - muy
    #scaling part
    scaling = np.sqrt(sum(x_tr*x_tr)+sum(y_tr*y_tr)) #sum of squares
    x_res = x_tr/scaling
    y_res = y_tr/scaling
    result = np.array([x_res, y_res])
    return center, scaling, result

def preprocess_all(landmarks):
    centers = {}
    scalings = {}
    pp_lms = {} #preprocessed landmarks
    for key in landmarks:
        centers[key]=[]
        scalings[key]=[]
        pp_lms[key]=[]
        for landmark in landmarks[key]:
            c, s, lm = preprocess_lm(landmark)
            centers[key].append(c)
            scalings[key].append(s)
            pp_lms[key].append(lm)
    return centers, scalings, pp_lms

def models_build(pp_lms, precision):
    models = {}
    means = {} #mean
    for key in pp_lms:
        means[key]=np.average(pp_lms[key], axis = 0)
    for key in pp_lms:
        i_r = deepcopy(pp_lms[key])
        d = 1
        while d > 1 - precision:
            err = []
            for item in i_r:
                er, item, a = procrustes(means[key], item)
                err.append(er)
            error = np.array(err)
            d = error.mean()
            means[key]=i_r
        models[key]=np.average(means[key], axis = 0)
    return models

def rearrange_landmarks(pp_lms):
    rearranged = {}
    for key in pp_lms:
        lms = []
        for lm in range(40):
            i_list=[]
            for coord in range(2):
                for i in range(len(pp_lms[key])):
                    i_list.append(pp_lms[key][i][coord][lm])
            i1 = np.array(i_list)
            lms.append(i1)
        rearranged[key]=np.array(lms)
    return rearranged

def pca(rearranged):
    eigenvectors = {}
    eigenvalues = {}
    proj_lms = {}
    sigmas = {}
    for key in rearranged:
        mu = rearranged[key].mean(axis=0)
        rearranged[key] = rearranged[key]-mu
        ev, eva, V = np.linalg.svd(rearranged[key].T, full_matrices=False)
        proj_d = np.dot(rearranged[key], ev)
        eigenvectors[key] = ev
        eigenvalues[key] = eva
        proj_lms[key] = proj_d
        sigma = proj_d.std(axis=0).mean()
        sigmas[key] = sigma
    return eigenvectors, eigenvalues, proj_lms, sigmas

def pca_analysis(ev, eva, f):
    eva_res={}
    ev_res={}
    for key in eva:
        s = eva[key].sum()
        eva_n = []
        for val in eva[key]:
            eva_n.append(val)
            if np.array(eva_n).sum()>=f*s:
                eva_n = eva_n[:-1]
                break
        eva_res[key] = np.array(eva_n)
        ev_i = []
        for i in range(len(ev[key].size)):
            for j in range(len(eva_n))
            ev_i.append(ev[key][i][j])
        ev_res[key]=np.array(ev_i)
    return ev_res, eva_res

def define_b(rearranged, ev):
    b = {}
    for key in rearranged:
        mu = rearranged[key].mean(axis=0)
        i_m = rearranged[key]-mu
        b[key]=np.dot(ev[key].T, i_m)
    return b


def model_show(models, key):
    plot = plt.figure()
    plt.plot(models[key][0], models[key][1])
    plt.show(plot)
