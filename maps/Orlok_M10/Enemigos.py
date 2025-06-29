##///
##||| ORLOK_M10/Enemigos.PY TITANIUM
##||| Change list:
##||| * OrkController 
##||| * Now spawns actual snow trolls
##\\\ 


import Bladex
import EnemyTypes
import Sparks
import Actions
import math
import Breakings
import LevelFuncs
import pocimac

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
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


#############################
### Orcos en sendero exterior
#############################


# Orco encrucijada. Sin AA.

arma=Bladex.CreateEntity("OrlokArmaOrcoEncrucijada", "Hacha4", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoOrcoEncrucijada","Escudo1", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokOrcoEncrucijada", Orkk, -43000, -31500, -21500, "Person")
enemigo.Angle=0.0
enemigo.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()


# Orco balcon. Areas 5 y 6

arma=Bladex.CreateEntity("OrlokArmaOrcoBalcon", "Maza2", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoBalcon", Orkk, -21500, -31500, 8000, "Person")
enemigo.Angle=3.14159/2.0
enemigo.Level=lvl_control.GiveLevel(7,13)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,4)
enemigo.ActionAreaMax=math.pow(2,5)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()


# Orco en el tunel hacia la fortaleza. Areas 25 y 26

arma=Bladex.CreateEntity("OrlokArmaOrcoTunel", "Martillo", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoTunel", Orkk, 2500, -33500, 31000, "Person")
enemigo.Angle=0.0
enemigo.Level=lvl_control.GiveLevel(6,12)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,24)
enemigo.ActionAreaMax=math.pow(2,25)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()

#enemigo.AddBayPoint=2500, -33500, 31000
#enemigo.AddBayPoint=500, -33500, 40000
#enemigo.AddBayPoint=2500, -33500, 31000
#enemigo.AddBayPoint=4500, -33500, 25500
#enemigo.AddBayPoint=5000, -33500, 19500
#enemigo.AddBayPoint=4500, -33500, 25500



#######################################
## Orcos en los accesos al primer valle
#######################################


# Orco en la torre natural que da al desfiladero. Areas 7 y 8

arma=Bladex.CreateEntity("OrlokArmaOrcoTorreNat", "Hacha3", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoTorreNat", "Ork", -38055, -46009, -22026, "Person")
enemigo.Angle=0.0
enemigo.Level=lvl_control.GiveLevel(8,13)
Actions.TakeObject(enemigo.Name, arma.Name)

inv=enemigo.GetInventory()
arco=Bladex.CreateEntity("OrlokArcoOrcoTorreNat","Arco",0,0,0,"Weapon")
carcaj=Bladex.CreateEntity("OrlokCarcajOrcoTorreNat","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(arco)
ItemTypes.ItemDefaultFuncs(carcaj)
inv.AddBow(arco.Name)
inv.AddQuiver(carcaj.Name)
carcaj.Data.ArrowsLeft=10

enemigo.ActionAreaMin=math.pow(2,6)
enemigo.ActionAreaMax=math.pow(2,7)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()


# Orco en zona elevada a la izquierda de la garganta estrecha. Areas 9 y 10

arma=Bladex.CreateEntity("OrlokArmaOrcoGargantaIzq", "Martillo", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoOrcoGargantaIzq","Escudo1", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokOrcoGargantaIzq", Orkk, -76500, -35500, -32500, "Person")
enemigo.Angle=3.14159/2.0
enemigo.Level=lvl_control.GiveLevel(8,13)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
enemigo.ActionAreaMin=math.pow(2,8)
enemigo.ActionAreaMax=math.pow(2,9)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Position=-64000, -36500, -32000
enemigo.SetOnFloor()


# Orco cercano al balcon exterior. Areas 11 y 12

arma=Bladex.CreateEntity("OrlokArmaOrcoCercaBalcon", "Maza2", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoCercaBalcon", Orkk, -27000, -35500, 12000, "Person")
enemigo.Angle=3.14159/2.0
enemigo.Level=lvl_control.GiveLevel(7,12)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,10)
enemigo.ActionAreaMax=math.pow(2,11)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Data.goto_limit2aa=0
enemigo.SetOnFloor()

#enemigo.AddBayPoint=-27000, -35500, 12000
#enemigo.AddBayPoint=-29000, -35500, 15500
#enemigo.AddBayPoint=-29500, -35000, 19000
#enemigo.AddBayPoint=-35000, -34500, 19000
#enemigo.AddBayPoint=-37500, -34000, 13500
#enemigo.AddBayPoint=-42000, -33500, 10500
#enemigo.AddBayPoint=-42500, -33000, 4500
#enemigo.AddBayPoint=-45000, -32500, -500
#enemigo.AddBayPoint=-42500, -33000, 4500
#enemigo.AddBayPoint=-42000, -33500, 10500
#enemigo.AddBayPoint=-37500, -34000, 13500
#enemigo.AddBayPoint=-35000, -34500, 19000
#enemigo.AddBayPoint=-29500, -35000, 19000
#enemigo.AddBayPoint=-29000, -35500, 15500



#########################################
## Enemigos emboscando en el primer valle
#########################################


# Orco emboscando cerca de la entrada del valle1. Areas 11 y 12

o=Bladex.CreateEntity("SaquitoOrcEntValle","Saquito",0,0,0,"Physic")
o.Solid=0
o.Scale=1.2
pocimac.CreatePotion("SaquitoOrcEntValle")

arma=Bladex.CreateEntity("OrlokArmaOrco1EmbValle1", "Orksword", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrco1EmbValle1", Orkk, -85124, -32576, -1045, "Person")
enemigo.Angle=4.2037
enemigo.Level=lvl_control.GiveLevel(7,13)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, "SaquitoOrcEntValle")
enemigo.ActionAreaMin=math.pow(2,10)
enemigo.ActionAreaMax=math.pow(2,11)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Data.goto_limit2aa=0
enemigo.SetOnFloor()


# Orco emboscando cerca del final del valle1. Areas 11 y 12

arma=Bladex.CreateEntity("OrlokArmaOrco2EmbValle1", "Martillo", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrco2EmbValle1", Orkk, -49536, -32090, -18651, "Person")
enemigo.Angle=0.6291
enemigo.Level=lvl_control.GiveLevel(9,13)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,10)
enemigo.ActionAreaMax=math.pow(2,11)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Data.goto_limit2aa=0
enemigo.SetOnFloor()


# Orco en zona elevada a la derecha de la garganta estrecha. Areas 15 y 16

arma=Bladex.CreateEntity("OrlokArmaOrcoGargantaDer", "Hacha4", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoGargantaDer", "Ork", -65500, -36500, -17500, "Person")
enemigo.Angle=0.0
enemigo.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(enemigo.Name, arma.Name)

inv=enemigo.GetInventory()
arco=Bladex.CreateEntity("OrlokArcoOrcoGargantaDer","Arco",0,0,0,"Weapon")
carcaj=Bladex.CreateEntity("OrlokCarcajOrcoGargantaDer","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(arco)
ItemTypes.ItemDefaultFuncs(carcaj)
inv.AddBow(arco.Name)
inv.AddQuiver(carcaj.Name)
carcaj.Data.ArrowsLeft=10

enemigo.ActionAreaMin=math.pow(2,14)
enemigo.ActionAreaMax=math.pow(2,15)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()


# Troll en el centro del valle1. Areas 11 y 12

arma=Bladex.CreateEntity("OrlokArmaTrollValle1", "Hachacarnicero", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokTrollValle1", "Troll_snow", -57058, -32500, -6359, "Person")
enemigo.Angle=5.2221
enemigo.Level=lvl_control.GiveLevel(5,10)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,10)
enemigo.ActionAreaMax=math.pow(2,11)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()
enemigo.InitPos=-75300, -34750, 1000.0 # -50250, -32500, -17250



##########################################
## Enemigos emboscando en el segundo valle
##########################################


# Orco a la derecha de la entrada del valle2. Areas 3 y 4

arma=Bladex.CreateEntity("OrlokArmaOrcoValle2", "Martillo", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoOrcoValle2","Escudo2", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokOrcoValle2", Orkk, -46033, -35544, 27000, "Person") # 25484, "Person")
enemigo.Angle=3.14159/2.0 # 0.2683
enemigo.Level=lvl_control.GiveLevel(9,13)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
enemigo.ActionAreaMin=math.pow(2,2)
enemigo.ActionAreaMax=math.pow(2,3)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()


# Troll a la izquierda de la entrada del valle2. Areas 3 y 4

arma=Bladex.CreateEntity("OrlokArmaTrollValle2", "Hachacarnicero", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokTrollValle2", "Troll_snow", -72002, -35059, 31203, "Person")
enemigo.Angle=5.4040
enemigo.Level=lvl_control.GiveLevel(6,11)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,2)
enemigo.ActionAreaMax=math.pow(2,3)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()




#############################
### Orcos en el laberinto
#############################


# Jefe Orco zona derecha. Areas 17 y 18

arma=Bladex.CreateEntity("OrlokArmaJefeOrcoLabDer", "Martillo2", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoJefeOrcoLabDer","Escudo9", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokJefeOrcoLabDer", "Great_Ork", -14000, -33300, 62000, "Person")
enemigo.Angle=3.14159
enemigo.Level=lvl_control.GiveLevel(10,13)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
enemigo.ActionAreaMin=math.pow(2,16)
enemigo.ActionAreaMax=math.pow(2,17)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()

#enemigo.AddBayPoint=-14000, -33300, 62000
#enemigo.AddBayPoint=-13000, -34500, 56500
#enemigo.AddBayPoint=-16250, -34500, 53000
#enemigo.AddBayPoint=-28750, -35700, 58000
#enemigo.AddBayPoint=-16250, -34500, 53000
#enemigo.AddBayPoint=-13000, -34500, 56500
#enemigo.AddBayPoint=-14000, -33300, 62000
#enemigo.AddBayPoint=-18000, -33300, 75000


# Jefe Orco zona izquierda. Areas 17 y 18

arma=Bladex.CreateEntity("OrlokArmaJefeOrcoLabIzq", "Martillo", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoJefeOrcoLabIzq","Escudo9", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokJefeOrcoLabIzq", "Great_Ork", -39000, -36900, 64000, "Person")
enemigo.Angle=3.14159
enemigo.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
enemigo.ActionAreaMin=math.pow(2,16)
enemigo.ActionAreaMax=math.pow(2,17)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()

#enemigo.AddBayPoint=-39000, -36900, 64000
#enemigo.AddBayPoint=-38500, -36900, 57500
#enemigo.AddBayPoint=-35000, -36900, 55500
#enemigo.AddBayPoint=-38500, -36900, 57500
#enemigo.AddBayPoint=-39000, -36900, 64000
#enemigo.AddBayPoint=-38500, -36900, 72500
#enemigo.AddBayPoint=-35000, -36900, 73750



#################################
### Orcos en la fortificacion
#################################


# Orco en tejado norte. Areas 21 y 22

arma=Bladex.CreateEntity("OrlokArmaOrcoTejadoNorte", "Hacha3", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoTejadoNorte", Orkk, 19000, -46000, 75500, "Person")
enemigo.Angle=3.14159
enemigo.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(enemigo.Name, arma.Name)

inv=enemigo.GetInventory()
arco=Bladex.CreateEntity("OrlokArcoOrcoTejadoNorte","Arco",0,0,0,"Weapon")
carcaj=Bladex.CreateEntity("OrlokCarcajOrcoTejadoNorte","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(arco)
ItemTypes.ItemDefaultFuncs(carcaj)
inv.AddBow(arco.Name)
inv.AddQuiver(carcaj.Name)
carcaj.Data.ArrowsLeft=10

enemigo.ActionAreaMin=math.pow(2,20)
enemigo.ActionAreaMax=math.pow(2,21)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Position=31103, -45642, 74505
enemigo.SetOnFloor()


# Orco en tejado sur. Areas 21 y 22

arma=Bladex.CreateEntity("OrlokArmaOrcoTejadoSur", "Hacha4", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokOrcoTejadoSur", Orkk, 31000, -46000, 62500, "Person")
enemigo.Angle=3.14159
enemigo.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(enemigo.Name, arma.Name)

inv=enemigo.GetInventory()
arco=Bladex.CreateEntity("OrlokArcoOrcoTejadoSur","Arco",0,0,0,"Weapon")
carcaj=Bladex.CreateEntity("OrlokCarcajOrcoTejadoSur","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs(arco)
ItemTypes.ItemDefaultFuncs(carcaj)
inv.AddBow(arco.Name)
inv.AddQuiver(carcaj.Name)
carcaj.Data.ArrowsLeft=10

enemigo.ActionAreaMin=math.pow(2,20)
enemigo.ActionAreaMax=math.pow(2,21)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Position=18821, -45992, 61064
enemigo.SetOnFloor()


# Caballero oscuro en patio este. Areas 27 y 28.

arma=Bladex.CreateEntity("OrlokArmaDknPatio", "EgyptSword", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoDknPatio","Escudo4", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokDknPatio", "Dark_Knight", 45000, -34000, 70500, "Person")
enemigo.Angle=3.14159/2.0
enemigo.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
enemigo.ActionAreaMin=math.pow(2,26)
enemigo.ActionAreaMax=math.pow(2,27)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.Position=42000, -34000, 69000
enemigo.SetOnFloor()

#enemigo.AddBayPoint=42000, -34000, 69000
#enemigo.AddBayPoint=36000, -33500, 69000
#enemigo.AddBayPoint=35000, -34000, 75000
#enemigo.AddBayPoint=34500, -34000, 63000
#enemigo.AddBayPoint=36000, -33500, 69000


# Caballero oscuro en piso superior. Areas 29 y 30.

o=Bladex.CreateEntity("Orlok2Pocima200","Pocima200", 0, 0, 0, "Physic")
o.Solid=0
o.Scale=1.2
pocimac.CreatePotion("Orlok2Pocima200")

arma=Bladex.CreateEntity("OrlokArmaDknPiso", "EgyptSword", 0.0, 0.0, 0.0, "Weapon")
escudo=Bladex.CreateEntity("OrlokEscudoDknPiso","Escudo4", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
ItemTypes.ItemDefaultFuncs(escudo)
enemigo=Bladex.CreateEntity("OrlokDknPiso", "Dark_Knight", 8000, -42250, 64750, "Person")
enemigo.Angle=3.14159/2.0
enemigo.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(enemigo.Name, arma.Name)
Actions.TakeObject(enemigo.Name, escudo.Name)
Actions.TakeObject(enemigo.Name, "Orlok2Pocima200")
enemigo.ActionAreaMin=math.pow(2,28)
enemigo.ActionAreaMax=math.pow(2,29)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()
enemigo.Blind=1
enemigo.Deaf=1



######################
## Troll del final
######################


# Troll en la entrada de la cueva. Areas 23 y 24

arma=Bladex.CreateEntity("OrlokArmaTrollFinal", "Hachacarnicero", 0.0, 0.0, 0.0, "Weapon") # "Hachacarnicero", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
enemigo=Bladex.CreateEntity("OrlokTrollFinal", "Troll_snow", 42500, -33500, 141500, "Person")
enemigo.Angle=3.0*3.14159/4.0
enemigo.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(enemigo.Name, arma.Name)
enemigo.ActionAreaMin=math.pow(2,22)
enemigo.ActionAreaMax=math.pow(2,23)
EnemyTypes.EnemyDefaultFuncs(enemigo)
enemigo.SetOnFloor()



### Ultimas areas de accion usadas: 29 y 30





###################################################
## Alteraciones en caliente de algunos enemigos
###################################################


######## Funcion: CambiaArqueroSurFortaleza(sec_index, ent_name)

######## Funcion: CambiaArqueroSurFortaleza(sec_index, ent_name)


entradasecreta=Bladex.GetSector(2750.0, -33000.0, 66000.0)
salidafortaleza=Bladex.GetSector(25000.0, -33000.0, 77250.0)

entradasecreta.OnEnter=CambiaArqueroSurFortaleza
salidafortaleza.OnEnter=CambiaArqueroNorteFortaleza
