class QuickSort:
    

    def quicksort_numbers_ascent(self, array, low, high):
        if low < high:
            pi = self.seleccionar_numbers_ascent(array, low, high)
            self.quicksort_numbers_ascent(array, low, pi-1)
            self.quicksort_numbers_ascent(array, pi+1, high)
        return array
    
    def seleccionar_numbers_ascent(self, array, low, high):
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
             
        aux = array[i + 1]  
        array[i + 1] = array[high]
        array[high] = aux
        return i + 1
    
    def quicksort_numbers_descent(self, array, low, high):
        if low < high:
            pi = self.seleccionar_numbers_descent(array, low, high)
            self.quicksort_numbers_descent(array, low, pi-1)
            self.quicksort_numbers_descent(array, pi+1, high)
        return array
    
    def seleccionar_numbers_descent(self, array, low, high):
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            if array[j] >= pivot:
                i += 1
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
             
        aux = array[i + 1]  
        array[i + 1] = array[high]
        array[high] = aux
        return i + 1
    
    def quicksort_models_ascent(self, array, low, high, atribute):        
        if low < high:
            pi = self.seleccionar_models_ascent(array, low, high, atribute)
            
            self.quicksort_models_ascent(array, low, pi - 1, atribute)
            self.quicksort_models_ascent(array, pi + 1, high, atribute)
        return array
    

    def seleccionar_models_ascent(self, array, low, high, atribute):
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            if getattr(array[j], atribute) <= getattr(pivot, atribute):
                i += 1
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
             
        aux = array[i + 1]  
        array[i + 1] = array[high]
        array[high] = aux
        return i + 1
    
    def quicksort_models_descent(self, array, low, high, atribute):        
        if low < high:
            pi = self.seleccionar_models_descent(array, low, high, atribute)
            
            self.quicksort_models_descent(array, low, pi - 1, atribute)
            self.quicksort_models_descent(array, pi + 1, high, atribute)
        return array


    def seleccionar_models_descent(self, array, low, high, atribute):
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            if getattr(array[j], atribute) >= getattr(pivot, atribute):
                i += 1
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
             
        aux = array[i + 1]  
        array[i + 1] = array[high]
        array[high] = aux
        return i + 1