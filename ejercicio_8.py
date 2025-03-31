# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_8 en python]
"""Recibir números hasta que 
exactamente aparezcan 5 cincos
 y 4 cuatros, el exceso en cincos
decrece al contador de cincos en uno
y coloca en cero al contador de cuatros,
el exceso en cuatros coloca en cero a 
ambos contadores, finalmente mostrar las
cantidades: ochos, nueves y otros números.
 """
c5inverso=5
estado_5=True
llego_a_4_cuatros=False
llego_a_5_cincos=False
c4,c5,c8,c9,cont=0,0,0,0,0
while True:
   numeros=int(input("ingrese numeros: "))
   if numeros == 4:
      c4+=1
      if c4==4:
         llego_a_4_cuatros=True # primera llave
      if c4>4: #en caso de exceder 4 cuatros
         c4=0 #se reinician a 0 ambos contadores
         c5=0
   elif numeros ==5:
      if c5<=5 and estado_5 ==True:
         c5+=1
      if c5>5: #en caso de exceder 5 cincos 
         estado_5=False
         c4=0 #y contador 4 se reinicia 
      if estado_5 ==False:
         c5-=1 #se reduce contador 5 uno a uno
      if c5 == 5:
         llego_a_5_cincos=True #segunda llave
   elif numeros==8:
      c8+=1
   elif numeros==9:
      c9+=1
   else:
      cont+=1
   #condicion para salir del bucle dos llaves True
   if llego_a_4_cuatros==True and llego_a_5_cincos==True:
      break
print(f"cantidad de 4:{c4} ") 
print(f"cantidad de 5:{c5} ") 
print(f"cantidad de 8:{c8} ") 
print(f"cantidad de 9:{c9} ") 
print(f"cantidad de otros:{cont} ") 

