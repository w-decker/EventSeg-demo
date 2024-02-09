#!/usr/bin/env brainiak_env

# imports
from brainiak.eventseg.event import EventSegment

import scipy.io
from scipy import stats
from scipy.stats import norm, zscore, pearsonr
from scipy.signal import gaussian, convolve

from sklearn import decomposition
from sklearn.model_selection import LeaveOneOut, KFold

import nibabel as nib
from nilearn.input_data import NiftiMasker

import numpy as np
import deepdish as dd

