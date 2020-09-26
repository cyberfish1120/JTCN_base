import time
import datetime
import numpy as np
import scipy
import tensorflow as tf
from bert.tokenization import FullTokenizer
from tqdm import tqdm
import tensorflow_hub as hub
from sklearn import preprocessing as prep


class timer(object):
    def __init__(self, name='default'):
        """
        timer object to record running time of functions, not for micro-benchmarking
        usage is:
            $ timer = utils.timer('name').tic()
            $ timer.toc('process A').tic()


        :param name: label for the timer
        """
        self._start_time = None
        self._name = name
        self.tic()

    def tic(self):
        self._start_time = time.time()
        return self

    def toc(self, message):
        elapsed = time.time() - self._start_time
        message = '' if message is None else message
        print('[{0:s}] {1:s} elapsed [{2:s}]'.format(self._name, message, timer._format(elapsed)))
        return self

    def reset(self):
        self._start_time = None
        return self

    @staticmethod
    def _format(s):
        delta = datetime.timedelta(seconds=s)
        d = datetime.datetime(1, 1, 1) + delta
        s = ''
        if (d.day - 1) > 0:
            s = s + '{:d} days'.format(d.day - 1)
        if d.hour > 0:
            s = s + '{:d} hr'.format(d.hour)
        if d.minute > 0:
            s = s + '{:d} min'.format(d.minute)
        s = s + '{:d} s'.format(d.second)
        return s


def batch(iterable, _n=1, drop=True):

    it_len = len(iterable)
    for ndx in range(0, it_len, _n):
        if ndx + _n < it_len:
            yield iterable[ndx:ndx + _n]
        elif drop is False:
            yield iterable[ndx:it_len]


def tfidf(x):
    x_idf = np.log(x.shape[0] - 1) - np.log(1 + np.asarray(np.sum(x > 0, axis=0)).ravel())
    x_idf = np.asarray(x_idf)
    x_idf_diag = scipy.sparse.lil_matrix((len(x_idf), len(x_idf)))
    x_idf_diag.setdiag(x_idf)
    x_tf = x.tocsr()
    x_tf.data = np.log(x_tf.data + 1)
    x_tfidf = x_tf * x_idf_diag
    return x_tfidf


def prep_standardize(x):
    std = 5
    x_nzrow = x.any(axis=1)
    scaler = prep.StandardScaler().fit(x[x_nzrow, :])
    x_scaled = np.copy(x)
    x_scaled[x_nzrow, :] = scaler.transform(x_scaled[x_nzrow, :])
    x_scaled[x_scaled > std] = std
    x_scaled[x_scaled < -std] = -std
    x_scaled[np.absolute(x_scaled) < 1e-5] = 0
    return scaler, x_scaled



