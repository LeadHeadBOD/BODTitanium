##///
##||| DWARF_M3/HOGUERAS.PY TITANIUM
##||| Change list:
##||| * All large fires should now cast shadows properly.
##||| * 
##\\\ 

import Breakings


##################################################
#######-----HOGUERA-EN--LA--SALA--ROTA--1----------------------------#######
##################################################

luz2=Bladex.CreateEntity("Luz2","Entity Spot",-47500,-10150,-44000)
luz2.Color=255,113,10
luz2.Intensity=20
luz2.Precission=0.08


H21=Bladex.CreateEntity("H21","Barril",-47540.699653,-9346.358723,-44105.098534)
H21.Static=0
H21.Scale=1.580459
H21.Orientation=0.068879,0.915567,-0.183464,-0.351188
H21.CatchOnFire (0,0,0)
H21.CastShadows=0

H22=Bladex.CreateEntity("H22","Barril",-48234.733639,-9476.994269,-45141.072357)
H22.Static=0
H22.Scale=1.347849
H22.Orientation=0.585323,0.609276,0.087767,0.527708
H22.CatchOnFire (0,0,0)
H22.CastShadows=0

H23=Bladex.CreateEntity("H23","Barril",-47396.754058,-9928.693112,-44671.741501)
H23.Static=0
H23.Scale=1.000000
H23.Orientation=0.537278,0.346478,0.153138,0.753548
H23.CatchOnFire (0,0,0)
H23.CastShadows=0

o=Bladex.CreateEntity("H24","Hoguera",-48700.790501,-9205.957695,-44370.229440)
o.Static=0
o.Scale=1.244716
o.Orientation=0.683013,0.683013,-0.183013,0.183013
o.FiresIntensity=[ 9 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("H25","Hoguera",-46763.280232,-9151.739223,-43701.130204)
o.Static=0
o.Scale=1.104622
o.Orientation=0.672499,0.672499,-0.218508,0.218508
o.FiresIntensity=[ 7 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



bo=Bladex.CreateEntity("H26","Astillas1",-48179.145707,-9123.914563,-43853.565367)
bo.Static=0
bo.Scale=0.620260
bo.Orientation=0.315135,-0.265598,-0.703211,-0.579346
bo.CastShadows=0

ao=Bladex.CreateEntity("H27","Astillas1",-48084.425353,-9687.207676,-46123.166019)
ao.Static=0
ao.Scale=0.795442
ao.Orientation=0.298790,0.616204,0.401369,0.608211
ao.CastShadows=0


oo=Bladex.CreateEntity("H28","Astillas2",-46668.374198,-9915.697469,-43958.408761)
oo.Static=0
oo.Scale=0.932718
oo.Orientation=0.787435,0.330084,0.484156,-0.191270
oo.CastShadows=0


o=Bladex.CreateEntity("H29","Hoguera",-48275.421469,-9173.720768,-46131.958686)
o.Static=0
o.Scale=1.269735
o.Orientation=0.122788,0.122788,0.696364,-0.696364
o.FiresIntensity=[ 9 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]






##################################################
#######----------------HOGUERA-EN--LA--SALA--ROTA----2----------------#######
##################################################


luzh=Bladex.CreateEntity("Luz2","Entity Spot",-62026.720392,-9992.723457,-2777.438267)
luzh.Color=255,113,10
luzh.Intensity=25
luzh.Precission=0.07        # Changed
# luzh.CastShadows=0        # Commented out

### All tables below added param 'CastShadows=0' -LeadHea
o=Bladex.CreateEntity("NoName0","Hoguera",-61390.575707,-9174.979716,-4072.316189)
o.Static=1
o.Scale=1.459527
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 5 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
o.CastShadows=0


o=Bladex.CreateEntity("NoName1","Hoguera",-63243.500546,-9203.435534,-2950.267202)
o.Static=1
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 5 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
o.CastShadows=0


ho1=Bladex.CreateEntity("NoName2","Barril",-62151.357459,-9399.845442,-4005.192438)
ho1.Static=1
ho1.Scale=1.445076
ho1.Orientation=0.596916,0.497116,0.579230,0.247103
ho1.CatchOnFire (0,0,0)
ho1.CastShadows=0

ho2=Bladex.CreateEntity("NoName3","Barril",-62126.720392,-9792.723457,-2977.438267)
ho2.Static=1
ho2.Scale=2.088246
ho2.Orientation=0.468902,0.795335,0.357454,0.140711
ho2.CatchOnFire (0,0,0)
ho2.CastShadows=0

o=Bladex.CreateEntity("NoName4","Tabla_rota",-63754.383310,-9108.214940,-3586.235052)
o.Static=1
o.Scale=1.361327
o.Orientation=0.403647,0.603264,0.452392,-0.518153
o.CastShadows=0


o=Bladex.CreateEntity("NoName5","Tabla_rota",-62948.465479,-9528.414264,-2148.672211)
o.Static=1
o.Scale=1.269735
o.Orientation=0.555513,0.006717,-0.454134,0.696507
o.CastShadows=0

o=Bladex.CreateEntity("NoName6","Tabla_rota",-67024.518845,-8964.082772,-2283.600187)
o.Static=0
o.Scale=1.780901
o.Orientation=0.638224,0.638224,-0.304417,0.304417
o.CastShadows=0


o=Bladex.CreateEntity("NoName7","Tabla_rota",-67528.293541,-9086.985548,-1945.992105)
o.Static=0
o.Scale=1.711410
o.Orientation=0.236037,0.236037,-0.666548,0.666548
o.CastShadows=0

#################################################
#################################################
#######-----HOGUERA-EN--LA--SALA--DEL--PALACIO-----------------------------###
#################################################

luzhf=Bladex.CreateEntity("Luzhf","Entity Spot",-210500,-15200,14500)
luzhf.Color=255,134,0
luzhf.Intensity=30
luzhf.Precission=0.12

HF1=Bladex.CreateEntity("HF1","Barril",-210800.008263,-14314.841965,14533.878700)
HF1.Static=1
HF1.Scale=1.000000
HF1.Orientation=0.120646,0.867708,-0.389988,-0.283615
HF1.CastShadows=0
HF1.CatchOnFire (0,0,0)


HF2=Bladex.CreateEntity("HF2","Barril",-210236.269787,-14595.315884,14317.549963)
HF2.Static=1
HF2.Scale=1.126825
HF2.Orientation=0.011070,-0.592357,-0.620821,-0.513393
HF2.CastShadows=0
HF2.CatchOnFire (0,0,0)


o=Bladex.CreateEntity("hf3","Hoguera",-210659.722850,-14240.356407,13822.643616)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 8 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("hf4","Hoguera",-210112.662923,-14233.586782,15061.177075)
o.Static=1
o.Scale=1.000000
o.Orientation=0.463904,0.463904,-0.533660,0.533660
o.FiresIntensity=[ 10 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("hf5","Astillas1",-210336.044361,-14267.906140,13808.824809)
o.Static=1
o.Scale=0.590156
o.Orientation=0.347345,-0.406058,0.524781,0.662626


o=Bladex.CreateEntity("hf6","Astillas2",-210530.890898,-14305.824825,15044.248204)
o.Static=1
o.Scale=0.861349
o.Orientation=0.199917,-0.817861,-0.521058,0.140124


o=Bladex.CreateEntity("hf7","Astillas2",-210630.277008,-14754.963945,14714.427558)
o.Static=1
o.Scale=0.518548
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("hf8","Rama1",-209901.077608,-14166.825824,14390.617818)
o.Static=1
o.Scale=0.720103
o.Orientation=0.902585,0.430511,0.000000,0.000000



import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fogatas.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("Fuego1")
darfuncs.FireOnGS("Fuego2")
darfuncs.FireOnGS("Fuego3")
darfuncs.FireOnGS("Fuego4")
darfuncs.FireOnGS("Fuego5")
darfuncs.FireOnGS("Fuego6")

