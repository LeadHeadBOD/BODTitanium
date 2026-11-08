##///
##||| Ruins_M4/Pivotes.PY TITANIUM
##||| Change list:
##||| * Replaced arrow traps with darts to better balance them against low player health in starting levels
##\\\ 

import Bladex
import InitDataField



MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8



##################
#     Varios     #
##################


Bladex.CreateTimer("Timer025", 0.25)



###################
#     Objetos     #
###################


lanzapivtimer=Bladex.CreateEntity("NoName276","Lanzapivotes",21089.260899,-1420.221380,32296.285090)
lanzapivtimer.Scale=1.4
lanzapivtimer.Orientation=0.500000,0.500000,-0.500000,0.500000

lanzapivtimer1=Bladex.CreateEntity("NoName277","Lanzapivotes",21089.260899,-1412.773944,34079.106076)
lanzapivtimer1.Scale=1.4
lanzapivtimer1.Orientation=0.500000,0.500000,-0.500000,0.500000

lanzapivtimer2=Bladex.CreateEntity("NoName278","Lanzapivotes",21089.260899,-1417.859055,35864.977859)
lanzapivtimer2.Scale=1.4
lanzapivtimer2.Orientation=0.500000,0.500000,-0.500000,0.500000

lanzapivtimer3=Bladex.CreateEntity("NoName279","Lanzapivotes",21089.260899,-1406.656239,37667.452077)
lanzapivtimer3.Scale=1.4
lanzapivtimer3.Orientation=0.500000,0.500000,-0.500000,0.500000

Pivotelab1=Bladex.CreateEntity("Pivotelab1","Pivote",20974.0,-1410.0,32305.0,"Arrow")
Pivotelab1.Scale=1.0
Pivotelab1.Orientation=0.0, 0.70710682869, -0.707106769085, 0.0
Pivotelab1.SendSectorMsgs=0
InitDataField.Initialise(Pivotelab1)
Pivotelab1.Data.NoFXOnHit=1

Pivotelab2=Bladex.CreateEntity("Pivotelab2","Pivote",20974.0,-1403.0,34086.0,"Arrow")
Pivotelab2.Scale=1.0
Pivotelab2.Orientation=0.0, 0.70710682869, -0.707106769085, 0.0
Pivotelab2.SendSectorMsgs=0
InitDataField.Initialise(Pivotelab2)
Pivotelab2.Data.NoFXOnHit=1

Pivotelab3=Bladex.CreateEntity("Pivotelab3","Pivote",20974.0,-1410.0,35872.0,"Arrow")
Pivotelab3.Scale=1.0
Pivotelab3.Orientation=0.0, 0.70710682869, -0.707106769085, 0.0
Pivotelab3.SendSectorMsgs=0
InitDataField.Initialise(Pivotelab3)
Pivotelab3.Data.NoFXOnHit=1

Pivotelab4=Bladex.CreateEntity("Pivotelab4","Pivote",20974.0,-1400.0,37676.0,"Arrow")
Pivotelab4.Scale=1.0
Pivotelab4.Orientation=0.0, 0.70710682869, -0.707106769085, 0.0
Pivotelab4.SendSectorMsgs=0
InitDataField.Initialise(Pivotelab4)
Pivotelab4.Data.NoFXOnHit=1

o=Bladex.CreateEntity("Lanzapivotesext1","Lanzapivotes",-15093.977078,-1411.370493,-17688.087930)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

o=Bladex.CreateEntity("Lanzapivotesext2","Lanzapivotes",-18392.769581,-971.598295,-15096.367520)
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("NoName284","Lanzapivotes",58410.788037,5995.528950,-61319.442768)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

o=Bladex.CreateEntity("NoName285","Lanzapivotes",58406.350447,6886.452678,-61321.699056)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

o=Bladex.CreateEntity("NoName286","Lanzapivotes",58410.573818,6449.043145,-62008.480344)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

o=Bladex.CreateEntity("NoName287","Lanzapivotes",58411.263842,6449.478017,-60636.855901)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

Pivotext1=Bladex.CreateEntity("Pivotext1","Pivote",-15000.598,-1412.396,-17696.588,"Arrow")
Pivotext1.Scale=1.0
Pivotext1.Orientation=0.0, 0.707106769085, 0.707106769085, 0.0
Pivotext1.SendSectorMsgs=0
InitDataField.Initialise(Pivotext1)
Pivotext1.Data.NoFXOnHit=1

Pivotext2=Bladex.CreateEntity("Pivotext2","Pivote",-18382.010,-967.265,-15000.499,"Arrow")
Pivotext2.Scale=1.0
Pivotext2.Orientation=0.5, 0.5, 0.5, 0.5
Pivotext2.SendSectorMsgs=0
InitDataField.Initialise(Pivotext2)
Pivotext2.Data.NoFXOnHit=1

Pivotint1=Bladex.CreateEntity("Pivotint1","Pivote",58500.537,6461.237,-62019.761,"Arrow")
Pivotint1.Scale=1.0
Pivotint1.Orientation=0.7071, 0.0, 0.0, -0.7071
Pivotint1.SendSectorMsgs=0
InitDataField.Initialise(Pivotint1)
Pivotint1.Data.NoFXOnHit=1

Pivotint2=Bladex.CreateEntity("Pivotint2","Pivote",58500.863,5991.060,-61329.302,"Arrow")
Pivotint2.Scale=1.0
Pivotint2.Orientation=0.7071, 0.0, 0.0, -0.7071
Pivotint2.SendSectorMsgs=0
InitDataField.Initialise(Pivotint2)
Pivotint2.Data.NoFXOnHit=1

Pivotint3=Bladex.CreateEntity("Pivotint3","Pivote",58500.044,6457.474,-60646.428,"Arrow")
Pivotint3.Scale=1.0
Pivotint3.Orientation=0.7071, 0.0, 0.0, -0.7071
Pivotint3.SendSectorMsgs=0
InitDataField.Initialise(Pivotint3)
Pivotint3.Data.NoFXOnHit=1

Pivotint4=Bladex.CreateEntity("Pivotint4","Pivote",58500.562,6890.940,-61325.458,"Arrow")
Pivotint4.Scale=1.0
Pivotint4.Orientation=0.7071, 0.0, 0.0, -0.7071
Pivotint4.SendSectorMsgs=0
InitDataField.Initialise(Pivotint4)
Pivotint4.Data.NoFXOnHit=1

Pivotetes1=Bladex.CreateEntity("Pivotetes1","Pivote",-40750.0,-2100.0,45250.0,"Arrow")
Pivotetes1.Scale=1.0
Pivotetes1.Orientation=0.500000,0.500000,0.500000,0.500000
Pivotetes1.SendSectorMsgs=0
InitDataField.Initialise(Pivotetes1)
Pivotetes1.Data.NoFXOnHit=1

Pivotetes2=Bladex.CreateEntity("Pivotetes2","Pivote",-45250.0,-1800.0,40750.0,"Arrow")
Pivotetes2.Scale=1.0
Pivotetes2.Orientation=0.000000,0.707107,-0.707107,0.000000
Pivotetes2.SendSectorMsgs=0
InitDataField.Initialise(Pivotetes2)
Pivotetes2.Data.NoFXOnHit=1

o=Bladex.CreateEntity("Lanzapivotestes1","Lanzapivotes",-40844.0,-2100.0,45250.0)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,-0.500000

o=Bladex.CreateEntity("Lanzapivotestes2","Lanzapivotes",-45250.0,-1800.0,40844.0)
o.Scale=1.402577
o.Orientation=0.000000,0.000000,0.707107,-0.707107



###################
#     Sonidos     #
###################


sonidoactivacionflechas=Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActivacionFlechas')
sonidoactivacionflechas.Volume=0.8
sonidoactivacionflechas.MinDistance=1000
sonidoactivacionflechas.MaxDistance=20000

sonidopiv=Bladex.CreateSound('../../Sounds/dart-shoot.wav','SonidoPivote')
sonidopiv.Volume=0.8
sonidopiv.MinDistance=1000
sonidopiv.MaxDistance=20000



#######################################
#     Clase y funciones generales     #
#######################################


nflecha=0


######## Funcion: FlechaClavada(hitting_ent, hit_ent)

######## Funcion: InicializaFlecha(entity_name)



######################################
#     Lanzapivotes del laberinto     #
######################################


ntimepiv=0
pivstop=0
splab=Bladex.GetSector(23000.0,-2000.0,35000.0)


######## Funcion: FuncPivotelab(SectorIndex,EntityName)

######## Funcion: FuncPivotelabStop(SectorIndex,EntityName)

######## Funcion: TimerFuncPivotelab(entname,time)

flechalab1=InicializaFlecha("Pivotelab1")
flechalab2=InicializaFlecha("Pivotelab2")
flechalab3=InicializaFlecha("Pivotelab3")
flechalab4=InicializaFlecha("Pivotelab4")

lanzapivtimer.TimerFunc=TimerFuncPivotelab
splab.OnEnter=FuncPivotelab
splab.OnLeave=FuncPivotelabStop



#####################################
#     Lanzapivotes del interior     #
#####################################


ntimepivint=0
spint=Bladex.GetSector(51763.9376071,6751.5,-61222.0342807)


######## Funcion: FuncPivoteint(SectorIndex,EntityName)

######## Funcion: TimerFuncPivoteint(entname,time)

flechaint1=InicializaFlecha("Pivotint1")
flechaint2=InicializaFlecha("Pivotint2")
flechaint3=InicializaFlecha("Pivotint3")
flechaint4=InicializaFlecha("Pivotint4")

lanzapivtimer1.TimerFunc=TimerFuncPivoteint
spint.OnEnter=FuncPivoteint



#####################################
#     Lanzapivotes del exterior     #
#####################################


ntimepivext=0
pivextstop=0
spext=Bladex.GetSector(-18954.3055099,-1248.5,-19370.2023245)

######## Funcion: FuncPivotext(SectorIndex,EntityName)

######## Funcion: FuncPivotextStop(SectorIndex,EntityName)

######## Funcion: TimerFuncPivotext(entname,time)

flechaext1=InicializaFlecha("Pivotext1")
flechaext2=InicializaFlecha("Pivotext2")

lanzapivtimer2.TimerFunc=TimerFuncPivotext
spext.OnEnter=FuncPivotext
spext.OnLeave=FuncPivotextStop



##############################################
#     Lanzapivotes de la sala del tesoro     #
##############################################


ntimepivtes=0
pivtesstop=0
sptes=Bladex.GetSector(-44000.0,-2000.0,44000.0)

######## Funcion: FuncPivotetes()

######## Funcion: LanzaFuncPivotetes(SectorIndex,EntityName)

######## Funcion: FuncPivotetesStop(SectorIndex,EntityName)

######## Funcion: TimerFuncPivotetes(entname,time)

flechates1=InicializaFlecha("Pivotetes1")
flechates2=InicializaFlecha("Pivotetes2")

lanzapivtimer3.TimerFunc=TimerFuncPivotetes
sptes.OnEnter=LanzaFuncPivotetes
sptes.OnLeave=FuncPivotetesStop
