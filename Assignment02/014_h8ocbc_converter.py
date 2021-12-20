from packages import KC_module as kc
from packages import fahrenheit_module as fahren

'''Aplikasi konversi suhu Celcius, Kelvin, Fahrenheit'''
'''
Fitur:
    1. Convert from Celcius to Kelvin
    2. Convert from Kelvin to Celcius
    3. Convert from Kelvin and Celcius to Fahrenheit
    4. Convert from Fahrenheit to Kelvin and Celcius 
    5. Perulangan dalam memilih menu
'''

print("==============ASSIGNMENT 2==============")


ulang = True

while (ulang == True) :
    print("Menu :")
    print("1. Convert from Celcius to Kelvin")
    print("2. Convert from Kelvin to Celcius")
    print("3. Convert from Kelvin and Celcius to Fahrenheit")
    print("4. Convert from Fahrenheit to Kelvin and Celcius")
    menu = int(input("Silahkan masukan nomor menu (1 s/d 4) : "))

    print('')
    if (menu == 1) :
        print("1. Convert from Celcius to Kelvin")
        celc = float(input('Masukan suhu (Celcius): '))
        result = kc.convertSuhuTo(celc, 'K')
        print(f'Result: {result}° Celcius')
    elif (menu == 2) :
        print("2. Convert from Kelvin to Celcius")
        kelv = float(input('Masukan suhu (Kelvin): '))
        result = kc.convertSuhuTo(kelv, 'C')
        print(f'Result: {result}° Kelvin')
    elif (menu == 3) :
        print("3. Convert from Kelvin and Celcius to Fahrenheit")
        kelv = float(input('Masukan suhu (Kelvin): '))
        celc = float(input('Masukan suhu (Celcius): '))
        fahren.toFahrenheit(kelv, celc)
    elif (menu == 4) :
        print("4. Convert from Fahrenheit to Kelvin and Celcius")
        suhu = float(input('Masukan suhu (Fahrenheit): '))
        fahren.fromFahrenheit(suhu)
    else:
        print('Choose right menu!')
    
    if(input('\nBack to Menu [y/n]? ') == 'y'):
        ulang=True
    else:
        ulang=False
        print("TERIMA KASIH!")
