##///
##||| BTOMB_M12/Enemigos.PY TITANIUM
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
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)
# e.g. to give an enemy a level between 0 and 4, do
#pers.Level= lvl_control.GiveLevel(0, 4)
#

### Orc controller
import OrkController
darkOrk_thresh = 13
goldOrk_thresh = 16
Orkk = OrkController.MinorOrk(darkOrk_thresh,goldOrk_thresh)


#------------------INICIO-----------------------

# orco patrullando

o=Bladex.CreateEntity("1ORCPotion","Saquito",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("1ORCPotion")


o=Bladex.CreateEntity("OasisGladius1","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)



pers=Bladex.CreateEntity("1ORC",Orkk,335009.202416, -121.45050209, -204159.588164,"Person")
pers.Angle=1.53233174861
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OasisGladius1")
Actions.TakeObject(pers.Name,"OasisEscudo1")
Actions.TakeObject(pers.Name,"1ORCPotion")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint335009.202416, -121.45050209, -204159.588164
#pers.AddBayPoint318248.307154, -111.20584421, -203991.114075
#pers.AddBayPoint317654.360772, -123.598670316, -194170.981419
#pers.AddBayPoint334280.632759, -133.516481594, -193837.915732



# orco a la izquierda del personaje según entra.


o=Bladex.CreateEntity("2ORCPotion","Saquito",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("2ORCPotion")

o=Bladex.CreateEntity("OasisGladius2","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("2ORC",Orkk,299625.731455, -63.6228910178, -196113.912936,"Person")
pers.Angle=4.78769881001
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius2")
Actions.TakeObject(pers.Name,"OasisEscudo2")
Actions.TakeObject(pers.Name,"2ORCPotion")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

# orco a la derecha del personaje según entra



o=Bladex.CreateEntity("2ORCbPotion","Saquito",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("2ORCbPotion")

o=Bladex.CreateEntity("OasisGladius2b","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo2b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("2ORCb",Orkk,340727.910906, -57.6153028075, -200795.047645,"Person")
pers.Angle=0.0871691173991
pers.Level=lvl_control.GiveLevel(8,10)
Actions.TakeObject(pers.Name,"OasisGladius2b")
Actions.TakeObject(pers.Name,"OasisEscudo2b")
Actions.TakeObject(pers.Name,"2ORCbPotion")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)



# orco mayor con poción frente a gran rastrillo mirando a la izquierda

ambiente2 = darfuncs.E_Grup()
ambiente2.OnDeath = Suenamusica3


o=Bladex.CreateEntity("OasisGladius3","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

#o=Bladex.CreateEntity("3ORCPotion","Pocima200",0,0,0)
#o.Static=0
#o.Solid=1
#o.Scale=1.220190
#pocimac.CreatePotion("3ORCPotion")



pers=Bladex.CreateEntity("3ORC","Great_Ork",324032.472228, -147.947266828, -184498.206818,"Person")
pers.Angle=3.09298621272
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OasisGladius3")
Actions.TakeObject(pers.Name,"OasisEscudo3")
#Actions.TakeObject(pers.Name,"3ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("3ORC")

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = Suenamusica3

## nuevo orco arkero tras baños

pers=Bladex.CreateEntity("OasisArq9", "Ork",379654.783154, 1205.88831235, -207441.222937,"Person")
pers.Angle=6.26509690691
pers.Level=lvl_control.GiveLevel(7,11)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("OasisArqEsp5","Maza",0,0,0,"Weapon")
inv=pers.GetInventory()
inv.AddWeapon("OasisArqEsp5")
ItemTypes.ItemDefaultFuncs(o)

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow9","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow9")

o=Bladex.CreateEntity("Oasisquiver9","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver9")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


#Golem en zona espejo con llave zona inferior

ambiente1 = darfuncs.E_Grup()
ambiente1.OnDeath = Suenamusica2

pers=Bladex.CreateEntity("Golem1","Golem_stone",356074, -229, -190820,"Person")
pers.Angle=6.18429861761
pers.Level=lvl_control.GiveLevel(2,6)
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
Actions.TakeObject(pers.Name,"Llaveorc")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Golem1")

ambiente1.AddGuy(pers.Name)
ambiente1.OnDeath = Suenamusica2

sectx3e=Bladex.GetSector(344000,0,-179000)


sectx3e.OnEnter=x3d




### arqueros en torres zona exterior


##1
pers=Bladex.CreateEntity("OasisArq1", "Ork",384219.758127, -862.908658553, -185335.138321,"Person")
pers.Angle=1.54055305818
pers.Level=lvl_control.GiveLevel(0,2)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow1","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow1")

o=Bladex.CreateEntity("Oasisquiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver1")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint384219.758127, -862.908658553, -185335.138321
#pers.AddBayPoint377626.372375, -865.952438886, -185591.972485
#pers.AddBayPoint377181.528223, -874.068329387, -182126.181158
#pers.AddBayPoint383505.487419, -857.75888654, -181951.703757


## 2

pers=Bladex.CreateEntity("OasisArq2", "Ork",393494.419102, -1879.89468524, -208013.881594,"Person")
pers.Angle=6.27008865442
pers.Level=lvl_control.GiveLevel(0,1)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow2","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow2")

o=Bladex.CreateEntity("Oasisquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver2")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint393494.419102, -1879.89468524, -208013.881594
#pers.AddBayPoint393454.40187, -1855.08214664, -198577.481212
#pers.AddBayPoint395501.07071, -1878.2446502, -198754.875684
#pers.AddBayPoint395243.662914, -1867.60570471, -208124.431609



# orco 1 en escalera exterior-termas

Rigor = darfuncs.E_Grup()
Rigor.OnDeath = TerminanLasMuertes

Rigorbis = darfuncs.E_Grup()
Rigorbis.OnDeath = ParaMusicaCombate


o=Bladex.CreateEntity("OasisGladius4","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)



pers=Bladex.CreateEntity("4ORC",Orkk,386600.035318, 8777.95682392, -216543.902717,"Person")
pers.Angle=6.24809433943
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius4")
Actions.TakeObject(pers.Name,"OasisEscudo4")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigor.AddGuy(pers.Name)
Rigor.OnDeath = TerminanLasMuertes

Rigorbis.AddGuy(pers.Name)
Rigorbis.OnDeath = ParaMusicaCombate

# orco 2 en escalera exterior-termas

o=Bladex.CreateEntity("5ORCPotion","Pocima50",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("5ORCPotion")

o=Bladex.CreateEntity("OasisGladius5","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo5","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("5ORC",Orkk,370581.747452, 3386.72016765, -189018.675363,"Person")
pers.Angle=3.10134627656
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OasisGladius5")
Actions.TakeObject(pers.Name,"OasisEscudo5")
Actions.TakeObject(pers.Name,"5ORCPotion")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigor.AddGuy(pers.Name)
Rigor.OnDeath = TerminanLasMuertes

Rigorbis.AddGuy(pers.Name)
Rigorbis.OnDeath = ParaMusicaCombate

# orco 3 en escalera exterior-termas 


o=Bladex.CreateEntity("OasisGladius6","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo6","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("6ORC","Great_Ork",363116.879263, 8871.76984485, -215378.903236,"Person")
pers.Angle=6.24111899
pers.Level=lvl_control.GiveLevel(5,8)
Actions.TakeObject(pers.Name,"OasisGladius6")
Actions.TakeObject(pers.Name,"OasisEscudo6")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigorbis.AddGuy(pers.Name)
Rigorbis.OnDeath = ParaMusicaCombate


sectxmusica=Bladex.GetSector(386059.794997, 8574.67932135, -209899.3822)
sectxmusica.OnEnter=Musicafondo

sectx3=Bladex.GetSector(368230.495819, 8986.86006937, -211588.522351)


# 2 Orcos contingentes con muerte 2 orcos anteriores

## orco contingente 1

o=Bladex.CreateEntity("OasisGladius7","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo7","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("7ORCPotion","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("7ORCPotion")

pers=Bladex.CreateEntity("7ORC",Orkk,344680.593309, 8943.20442816, -228791.920902,"Person")
pers.Angle=5.64225330099
pers.Level=lvl_control.GiveLevel(5,9)
Actions.TakeObject(pers.Name,"OasisGladius7")
Actions.TakeObject(pers.Name,"OasisEscudo7")
Actions.TakeObject(pers.Name,"7ORCPotion")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigorbis.AddGuy(pers.Name)
Rigorbis.OnDeath = ParaMusicaCombate

darfuncs.HideBadGuy("7ORC")

# orco contingente 2


o=Bladex.CreateEntity("OasisGladius8","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo8","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("8ORC",Orkk,358037.666703, 8938.44851231, -228353.637901,"Person")
pers.Angle=0.0376471243159
pers.Level=lvl_control.GiveLevel(5,12)
Actions.TakeObject(pers.Name,"OasisGladius8")
Actions.TakeObject(pers.Name,"OasisEscudo8")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigorbis.AddGuy(pers.Name)
Rigorbis.OnDeath = ParaMusicaCombate

darfuncs.HideBadGuy("8ORC")








# orco mayor con pocion en ppio plaza inferior


o=Bladex.CreateEntity("OasisGladius13","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo13","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("13ORCPotion","Pocima50",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("13ORCPotion")




pers=Bladex.CreateEntity("13ORC","Great_Ork",388088.073029, 20585.2, -222524.84135,"Person")
pers.Angle=4.73794394835
pers.Level=lvl_control.GiveLevel(4,8)
Actions.TakeObject(pers.Name,"OasisGladius13")
Actions.TakeObject(pers.Name,"OasisEscudo13")
Actions.TakeObject(pers.Name,"13ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#Orco escondido en escaleras hacia plaza inferior

o=Bladex.CreateEntity("OasisGladius13a","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo13a","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("13aORC",Orkk,399222.896689, 19631.1788236, -221593.02086,"Person")
pers.Angle=6.27158304094
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OasisGladius13a")
Actions.TakeObject(pers.Name,"OasisEscudo13a")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.nodos=[(399468.754695, 16641.4029569, -212007.784067), (391715.359919, 14635.8856549, -211772.573006), (391877.136465, 12366.4344377, -220082.50748), (398993.953319, 11128.7523841, -220008.00612)]
pers.Data.nodo_actual=0

sectx3b=Bladex.GetSector(395665.628323, 8864.12865831, -212093.613668)
sectx3b.OnEnter=x3b


# orco 1 en plaza inferior


o=Bladex.CreateEntity("OasisGladius14","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo14","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("14ORCPotion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("14ORCPotion")

pers=Bladex.CreateEntity("14ORC",Orkk,363741.604404, 20921.6003815, -216378.275371,"Person")
pers.Angle=4.72396878742
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OasisGladius14")
Actions.TakeObject(pers.Name,"OasisEscudo14")
Actions.TakeObject(pers.Name,"14ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#pers.AddBayPoint363741.604404, 20921.6003815, -216378.275371
#pers.AddBayPoint383830.031317, 20921.6003815, -216209.058431
#pers.AddBayPoint383857.746416, 20921.6003815, -239734.838961
#pers.AddBayPoint362166.717, 20921.6003815, -240098.563024






# orco 2 en plaza inferior


o=Bladex.CreateEntity("OasisGladius15","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo15","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("15ORCPotion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("15ORCPotion")


pers=Bladex.CreateEntity("15ORC",Orkk,365143.013187, 20921.6003815, -238261.000359,"Person")
pers.Angle=4.76380496077
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius15")
Actions.TakeObject(pers.Name,"OasisEscudo15")
Actions.TakeObject(pers.Name,"15ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#pers.AddBayPoint365143.013187, 20921.6003815, -238261.000359
#pers.AddBayPoint382001.855927, 20921.6003815, -238476.816289
#pers.AddBayPoint381955.437695, 20921.6003815, -217969.900842
#pers.AddBayPoint363995.170661, 20921.6003815, -218122.85826




## orcos en patio 2 junto a gran deposito de agua


ambiente = darfuncs.E_Grup()
ambiente.OnDeath = Suenamusica1


##1

o=Bladex.CreateEntity("17ORCPotion","Pocima50",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("17ORCPotion")

o=Bladex.CreateEntity("OasisGladius17","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo17","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("17ORC","Great_Ork",316115.185692, 9113.69935937, -228983.674906,"Person")
pers.Angle=3.14683759937
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius17")
Actions.TakeObject(pers.Name,"OasisEscudo17")
Actions.TakeObject(pers.Name,"17ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
ambiente.AddGuy(pers.Name)
ambiente.OnDeath = Suenamusica1


pers.Data.nodos=[(316818.567371, 9116.20636122, -234883.922251), (320992.781378, 8856.23273131, -234587.894832)]
pers.Data.nodo_actual=0

darfuncs.EnterSecEvent(330476.411517, 8881.58075597, -234326.00662,x3c)

##2

o=Bladex.CreateEntity("OasisGladius18","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo18","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("18ORC",Orkk,291235.573172, 8845.1156793, -202829.017394,"Person")
pers.Angle=3.12204677198
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OasisGladius18")
Actions.TakeObject(pers.Name,"OasisEscudo18")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
ambiente.AddGuy(pers.Name)
ambiente.OnDeath = Suenamusica1


pers.Data.nodos=[(291333.454543, 9027.06747859, -211499.312125), (309809.958963, 9085.54259113, -214730.518173)]
pers.Data.nodo_actual=0


### orkos arkeros en el susodicho patio

## 1

pers=Bladex.CreateEntity("OasisArq3", "Ork",307053.580111, -567.0911029, -233962.739906,"Person")
pers.Angle=4.83751605331
pers.Level=lvl_control.GiveLevel(0,4)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow3")

o=Bladex.CreateEntity("Oasisquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver3")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("OasisArq3")
#ambiente.AddGuy(pers.Name)
#ambiente.OnDeath = Suenamusica1

##2


pers=Bladex.CreateEntity("OasisArq4", "Ork",292171.929626, 3898.05839141, -217499.005532,"Person")
pers.Angle=4.39630268661
pers.Level=lvl_control.GiveLevel(0,3)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow4","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow4")

o=Bladex.CreateEntity("Oasisquiver4","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver4")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("OasisArq4")

#ambiente.AddGuy(pers.Name)
#ambiente.OnDeath = Suenamusica1


sectx4a=Bladex.GetSector(325558.558581, 8932.1101738, -228232.538031)
sectx4b=Bladex.GetSector(333447.668575, 5131.2547376, -234044.69251)
sectx4a.OnEnter=x4
sectx4b.OnEnter=x4

# orco en escaleras junto a primer rastrillo movil


o=Bladex.CreateEntity("OasisGladius19","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo19","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("19ORC",Orkk,302567.667636, 8774.49925188, -189518.192688,"Person")
pers.Angle=0.0327185160089
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius19")
Actions.TakeObject(pers.Name,"OasisEscudo19")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("19ORC")





































#########
#########
#########
######### SEGUNDA PARTE


## orcos en castillo

ambiente3 = darfuncs.E_Grup()
ambiente3.OnDeath = Suenamusica4

##1

o=Bladex.CreateEntity("Btomb20ORCPotion","PocimaTodo",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("Btomb20ORCPotion")

o=Bladex.CreateEntity("OasisGladius20","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo20","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("20ORC",Orkk,336479.592447, 1449.99521054, -146515.190518,"Person")
pers.Angle=3.21822363318
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"OasisGladius20")
Actions.TakeObject(pers.Name,"OasisEscudo20")
Actions.TakeObject(pers.Name,"Btomb20ORCPotion")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = Suenamusica4

darfuncs.HideBadGuy("20ORC")

pers.Data.nodos=[(336607.105948, 1399.44358596, -157697.311505), (330538.775894, 1386.32341091, -161789.210109), (315918.814958, 1132.49943572, -161387.137703), (316067.092565, -97.8243678511, -171642.948767), (324357.49192, -115.194332666, -172362.661644)]
pers.Data.nodo_actual=0



##2


o=Bladex.CreateEntity("OasisGladius21","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo21","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)




pers=Bladex.CreateEntity("21ORC",Orkk,316615.63721, -67.9546440618, -172977.436971,"Person")
pers.Angle=0.0363564653059
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OasisGladius21")
Actions.TakeObject(pers.Name,"OasisEscudo21")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("21ORC")

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = Suenamusica4

pers.Data.nodos=[(311984.276336, 1449.16068103, -149378.749499), (315395.868533, 1446.82065223, -148702.947393)]
pers.Data.nodo_actual=0


sectx5=Bladex.GetSector(325253.442982, -146.898697828, -177323.272144)

sectx5.OnEnter=x5


#nuevos orcos castillo

#3

o=Bladex.CreateEntity("OasisGladius21b","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo21b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("21ORCb",Orkk,318770.200833, 1632.7507367, -148369.25822,"Person")
pers.Angle=1.62552869979
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OasisGladius21b")
Actions.TakeObject(pers.Name,"OasisEscudo21b")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = Suenamusica4

darfuncs.HideBadGuy("21ORCb")


#4


o=Bladex.CreateEntity("OasisGladius21c","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo21c","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("21ORCcPotion","Pocima200",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("21ORCcPotion")


pers=Bladex.CreateEntity("21ORCc","Great_Ork",326672.240318, -6226.36376284, -161217.252946,"Person")
pers.Angle=4.71433401535
pers.Level=lvl_control.GiveLevel(5,10)
Actions.TakeObject(pers.Name,"OasisGladius21c")
Actions.TakeObject(pers.Name,"OasisEscudo21c")
Actions.TakeObject(pers.Name,"21ORCcPotion")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("21ORCc")





# esqueleto en escaleras a secreto tablilla

o=Bladex.CreateEntity("OasisGladius24","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo24","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("24Esq","Skeleton",358406.367566, 8647.90075036, -127401.931436,"Person")
pers.Angle=2.36915916531
pers.Level=lvl_control.GiveLevel(5,8)

Actions.TakeObject(pers.Name,"OasisGladius24")
Actions.TakeObject(pers.Name,"OasisEscudo24")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)





#esqueleto elevador secreto

o=Bladex.CreateEntity("OasisGladius24a","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo24a","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("24aEsq","Skeleton",341301.062909, 16013.9470555, -134112.133494,"Person")
pers.Angle=5.39255478803
pers.Level=lvl_control.GiveLevel(7,10)

Actions.TakeObject(pers.Name,"OasisGladius24a")
Actions.TakeObject(pers.Name,"OasisEscudo24a")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)








### esqueletos en descenso a puente 

ambiente4 = darfuncs.E_Grup()
ambiente4.OnDeath = Suenamusica5


#esqueleto 1 arkero

pers=Bladex.CreateEntity("OasisArq5", "Skeleton",342299.035203, 13835.2, -114022.158568,"Person")
pers.Angle=0.749448591867
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

o=Bladex.CreateEntity("OasisArqEsp1","Espadaelfica",0,0,0,"Weapon")
inv=pers.GetInventory()
inv.AddWeapon("OasisArqEsp1")
ItemTypes.ItemDefaultFuncs(o)

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow5")

o=Bladex.CreateEntity("Oasisquiver5","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver5")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = Suenamusica5

#esqueleto 1b

sectx9=Bladex.GetSector(359351.582871, 8831.93574174, -112562.092937)
sectx9.OnEnter=x9

o=Bladex.CreateEntity("OasisGladius26b","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo26b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("26bEsq","Skeleton",337031.81686, 14468.1513304, -106238.811408,"Person")
pers.Angle=3.54280464584
pers.Level=lvl_control.GiveLevel(6,11)
Actions.TakeObject(pers.Name,"OasisGladius26b")
Actions.TakeObject(pers.Name,"OasisEscudo26b")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = Suenamusica5


#esqueleto 2


o=Bladex.CreateEntity("OasisGladius27","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo27","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("27Esq","Skeleton",325532.880124, 20952.08174, -91651.0421688,"Person")
pers.Angle=3.27605480189
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OasisGladius27")
Actions.TakeObject(pers.Name,"OasisEscudo27")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#esqueleto 3


o=Bladex.CreateEntity("OasisGladius27b","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo27b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("27bEsq","Skeleton",302906.166536, 24927.2081148, -85756.9325619,"Person")
pers.Angle=4.19252115423
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OasisGladius27b")
Actions.TakeObject(pers.Name,"OasisEscudo27b")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


# Minorx en cueva antes de puente inferior

darfuncs.EnterSecEvent(300168.354732, 36882.6071846, -100926.07645,xtrl1)

#sectxtrl2=Bladex.GetSector(325009.420761, 43881.2253566, -100254.35338)
#sectxtrl2.OnEnter=sectxtrl2

o=Bladex.CreateEntity("Hachacarnicero","Hachacarnicero",0,0,0,"Weapon")

pers=Bladex.CreateEntity("TRL2","Minotaur",325463.629038, 43888.4093986, -125183.886675,"Person")
pers.Angle=6.23028397513
pers.Level=lvl_control.GiveLevel(3,7)
Actions.TakeObject(pers.Name,"Hachacarnicero")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#keleto amigo de minorx

o=Bladex.CreateEntity("OasisGladius27c","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo27c","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("27cEsq","Skeleton",309156.26726, 36929.0354831, -105087.207837,"Person")
pers.Angle=0.210876040789
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius27c")
Actions.TakeObject(pers.Name,"OasisEscudo27c")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)





### esqueletos arkeros en zona tablilla

# esqueleto 1 superior

ambiente5 = darfuncs.E_Grup()
ambiente5.OnDeath = Suenamusica6


pers=Bladex.CreateEntity("OasisArq7", "Skeleton",338129.102245, 2606.42041383, -75994.4793411,"Person")
pers.Angle=0.0
pers.Level=lvl_control.GiveLevel(5,9)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("OasisArqEsp3","Maza2",0,0,0,"Weapon")
inv=pers.GetInventory()
inv.AddWeapon("OasisArqEsp3")
ItemTypes.ItemDefaultFuncs(o)

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow7")

o=Bladex.CreateEntity("Oasisquiver7","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver7")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint338129.102245, 2606.42041383, -75994.4793411
#pers.AddBayPoint338129.102245, 2597.95337208, -40555.7818731
#pers.AddBayPoint335269.332311, 2605.93016331, -40322.5177369
#pers.AddBayPoint335131.85826, 2685.47344956, -74225.0033583

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica6

# esqueleto 2 superior

pers=Bladex.CreateEntity("OasisArq8", "Skeleton",311624.575494, 2619.30112702, -40205.1334844,"Person")
pers.Angle=3.16746457893
pers.Level=lvl_control.GiveLevel(6,10)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("OasisArqEsp4","HookSword",0,0,0,"Weapon")
inv=pers.GetInventory()
inv.AddWeapon("OasisArqEsp4")
ItemTypes.ItemDefaultFuncs(o)

inv=pers.GetInventory()
o=Bladex.CreateEntity("Oasisbow8","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Oasisbow8")

o=Bladex.CreateEntity("Oasisquiver8","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Oasisquiver8")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint311624.575494, 2619.30112702, -40205.1334844
#pers.AddBayPoint311707.5173, 2612.09300339, -74541.6937159
#pers.AddBayPoint314494.520957, 2583.22817056, -74658.8526065
#pers.AddBayPoint314132.464561, 2601.62523194, -40079.6219761

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica6


# esqueleto 3 superior 

o=Bladex.CreateEntity("OasisGladius29","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo29","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("29Esq","Skeleton",324868.91674, 2637.52899212, -34579.8369595,"Person")
pers.Angle=3.07253109006
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OasisGladius29")
Actions.TakeObject(pers.Name,"OasisEscudo29")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica6







######
#####
##### TRAS LA TABLILLA Y FINAL

# minorx astutamente apostado junto a ascensor 

o=Bladex.CreateEntity("Hachacarnicero2","Hachacarnicero",0,0,0,"Weapon")

pers=Bladex.CreateEntity("TRL3","Minotaur",325046.15216, 37446.0816322, 18019.6020084,"Person")
pers.Angle=3.21644743057
pers.Level=lvl_control.GiveLevel(3,7)
Actions.TakeObject(pers.Name,"Hachacarnicero2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

## keletos pregolem

sectx10=Bladex.GetSector(356913.446088, 37440.3150351, 29533.6462932)
sectx10.OnEnter=x10

#1

ambiente6 = darfuncs.E_Grup()
ambiente6.OnDeath = Suenamusica7


o=Bladex.CreateEntity("OasisGladius31","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo31","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("31Esq","Skeleton",399904.82744, 46426.2822726, 62615.8386839,"Person")
pers.Angle=1.76004961528
pers.Level=lvl_control.GiveLevel(6,11)
Actions.TakeObject(pers.Name,"OasisGladius31")
Actions.TakeObject(pers.Name,"OasisEscudo31")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = Suenamusica7


#2


o=Bladex.CreateEntity("OasisGladius32","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo32","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("32Esq","Skeleton",395217.85589, 45691.0993571, 58500.3815055,"Person")
pers.Angle=1.76530209481
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius32")
Actions.TakeObject(pers.Name,"OasisEscudo32")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = Suenamusica7





sectx11=Bladex.GetSector(472267.594767, 53678.2236554, 107250.422267)
sectx11.OnEnter=x11



#3

o=Bladex.CreateEntity("OasisGladius33","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo33","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("33Esq","Skeleton",514510.200947, 57958.6087246, 54742.0751073,"Person")
pers.Angle=2.9656891447
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius33")
Actions.TakeObject(pers.Name,"OasisEscudo33")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


pers.Data.nodos=[(505492.159808, 57901.0473287, 68149.3577537), (501362.96898, 57893.6558546, 76631.5329129), (488340.277217, 57888.749705, 85510.449545), (479180.165001, 54331.4827604, 101580.445775)]
pers.Data.nodo_actual=0


#4

o=Bladex.CreateEntity("OasisGladius34","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo34","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("34Esq","Skeleton",504450.734669, 57879.2653423, 70733.4930731,"Person")
pers.Angle=3.58394277936
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OasisGladius34")
Actions.TakeObject(pers.Name,"OasisEscudo34")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.nodos=[(500347.35515, 57898.2759698, 76834.3711557), (488491.793293, 57875.0629117, 83818.4209731), (479835.248505, 54022.1615017, 104208.191032)]
pers.Data.nodo_actual=0


#5

o=Bladex.CreateEntity("OasisGladius35","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo35","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("35Esq","Skeleton",517605.01197, 57878.6892952, 44722.6880462,"Person")
pers.Angle=3.71372174036
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius35")
Actions.TakeObject(pers.Name,"OasisEscudo35")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.nodos=[(502186.069702, 57889.3379297, 75294.1894466), (489153.325543, 57897.179997, 85787.6364184)]
pers.Data.nodo_actual=0





#6

sectx12=Bladex.GetSector(442297.711252, 46996.7935514, 35863.159717)


o=Bladex.CreateEntity("OasisGladius36","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo36","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("36Esq","Skeleton",483432.070159, 53680.2306469, 25339.6006699,"Person")
pers.Angle=2.44834190702
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OasisGladius36")
Actions.TakeObject(pers.Name,"OasisEscudo36")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#7


o=Bladex.CreateEntity("OasisGladius37","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo37","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("37Esq","Skeleton",494799.848402, 55122.986237, 36565.3223852,"Person")
pers.Angle=2.24573433499
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OasisGladius37")
Actions.TakeObject(pers.Name,"OasisEscudo37")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## golem FINAL


Rigor2 = darfuncs.E_Grup()
Rigor2.OnDeath = achalaymybrother


pers=Bladex.CreateEntity("GolemFinal","Golem_stone",424410.978669, 46378.5569043, 61143.1268175,"Person")
pers.Angle=1.56351720108
pers.Level=lvl_control.GiveLevel(4,8)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Rigor2.AddGuy(pers.Name)
Rigor2.OnDeath = achalaymybrother

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = Suenamusica7






# 4 esqueletos mal aseados en el templo final

GuankeroKounter = darfuncs.E_Grup()
GuankeroKounter.OnDeath = MurioElEsqueleto



o=Bladex.CreateEntity("OasisNaginata1","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo40","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("40Esq","Skeleton",464478.775207, 46535.2, 83013.9336681,"Person")
pers.Angle=3.2223999723
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"OasisNaginata1")
Actions.TakeObject(pers.Name,"OasisEscudo40")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
GuankeroKounter.AddGuy(pers.Name)





o=Bladex.CreateEntity("OasisNaginata2","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo41","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("41Esq","Skeleton",470824.203616, 46535.2, 83164.3751548,"Person")
pers.Angle=3.11164429268
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OasisNaginata2")
Actions.TakeObject(pers.Name,"OasisEscudo41")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
GuankeroKounter.AddGuy(pers.Name)


o=Bladex.CreateEntity("OasisNaginata3","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo42","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("42Esq","Skeleton",470237.060202, 46535.2, 39517.8536737,"Person")
pers.Angle=0.118846988825
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"OasisNaginata3")
Actions.TakeObject(pers.Name,"OasisEscudo42")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
GuankeroKounter.AddGuy(pers.Name)



o=Bladex.CreateEntity("OasisNaginata4","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OasisEscudo43","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("43Esq","Skeleton",464701.374092, 46535.2, 39776.0234825,"Person")
pers.Angle=6.21208904124
pers.Level=lvl_control.GiveLevel(8,11)

Actions.TakeObject(pers.Name,"OasisNaginata4")
Actions.TakeObject(pers.Name,"OasisEscudo43")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
GuankeroKounter.AddGuy(pers.Name)




## golem susto 

Rigor3 = darfuncs.E_Grup()
Rigor3.OnDeath = segundaparteputada

pers=Bladex.CreateEntity("Golem2","Golem_stone",324941.629925, 13627.9898185, -31879.4470224,"Person")
pers.Angle=3.24050487767
pers.Level=lvl_control.GiveLevel(2,6)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Golem2")

Rigor3.AddGuy(pers.Name)



