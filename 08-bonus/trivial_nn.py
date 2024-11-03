import random

train = [(0,0),
         (1,2),
         (2,4),
         (3,6),
         (4,8)
        ]

def error(a, b):
    return (a - b)**2

def cost(w):
    c = 0
    for x,y in train:
        pred = x * w
        c += error(y, pred)
    return c / len(train)


if __name__ == "__main__":
    # want to learn: y = x * w
    epochs = 500
    epsilon = 0.001
    lr = 0.001

    w = random.random() * 10.0

    for e in range(epochs):
        dcost = ( cost(w + epsilon) - cost(w) ) / epsilon
        w -= lr * dcost
        if (e + 1) % 25 == 0:
            print(f'Epoch [{e}], Cost: [{cost(w)}] -> w = {w}')











