from timer.timer import WorkTimer
from notification.notifier import ConsoleNotifier
from suggestions.suggestion_provider import SuggestionProvider
import time

class BreakReminder:
    def __init__(self, interval_minutes: int):
        self.suggestion_provider = SuggestionProvider()
        self.notifier = ConsoleNotifier()
        self.timer = WorkTimer(interval_minutes, self._break_time)

    def _break_time(self):
        suggestion = self.suggestion_provider.get_random_suggestion()
        self.notifier.notify(f"Đã đến giờ nghỉ giải lao!\n\nGợi ý: {suggestion}")

    def start(self):
        print(f"Chương trình nhắc nhở nghỉ giải lao đã được khởi động...")
        self.timer.start()

    def stop(self):
        self.timer.stop()

if __name__ == "__main__":
    reminder = BreakReminder(interval_minutes=30)  # Nhắc nhở mỗi 30 phút
    try:
        print("Chương trình đang chạy. Nhấn Ctrl+C để dừng...\n")
        reminder.start()
        while True:
            time.sleep(1)  # Sleep for 1 second instead of busy waiting
    except KeyboardInterrupt:
        print("\nĐang dừng chương trình...")
        reminder.stop()
        print("Chương trình đã dừng.")