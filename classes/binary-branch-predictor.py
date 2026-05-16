

class TwoBitPredictor:
    def __init__(self):
        self.state = 1

    def predict(self):
        return self.state >= 2

    def update(self, actual_outcome):
        if actual_outcome:
            if self.state < 3:
                self.state += 1

