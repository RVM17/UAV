from ui_files.ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from datetime import datetime
from core.xml_core import parameters

GLOBAL_STATE = 0


def current_time() -> str:
    return datetime.strftime(datetime.now(), '%H:%M')


class MainWindow(QMainWindow):
    m_line_edit = ['line_x0', 'line_y0', 'line_z', 'line_radius', 'line_points', 'line_rect_a', 'line_rect_b']

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.ui.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.ui.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.ui.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.ui.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.ui.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.ui.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.ui.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)

        def move_window(event):
            if returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = move_window
        UIFunctions.uiDefinitions(self)
        self.show()

    def update_bar(self, value: int):
        self.ui.progressBar.setValue(value)

    def update_table(self, value: str):
        self.ui.table_log.scrollToBottom()
        self.ui.table_log.insertRow(self.ui.table_log.rowCount())
        cur_index = self.ui.table_log.rowCount() - 1
        self.ui.table_log.setItem(cur_index, 0, QTableWidgetItem(current_time(), 0))
        self.ui.table_log.setItem(cur_index, 1, QTableWidgetItem(value, 0))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def set_params(self) -> str:
        """Функция устанавливает параметры из файла bin/parameters.xml.
            Вывод:
                Полный путь файла со статусом (str)
            """
        xml_parameters = parameters('bin/parameters.xml')
        values = xml_parameters.get()
        if values is not None:
            for i, value in enumerate(values):
                line_edit: QLineEdit = getattr(self.ui, self.m_line_edit[i])
                line_edit.setText(value)

    def get_params(self):
        """Функция сохраняет параметры в файл bin/parameters.txt.

            Ввод:
                Полный путь файла-статуса: str;
        """
        xml_parameters = parameters('bin/parameters.xml')
        m_data = list()
        for name in self.m_line_edit:
            line_edit: QLineEdit = getattr(self.ui, name)
            m_data.append(line_edit.text())
        xml_parameters.set(m_data)


def returnStatus():
    return GLOBAL_STATE


class UIFunctions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("#drop_shadow_frame{"
                                                    "background-color: rgb(38, 36, 36);"
                                                    "border-radius: 0px;}")
            self.ui.btn_maximaze.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("#drop_shadow_frame{"
                                                    "background-color: rgb(38, 36, 36);"
                                                    "border-radius: 10px;}")
            self.ui.btn_maximaze.setToolTip("Maximize")

    def uiDefinitions(self):
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
        self.ui.btn_maximaze.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
