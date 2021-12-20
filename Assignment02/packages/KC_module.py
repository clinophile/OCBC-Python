'''Module ini berisi 1 function yang digunakan untuk convert kelvin ke celcius atau celcius ke kelvin.'''


def convertSuhuTo(suhu, tipe) :
    if (tipe.upper() == 'K') :
        result = suhu + 273.15
    elif (tipe.upper() == 'C') :
        result = suhu - 273.15
    
    return result

