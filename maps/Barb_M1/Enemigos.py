#from megaimport import *

from math import pow
import EnemyTypes
import Sparks
import Actions
import pocimac
import darfuncs

#---------ORCO-PRIMERA-CASETA-----------------------


Espada1=Bladex.CreateEntity("barbEspada1","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbEspada1")


pers=Bladex.CreateEntity("1ORC","Ork",-130531.27838, -6967.8173963, -26497.5388876,"Person")
pers.Angle=1.23404798421
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=BarbDefeatsOrc
pers.SetOnFloor()

#---PUENTE-ORCO---

Espada2=Bladex.CreateEntity("barbEspada2","Garrote",0,0,0,"Weapon")
escudo2=Bladex.CreateEntity("barbEscudo2","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo2")
Breakings.SetBreakableWS("barbEscudo2")
Breakings.SetBreakableWS("barbEspada2")
potion=Bladex.CreateEntity("PotionO2","Pocima25",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("PotionO2")


pers=Bladex.CreateEntity("2ORC","Ork",-117137.608353, -11159.9307817, -53098.0866595,"Person")
#pers=Bladex.CreateEntity("2ORC","Ork",-116500,-12000,-43000)
pers.Angle=6.23582495054
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada2")
Actions.TakeObject(pers.Name,"barbEscudo2")
Actions.TakeObject(pers.Name,"PotionO2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=BarbDefeatsOrc
pers.SetOnFloor()

"""
pers.AddBayPoint=-117137.608353, -11159.9307817, -53098.0866595
pers.AddBayPoint=-116951.842114, -7666.50499627, -35722.7485584
pers.AddBayPoint=-136753.189607, -6746.51090912, -31852.7995443
pers.AddBayPoint=-140962.735406, -6543.963871, -26909.9968481
pers.AddBayPoint=-136753.189607, -6746.51090912, -31852.7995443
pers.AddBayPoint=-116951.842114, -7666.50499627, -35722.7485584
pers.AddBayPoint=-116882.495861, -9305.98498724, -44745.7979041
"""



#---ORCOS-EN-GRUTA---------

#---1
Espada3=Bladex.CreateEntity("barbEspada3","Gladius",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbEspada3")

pers=Bladex.CreateEntity("3ORC","Ork",-77768.3664835, -11159.6285462, -81408.8238848,"Person")
pers.Angle=3.60287491073
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada3")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)

EnemyTypes.EnemyDefaultFuncs(pers)

#---2
Espada4=Bladex.CreateEntity("barbEspada4","Garrote",0,0,0,"Weapon")
escudo4=Bladex.CreateEntity("barbEscudo4","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo4")
Breakings.SetBreakableWS("barbEscudo4")
Breakings.SetBreakableWS("barbEspada4")
potion=Bladex.CreateEntity("PotionO4","Pocima25",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("PotionO4")
pers.SetOnFloor()

pers=Bladex.CreateEntity("4ORC","Ork",-74064.0397584, -11158.7978885, -86260.5431127,"Person")
pers.Angle=0.16970304176
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada4")
Actions.TakeObject(pers.Name,"barbEscudo4")
Actions.TakeObject(pers.Name,"PotionO4")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#-------------------------patrullas variadas-TRAS EL PUENTE

#----1	en la caseta
Espada5=Bladex.CreateEntity("barbEspada5","Garrote",0,0,0,"Weapon")
escudo5=Bladex.CreateEntity("barbEscudo5","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo5")
Breakings.SetBreakableWS("barbEscudo5")
Breakings.SetBreakableWS("barbEspada5")

pers=Bladex.CreateEntity("5ORC","Ork",-74720.7497453, -11959.0939721, -42887.9934098,"Person")
pers.Angle=4.55205587735
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada5")
Actions.TakeObject(pers.Name,"barbEscudo5")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-74720.7497453, -11959.0939721, -42887.9934098
pers.AddBayPoint=-61048.1812481, -12259.2334971, -44948.8236083
pers.AddBayPoint=-48640.1237056, -12449.9907544, -32215.0475721
pers.AddBayPoint=-53261.8417117, -12061.6892196, -14043.6628038
"""

#----1	en la al lado del fuego
Espada5=Bladex.CreateEntity("barbEspada5b","Garrote",0,0,0,"Weapon")
escudo5=Bladex.CreateEntity("barbEscudo5b","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo5b")
Breakings.SetBreakableWS("barbEscudo5b")
Breakings.SetBreakableWS("barbEspada5b")

pers=Bladex.CreateEntity("5bORC","Ork",-44995.3389882, -12426.0839639, -16455.8786951,"Person")
pers.Angle=1.2
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada5b")
Actions.TakeObject(pers.Name,"barbEscudo5b")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#----2	 EN LA CASITA DEL HERMITANYO

espada6=Bladex.CreateEntity("barbespada6","Gladius",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbespada6")

pers=Bladex.CreateEntity("H6ORC","Ork",15060.2790355, -22221.6863333, 53467.5477254,"Person")
pers.Angle=2.37530708478
pers.Level=2
Actions.TakeObject(pers.Name,"barbespada6")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

"""
#----2	debajo de los puentes naturales

espada6=Bladex.CreateEntity("barbespada6","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbespada6")

pers=Bladex.CreateEntity("6ORC","Ork",-3553.25363186, -10459.1323469, 53923.4973735,"Person")
pers.Angle=2.37530708478
pers.Level=0
Actions.TakeObject(pers.Name,"barbespada6")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.AddBayPoint=947.908292222, -10222.7367759, 48814.8387395
#pers.AddBayPoint=-2169.09643943, -11216.8429327, 32512.9162085
pers.AddBayPoint=-6000.9173977, -11458.6761518, 15206.9789979
pers.AddBayPoint=-19676.2113526, -11470.8366028, 7547.49423751
pers.AddBayPoint=-38833.4496479, -11460.5876914, 3109.34984251
pers.AddBayPoint=-47079.8002683, -11525.6893901, -2813.90356637
pers.AddBayPoint=-47898.0736116, -11698.775443, -6960.75919772
pers.AddBayPoint=-43965.3910932, -11597.515415, -5564.49516698

pers.AddBayPoint=-38833.4496479, -11460.5876914, 3109.34984251
pers.AddBayPoint=-19676.2113526, -11470.8366028, 7547.49423751
pers.AddBayPoint=-6647.9173977, -11458.6761518, 15206.9789979
pers.AddBayPoint=-2217.90231334, -11150.8351313, 33975.0510168
pers.AddBayPoint=-3064.48932814, -10467.9243498, 50220.6557104
"""


##frente a la puerta que no se abre


#1
#Espada7=Bladex.CreateEntity("barbEspada7","Garrote",0,0,0,"Weapon")
#Breakings.SetBreakableWS("barbEspada7")
##potion=Bladex.CreateEntity("PotionO7","Pocima50",0,0,0)
#potion.Static=0
#potion.Solid=1
#potion.Scale=1.0
#pocimac.CreatePotion("PotionO7")


#pers=Bladex.CreateEntity("7ORC","Great_Ork",-33200.0230385, -11065.3964188, 47333.9931301,"Person")
#pers.Angle=5.4405856872
#pers.Level=0
#Actions.TakeObject(pers.Name,"barbEspada7")
#Actions.TakeObject(pers.Name,"PotionO7")
#pers.ActionAreaMin=pow(2,4)
#pers.ActionAreaMax=pow(2,5)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.SetOnFloor()

#2
Espada8=Bladex.CreateEntity("barbEspada8","Gladius",0,0,0,"Weapon")
escudo8=Bladex.CreateEntity("barbEscudo8","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo8")
Breakings.SetBreakableWS("barbEscudo8")
Breakings.SetBreakableWS("barbEspada8")


pers=Bladex.CreateEntity("8ORC","Ork",-33430.6910776, -11638.09038, 56054.2316482,"Person")
pers.Angle=5.37154164506
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada8")
Actions.TakeObject(pers.Name,"barbEscudo8")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-33430.6910776, -11638.09038, 56054.2316482
pers.AddBayPoint=-35108.5916844, -11975.0768421, 51178.1938169
pers.AddBayPoint=-31869.5352754, -11620.3555468, 49258.9839069
pers.AddBayPoint=-27535.6067163, -11015.3725479, 54228.8652555
pers.AddBayPoint=-22148.7424279, -10816.7909138, 58144.5988981
pers.AddBayPoint=-21934.7738368, -10821.2390306, 61715.8397629
pers.AddBayPoint=-26186.6322375, -10837.7215113, 60168.3393045
"""
#al otro lado de la puerta--------

#1
Espada9=Bladex.CreateEntity("barbEspada9","Gladius",0,0,0,"Weapon")
Espada9.Weapon=1
escudo9=Bladex.CreateEntity("barbEscudo9","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo9")
Breakings.SetBreakableWS("barbEscudo9")
Breakings.SetBreakableWS("barbEspada9")


pers=Bladex.CreateEntity("9ORC","Ork",-55400.739138, -12231.8235567, 58053.0047823,"Person")
pers.Angle=0.787313142929
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada9")
Actions.TakeObject(pers.Name,"barbEscudo9")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-55400.739138, -12231.8235567, 58053.0047823
pers.AddBayPoint=-67308.5096626, -12461.2877023, 69675.540308
"""

#2
Espada10=Bladex.CreateEntity("barbEspada10","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbEspada10")

pers=Bladex.CreateEntity("10ORC","Ork",-74810.5211031, -10245.1482164, 75959.6679414,"Person")
pers.Angle=0.776129621307
pers.Level=2
Actions.TakeObject(pers.Name,"barbEspada10")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-74810.5211031, -10245.1482164, 75959.6679414
pers.AddBayPoint=-79159.8932592, -9984.73859533, 81506.40069
pers.AddBayPoint=-79159.8932592, -9984.73859533, 81506.40069
pers.AddBayPoint=-94198.3634407, -8711.19470967, 77810.5292923
pers.AddBayPoint=-95887.1671975, -8656.72343524, 74015.4105939
pers.AddBayPoint=-93805.6249091, -8859.91344247, 73581.3746129
pers.AddBayPoint=-84664.0356283, -9881.17132503, 76883.6033607
"""

## orco patrullando en interior pueblo

Espada11=Bladex.CreateEntity("barbEspada11","Hacha",0,0,0,"Weapon")
escudo11=Bladex.CreateEntity("barbEscudo11","Escudo2",0,0,0)
Sparks.MakeShield("barbEscudo11")
Breakings.SetBreakableWS("barbEscudo11")
Breakings.SetBreakableWS("barbEspada11")
potion=Bladex.CreateEntity("Potion11","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("Potion11")


pers=Bladex.CreateEntity("11ORC","Great_Ork",-119450.419998, -6288.86941448, 102847.187754,"Person")
pers.Angle=0.990235456459
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada11")
Actions.TakeObject(pers.Name,"barbEscudo11")
Actions.TakeObject(pers.Name,"Potion11")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
pers.AddBayPoint=-119450.419998, -6288.86941448, 102847.187754
pers.AddBayPoint=-165884.659009, -6289.49618279, 134077.21883
"""

#---ORCOS-accesorios en pueblo---

#---1---
Espada12=Bladex.CreateEntity("barbEspada12","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbEspada12")

pers=Bladex.CreateEntity("12ORC","Ork",-109551.103257, -7876.89449812, 120220.389773,"Person")
pers.Angle=2.18172778005
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada12")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#---2---
Espada13=Bladex.CreateEntity("barbEspada13","Garrote",0,0,0,"Weapon")
escudo13=Bladex.CreateEntity("barbEscudo13","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo13")
Breakings.SetBreakableWS("barbEscudo13")
Breakings.SetBreakableWS("barbEspada13")


pers=Bladex.CreateEntity("13ORC","Ork",-151539.460088, -8074.9171658, 149163.609201,"Person")
pers.Angle=2.15616609401
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada13")
Actions.TakeObject(pers.Name,"barbEscudo13")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


##############################################################################
##############################################################################

##zombies en segunda parte


#---1---
Espada19=Bladex.CreateEntity("barbEspada19","Garrote",0,0,0,"Weapon")
Breakings.SetBreakableWS("barbEspada19")


pers=Bladex.CreateEntity("19ZM","Lich",-140241.1271, -20488.5006214, 181763.700343,"Person")
pers.Angle=0.682276452172
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada19")
pers.ActionAreaMin=pow(2,15)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

####en la zona de las cositas

#---2---
Espada20=Bladex.CreateEntity("barbEspada20","Hacha",0,0,0,"Weapon")
escudo20=Bladex.CreateEntity("barbEscudo20","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo20")
Breakings.SetBreakableWS("barbEscudo20")
Breakings.SetBreakableWS("barbEspada20")

pers=Bladex.CreateEntity("20ZM","Lich",-131981.592522, -25275.5432216, 165710.034904,"Person")
pers.Angle=0.683543204155
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada20")
Actions.TakeObject(pers.Name,"barbEscudo20")
#pers.ActionAreaMin=pow(2,2)
#pers.ActionAreaMax=pow(2,2)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()




#---COSITAS frente a CASA DE TEJADO INCLINADO

#1
pers=Bladex.CreateEntity("1cos","Cos",-109037.07346, -24277.2371467, 157599.711041,"Person")
pers.Angle=1.25850192312
pers.Level=0
#pers.ActionAreaMin=pow(2,2)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#2
pers=Bladex.CreateEntity("2cos","Cos",-114020.588363, -24277.3311436, 159593.994649,"Person")
pers.Angle=1.46242257244
pers.Level=2
#pers.ActionAreaMin=pow(2,2)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3
pers=Bladex.CreateEntity("3cos","Cos",-116526.664824, -24299.2541561, 156822.973137,"Person")
pers.Angle=1.29369242322
pers.Level=2
#pers.ActionAreaMin=pow(2,2)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()




#####################################################################
#### en casa del jefe



#1
Espada21=Bladex.CreateEntity("barbEspada21","Maza",0,0,0,"Weapon")
escudo21=Bladex.CreateEntity("barbEscudo21","Escudo2",0,0,0)
Sparks.MakeShield("barbEscudo21")
Breakings.SetBreakableWS("barbEscudo21")
Breakings.SetBreakableWS("barbEspada21")

pers=Bladex.CreateEntity("21ZM","Skeleton",-58524.664879, -30296.5470709, 157781.193137,"Person")
pers.Angle=1.09276331014
pers.Level=2
Actions.TakeObject(pers.Name,"barbEspada21")
Actions.TakeObject(pers.Name,"barbEscudo21")
#pers.ActionAreaMin=pow(2,1)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
Espada22=Bladex.CreateEntity("barbEspada22","Hacha",0,0,0,"Weapon")
escudo22=Bladex.CreateEntity("barbEscudo22","Escudo2",0,0,0)
Sparks.MakeShield("barbEscudo22")
Breakings.SetBreakableWS("barbEscudo22")
Breakings.SetBreakableWS("barbEspada22")

pers=Bladex.CreateEntity("22ZM","Skeleton",-75632.3967294, -31991.6729537, 147371.43794,"Person")
pers.Angle=0.373207196344
pers.Level=2
Actions.TakeObject(pers.Name,"barbEspada22")
Actions.TakeObject(pers.Name,"barbEscudo22")
#pers.ActionAreaMin=pow(2,1)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



####en planta intermedia con luz genital
#1
Espada23=Bladex.CreateEntity("barbEspada23","Garrote",0,0,0,"Weapon")
escudo23=Bladex.CreateEntity("barbEscudo23","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo23")
Breakings.SetBreakableWS("barbEscudo23")
Breakings.SetBreakableWS("barbEspada23")

pers=Bladex.CreateEntity("23ZM","Lich",-56364.06391, -34364.5492384, 127937.527031,"Person")
pers.Angle=6.14396422389
pers.Level=1
Actions.TakeObject(pers.Name,"barbEspada23")
Actions.TakeObject(pers.Name,"barbEscudo23")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,2)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
Espada24=Bladex.CreateEntity("barbEspada24","Maza",0,0,0,"Weapon")
escudo24=Bladex.CreateEntity("barbEscudo24","Escudo2",0,0,0)
Sparks.MakeShield("barbEscudo24")
Breakings.SetBreakableWS("barbEscudo24")
Breakings.SetBreakableWS("barbEspada24")

pers=Bladex.CreateEntity("24ZM","Skeleton",-51363.3911947, -34364.6141634, 127923.755387,"Person")
pers.Angle=6.14396446051
pers.Level=2
Actions.TakeObject(pers.Name,"barbEspada24")
Actions.TakeObject(pers.Name,"barbEscudo24")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,2)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


##	en la sala bajita
#4
Espada25=Bladex.CreateEntity("barbEspada25","Hacha",0,0,0,"Weapon")
escudo25=Bladex.CreateEntity("barbEscudo25","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo25")
Breakings.SetBreakableWS("barbEscudo25")
Breakings.SetBreakableWS("barbEspada25")

pers=Bladex.CreateEntity("25ZM","Lich",-38909.8332441, -30018.8368523, 147120.583789,"Person")
pers.Angle=0.159018356021
pers.Level=0
Actions.TakeObject(pers.Name,"barbEspada25")
Actions.TakeObject(pers.Name,"barbEscudo25")
pers.ActionAreaMin=pow(2,1)
pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


###en la zona de las bolas

#1
Espada21=Bladex.CreateEntity("barbEspada26","Hacha",0,0,0,"Weapon")
escudo21=Bladex.CreateEntity("barbEscudo26","Escudo5",0,0,0)
Sparks.MakeShield("barbEscudo26")
Breakings.SetBreakableWS("barbEscudo26")
Breakings.SetBreakableWS("barbEspada26")

pers=Bladex.CreateEntity("26ZM","Skeleton",30000, -47500, 159000,"Person")
pers.Angle=3.14
pers.Level=2
Actions.TakeObject(pers.Name,"barbEspada26")
Actions.TakeObject(pers.Name,"barbEscudo26")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("26ZM")

darfuncs. EnterSecEvent(28000, -48000, 148000,SKELRO)

#---ARANIAS EN LAS GRUTAS


#----PRIMER GRUPO
#1
pers=Bladex.CreateEntity("1SPD","Spidersmall",-14500,-8000,-81000,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
pers=Bladex.CreateEntity("2SPD","Spidersmall",-17000,-8000,-93000,"Person")
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#----SEGUNDO GRUPO
#1
pers=Bladex.CreateEntity("3SPD","Spidersmall",4000,-10200,-98500,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,1)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
pers=Bladex.CreateEntity("4SPD","Spidersmall",-6000,-11200,-106500,"Person")
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,1)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#3
pers=Bladex.CreateEntity("5SPD","Spidersmall",-20000,-13200,-117500,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,1)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#4
pers=Bladex.CreateEntity("6SPD","Spidersmall",-20500,-15000,-125500,"Person")
pers.Level=1
pers.Angle=1.49589570635
#pers.ActionAreaMin=pow(2,1)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#----TERCER GRUPO
#1
pers=Bladex.CreateEntity("7SPD","Spidersmall",-38000,-16000,-102000,"Person")
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
pers=Bladex.CreateEntity("8SPD","Spidersmall",-47500,-16000,-106000,"Person")
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#-------ARANIAS EN SOTANO DE LA CASA
"""
#1
pers=Bladex.CreateEntity("9SPD","Spidersmall",-167500,-10000,203500,"Person")
pers.Angle=3.5
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""
#2
pers=Bladex.CreateEntity("10SPD","Spidersmall",-162500,-9800,206500,"Person")
pers.Angle=3
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#3
pers=Bladex.CreateEntity("11SPD","Spidersmall",-160000,-10000,209000,"Person")
pers.Angle=3
pers.Level=1
pers.Angle=1.49589570635
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#4
pers=Bladex.CreateEntity("12SPD","Spidersmall",-170500,-10000,205000,"Person")
pers.Angle=3
pers.Level=0
pers.Angle=1.49589570635
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


