from abc import ABC, abstractmethod
import threading
import time

class Timer(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class WorkTimer(Timer):
    def __init__(self, interval_minutes: int, callback):
        self.interval = interval_minutes * 60  # Convert to seconds
        self.callback = callback
        self.is_running = False
        self.thread = None
        self.stop_event = threading.Event()

    def start(self):
        self.is_running = True
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.is_running = False
        self.stop_event.set()
        if self.thread:
            self.thread.join(timeout=1)  # Wait for at most 1 second

    def _run(self):
        while self.is_running:
            # Wait for the interval or until stop_event is set
            if self.stop_event.wait(timeout=self.interval):
                break
            if self.is_running:
                self.callback() 