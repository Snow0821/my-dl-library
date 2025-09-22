and_dataset = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
]

or_dataset = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
]

def mseloss(y, y_pred):
    return (y - y_pred) ** 2

class my_and_gate:
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.b = 0.5
        return
    
    def forward(self, x1, x2):
        return self.w1 * x1 + self.w2 * x2 + self.b
    
    def backward(self, x1, x2, y, y_pred, lr = 0.01):
        delta = y - y_pred
        self.w1 = self.w1 + 2 * lr * x1 * delta
        self.w2 = self.w2 + 2 * lr * x2 * delta
        self.b = self.b + 2 * lr * delta
        return
    
myand = my_and_gate()

lr = 0.001
epochs = 1000

for _ in range(epochs):
    loss = 0
    for x1, x2, y in and_dataset:
        y_pred = myand.forward(x1, x2)
        print(y, y_pred)
        myand.backward(x1, x2, y, y_pred, lr)
        loss += mseloss(y, y_pred)
    print("loss:", loss / 4)
