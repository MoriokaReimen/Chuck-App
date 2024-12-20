# -*- coding: utf-8 -*-
from core.Observer import Observer
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QGroupBox,
    QTableWidget,
    QVBoxLayout,
    QWidget,
    QTableWidgetItem
)
from PyQt6.QtCore import Qt
from typing import override
from core import Core

class TableUI(QWidget, Observer):

    def __init__(self, core : Core) -> None:
        super().__init__()

        self._core = core

        # Group Box
        groupbox = QGroupBox("Table")

        # Configure group layout
        grouplayout = QVBoxLayout()
        buttonlayout = QHBoxLayout()
        groupbox.setLayout(grouplayout)

        # Configure widget layout
        widgetlayout = QVBoxLayout()
        widgetlayout.addWidget(groupbox)
        self.setLayout(widgetlayout)

        # update button
        self.bt_update = QPushButton()
        self.bt_update.setText('Update')
        self.bt_update.pressed.connect(self.update_table)
        buttonlayout.addWidget(self.bt_update)

        # Table
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Time Sent'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Title'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Contents'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Sender'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Receiver'))
        self.table.horizontalHeader().setStretchLastSection(True)
        grouplayout.addWidget(self.table)

        # add buttons bottom of console
        grouplayout.addLayout(buttonlayout)

        # Attach to subject
        self._core.attach(self)

    def update_table(self) -> None:
        self.table.setRowCount(0)
        entries = self._core.database.get_all()
        for index, entry in enumerate(entries):
            self.table.insertRow(self.table.rowCount())

            # time_sent
            item = QTableWidgetItem(entry.time_sent.isoformat())
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(self.table.rowCount()-1, 0, item)

            # Title
            item = QTableWidgetItem(entry.title[0:20])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(self.table.rowCount()-1, 1, item)

            # Contents
            item = QTableWidgetItem(entry.contents[0:20])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(self.table.rowCount()-1, 2, item)

            # Sender
            item = QTableWidgetItem(entry.sender[0:20])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(self.table.rowCount()-1, 3, item)

            # Receiver
            item = QTableWidgetItem(entry.receiver[0:20])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(self.table.rowCount()-1, 4, item)

            item = QTableWidgetItem(str(index))
            self.table.setVerticalHeaderItem(self.table.rowCount()-1, item)

    @override
    def update(self, message : str) -> None:
        pass
