class Insercion:
    
    def sort_primitive_ascent(self, array):
        
        for i in range(1, len(array)):
            j =  i -1 
            t = array[i]
            while j>=0 and t < array[j]:
                array[j+1] = array[j]
                j = j - 1
            array[j+1] = t
        return array
    
    
    def sort_primitive_descent(self, array):
        
        for i in range(1, len(array)):
            j =  i -1 
            t = array[i]
            while j >=0 and t > array[j]:
                array[j+1] = array[j]
                j = j - 1
            array[j+1] = t
        return array
    
    #getattr(array[j-1], atribute) > getattr(array[j], atribute)
    
    def sort_models_ascent(self, array, atribute):
        
        for i in range(1, len(array)):
            j =  i -1 
            t = array[i]
            while j>=0 and getattr(t, atribute) < getattr(array[j], atribute):
                array[j+1] = array[j]
                j = j - 1
            array[j+1] = t
        return array
    
    
    def sort_models_descent(self, array, atribute):
        
        for i in range(1, len(array)):
            j =  i -1 
            t = array[i]
            while j>=0 and getattr(t, atribute) > getattr(array[j], atribute):
                array[j+1] = array[j]
                j = j - 1
            array[j+1] = t
        return array