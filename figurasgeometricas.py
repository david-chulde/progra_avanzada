import math
def menu():
    print("\n********************************************")
    print("\t          ESCUELA POLITECNICA NACIONAL")
    print("\t BIENVENIDOS AL MENU NUMERO LADOS DE FIGURAS GEOMETRICAS")
    print("digite cero para salir")

def pentagono ( lados,ra ) :
        archi=open('Pentagono.txt','a')
        peri=lados*5
        lados=lados/2
        a=math.sqrt((ra**2)-(lados**2))
        área = (peri*a)/2
        print("El perimetro es: ",peri)
        archi.write('\nEl perimetro es:'+str(peri))
        print ("El area es:" , área)
        archi.write('\nEl area es:'+str(área))
        print("el apotema es: ",a)
        archi.write("el apotema es: "+str(a))
        archi.close()
 
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
        archi=open('Triangulo.txt','a')
        área = (b * h)/2
        peri=b+h+y
        print ("El area es:" , área)
        archi.write('\nEl area es:'+str(área))
        print("El perimetro es: ",peri)
        archi.write('\nEl perimetro es:'+str(peri))
        archi.close()
def heptagono(lados):
    t=360/7
    peri=lados*7
    a=lados/(2 * math.tan(t/2)) 
    área=(lados*a*7)/2
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)
    print("El apotemea es: ",a)

def octogono(lados):
    t=360/8
    peri=lados*8
    a=lados/(2 * math.tan(t/2)) 
    área=4*lados*a
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)
    print("El apotemea es: ",a)


def nonagono(lados):
    peri=lados*9
    área=9*(lados**2)/(4 * math.tan(180/2)) 
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)

def decagono(lados):
    peri=lados*10
    área=10*(lados**2)/(4 * math.tan(180/10)) 
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)



def nonagono(lados):
    peri=lados*9
    área=9*(lados**2)/(4 * math.tan(180/2)) 
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)

def decagono(lados):
    peri=lados*10
    área=10*(lados**2)/(4 * math.tan(180/10)) 
    print ("El area es:" ,  área)
    print("El perimetro es: ",peri)
    
def main(): 
    opc=1
    while(opc!=10 | opc!=1 | opc!=2):
        menu()
        print("Ingrese numero de lados\n")
        opc = int(input ())
        if opc == 3:
            
            archi=open('Triangulo.txt','w')
            archi.close()
            archi=open('Triangulo.txt','a')
            print("El numero de lados ingresado corresponde a un triangulo")
            archi.write("FIGURA TRIANGULO\n")
            b = int ( input ( "introducir la base:" ) )
            archi.write('\nBASE: '+str(b))
            h = int ( input ( "introducir la altura:" ) )
            archi.write('\nALTURA: '+str(h))
            y=int(input("introducir los lados"))
            archi.write('\nLADOS: '+str(y))
            archi.close()
            triangulo(b,h,y )
        elif opc ==4 :
            
            archi=open('Triangulo.txt','w')
            archi.close()
            print("El numero de lados ingresado corresponde a un cuadrado")
            Lado = int ( input ( "introducir el valor del Lado:" ) )
            cuadrado ( Lado )
        elif opc == 5:

            archi=open('Pentagono.txt','w')
            archi.close()
            archi=open('Pentagono.txt','a')
            print("El numero de lados ingresado corresponde a un pentagono")
            archi.write("FIGURA PENTAGONO\n")
            ra=int(input("ingrese radio: "))
            archi.write("\nRADIO: "+str(ra))
            lados=int(input("introducir longitud de los lados: " ) )
            archi.write("\nLONGITUD DE LADOS: "+str(lados))
            archi.close()
            pentagono ( lados,ra )
        elif opc ==6 :
            print("El numero de lados ingresado corresponde a un hexagono")
            ra=int(input("ingrese radio: "))
            hexagono(ra)
        elif opc ==7 :
            print("El numero de lados ingresado corresponde a un heptagono")
            lados=float(input("Ingrese longitud de los lados"))
            heptagono(lados)
        elif opc ==8 :
            print("El numero de lados ingresado corresponde a un octagono")
            lados=float(input("Ingrese longitud de los lados"))
            octogono(lados)
        elif opc ==9 :
            print("El numero de lados ingresado corresponde a un nonagono")
            lados=float(input("Ingrese longitud de los lados"))
            nonagono(lados)
        elif opc ==10 :
            print("El numero de lados ingresado corresponde a un decagono")
            lados=float(input("Ingrese longitud de los lados"))
            decagono(lados)
        elif opc==0:
            print ("Has salido de la aplicación")
            exit()
        else:
                print ("Opcion incorrecta:....!!!!")
main()
