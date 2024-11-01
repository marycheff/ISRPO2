import math

def y(x):
    return x**2 - math.exp(x)  


X0 = float(input("X0: "))
h = float(input("h: "))
X = X0
Y = 0

points = []
while True:
    Y = y(X)
    
    if -10.001 <= Y <= -9.999:
        points.append((X, Y))  
        
    if Y < -11:
        break
    X += h 


if points:
    print("Найденные точки в диапазоне от -10.001 до - 9.999:")
    for point in points:
        print(f"X: {point[0]:.5f}, Y: {point[1]:.5f}")
else:
    print("Точки в диапазоне от -10.001 до - 9.999 не найдены.")

