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
    
myand = my_and_gate()

loss = 0
for x1, x2, y in and_dataset:
    y_pred = myand.forward(x1, x2)
    loss += mseloss(y, y_pred)
print(loss / len(and_dataset))


