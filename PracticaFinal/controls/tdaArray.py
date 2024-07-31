from controls.exception.arrayPositionException import ArrayPositionException

class TDAArray:

    def __init__(self, size, value = None):
        self.__size = size
        self.__position = 0
        if size > 0:
            self.__array = []            
            for i in range(0, self.__size):
                self.__array.append(None)   
                     
        else:
            self.__array = None

    @property
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value

    def insert(self, value, pos):
        # size = 5   pos = 6
        if (pos < self.__size and pos >= 0):            
            self.__array[pos] = value
        else:
            raise ArrayPositionException("Index found error "+str(pos))

    def save(self, value):
        # size = 5   pos = 6
        #if self.__array[0] == None:
            self.__array[self.__position] = value
            self.__position = self.__position + 1
        #else:            
         #   self.__array[self.__position] = value
          #  self.__position = self.__position + 1
        

    def check(self):
        i = -1
        #cont = 0
        for j in range(0, self.__size):
            if self.__array[j] == None:
                i = j
                break
        #for value in self.__array:
        #    if value == None:
        #        i = cont
        #        break
        #    cont = cont + 1
        return i 
    
    def get(self, pos): 
        if (pos < self.__size and pos >= 0):            
            return self.__array[pos]
        else:
            raise ArrayPositionException("Index found error "+str(pos))    
        
    def len(self):
        return len(self.__array)
        
    def __str__(self):
        return str(self.__array)   
        