

class Burbuja:
    
    def sort_burbuja_number_ascent(self, array):
        
        for i in range(0, len(array) - 1):
            for j in range(1, len(array)):
                if array[j-1] > array[j]:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
    
    def sort_burbuja_number_descent(self, array):
        for i in range(0, len(array) - 1):
            for j in range(1, len(array)):
                if array[j-1] < array[j]:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
    
    
    def sort_burbuja_atribute_ascent(self, array, atribute):    
        
        for i in range(0, len(array) - 1):
            for j in range(1, len(array)):
                #cls = getattr(array[0], "_apellidos")
                if getattr(array[j-1], atribute) > getattr(array[j], atribute):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
    
    def sort_burbuja_atribute_descent(self, array, atribute):   
        print("entro al metodo") 
        for i in range(0, len(array) - 1):
            for j in range(1, len(array)):
                if getattr(array[j-1], atribute) < getattr(array[j], atribute):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array