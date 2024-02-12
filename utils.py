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

import wget
import os

def download_data(output: str):
    """Download sherlock dataset"""

    # sherlock data URLs
    url_sherlock = 'https://ndownloader.figshare.com/files/9017983'
    url_AG_movie = 'https://ndownloader.figshare.com/files/9055612'

    # download data
    wget.download(url_sherlock, out=os.path.join(output, 'sherlock.h5'))
    wget.download(url_AG_movie, out=os.path.join(output, 'AG_movie_1recall.h5'))  

    # check
    if os.path.exists(os.path.join(output, 'sherlock.h5')) and \
    os.path.exists(os.path.join(output, 'AG_movie_1recall.h5')):
        print(f'Successful download in \t {output}')

    else:
        print(f'Failed to download in \t {output}')


def load_data(path, dataset) -> np.ndarray:
    """Load sherlock data
    
    Parameters
    ----------
    path: str or os.path.object
        Path to data directory

    dataset: str
        'sherlock' or 'AG_movie_1_recall'

    Return
    -------
    D: numpy.ndarray
    """

    D = dd.io.load(os.path.join(path, f'{dataset}.h5'))

    print(f'Access variables like \n D["BOLD"] \n D["coords"] \n D["human_bounds"]')

    return D

