# -*- coding: utf-8 -*-
from app.Pixmap import load
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QGroupBox
)
from app.QLed import QLed
from core import Core
from typing import override
from PyQt6.QtCore import pyqtSignal

class StartStopUI(QWidget):
    signal_indicator = pyqtSignal()

    def __init__(self, core : Core) -> None:
        super().__init__()

        self._core = core

        # Group Box
        groupbox = QGroupBox("Start/Stop")

        # Configure group layout
        grouplayout = QGridLayout()
        grouplayout.rowStretch(1)
        grouplayout.columnStretch(1)
        groupbox.setLayout(grouplayout)

        # Configure widget layout
        widgetlayout = QVBoxLayout()
        widgetlayout.addWidget(groupbox)
        self.setLayout(widgetlayout)

        # indicator
        self.signal_indicator.connect(self.blink_indicator)
        self._led = QLed(onColour = 7)
        self._led.value = True
        grouplayout.addWidget(self._led, 0, 0)

        # relay button
        self.bt_start = QPushButton()
        self.bt_start.setText('Off')
        self.bt_start.setIcon(load('OFF_BUTTON'))
        self.bt_start.pressed.connect(self.on_pressed)
        grouplayout.addWidget(self.bt_start, 0, 1)

        # Attach to subject
        self._core.attach(self)

    def on_pressed(self) -> None:
        if self.bt_start.text() == 'Off' :
            self.bt_start.setText('On')
            self.bt_start.setIcon(load('ON_BUTTON'))
            self._core.start()
        else:
            self.bt_start.setText('Off')
            self.bt_start.setIcon(load('OFF_BUTTON'))
            self._core.stop()

    def blink_indicator(self):
        self._led.toggleValue()

    @override
    def update(self, message : str) -> None:
        if "Heart Beat : " in message:
            self.signal_indicator.emit()
