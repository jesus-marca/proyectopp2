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
    s=str(n)
    if s == '12:00:00':
        s="12 m"        
        return s
    else:
        return n

register.filter("formatoHora",formatoHora)

def renombrar(n):    
    if n == 'parent':               
        return 'estudiante'  
    if n == 'student':               
        return 'estudiante'
    if n == 'teacher':               
        return 'profesor' 

register.filter("renombrar",renombrar)


def formatoDia(n): 
    n=str(n)   
    if n == 'Monday':               
        return 'Lunes'  
    if n == 'Tuesday':               
        return 'Martes'
    if n == 'Wednesday':               
        return 'Miercoles' 
    if n == 'Thursday':               
        return 'Jueves'
    if n == 'Friday':               
        return 'Viernes'

register.filter("formatoDia",formatoDia)

# def filtrar(subjects,slt):
#     count=0   
#     n=6
 
    
#     for subject in subjects:
#         if subject.standard_slots_subject.all.count == 0 :
#             for slot in subject.standard_slots_subject.all :
#                 if slot.day.id == 1 and slot.slot == slt :
#                     count=count+1
#     if count == n :
#         return True
#     else:
#         return False
# register.filter("filtrar",filtrar)

@register.simple_tag
def define(val=0):
  return val