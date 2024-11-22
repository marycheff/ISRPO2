import math

def y(x):
    return x**2 - math.e ** x  

X0 = float(input("X0: "))
h = float(input("h: "))

if h == 0:
    print("Введён неверный шаг")
else:
    if h < 0 and X0<10:
        print("Точки в диапазоне от -10.001 до -9.999 не могут быть найдены, т.к. график убывающий, и в данном случае точек с отрицательным шагом быть не может")
    else:
        X = X0
        points = []
        while True:
            Y = y(X)
            if -10.001 <= Y <= -9.999:
                points.append((X, Y))  
            if Y < -11 and h>0:
                break
            elif Y > -9:
                break
            X += h 
        if points:
            print("Найденные точки в диапазоне от -10.001 до -9.999:")
            for point in points:
                print(f"X: {point[0]:.5f}, Y: {point[1]:.5f}")
        else:
            print("Точки в диапазоне от -10.001 до -9.999 не найдены")


