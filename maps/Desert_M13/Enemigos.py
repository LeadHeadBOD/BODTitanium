##///
##||| DESERT_M13/Enemigos.PY TITANIUM
##||| Change list:
##||| * OrkController 
##||| * Renamed the orc archer's potion to "desertPotion10" to resolve naming conflict in Volcano_M14
##\\\ 

from math import pow
import EnemyTypes
import AniSound
import Sparks
import Actions
import pocimac
import darfuncs
import ItemTypes
import darfuncs
import Ontake
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 9
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)
# e.g. to give an enemy a level between 0 and 4, do
# pers.Level= lvl_control.GiveLevel(0, 4)
#

### Orc controller
import OrkController
darkOrk_thresh = 14
goldOrk_thresh = 17
Orkk = OrkController.MinorOrk(darkOrk_thresh,goldOrk_thresh)
#

#------------------ORCOs-EN-ACANTILADO-----------------------


## orcos guardianes en el campo antes de entrada ciudad

#2

Inicio0 = darfuncs.E_Grup()
Inicio0.OnDeath = TerminanLasMuertes0

Inicio00 = darfuncs.E_Grup()
Inicio00.OnDeath = TerminanLasMuertes00


sectx0=Bladex.GetSector(-4799.2870635, 5667.08007634, -120404.738238)
sectx0.OnEnter=x0


pers=Bladex.CreateEntity("2ORC","Ork",-37222.5742862, 4934.56398566, -84290.6570156,"Person")
pers.Level=lvl_control.GiveLevel(7,10)
pers.Angle=4.39368937234
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada2","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO2","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "exterior")

Inicio0.AddGuy(pers.Name)

#2b


pers=Bladex.CreateEntity("2ORCb","Ork",-21923.220845, 5193.59204386, -86733.4496534,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=1.81921250903
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada2b","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo2b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO2b","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "exterior")



#####################################################################
## orcos que aparecen de pronto en entrada ciudad

sectx1=Bladex.GetSector(-27542.7933369, 4898.75161701, -91045.6475224)
sectx1.OnEnter=x1


#1

pers=Bladex.CreateEntity("3ORC","Ork",-20221.2363631, -771.641397918, -49664.5013583,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=1.74689462183
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada3","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO3","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "exterior")

Inicio00.AddGuy(pers.Name)

#2 -arkero-

pers=Bladex.CreateEntity("DesertArq1", "Ork",-27950.5493517, -767.011749857, -45995.8917589,"Person")
pers.Angle=4.73068197246
pers.Level=lvl_control.GiveLevel(4,9)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada1","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow1","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver1","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio0.AddGuy(pers.Name)



## orcos contingentes con 2 orcos anteriores en entrada a recinto


#1


pers=Bladex.CreateEntity("4ORC","Great_Ork",-3454.16070973, -2015.83978532, -20498.6271907,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=3.14077725778
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada4","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo4","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio")

darfuncs.HideBadGuy(pers.Name)

#2
pers=Bladex.CreateEntity("5ORC",Orkk,-36787.1052496, -777.200432438, -20832.5365265,"Person")
pers.Level=lvl_control.GiveLevel(7,10)
pers.Angle=3.21912063589
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada5","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo5","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio")

Inicio00.AddGuy(pers.Name)
darfuncs.HideBadGuy(pers.Name)



#########################################33
#orcos guardianes del templo


Inicio1 = darfuncs.E_Grup()
Inicio1.OnDeath = TerminanLasMuertes1

#1
pers=Bladex.CreateEntity("7ORC",Orkk,-19732.5665272, -1453.40184242, 11955.5111569,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=3.05462300575
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada7","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name, sword.Name)

shield=Bladex.CreateEntity("DesertEscudo7","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name, shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio")
Inicio1.AddGuy(pers.Name)
darfuncs.HideBadGuy(pers.Name)

#2
pers=Bladex.CreateEntity("8ORC",Orkk,-35263.4878865, -1432.63029026, 11069.4346971,"Person")
pers.Level=lvl_control.GiveLevel(10,13)
pers.Angle=2.68331217078
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada8","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name, sword.Name)

shield=Bladex.CreateEntity("DesertEscudo8","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name, shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("8ORC", "inicio")
Inicio1.AddGuy(pers.Name)
darfuncs.HideBadGuy(pers.Name)





################################################################################
# arkeros en pasarelas centrales





#1
pers=Bladex.CreateEntity("DesertArq2", "Ork",-13530.565803, -8107.46663935, -8802.24925958,"Person")
pers.Angle=6.24948223573
pers.Level=lvl_control.GiveLevel(6,9)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

potion=Bladex.CreateEntity("PotionO5","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada2","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow2","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver2","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (quiver)
Actions.TakeObject(pers.Name,quiver.Name)
quiver.Data.SetNumberOfArrows(10, pers.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#1b


pers=Bladex.CreateEntity("DesertArq2b", "Ork",-889.017192829, -8113.19196499, -15643.2794861,"Person")
pers.Angle=2.74242186295
pers.Level=lvl_control.GiveLevel(10,13)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

potion=Bladex.CreateEntity("PotionO5b","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada2b","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow2b","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver2b","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (quiver)
Actions.TakeObject(pers.Name,quiver.Name)
quiver.Data.SetNumberOfArrows(10, pers.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2


pers=Bladex.CreateEntity("DesertArq3", "Ork",-36335.1829773, -7072.27455836, -15633.2890761,"Person")
pers.Angle=3.22523156378
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

potion=Bladex.CreateEntity("PotionO6","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada3","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver3","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2b


pers=Bladex.CreateEntity("DesertArq3b", "Ork",-34939.6267962, -7050.67847367, -8594.26924104,"Person")
pers.Angle=0.123545991743
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada3b","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow3b","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver3b","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)













################################################################################
# orkos eskondidos y kontingentes kon 2 orkos guardianes.

#1	en el altar del agua	CUANDO SALE????? cuando matas a los 2 guardianes
pers=Bladex.CreateEntity("9ORC",Orkk,-58584.1242899, -3509.0985666, 33369.3031919,"Person")
pers.Level=lvl_control.GiveLevel(7,12)
pers.Angle=4.71989783399
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada9","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo9","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO7","Pocima100",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio")
darfuncs.HideBadGuy(pers.Name)


#2	en el altar del agua
pers=Bladex.CreateEntity("10ORC","Great_Ork",-5717.86848192, -3809.7686689, 33998.2434446,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=4.70544031985
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada10","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo10","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO8","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio")
darfuncs.HideBadGuy(pers.Name)


##########################################################################
##super-GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM--GOLEM-delaTablilla


#pers=Bladex.CreateEntity("Golem5","Golem_stone",-25467.2888614, -4131.02396932, 131965.848519,"Person")
pers=Bladex.CreateEntity("Golem5","Golem_stone",2288.70756943, -4024.19400691, 123186.180818,"Person")
pers.Level=lvl_control.GiveLevel(5,9)
#pers.Angle=3.11947077573
pers.Angle=1.5
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

EnemyTypes.EnemyDefaultFuncs(pers)


#########################################################################
## arkeros tras foso,en patios cercanos a tablilla


#1
pers=Bladex.CreateEntity("DesertArq4", Orkk,-16123.6050603, -4408.33862313, 105925.705493,"Person")
pers.Angle=3.12875338656
pers.Level=lvl_control.GiveLevel(6,9)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada4","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow4","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver4","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#2
pers=Bladex.CreateEntity("DesertArq5", "Ork",12586.3283147, -4417.77752735, 64310.265895,"Person")
pers.Angle=1.74233443926
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada5","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver5","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#3
pers=Bladex.CreateEntity("DesertArq6", Orkk,-36975.6850209, -4421.04486899, 107049.515479,"Person")
pers.Angle=3.95611364461
pers.Level=lvl_control.GiveLevel(6,8)
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada6","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow6","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver6","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#4
pers=Bladex.CreateEntity("DesertArq7", "Ork",-62852.6557232, -4416.86860433, 80164.1583074,"Person")
pers.Angle=3.71540610651
pers.Level=lvl_control.GiveLevel(5,9)
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada7","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver7","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


##############################################################################
## arkeros en pasarelas elevadas


#1
pers=Bladex.CreateEntity("DesertArq8", "Ork",-13095.7861699, -12204.0386411, 88212.86654,"Person")
pers.Angle=3.3386017551
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
pers.SetOnFloor()

potion=Bladex.CreateEntity("PotionO9","Pocima100",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada8","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow8","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver8","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2
pers=Bladex.CreateEntity("DesertArq9", "Ork",-45598.37513, -13881.5978078, 82647.9367967,"Person")
pers.Angle=4.71721032169
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
pers.SetOnFloor()

potion=Bladex.CreateEntity("desertPotion10","Pocima100",0,0,0,"Physic")     # Renamed	-LeadHead
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada9","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow9","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver9","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



##############################################################################
# orcos en zona inferior exterior antes de tablilla  (2,2) (2,3)

#1
pers=Bladex.CreateEntity("11ORC","Great_Ork",-38507.2235253, -5278.6947666, 68023.6055064,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=0.0592383928054
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada11","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo11","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio2")

#pers.AddBayPoint=-38460.4630094, -5558.1968211, 81042.2322242
#pers.AddBayPoint=-11753.2152575, -5576.12873989, 80887.9837595
#pers.AddBayPoint=-11655.3422639, -5603.97829835, 74266.0197975
#pers.AddBayPoint=-7427.10176261, -5619.28313674, 74418.9198493
#pers.AddBayPoint=-7451.17952752, -5599.40430885, 81769.2552575
#pers.AddBayPoint=-14755.6647123, -5603.75020418, 83057.7923861
#pers.AddBayPoint=-41854.8950919, -5618.68252116, 83140.7013529
#pers.AddBayPoint=-41653.2723777, -5309.19365377, 67853.8943826


#2

pers=Bladex.CreateEntity("12ORC","Great_Ork",-26226.2374605, -5629.62127493, 84667.3920818,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=3.17155973083
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada12","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo12","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("DesertPotion11","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

#Actions.TakeObject(pers.Name,"llave1")

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "inicio2")











########################################################################################
###
### entramos en el "palacio"
###
########################################################################################




##caballeros negros que salen al exterior a investigar que ocurre una vez se ha 
## completado el enigma del agua y el fuego

#1 caballero que se queda en el pórtico

Inicio2 = darfuncs.E_Grup()
Inicio2.OnDeath = TerminanLasMuertes2


pers=Bladex.CreateEntity("13Kngt","Dark_Knight",4548.21254736, -3896.91454302, 14263.0009652,"Person")
pers.Angle=3.17235129913
pers.Level=lvl_control.GiveLevel(6,10)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada13","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo13","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion12","Pocima100",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("13Kngt", "palacio")
Inicio2.AddGuy(pers.Name)
darfuncs.HideBadGuy("13Kngt")



#2 caballero negro que sale a inspeccionar que ocurre


pers=Bladex.CreateEntity("14Kngt","Dark_Knight",4865.81892316, -3895.44266838, 721.999439499,"Person")
pers.Angle=0.036886509263
pers.Level=lvl_control.GiveLevel(7,11)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada14","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo14","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)


EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "palacio")
darfuncs.HideBadGuy(pers.Name)

pers.Data.nodos=[(4693.59401942, -3440.22538243, 5683.21743856), (-5572.74659191, -1442.20845504, 4952.75196928), (-33890.094155, -1429.40826072, 4083.34971063), (-43968.0080797, -1449.4927567, 9803.36692589), (-44484.6515639, -1446.90999427, 19230.0478325), (-24278.2638091, -2356.94329456, 20555.4851609), (-5686.87329669, -1450.1438723, 19865.0688867), (-5964.47512335, -1432.37499475, 5230.43227446)]
pers.Data.nodo_actual=0



# 3 caballero negro con llave palacio que queda en el interior


pers=Bladex.CreateEntity("14cKngt","Dark_Knight",26605.2507196, -5146.02274542, 7430.06631298,"Person")
pers.Angle=1.61872444876
pers.Level=lvl_control.GiveLevel(6,10)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada14c","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo14c","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,"DesertEscudo14c")
EnemyTypes.EnemyDefaultFuncs(pers)
Actions.TakeObject(pers.Name,"llave1")
pers.Data.JoinGroup(pers.Name, "palacio")
Inicio2.AddGuy(pers.Name)
darfuncs.HideBadGuy(pers.Name)


## ojo, esto activa a los 2 caballeros negros del interior del palacio, una vez 
#se ha abierto la reja y dependiendo de los que hayan muerto antes

sectx6=Bladex.GetSector(14902.3079305, -4149.85542094, 19122.1948543)



## caballeros negros en palacio, contingentes con los anteriores


#1
pers=Bladex.CreateEntity("14aKngt","Dark_Knight",23272.6894803, -4149.75546179, 43738.8168697,"Person")
pers.Angle=1.52849027888
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada14a","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo14a","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "palacio")
darfuncs.HideBadGuy(pers.Name)


#2


pers=Bladex.CreateEntity("14bKngt","Dark_Knight",24521.342166, -5339.26737384, 30919.1154254,"Person")
pers.Angle=3.11447999515
pers.Level=lvl_control.GiveLevel(5,9)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada14b","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo14b","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "palacio")
darfuncs.HideBadGuy(pers.Name)


######################################################################
# caballeros negros arkeros en piso superior (2,6) (2,7)



#1
pers=Bladex.CreateEntity("DesertArq10", "Dark_Knight",4547.45284976, -9956.39000673, -5262.44948645,"Person")
pers.Angle=6.26487245926
pers.Level=lvl_control.GiveLevel(9,11)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

potion=Bladex.CreateEntity("Potion14","Pocima100",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada10","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow10","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver10","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)


#2
pers=Bladex.CreateEntity("DesertArq11", "Dark_Knight",27286.0851628, -10840.2410967, 12840.8865554,"Person")
pers.Angle=1.60295438683
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertArcEspada11","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow11","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver11","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)


sectx4=Bladex.GetSector(35242.7512336, -10879.9991011, 902.300383182)
sectx4.OnEnter=x4


# arkero en el suelo que sale de pronto

pers=Bladex.CreateEntity("DesertArq12", "Ork",-286.160570855, -1445.53955951, 16318.4332057,"Person")
pers.Angle=1.77860910441
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

potion=Bladex.CreateEntity("Potion16","Saquito",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

sword=Bladex.CreateEntity("DesertArcEspada12","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Desertbow12","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Desertquiver12","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)

sectx5=Bladex.GetSector(-1336.84728076, -8095.44214262, -14087.9513155)
sectx5.OnEnter=x5

#######################################################################################
#cabs negros gordos al final zona tonta



#1
pers=Bladex.CreateEntity("16Kngt","Dark_Knight",-24093.6751123, -11054.1020731, -49124.7788813,"Person")
pers.Angle=3.17346404526
pers.Level=lvl_control.GiveLevel(12,13)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada16","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo16","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("desertPotion17","PocimaTodo",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2
pers=Bladex.CreateEntity("16aKngt","Dark_Knight",-23939.4508903, -11032.1073292, -44640.6294825,"Person")
pers.Angle=0.0354724900962
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada16a","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo16a","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#3

sectx10=Bladex.GetSector(-43181.0585686, -10097.2889273, -44541.0063471)
sectx10.OnEnter=x10


pers=Bladex.CreateEntity("16bKngt","Dark_Knight",-26570.3847305, -11007.3164935, -47083.3239399,"Person")
pers.Angle=4.67978043923
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada16b","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo16b","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.nodos=[(720.518232246, -10410.9523945, -46921.8255807), (422.360302004, -12863.2652347, -28245.7725709), (6583.90681609, -13072.2420299, -28662.9845232), (15763.6732399, -12131.3650301, -28545.8835437)]
pers.Data.nodo_actual=0



# Orco gordo al final zona tonta

sectx9=Bladex.GetSector(-53220.0032645, -8318.62289371, -18253.3270968)
sectx9.OnEnter=x9


pers=Bladex.CreateEntity("16bORC","Great_Ork",-48387.1322034, -9601.6439993, -35452.1278571,"Person")
pers.Angle=1.61381181474
pers.Level=lvl_control.GiveLevel(10,13)
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada16b","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo16b","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "palacio")






















##########################################################################################
#### lichs hacia el bastón mágico


#1
pers=Bladex.CreateEntity("17Lich","Lich",24095.0014699, 2182.61029288, 32544.929793,"Person")
pers.Angle=1.27397192325
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada17","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo17","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2
pers=Bladex.CreateEntity("17bLich","Lich",16386.1086893, 2182.59301604, 19862.9657724,"Person")
pers.Angle=6.21116859569
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada17b","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo17b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#3
pers=Bladex.CreateEntity("18Lich","Lich",7057.23541071, 2115.64947738, 51535.1602983,"Person")
pers.Angle=3.17358060353
pers.Level=lvl_control.GiveLevel(9,11)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada18","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo18","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

sectx7=Bladex.GetSector(33749.3854557, -3634.29056026, 51721.8303658)
sectx7.OnEnter=x7


#4
pers=Bladex.CreateEntity("19Lich","Lich",17498.5566077, 2372.48605234, 46572.4834543,"Person")
pers.Angle=3.15688926073
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada19","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo19","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
sectx8=Bladex.GetSector(21471.3448783, 2622.53939436, 43706.9158589)
sectx8.OnEnter=x8


#5
pers=Bladex.CreateEntity("20Lich","Lich",41502.4633908, 1619.74668713, 18891.4938984,"Person")
pers.Angle=1.51531924675
pers.Level=lvl_control.GiveLevel(4,11)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada20","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo20","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#######################
# Lichs zona oscura
#######################


#1
pers=Bladex.CreateEntity("21Lich","Lich",22125.9156273, 5150.65388124, 7857.59995609,"Person")
pers.Angle=4.68323521154
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada21","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo21","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("21Lich")

#2

pers=Bladex.CreateEntity("22Lich","Lich",17585.6455914, 5135.30620681, 10881.3331981,"Person")
pers.Angle=4.59918209644
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada22","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo22","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("22Lich")

#3
pers=Bladex.CreateEntity("23Lich","Lich",1896.05232894, 6383.3583753, 3745.02116717,"Person")
pers.Angle=0.0236477375351
pers.Level=lvl_control.GiveLevel(9,11)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada23","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo23","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("23Lich")


#4
pers=Bladex.CreateEntity("24Lich","Lich",-10410.1342359, 6629.50073045, -3674.23335579,"Person")
pers.Angle=4.8637612114
pers.Level=lvl_control.GiveLevel(10,12)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada24","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo24","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("24Lich")


#5
pers=Bladex.CreateEntity("25Lich","Lich",-17401.1424797, 6645.82073255, -1433.75432276,"Person")
pers.Angle=4.78449849946
pers.Level=lvl_control.GiveLevel(11,13)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada25","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo25","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("25Lich")



darfuncs. EnterSecEvent(41500, 3000, 6250,KreaLichosc)

##################################################

###	GOLEM DE LA LLAVE
pers=Bladex.CreateEntity("keyGLM","Golem_stone",-24126.1636409, -2123.98027515, -29847.3734306,"Person")
pers.Angle=0
pers.Level=lvl_control.GiveLevel(5,10)
pers.SetOnFloor()

o=Bladex.CreateEntity("estatuaG","EstatuaGolem",-24107.053334,-1552.146332,-30534.104175)
o.Scale=1.000000
o.Orientation=0.006171,0.006171,0.707080,-0.707080
Sparks.SetSparkling("estatuaG")

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)

Ontake.AddOnTakeEvent("llave4",	CambiazoGolem)


eg = darfuncs.E_Grup()
eg.AddGuy(pers.Name)
eg.OnDeath = MuereElGolemMaldito


###########################################################################################
#
#caballeros dentro del templo
#
###########################################################################################


#1 este protege la gema


pers=Bladex.CreateEntity("26Kngt","Dark_Knight",-25353.5482788, -12118.0134218, 31290.0762053,"Person")
pers.Angle=3.17346404526
pers.Level=lvl_control.GiveLevel(12,14)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada26","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo26","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion18","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)

#2

pers=Bladex.CreateEntity("27Kngt","Dark_Knight",-15151.4866188, -5622.77958668, 73395.6582661,"Person")
pers.Angle=3.12867245201
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada27","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo27","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)


#3

pers=Bladex.CreateEntity("28Kngt","Dark_Knight",-15354.2173807, -4368.24645784, 66638.313732,"Person")
pers.Angle=3.19070034873
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada28","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo28","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion19","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)


#4


pers=Bladex.CreateEntity("29Kngt","Dark_Knight",-33183.6106876, -8864.68576553, 74456.3324607,"Person")
pers.Angle=4.66317702746
pers.Level=lvl_control.GiveLevel(5,9)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

sword=Bladex.CreateEntity("DesertEspada29","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("DesertEscudo29","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion20","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)


GrupoDKGT=darfuncs.E_Grup()
GrupoDKGT.OnDeath =finGrupoDKGT
GrupoDKGT.AddGuy("26Kngt")
GrupoDKGT.AddGuy("27Kngt")
GrupoDKGT.AddGuy("28Kngt")
GrupoDKGT.AddGuy("29Kngt")