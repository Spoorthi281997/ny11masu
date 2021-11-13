import numpy as np
from ipywidgets import interact,fixed
from PIL import Image

def imshow(X, resize=none):
    img = Image.fromarray(X)
    resize = img.resize(size=(100, 100))
    return resize

