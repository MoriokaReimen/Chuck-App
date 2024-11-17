# -*- coding: utf-8 -*-
from core.Observer import Subject
from threading import Thread, Event
from datetime import datetime
from time import sleep
from driver.DataBase import DataBase

class Core(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.database = DataBase()
        self._stop_event = Event()
        self._thread = None

    def __del__(self):
        self.stop()

    def start(self):
        # Publish message
        date_s = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.notify_observers(f"{date_s} : Start Task")

        # Start Worker thread
        self._thread = Thread(target = self._task)
        self._stop_event.clear()
        self._thread.start()

    def stop(self):
        # Stop worker thread
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join(1)

    def _task(self) -> None:
        # Cyclic process
        while True:
            sleep(1)
            # Break if stop requrested
            if self._stop_event.is_set():
                break
            # TODO add cyclic task
            self.notify_observers("Heart Beat : ")

        # Exit Task
        date_s = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.notify_observers(f"{date_s} : Stop Task...")

