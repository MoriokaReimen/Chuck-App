# -*- coding: utf-8 -*-
import sys
from app.StartStopUI import StartStopUI
from app.ConsoleUI import ConsoleUI
from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QApplication,
    QMainWindow,
)
from qt_material import apply_stylesheet
from core import Core

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._core = Core.Core()

        # Confiture Window
        self.setWindowTitle("Chuck Norris")

        # Configure layout
        pagelayout = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(pagelayout)

        # Configure Console UI
        self.console_ui = ConsoleUI(self._core)
        pagelayout.addWidget(self.console_ui, 0, 0)

        # Configure StartStop UI
        self.start_stop_ui = StartStopUI(self._core)
        pagelayout.addWidget(self.start_stop_ui, 1, 0)

        # tie whole widgets to Window
        self.setCentralWidget(self.widget)

    def __del__(self):
        self._core.stop()

def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme = 'dark_cyan.xml')
    window.show()
    app.exec()

if __name__ == '__main__':
    # Execute main function
    main()
