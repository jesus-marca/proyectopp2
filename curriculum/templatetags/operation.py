from django.template import Library
register=Library()
def multiplicar(id_atributo):
    if(id_atributo <= 7):        
        return (id_atributo*55  +id_atributo)
    else:
        if (id_atributo <= 15):
            return (id_atributo*21+70 +id_atributo)
        else:
            if (id_atributo <= 23):
                return (id_atributo*15+70 +id_atributo)
            else:
                if (id_atributo <= 30):
                    return (id_atributo*12+60 +id_atributo)
                else:
                    if (id_atributo <= 37):
                        return (id_atributo*10+40 +id_atributo)
                    else:                         
                        return (id_atributo*8+60 +id_atributo)
            
register.filter("multiplicar",multiplicar)

def modificar (id_atributo):
    return (id_atributo*2 +50)

register.filter("modificar",modificar)


def arreglo (n):
    f = []

    for i in range(n):
       f.append(i+1)
    return f
register.filter("arreglo",arreglo)



def parseada (n):

    return str(n)
register.filter("parseada",parseada)

def parseada2 (n):
    return ("prop"+str(n))
register.filter("parseada2",parseada2)


def combinacion (n):
    return ("#"+str(n))
register.filter("combinacion",combinacion)



def combinacionLabel (n):
    return ("staticBackdropLabel"+str(n))
register.filter("combinacionLabel",combinacionLabel)

def combinacion2 (n):
    return ("#prop"+str(n))
register.filter("combinacion2",combinacion2)

def formatoHora(n):
    
    inicio = n[:-14]
    final= n[:-3]
    final=final[11:]
    
    h1=inicio[1]
    hEntero1=int(h1)
    
    h2=inicio[1]
    hEntero2=int(h2)
    
    if(hEntero1 == 12 ):
        mi="m"
    if(hEntero1 > 12 ):
        mi="pm"
    if(hEntero1 < 12 ):
        mi="am"
        
    if(hEntero2 == 12 ):
        mf="m"
    if(hEntero2 > 12 ):
        mf="pm"
    if(hEntero2 < 12 ):
        mf="am"
    
    inicio = inicio + mi
    final = final + mf
    
    return (inicio + " - "+ final)
register.filter("formatoHora",formatoHora)