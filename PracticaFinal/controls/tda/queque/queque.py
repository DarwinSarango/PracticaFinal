from controls.tda.queque.quequeOperation import QuequeOperation

#Encuapsulamos para que no se vean esos metodos que no pertenecen a stack, PATRON DE DEISEÑO FACADE
class QueQue():
    def __init__(self, top):
        self.__queque = QuequeOperation(top)

    def queque(self, data):
        self.__queque.queque(data)

    @property
    def dequeque(self):
        return self.__queque.dequeque
    
    @property
    def print(self):
        self.__queque.print

    def verifyTop(self):
        self.__queque.verifyTop

    def isEmpty(self):
        self.__queque.isEmpty

  

    