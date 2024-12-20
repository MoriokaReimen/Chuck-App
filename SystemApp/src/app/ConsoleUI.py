# -*- coding: utf-8 -*-
from core.Observer import Observer
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QGroupBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import pyqtSignal
import easygui
from typing import override
from core import Core

class ConsoleUI(QWidget, Observer):
    signal_append_console = pyqtSignal(str)

    def __init__(self, core : Core) -> None:
        super().__init__()

        self._core = core

        # Group Box
        groupbox = QGroupBox("Console")

        # Configure group layout
        grouplayout = QVBoxLayout()
        buttonlayout = QHBoxLayout()
        groupbox.setLayout(grouplayout)

        # Configure widget layout
        widgetlayout = QVBoxLayout()
        widgetlayout.addWidget(groupbox)
        self.setLayout(widgetlayout)

        # clear button
        self.bt_clear = QPushButton()
        self.bt_clear.setText('Clear')
        self.bt_clear.pressed.connect(self.clear)
        buttonlayout.addWidget(self.bt_clear)

        # save button
        self.bt_save = QPushButton()
        self.bt_save.setText('Save')
        self.bt_save.pressed.connect(self.save)
        buttonlayout.addWidget(self.bt_save)

        # Console for dispaly data
        self.te_console = QTextEdit()
        self.te_console.setReadOnly(True)
        grouplayout.addWidget(self.te_console)

        # add buttons bottom of console
        grouplayout.addLayout(buttonlayout)

        # Attach to subject
        self._core.attach(self)
        self.signal_append_console.connect(self.te_console.append)

    def save(self) -> None:
        file_name = easygui.filesavebox("", "Save file as *.txt", "*.txt")
        if file_name :
            with open(file_name, mode="w") as file:
                file.write(self.te_console.toPlainText())

    def clear(self) -> None:
        self.te_console.clear()

    @override
    def update(self, message : str) -> None:
        if "Heart Beat : " not in message:
            self.signal_append_console.emit(message)
