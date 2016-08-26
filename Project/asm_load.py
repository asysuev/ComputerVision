import numpy as np
import cv2


def lm_files_to_dict(path = '/Users/asysuev/OneDrive/Study/KULeuven/ComputerVision/Project Data(2)/_Data/Landmarks/', dest = 'original'):
    """
    A preliminary loader of landmark files in format provided in project

    Load names of files into dictionary for easiness of further loading

    Inputs:
    __________
    path
        Absolute path where lies the files (optional)
        By default: absolute path at my laptop
    dest
        Original or mirrored landmark files to search
        By default: Original

    Outputs:
    ___________
    landmark_files
            Dictionary with pathes to every landmark file (presented in project, so 14 files for each of the incisors)

    """
    path_to_landmarks = path+dest+'/'
    landmark_files = {}
    lm_name = 'landmarks'
    for i in range(1,9):
        key = str(i)
        landmark_files[key]=[]
        for j in range(1,15):
            landmark_files[key].append(path_to_landmarks+lm_name+str(j)+'-'+key+'.txt')
    return landmark_files

def load_landmarks(landmark_files):
    """
    Load landmarks from list of files
    Landmarks stored as nparrays

    Inputs
    ___________
    landmark_files
        Dictionary of pathes to landmarks of every incisor

    Outputs
    ___________
    landmarks
        Dictionary of numpy arrays for every incisor    
    """
    landmarks = {}
    for key in landmark_files:
        landmarks[key]=[]
        for fl in landmark_files[key]:
            with open(fl) as infile:
                data = infile.readlines()
            landmarks_1 = []
            for line in data:
                landmarks_1.append(float(line))
            landmarks[key].append(np.asarray(landmarks_1))
    return landmarks

def load_images(path = '/Users/asysuev/OneDrive/Study/KULeuven/ComputerVision/Project Data(2)/_Data/Radiographs/'):
    images = {}
    path_end = '.tif'
    for i in range(1, 15):
        key = str(i)
        path_to_img = path+key.zfill(2)+path_end
        images[key] = cv2.imread(path_to_img, 0)
    return images
