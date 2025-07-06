##///
##||| DWARF_M3/objrot.PY TITANIUM
##||| Change list:
##||| * spark pass
##\\\ 

import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac

Bladex.AddCombustionDataFor("Caja_i_i", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("Cajon2", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("CajonPieza1", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza2", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza3", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza4", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza5", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza6", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza7", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza8", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza9", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza10", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza11", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza12", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza13", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza14", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza15", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza16", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza17", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza18", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("Barril", "LargeFire", 250, 400, 4, 1.5, 1, (BoxBurnTime+BoxDestroyTime)*3)
Bladex.AddCombustionDataFor("BarrilPieza1", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza2", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza3", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza4", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza5", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza6", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)



###########################################################
####----CAJAS-TAPANDO-LA-PUERTA-DEL-COMEDOR---#############
###########################################################

#1
Breakings.SetBreakable("CAJCO1",8,12)
#2
Breakings.SetBreakable("CAJCO2",8,12)
#3
Breakings.SetBreakable("CAJCO3",8,12)
#4
Breakings.SetBreakable("CAJCO4",8,12)
#5
Breakings.SetBreakable("CAJCO5",8,12)


#######################################
#---------SALA-SECRETA-DEL-COMEDOR--###
#######################################
#1
o=Bladex.CreateEntity("cofss1","Cofre",-28353.528009,-6555.132946,4927.953361,"Physic")
o.Scale=1.000000
o.Orientation=0.645974,0.645974,-0.287606,0.287606
platoss1=Breakings.CreateHiddenObject("platoss1", "Palangana",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
platoss1.FiresIntensity=[ 40 ]
platoss1.Lights=[ (0.000000,0.0,(0,0,0)) ]
platoss1.Solid=1
pocimac.CreatePotion("platoss1")
Breakings.SetBreakable("cofss1",8,12,"platoss1")

#2
o=Bladex.CreateEntity("cofss2","Cofre",-28725.427976,-6402.787928,3172.948939,"Physic")
o.Scale=0.727304
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofss2",8,12)

#3
o=Bladex.CreateEntity("cofss3","Cofre",-28459.300789,-7423.217383,3907.235253,"Physic")
o.Scale=0.878663
o.Orientation=0.223816,0.146728,-0.738152,0.619281
Breakings.SetBreakable("cofss3",8,12)

#4
o=Bladex.CreateEntity("cofss4","Cofre",-37377.061986,-6549.117190,459.994545,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
PocimaTodoDw1=Breakings.CreateHiddenObject("PocimaTodoDw1", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
PocimaTodoDw1.Solid=1
pocimac.CreatePotion("PocimaTodoDw1")
Breakings.SetBreakable("cofss4",8,12,"PocimaTodoDw1")


#5
o=Bladex.CreateEntity("cofss5","Caja_i_i",-36231.174978,-6606.942142,6900.321368,"Physic")
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("cofss5")  # Added -LeadHead

#6
o=Bladex.CreateEntity("cofss6","Caja_i_i",-34865.855317,-6372.776736,6987.759958,"Physic")
o.Scale=0.852821
o.Orientation=0.529592,0.529592,-0.468543,0.468543
Sparks.SetMetalSparkling("cofss6")  # Added -LeadHead

#7
#o=Bladex.CreateEntity("cofss7","Caja_i_r",-36516.993970,-6430.465418,8532.571053,"Physic")
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#Sparks.SetMetalSparkling("cofss7")


#8
o=Bladex.CreateEntity("cofss8","Cajon2",-29397.019246,-6597.150159,-4213.247075,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofss8",8,12)


#9
o=Bladex.CreateEntity("cofss9","Cajon2",-29181.465200,-6870.683283,-2798.818667,"Physic")
o.Scale=1.000000
o.Orientation=0.572001,0.414305,0.413618,0.574531
Breakings.SetBreakable("cofss9",8,12)


####################
######---MESAS--####
####################


Breakings.SetBreakable("dmesa1",8,12)
Breakings.SetBreakable("dmesa2",8,12)
Breakings.SetBreakable("dmesa3",8,12)
Breakings.SetBreakable("dmesa4",8,12)
Breakings.SetBreakable("dmesa5",8,12)  #biblioteca

#Breakings.SetBreakable("dmesa6",8,12)
Breakings.SetBreakable("dmesa7",8,12)
Breakings.SetBreakable("dmesa9",8,12)
Breakings.SetBreakable("dmesa10",8,12)  # Re-enabled LeadHead
Breakings.SetBreakable("dmesa11",8,12)
Breakings.SetBreakable("dmesa12",8,12)
Breakings.SetBreakable("dmesa13",8,12)

Breakings.SetBreakable("mesa14",8,12)
Breakings.SetBreakable("dmesa16",8,12)

##############CAJAS EN SALA CON FORMA DE ESTRELLA

Breakings.SetBreakable("dcajon1",8,12)
#
Breakings.SetBreakable("dcajon2",8,12)
#
pan=Breakings.CreateHiddenObject("pancom3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom3")
Breakings.SetBreakable("dcajon3",8,12,"pancom3")
#
pan=Breakings.CreateHiddenObject("pancom4", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom4")
Breakings.SetBreakable("dcajon4",8,12,"pancom4")
#
Breakings.SetBreakable("dcajon5",8,12)
#
##############CAJAS EN SALA DE LOS SUBTERRANEOS

Breakings.SetBreakable("dcajon6",8,12)
#
Breakings.SetBreakable("dcajon7",8,12)
#
Breakings.SetBreakable("dcajon8",8,12)
#
Breakings.SetBreakable("dcajon9",8,12)
#
Breakings.SetBreakable("dcajon10",8,12)
#
Breakings.SetBreakable("dcajon11",8,12)
#
Breakings.SetBreakable("dcajon12",8,12)
#

Breakings.SetBreakable("dbarril1",8,12)
#
pan=Breakings.CreateHiddenObject("pancom12", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom12")
Breakings.SetBreakable("dbarril2",8,12,"pancom12")
#
Breakings.SetBreakable("dbarril3",8,12)
#
Breakings.SetBreakable("dbarril4",8,12)


#al lado de la primera hoguera
Breakings.SetBreakable("dbarril5",8,12)
#
Breakings.SetBreakable("dbarril6",8,12)
#
Breakings.SetBreakable("dbarril7",8,12)
#
Breakings.SetBreakable("darmero1",8,12)

###DONDE ESTA EL PRIMER TROLL

#
pan=Breakings.CreateHiddenObject("pancomb8", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancomb8")
Breakings.SetBreakable("dbarril8",8,12,"pancomb8")
#
Breakings.SetBreakable("dbarril9",8,12)
#
pan=Breakings.CreateHiddenObject("pancomb10", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancomb10")
Breakings.SetBreakable("dbarril10",8,12,"pancomb10")
#



##############SILLAS EN SALA DEL PALACIO

Breakings.SetBreakable("silla1",8,12)
#
Breakings.SetBreakable("silla2",8,12)
#
Breakings.SetBreakable("silla3",8,12)
#
Breakings.SetBreakable("silla4",8,12)
#
Breakings.SetBreakable("silla5",8,12)
#
Breakings.SetBreakable("silla6",8,12)
#
Breakings.SetBreakable("silla7",8,12)
#



##############CAJAS EN SALA DE GUARDIA

Breakings.SetBreakable("dcajon13",8,12)
#
pan=Breakings.CreateHiddenObject("pancom14", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom14")
Breakings.SetBreakable("dcajon14",8,12,"pancom14")
#
Breakings.SetBreakable("dcajon15",8,12)
#
pan=Breakings.CreateHiddenObject("pancom16", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom16")
Breakings.SetBreakable("dcajon16",8,12,"pancom16")
#
Breakings.SetBreakable("dcajon17",8,12)
#
pan=Breakings.CreateHiddenObject("pancom18", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom18")
Breakings.SetBreakable("dcajon18",8,12,"pancom18")
#
#mesa que atasca la puerta
#Breakings.SetBreakable("dmesasa15",8,12)
#

##BLOQUES TRANSPARENTES

o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-279857.699966,-28276.402456,42246.653006,"Physic")
o.Scale=3.908663
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.CastShadows=0
o.Alpha = 0