import numpy as np
from numpy import sin, cos, pi
from .geometry import *


class volume():
    _Img_size = 512
    _Img = np.zeros((512, 512))

    def volume(self, img):
        self._Img_size = img.shape[0]
        self._Img = img

    def _get_val(self, x, y):
        # 坐标转换
        return self._Img[int(np.ceil(x-self._Img_size/2)), int(np.ceil(y-self._Img_size/2))]

    def _set_vol(self, img):
        self._Img = img / np.float32(1.0)

    def _get_vol(self):
        return self._Img
