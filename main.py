import sys
import time
import subprocess
import os
from PyQt5.QtWidgets import QApplication
from ui_files.mainwindow import MainWindow
from PyQt5.QtCore import QUrl, QThread
from QSwitchControl import SwitchControl
from threading import Thread
from functools import partial
from core.drone import BackyardFlyer
from core.sub_func import trajectory
from udacidrone.connection import MavlinkConnection
from core.thread_handler import ui_handler

M_TOGGLE = ['toggle_rect', 'toggle_circle', 'toggle_helix', 'toggle_reverse_helix']
drone_thread = QThread()


def my_exception_hook(*exc_info):
    sys.__excepthook__(*exc_info)
    sys.exit(1)


class launch_thread(QThread):
    def __init__(self, m_point, parent=None):
        super(launch_thread, self).__init__(parent)
        self.m_point = m_point

    def run(self):
        conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=False, PX4=False)
        drone = BackyardFlyer(conn, ui_handler(main_win))
        drone.all_waypoints = self.m_point
        drone.start()


def web_updater():
    while True:
        ui.web.update()
        time.sleep(0.3)


def toggle_worker(toggle_name: str):
    for cur_toggle in M_TOGGLE:
        if cur_toggle != toggle_name:
            tmp_toggle: SwitchControl = getattr(ui, cur_toggle)
            tmp_toggle.start_animation(False)


def start_fly():
    global drone_thread
    if drone_thread.isRunning():
        ui.label_global_err.setText('Поток уже запущен')
    else:
        flag_circle = True
        flag_rect = True
        height = 0.0
        x0 = 0.0
        y0 = 0.0
        ui.label_global_err.setText('')

        try:
            height = float(ui.line_z.text())
            if height < 0:
                flag = False
            x0 = float(ui.line_x0.text())
            y0 = float(ui.line_y0.text())
            flag = True
        except ValueError:
            flag = False

        if flag:
            trajectory_object = trajectory(x0, y0, height)
            if ui.toggle_helix.isChecked() or ui.toggle_reverse_helix.isChecked() or ui.toggle_circle.isChecked():
                try:
                    flag_rect = False
                    radius = float(ui.line_radius.text())
                    num_points = int(ui.line_points.text())
                    trajectory_object.set_circle_params(radius, num_points)
                except ValueError:
                    flag_circle = False
                    ui.label_global_err.setText('Проверьте вводимые значения в поле "окружность"')
                if flag_circle:
                    if ui.toggle_helix.isChecked():
                        trajectory_object.helix()
                    elif ui.toggle_reverse_helix.isChecked():
                        trajectory_object.helix_rev()
                    elif ui.toggle_circle.isChecked():
                        trajectory_object.circle_snake()

            elif ui.toggle_rect.isChecked():
                try:
                    flag_circle = False
                    a = float(ui.line_rect_a.text())
                    b = float(ui.line_rect_b.text())
                    trajectory_object.set_rect_params(a, b, 0)
                    trajectory_object.rect()
                except ValueError:
                    flag_rect = False
                    ui.label_global_err.setText('Проверьте вводимые значения в поле "прямоугольник"')

            if flag_rect or flag_circle:
                # Запуск потока обновления поля вэб
                main_thread = Thread(target=web_updater, daemon=True)
                main_thread.start()
                main_win.get_params()
                # Запуск потока полета дрона

                drone_thread = launch_thread(trajectory_object.points)
                drone_thread.start()
        else:
            ui.label_global_err.setText('Введите корректные данные в общие параметры')


def main():
    ui.label_global_err.setText('')
    if os.path.exists('bin/parameters.xml'):
        main_win.set_params()
    for toggle_name in M_TOGGLE:
        toggle: SwitchControl = getattr(ui, toggle_name)
        toggle.stateChanged.connect(partial(toggle_worker, toggle_name=toggle_name))

    ui.btn_start.clicked.connect(start_fly)


sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    ui = main_win.ui
    ui.web.setUrl(QUrl('http://localhost:8097'))
    main()
    sys.exit(app.exec())
