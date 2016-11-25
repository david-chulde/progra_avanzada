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
        archi.write("\nel apotema es: "+str(a))
        archi.close()
 
def cuadrado ( Lado ) :
        archi=open('Cuadrado.txt','a')
        área = Lado ** 2
        peri=Lado*4
        print ("El area es:" ,  área)
        archi.write('\nEl area es:'+str(área))
        print("El perimetro es: ",peri)
        archi.write('\nEl perimetro es:'+str(peri))
        archi.close()
        
def hexagono(ra):
    archi=open('Hexagono.txt','a')
    peri=ra*6
    a=math.sqrt((ra**2)-((ra/2)**2))
    área = (peri*a)/2
    print ("El area es:" , área)
    archi.write('\nEl area es:'+str(área))
    print("El perimetro es: ",peri)
    archi.write('\nEl perimetro es:'+str(peri))
    print("El apotema es: ",a)
    archi.write("\nel apotema es: "+str(a))
    archi.close()
 
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
    archi=open('Heptagono.txt','a')
    t=360/7
    peri=lados*7
    a=lados/(2 * math.tan(t/2)) 
    área=(lados*a*7)/2
    print ("El area es:" ,  área)
    archi.write('\nEl area es:'+str(área))
    print("El perimetro es: ",peri)
    archi.write('\nEl perimetro es:'+str(peri))
    print("El apotemea es: ",a)
    archi.write("\nEl apotema es: "+str(a))
    archi.close()

def octogono(lados):
    archi=open('Octagono.txt','a')
    t=360/8
    peri=lados*8
    a=lados/(2 * math.tan(t/2)) 
    área=4*lados*a
    print ("El area es:" ,  área)
    archi.write('\nEl area es:'+str(área))
    print("El perimetro es: ",peri)
    archi.write('\nEl perimetro es:'+str(peri))
    print("El apotemea es: ",a)
    archi.write("\nEl apotema es: "+str(a))
    archi.close()

def nonagono(lados):
    archi=open('Nonagono.txt','a')
    peri=lados*9
    área=9*(lados**2)/(4 * math.tan(180/2)) 
    print ("El area es:" ,  área)
    archi.write('\nEl area es:'+str(área))
    print("El perimetro es: ",peri)
    archi.write('\nEl perimetro es:'+str(peri))
    archi.close()

def decagono(lados):
    archi=open('Nonagono.txt','a')
    peri=lados*10
    área=10*(lados**2)/(4 * math.tan(180/10)) 
    print ("El area es:" ,  área)
    archi.write('\nEl area es:'+str(área))
    print("El perimetro es: ",peri)
    archi.write('\nEl perimetro es:'+str(peri))
    archi.close()


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
            
            archi=open('Cuadrado.txt','w')
            archi.close()
            archi=open('Cuadrado.txt','a')
            print("El numero de lados ingresado corresponde a un cuadrado")
            archi.write("FIGURA CUADRADO\n")
            Lado = int ( input ( "introducir el valor del Lado:" ) )
            archi.write('\nLADO: '+str(Lado))
            archi.close()
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
            archi=open('Hexagono.txt','w')
            archi.close()
            archi=open('Hexagono.txt','a')
            print("El numero de lados ingresado corresponde a un hexagono")
            archi.write("FIGURA HEXAGONO\n")
            ra=int(input("ingrese radio: "))
            archi.write("\nRADIO: "+str(ra))
            archi.close()
            hexagono(ra)
        elif opc ==7 :

            archi=open('Heptagono.txt','w')
            archi.close()
            archi=open('Heptagono.txt','a')
            print("El numero de lados ingresado corresponde a un heptagono")
            archi.write("FIGURA HEPTAGONO\n")
            lados=float(input("Ingrese longitud de los lados"))
            archi.write("\nLONGITUD DE LADOS: "+str(lados))
            archi.close()
            heptagono(lados)
            
        elif opc ==8 :

            archi=open('Octagono.txt','w')
            archi.close()
            archi=open('Octagono.txt','a')
            print("El numero de lados ingresado corresponde a un octagono")
            archi.write("FIGURA OCTAGONO\n")
            lados=float(input("Ingrese longitud de los lados"))
            archi.write("\nLONGITUD DE LADOS: "+str(lados))
            archi.close()
            octogono(lados)
            
        elif opc ==9 :

            archi=open('Nonagono.txt','w')
            archi.close()
            archi=open('Nonagono.txt','a')
            print("El numero de lados ingresado corresponde a un nonagono")
            archi.write("FIGURA NONAGONO\n")
            lados=float(input("Ingrese longitud de los lados"))
            archi.write("\nLONGITUD DE LADOS: "+str(lados))
            archi.close()
            nonagono(lados)
            
        elif opc ==10 :
            
            archi=open('Decagono.txt','w')
            archi.close()
            archi=open('Decagono.txt','a')
            print("El numero de lados ingresado corresponde a un decagono")
            archi.write("FIGURA DECAGONO\n")
            lados=float(input("Ingrese longitud de los lados"))
            archi.write("\nLONGITUD DE LADOS: "+str(lados))
            archi.close()
            decagono(lados)
            
        elif opc==0:
            print ("Has salido de la aplicación")
            exit()
        else:
                print ("Opcion incorrecta:....!!!!")
main()
