class ConversionNotPossible(Exception):
    pass


def convert(fromUnit,toUnit,value):
    
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    
    if(str(value).isalpha()==True):
        raise ConversionNotPossible("Not a number!")
        
    value = float(value)
    
    if fromUnit == toUnit:
        return value

    #Celsius
    elif fromUnit == 'celsius' and toUnit == 'fahrenheit':
        far = (value*(9/5)) + 32
        return far
    
    elif fromUnit == 'celsius' and toUnit =='kelvin':
        kel = value + 273.15
        return kel
    
    #Fahreneheit
    elif fromUnit == 'fahrenheit' and toUnit == 'celsius':
        cel = (value-32) * (5/9)
        return cel
    
    elif fromUnit == 'fahrenheit' and toUnit == 'kelvin':
        kel = (value+459.67) * (5/9)
        return kel
    
    #Kelvin
    elif fromUnit == 'kelvin' and toUnit == 'celsius':
        cel = value - 273.15
        return cel
    
    elif fromUnit == 'kelvin' and toUnit == 'fahrenheit':
        far = (value*(9/5))-459.67
        return far
    
    #Miles
    elif fromUnit == 'miles' and toUnit == 'meters':
        me = value * 1609.344
        return me
    
    elif fromUnit == 'miles' and toUnit == 'yards':
        ya = value * 1760 
        return ya
    
    #Meters
    elif fromUnit == 'meters' and toUnit == 'miles':
        mi = value/1609.344
        return mi
    
    elif fromUnit == 'meters' and toUnit == 'yards':
        ya = value * 1.0936132983
        return round(ya)
        
    #Yards
    elif fromUnit == 'yards' and toUnit == 'miles':
        mi = value/1760
        return mi
    
    elif fromUnit == 'yards' and toUnit == 'meters':
        me = value * 0.9144
        return me
    
    else:
        raise ConversionNotPossible("The unit types do not match!")

    
    
    
