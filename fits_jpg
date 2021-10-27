#!/usr/bin/python
# -*- coding:  cp1251 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:38:11 2019

@author: liuqiang
"""
import random as random_number
import sys
import math
import numpy as np
from scipy import stats
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.ticker import NullFormatter
from numpy import *
from pylab import *
import os
import glob
import shutil
#import subprocess
import signal


import subprocess as sub


# Function to create png files using ds9

def ds9_image(image,name):
	sub.call("ds9 %s -scale zscale -export jpg %s.jpg -exit" % (image,name), shell=True, close_fds=False)

# fits所在路径
data_path = r"D:/A_Postgraduate/den/bila/bila_4/"
fits_path = os.path.join(data_path,'*.fit*')
fits_list = glob.glob(fits_path)

for index,fit in enumerate(fits_list):
    name_index = fit.split("/")[-1].split(".fits")[0]
    ds9_image(fit,name_index)

print("completed!!!")










