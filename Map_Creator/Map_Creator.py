import cv2 as cv #Libreria para crear formas y usar imagenes
import math #Libreria para usar el coseno y seno
import keyboard 


#Carlos Octavio Solorzano Aguilar


dis = []
hoy = 0
stop = 1
size = 1024

ang = []
coor_x = [] #Almacenaje de coordenadas horizontales
coor_y = [] #Almacenaje de coordenadas verticales

dis = [
 38, 
39, 
40, 
51, 
50, 
51, 
37, 
31, 
31, 
119, 
120, 
119, 
60, 
63, 
104, 
43, 
42, 
41, 
41, 
42, 
56, 
55, 
42, 
36, 
36, 
34, 
35, 
37, 
56, 
55, 
41, 
39,
 ]

si = 1
mov = 0
zoom = 2
clavo = 0
acer = 0
desh = 320
hor = 0
desy = 240
ver = 0

#Imprime las coordenadas
#print("Coordenadas x")
#print(coor_x)
#print("Coordenadas y")
#print(coor_y)
#print("Angulo de mas")
#print(mov)

num_ang = range(0,len(dis))
num = range(0,len(dis)-1) #Numero de lineas (mas uno que se hara aparte)

while si == 1:

 if keyboard.is_pressed("v"):
     mov = 0
     zoom = 2
     clavo = 0
     acer = 0
     desh = 320
     hor = 0
     desy = 240
     ver = 0

 if keyboard.is_pressed("u") == 0 and keyboard.is_pressed("i") == 0:
     clavo -= clavo / 6

 if keyboard.is_pressed("i"):
      if clavo <= 2:
       clavo +=0.1
 
 if keyboard.is_pressed("u"):
     if clavo >= -2:
       clavo -= 0.1

 if keyboard.is_pressed("j") == 0 and keyboard.is_pressed("k") == 0:
     acer -= acer / 6

 if keyboard.is_pressed("k"):
      if acer <= 2 :
       acer +=0.1
 
 if keyboard.is_pressed("j") and zoom > 0:
     if acer >= -2:
       acer -= 0.1
 
 if keyboard.is_pressed("a") == 0 and keyboard.is_pressed("d") == 0:
     hor -= hor / 6

 if keyboard.is_pressed("d"):
      if hor <= 2:
       hor +=0.1
 
 if keyboard.is_pressed("a"):
     if hor >= -2:
       hor -= 0.1

 if keyboard.is_pressed("w") == 0 and keyboard.is_pressed("s") == 0:
     ver -= ver / 6

 if keyboard.is_pressed("s"):
      if ver <= 2:
       ver +=0.1
 
 if keyboard.is_pressed("w"):
     if ver >= -2:
       ver -= 0.1

 mov += clavo
 zoom += acer / 30
 desh += hor 
 desy += ver

 while mov >= 360:
     mov -= 360

 while mov <= 0:
     mov += 360

 while zoom < 0:
     zoom = 0

 for e in num_ang:  #Se asignan valores de coordenadas a partir de la distancias y el angulo 
   ang.append(e * 360/len(dis))
   coor_x.append(e/len(dis))
   coor_y.append(e/len(dis))

   coor_x[e] = int (desh + ((math.sin((int (ang[e] + mov) * math.pi)/180))*dis[e] * zoom )) #Coordenadas horizontales X
   coor_y[e] = int (desy + (((math.cos((int (ang[e] + mov) * math.pi)/180))*dis[e] * zoom) * -1)) #Coordenadas verticales Y

 mg = cv.imread('plano.png') #Se usa una imagen predeterminada
 
 cv.line(mg, (coor_x[len(dis)-1], coor_y[len(dis)-1]), (coor_x[0], coor_y[0] ), (200,255,0), thickness = 2) #Linea que une el mapa o la forma
 cv.line(mg, (int(desh),int(desy)), (coor_x[len(dis)-1], coor_y[len(dis)-1]), (0,255,0), thickness = 1) #Creacion de lineas a partir de las coordenadas
 cv.circle(mg, (coor_x[len(dis)-1], coor_y[len(dis)-1]), 2, (0,0,255) , thickness = 2) #Creacion de puntos a partir de las coordenadas

 for n in num: #Creacion del mapa
  cv.line(mg, (coor_x[n], coor_y[n]), (coor_x[n + 1], coor_y[n + 1]), (255,0,0), thickness = 2) #Creacion de lineas a partir de las coordenadas
  cv.line(mg, (int(desh),int(desy)), (coor_x[n], coor_y[n]), (0,255,0), thickness = 1) #Creacion de lineas a partir de las coordenadas
  cv.circle(mg, (coor_x[n], coor_y[n]), 2, (0,0,255) , thickness = 2) #Creacion de puntos a partir de las coordenadas

 cv.imshow('MAPA', mg) #Muestra el mapa en una ventana
 cv.waitKey(delay = 1) #Esto evita que a ventana se cierre de inmediato