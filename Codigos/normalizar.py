#!/usr/bin/env jupyter
import numpy as np
import scipy as scp
from scipy.signal import medfilt
from scipy.signal import savgol_filter
from scipy.signal import spline_filter


def filtro(wave, flux, params, tipo='med'):
    if tipo == 'med':
        return medfilt(flux, *params)
    elif tipo == 'sg':
        return savgol_filter(flux, *params)
    elif tipo == 'spline':
        return spline_filter(flux, params)
