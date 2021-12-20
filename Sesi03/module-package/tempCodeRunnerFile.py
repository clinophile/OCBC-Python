import car
import importlib
car.brands = ['honda', 'toyota']
importlib.reload(car)
print (car)