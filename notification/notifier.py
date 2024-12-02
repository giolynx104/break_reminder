from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class ConsoleNotifier(Notifier):
    def notify(self, message: str):
        print("\n" + "="*50)
        print(message)
        print("="*50 + "\n") 