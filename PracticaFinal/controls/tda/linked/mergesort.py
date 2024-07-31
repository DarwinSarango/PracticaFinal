class MergeSort:
    
    def mergeSort_number_ascent(self, array):
        if len(array) ==1:
            return array
        
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]
        
        izquierda = self.mergeSort_number_ascent(izquierda)
        derecha = self.mergeSort_number_ascent(derecha)
        
        return self.merge_number_ascent(izquierda, derecha)
    
    def merge_number_ascent(self, izquierda, derecha):
        array = []
        while len(izquierda) > 0 and len(derecha) > 0:
            if izquierda[0] < derecha[0]:
                array.append(derecha[0])
                derecha.pop(0)
            else:
                array.append(izquierda[0])
                izquierda.pop(0)
            
        while len(izquierda) > 0:
            array.append(izquierda[0])
            izquierda.pop(0)
        
        while len(derecha) > 0:
            array.append(derecha[0])
            derecha.pop(0)
            
        return array
    
    def mergeSort_number_descent(self, array):
        if len(array) ==1:
            return array
        
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]
        
        izquierda = self.mergeSort_number_descent(izquierda)
        derecha = self.mergeSort_number_descent(derecha)
        
        return self.merge_number_descent(izquierda, derecha)
    
    def merge_number_descent(self, izquierda, derecha):
        array = []
        while len(izquierda) > 0 and len(derecha) > 0:
            if izquierda[0] >  derecha[0]:
                array.append(derecha[0])
                derecha.pop(0)
            else:
                array.append(izquierda[0])
                izquierda.pop(0)
            
        while len(izquierda) > 0:
            array.append(izquierda[0])
            izquierda.pop(0)
        
        while len(derecha) > 0:
            array.append(derecha[0])
            derecha.pop(0)
            
        return array
    
    
    def mergeSort_models_ascent(self, array, atribute):
        if len(array) ==1:
            return array
        
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]
        
        izquierda = self.mergeSort_models_ascent(izquierda, atribute)
        derecha = self.mergeSort_models_ascent(derecha, atribute)
        
        return self.merge_models_ascent(izquierda, derecha, atribute)
    
    
    
    def merge_models_ascent(self, izquierda, derecha, atribute):
        array = []
        while len(izquierda) > 0 and len(derecha) > 0:
            if getattr(izquierda[0], atribute) > getattr(derecha[0], atribute):
                array.append(derecha[0])
                derecha.pop(0)
            else:
                array.append(izquierda[0])
                izquierda.pop(0)
            
        while len(izquierda) > 0:
            array.append(izquierda[0])
            izquierda.pop(0)
        
        while len(derecha) > 0:
            array.append(derecha[0])
            derecha.pop(0)
            
        return array
    
    
    
    def mergeSort_models_descent(self, array, atribute):
        if len(array) ==1:
            return array
        
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]
        
        izquierda = self.mergeSort_models_descent(izquierda, atribute)
        derecha = self.mergeSort_models_descent(derecha, atribute)
        
        return self.merge_models_descent(izquierda, derecha, atribute)
    
    
    
    def merge_models_descent(self, izquierda, derecha, atribute):
        array = []
        while len(izquierda) > 0 and len(derecha) > 0:
            if getattr(izquierda[0], atribute) < getattr(derecha[0], atribute):
                array.append(derecha[0])
                derecha.pop(0)
            else:
                array.append(izquierda[0])
                izquierda.pop(0)
            
        while len(izquierda) > 0:
            array.append(izquierda[0])
            izquierda.pop(0)
        
        while len(derecha) > 0:
            array.append(derecha[0])
            derecha.pop(0)
            
        return array
    
    
    