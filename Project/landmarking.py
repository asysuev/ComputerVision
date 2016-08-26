def lm_files(path_to_image):
    path_to_landmarks = '/Users/asysuev/OneDrive/Study/KULeuven/ComputerVision/Project Data(2)/_Data/Landmarks/original/'
    im_path = str(Image)
    landmarks = {}
    lm_name = 'landmarks'
    im_number_str = str(int(im_path[-6:][:2]))
    for i in range(1,9):
        key = str(i)
        landmarks[key]=path_to_landmarks+lm_name+im_number_str+'-'+key
    return landmarks
