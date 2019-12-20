# GINO - libreria de funciones
#  ejercicio 1
# funcion que devuelva el area de un rectangulo
def area_rectangulo(base,altura):
    area=(base*altura)
    return area
#  ejercicio 2
# funcion que devuelva la suma de dos numeros
def suma(a,b):
    s=a+b
    return s
#  ejercicio 3
# funcion que devuelva la resta de dos numeros
def resta(n,m):
    respuesta=n-m
    return respuesta
#  ejercicio 4
# funcion que devuelva el resultado de una multiplicacion
def multiplicacion(x,y):
    res=x*y
    return res
#  ejercicio 5
# funcion que devuelva la divicion de dos numeros
def division(a1,a2):
    div=a1/a2
    return div
#  ejercicio 6
# funcion que devuelva el area de un cuadrilatero
def area_cuadrilatero(a,b,c):
    area=2*(a*b+b*c+a*c)
    return area
#  ejercicio 7
# funcion que devuelva el volumen de un cuadrilatero
def volumen_cuadrilatero(l1,l2,l3):
    volumen=l1*l2*l3
    return volumen
#  ejercicio 8
# funcion que devuelva el nombre de un sujeto
def nombre_sujeto(nom):
    nombre=nom
    return nombre
#  ejercicio 9
# funcion que devuelva el promedio aritmetico de 2 numeros
def promedio_aritmetico(h1,h2):
    promedio=(h1*h2)/2
    return promedio
#  ejercicio 10
# funcion que devuelva la velocidad del movil
def velocidad_movil(d,t):
    velocidad=d/t
    return velocidad
#  ejercicio 11
#funcion que devuelva la distancia recorrida de un movil
def distancia_recorrida(v,t):
    distancia=v*t
    return distancia
#  ejercicio 12
# funcion que devuelva el promedio geometrico de dos numeros
def promedio_geometrico(a,b):
    promed=(a*b)/2
    return promed
#  ejercicio 13
# funcion que devuelva el area del cuadrado
def area_cuadrado(l):
    area=6*(l**2)
    return area
#  ejercicio 14
# funcion que devuelva la suma de 3 numeros
def sumar(a,b,c):
    res=a+b+c
    return res
#  ejercicio 15
# funcion que devuelva el numero mayor de 2 numeros
def mayor(n1, n2):
    if (n1 > n2):
        return n1
    else:
        return n2
#  ejercicio 16
# funcion que devuelva el numero menor de 2 numeros
def menor(p1, p2):
    if (p1 < p2):
        return p1
    else:
        return p2
#  ejercicio 17
# funcion que devuelva la edad comprendida entre 18 y 25
def pedir_edad(msj):
    return (msj,18,25)
#  ejercicio 18
# funcion que devuelva si el nro es impar,devolver true,caso contrario,false
def es_impar(num):
    if (num % 2 != 0):
        return True
    else:
        return False
#  ejercicio 19
# funcion que devuelva si el nro es par,devolver true,caso contrario,false
def es_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False
#  ejercicio 20
# funcion que devuelva el promedio armonico de 2 numeros
def promedio_armonico(a,b):
    prom=(a+b)/(a*b)
    return prom
#  ejercicio 21
# funcion que devuelva la fuerza de un hombre que aplica en un cuerpo
def fuerza_hombre(m,a):
    fuerza=m*a
    return fuerza
#  ejercicio 22
# funcion que devuelva la potencia de un motor en el trabajo respecto al tiempo
def potencia_motor(w,t):
    potencia=w/t
    return potencia
#  ejercicio 23
# funcion que devuelva la respuesta de una ecuacion de primer grado
def ecuacion_grado1(x,y):
    respuesta=((x+y)*x)-y
    return respuesta
#  ejercicio 24
# funcion que devuelva el perimetro de un triangulo equilatero
def perimetro_triangulo(l):
    perimetro=3*l
    return perimetro
#  ejercicio 25
# funcion que devuelva la hipotenusa usando pitagoras
def hipotenusa_pitagoras(b,c):
    hipotenusa=((b**2)+(c**2))**(1/2)
    return hipotenusa
#fin_25-ejercicios_GINO