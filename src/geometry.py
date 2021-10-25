import numpy as np
from numpy import sin, cos, pi


class Geometry():
    _Raysourse_radius = 500  # 这是x射线源半径
    _Det_radius = 500  # 这是探测器半径,准确说是与中心垂线长度，因为这里探测器是平面而不是圆弧
    _Det_size = 1  # 这是探测器大小，在做仿真时射线与探测器中心连线，后面会说到
    _Det_length = 512  # 这是所有探测器整个的长度
    _Det_num = 512  # 这是探测器个数

    _Angle_num = 180  # 这是总旋转角个数
    _Theta = pi  # 这是旋转角度
    _Delta_angle = 0  # 测量间距

    def Geometry(self,
                 sourse_radius=500,
                 det_radius=500,
                 det_size=1,
                 det_length=512,
                 det_num=512,
                 angle_num=180,
                 theta=pi):
        self._Raysourse_radius = sourse_radius
        self._Det_radius = det_radius
        self._Det_size = det_size
        self._Det_length = det_length
        self._Det_num = det_num
        self._Angle_num = angle_num
        self._Theta = theta
        self._Delta_angle = self._Theta / self._Angle_num

    def _get_Raysourse_radius(self):
        return self._Raysourse_radius

    def _get_Det_radius(self):
        return self._Det_radius

    def _get_Det_size(self):
        return self._Det_size

    def _get_Det_length(self):
        return self._Det_length

    def _get_Det_num(self):
        return self._Det_num

    def _get_Angle_num(self):
        return self._Angle_num

    def _get_Theta(self):
        return self._Theta

    def _get_Delta_angle(self):
        return self._Delta_angle


class Raysourse():
    def Raysourse(self, radius):
        self._radius = radius
        self._update_xy()  # 更新射线源坐标

    _x, _y = 0, 0
    _angle = 0
    _radius = 500

    def _set_angle(self, ang):
        self._angle = ang
        self._update_xy()

    def _update_xy(self):
        self._x = self._radius * sin(self._angle)
        self._y = self._radius * cos(self._angle)


class Detectors():
    _Det_radius = 500
    _Det_size = 1  # 这是探测器大小，在做仿真时射线与探测器中心连线，后面会说到
    _Det_length = 512  # 这是所有探测器整个的长度
    _Det_num = 512  # 这是探测器个数
    _angle = 0
    _dets_x = [0]*_Det_num  # 每个探测器中心的横坐标
    _dets_y = [0]*_Det_num
    _dets = np.linspace(-(_Det_length/2-_Det_size/2), (_Det_length/2-_Det_size/2), _Det_num)  # 这个dets记录相对关系(探测器中心接受射线)

    def Detectors(self,
                  det_radius=500,
                  det_length=512,
                  det_num=512):
        self._Det_radius = det_radius
        self._Det_length = det_length
        self._Det_num = det_num
        self._Det_size = self._Det_length/self._Det_num

    def _set_angle(self, ang):
        self._angle = ang
        self._update_dets()

    def _update_dets(self):
        # 首先确定垂心坐标
        x_mid = self._Det_radius * sin(self._angle + pi)  # 与射线对称方向
        y_mid = self._Det_radius * cos(self._angle + pi)

        # 接下来计算第i个的坐标偏移
        for i in range(self._Det_num):
            offset = self._dets[i]  # 和中心的距离差(三角形斜边)
            x_offset = offset * cos(self._angle)
            y_offset = offset * sin(self._angle)
            self._dets_x[i] = x_mid + x_offset
            self._dets_y[i] = y_mid + y_offset

    def _get_dets(self):
        return self._dets_x, self._dets_y


