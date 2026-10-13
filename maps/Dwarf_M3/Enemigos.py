from megaimport import *

from math import pow
import EnemyTypes
import Sparks
import Actions
import pocimac

#######################################################################
###########
###########	BICHOS AL PRINCIPIO DEL NIVEL
###########
#######################################################################


#####PRIMEROS ORCOS SOBRE ESCALERAS DE ENTRADA


#1-----------------ORC-PATRULLANDO---1-------------------

Orksword1=Bladex.CreateEntity("dwarfGladius1","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("dwarfGladius1")

pers=Bladex.CreateEntity("1ORC","Ork",91641.925653, 3532.17923102, -20505.5709591,"Person")
pers.Angle=6.26312373572
pers.Level=0
Actions.TakeObject(pers.Name,"dwarfGladius1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=DwarfDefeatsOrc
pers.SetOnFloor()
"""
pers.AddBayPoint=91641.925653, 3532.17923102, -20505.5709591
pers.AddBayPoint=91083.1394259, 3529.49836016, -33248.9657573
pers.AddBayPoint=93128.6284486, 3532.00790901, -36313.4126106
pers.AddBayPoint=95496.4302092, 3531.43492076, -33217.9682479
pers.AddBayPoint=95593.1879763, 3529.28203785, -21225.9996849
pers.AddBayPoint=93569.2930738, 3548.70957528, -19018.9191431
"""

#2-----------------ORC-SOBRE-ESCALERAS---2-------------------

espada=Bladex.CreateEntity("dwarfGladius2","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwarfEscudo2","Escudo5",0,0,0)
Sparks.MakeShield("dwarfEscudo2")
Breakings.SetBreakableWS("dwarfEscudo2")
Breakings.SetBreakableWS("dwarfGladius2")


pers=Bladex.CreateEntity("2ORC","Ork",74092.9096907, 128.369448039, -15044.9217653,"Person")
pers.Angle=4.54816107478
pers.Level=0
Actions.TakeObject(pers.Name,"dwarfGladius2")
Actions.TakeObject(pers.Name,"dwarfEscudo2")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#2b-----------------ORC-TRAS PUERTA QUE SE ABRE--2b-------------------

espada=Bladex.CreateEntity("dwfGladius2b","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo2b","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo2b")
Breakings.SetBreakableWS("dwfEscudo2b")
Breakings.SetBreakableWS("dwfGladius2b")

pers=Bladex.CreateEntity("2bORC","Ork",14179.1328835, -870.930199857, -27539.1431826,"Person")
pers.Angle=3.10314325023
pers.Level=0
Actions.TakeObject(pers.Name,"dwfGladius2b")
Actions.TakeObject(pers.Name,"dwfEscudo2b")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3-----------------JEFE ORC-CON LLAVE-----------------------

espada=Bladex.CreateEntity("dwfOrksword3","Gladius",0,0,0,"Weapon")
Breakings.SetBreakableWS("dwfOrksword3")

#pers=Bladex.CreateEntity("3ORC","Great_Ork",36137.9974301, -1894.13391242, -16153.8617126,"Person")
pers=Bladex.CreateEntity("3ORC","Ork",28562.9817626, -1872.74938902, -11275.3625443,"Person")
pers.Angle=1.67604968684
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword3")
Actions.TakeObject("3ORC","llave1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#4-----------------ORCO-ACOMPAÑANDO AL ANTERIOR JEFE-----------
#1
espada=Bladex.CreateEntity("dwfOrksword4","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo4","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo4")
Breakings.SetBreakableWS("dwfEscudo4")
Breakings.SetBreakableWS("dwfOrksword4")

pers=Bladex.CreateEntity("4ORC","Ork",28675.298468, -1880.10849975, -26871.5659024,"Person")
pers.Angle=0.541636220918
pers.Level=0
Actions.TakeObject(pers.Name,"dwfOrksword4")
Actions.TakeObject(pers.Name,"dwfEscudo4")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

##############################################################################
##########
##########	PASAMOS LA PRIMERA PUERTA
##########
##############################################################################

# ORCO APOSTADO EN ESCALERAS

espada=Bladex.CreateEntity("dwfOrksword5","Garrote",0,0,0,"Weapon")
#escudo=Bladex.CreateEntity("dwfEscudo5","Escudo5",0,0,0)
#Sparks.MakeShield("dwfEscudo5")
#Breakings.SetBreakableWS("dwfEscudo5")
Breakings.SetBreakableWS("dwfOrksword5")


pers=Bladex.CreateEntity("5ORC","Ork",-12465.7005213, -5783.6159203, -24829.0496834,"Person")
pers.Angle=2.08964365911
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword5")
#Actions.TakeObject(pers.Name,"dwfEscudo5")
pers.ActionAreaMin=pow(2,3)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


# ORCO JUSTO ANTES DE LA GRIETA

espada=Bladex.CreateEntity("dwfOrksword7","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo7","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo7")
Breakings.SetBreakableWS("dwfEscudo7")
Breakings.SetBreakableWS("dwfOrksword7")


pers=Bladex.CreateEntity("7ORC","Ork",-27295.5956305, -7370.7716098, -20556.0229133,"Person")
pers.Angle=4.69325666092
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword7")
Actions.TakeObject(pers.Name,"dwfEscudo7")
pers.ActionAreaMin=pow(2,3)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#################################################################################################
############
############
############ BICHOS A PARTIR ESCENA PELEA SALA ROTA
############
#################################################################################################




###################################################################
## 	TROLL guardian de los pulsadores con llave

"""
espada=Bladex.CreateEntity("dwfgarrote11","Garropin",0,0,0,"Weapon")

#pers=Bladex.CreateEntity("11TRL","Troll_Dark",-37911.3655634, -8668.73235028, -78790.0840093,"Person")
pers=Bladex.CreateEntity("11TRL","Troll_Dark",-30347.8635069, -8985.46910338, -69030.491702,"Person")
pers.Angle=3
Actions.TakeObject(pers.Name,"dwfgarrote11")
Actions.TakeObject("11TRL","llave2")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
espada=Bladex.CreateEntity("dwfOrksword11","Gladius",0,0,0,"Weapon")
Breakings.SetBreakableWS("dwfOrksword11")

pers=Bladex.CreateEntity("11ORC","Great_Ork",-30347.8635069, -8985.46910338, -69030.491702,"Person")
pers.Angle=1.67604968684
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword11")
Actions.TakeObject("11ORC","llave2")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

## 2 orcos acompañando a troll anterior


#1
espada=Bladex.CreateEntity("dwfOrksword8","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo8","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo8")
Breakings.SetBreakableWS("dwfEscudo8")
Breakings.SetBreakableWS("dwfOrksword8")

pers=Bladex.CreateEntity("8ORC","Ork",-38074.8386947, -8668.88877328, -73679.6655051,"Person")
pers.Angle=0.812191418694
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword8")
Actions.TakeObject(pers.Name,"dwfEscudo8")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


"""
#2
espada=Bladex.CreateEntity("dwfOrksword8a","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo8a","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo8a")
Breakings.SetBreakableWS("dwfEscudo8a")
Breakings.SetBreakableWS("dwfOrksword8a")

pers=Bladex.CreateEntity("8aORC","Ork",-54926.813604, -8670.59196532, -78637.9979769,"Person")
pers.Angle=0.025866692913
pers.Level=0
Actions.TakeObject(pers.Name,"dwfOrksword8a")
Actions.TakeObject(pers.Name,"dwfEscudo8a")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""


################################################################################
### jefe orco en la sala del elevador

potion9orc=Bladex.CreateEntity("Potion9orc","Pocima50",0,0,0)
potion9orc.Static=0
potion9orc.Solid=0
potion9orc.Scale=1.220190
pocimac.CreatePotion("Potion9orc")

espada=Bladex.CreateEntity("dwfOrksword9","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo9","Escudo2",0,0,0)
Sparks.MakeShield("dwfEscudo9")
Breakings.SetBreakableWS("dwfEscudo9")
Breakings.SetBreakableWS("dwfOrksword9")


#pers=Bladex.CreateEntity("9ORC","Great_Ork",-123056.111449, -8626.93322894, -83305.8772201,"Person")
pers=Bladex.CreateEntity("9ORC","Great_Ork",-128398.804224, -8633.50494356, -78128.9025755,"Person")
pers.Angle=5.4
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword9")
Actions.TakeObject(pers.Name,"dwfEscudo9")
Actions.TakeObject(pers.Name,"Potion9orc")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#################################################################
##
##	ORCO PATRULLANDO POR EL PISO INFERIOR	


espada=Bladex.CreateEntity("dwfOrksword10","Garrote",0,0,0,"Weapon")
#escudo=Bladex.CreateEntity("dwfEscudo10","Escudo5",0,0,0)
#Sparks.MakeShield("dwfEscudo10")
#Breakings.SetBreakableWS("dwfEscudo10")
Breakings.SetBreakableWS("dwfOrksword10")

#pers=Bladex.CreateEntity("10ORC","Ork",-141045.529536, -1371.61326569, -58208.426868,"Person")
pers=Bladex.CreateEntity("10ORC","Ork",-127699.716936, -887.539374806, -81624.1828156,"Person")
pers.Angle=3.10845503211
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword10")
#Actions.TakeObject(pers.Name,"dwfEscudo10")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

"""
pers.AddBayPoint=-127699.716936, -887.539374806, -81624.1828156
pers.AddBayPoint=-121973.411704, -887.692334186, -79231.9484458
pers.AddBayPoint=-121463.521983, -888.403810415, -73006.3939613
pers.AddBayPoint=-126182.183564, -890.615198231, -70003.6047939
pers.AddBayPoint=-138807.516819, -688.122926839, -72183.6621895
pers.AddBayPoint=-145943.045245, -689.539618795, -78465.9928492
pers.AddBayPoint=-151304.472088, -689.406956732, -78947.2850794
pers.AddBayPoint=-153771.1943, -688.510708268, -75004.6576533
pers.AddBayPoint=-150934.711287, -689.405939029, -75327.8669509
pers.AddBayPoint=-147261.978892, -693.283377489, -77985.7165221
pers.AddBayPoint=-136495.025307, -689.765469895, -78681.2207308
"""

#######################################################################
##
##	ORCOS TRAS LAS BARRAS-AURELIO
##


#1
espada=Bladex.CreateEntity("dwfOrksword17","Hacha",0,0,0,"Weapon")
Breakings.SetBreakableWS("dwfOrksword17")

#pers=Bladex.CreateEntity("17ORC","Great_Ork",-89786.437064, -4403.46423786, 401.414184104,"Person")
pers=Bladex.CreateEntity("17ORC","Great_Ork",-111335.436528, -3397.21247962, -35289.618985,"Person")
pers.Angle=1.5
pers.Level=0
Actions.TakeObject(pers.Name,"dwfOrksword17")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#2
espada=Bladex.CreateEntity("dwfOrksword29","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo29","Escudo2",0,0,0)
Sparks.MakeShield("dwfEscudo29")
Breakings.SetBreakableWS("dwfEscudo29")
Breakings.SetBreakableWS("dwfOrksword29")

#pers=Bladex.CreateEntity("29ORC","Ork",-87514.7235433, -5623.51237864, 7859.02089657,"Person")
pers=Bladex.CreateEntity("29ORC","Ork",-123387.103994, -2989.15415315, -28818.0131783,"Person")
pers.Angle=2.98599034706
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword29")
Actions.TakeObject(pers.Name,"dwfEscudo29")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#############################################################################
##
##	ORCO DENTRO DE LA SALA DE LA COMIDA????????

#1
espada=Bladex.CreateEntity("dwfOrksword30","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo30","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo30")
Breakings.SetBreakableWS("dwfEscudo30")
Breakings.SetBreakableWS("dwfOrksword30")

#pers=Bladex.CreateEntity("30ORC","Ork",-65560.9327292, -8870.68403052, 9718.03087984,"Person")
pers=Bladex.CreateEntity("30ORC","Ork",-65560.9327292, -8870.68403052, 9718.03087984,"Person")
pers.Angle=1.53304132239
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword30")
Actions.TakeObject(pers.Name,"dwfEscudo30")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#################################################################################
##
##	ORCOS TRAS LA SALA ROTA 2



#4
espada=Bladex.CreateEntity("dwfOrksword31","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo31","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo31")
Breakings.SetBreakableWS("dwfEscudo31")
Breakings.SetBreakableWS("dwfOrksword31")

pers=Bladex.CreateEntity("31ORC","Ork",-111139.929525, -9684.34693154, 2779.51487646,"Person")
pers.Angle=3.9676402848
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword31")
Actions.TakeObject(pers.Name,"dwfEscudo31")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#5
espada=Bladex.CreateEntity("dwfOrksword32","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo32","Escudo2",0,0,0)
Sparks.MakeShield("dwfEscudo32")
Breakings.SetBreakableWS("dwfEscudo32")
Breakings.SetBreakableWS("dwfOrksword32")

pers=Bladex.CreateEntity("32ORC","Ork",-132600.825399, -8262.96084304, 581.126089702,"Person")
pers.Angle=4.76353217549
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword32")
Actions.TakeObject(pers.Name,"dwfEscudo32")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


####################################################################
#18-----------------TROLL-EN-LA-SALA-GRANDE-DEL-PALACIO----------
####################################################################

garrote=Bladex.CreateEntity("dwfOrksword18","Maza",0,0,0,"Weapon")
Breakings.SetBreakableWS("dwfOrksword18")

pers=Bladex.CreateEntity("18TRL","Troll_Dark",-228643.44971, -14895.4804574, 15928.0929515,"Person")
pers.Angle=5.84596352431
pers.Level=0
Actions.TakeObject(pers.Name,"dwfOrksword18")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.ImDeadFunc = AbreDespuesDeMorir


###################################################################
## bichos variados hasta sala del trono
###################################################################


#1
espada=Bladex.CreateEntity("dwfOrksword33","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo33","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo33")
Breakings.SetBreakableWS("dwfEscudo33")
Breakings.SetBreakableWS("dwfOrksword33")

#pers=Bladex.CreateEntity("33ORC","Ork",-248864.003206, -19872.1997248, 20849.2581814,"Person")
pers=Bladex.CreateEntity("33ORC","Ork",-246500.709795, -19889.2770337, 20677.7414757,"Person")
pers.Angle=0.9
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword33")
Actions.TakeObject(pers.Name,"dwfEscudo33")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#2
espada=Bladex.CreateEntity("dwfOrksword34","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo34","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo34")
Breakings.SetBreakableWS("dwfEscudo34")
Breakings.SetBreakableWS("dwfOrksword34")

pers=Bladex.CreateEntity("34ORC","Ork",-238468.189076, -19871.895677, 54779.6656534,"Person")
pers.Angle=1.62477910267
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword34")
Actions.TakeObject(pers.Name,"dwfEscudo34")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()




###	OCO JEFE EN LA SALA DEL TRONO

#1
potion35orc=Bladex.CreateEntity("dwarfPotion35orc","PocimaTodo",0,0,0)
potion35orc.Static=0
potion35orc.Solid=0
potion35orc.Scale=1.220190
pocimac.CreatePotion("dwarfPotion35orc")

espada=Bladex.CreateEntity("dwfOrksword35","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo35","Escudo2",0,0,0)
Sparks.MakeShield("dwfEscudo35")
Breakings.SetBreakableWS("dwfEscudo35")
Breakings.SetBreakableWS("dwfOrksword35")

pers=Bladex.CreateEntity("35ORC","Great_Ork",-218300.258573, -19895.1292691, 64187.4221368,"Person")
#pers=Bladex.CreateEntity("35ORC","Great_Ork",-220843.581159, -20073.6016611, 69688.2143103,"Person")
pers.Angle=1.86
pers.Level=0
Actions.TakeObject(pers.Name,"dwfOrksword35")
Actions.TakeObject(pers.Name,"dwfEscudo35")
Actions.TakeObject(pers.Name,"dwarfPotion35orc")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#############################################################
#########	orco patrulla en puente roto con antorcha
#1
potion36orc=Bladex.CreateEntity("dwarfPotion36orc","PocimaTodo",0,0,0)
potion36orc.Static=0
potion36orc.Solid=0
potion36orc.Scale=1.220190
pocimac.CreatePotion("dwarfPotion36orc")

antorcha=Bladex.CreateEntity("Antorcha36","Antorcha",0,0,0,"Weapon")
antorcha.FiresIntensity=[ 3 ]
antorcha.Lights=[ (10.000000,0.09,(237,180,61)) ]
Torchs.SetUsable("Antorcha36",10.000000,0.09,-1)

espada=Bladex.CreateEntity("dwfOrksword36","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo36","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo36")
Breakings.SetBreakableWS("dwfEscudo36")
Breakings.SetBreakableWS("dwfOrksword36")

pers=Bladex.CreateEntity("36ORC","Ork",-180522.924781, -11906.3612555, 12282.6696591,"Person")
pers.Angle=6
pers.Level=1
#Actions.TakeObject(pers.Name,"dwfOrksword36")
Actions.TakeObject(pers.Name,"Antorcha36")
#Actions.TakeObject(pers.Name,"dwfEscudo36")
Actions.TakeObject(pers.Name,"dwarfPotion36orc")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-180522.924781, -11906.3612555, 12282.6696591
pers.AddBayPoint=-170468.342365, -10902.8299474, 11338.220098
pers.AddBayPoint=-160415.924994, -10317.0053576, 11694.8134348
pers.AddBayPoint=-159808.849815, -10287.1336909, 13875.8921061
pers.AddBayPoint=-163001.961951, -10565.0120094, 15116.2454303
pers.AddBayPoint=-168855.040107, -10898.7264695, 16089.0221568
pers.AddBayPoint=-179135.764386, -11900.3844692, 14564.2663074
"""


# tras puente roto sale de la puerta amenazante QUE POR CIERTO NO SALE

espada=Bladex.CreateEntity("dwfOrksword37","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo37","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo37")
Breakings.SetBreakableWS("dwfEscudo37")
Breakings.SetBreakableWS("dwfOrksword37")


pers=Bladex.CreateEntity("37ORC","Great_Ork",-185385.97497, -11898.4319376, 18290.9752846,"Person")
pers.Angle=4.2268263204
pers.Level=1
Actions.TakeObject(pers.Name,"dwfOrksword37")
Actions.TakeObject(pers.Name,"dwfEscudo37")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#darfuncs.HideBadGuy("37ORC")


#sectx1=Bladex.GetSector(-158197.789085, -10110.6508041, 13970.7184006)

#sectx1.OnEnter=x1

########################################################################
####	ORCOS QUE SALEN DE LA PUERTA DE LA SALA GRANDE

espada=Bladex.CreateEntity("dwfOrksword38","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo38","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo38")
Breakings.SetBreakableWS("dwfEscudo38")
Breakings.SetBreakableWS("dwfOrksword38")


pers=Bladex.CreateEntity("38ORC","Ork",-230417.838956, -14890.9008515, -6745.81155729,"Person")
pers.Angle=6
pers.Level=2
Actions.TakeObject(pers.Name,"dwfOrksword38")
Actions.TakeObject(pers.Name,"dwfEscudo38")
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



########################################################################
####	ORCOS EN LA BIBLIOTECA

#1
espada=Bladex.CreateEntity("dwfOrksword39","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo39","Escudo5",0,0,0)
Sparks.MakeShield("dwfEscudo39")
Breakings.SetBreakableWS("dwfEscudo39")
Breakings.SetBreakableWS("dwfOrksword39")


pers=Bladex.CreateEntity("39ORC","Ork",-246000, -28140.074, 59462.975,"Person")
pers.Angle=6
pers.Level=3
Actions.TakeObject(pers.Name,"dwfOrksword39")
Actions.TakeObject(pers.Name,"dwfEscudo39")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#2
espada=Bladex.CreateEntity("dwfOrksword40","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("dwfEscudo40","Escudo2",0,0,0)
Sparks.MakeShield("dwfEscudo40")
Breakings.SetBreakableWS("dwfEscudo40")
Breakings.SetBreakableWS("dwfOrksword40")


pers=Bladex.CreateEntity("39ORC","Ork",-251529.704862, -28146.7050701, 44235.3240287,"Person")
pers.Angle=6
pers.Level=3
Actions.TakeObject(pers.Name,"dwfOrksword40")
Actions.TakeObject(pers.Name,"dwfEscudo40")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()






########################################################################
#---ARANIAS EN LA SALA DEL HACHA

#----PRIMER GRUPO
#1
pers=Bladex.CreateEntity("1SPD","Spidersmall",-43500,-11000,-111000,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
pers=Bladex.CreateEntity("2SPD","Spidersmall",-41000,-11000,-114000,"Person")
pers.Level=2
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3
pers=Bladex.CreateEntity("3SPD","Spidersmall",-38500,-11000,-121500,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#4
pers=Bladex.CreateEntity("4SPD","Spidersmall",-35500,-11000,-124000,"Person")
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#---ARANIAS EN LA SALA DE LAS COLUMNAS

#----PRIMER GRUPO
#1
pers=Bladex.CreateEntity("5SPD","Spidersmall",1955.2262072, -6885.04294568, -10504.2887759,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,5)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#2
pers=Bladex.CreateEntity("6SPD","Spidersmall",892.64111, -6886.7598, 4557.434,"Person")
pers.Level=2
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,5)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3
pers=Bladex.CreateEntity("7SPD","Spidersmall",-11925.8987, -6878.68525, -2737.074,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,5)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#4
pers=Bladex.CreateEntity("8SPD","Spidersmall",-21249.1804, -6877.425, -5482.628,"Person")
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,5)
pers.ActionAreaMax=pow(2,4)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()