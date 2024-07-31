class ShellSort:
    
    
    def shell_number_ascent(self, array):
        mitad = len(array) // 2
        
        while mitad > 0:
            for i in range(len(array)):
                for j in range(i + mitad, len(array), mitad):
                    valor = array[j]
                    posicion = j
                    
                    while posicion >= mitad and array[posicion - mitad] > valor:
                        array[posicion] = array[posicion - mitad]
                        posicion = posicion - mitad
                    
                    array[posicion] = valor
                    
            mitad = mitad // 2
            
        return array
    
    
    def shell_number_descent(self, array):
        mitad = len(array) // 2
        
        while mitad > 0:
            for i in range(len(array)):
                for j in range(i + mitad, len(array), mitad):
                    valor = array[j]
                    posicion = j
                    
                    while posicion >= mitad and array[posicion - mitad] < valor:
                        array[posicion] = array[posicion - mitad]
                        posicion = posicion - mitad
                    
                    array[posicion] = valor
                    
            mitad = mitad // 2
            
        return array
    
    
    
    def shell_models_ascent(self, array ,atribute):
        mitad = len(array) // 2
        
        while mitad > 0:
            for i in range(len(array)):
                for j in range(i + mitad, len(array), mitad):
                    valor = array[j]
                    posicion = j
                    
                    while posicion >= mitad and getattr(array[posicion - mitad], atribute) > getattr(valor, atribute):
                        array[posicion] = array[posicion - mitad]
                        posicion = posicion - mitad
                    
                    array[posicion] = valor
                    
            mitad = mitad // 2
            
        return array
    
    
    def shell_models_descent(self, array ,atribute):
        mitad = len(array) // 2
        
        while mitad > 0:
            for i in range(len(array)):
                for j in range(i + mitad, len(array), mitad):
                    valor = array[j]
                    posicion = j
                    
                    while posicion >= mitad and getattr(array[posicion - mitad], atribute) < getattr(valor, atribute):
                        array[posicion] = array[posicion - mitad]
                        posicion = posicion - mitad
                    
                    array[posicion] = valor
                    
            mitad = mitad // 2
            
        return array
    
    
                