class Ventana:
    __titulo=''
    __xsupizq=0
    __ysupizq=0
    __xinfder=500
    __yinfder=500
    def __init__(self,titulo,xsupizq=100,ysupizq=100,xinfder=100,yinfder=100):
        self.__titulo=titulo
        self.__xsupizq=int(xsupizq)
        self.__ysupizq=int(ysupizq)
        self.__xinfder=int(xinfder)
        self.__yinfder=int(yinfder)
    def mostrar(self):
        print('Titulo: {}'.format(self.__titulo))
        print('Vertice x superior izquierdo: {}\n'.format(self.__xsupizq))
        print('Vertice y superior izquierdo: {}\n'.format(self.__ysupizq))
        print('Vertice x inferior derecho: {}\n'.format(self.__xinfder))
        print('Vertice y inferior derecho: {}\n'.format(self.__yinfder))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__yinfder-self.__ysupizq)
    def ancho(self):
        return (self.__xinfder-self.__xsupizq)
    def moverDerecha(self,desplazamiento=1):
        if desplazamiento+self.__xinfder <=500 and desplazamiento+self.__xsupizq < self.__xinfder:
            self.__xinfder+=desplazamiento
            self.__xsupizq+=desplazamiento
        else:
            print('Desplazamiento en x no cumple con las condiciones')
    def moverIzquierda(self,desplazamiento=1):
        if self.__ysupizq-desplazamiento>=0 and self.__yinfder-desplazamiento>self.__ysupizq:
            self.__yinfder-=desplazamiento
            self.__ysupizq-=desplazamiento
        else:
            print('Desplazamiento en y no cumple con las condiciones')
    def bajar(self,desplazamiento=1):
        if desplazamiento+self.__xinfder <=500 and desplazamiento+self.__xsupizq < self.__xinfder:
            self.__xinfder+=desplazamiento
            self.__xsupizq+=desplazamiento
    def subir(self,desplazamiento=1):
        if self.__ysupizq-desplazamiento>=0 and self.__yinfder-desplazamiento>self.__ysupizq:
            self.__yinfder-=desplazamiento
            self.__ysupizq-=desplazamiento