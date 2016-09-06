import asm_load as l
import model_build as mb
import image_preprocess as ip
import model_fit as mf

def prelim(path_to_img = '/Users/asysuev/OneDrive/Study/KULeuven/ComputerVision/Project Data(2)/_Data/Radiographs/', path_to_lm = '/Users/asysuev/OneDrive/Study/KULeuven/ComputerVision/Project Data(2)/_Data/Landmarks/', dest= 'original'):
    """
        Loading, prerpocessing, model build and PCA analysis
        Inputs
        ____________
        path_to_img
            Path, where training images are stored
        path_to_lm
            Path, where landmarks of training images are stored
        dest
            Use original or mirrored landmarks. Folder with landmarks should have at least folder named original
        Outputs
        ____________
        landmarks
            Dictionary, containing landmarks for each tooth
        models
            Dictionary, containing models for each tooth
        ev
            Eigenvectors of landmarks distribution
        eva
            Eigenvalues, corresponding to ev
        b
            b vector for model fitting
        images
            Dictionary of Radiographs
        pp_imgs
            Dictionary of preprocessed images (Gaussian pyramid)
        pp_edges
            Dictionary of edges, corresponding to pp_imgs
    """
    images = l.load_images(path_to_img)
    landmarks = l.load_landmarks(l.lm_files_to_dict(path_to_lm, dest))
    centers, scalings, pp_lms = mb.preprocess_all(landmarks)
    models = mb.models_build(pp_lms, 0.98)
    rearranged = mb.rearrange_landmarks(pp_lms)
    ev, eva, p_lms, sigmas = pca(rearranged)
    ev, eva = mb.pca_analysis(ev, eva, 0.95)
    b = mb.define_b(rearranged, ev)
    pp_imgs, pp_edges = ip.images_preprocess(images)
    return landmarks, models, ev, eva, b, images, pp_imgs, pp_edges
#TODO Add model fitting and entrance points
