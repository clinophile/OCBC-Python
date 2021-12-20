import person
print(person.name)
print(person.devices)
print(person.devices[1])
person.display('Good Morning!!')

print("====================")

# import sys
# sys.path.append(r'd:/Data/Python Project/Sesi03/module-package/model')
# print(sys.path)


print("====================")


from person import name as p_name, devices as p_devices
name = 'alex'
devices= ['tv', 'ac', 'speaker']
print('name = ',name)
print('p_name = ', p_name)
print('devices = ', devices)
print('p_devices = ', p_devices)

print("===========================================")

from person import name, devices
print(dir(name))

print("============================================")
import car
import importlib
importlib.reload(car)


print("============================================")
import pkg.mod1
from pkg import mod2
from person import display

display(pkg.mod1.kitchen_sets)
display(mod2.artist_kits)