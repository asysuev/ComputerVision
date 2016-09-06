import numpy as np
import matplotlib.pyplot as plt
import cv2

def pyramid(image):
    images = [image]
    for i in range(5):
        lower_reso = cv2.pyrDown(images[i])
        blur = cv2.GaussianBlur(lower_reso, (5,5), 0)
        images.append(blur)
    return images

def edges_detection(images):
    edges_pyramid = []
    for image in images:
        edges = cv2.Canny(image, 40, 80)
        edges_pyramid.append(edges)
    return edges_pyramid

def images_preprocess(images):
    images_res = {}
    edges = {}
    for key in images:
        image = images[key]
        images_res[key] = pyramid(image)
        edges[key] = edges_detection(images_res[key])
    return images_res, edges
