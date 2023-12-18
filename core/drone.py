from enum import Enum
from threading import Thread
import numpy as np
from udacidrone import Drone
from udacidrone.messaging import MsgID
from core.thread_handler import ui_handler
import visdom
from time import time

START = 0.0
END = 0.0


class States(Enum):
    MANUAL = 0
    ARMING = 1
    TAKEOFF = 2
    WAYPOINT = 3
    LANDING = 4
    DISARMING = 5


class BackyardFlyer(Drone):

    def __init__(self, connection, ui_hndlr: ui_handler):
        super().__init__(connection)
        self.v = visdom.Visdom()
        self.ui_handler = ui_hndlr
        self.count_point: int = None
        assert self.v.check_connection()

        ne = np.array([self.local_position[0], self.local_position[1]]).reshape(1, -1)
        self.ne_plot = self.v.scatter(ne, opts=dict(
            title="Траектория движения БПЛА",
            xlabel='X',
            ylabel='Y'
        ))
        self.target_position = np.array([0.0, 0.0, 0.0, 0.0])
        self.all_waypoints = []
        self.in_mission = True
        self.check_state = {}

        self.flight_state = States.MANUAL

        self.register_callback(MsgID.LOCAL_POSITION, self.local_position_callback)
        self.register_callback(MsgID.LOCAL_VELOCITY, self.velocity_callback)
        self.register_callback(MsgID.STATE, self.state_callback)
        self.sub_thread = Thread(target=self.update_plot, daemon=False)
        self.sub_thread.start()

    def update_plot(self):
        while self.flight_state != States.DISARMING:
            ne = np.array([self.local_position[1], self.local_position[0]]).reshape(1, -1)
            self.v.scatter(ne, win=self.ne_plot, update='append')

    def local_position_callback(self):
        if self.flight_state == States.TAKEOFF:
            if -1.0 * self.local_position[2] > 0.99 * self.target_position[2]:
                self.waypoint_transition()
        elif self.flight_state == States.WAYPOINT:
            if np.linalg.norm(self.target_position[0:2] - self.local_position[0:2]) < 1.0:
                if len(self.all_waypoints) > 0:
                    self.waypoint_transition()
                else:
                    if np.linalg.norm(self.local_velocity[0:2]) < 1.0:
                        self.landing_transition()

    def velocity_callback(self):
        if self.flight_state == States.LANDING:
            if self.global_position[2] - self.global_home[2] < 0.1:
                if abs(self.local_position[2]) < 0.01:
                    self.disarming_transition()

    def state_callback(self):
        if self.in_mission:
            if self.flight_state == States.MANUAL:
                self.arming_transition()
            elif self.flight_state == States.ARMING:
                if self.armed:
                    self.takeoff_transition()
            elif self.flight_state == States.DISARMING:
                if ~self.armed & ~self.guided:
                    self.manual_transition()

    def arming_transition(self):
        self.ui_handler.table_signal.emit('Переход на ручной режим')
        self.take_control()
        self.arm()
        self.set_home_position(self.global_position[0], self.global_position[1], self.global_position[2])

        self.flight_state = States.ARMING

    def takeoff_transition(self):
        global START
        START = time()
        self.ui_handler.table_signal.emit('Взлет')
        target_altitude = 12.75
        self.target_position[2] = target_altitude
        self.takeoff(target_altitude)
        self.flight_state = States.TAKEOFF

    def waypoint_transition(self):

        self.target_position = self.all_waypoints.pop(0)
        pg_val = int((self.count_point - len(self.all_waypoints)) / self.count_point * 100)
        self.ui_handler.progress_signal.emit(pg_val)
        self.cmd_position(*self.target_position)
        self.flight_state = States.WAYPOINT

    def landing_transition(self):
        global END
        END = time()
        self.ui_handler.table_signal.emit('Приземление')

        self.land()
        self.flight_state = States.LANDING

    def disarming_transition(self):
        self.ui_handler.table_signal.emit('Переход в автоматический режим')
        self.disarm()
        self.release_control()
        self.flight_state = States.DISARMING

    def manual_transition(self):
        self.ui_handler.table_signal.emit('Остановка двигателей')
        self.ui_handler.table_signal.emit(f'Время: {round(END - START, 1)} с')
        self.stop()
        self.in_mission = False
        self.flight_state = States.MANUAL

    def start(self):
        self.count_point = len(self.all_waypoints)
        super().start()



