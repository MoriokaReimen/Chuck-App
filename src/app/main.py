# -*- coding: utf-8 -*-
import sys
from app.StartStopUI import StartStopUI
from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QApplication,
    QMainWindow,
)
from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Confiture Window
        self.setWindowTitle("Chuck Norris")

        # Configure layout
        pagelayout = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(pagelayout)

        # Configure StartStop UI
        self.start_stop_ui = StartStopUI()
        pagelayout.addWidget(self.start_stop_ui, 0, 0)

        # tie whole widgets to Window
        self.setCentralWidget(self.widget)

    def __del__(self):
        pass

def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme = 'dark_cyan.xml')
    window.show()
    app.exec()

if __name__ == '__main__':
    # Execute main function
    main()
