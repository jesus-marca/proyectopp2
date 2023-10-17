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


def combinacion (n):
    return ("#"+str(n))
register.filter("combinacion",combinacion)
