class ReadOnlyError(Exception):
    def __init__(self, filename):
        self.message = f"{filename} is read-only"
        super().__init__(self.message)

class ActionsTableValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)