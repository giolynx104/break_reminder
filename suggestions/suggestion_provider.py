import random

class SuggestionProvider:
    def __init__(self):
        self.suggestions = [
            "Uống một ly nước!",
            "Đứng dậy và đi bộ 5 phút",
            "Thực hiện các bài tập giãn cơ cổ",
            "Nhắm mắt thư giãn 2 phút",
            "Hít thở sâu 10 lần",
            "Nghe một bài nhạc thư giãn",
            "Vươn vai và duỗi người"
        ]

    def get_random_suggestion(self) -> str:
        return random.choice(self.suggestions) 