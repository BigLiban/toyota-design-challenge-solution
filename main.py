from google.colab import drive
drive.mount('/content/gdrive')

# import dependencies
import os
import sys

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

import cv2

import ipywidgets as widgets
from ipywidgets import interact, interact_manual

from IPython.display import display, Javascript, Image

from google.colab.output import eval_js
from base64 import b64decode, b64encode
import PIL
import io
import html
import time

#Get Python and OpenCV Version

print('OpenCV-Python Lib Version:', cv2.__version__)
print('Python Version:',sys.version)


# # Download the test image
# !wget --no-check-certificate \
#     https://raw.githubusercontent.com/computationalcore/introduction-to-opencv/master/assets/noidea.jpg \
#     -O noidea.jpg

# # Download other Sample Images
# !wget --no-check-certificate \
#     https://raw.githubusercontent.com/MeAmarP/sample_imgs/master/wiki_shapes.jpg \
#     -O wiki_shapes.jpg

# !wget --no-check-certificate \
#     https://raw.githubusercontent.com/MeAmarP/sample_imgs/master/indian_coins.jpg \
#     -O indian_coins.jpg