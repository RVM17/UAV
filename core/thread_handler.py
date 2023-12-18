from ui_files.mainwindow import MainWindow
from PyQt5.QtCore import QObject, pyqtSignal


class ui_handler(QObject):
    progress_signal = pyqtSignal(int)
    table_signal = pyqtSignal(str)

    def __init__(self, main_win: MainWindow):
        super().__init__()
        self.progress_signal.connect(main_win.update_bar)
        self.table_signal.connect(main_win.update_table)

