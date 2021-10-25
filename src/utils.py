import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

_xsourse_radius = 500  # 这是x射线源半径
_det_radius = 500  # 这是探测器半径
_det_dist = 1  # 这是探测器大小，在做仿真时射线与探测器中心连线，后面会说到
_det_size = 512  # 这是所有探测器整个的长度
_det_num = 512  # 这是探测器个数

_angle_num = 180  # 这是总旋转角个数
_angle_size = 180  # 这是总旋转角度
_delta_angle = _angle_size / _angle_num * np.pi  # 测量间距

_det = np.linspace(-(_det_size / 2 - _det_dist / 2), (_det_size / 2 - _det_dist / 2), _det_num)


# 获取射线源坐标
def get_xsourse_xy(theta):
    x = _xsourse_radius * sin(theta)
    y = _xsourse_radius * cos(theta)
    return x, y


# 获取探测器坐标（第num个）
def get_det_xy(theta, num):
    # 首先确定垂心坐标
    x_mid = _det_radius * sin(theta + pi)  # 与射线对称方向
    y_mid = _det_radius * cos(theta + pi)

    # 接下来计算第num个的坐标偏移
    offset = _det[num]
    x_offset = offset * cos(theta)
    y_offset = offset * sin(theta)

    return (x_mid + x_offset), (y_mid + y_offset)
