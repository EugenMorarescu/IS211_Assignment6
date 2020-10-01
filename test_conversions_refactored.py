import unittest
import conversion_refactored


class KnownValues(unittest.TestCase):
    
    #Celsius,Fahrenheit,Kelvin
    known_values_temp = [
        [500.00,932.00,773.15],
        [440.00,824.00,713.15],
        [140.00,284.00,413.15],
        [0.00,32.00,273.15],
        [-273.15,-459.67,0.00]
              
        ]
    
    #Miles, Yards, Meters
    known_values_dist = [
        [1.00,1760.00,1609.344],
        [8.00,14080.00,12874.752],
        [10.00,17600.00,16093.44],
        [13.00,22880.00,20921.472],
        [25.00,44000.00,40233.6]
        
        ]
    
    temps=['Celsius','Fahrenheit','Kelvin']
    temps2=['Celsius','Fahrenheit','Kelvin']
    
    dist=['Miles','Yards','Meters']
    dist2=['Miles','Yards','Meters']
    
    
    
    def test_to_all(self):
       
       for t in self.temps:
            
            if(t == 'Celsius'):
                count=0
                while count<=2:
                    for t2 in self.temps2:
                             for i in self.known_values_temp:
         
                                 result = conversion_refactored.convert(t,t2,i[0])
                                 self.assertAlmostEqual(i[count], result)
                                 print('The temperature {0} in {1} is {2} in {3}'.format(i[0],t,result,t2)) 
                         
                             count+=1
                         
            if(t == 'Fahrenheit'):
                count=0
                while count<=2:
                    for t2 in self.temps2:
                        for i in self.known_values_temp:
     
                             result = conversion_refactored.convert(t,t2,i[1])
                             self.assertAlmostEqual(i[count], result)
                             print('The temperature {0} in {1} is {2} in {3}'.format(i[1],t,result,t2)) 
                     
                        count+=1
                        
            if(t == 'Kelvin'):
                count=0
                while count<=2:
                    for t2 in self.temps2:
                        for i in self.known_values_temp:
     
                             result = conversion_refactored.convert(t,t2,i[2])
                             self.assertAlmostEqual(i[count], result)
                             print('The temperature {0} in {1} is {2} in {3}'.format(i[2],t,result,t2)) 
                     
                        count+=1
                
       for d in self.dist:
           
            if(d == 'Miles'):
                count=0
                while count<=2:
                    for d2 in self.dist2:
                        for i in self.known_values_dist:
    
                            result = conversion_refactored.convert(d,d2,i[0])
                            self.assertAlmostEqual(i[count], result)
                            print('The distance {0} in {1} is {2} in {3}'.format(i[0],d,result,d2)) 
                         
                        count+=1
                        
            if(d == 'Yards'):
                count=0
                while count<=2:
                    for d2 in self.dist2:
                        for i in self.known_values_dist:
    
                            result = conversion_refactored.convert(d,d2,i[1])
                            self.assertAlmostEqual(i[count], result)
                            print('The distance {0} in {1} is {2} in {3}'.format(i[1],d,result,d2)) 
                         
                        count+=1
                        
            if(d == 'Meters'):
                count=0
                while count<=2:
                    for d2 in self.dist2:
                        for i in self.known_values_dist:
    
                            result = conversion_refactored.convert(d,d2,i[2])
                            self.assertAlmostEqual(i[count], result)
                            print('The distance {0} in {1} is {2} in {3}'.format(i[2],d,result,d2)) 
                         
                        count+=1
                        
       self.assertRaises(conversion_refactored.ConversionNotPossible, conversion_refactored.convert, '','Celsius',400)
       self.assertRaises(conversion_refactored.ConversionNotPossible, conversion_refactored.convert, 'Kelvin','Celsius','A')

if __name__ == '__main__':
    unittest.main()
            
        
                
            
        
        
        