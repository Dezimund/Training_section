class StudentLimitError(Exception):
    def __init__(self, message="Досягнуто максимальну кількість студентів у групі (10)"):
        self.message = message
        super().__init__(self.message)
