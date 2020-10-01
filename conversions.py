def convertCelsiusToKelvin(num):
    
    kel = num + 273.15
    
    return kel

def convertCelsiusToFahrenheit(num):
    
    far = (num*(9/5)) + 32
    
    return far
    
def convertFahrenheitToCelsius(num):
    
    cel = (num-32) * (5/9)
    
    return cel

def convertFahrenheitToKelvin(num):
    
    kel = (num+459.67) * (5/9)
    
    return kel

def convertKelvinToFahrenheit(num):
    
    far = (num*(9/5))-459.67
    
    return far

def convertKelvinToCelsius(num):
    
    cel = num - 273.15
    
    return cel