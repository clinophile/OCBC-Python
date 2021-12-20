from packages import KC_module as kc
'''Module ini berisi 1 function yang digunakan untuk convert suhu ke fahrenheit atau dari fahrenheit.'''

'''function toFahrenheit() digunakan untuk mengubah suhu Kelvin dan Celcius ke Fahrenheit.
Terdapat 2 parameter, yaitu kelvin dan celcius :
parameter kelvin untuk menerima value suhu dengan satuan Kelvin.
parameter celcius untuk menerima value suhu dengan satuan Celcius.'''
def toFahrenheit(kelvin, celcius) :
    '''dari kelvin ke fahrenheit'''
    temp = kc.convertSuhuTo(kelvin, 'C') #convert dari kelvin ke celcius
    kelv = (( 9 / 5 ) * temp) + 32

    '''dari celcius ke fahrenheit'''
    celc = (( 9 / 5 ) * celcius) + 32

    print("\nFrom Kelvin to Fahrenheit : ")
    print('Result: ', '{:.3f}'.format(kelv), 'Fahrenheit')
    
    print("From Celcius to Fahrenheit : ")
    print('Result: ', '{:.3f}'.format(celc), 'Fahrenheit')


'''function fromFahrenheit() digunakan untuk mengubah suhu Fahrenheit ke Kelvin dan Celcius.
Terdapat 2 parameter, yaitu suhu.
parameter kelvin untuk menerima value suhu dengan satuan Kelvin.
parameter celcius untuk menerima value suhu dengan satuan Celcius.'''
def fromFahrenheit(suhu) :
    celc = (suhu - 32) * 5 / 9
    kelv = kc.convertSuhuTo(celc, 'K')

    print("\nFrom Fahrenheit to Kelvin : ")
    print('Result: ', '{:.3f}°'.format(kelv), 'Kelvin')
    print("From Fahrenheit to Celcius : ")
    print('Result: ', '{:.3f}°'.format(celc), 'Celcius')
