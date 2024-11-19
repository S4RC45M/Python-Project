class Question:
    def __init__(self, object, answer):
        self.object = object
        self.answer = answer

Q1 = Question("tomato",6)

print(f"{Q1.object}")
