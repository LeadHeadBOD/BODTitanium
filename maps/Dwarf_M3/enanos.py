import darfuncs
from math import pow
import EnemyTypes
import AniSound
import Sparks
import Actions
import pocimac
import Scorer
import Bladex
import GameText

"""
Orkswordx1=Bladex.CreateEntity("Gladiusx1","Gladius",0,0,0)
Orkswordx1.Weapon=1
escudo=Bladex.CreateEntity("Escudox1","Escudo1",0,0,0)
Sparks.MakeShield("Escudox1")
Breakings.SetBreakableWS("Escudox1")
Breakings.SetBreakableWS("Gladiusx1")

pers=Bladex.CreateEntity("x1ORC","Ork",127096.43323, 5058.34872344, -89314.9678645)
pers.Person=1
pers.Angle=3
Actions.TakeObject(pers.Name,"Gladiusx1")
Actions.TakeObject(pers.Name,"Escudox1")
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
AniSound.AsignarSonidosOrco('x1ORC')
"""

darfuncs.MuertoyTroceado(109552.221511, 5983.35108641, -22875.7557749,"Enano2","",(1,7))
darfuncs.MuertoyTroceado(111073.648725, 5983.62461273, -37665.0801836,"Enano1","",(4,),0)
darfuncs.MuertoyTroceado(106491.067361, 5966.79911185, -23676.371382,"Ork","Hacha",(5,3))
darfuncs.MuertoyTroceado(116529.360884, 5969.88022067, -16772.3161455,"Enano2","",(4,))
darfuncs.MuertoyTroceado(102711.596507, 4619.18290938, -3925.59748387,"Enano2","Hacha",(7,))
darfuncs.MuertoyTroceado(92945.6584756, 4482.22221771, -4373.39763018,"Enano1","",(7,6))
darfuncs.MuertoyTroceado(96391.3798269, 4481.90476733, -52081.9143014,"Ork","",(8,),0)
darfuncs.MuertoyTroceado(101472.507155, 4911.89348965, -48208.5299767,"Enano2","Hacha",(3,))
darfuncs.MuertoyTroceado(90608.9675742, 3283.59541105, -19183.1578147,"Enano1","",(2,))
darfuncs.MuertoyTroceado(116364.72046, 5983.61502442, -31035.81042,"Enano1","Hacha",(2,))
darfuncs.MuertoyTroceado(107163.957337, 5981.42025684, -29476.6655148,"Enano2","",(2,))
darfuncs.MuertoyTroceado(106224.650377, 5983.62243726, -18107.271705,"Enano1","Hacha",(8,))

#tras la puerta de la sala octogonal
darfuncs.MuertoyTroceado(-4614.14513914, -1137.2503592, -37914.3478464,"Ork","",(8,),2.39)

#al lado de una fogata
darfuncs.MuertoyTroceado(-80619.1157453, -10289.7752132, -56257.3758936,"Enano2","",(8,1),5.45)

#donde se encuentra el troll
darfuncs.MuertoyTroceado(-31088.939183, -9324.73043295, -57609.4541473,"Enano1","",(7,6),4.7)

#en sala lateral al otro lado de la grieta
darfuncs.MuertoyTroceado(-48966.728733, -9637.82753813, 18715.0114232,"Enano2","",(7,6),3.6)

#Antes de entrar en la sala grande
darfuncs.MuertoyTroceado(-191070.451935, -14868.9702958, 25786.2195794,"Enano2","",(7,6,1),1.8)

#detras del trono
#darfuncs.MuertoyTroceado(-221697.692672, -20086.5083376, 77574.6923486,"Enano2","",(7,6,1),4.2)

#Entrada a la gruta por debajo
#darfuncs.MuertoyTroceado(-134634.254636, -1596.56186421, -31861.3358323,"Enano2","",(7,6,1),0.6)



SEscenaMasacre = Bladex.GetSector(117718, 6665, -26740)
SEscenaMasacre.OnEnter = CaMasacre1