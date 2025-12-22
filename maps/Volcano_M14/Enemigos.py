##///
##||| Volcano_M14/Enemigos.PY TITANIUM
##||| Change list:
##||| * OrkController 
##||| * Renamed the weapon store key dark knight's potion to "volcPotion10" to resolve it spawning as 500hp
##|||	insetad of the intended 1000hp if you already have "Potion10" from Desert_M13
##|||
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

# principio hasta escalera rota orkos

#1

o=Bladex.CreateEntity("VolcanoEspada1","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("PotionO1","Pocima25",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("PotionO1")

pers=Bladex.CreateEntity("1ORC",Orkk,42710.4822829, -5951.5160849, 18948.8821268,"Person")
pers.Level=lvl_control.GiveLevel(8,13)
pers.Angle=4.65575807943
Actions.TakeObject(pers.Name,"VolcanoEspada1")
Actions.TakeObject(pers.Name,"VolcanoEscudo1")
Actions.TakeObject(pers.Name,"PotionO1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("1ORC", "exterior")
pers.SetOnFloor()

#2

o=Bladex.CreateEntity("VolcanoEspada2","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo2","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("PotionO2","Pocima50",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("PotionO2")

pers=Bladex.CreateEntity("2ORC","Great_Ork",42694.6301741, -5932.52618439, 4898.10830314,"Person")
pers.Level=lvl_control.GiveLevel(8,13)
pers.Angle=4.78644138407
Actions.TakeObject(pers.Name,"VolcanoEspada2")
Actions.TakeObject(pers.Name,"VolcanoEscudo2")
Actions.TakeObject(pers.Name,"PotionO2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

# desde escalera rota a elevador + puente roto orkos 

#1

o=Bladex.CreateEntity("VolcanoEspada3","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("3ORC",Orkk,37912.4352487, -1196.98165208, 16105.2259272,"Person")
pers.Level=lvl_control.GiveLevel(8,10)
pers.Angle=1.54139175589
Actions.TakeObject(pers.Name,"VolcanoEspada3")
Actions.TakeObject(pers.Name,"VolcanoEscudo3")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#2

o=Bladex.CreateEntity("VolcanoEspada4","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("4ORC",Orkk,38065.2751479, -1117.80986226, 7516.78939648,"Person")
pers.Level=lvl_control.GiveLevel(9,11)
pers.Angle=1.51864960281
Actions.TakeObject(pers.Name,"VolcanoEspada4")
Actions.TakeObject(pers.Name,"VolcanoEscudo4")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3

o=Bladex.CreateEntity("VolcanoEspada5","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo5","Escudo9",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("PotionO3","Pocima50",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("PotionO3")


orc5=Bladex.CreateEntity("ORC5","Great_Ork",37872.7669041, -1559.12709043, 35426.0959756,"Person")
orc5.Level=lvl_control.GiveLevel(9,13)
orc5.Angle=2.33843560835
Actions.TakeObject(orc5.Name,"VolcanoEspada5")
Actions.TakeObject(orc5.Name,"VolcanoEscudo5")
Actions.TakeObject(orc5.Name,"PotionO3")
orc5.ActionAreaMin=pow(2,2)
orc5.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(orc5)
orc5.Deaf=1
orc5.Blind=1
orc5.SetOnFloor()




#4

o=Bladex.CreateEntity("VolcanoEspada6","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo6","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

orc6=Bladex.CreateEntity("ORC6",Orkk,29780.4308624, 657.884173577, 38247.6237586,"Person")
orc6.Level=lvl_control.GiveLevel(8,14)
orc6.Angle=5.36291533172
Actions.TakeObject(orc6.Name,"VolcanoEspada6")
Actions.TakeObject(orc6.Name,"VolcanoEscudo6")
orc6.ActionAreaMin=pow(2,2)
orc6.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(orc6)
orc6.Deaf=1
orc6.Blind=1
orc6.SetOnFloor()



# desde puente roto a roto escaleras kaballeros negros + lichs


#2

pers=Bladex.CreateEntity("VolcanoArq2", "Dark_Knight",8288.13336537, 531.110550562, 38880.417217,"Person")
pers.Angle=3.30716028553
pers.Level=lvl_control.GiveLevel(7,11)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada2","EgyptSword",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada2")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow2","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow2")

o=Bladex.CreateEntity("Volcanoquiver2","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver2")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


#3


o=Bladex.CreateEntity("VolcanoEspada7","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo7","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("Potion04","Pocima200",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion04")

pers=Bladex.CreateEntity("7Kngt","Dark_Knight",17460.9214981, 474.421401126, 31515.6742722,"Person")
pers.Angle=1.60451967312
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"VolcanoEspada7")
Actions.TakeObject(pers.Name,"VolcanoEscudo7")
Actions.TakeObject(pers.Name,"Potion04")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Data.nodos=[(4447.00290008, 480.749890143, 31749.0298695), (4640.34800895, 498.289760057, 37037.5271524)]
pers.Data.nodo_actual=0

sectx7=Bladex.GetSector(20065.7022566, 471.470522703, 37878.2999704)
sectx7.OnEnter=x7

#4

o=Bladex.CreateEntity("VolcanoEspada8","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo8","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("8Lich","Lich",-13421.9737741, -1317.68746661, 35437.4830969,"Person")
pers.Angle=5.64231461261
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
Actions.TakeObject(pers.Name,"VolcanoEspada8")
Actions.TakeObject(pers.Name,"VolcanoEscudo8")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("8Lich")


#5

o=Bladex.CreateEntity("VolcanoEspada9","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9Lich","Lich",-15549.634233, -2029.16883193, 41474.1049427,"Person")
pers.Angle=4.06297633997
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
Actions.TakeObject(pers.Name,"VolcanoEspada9")
Actions.TakeObject(pers.Name,"VolcanoEscudo9")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("9Lich")

#5b

o=Bladex.CreateEntity("VolcanoEspada9b","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9b","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9bLich","Lich",-30581.7679796, -3481.83138272, 37548.0311742,"Person")
pers.Angle=4.85660177761
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
Actions.TakeObject(pers.Name,"VolcanoEspada9b")
Actions.TakeObject(pers.Name,"VolcanoEscudo9b")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("9bLich")

#5c


o=Bladex.CreateEntity("VolcanoEspada9c","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9c","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9cLich","Lich",-19358.256836, -4611.58026002, 34458.9011917,"Person")
pers.Angle=0.467320277902
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
Actions.TakeObject(pers.Name,"VolcanoEspada9c")
Actions.TakeObject(pers.Name,"VolcanoEscudo9c")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("9cLich")

# desde roto escaleras hasta minotauro zampon kaballeros negros

## lich nuevo 1

o=Bladex.CreateEntity("VolcanoEspada9cc","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9cc","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9ccLich","Lich",-35276.5120472, -9759.65571017, 40388.4734023,"Person")
pers.Angle=3.24242175731
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,"VolcanoEspada9cc")
Actions.TakeObject(pers.Name,"VolcanoEscudo9cc")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


## lich nuevo 2

o=Bladex.CreateEntity("VolcanoEspada9cc2","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9cc2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9cc2Lich","Lich",-42080.4976359, -9761.43305329, 42902.795926,"Person")
pers.Angle=4.78107097058
pers.Level=lvl_control.GiveLevel(6,10)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,"VolcanoEspada9cc2")
Actions.TakeObject(pers.Name,"VolcanoEscudo9cc2")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()





## lich nuevo 3

o=Bladex.CreateEntity("VolcanoEspada9cc3","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo9cc3","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9cc3Lich","Lich",-42429.1377533, -9771.88006746, 36355.5250193,"Person")
pers.Angle=6.11459779526
pers.Level=lvl_control.GiveLevel(5,9)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,"VolcanoEspada9cc3")
Actions.TakeObject(pers.Name,"VolcanoEscudo9cc3")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#1



ambiente2 = darfuncs.E_Grup()
ambiente2.OnDeath = TerminanLasMuertes2

o=Bladex.CreateEntity("VolcanoEspada10","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo10","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("10Kngt","Dark_Knight",-40437.8657141, -16352.9793951, 5606.10766076,"Person")
pers.Angle=4.65519951245
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"VolcanoEspada10")
Actions.TakeObject(pers.Name,"VolcanoEscudo10")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = TerminanLasMuertes2


pers.Data.nodos=[(-17389.8673709, -13076.5674296, 5880.28630716), (-17682.6228264, -13145.4984736, 9036.18574709)]
pers.Data.nodo_actual=0


#2

o=Bladex.CreateEntity("VolcanoEspada11","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo11","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("VolcanoPotion05","Pocima200",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("VolcanoPotion05")

pers=Bladex.CreateEntity("11Kngt","Dark_Knight",-40481.6576571, -16343.646207, 13920.0019392,"Person")
pers.Angle=3.16696984981
pers.Level=lvl_control.GiveLevel(11,13)
Actions.TakeObject(pers.Name,"VolcanoEspada11")
Actions.TakeObject(pers.Name,"VolcanoEscudo11")
Actions.TakeObject(pers.Name,"VolcanoPotion05")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = TerminanLasMuertes2

pers.Data.nodos=[(-40261.4659834, -16347.7706192, 5503.13184144), (-22457.7611407, -13142.3744619, 5723.05954805), (-22620.4291253, -13152.3183886, 8834.95979141)]
pers.Data.nodo_actual=0


sectx2=Bladex.GetSector(-17045.1734895, -13344.7215308, 21345.228205)

sectx2.OnEnter=x2

#3   este tiene la llave que permite seguir, la que esta en la celda del minotauro

o=Bladex.CreateEntity("VolcanoEspada12","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo12","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("12Kngt","Dark_Knight",-44325.1039646, -12096.465573, 9793.2344893,"Person")
pers.Angle=6.27264822811
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"VolcanoEspada12")
Actions.TakeObject(pers.Name,"VolcanoEscudo12")
Actions.TakeObject(pers.Name,"llave4")
pers.ActionAreaMin=pow(2,26)
pers.ActionAreaMax=pow(2,27)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = TerminanLasMuertes2

### keletos arqueros tras minotauro zampon 2,10  2,11


#1

pers=Bladex.CreateEntity("VolcanoArq3", "Skeleton",-35536.9117305, -14106.1096087, 1821.7236094,"Person")
pers.Angle=4.60735409874
pers.Level=lvl_control.GiveLevel(9,13)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada3","HookSword",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada3")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow3")

o=Bladex.CreateEntity("Volcanoquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver3")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


#2

pers=Bladex.CreateEntity("VolcanoArq4", "Skeleton",-34866.3065243, -14111.9492516, -3168.13268986,"Person")
pers.Angle=4.7422163
pers.Level=lvl_control.GiveLevel(10,14)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada4","Espadacurva",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada4")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow4","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow4")

o=Bladex.CreateEntity("Volcanoquiver4","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver4")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


#3

pers=Bladex.CreateEntity("VolcanoArq5", "Skeleton",-47271.9257579, -13621.7292402, -7245.44242381,"Person")
pers.Angle=3.35447559123
pers.Level=lvl_control.GiveLevel(7,12)
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada5","HookSword",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada5")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow5")

o=Bladex.CreateEntity("Volcanoquiver5","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver5")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


##zombis en escalera de caracol despues de minot zampon 2,12  2,13

#1

o=Bladex.CreateEntity("VolcanoEspada13","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo13","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("13Zombi","Knight_Zombie",-18868.1309529, -11259.9399934, -16666.2716019,"Person")
pers.Angle=0.896488062614
pers.Level=lvl_control.GiveLevel(8,13)
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
Actions.TakeObject(pers.Name,"VolcanoEspada13")
Actions.TakeObject(pers.Name,"VolcanoEscudo13")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Data.nodos=[(-21060.3562678, -10096.052163, -12407.6639921), (-19137.4394467, -8906.85055723, -8069.88867416), (-15682.772168, -8101.59228332, -8169.2736859)]
pers.Data.nodo_actual=0

sectx3=Bladex.GetSector(-14639.6930198, -11921.1285703, -15252.095868)
sectx3.OnEnter=x3

#2

o=Bladex.CreateEntity("VolcanoEspada14","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo14","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("14Zombi","Knight_Zombie",-15703.8378967, -5708.61497915, -16584.8360388,"Person")
pers.Angle=5.6908148535
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
Actions.TakeObject(pers.Name,"VolcanoEspada14")
Actions.TakeObject(pers.Name,"VolcanoEscudo14")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3

o=Bladex.CreateEntity("VolcanoEspada15","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo15","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("15Zombi","Knight_Zombie",-15309.4976719, -1909.81553293, -9324.90228159,"Person")
pers.Angle=4.05388166973
pers.Level=lvl_control.GiveLevel(7,11)
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
Actions.TakeObject(pers.Name,"VolcanoEspada15")
Actions.TakeObject(pers.Name,"VolcanoEscudo15")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



## keletos 2,12  2,13

#1

ambiente3 = darfuncs.E_Grup()
ambiente3.OnDeath = TerminanLasMuertes3


o=Bladex.CreateEntity("VolcanoEspada16","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo16","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("16Esq","Skeleton",1192.91879345, -2224.60247647, -897.117447589,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=3.1337730183
Actions.TakeObject(pers.Name,"VolcanoEspada16")
Actions.TakeObject(pers.Name,"VolcanoEscudo16")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("16Esq")

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = TerminanLasMuertes3


#2

o=Bladex.CreateEntity("VolcanoEspada17","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo17","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("17Esq","Skeleton",674.886027282, 273.963117142, -25684.2687194,"Person")
pers.Level=lvl_control.GiveLevel(9,13)
pers.Angle=6.23521594639
Actions.TakeObject(pers.Name,"VolcanoEspada17")
Actions.TakeObject(pers.Name,"VolcanoEscudo17")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("17Esq")

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = TerminanLasMuertes3



#3

o=Bladex.CreateEntity("VolcanoEspada18","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo18","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("18Esq","Skeleton",15890.0770801, 1617.66485543, -25541.2839941,"Person")
pers.Level=lvl_control.GiveLevel(8,12)
pers.Angle=1.49515243216
Actions.TakeObject(pers.Name,"VolcanoEspada18")
Actions.TakeObject(pers.Name,"VolcanoEscudo18")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("18Esq")

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = TerminanLasMuertes3


darfuncs.EnterSecEvent(-2308.08568703, -1491.14509823, -11743.6075003,activakeletos)

#cab negros charlando uno de los cuales tiene la llave misteriosa

#1

ambiente4 = darfuncs.E_Grup()
ambiente4.OnDeath = TerminanLasMuertes4

o=Bladex.CreateEntity("VolcanoEspada19","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo19","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("Potion06","Pocima100",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion06")

pers=Bladex.CreateEntity("19Kngt","Dark_Knight",1599.40682755, 5880.70791357, 1835.17678407,"Person")
pers.Angle=4.7291048539
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"VolcanoEspada19")
Actions.TakeObject(pers.Name,"VolcanoEscudo19")
Actions.TakeObject(pers.Name,"Potion06")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = TerminanLasMuertes4


#2



o=Bladex.CreateEntity("VolcanoEspada20","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo20","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("Potion07","Pocima100",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion07")

pers=Bladex.CreateEntity("20Kngt","Dark_Knight",1656.83886653, 5827.3856766, -661.153271174,"Person")
pers.Angle=4.7291048539
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"VolcanoEspada20")
Actions.TakeObject(pers.Name,"VolcanoEscudo20")
Actions.TakeObject(pers.Name,"Potion07")
Actions.TakeObject(pers.Name,"llaverag")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

sectx15=Bladex.GetSector(15749,2496,-12486)
sectx15.OnEnter=x15

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = TerminanLasMuertes4


## tras cab negros anteriores:minotauro y cab negro en zona trampa pinchos desestimada

ambiente5 = darfuncs.E_Grup()
ambiente5.OnDeath = TerminanLasMuertes5


#1 Minotauro

o=Bladex.CreateEntity("Hachacarnicero","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("21Minorx","Minotaur",-41155.2523047, 6878.96470633, 10334.3156721,"Person")
pers.Level=lvl_control.GiveLevel(5,10)
pers.Angle=3.27930543557
Actions.TakeObject(pers.Name,"Hachacarnicero")
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = TerminanLasMuertes5

#2 cab neg


o=Bladex.CreateEntity("VolcanoEspada22","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo22","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("volcPotion10","Pocima200",0,0,0,"Physic")	# Renamed, referenced later in code as potion.Name	-LeadHead
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)		

pers=Bladex.CreateEntity("22Kngt","Dark_Knight",-25694.3908123, 7371.67299813, 4804.74281317,"Person")
pers.Angle=1.48636296227
pers.Level=lvl_control.GiveLevel(10,13)
Actions.TakeObject(pers.Name,"VolcanoEspada22")
Actions.TakeObject(pers.Name,"VolcanoEscudo22")
Actions.TakeObject(pers.Name,potion.Name)
Actions.TakeObject(pers.Name,"llave1")
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = TerminanLasMuertes5

pers.Data.nodos=[(-43318.2095517, 6893.4251472, 5761.37792114), (-43704.9351431, 6868.27563103, 11040.8817196)]
pers.Data.nodo_actual=0

sectx5=Bladex.GetSector(-17245.7938137, 7876.31341767, 2198.69069743)
sectx5.OnEnter=x5



#####  salamanders -los unicos del juego, por cierto-


salamanders = darfuncs.E_Grup()
salamanders.OnDeath = aparecensalam


#1


pers=Bladex.CreateEntity("23Salamander","Salamander",-43241.6804008, 17665.7873157, -42308.0367141,"Person")
pers.Level=lvl_control.GiveLevel(6,9)
pers.Angle=4.6663845927
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

salamanders.AddGuy(pers.Name)
salamanders.OnDeath = aparecensalam


darfuncs.HideBadGuy("23Salamander")

#2


pers=Bladex.CreateEntity("23bSalamander","Salamander",-30265.518746, 17703.9650703, -41692.6826871,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=1.67758247772
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

salamanders.AddGuy(pers.Name)
salamanders.OnDeath = aparecensalam

darfuncs.HideBadGuy("23bSalamander")




#2


pers=Bladex.CreateEntity("25Salamander","Salamander",-53808.9913171, 12795.0269512, -17188.6809504,"Person")
pers.Level=lvl_control.GiveLevel(8,10)
pers.Angle=3.09432133234
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("25Salamander")


## lichs en subida desde escena #Prisioneros a la parrilla.2,18  2,19
	
Prisioneros = darfuncs.E_Grup()
Prisioneros.OnDeath = TerminanLasMuertes1

#1

o=Bladex.CreateEntity("VolcanoEspada25","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo25","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("25Lich","Lich",55942.4010134, 2669.49183581, -30143.1574538,"Person")
pers.Angle=6.24698457199
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada25")
Actions.TakeObject(pers.Name,"VolcanoEscudo25")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

Prisioneros.AddGuy(pers.Name)
Prisioneros.OnDeath = TerminanLasMuertes1



#2

o=Bladex.CreateEntity("VolcanoEspada26","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo26","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("26Lich","Lich",47362.5626607, 2133.44269337, -29156.635803,"Person")
pers.Angle=4.85069386033
pers.Level=lvl_control.GiveLevel(7,9)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada26")
Actions.TakeObject(pers.Name,"VolcanoEscudo26")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

Prisioneros.AddGuy(pers.Name)
Prisioneros.OnDeath = TerminanLasMuertes1


#3

o=Bladex.CreateEntity("VolcanoEspada27","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo27","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("27Lich","Lich",40235.1759806, 1581.90760182, -28049.5428479,"Person")
pers.Angle=4.66950402131
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada27")
Actions.TakeObject(pers.Name,"VolcanoEscudo27")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#4

o=Bladex.CreateEntity("VolcanoEspada28","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo28","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("28Lich","Lich",34054.774802, 1392.74591086, -21061.4702275,"Person")
pers.Angle=3.16566966493
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada28")
Actions.TakeObject(pers.Name,"VolcanoEscudo28")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#kontingentes en escalera de caracol:


#1

o=Bladex.CreateEntity("VolcanoEspada29","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo29","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("29Lich","Lich",38523.4102343, 67.359105116, -13184.4517428,"Person")
pers.Angle=2.50302998099
pers.Level=lvl_control.GiveLevel(9,11)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada29")
Actions.TakeObject(pers.Name,"VolcanoEscudo29")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("29Lich")


#2

o=Bladex.CreateEntity("VolcanoEspada30","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo30","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("30Lich","Lich",31400.3836794, -2530.80261899, -12903.0246333,"Person")
pers.Angle=6.16145094668
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada30")
Actions.TakeObject(pers.Name,"VolcanoEscudo30")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("30Lich")


#3

o=Bladex.CreateEntity("VolcanoEspada31","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo31","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("31Lich","Lich",34122.3857585, -10184.1453568, -16547.4751806,"Person")
pers.Angle=1.00040014028
pers.Level=lvl_control.GiveLevel(5,8)
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
Actions.TakeObject(pers.Name,"VolcanoEspada31")
Actions.TakeObject(pers.Name,"VolcanoEscudo31")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("31Lich")

### keletos peligrosos  2,20  2,21 el primero en llamas

ambiente6 = darfuncs.E_Grup()
ambiente6.OnDeath = TerminanLasMuertes6

#1



o=Bladex.CreateEntity("VolcanoEspada32","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo32","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("32Esq","Skeleton",34503.1704315, -11533.0134714, 5439.92861142,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=6.27522026424
Actions.TakeObject(pers.Name,"VolcanoEspada32")
Actions.TakeObject(pers.Name,"VolcanoEscudo32")
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("32Esq")

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = TerminanLasMuertes6

pers.Data.nodos=[(34481.2319194, -11834.4108148, 32607.0953445), (39180.8068705, -12116.2420054, 38258.5048047), (34363.5688387, -12117.260118, 42274.9138127), (29672.8732077, -12138.5541741, 38123.1175065), (10791.4363835, -13139.4042269, 38010.3383639)]
pers.Data.nodo_actual=0

sectx8=Bladex.GetSector(38453.6317013, -11315.4829036, -9926.10174062)
sectx8.OnEnter=x8


#2 OJO OCULTAR ESTE PORQUE SE LE VE DESDE ABAJO

o=Bladex.CreateEntity("VolcanoEspada33","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo33","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("33Esq","Skeleton",6103.58058394, -13138.1904192, 39899.8195976,"Person")
pers.Level=lvl_control.GiveLevel(9,12)
pers.Angle=3.20175694865
Actions.TakeObject(pers.Name,"VolcanoEspada33")
Actions.TakeObject(pers.Name,"VolcanoEscudo33")
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("33Esq")


pers.Data.nodos=[(6076.44353529, -13138.9736453, 37850.372607), (-11777.4409672, -14395.087502, 37622.075249), (-16604.7904806, -15420.8023213, 41590.670704), (-19703.0811382, -16142.2494179, 41122.3162011), (-21470.603773, -17144.9698881, 37394.2706421), (-17215.8864371, -18394.6795443, 32728.3972721), (-17404.0300222, -20647.9163916, 20125.3274421)]
pers.Data.nodo_actual=0

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = TerminanLasMuertes6

sectx9=Bladex.GetSector(10805.3585164, -13116.8673335, 37866.291451)
sectx9.OnEnter=x9


#3


o=Bladex.CreateEntity("VolcanoEspada34","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo34","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("34Esq","Skeleton",-13941.774803, -18387.4971687, 36002.8174053,"Person")
pers.Level=lvl_control.GiveLevel(8,11)
pers.Angle=2.21780565522
Actions.TakeObject(pers.Name,"VolcanoEspada34")
Actions.TakeObject(pers.Name,"VolcanoEscudo34")
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente6.AddGuy(pers.Name)
ambiente6.OnDeath = TerminanLasMuertes6


## cab muertos vivientes 2,22  2,23


#1

o=Bladex.CreateEntity("VolcanoEspada35","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo35","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("35Zombi","Knight_Zombie",-18521.3058264, -17901.9252318, -15652.1357051,"Person")
pers.Angle=4.53133609705
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"VolcanoEspada35")
Actions.TakeObject(pers.Name,"VolcanoEscudo35")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#2

o=Bladex.CreateEntity("VolcanoEspada36","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo36","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("36Zombi","Knight_Zombie",14945.5104259, -14861.9104165, -18805.8322212,"Person")
pers.Angle=6.21278698612
pers.Level=lvl_control.GiveLevel(9,12)
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"VolcanoEspada36")
Actions.TakeObject(pers.Name,"VolcanoEscudo36")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("36Zombi")

pers.Data.nodos=[(14500.72287, -15557.0934417, -12596.5520042), (876.18443873, -15544.6705426, -12995.743932)]
pers.Data.nodo_actual=0


#3

o=Bladex.CreateEntity("VolcanoEspada37","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo37","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("37Zombi","Knight_Zombie",15567.0819234, -14301.2495976, -23398.4129038,"Person")
pers.Angle=0.0353226677233
pers.Level=lvl_control.GiveLevel(8,11)
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"VolcanoEspada37")
Actions.TakeObject(pers.Name,"VolcanoEscudo37")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("37Zombi")

pers.Data.nodos=[(15801.959466, -15547.5409137, -11778.0570348), (7243.4387669, -15538.4624781, -11965.5649522)]
pers.Data.nodo_actual=0


sectx10=Bladex.GetSector(-13374.0059742, -15874.0520915, -14062.9147492)
sectx10.OnEnter=x10


#4

o=Bladex.CreateEntity("VolcanoEspada38","Martillo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo38","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("38Zombi","Knight_Zombie",10879.2714688, -12142.6477496, -12484.4148851,"Person")
pers.Angle=3.12677343813
pers.Level=lvl_control.GiveLevel(9,13)
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"VolcanoEspada38")
Actions.TakeObject(pers.Name,"VolcanoEscudo38")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("38Zombi")

pers.Data.nodos=[(10751.8430167, -13647.4076039, -26114.421898), (15805.2386927, -14150.0097786, -25766.6305353), (15376.3171952, -15199.8960141, -16387.5331363)]
pers.Data.nodo_actual=0


#5

o=Bladex.CreateEntity("VolcanoEspada39","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo39","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("39Zombi","Knight_Zombie",9581.81580534, -12544.4378837, -16658.3345793,"Person")
pers.Angle=3.15792463642
pers.Level=lvl_control.GiveLevel(8,12)
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"VolcanoEspada39")
Actions.TakeObject(pers.Name,"VolcanoEscudo39")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("39Zombi")

pers.Data.nodos=[(10784.8167975, -13665.1613564, -25260.8126036), (16108.3729692, -14163.7873825, -24628.3745651), (16188.6217814, -14547.3988327, -21331.8993198)]
pers.Data.nodo_actual=0

sectx11=Bladex.GetSector(-2033.91593373, -15568.9702583, -11940.9971145)
sectx11.OnEnter=x11


#6

o=Bladex.CreateEntity("VolcanoEspada39b","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo39b","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("39bKngt","Dark_Knight",6316.62340736, -9521.22536162, -12131.4494751,"Person")
pers.Angle=6.26465342863
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"VolcanoEspada39b")
Actions.TakeObject(pers.Name,"VolcanoEscudo39b")
Actions.TakeObject(pers.Name,"llavemaz")
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


## cab negros pre finales 2,24  2,25

final1= darfuncs.E_Grup()
final1.OnDeath = SigueAdelante

#1

o=Bladex.CreateEntity("VolcanoEspada40","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo40","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("Potion08","Pocima100",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion08")

pers=Bladex.CreateEntity("40Kngt","Dark_Knight",16496.9145194, -8654.71553198, -32401.1082205,"Person")
pers.Angle=1.61008916627
pers.Level=lvl_control.GiveLevel(9,11)
Actions.TakeObject(pers.Name,"VolcanoEspada40")
Actions.TakeObject(pers.Name,"VolcanoEscudo40")
Actions.TakeObject(pers.Name,"Potion08")
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

final1.AddGuy(pers.Name)
final1.OnDeath = SigueAdelante



#2

o=Bladex.CreateEntity("VolcanoEspada42","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo42","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("42Kngt","Dark_Knight",10276.0128616, -9748.46993466, -45905.2817925,"Person")
pers.Angle=1.61503235429
pers.Level=lvl_control.GiveLevel(8,10)
Actions.TakeObject(pers.Name,"VolcanoEspada42")
Actions.TakeObject(pers.Name,"VolcanoEscudo42")
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

final1.AddGuy(pers.Name)
final1.OnDeath = SigueAdelante


#3

o=Bladex.CreateEntity("VolcanoEspada43","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo43","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoPocimaTodo","PocimaTodo",0,0,0,"Physic")
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("VolcanoPocimaTodo")

pers=Bladex.CreateEntity("43Kngt","Dark_Knight",2838.46913619, -9752.43145416, -45643.3091544,"Person")
pers.Angle=4.72043907357
pers.Level=lvl_control.GiveLevel(11,13)
Actions.TakeObject(pers.Name,"VolcanoEspada43")
Actions.TakeObject(pers.Name,"VolcanoEscudo43")
Actions.TakeObject(pers.Name,"VolcanoPocimaTodo")
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

final1.AddGuy(pers.Name)
final1.OnDeath = SigueAdelante

### bichos zona secreta derrumbamientos 2,28  2,29

## keletos arkeros

#1

pers=Bladex.CreateEntity("VolcanoArq6", "Skeleton",-48987.2105796, 5923.04832323, -15708.4079526,"Person")
pers.Angle=3.2691412717
pers.Level=lvl_control.GiveLevel(9,11)
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada6","Espadacurva",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada6")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow6","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow6")

o=Bladex.CreateEntity("Volcanoquiver6","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver6")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("VolcanoArq6")

pers.Data.nodos=[(-48654.1456349, 7677.53934069, -30470.8872734), (-51145.4484896, 8177.81938495, -32977.6098686), (-53205.5173902, 8425.95072951, -33600.2963158), (-66696.0485952, 8940.64404541, -33376.8918634), (-67617.2788204, 10426.0309302, -17290.1870279)]
pers.Data.nodo_actual=0


#2

pers=Bladex.CreateEntity("VolcanoArq7", "Skeleton",-46951.1719784, 6380.84426552, -19298.7695754,"Person")
pers.Angle=3.14738935857
pers.Level=lvl_control.GiveLevel(8,10)
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
pers.SetOnFloor()

o=Bladex.CreateEntity("VolcanoArcEspada7","HookSword",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("VolcanoArcEspada7")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Volcanobow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Volcanobow7")

o=Bladex.CreateEntity("Volcanoquiver7","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Volcanoquiver7")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("VolcanoArq7")

pers.Data.nodos=[(-46846.1110209, 7897.33033845, -30916.2357014), (-52263.9917848, 8382.76656527, -35434.1923083), (-70557.0974846, 8881.8911815, -35242.411975), (-70540.8039572, 10952.4371524, -8833.58117601), (-55251.2203212, 11644.6770479, -8974.12325474), (-55125.8623133, 11625.6647779, -11065.9409484)]
pers.Data.nodo_actual=0

sectx13=Bladex.GetSector(-40718.1992011, 2115.46972807, -12072.7999486)
sectx13.OnEnter=x13


#3 convertirlo en arkero

o=Bladex.CreateEntity("VolcanoEspada44","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudo44","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("44Esq","Skeleton",-60684.7071363, 11373.6871131, -11629.5269168,"Person")
pers.Level=lvl_control.GiveLevel(9,11)
pers.Angle=3.15098501991
Actions.TakeObject(pers.Name,"VolcanoEspada44")
Actions.TakeObject(pers.Name,"VolcanoEscudo44")
pers.ActionAreaMin=pow(2,28)
pers.ActionAreaMax=pow(2,29)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#####################
#MINOTAURO ENCERRADO#
#####################

o=Bladex.CreateEntity("VolcanoCachoGarrote","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot","Minotaur",-47066.7835794, -12031.2481911, 9928.28008639,"Person")
pers.Level=lvl_control.GiveLevel(6,11)
pers.Angle=5.45932587962
Actions.TakeObject(pers.Name,"VolcanoCachoGarrote")
pers.ActionAreaMin=pow(2,26)
pers.ActionAreaMax=pow(2,27)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = TerminanLasMuertes2

sectx14=Bladex.GetSector(-27000,-13000,5000)
sectx14.OnEnter=Suenamusica1


############ESQUELETOS EN LLAMAS
####### En el hurryup 
o=Bladex.CreateEntity("VolcanoEspadaLL1","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("VolcanoEscudoLL1","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("LL1Esq","Skeleton",-53788, 5015, 25026,"Person")
pers.Level=lvl_control.GiveLevel(15,16)
pers.Angle=4.6337730183
Actions.TakeObject(pers.Name,"VolcanoEspadaLL1")
Actions.TakeObject(pers.Name,"VolcanoEscudoLL1")
#pers.ActionAreaMin=pow(2,12)
#pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.EnciendeEnLlamas(pers)
