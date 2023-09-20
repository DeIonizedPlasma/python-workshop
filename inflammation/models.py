"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    Parameters
    ----------
    filename : string
        Path of csv file to load

    Returns
    -------
    np.ndarray of loaded txt
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    Parameters
    ----------
    data : list or np.ndarray
        Data to calculate mean of

    Returns
    -------
    float representing mean of data
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    Parameters
    ----------
    data : list or np.ndarray of data

    Returns
    -------
    Maximum value(s) of data along principal axis. For data w/ shape (a,b,c,...)
    then returned array will have shape (b,c,...).
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    Parameters
    ----------
    data : list or np.ndarray of data

    Returns
    -------
    Minimum value(s) of data along principal axis. For data w/ shape (a,b,c,...)
    then returned array will have shape (b,c,...).
    -------
    """
    return np.min(data, axis=0)

