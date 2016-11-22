import math
def menu():
    print("\n********************************************")
    print("\t          ESCUELA POLITECNICA NACIONAL")
    print("\t BIENVENIDOS AL MENU NUMERO LADOS DE FIGURAS GEOMETRICAS")
    print("digite cero para salir")

def pentagono ( lados,ra ) :
        peri=lados*5
        lados=lados/2
        a=math.sqrt((ra**2)-(lados**2))
        área = (peri*a)/2
        print("El perimetro es: ",peri)
        print ("El area es:" , área)
        print("el apotema es: ",a)
 
def cuadrado ( Lado ) :
        área = Lado ** 2
        peri=Lado*4
        print ("El area es:" ,  área)
        print("El perimetro es: ",peri)

def hexagono(ra):
    peri=ra*6
    a=math.sqrt((ra**2)-((ra/2)**2))
    área = (peri*a)/2
    print ("El area es:" , área)
    print("El perimetro es: ",peri)
    print("El apotema es: ",a)
 
def triangulo (b,h,y) :
        área = (b * h)/2
        peri=b+h+y
        print ("El area es:" , área)
        print("El perimetro es: ",peri)
        a=6


def main(): 
    opc=1
    while(opc!=6 | opc!=1 | opc!=2):
        menu()
        print("Ingrese numero de lados\n")
        opc = int(input ())
        if opc == 3:
            print("El numero de lados ingresado corresponde a un triangulo")
            b = int ( input ( "introducir la base:" ) )
            h = int ( input ( "introducir la altura:" ) )
            y=int(input("introducir los lados"))
            triangulo(b,h,y )
        elif opc ==4 :
            print("El numero de lados ingresado corresponde a un cuadrado")
            Lado = int ( input ( "introducir el valor del Lado:" ) )
            cuadrado ( Lado )
        elif opc == 5:
            print("El numero de lados ingresado corresponde a un pentagono")
            ra=int(input("ingrese radio: "))
            lados=int(input("introducir longitud de los lados: " ) )
            pentagono ( lados,ra )
        elif opc ==6 :
            print("El numero de lados ingresado corresponde a un hexagono")
            ra=int(input("ingrese radio: "))
            hexagono(ra)
        elif opc==0:
            print ("Has salido de la aplicación")
            exit()
        else:
                print ("Opcion incorrecta:....!!!!")
main()
