from itertools import cycle
import argparse
import random

class Rut:

    def __init__(self,init,end,cantidad,formato):
        self.init = init
        self.end = end
        self.cantidad = cantidad
        self.ruts_generados = []
        self.formato = formato


    def retorna_formato(self,rut,dv):
        
        formatos = {
            1: lambda r, d: f"{r}-{d}", # Formato rut-dv
            2: lambda r, d: f"{r}{d}",  # Formato rutdv
            3: lambda r, d: f"{r}",  # Formato rut sin DV
        }
        try:
            return formatos[self.formato](rut, dv)
        except KeyError:
            raise ValueError(f"Formato desconocido: {self.formato}")
            

    @staticmethod
    def obten_dv(rut):

        rut = rut.upper().replace("-", "").replace(".", "")
        rut_aux = rut[:]

        revertido = map(int, reversed(rut_aux))
        factors = cycle(range(2, 8))
        suma = sum(d * f for d, f in zip(revertido, factors))
        residuo = suma % 11
        dv = 11 - residuo
    
        if dv == 10:
            return "K"
        elif dv == 11:
            return "0"
        else:
            return dv
    
        
    def generar_rut(self):
        for _ in range(self.cantidad):
            aux = random.randrange(inicio,fin)
            dv = Rut.obten_dv(str(aux))
            rut = self.retorna_formato(rut=aux,dv=dv)
            self.ruts_generados.append(rut)
        self.ruts_generados = list(set(self.ruts_generados))
        
        print(f"[+] Se generaron {len(self.ruts_generados)} ruts correctamente")


    @staticmethod
    def exportar_ruts(ruts,output):
        try: 
            with open(output,"w") as f:
                for x in ruts(): 
                    f.write(f"{x}\n")
            print(f"[+] Archivo {output} generado correctamente!!!")
        except Exception as e:
            print(f"[X] Ha ocurrido un error al generar {output}")
        

    def obtener_ruts(self): 
        return self.ruts_generados


parser = argparse.ArgumentParser(description="Programa pensado en el uso de generacion de diccionarios de ruts chilenos")
parser.add_argument("-i","--init",help="Inicio de generador de rut",type=int,default=1_000_000)
parser.add_argument("-e","--end",help="final de generador de rut",type=int,default=40_000_000)
parser.add_argument("-c","--count",help="Cantidad de ruts a generar",type=int,default=50)
parser.add_argument("-f","--formato",help="Formato salida rut: \n 1.- rut-DV \n 2.- rutDV \n 3.-rut sin dv",type=int,default=1,choices=[1,2,3])
parser.add_argument("-o","--output",help="Archivo salida",type=str,default="ruts.txt")

args = parser.parse_args()

inicio = args.init
fin = args.end
count = args.count
output = args.output 
formato = args.formato


ruts = Rut(inicio,fin,count,formato)
ruts.generar_rut()
Rut.exportar_ruts(ruts.obtener_ruts,output)

