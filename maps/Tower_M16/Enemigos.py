##///
##||| Tower_M16/Enemigos.PY TITANIUM
##||| Change list:
##||| * OrkController 
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


### Orc controller
import OrkController
darkOrk_thresh = 16
goldOrk_thresh = 18
Orkk = OrkController.MinorOrk(darkOrk_thresh,goldOrk_thresh)
###


#################################################################
###		ORCOS EN LA EMBOSCADA		###

#1
pers=Bladex.CreateEntity("1ORC",Orkk,-3451.3, -3818.7, -19207.8,"Person")
pers.Level=16
pers.Angle=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada1","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("1ORC")




#2
pers=Bladex.CreateEntity("2ORC",Orkk,-11588.7, -3814.4, -20115.2,"Person")
pers.Level=16
pers.Angle=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada2","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("2ORC")


#3
pers=Bladex.CreateEntity("3ORC",Orkk,-18777.6, -3813.4, -20115.1,"Person")
pers.Level=16
pers.Angle=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada3","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("3ORC")
#emboscada.AddGuy("3ORC")

#4
pers=Bladex.CreateEntity("4ORC","Great_Ork",-14351.4, -3816.7, -17888.3,"Person")
pers.Level=17
pers.Angle=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada4","Hacha2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo4","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("4ORC")
#emboscada.AddGuy("4ORC")

#################################################
###
###arquero delante del puente y compagnia
###

pers=Bladex.CreateEntity("5DKGT", "Dark_Knight",62242.97, -4542.61, 19673.757,"Person")
pers.Angle=0.24
pers.Level=14
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada5","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("towerbow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver5","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("5DKGT")


#2
pers=Bladex.CreateEntity("6DKGT","Dark_Knight",66862.43, -2812.68, 14289.039,"Person")
pers.Angle=5.5
pers.Level=15
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada6","DoubleSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo6","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion20","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("6DKGT")


#################################################
###
###	ARQUEROS SOBRE LA SALA DEL GOLEM11
###
#################################################

#1
#pers=Bladex.CreateEntity("7DKGT", "Dark_Knight",-513.1, -12117.0, 9540.1,"Person")
#pers.Angle=1.5
#pers.Level=10
#pers.ActionAreaMin=pow(2,2)
#pers.ActionAreaMax=pow(2,3)
#pers.SetOnFloor()

#bow=Bladex.CreateEntity("towerbow7","Arco",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs(bow)
#Actions.TakeObject(pers.Name,bow.Name)

#quiver=Bladex.CreateEntity("towerquiver7","CarcajEnvenenado",0,0,0,"Physic")
#ItemTypes.ItemDefaultFuncs (quiver)
#quiver.Data.SetNumberOfArrows(10, pers.Name)
#Actions.TakeObject(pers.Name,quiver.Name)
#EnemyTypes.EnemyDefaultFuncs(pers)

#darfuncs.HideBadGuy("7DKGT")

#2
pers=Bladex.CreateEntity("8DKGT", "Dark_Knight",-22704.3, -12866.9, 578.5,"Person")
pers.Angle=4.9
pers.Level=11
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow8","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver8","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("8DKGT")


#3
pers=Bladex.CreateEntity("9DKGT", "Dark_Knight",-22751.32, -12870.58, 17717.65,"Person")
pers.Angle=4.3
pers.Level=9
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow9","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver9","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("9DKGT")


###################################################################
###		ESQUELETOS CALENTITOS  EN ZONA OSCURA		###

#1
pers=Bladex.CreateEntity("11HSKL","Skeleton",-11888.224, -32054.219, 26496.495,"Person")
pers.Level=15
pers.Angle=3
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada11","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo11","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("11HSKL")
#Skelsector1.AddGuy("11HSKL")

#2
pers=Bladex.CreateEntity("12HSKL","Skeleton",-10057.23, -32068.38, 25144.026,"Person")
pers.Level=15
pers.Angle=3
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada12","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo12","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("12HSKL")
#Skelsector1.AddGuy("12HSKL")


####segundo grupo
#1
pers=Bladex.CreateEntity("13HSKL","Skeleton",2318.30660746, -32067.1159763, 25902.6665348,"Person")
pers.Level=16
pers.Angle=3
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada13","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo13","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("13HSKL")
#Skelsector2.AddGuy("13HSKL")


#2
pers=Bladex.CreateEntity("14HSKL","Skeleton",5763.23113937, -31989.8796534, 24148.6214838,"Person")
pers.Level=14
pers.Angle=3
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada14","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo14","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("14HSKL")
#Skelsector2.AddGuy("14HSKL")


####tercer grupo
#1
pers=Bladex.CreateEntity("15HSKL","Skeleton",8021.15, -33063.19, 8269.34,"Person")
pers.Level=14
pers.Angle=0
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada15","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo15","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("15HSKL")
#Skelsector2.AddGuy("15HSKL")


#2
pers=Bladex.CreateEntity("16HSKL","Skeleton",5099.60119887, -33048.2238495, 5786.17533459,"Person")
pers.Level=15
pers.Angle=0
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada16","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo16","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("16HSKL")
#Skelsector2.AddGuy("16HSKL")


#####

pers=Bladex.CreateEntity("17HSKL", "Skeleton",5850.04, -35565.8, -5088.5,"Person")
pers.Angle=4.73068197246
pers.Level=13
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada17","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Towerbow17","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Towerquiver17","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

#Inicio0.AddGuy(pers.Name)

darfuncs.HideBadGuy("17HSKL")


#########################################################
##
## orcos delante de la puerta de la escalera
##
#########################################################


#1
pers=Bladex.CreateEntity("18ORC",Orkk,54967.9, 18932.6, 6036.8,"Person")
pers.Level=15
pers.Angle=2
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada18","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo18","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#2
pers=Bladex.CreateEntity("19ORC",Orkk,56008.5, 18933.2, 2149.5,"Person")
pers.Level=14
pers.Angle=0.6
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada19","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo19","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

##############################################
## caballeros en la escalera de caracoll
##############################################

#1
pers=Bladex.CreateEntity("20DKGT","Dark_Knight",71635.1, 17629.7, 3384.1,"Person")
pers.Angle=0.6
pers.Level=14
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada20","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo20","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion2","Pocima200",0,0,0,"Physic")
potion.Scale=1.
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("20DKGT")

#2
pers=Bladex.CreateEntity("21DKGT","Dark_Knight",82222.1, 14631.7, 4929.4,"Person")
pers.Angle=1.66
pers.Level=16
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow21","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver21","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

sword=Bladex.CreateEntity("towerEspada21","Espada",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo21","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion21","Pocima200",0,0,0,"Physic")
potion.Scale=1.
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("21DKGT")

#3
pers=Bladex.CreateEntity("22DKGT","Dark_Knight",78892.0, 7734.9, 7972.1,"Person")
pers.Angle=3
pers.Level=16
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow22","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver22","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

sword=Bladex.CreateEntity("towerEspada22","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo22","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("Potion22","Pocima200",0,0,0,"Physic")
potion.Scale=1.
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("22DKGT")


Grupocaracoll=darfuncs.E_Grup()
Grupocaracoll.OnDeath =finGrupocaracoll
Grupocaracoll.AddGuy("20DKGT")
Grupocaracoll.AddGuy("21DKGT")
Grupocaracoll.AddGuy("22DKGT")

Grupoesc1=darfuncs.E_Grup()
Grupoesc1.OnDeath =finGrupoesc1
Grupoesc1.AddGuy("18ORC")
Grupoesc1.AddGuy("19ORC")


##################################################################
###
###	ESQUELETOS CALENTITOS EN LAS PASARELAS
###
##################################################################

#1
pers=Bladex.CreateEntity("23HSKL", "Skeleton",-26880.7, -55611.4, 2157.4,"Person")
pers.Angle=6
pers.Level=15
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada23","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Towerbow23","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Towerquiver23","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("23HSKL")


#2
pers=Bladex.CreateEntity("24HSKL", "Skeleton",-24033.0, -55345.5, 218.6,"Person")
pers.Angle=1.4
pers.Level=15
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada24","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Towerbow24","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Towerquiver24","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("24HSKL")


#3
pers=Bladex.CreateEntity("25HSKL", "Skeleton",-2270.7, -55345.0, -6943.6,"Person")
pers.Angle=1.4
pers.Level=13
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada25","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Towerbow25","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Towerquiver25","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("25HSKL")


#4
pers=Bladex.CreateEntity("26HSKL", "Skeleton",2016.2, -55349.3, -10574.6,"Person")
pers.Angle=1
pers.Level=13
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada26","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Towerbow26","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Towerquiver26","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("26HSKL")


GrupoMuerte2         = darfuncs.E_Grup()
GrupoMuerte2.OnDeath = finGrupoMuerte2
GrupoMuerte2.AddGuy("23HSKL")
GrupoMuerte2.AddGuy("24HSKL")
GrupoMuerte2.AddGuy("25HSKL")
GrupoMuerte2.AddGuy("26HSKL")

	
darfuncs. EnterSecEvent(-25487.6, -49101.6, 24761.0,Skelpas)




#################################################################
###		ORCOS EN LA HOGUERA	      	###

#1
pers=Bladex.CreateEntity("27ORC",Orkk,59891.8, 14930.7, 64666.4,"Person")
pers.Level=13
pers.Angle=1
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada27","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo27","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#2
pers=Bladex.CreateEntity("28ORC",Orkk,56105.1, 14931.5, 67739.3,"Person")
pers.Level=16
pers.Angle=4.3
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada28","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo28","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#3
pers=Bladex.CreateEntity("29ORC","Great_Ork",59319.5947805, 14933.1429106, 59759.4,"Person")
pers.Level=16
pers.Angle=4.3
#pers.ActionAreaMin=pow(2,4)
#pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("TowerEspada29","Hacha6",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("TowerEscudo29","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



#####################################################################
###
###	ARQUEROS SOBRE POSICION EXTERIOR
###
#####################################################################

#1
pers=Bladex.CreateEntity("30DKGT", "Dark_Knight",25162.7758326, 6889.3247617, 46661.8,"Person")
pers.Angle=4.5
pers.Level=14
pers.ActionAreaMin=pow(2,7)
pers.ActionAreaMax=pow(2,8)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow30","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada30","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo30","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver30","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


#2
pers=Bladex.CreateEntity("31DKGT", "Dark_Knight",-14237.42, 4832.41807314, 43632.4,"Person")
pers.Angle=4.5
pers.Level=15
pers.ActionAreaMin=pow(2,7)
pers.ActionAreaMax=pow(2,8)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow31","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

Actions.TakeObject("31DKGT","llave1")

sword=Bladex.CreateEntity("towerEspada31","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo31","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver31","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint=-14237.42, 4832.41807314, 43632.4
#pers.AddBayPoint=4153.26835396, 5235.04700872, 43129.2
#pers.AddBayPoint=5702.25616972, 5310.61671424, 46531.7
#pers.AddBayPoint=-2103.87063321, 5164.30625272, 47605.9
#pers.AddBayPoint=-12086.8932317, 4927.80204383, 48307.9




#3
pers=Bladex.CreateEntity("32DKGT", "Dark_Knight",36318.0123534, 9426.56567297, 6992.91085368,"Person")
pers.Angle=4.5
pers.Level=14
pers.ActionAreaMin=pow(2,7)
pers.ActionAreaMax=pow(2,8)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow32","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada32","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo32","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver32","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

#################################################################################
###
###	COSITAS EN CLOACAS
###
#################################################################################

#1
pers=Bladex.CreateEntity("1cos","Cos",-42096.2707639, 3866.46340846, -8598.3,"Person")
pers.Angle=1.3
pers.Level=14
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
pers=Bladex.CreateEntity("2cos","Cos",-48549.3240662, -1134.78382294, 20365.4,"Person")
pers.Angle=1.3
pers.Level=10
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#3
pers=Bladex.CreateEntity("3cos","Cos",-42522.5045706, -1135.42008886, 20569.5,"Person")
pers.Angle=3
pers.Level=12
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#4
pers=Bladex.CreateEntity("4cos","Cos",-42131.7890585, 3936.82145423, -5922.3,"Person")
pers.Angle=1.9
pers.Level=14
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#5
pers=Bladex.CreateEntity("5cos","Cos",-43337.465969, -1066.75044541, 20717.7,"Person")
pers.Angle=3
pers.Level=16
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#################################################################################
###
###	ARQUEROS EN LAGO DE ACIDO
###
#################################################################################


#1
pers=Bladex.CreateEntity("33DKGT", "Dark_Knight",-24669.9, 9896.1, 30727.0,"Person")
pers.Angle=4.5
pers.Level=13
pers.ActionAreaMin=pow(2,11)
pers.ActionAreaMax=pow(2,12)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow33","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada33","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo33","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver33","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

#2
pers=Bladex.CreateEntity("33DKGT", "Dark_Knight",-30639.3465824, 9884.58807379, 21219.8,"Person")
pers.Angle=4.5
pers.Level=14
pers.ActionAreaMin=pow(2,11)
pers.ActionAreaMax=pow(2,12)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow33","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada33","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo33","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver33","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

#################################################################################
###
###	ARQUEROS EN LA GALERIA
###
#################################################################################

#1
pers=Bladex.CreateEntity("34DKGT", "Dark_Knight",-11165.4131096, -7065.5545953, 34674.8,"Person")
pers.Angle=3.2
pers.Level=15
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow34","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada34","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo34","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver34","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


#2
pers=Bladex.CreateEntity("35DKGT", "Dark_Knight",-3793.01166117, -7065.25795214, 33836.42,"Person")
pers.Angle=3.2
pers.Level=13
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow35","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

sword=Bladex.CreateEntity("towerEspada35","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo35","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

quiver=Bladex.CreateEntity("towerquiver35","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


#pers.AddBayPoint=-3793.01166117, -7065.25795214, 33836.42
#pers.AddBayPoint=5374.89332774, -7065.06989106, 34069.9
#pers.AddBayPoint=4390.55867954, -7049.79823127, 37086.5
#pers.AddBayPoint=-4526.76764703, -7065.75386954, 36844.4



#################################################################################
###
###	ARQUERO EN el piso roto
###
#################################################################################

#1
pers=Bladex.CreateEntity("36DKGT", "Dark_Knight",1103.0, -18993.2326669, -11121.4,"Person")
#pers=Bladex.CreateEntity("36DKGT", "Dark_Knight",524.862790482, -18968.4063917, -11017.1198835,"Person")
pers.Angle=5.6
pers.Level=10
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow36","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver36","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)


####################################################################################################
##
##	ENEMIGOS EN EL SEGUNDO PISO


## EN LA SALA DE LAS VIDRIERAS ROTAS

##1
pers=Bladex.CreateEntity("37DKGT", "Dark_Knight",15985.9367733, -12067.8133401, 17658.168307,"Person")
pers.Angle=1.8
pers.Level=15
#pers.ActionAreaMin=pow(2,3)
#pers.ActionAreaMax=pow(2,2)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada37","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo37","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("37DKGT")



##2
pers=Bladex.CreateEntity("38DKGT", "Dark_Knight",17930.778706, -12061.4080698, 23506.7250233,"Person")
pers.Angle=2.4
pers.Level=15
#pers.ActionAreaMin=pow(2,3)
#pers.ActionAreaMax=pow(2,2)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada38","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo38","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("38DKGT")


##3 JEFE
pers=Bladex.CreateEntity("39DKGT", "Dark_Knight",-417.171871045, -12052.4842686, 8916.64436201,"Person")
pers.Angle=5.6
pers.Level=12
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada39","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo39","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("39DKGT")


##1 sale por la puerta

pers=Bladex.CreateEntity("40DKGT", "Dark_Knight",-11567.755192, -12347.5600623, -10508.9712379,"Person")
pers.Angle=5
pers.Level=13
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada40","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo40","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("40DKGT")

##1 ESTA DE FRENTE

pers=Bladex.CreateEntity("40bDKGT", "Dark_Knight",-26610.7333914, -12798.8884299, -8409.9,"Person")
pers.Angle=4.9
pers.Level=14
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada40b","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo40b","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("40bDKGT")

Grupoalist1=darfuncs.E_Grup()
Grupoalist1.OnDeath =finGrupoalist1
Grupoalist1.AddGuy("37DKGT")
Grupoalist1.AddGuy("38DKGT")
Grupoalist1.AddGuy("39DKGT")

darfuncs. EnterSecEvent(5963.4, -10302.5, 24537.7,arqueroslistos1)


##2 escondido

pers=Bladex.CreateEntity("41DKGT", "Dark_Knight",-9892.95320236, -12610.7531158, -1636.71038816,"Person")
pers.Angle=2.9
pers.Level=15
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("towerEspada41","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo41","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("41DKGT")


darfuncs. EnterSecEvent(-767.3, -12356.9, -6123.8,arquerocobarde)



kgteros=darfuncs.E_Grup()
kgteros.OnDeath =finGrupokgteros
kgteros.AddGuy("34DKGT")
kgteros.AddGuy("35DKGT")
kgteros.AddGuy("37DKGT")
kgteros.AddGuy("38DKGT")
kgteros.AddGuy("39DKGT")
kgteros.AddGuy("40bDKGT")
kgteros.AddGuy("40DKGT")
kgteros.AddGuy("41DKGT")


###	ARQUERO DISPARANDO A TRAVES DEL SUELO ROTO EN TERCERA PLANTA
#1
pers=Bladex.CreateEntity("42DKGT", "Dark_Knight",-27732.3977254, -19302.829227, 19354.0,"Person")
pers.Angle=3
pers.Level=9
pers.ActionAreaMin=1<<31
pers.ActionAreaMax=1<<31
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow42","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver42","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("42DKGT")

#2 en la cuarta sobre las escaleras
pers=Bladex.CreateEntity("42bDKGT", "Dark_Knight",-1314.92698763, -25309.0608278, 2,"Person")
pers.Angle=1.34
pers.Level=15
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

bow=Bladex.CreateEntity("towerbow42b","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("towerquiver42b","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

sword=Bladex.CreateEntity("towerEspada42b","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("towerEscudo42b","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

darfuncs.HideBadGuy("42bDKGT")


darfuncs. EnterSecEvent(-22161.6693078, -12784.027984, -7318.7,darkk42)


darfuncs. EnterSecEvent(-227.158507458, -19059.0571292, 27869.6,darkko42)


############# 	MINORXO DELANTE DEL ASCENSOR

espada=Bladex.CreateEntity("garroteM43","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("43MINOT","Minotaur",-9698.88217226, -13054.1493545, 22316.7,"Person")
pers.Level=11
pers.Angle=1.1
Actions.TakeObject(pers.Name,"garroteM43")

#pers.ActionAreaMin=pow(2,6)
#pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("43MINOT")


	

darfuncs. EnterSecEvent(-27142.6070934, -12782.3433265, 22200.159509,MINORXO43)