##///
##||| ORC_M9/Enemigos.PY TITANIUM
##||| Change list:
##||| * OrkController 
##\\\ 

from math import pow
import EnemyTypes
import Sparks
import Actions
import pocimac
import Breakings
import ItemTypes
import darfuncs
import Bladex
import ItemTypes
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)
# e.g. to give an enemy a level between 0 and 4, do
# pers.Level= lvl_control.GiveLevel(0, 4)
#

### Orc controller
import OrkController
darkOrk_thresh = 13
goldOrk_thresh = 16
Orkk = OrkController.MinorOrk(darkOrk_thresh,goldOrk_thresh)
###

#------------------ORCOS INICIALES ANTES DE LA BOLA APLASTADORA-----------------------

#1

o=Bladex.CreateEntity("1ORCPotion","Saquito",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("1ORCPotion")


o=Bladex.CreateEntity("OrcGladius1","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("1ORC",Orkk,32943.462708, 48902.0696142, -1079.47249229,"Person")
pers.Angle=3.10137884787
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OrcGladius1")
Actions.TakeObject(pers.Name,"OrcEscudo1")
Actions.TakeObject(pers.Name,"1ORCPotion")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)



#2


o=Bladex.CreateEntity("OrcGladius2","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("2ORC",Orkk,37173.1926286, 48895.5639069, -7772.16965932,"Person")
pers.Angle=1.55686721225
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OrcGladius2")
Actions.TakeObject(pers.Name,"OrcEscudo2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## segundo grupo de orcos apollardaos


## genera orcos al lado de armadura oculta

Trasbola = darfuncs.E_Grup()
Trasbola.OnDeath = TerminanLasMuertes


#1

o=Bladex.CreateEntity("3ORCPotion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("3ORCPotion")


o=Bladex.CreateEntity("OrcGladius3","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("3ORC","Great_Ork",51349.991333, 48708.7995368, -3562.344,"Person")
pers.Angle=3.3471807728
pers.Level=lvl_control.GiveLevel(8,10)
Actions.TakeObject(pers.Name,"OrcGladius3")
Actions.TakeObject(pers.Name,"OrcEscudo3")
Actions.TakeObject(pers.Name,"3ORCPotion")
Actions.TakeObject("3ORC","llaver3")
#pers.ActionAreaMin=pow(2,1)
#pers.ActionAreaMax=pow(2,2)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#Trasbola.AddGuy(pers.Name)
#Trasbola.OnDeath = TerminanLasMuertes


#3

o=Bladex.CreateEntity("OrcGladius4","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

orcosinicio= darfuncs.E_Grup()
orcosinicio.OnDeath = ambiente1


orc4=Bladex.CreateEntity("orc4","Great_Ork",53527.9053652, 48879.280157, 39162.6538636,"Person")
orc4.Angle=2.0620982705494
orc4.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(orc4.Name,"OrcGladius4")
Actions.TakeObject(orc4.Name,"OrcEscudo4")
orc4.ActionAreaMin=pow(2,2)
orc4.ActionAreaMax=pow(2,3)
orc4.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(orc4)

Trasbola.AddGuy(pers.Name)
Trasbola.OnDeath = TerminanLasMuertes

orcosinicio.AddGuy(pers.Name)
orcosinicio.OnDeath = ambiente1

orc4.Data.nodos=[(53735.1827911, 48362.9019719, 47603.1369473), (48588.803081, 48435.1800165, 47379.2919405)]
orc4.Data.nodo_actual=0



listabichos=[orc4]


sectx1=Bladex.GetSector(53028.7212305, 48850.1805573, -1232.29360856)

sectx1.OnEnter=x1

## orco víctima bola


o=Bladex.CreateEntity("OrcGladius5","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo5","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc5","Great_Ork",37432.3363844, 44892.057624, 33565.66,"Person")
pers.Angle=3.12606128142
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OrcGladius5")
Actions.TakeObject(pers.Name,"OrcEscudo5")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Trasbola.AddGuy(pers.Name)
Trasbola.OnDeath = TerminanLasMuertes



##########GRUPO DESPUES DE LA BOLA#############

o=Bladex.CreateEntity("6ORCPotion","Pocima50",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("6ORCPotion")


o=Bladex.CreateEntity("OrcGladius6","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo6","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc6","Great_Ork",26365.6416846, 36992.0512705, 1112.60338457,"Person")
pers.Angle=6.21083650723
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OrcGladius6")
Actions.TakeObject(pers.Name,"OrcEscudo6")
Actions.TakeObject(pers.Name,"6ORCPotion")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#orko  1

o=Bladex.CreateEntity("OrcGladiusxx","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudoxx","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("OrcArq1", Orkk,-35529.3792614, 36870.6325354, 10315.2424657,"Person")
pers.Angle=4.54626845719
pers.Level=lvl_control.GiveLevel(4,9)
Actions.TakeObject(pers.Name,"OrcGladiusxx")
Actions.TakeObject(pers.Name,"OrcEscudoxx")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## orkos kontingentes


o=Bladex.CreateEntity("OrcGladius8","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo8","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc8",Orkk,-31813.9717155, 36857.3517486, 13982.4230642,"Person")
pers.Angle=3.16819032318
pers.Level=lvl_control.GiveLevel(5,12)
Actions.TakeObject(pers.Name,"OrcGladius8")
Actions.TakeObject(pers.Name,"OrcEscudo8")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc8")



o=Bladex.CreateEntity("OrcGladius9","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("OrcEscudo9","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc9","Great_Ork",-42311.8855342, 36807.2684685, 36256.9837856,"Person")
pers.Angle=4.07204588916
pers.Level=lvl_control.GiveLevel(5,9)
Actions.TakeObject(pers.Name,"OrcGladius9")
Actions.TakeObject(pers.Name,"OrcEscudo9")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc9")


## zona arkeros hijoputosos + orko kondido

arkeros= darfuncs.E_Grup()
arkeros.OnDeath = ambiente2

Trasllave = darfuncs.E_Grup()
Trasllave.OnDeath = TerminanLasMuertes3


#1

pers=Bladex.CreateEntity("OrcArq2", "Ork",-21182.8458767, 29880.3635003, 62051.1955534,"Person")
pers.Angle=3.14416028825
pers.Level=lvl_control.GiveLevel(8,12)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("OrcArcGladius2","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("OrcArcGladius2")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Orcbow2","Arco",0,0,0,"Weapon")
inv.AddBow("Orcbow2")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Orcbow2"))

o=Bladex.CreateEntity("Orcquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Orcquiver2")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

arkeros.AddGuy(pers.Name)
arkeros.OnDeath = ambiente2

Trasllave .AddGuy(pers.Name)
Trasllave .OnDeath = TerminanLasMuertes3


#2

pers=Bladex.CreateEntity("OrcArq3", "Ork",-13721.8580176, 29896.6113983, 62337.7878303,"Person")
pers.Angle=2.89629923752
pers.Level=lvl_control.GiveLevel(7,12)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("OrcArcGladius3","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("OrcArcGladius3")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Orcbow3","Arco",0,0,0,"Weapon")
inv.AddBow("Orcbow3")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Orcbow3"))

o=Bladex.CreateEntity("Orcquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Orcquiver3")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

arkeros.AddGuy(pers.Name)
arkeros.OnDeath = ambiente2

Trasllave .AddGuy(pers.Name)
Trasllave .OnDeath = TerminanLasMuertes3


## orko kondido

o=Bladex.CreateEntity("10ORCPotion","Pocima100",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("10ORCPotion")

o=Bladex.CreateEntity("OrcGladius10","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo10","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc10","Great_Ork",-1033.61392877, 30914.6748736, 46815.329,"Person")
pers.Angle=2.82
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OrcGladius10")
Actions.TakeObject(pers.Name,"OrcEscudo10")
Actions.TakeObject(pers.Name,"10ORCPotion")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

arkeros.AddGuy(pers.Name)
arkeros.OnDeath = ambiente2

Trasllave .AddGuy(pers.Name)
Trasllave .OnDeath = TerminanLasMuertes3


### pasillo lateral + zona superior a comedor




Traspasillo = darfuncs.E_Grup()
Traspasillo.OnDeath = TerminanLasMuertes2


o=Bladex.CreateEntity("OrcGladius11","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo11","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc11",Orkk,-5331.40020928, 30660.9224879, 21928.8595659,"Person")
pers.Angle=3.39729181253
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OrcGladius11")
Actions.TakeObject(pers.Name,"OrcEscudo11")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Traspasillo.AddGuy(pers.Name)
Traspasillo.OnDeath = TerminanLasMuertes2



o=Bladex.CreateEntity("OrcGladius12","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo12","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc12",Orkk,1574.50679833, 30637.9282548, 15162.1044104,"Person")
pers.Angle=6.28317709327
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"OrcGladius12")
Actions.TakeObject(pers.Name,"OrcEscudo12")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Traspasillo.AddGuy(pers.Name)
Traspasillo.OnDeath = TerminanLasMuertes2



o=Bladex.CreateEntity("13ORCPotion","Pocima200",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("13ORCPotion")

o=Bladex.CreateEntity("OrcGladius13","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo13","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc13","Great_Ork",25722.607591, 25516.1216039, 52776.3545161,"Person")
pers.Angle=3.0839609308
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OrcGladius13")
Actions.TakeObject(pers.Name,"OrcEscudo13")
Actions.TakeObject(pers.Name,"13ORCPotion")
Actions.TakeObject("orc13","llave1")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Traspasillo.AddGuy(pers.Name)
Traspasillo.OnDeath = TerminanLasMuertes2

# orkos kontingentes

o=Bladex.CreateEntity("OrcGladius14","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo14","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc14",Orkk,969.70160384, 30914.9785558, 13426.5325217,"Person")
pers.Angle=6.1961450953
pers.Level=lvl_control.GiveLevel(7,12)
Actions.TakeObject(pers.Name,"OrcGladius14")
Actions.TakeObject(pers.Name,"OrcEscudo14")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc14")



o=Bladex.CreateEntity("OrcGladius15","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo15","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc15",Orkk,11930.1064444, 30825.0451775, 18344.065836,"Person")
pers.Angle=1.50454130568
pers.Level=lvl_control.GiveLevel(5,9)
Actions.TakeObject(pers.Name,"OrcGladius15")
Actions.TakeObject(pers.Name,"OrcEscudo15")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc15")




## orkos komedor y final


Trascomedor = darfuncs.E_Grup()
Trascomedor.OnDeath = TerminanLasMuertes4


o=Bladex.CreateEntity("OrcGladius16","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo16","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc16",Orkk,18958.2204164, 30902.9529966, 31617.4755677,"Person")
pers.Angle=6.16251523429
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OrcGladius16")
Actions.TakeObject(pers.Name,"OrcEscudo16")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Trascomedor.AddGuy(pers.Name)
Trascomedor.OnDeath = TerminanLasMuertes4

darfuncs.HideBadGuy("orc16")



o=Bladex.CreateEntity("OrcGladius17","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo17","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc17",Orkk,9970.06870609, 33176.565602, 30130.3705578,"Person")
pers.Angle=6.26044916463
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OrcGladius17")
Actions.TakeObject(pers.Name,"OrcEscudo17")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Trascomedor.AddGuy(pers.Name)
Trascomedor.OnDeath = TerminanLasMuertes4

darfuncs.HideBadGuy("orc17")




### a partir de la mazmorra y hasta el final.



Trasdungeon = darfuncs.E_Grup()
Trasdungeon.OnDeath = TerminanLasMuertes5


o=Bladex.CreateEntity("OrcGladius18","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo18","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc18",Orkk,2190.48076862, 37367.2137606, 30784.3846067,"Person")
pers.Angle=3.28240288813
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OrcGladius18")
Actions.TakeObject(pers.Name,"OrcEscudo18")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc18")

Trasdungeon.AddGuy(pers.Name)
Trasdungeon.OnDeath = TerminanLasMuertes5


o=Bladex.CreateEntity("OrcGladius19","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo19","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc19",Orkk,18448.6419573, 37353.7400485, 31148.3159078,"Person")
pers.Angle=3.01350682854
pers.Level=lvl_control.GiveLevel(7,12)
Actions.TakeObject(pers.Name,"OrcGladius19")
Actions.TakeObject(pers.Name,"OrcEscudo19")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc19")

Trasdungeon.AddGuy(pers.Name)
Trasdungeon.OnDeath = TerminanLasMuertes5




# contingentes


o=Bladex.CreateEntity("OrcGladius20","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo20","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc20",Orkk,18206.3706693, 42877.7586796, 25481.6837407,"Person")
pers.Angle=1.61072267399
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OrcGladius20")
Actions.TakeObject(pers.Name,"OrcEscudo20")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc20")



o=Bladex.CreateEntity("OrcGladius21","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo21","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc21",Orkk,1744.75734357, 42860.1542221, 25586.5252997,"Person")
pers.Angle=4.7296873429
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OrcGladius21")
Actions.TakeObject(pers.Name,"OrcEscudo21")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc21")



#patrullante no contingente con llave

Trasdungeon2 = darfuncs.E_Grup()
Trasdungeon2.OnDeath = TerminanLasMuertes6


o=Bladex.CreateEntity("OrcGladius22","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo22","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc22","Great_Ork",647.587701768, 44827.6096282, 17089.1854172,"Person")
pers.Angle=4.75767637472
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"OrcGladius22")
Actions.TakeObject(pers.Name,"OrcEscudo22")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Trasdungeon2.AddGuy(pers.Name)
Trasdungeon2.OnDeath = TerminanLasMuertes6


pers.AddBayPoint=647.587701768, 44827.6096282, 17089.1854172
pers.AddBayPoint=26030.3915192, 44801.2627591, 17184.0986264
pers.AddBayPoint=25967.80992, 44876.8208735, 19448.0752082
pers.AddBayPoint=679.451653181, 44856.1897804, 19762.0411615

# compañero del anterior

o=Bladex.CreateEntity("23ORCPotion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("23ORCPotion")


o=Bladex.CreateEntity("OrcGladius23","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo23","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc23",Orkk,26988.2249315, 44851.3379389, 27961.6425904,"Person")
pers.Angle=2.9679932991
pers.Level=lvl_control.GiveLevel(6,11)
Actions.TakeObject(pers.Name,"OrcGladius23")
Actions.TakeObject(pers.Name,"OrcEscudo23")
Actions.TakeObject(pers.Name,"23ORCPotion")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

Trasdungeon2.AddGuy(pers.Name)
Trasdungeon2.OnDeath = TerminanLasMuertes6

## orcos contingentes respecto de los 2 anteriores

#1

o=Bladex.CreateEntity("OrcGladius24","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo24","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc24",Orkk,21259.5214117, 46148.5223547, 62434.9977675,"Person")
pers.Angle=6.10019260015
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"OrcGladius24")
Actions.TakeObject(pers.Name,"OrcEscudo24")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc24")


#2


o=Bladex.CreateEntity("OrcGladius25","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo25","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc25",Orkk,1225.71114814, 46155.3533616, 62491.9126879,"Person")
pers.Angle=6.03052699378
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"OrcGladius25")
Actions.TakeObject(pers.Name,"OrcEscudo25")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc25") 




## troll guarda supermegaespada

aftertroll= darfuncs.E_Grup()
aftertroll.OnDeath = ambiente4


o=Bladex.CreateEntity("Hachacarnicero","Hachacarnicero",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("TRL1","Troll_Dark",-18390.2391601, 48188.4132841, 25745.3159735,"Person")
pers.Angle=5.41798791935
pers.Level=lvl_control.GiveLevel(5,8)
Actions.TakeObject(pers.Name,"Hachacarnicero")
Actions.TakeObject("TRL1","llave88")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)

aftertroll.AddGuy(pers.Name)
aftertroll.OnDeath = ambiente4



############3
#######segunda revision

o=Bladex.CreateEntity("OrcArq44Potion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("OrcArq44Potion")


pers=Bladex.CreateEntity("OrcArq44", "Ork",52318.8842254, 40891.4428294, 50682.18,"Person")
pers.Angle=3.05
pers.Level=lvl_control.GiveLevel(8,12)
pers.ActionAreaMin=pow(2,7)
pers.ActionAreaMax=pow(2,2)
Actions.TakeObject(pers.Name,"OrcArq44Potion")
pers.SetOnFloor()

o=Bladex.CreateEntity("OrcArcGladius44","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("OrcArcGladius44")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Orcbow44","Arco",0,0,0,"Weapon")
inv.AddBow("Orcbow44")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Orcbow44"))

o=Bladex.CreateEntity("Orcquiver44","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Orcquiver44")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

orcosinicio.AddGuy(pers.Name)
orcosinicio.OnDeath = ambiente1


o=Bladex.CreateEntity("OrcArq55Potion","Pocima25",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("OrcArq55Potion")

pers=Bladex.CreateEntity("OrcArq55", "Ork",45533.7074428, 40889.4851763, 42709.1487,"Person")
pers.Angle=3.05
pers.Level=lvl_control.GiveLevel(6,12)
pers.ActionAreaMin=pow(2,7)
pers.ActionAreaMax=pow(2,2)
Actions.TakeObject(pers.Name,"OrcArq55Potion")
pers.SetOnFloor()

o=Bladex.CreateEntity("OrcArcGladius55","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("OrcArcGladius55")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Orcbow55","Arco",0,0,0,"Weapon")
inv.AddBow("Orcbow55")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Orcbow55"))


o=Bladex.CreateEntity("Orcquiver55","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Orcquiver55")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

orcosinicio.AddGuy(pers.Name)
orcosinicio.OnDeath = ambiente1


## ORCOS DONDE EL TROLL

#1

OrcosTroll= darfuncs.E_Grup()
OrcosTroll.OnDeath = ApareceCapullo



o=Bladex.CreateEntity("OrcGladius244","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo244","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc244","Great_Ork",-8042.83246563, 48202.9518638, 44513.2893712,"Person")
pers.Angle=6.23346813387
pers.Level=lvl_control.GiveLevel(7,9)
Actions.TakeObject(pers.Name,"OrcGladius244")
Actions.TakeObject(pers.Name,"OrcEscudo244")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc244")

OrcosTroll.AddGuy(pers.Name)
OrcosTroll.OnDeath = ApareceCapullo

aftertroll.AddGuy(pers.Name)
aftertroll.OnDeath = ambiente4



## 2

o=Bladex.CreateEntity("OrcGladius255","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo255","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc255","Great_Ork",-14510.7431276, 48202.9520996, 35509.9267892,"Person")
pers.Angle=5.86098458062
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OrcGladius255")
Actions.TakeObject(pers.Name,"OrcEscudo255")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc255")

aftertroll.AddGuy(pers.Name)
aftertroll.OnDeath = ambiente4


## 3

o=Bladex.CreateEntity("OrcGladius256","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo256","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc256","Great_Ork",-9885.81217535, 47919.2727528, 24435.1589113,"Person")
pers.Angle=6.1875879287
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OrcGladius256")
Actions.TakeObject(pers.Name,"OrcEscudo256")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc256")

aftertroll.AddGuy(pers.Name)
aftertroll.OnDeath = ambiente4

















#################################
#SALEN DESPUES DE ABRIR LA PUERTA
#################################
o=Bladex.CreateEntity("OrcGladius355","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo355","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc355","Great_Ork",2334.72816163, 43006.2187279, 24512.856,"Person")
pers.Angle=3.15
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OrcGladius355")
Actions.TakeObject(pers.Name,"OrcEscudo355")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,6)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc355")
#################################
o=Bladex.CreateEntity("OrcGladius345","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo345","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orc345","Great_Ork",627.632305511, 46174.8973264, 63423.3005,"Person")
pers.Angle=0.8
pers.Level=lvl_control.GiveLevel(7,9)
Actions.TakeObject(pers.Name,"OrcGladius345")
Actions.TakeObject(pers.Name,"OrcEscudo345")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,6)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orc345")


##########################################

TrollMuerte = darfuncs.E_Grup()
TrollMuerte.OnDeath = ActivaSacaMierda
TrollMuerte.AddGuy("TRL1")

##########################################


Finalfinal= darfuncs.E_Grup()
Finalfinal.OnDeath = Ambientefinal



o=Bladex.CreateEntity("OrcGladiusFin1","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudoFin1","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orcFin1","Great_Ork",13641.426365, 55905.9020715, 49463.672,"Person")
pers.Angle=4.8
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"OrcGladiusFin1")
Actions.TakeObject(pers.Name,"OrcEscudoFin1")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orcFin1")

Finalfinal.AddGuy(pers.Name)
Finalfinal.OnDeath = Ambientefinal


##########################################

o=Bladex.CreateEntity("OrcGladiusFin2","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudoFin2","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("orcFin2","Great_Ork",3480.0546334, 55889.138573, 48180.790,"Person")
pers.Angle=4.8
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"OrcGladiusFin2")
Actions.TakeObject(pers.Name,"OrcEscudoFin2")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("orcFin2")

Finalfinal.AddGuy(pers.Name)
Finalfinal.OnDeath = Ambientefinal
