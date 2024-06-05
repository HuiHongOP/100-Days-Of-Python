def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)


add(1, 2, 3, 4, 5, 6, 7, 8)


def calculate(n, **kwargs):
    for key, value, in kwargs.items():
        print(n, key, value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs.get('model')

my_car = Car(make="BMW")
print(my_car.model)
