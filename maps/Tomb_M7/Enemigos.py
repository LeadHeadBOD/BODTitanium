from math import pow
import EnemyTypes
import Sparks
import Actions
import pocimac
import darfuncs
import Breakings
import ItemTypes

Nukeleto = 3



Nukezombi = 2



#############################################################
#---orco arquero patrullando al ppio en la muralla--------

#1

enm=Bladex.CreateEntity("Tombarq1", "Ork",-26875.7686451, -5556.02601416, 432.975275275,"Person")
enm.Angle=6.28033830724
enm.Level=4
enm.ActionAreaMin=pow(2,0)
enm.ActionAreaMax=pow(2,1)
enm.SetOnFloor()

#enm.AddBayPoint=-26875.7686451, -5556.02601416, 432.975275275
#enm.AddBayPoint=-26814.5722844, -5551.89002536, 21958.1095745

o=Bladex.CreateEntity("TombArqesp1","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv=enm.GetInventory()
inv.AddWeapon("TombArqesp1")


o=Bladex.CreateEntity("TombArqbow1","Arco",0,0,0,"Weapon")
inv.AddBow("TombArqbow1")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("TombArqbow1"))

o=Bladex.CreateEntity("TombArqquiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("TombArqquiver1")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)


## orco escondido 1 junto a arquero inicial	( poner como arquero en la ventana al interior)
"""
o=Bladex.CreateEntity("TombEspada1","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("1ORC","Ork",-36159.3702019, -5000, -9624.08160354,"Person")
pers.Level=2
pers.Angle=0.0
Actions.TakeObject(pers.Name,"TombEspada1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
"""

enm=Bladex.CreateEntity("Tombarq31", "Ork",-25858.3617258, -5626.98393693, -10415.4462398,"Person")
enm.Angle=4.5
enm.Level=3
enm.ActionAreaMin=pow(2,0)
enm.ActionAreaMax=pow(2,1)
enm.SetOnFloor()
enm.Deaf = 1
darfuncs.EnterSecIdEvent("entraguardia",ElArqueroSeDestapaLosOidos)

o=Bladex.CreateEntity("TombArqesp31","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv=enm.GetInventory()
inv.AddWeapon("TombArqesp31")


o=Bladex.CreateEntity("TombArqbow31","Arco",0,0,0,"Weapon")
inv.AddBow("TombArqbow31")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("TombArqbow31"))

o=Bladex.CreateEntity("TombArqquiver31","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("TombArqquiver31")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)


## orco escondido 2 junto a arquero inicial

o=Bladex.CreateEntity("TombEspada1b","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("TombEscudo1b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

potion=Bladex.CreateEntity("Potion1borc","Pocima50",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion1borc")

pers=Bladex.CreateEntity("1bORC","Ork",-33463.808737, -5067.63217784, 33121.9875191,"Person")
pers.Angle=3.81583487909
pers.Level=4
Actions.TakeObject(pers.Name,"TombEspada1b")
Actions.TakeObject(pers.Name,"TombEscudo1b")
Actions.TakeObject(pers.Name,"Potion1borc")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()




## orco jefe patrullando abajo al ppio

o=Bladex.CreateEntity("TombEspada2","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("2ORC","Great_Ork",-22982.6792291, 5131.49708002, 12733.0437013,"Person")
pers.Angle=3.22854082906
pers.Level=4
Actions.TakeObject(pers.Name,"TombEspada2")
Actions.TakeObject(pers.Name,"TombEscudo2")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#pers.AddBayPoint=-22982.6792291, 5131.49708002, 12733.0437013
#pers.AddBayPoint=-22214.5080616, 5091.63080107, -25306.4787334
#pers.AddBayPoint=-18089.077452, 5072.90481219, -23002.8808519
#pers.AddBayPoint=-18716.1836096, 5074.8940198, 4295.28343276


###################################################################################
####    arquero 2 que hay que poner patrullando en la plataforma delante del templo


enm=Bladex.CreateEntity("Tombarq2", "Ork",-19247.6781809, -70.8951466149, 18313.8958658,"Person")
enm.Angle=3.08503110482
enm.Level=3
enm.ActionAreaMin=pow(2,2)
enm.ActionAreaMax=pow(2,3)

o=Bladex.CreateEntity("TombArqesp2","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv=enm.GetInventory()
inv.AddWeapon("TombArqesp2")


o=Bladex.CreateEntity("TombArqbow2","Arco",0,0,0,"Weapon")
inv.AddBow("TombArqbow2")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("TombArqbow2"))

o=Bladex.CreateEntity("TombArqquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("TombArqquiver2")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)
enm.SetOnFloor()

#enm.AddBayPoint=-19247.6781809, -70.8951466149, 18313.8958658
#enm.AddBayPoint=-12672.3136116, -98.0349409962, 21350.5576972
#enm.AddBayPoint=-5144.42384889, -125.098433588, 23259.8600817
#enm.AddBayPoint=-2665.57166396, -104.683702891, 28343.5120681
#enm.AddBayPoint=-5406.59201541, -117.52072132, 31647.8835263
#enm.AddBayPoint=-7212.96002189, -109.537482101, 28838.3555195
#enm.AddBayPoint=-5209.68745102, -133.179950166, 23161.9382656
#enm.AddBayPoint=-17613.612158, -128.941241445, 21908.0117583


#########################################################
# orco compañero del anterior patrullando
### este orco y su patrulla hacen que casque el engine

saquito3orc=Bladex.CreateEntity("Saquito3orc","Saquito",0,0,0,"Physic")
saquito3orc.Solid=0
saquito3orc.Scale=1.220190
pocimac.CreatePotion("Saquito3orc")

o=Bladex.CreateEntity("TombEspada3","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo3","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("3ORC","Ork",-4005.49452701, -67.8030319537, 18674.9648841,"Person")
pers.Angle=3.18343664834
pers.Level=4
Actions.TakeObject(pers.Name,"TombEspada3")
Actions.TakeObject(pers.Name,"TombEscudo3")
Actions.TakeObject(pers.Name,"Saquito3orc")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#pers.AddBayPoint=-4005.49452701, -67.8030319537, 18674.9648841
#pers.AddBayPoint=-3400.14854769, -68.6499116097, -22856.9957531
#pers.AddBayPoint=43457.8772492, -111.52171341, -22697.9448855
#pers.AddBayPoint=45582.0855182, -112.638271408, -19655.0608999
#pers.AddBayPoint=47986.973832, -110.027395106, -19317.2262452
#pers.AddBayPoint=48250.8552618, -106.978331291, -24509.5629565
#pers.AddBayPoint=-10888.9571846, -111.549189842, -24232.1146952
#pers.AddBayPoint=-11298.7597007, -124.181550357, 18856.9408051


###########################################################
## COSITAS EN LA SALA DE LOS ARCOS LATERALES

pers=Bladex.CreateEntity("1cos","Cos",26410.1480024, 4929.41075745, -32267.0775982,"Person")
pers.Angle=1.42361017525
pers.Level=5
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#2
#pers=Bladex.CreateEntity("2cos","Cos",29134.0529414, 4932.89950558, -37462.6769662,"Person")
#pers.Level=6
#pers.Angle=1.24556715337
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.SetOnFloor()

#3
pers=Bladex.CreateEntity("3cos","Cos",45402.183106, 4947.6932149, -32933.364746,"Person")
pers.Angle=1.58977192645
pers.Level=4
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#4
#pers=Bladex.CreateEntity("4cos","Cos",21261.3842086, 4943.89389771, -36120.5897041,"Person")
#pers.Level=6
#pers.Angle=4.94579985189
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.SetOnFloor()


#5
pers=Bladex.CreateEntity("5cos","Cos",36655.1658354, 4930.59517548, -38353.3184763,"Person")
pers.Angle=6.148864351
pers.Level=8
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#6
pers=Bladex.CreateEntity("6cos","Cos",48639.1714894, 4932.58375399, -37568.0007087,"Person")
pers.Angle=0.161923615369
pers.Level=5
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


############################################################################################
##
############################	ZONA DE LA TORRE




########################################
# orcos  antes de escalera de caracol

#1
potion=Bladex.CreateEntity("Potion4ORC","Pocima50",0,0,0,"Physic")
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion4ORC")

o=Bladex.CreateEntity("TombEspada4","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("4ORC","Great_Ork",67972.7908887, 5279.34553939, -23412.0689921,"Person")
pers.Angle=0.81597339004
pers.Level=5
Actions.TakeObject(pers.Name,"TombEspada4")
Actions.TakeObject(pers.Name,"TombEscudo4")
Actions.TakeObject(pers.Name,"Potion4ORC")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("4ORC")


sectx1=Bladex.GetSector(52565.5994308, 5332.68513105, -19668.6621622)

sectx1.OnEnter=x1


#########################################################################
#####		orco donde las cositas protegiendo la puerta
#2
o=Bladex.CreateEntity("TombEspada5","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo5","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("5ORC","Great_Ork",-1992.79312852, 4942.93561437, -31193.3,"Person")
#pers=Bladex.CreateEntity("5ORC","Great_Ork",-5000.3140923, 5348.81879198, -29093.9192202,"Person")
pers.Angle=3.1
pers.Level=5
Actions.TakeObject(pers.Name,"TombEspada5")
Actions.TakeObject(pers.Name,"TombEscudo5")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()




#########
#########
######### FOLLON TORRE CON LLAVE




#3  orco super mega patrullante por los pisos de la torre

o=Bladex.CreateEntity("TombEspada5b","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo5b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("5ORCb","Ork",75745.7247603, 5330.92658915, -31587.4885904,"Person")
pers.Angle=5.25155348167
pers.Level=3
Actions.TakeObject(pers.Name,"TombEspada5b")
Actions.TakeObject(pers.Name,"TombEscudo5b")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

#pers.AddBayPoint=75745.7247603, 5330.92658915, -31587.4885904
#pers.AddBayPoint=68505.9558997, 5332.63772983, -31669.2926125

#pers.AddBayPoint=67713.037908, 5332.63725044, -36328.56924
#pers.AddBayPoint=82243.5986903, 5032.9900318, -36580.5140243

#pers.AddBayPoint=82476.9091363, 3545.31097877, -25879.5679725
#pers.AddBayPoint=85046.8142472, 2632.25502396, -23924.4961712
#pers.AddBayPoint=88645.6445373, 1146.00437606, -25689.0045863
#pers.AddBayPoint=88818.9629, -56.6251993153, -29252.6946003
#pers.AddBayPoint=86149.3347795, -1253.95436971, -31538.3031313
#pers.AddBayPoint=82604.9496119, -1569.11930666, -31637.94522

#pers.AddBayPoint=82837.5039347, -2468.14501888, -38778.3992574
#pers.AddBayPoint=86040.3313522, -2468.27840694, -38780.776626
#pers.AddBayPoint=85957.7452166, -2467.39143998, -35195.8959634
#pers.AddBayPoint=82475.0848023, -2467.1711789, -35156.2780658

#pers.AddBayPoint=82604.9496119, -1569.11930666, -31637.94522
#pers.AddBayPoint=86149.3347795, -1253.95436971, -31538.3031313
#pers.AddBayPoint=88818.9629, -56.6251993153, -29252.6946003
#pers.AddBayPoint=88645.6445373, 1146.00437606, -25689.0045863
#pers.AddBayPoint=85046.8142472, 2632.25502396, -23924.4961712
#pers.AddBayPoint=82476.9091363, 3545.31097877, -25879.5679725

#pers.AddBayPoint=82243.5986903, 5032.9900318, -36580.5140243
#pers.AddBayPoint=76740.4827483, 5331.03277083, -36172.4259789
#pers.AddBayPoint=75745.7247603, 5330.92658915, -31587.4885904




## arquero en ventana, en habitacion llave

enm=Bladex.CreateEntity("Tombarq3", "Ork",62843, -3316, -19307,"Person")
enm.Angle=1.70280274342
enm.Level=0
enm.ActionAreaMin=pow(2,0)
enm.ActionAreaMax=pow(2,1)

o=Bladex.CreateEntity("TombArqesp3","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv=enm.GetInventory()
inv.AddWeapon("TombArqesp3")


o=Bladex.CreateEntity("TombArqbow3","Arco",0,0,0,"Weapon")
inv.AddBow("TombArqbow3")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("TombArqbow3"))

o=Bladex.CreateEntity("TombArqquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("TombArqquiver3")
o.Data.ArrowsLeft=10

enm.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(enm)



# orco al lado de agujero que da acceso a habitacion llave	(solo sale de vez en cuando)	

o=Bladex.CreateEntity("TombEspada6b","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo6b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("6ORCb","Ork",71087.6815041, -10016.4240739, -37815.8721427,"Person")
pers.Angle=4.70068353108
pers.Level=6
Actions.TakeObject(pers.Name,"TombEspada6b")
Actions.TakeObject(pers.Name,"TombEscudo6b")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("6ORCb")



## orco frente LA habitacion de la llave	(	poner con patrulla	)

o=Bladex.CreateEntity("TombEspada6","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo6","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("6ORC","Ork",70340.8981408, -3114.36892476, -30360.8953913,"Person")
pers.Angle=3.84922045636
pers.Level=4
Actions.TakeObject(pers.Name,"TombEspada6")
Actions.TakeObject(pers.Name,"TombEscudo6")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("6ORC", "T1")
pers.SetOnFloor()

#pers.AddBayPoint=70340.8981408, -3114.36892476, -30360.8953913
#pers.AddBayPoint=67360.5793197, -3066.89345763, -35153.72556
#pers.AddBayPoint=68299.468524, -3065.90621169, -39062.8757254
#pers.AddBayPoint=71034.6228303, -3068.99482495, -40269.7230586
#pers.AddBayPoint=74474.2333016, -3068.841425, -38384.5682839
#pers.AddBayPoint=74614.063123, -3066.04961154, -32876.7831858


pers.Data.ImDeadFuncPlus	= pers.ImDeadFunc
pers.ImDeadFunc			= MuerteOrcoDeMierda




# orco en lo alto de la torre

o=Bladex.CreateEntity("TombEspada7","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo7","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

#pers=Bladex.CreateEntity("7ORC","Great_Ork",67433.13901, -16292.8492973, -35017.6152607,"Person")
pers=Bladex.CreateEntity("7ORC","Great_Ork",74050.3554405, -16272.1597316, -39859.8376088,"Person")
pers.Angle=4.53745847786
pers.Level=5
Actions.TakeObject(pers.Name,"TombEspada7")
Actions.TakeObject(pers.Name,"TombEscudo7")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("7ORC", "T1")
pers.SetOnFloor()

#pers.AddBayPoint=74050.3554405, -16272.1597316, -39859.8376088
#pers.AddBayPoint=73359.5372524, -16296.8088813, -22875.1960004


################################################################################################
#############										       #
#############										       #
#############
#############
############################SEGUNDA PARTE 






## esqueleto colega de toda la vida de los que salen tras las puertas en twoskel.py

#1
o=Bladex.CreateEntity("TombtsAxeC","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombtsShieldC","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
 
tsSkeletonC=Bladex.CreateEntity("tsSkeletonC","Skeleton",23412.880, -666.650471701, 40275.930,"Person")
tsSkeletonC.Angle=4.66769793915
tsSkeletonC.Level=6
Actions.TakeObject(tsSkeletonC.Name,"TombtsAxeC")
Actions.TakeObject(tsSkeletonC.Name,"TombtsShieldC")
tsSkeletonC.ActionAreaMin=pow(2,2)
tsSkeletonC.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(tsSkeletonC)

tsSkeletonC.SetOnFloor()

tsSkeletonC.Data.ImDeadFuncPlus   = tsSkeletonC.ImDeadFunc
tsSkeletonC.ImDeadFunc            = MuerteesqueletoDeMierda


#2
hachasorpresa=Bladex.CreateEntity("TombHachaSorpresa","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
escudodorpresa=Bladex.CreateEntity("TombEscudoSorpresa","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
 
keletosorpresa1=Bladex.CreateEntity("KeletoSorpresa1","Skeleton",11427.4419, -351.626, 18387.63,"Person")
keletosorpresa1.Angle=1.5739783841
keletosorpresa1.Level=5
Actions.TakeObject(keletosorpresa1.Name,"TombHachaSorpresa")
Actions.TakeObject(keletosorpresa1.Name,"TombEscudoSorpresa")
keletosorpresa1.ActionAreaMin=pow(2,2)
keletosorpresa1.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(keletosorpresa1)
keletosorpresa1.SetOnFloor()


darfuncs.HideBadGuy("KeletoSorpresa1")


	

pers.Data.ImDeadFuncPlus	= pers.ImDeadFunc
pers.ImDeadFunc			= MuerteOrcoDeMierda




## esqueleto arquero "inteligentisimamente" colocado para joder al maximo en la galeria

enm=Bladex.CreateEntity("KeletoArkero", "Skeleton",72221, -813.389895065, 42950.0834501,"Person")
enm.Level=5
enm.Angle=2.60203006531
enm.ActionAreaMin=pow(2,2)
enm.ActionAreaMax=pow(2,3)

o=Bladex.CreateEntity("TombArqesp4","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv=enm.GetInventory()
inv.AddWeapon("TombArqesp4")


o=Bladex.CreateEntity("TombArqbow4","Arco",0,0,0,"Weapon")
inv.AddBow("TombArqbow4")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("TombArqbow4"))

o=Bladex.CreateEntity("TombArqquiver4","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("TombArqquiver4")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)
enm.SetOnFloor()



## esqueleto que te espera tras la segunda sala de vidrieras

o=Bladex.CreateEntity("TombKeletoaxe1","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombKeletoShield1","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

keleton1=Bladex.CreateEntity("Keleton1","Skeleton",87471.464, -1604.947, 30505.127,"Person")
keleton1.Level=4
keleton1.Angle=1.5329
Actions.TakeObject(keleton1.Name,"TombKeletoaxe1")
Actions.TakeObject(keleton1.Name,"TombKeletoShield1")
keleton1.ActionAreaMin=pow(2,2)
keleton1.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(keleton1)
keleton1.SetOnFloor()



sectx5=Bladex.GetSector(81317.4542505, -714.230080417, 53525.1326411)

sectx5.OnEnter=x5




## esqueletos protegen llave del cementerio

#1
o=Bladex.CreateEntity("TombKeletoaxe4","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombKeletoShield4","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

keleton4=Bladex.CreateEntity("Keleton4","Skeleton",124695.42, -3268.76, 22753.3,"Person")
keleton4.Angle=3.07887501201
keleton4.Level=5
Actions.TakeObject(keleton4.Name,"TombKeletoaxe4")
Actions.TakeObject(keleton4.Name,"TombKeletoShield4")
keleton4.ActionAreaMin=pow(2,2)
keleton4.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(keleton4)
keleton4.SetOnFloor()

darfuncs.HideBadGuy("Keleton4")


#2
o=Bladex.CreateEntity("TombKeletoaxe5","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombKeletoShield5","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)


keleton5=Bladex.CreateEntity("Keleton5","Skeleton",126937.61, -3315.477, 25272.052,"Person")
keleton5.Angle=2.83103691964
keleton5.Level=5
Actions.TakeObject(keleton5.Name,"TombKeletoaxe5")
Actions.TakeObject(keleton5.Name,"TombKeletoShield5")
keleton5.ActionAreaMin=pow(2,2)
keleton5.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(keleton5)
keleton5.SetOnFloor()

darfuncs.HideBadGuy("Keleton5")

	

sectx7=Bladex.GetSector(119715.38, -3311.941, 11066.92)

sectx7.OnEnter=x7



###########################################################################################################
########### ZOMBIES	 ZOMBIES	 ZOMBIES	 ZOMBIES	 ZOMBIES	 ZOMBIES
###########################################################################################################

"""
#1
o=Bladex.CreateEntity("TombHachaZombi1","Hacha5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi1","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

#pers=Bladex.CreateEntity("Zombi1","Knight_Zombie",100323.715909, 7904.99789503, 29536.2049072,"Person")
pers=Bladex.CreateEntity("Zombi1","Knight_Zombie",95060.5153822, 7930.74867976, 19069.4315889,"Person")
pers.Level=6
pers.Angle=2.50733515073
Actions.TakeObject(pers.Name,"TombHachaZombi1")
Actions.TakeObject(pers.Name,"TombEscudoZombi1")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,8)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#2
o=Bladex.CreateEntity("TombHachaZombi2","Hacha5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

#pers=Bladex.CreateEntity("Zombi2","Knight_Zombie",95168.3, 7884.83, 32273.28,"Person")
pers=Bladex.CreateEntity("Zombi2","Knight_Zombie",88184.1087765, 7432.20712127, 28773.4090451,"Person")
pers.Level=4
pers.Angle=3.07441765871
Actions.TakeObject(pers.Name,"TombHachaZombi2")
Actions.TakeObject(pers.Name,"TombEscudoZombi2")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,8)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#3
o=Bladex.CreateEntity("TombHachaZombi3","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi3","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("Zombi3","Knight_Zombie",88509.43, 7384.601, 26855.86,"Person")
pers.Level=5
pers.Angle=5.6263912909
Actions.TakeObject(pers.Name,"TombHachaZombi3")
Actions.TakeObject(pers.Name,"TombEscudoZombi3")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,8)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#4
o=Bladex.CreateEntity("TombHachaZombi4","Hacha5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

#pers=Bladex.CreateEntity("Zombi4","Knight_Zombie",82254.22, 6386.890, 57098.96,"Person")
pers=Bladex.CreateEntity("Zombi4","Knight_Zombie",78293.8377705, 6708.55551604, 43766.9947123,"Person")
pers.Level=6
pers.Angle=2.50588776199
Actions.TakeObject(pers.Name,"TombHachaZombi4")
Actions.TakeObject(pers.Name,"TombEscudoZombi4")
pers.ActionAreaMin=pow(2,9)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#5
o=Bladex.CreateEntity("TombHachaZombi5","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi5","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

#pers=Bladex.CreateEntity("Zombi5","Knight_Zombie",78309.64, 6590.72, 50910.18,"Person")
pers=Bladex.CreateEntity("Zombi5","Knight_Zombie",81659.8305322, 6633.2644289, 36328.9427621,"Person")
pers.Level=3
pers.Angle=3.24548708361
Actions.TakeObject(pers.Name,"TombHachaZombi5")
Actions.TakeObject(pers.Name,"TombEscudoZombi5")
pers.ActionAreaMin=pow(2,9)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()


#6
o=Bladex.CreateEntity("TombHachaZombi6","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi6","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("Zombi6","Knight_Zombie",63368.93, 6774.535, 52182.78,"Person")
pers.Level=5
pers.Angle=4.36897535664
Actions.TakeObject(pers.Name,"TombHachaZombi6")
Actions.TakeObject(pers.Name,"TombEscudoZombi6")
pers.ActionAreaMin=pow(2,9)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Data.ImDeadFuncPlus   = pers.ImDeadFunc
pers.ImDeadFunc            = MuerteZombiDeMierda



#7
o=Bladex.CreateEntity("TombHachaZombi7","Hacha5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudoZombi7","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("Zombi7","Knight_Zombie",58289.2889119, 6776.375, 56461.0,"Person")
pers.Level=5
pers.Angle=4.39241130363
Actions.TakeObject(pers.Name,"TombHachaZombi7")
Actions.TakeObject(pers.Name,"TombEscudoZombi7")
pers.ActionAreaMin=pow(2,9)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Data.ImDeadFuncPlus   = pers.ImDeadFunc
pers.ImDeadFunc            = MuerteZombiDeMierda

"""
## ya no hay mas zombies



########################################################################
####
####
## 2 keletos congelados hasta salida zona zombiesssssss
########################################################################
"""
#1
o=Bladex.CreateEntity("TombKeletoaxe2","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombKeletoShield2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

keleton2=Bladex.CreateEntity("Keleton2","Skeleton",56768.8, 5191.426, 26610.77,"Person")
keleton2.Level=4
keleton2.Angle=4.78476944589
Actions.TakeObject(keleton2.Name,"TombKeletoaxe2")
Actions.TakeObject(keleton2.Name,"TombKeletoShield2")
keleton2.ActionAreaMin=pow(2,10)
keleton2.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(keleton2)
keleton2.SetOnFloor()


darfuncs.HideBadGuy("Keleton2")



#2
o=Bladex.CreateEntity("TombKeletoaxe3","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombKeletoShield3","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

keleton3=Bladex.CreateEntity("Keleton3","Skeleton",72821.06, 5161.222, 26688.13,"Person")
keleton3.Level=5
keleton3.Angle=1.40744355628
Actions.TakeObject(keleton3.Name,"TombKeletoaxe3")
Actions.TakeObject(keleton3.Name,"TombKeletoShield3")
keleton3.ActionAreaMin=pow(2,10)
keleton3.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(keleton3)
keleton3.SetOnFloor()

darfuncs.HideBadGuy("Keleton3")


keleton2.Data.nodos=[(61954.2224996, 5187.58693565, 27029.3355911), (65065.0667634, 5870.97033585, 33983.5600357)]
keleton2.Data.nodo_actual=0

keleton3.Data.nodos=[(68744.065353, 5158.18072723, 27688.7380337), (68101.9227911, 5856.67151453, 33950.2260327)]
keleton3.Data.nodo_actual=0



listaeskeletos=[keleton2, keleton3]


"""


