##///
##||| Tower_M16/Lavax.PY TITANIUM
##||| Change list:
##||| * Fixed visible artifacts caused by incorrect lava height on the exterior.
##\\\ 


#############################################################################
#																			#
# lavas de la fase esta de la tower ( que no se acaba en la p.t. vida )		#
#																			#
# (Yuio)																	#
#																			#
#############################################################################

import LavaDefDamage

vLavaDM1=LavaDefDamage.LAVA_AREA()
vLavaDM2=LavaDefDamage.LAVA_AREA()
vLavaDM3=LavaDefDamage.LAVA_AREA()
vLavaDM4=LavaDefDamage.LAVA_AREA()
vLavaDM5=LavaDefDamage.LAVA_AREA()
vLavaDM6=LavaDefDamage.LAVA_AREA()
vLavaDM7=LavaDefDamage.LAVA_AREA()
vLavaDM8=LavaDefDamage.LAVA_AREA()
vLavaDM9=LavaDefDamage.LAVA_AREA()
vLavaDM10=LavaDefDamage.LAVA_AREA()
vLavaDM11=LavaDefDamage.LAVA_AREA()


#EN LAS GRIETAS EXTERIORES 
vLavaDM1.CreateLava ("vLava1" ,4500 , 34000 ,  59000 ,"cala2",0.02)

 
vLavaDM2.CreateLava ("vLava2" ,59000 , 34000 , -22000 ,"cala2",0.02)


#vLavaDM3.CreateLava ("vLava3" ,58000 ,  19000 , -54000 ,"cala2",0.02)

#al final
vLavaDM4.CreateLava ("vLava4" ,-3000 ,  34000 , -52000 ,"cala2",0.02)       # height was 3500 creating visible cracks in geometry

#interior 
vLavaDM5.CreateLava ("vLava5" ,-31000 ,  22000 , -28000 ,"cala2",0.02)



# EN LA SALA DE LOS SALAMANDERS
vLavaDM7.CreateLava ("vLava7" ,-26763 ,  -46700 , 16001 ,"cala2",0.03)

# EN LA SALA DE LA DERECHA
vLavaDM8.CreateLava ("vLava8" ,-12156.7, -48000.3, 24556.8 ,"cala2",0.03)

# EN LA SALA DE LA IZQUIERDA
vLavaDM9.CreateLava ("vLava9" ,-10471.3, -48682.0, -6106.9 ,"cala2",0.03)

# EN LA SALA ENORME
vLavaDM10.CreateLava ("vLava10" ,-15401.0, -66226.5, 5890.6 ,"cala2",0.04)

# EN LA ESCALERA DE CARACOLL
vLavaDM11.CreateLava ("vLava11" ,77000, 26000, 4500 ,"cala2",0.04)

# ACIDO DEL LAGO
vLavaDM6.CreateLava ("vLava6" ,-22000 , 16800 , 23000 ,"lava",0.04)


