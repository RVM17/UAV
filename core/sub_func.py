from math import sin, cos, acos, tan, sqrt, ceil, floor, radians, pi


class trajectory:

    def __init__(self, x0: float, y0: float, height: float):
        self.h = height
        self.x0 = x0
        self.y0 = y0
        self.radius = None
        self.count_point = None
        self.a = None
        self.b = None
        self.angle = None
        self.delta_l = None
        self.delta_R = None
        self.count_branch = None
        self.points: list[list[float, float, float, float]] = list()
        cam_angle = 84
        delta = round(16 * 2 * self.h * tan(radians(cam_angle / 2)) * sqrt(1 / (16 ** 2 + 9 ** 2)))
        delta -= 0.1 * delta
        self.delta_l = floor(delta)

    def set_start_point(self):
        self.points.append([self.x0, self.y0, self.h])

    def set_circle_params(self, radius: float, count_point: int):
        self.radius = radius
        self.count_point = count_point
        self.delta_R = self.delta_l / self.count_point
        self.count_branch = ceil(self.radius / self.delta_l)

    def set_rect_params(self, a: float, b: float, angle: float):
        self.a = a
        self.b = b
        self.angle = angle

    def calculate(self, segment: int):
        ang = 360 / self.count_point * segment
        y = self.y0 + self.radius * sin(radians(ang))
        x = self.x0 + self.radius * cos(radians(ang))
        self.points.append([round(x, 1), round(y, 1), self.h, 0.0])

    def rect(self):
        x_ctrl = self.x0 - self.a / 2
        y_ctrl = self.y0 + self.b / 2
        if self.a > self.b:
            x = self.b / self.delta_l
        else:
            x = self.a / self.delta_l

        for i in range(ceil(x)):
            if (i % 2 == 0) and (i != 0):
                if self.a > self.b:
                    self.angle -= 90
                    self.points.append([x_ctrl + self.a, y_ctrl - i * self.b / x, self.h, radians(self.angle)])
                    self.angle -= 90
                    self.points.append([x_ctrl, y_ctrl - i * self.b / x, self.h, radians(self.angle)])
                else:
                    self.angle += 90
                    self.points.append([x_ctrl + i * self.a / x, y_ctrl - self.b, self.h, radians(self.angle)])
                    self.angle += 90
                    self.points.append([x_ctrl + i * self.a / x, y_ctrl, self.h, radians(self.angle)])
            elif i == 0:
                self.points.append([x_ctrl, y_ctrl, self.h, radians(0.0)])
                self.points.append([x_ctrl + self.a, y_ctrl, self.h, radians(self.angle)])
                self.angle -= 90
                self.points.append([x_ctrl + self.a, y_ctrl - self.b, self.h, radians(self.angle)])
                self.angle -= 90
                self.points.append([x_ctrl, y_ctrl - self.b, self.h, radians(self.angle)])
                self.angle -= 90
                self.points.append([x_ctrl, y_ctrl, self.h, radians(self.angle)])
            else:
                if self.a > self.b:
                    self.angle += 90
                    if i == 1:
                        self.angle += 90
                    self.points.append([x_ctrl, y_ctrl - i * self.b / x, self.h, radians(self.angle)])
                    self.angle += 90
                    self.points.append([x_ctrl + self.a, y_ctrl - i * self.b / x, self.h, radians(self.angle)])
                else:
                    self.angle -= 90
                    self.points.append([x_ctrl + i * self.a / x, y_ctrl, self.h, radians(self.angle)])
                    self.angle -= 90
                    self.points.append([x_ctrl + i * self.a / x, y_ctrl - self.b, self.h, radians(self.angle)])
        self.points.append([0.0, 0.0, self.h, 0.0])

    def circle_snake(self):
        self.circle()
        x = self.points[0][0]
        m_res = list()
        check = 0
        while check < round(2 * self.radius / self.delta_l):
            x -= self.delta_l
            alfa = acos((x - self.x0) / self.radius)
            y1 = self.y0 + self.radius * sin(alfa)
            y2 = self.y0 + self.radius * sin(2 * pi - alfa)
            check += 1
            if check % 2 == 0:
                m_res.append([x, y1, self.h, 0.0])
                m_res.append([x, y2, self.h, 0.0])
            else:
                m_res.append([x, y2, self.h, 0.0])
                m_res.append([x, y1, self.h, 0.0])
        m_res.append([0, 0, self.h, 0.0])
        self.points += m_res

    def circle(self):
        for i in range(self.count_point + 1):
            self.calculate(i)

    def helix(self):
        self.helix_rev()
        self.points.reverse()
        self.points.append(self.points[0])
        self.points.pop(0)

    def helix_rev(self):
        self.circle()
        for i in range(self.count_branch):
            for j in range(self.count_point + 1):
                if self.radius < 0:
                    self.points.append([0.0, 0.0, self.h, 0.0])
                    return
                self.calculate(j)
                self.radius -= self.delta_R
