# -*- coding: utf-8 -*-
"""
Implementation of Observer pattern in Python
Ref: https://medium.com/@amirm.lavasani/design-patterns-in-python-observer-ac50bbf861b5
"""
import PyQt6.sip as sip

# The Subject
class Subject:
    def __init__(self) -> None:
        self._observers = set()

    def attach(self, observer) -> None:
        """Adds an observer to the subject's list."""
        self._observers.add(observer)

    def detach(self, observer) -> None:
        """Removes an observer from the subject's list."""
        self._observers.remove(observer)

    def notify_observers(self, message : str) -> None:
        """Notifies all attached observers."""
        for observer in self._observers:
            if not sip.isdeleted(observer):
                observer.update(message)

# Step 2: The Observer Interface
class Observer:
    def update(self, message : str) -> None:
        """Abstract method for receiving updates."""
        pass
