##///
##||| Ragnar_M2/Objs.PY TITANIUM
##||| Change list:
##||| * Spark pass
##||| * Shadow pass
##||| * Removed selection data from some inconsequential items
##||| * Added glitter to final pergament to make it obvious wtf you're supposed to do
##\\\ 

import Sparks
import pocimac
import time
import Bladex
import Breakings
import darfuncs
import ItemTypes



#########
#####zocalosuelo de la trampa de los pendulos
##########################

o=Bladex.CreateEntity("zoc1","ZocaloSuelo",-123510.991437,3710.105167,-98732.730845,"Physic")
o.Scale=2.026831
o.Orientation=0.707107,-0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("zoc2","ZocaloSuelo",-119250.991437,3710.105167,-98732.730845,"Physic")
o.Scale=2.026831
o.Orientation=0.707107,-0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

###########################
#####adoquines pulsadores invisibles
###########################

adoq=Bladex.CreateEntity("Adoq0","Adoquinpulsador",-114811.969703,9465.504458,82328.308119)
adoq.Scale=2.238882
adoq.Orientation=0.500000,0.500000,0.500000,-0.500000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq1","Adoquinpulsador",-108168.938581,2670.593059,-96009.186299)
adoq.Scale=2.786772
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq2","Adoquinpulsador",-99929.516426,2803.062968,-100021.905347)
adoq.Scale=3.235356
adoq.Orientation=0.495618,0.495618,0.504344,-0.504344
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq3","Adoquinpulsador",-101864.166895,3184.377233,69259.401772)
adoq.Scale=4.769311
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq4","Adoquinpulsador",-111959.533478,3156.364654,69277.992719)
adoq.Scale=4.629047
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq5","Adoquinpulsador",-116467.320555,12588.166303,57909.514583)
adoq.Scale=3.538461
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq6=Bladex.CreateEntity("Adoq6","Adoquinpulsador",-103258.305, -10795.363, 39197.878)
adoq6.Scale=4
adoq6.Orientation=0.500000,0.500000,0.500000,-0.500000
adoq6.CastShadows=0
adoq6.Alpha = 0

adoq7=Bladex.CreateEntity("Adoq7","Adoquinpulsador",-104455.734588, 3754.46326715, -70506.2147314)
adoq7.Scale=7
adoq7.Orientation=0.707107,0.707107,0.000000,0.000000
adoq7.CastShadows=0
adoq7.Alpha = 0

o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-147117.351619,-696.746714,-91747.831717)
o.Scale=2.329790
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-147089.146041,-692.737044,-99243.738101)
o.Scale=2.329790
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-147132.559519,-727.007085,-106744.188411)
o.Scale=2.329790
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName4","Adoquinpulsador",-148954.401064,-33675.310466,-111095.917374)
o.Scale=3.047852
o.Orientation=0.270598,-0.653282,0.653282,-0.270598
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName5","Adoquinpulsador",-150211.564573,-33673.374221,-112348.978780)
o.Scale=3.047852
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName6","Adoquinpulsador",-150186.752146,-33671.245402,-115693.209228)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName7","Adoquinpulsador",-148924.461337,-33698.606537,-116924.898170)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName8","Adoquinpulsador",-145511.831169,-33690.606643,-116850.070978)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName9","Adoquinpulsador",-144383.646789,-33684.617877,-115734.169259)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName10","Adoquinpulsador",-140374.272744,-33883.110637,-116939.473162)
o.Scale=3.718959
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName11","Adoquinpulsador",-136117.873611,-33884.296113,-116974.152290)
o.Scale=3.718959
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName12","Adoquinpulsador",-131627.905504,-33894.692587,-116939.747398)
o.Scale=3.718959
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName13","Adoquinpulsador",-127235.752211,-33898.442472,-116942.721218)
o.Scale=3.718959
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName14","Adoquinpulsador",-123209.561369,-34439.435174,-115412.143032)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName15","Adoquinpulsador",-117279.960521,-34461.141235,-115382.525988)
o.Scale=3.047852
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-80725.000000,4475.000000,-98500.000000)
o.Scale=3.047852
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-80725.000000,4475.000000,-100000.000000)
o.Scale=3.047852
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-73994.317959,17876.306163,71139.509484)
o.Scale=3.538461
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-120207.106000,-1000.000000,52003.221000)
o.Scale=5.113347
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-120200.000000,-1000.000000,57987.972000)
o.Scale=5.113347
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvFinal","Adoquinpulsador",-136830.754149, -32684.409636, -94109.189557)
o.Scale=3.366725
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqAlcantUlt","Adoquinpulsador",-111737.935747,7240.285673,48742.580144)
o.Scale=3.078330
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqAlcant1","Adoquinpulsador",-78750.000000,12740.000000,81500.000000)
o.Scale=3.078330
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqAlcant2","Adoquinpulsador",-88760.000000,12740.000000,81500.000000)
o.Scale=3.078330
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqAlcant3","Adoquinpulsador",-101775.000000,12740.000000,81500.000000)
o.Scale=3.078330
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqAlcant4","Adoquinpulsador",-162227.614457,10380.016430,66064.120356)
o.Scale=5.164481
o.Orientation=0.632814,0.315509,0.315509,0.632814
o.CastShadows=0
o.Alpha = 0





##########################
o=Bladex.CreateEntity("NoName0","Vigaro1",-76962.648000,2958.930000,78964.017000,"Physic")
o.Scale=1.160969
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Vigaro1",-80146.788000,2840.566000,77340.920000,"Physic")
o.Scale=1.138093
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


rej7=Bladex.CreateEntity("Rej7","Reja",-111712.650000,2187.333000,69200.916000,"Physic")
rej7.Scale=2.376619
rej7.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling("Rej7")


o=Bladex.CreateEntity("NoName1","Farol2",-94789.134000,-10826.347000,70277.276000,"Physic")
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.10000,(255,175,87)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Polea",-94771.641000,-12725.546000,71099.341000,"Physic")
o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Cuerda",-94788.089000,-11877.454000,70242.607000,"Physic")
o.Scale=0.951466
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Roca1Aurelio",-125995.726000,17683.468000,49025.515000,"Physic")
o.Scale=2.173037
o.Orientation=0.762153,0.300220,-0.533666,0.210216
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





o=Bladex.CreateEntity("NoName0","Vigaro2",-122912.910000,-10056.400000,55232.011000,"Physic")
o.Scale=0.720103
o.Orientation=0.459229,0.459229,0.537688,-0.537688
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Vigaro1",-121923.897000,-9169.846000,55142.741000,"Physic")
o.Scale=0.528971
o.Orientation=0.893265,-0.054634,0.035008,-0.444822
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión








rej8=Bladex.CreateEntity("Rej8","Reja",-118483.588000,-4881.410000,51990.926000,"Physic")
rej8.Scale=1.909366
rej8.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling("Rej8")


rej9=Bladex.CreateEntity("Rej9","Reja",-118547.347000,-4858.762000,57853.977000,"Physic")
rej9.Scale=2.283884
rej9.Orientation=0.703642,0.004422,0.710541,0.000247
Sparks.SetMetalSparkling("Rej9")





o=Bladex.CreateEntity("NoName0","Lamparatecho",-83758.916000,-8833.457000,39530.549000,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 7 ]
o.Lights=[ (30.000000,0.070000,(255,142,17)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-83480.841000,-8891.878000,46913.238000,"Physic")
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 12 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName4","Cuerda",-83470.548000,-9741.384000,46912.540000,"Physic")
o.Scale=0.923483
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Cuerda",-83473.653000,-11193.373000,46919.189000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Cuerda",-83470.412000,-12190.010000,46924.259000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




tab3=Bladex.CreateEntity("tab3","Taburete",-85425.433000,-5594.046000,37639.883000,"Weapon")
tab3.Scale=1.000000
tab3.Orientation=0.707107,0.707107,0.000000,0.000000


tab4=Bladex.CreateEntity("tab4","Taburete",-82226.622000,-5602.052000,37531.809000,"Weapon")
tab4.Scale=1.000000
tab4.Orientation=0.707107,0.707107,0.000088,-0.000088


o=Bladex.CreateEntity("NoName0","Farol2",-93576.934000,-9140.024000,36952.512000,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 5 ]                              # Changed
o.Lights=[ (22.000000,0.500000,(255,165,64)) ]      #
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Hoguera",-80068.409000,-3230.580000,28564.904000,"Physic")
o.Scale=1.834864
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(206,92,0)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



o=Bladex.CreateEntity("NoName0","Lamparatecho",-100480.672000,-8755.629000,8676.156000,"Physic")
o.Scale=2.548057
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (25.000000,0.031250,(249,131,0)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Amuleto",-100419.809000,-13123.632000,8680.694000,"Physic")
o.Scale=3.140205
o.Orientation=0.999962,0.008727,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Cuerda",-100479.084000,-11793.759000,8675.964000,"Physic")
o.Scale=1.711410
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


rej10=Bladex.CreateEntity("Rej10","Reja",-161624.874000,9750.631000,65510.990000,"Physic")
rej10.Scale=3.333391
rej10.Orientation=0.464179,0.820433,-0.164374,0.290531
Sparks.SetMetalSparkling("Rej10")


can1=Bladex.CreateEntity("Can1","Candelabro",-99732.192000,-1062.979000,12723.304000,"Physic")
can1.Scale=1.000000
can1.Orientation=0.707107,0.707107,0.000000,0.000000
can1.FiresIntensity=[ 9 ]
can1.Lights=[ (0.000000,0.031250,(129,254,238)) ]
Sparks.SetSparkling("Can1")


can2=Bladex.CreateEntity("Can2","Candelabro",-101239.325000,-1061.935000,13087.211000,"Physic")
can2.Scale=1.000000
can2.Orientation=0.435338,0.435338,-0.557208,0.557208
can2.FiresIntensity=[ 14 ]
can2.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can2")





o=Bladex.CreateEntity("NoName5","Candelpeque",-106556.520000,-1089.372000,12865.995000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 11 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


can3=Bladex.CreateEntity("Can3","Candelabro",-108182.480000,-1060.742000,12685.552000,"Physic")
can3.Scale=1.000000
can3.Orientation=0.707107,0.707107,0.000000,0.000000
can3.FiresIntensity=[ 9 ]
can3.Lights=[ (0.000000,0.031250,(254,219,171)) ]
Sparks.SetSparkling("Can3")


can4=Bladex.CreateEntity("Can4","Candelabro",-108979.553000,-910.460000,12644.791000,"Physic")
can4.Scale=0.861349
can4.Orientation=0.545621,0.545621,0.449775,-0.449775
can4.FiresIntensity=[ 11 ]
can4.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can4")


can5=Bladex.CreateEntity("Can5","Candelabro",-106850.949000,-1062.063000,4984.534000,"Physic")
can5.Scale=1.000000
can5.Orientation=0.541675,0.541675,0.454519,-0.454519
can5.FiresIntensity=[ 13 ]
can5.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can5")


can6=Bladex.CreateEntity("Can6","Candelabro",-101372.153000,-1062.019000,4687.476000,"Physic")
can6.Scale=1.000000
can6.Orientation=0.707107,0.707107,0.000000,0.000000
can6.FiresIntensity=[ 10 ]
can6.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can6")


can7=Bladex.CreateEntity("Can7","Candelabro",-99735.815000,-859.579000,4879.791000,"Physic")
can7.Scale=0.811430
can7.Orientation=0.241845,0.241845,0.664463,-0.664463
can7.FiresIntensity=[ 12 ]
can7.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can7")


o=Bladex.CreateEntity("NoName11","Candelpeque",-100506.338000,-274.572000,4335.450000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 10 ]
o.Lights=[ (0.000000,0.031250,(134,243,255)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName12","Velon",-107012.123000,-964.000000,12744.525000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 12 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName13","Velon",-101761.013000,-779.154000,12419.447000,"Physic")
o.Scale=1.000000
o.Orientation=0.710103,0.701985,-0.050617,0.020217
o.FiresIntensity=[ 6 ]
o.Lights=[ (0.000000,0.031250,(255,165,66)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName0","Braseroarana",-89692.470000,3114.969000,-21285.176000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.000000,0.031250,(183,253,255)) ]
Sparks.SetMetalSparkling(o.Name)                # Add








o=Bladex.CreateEntity("NoName1","Lamparatecho",-86620.836000,-8820.901000,9348.219000,"Physic")
o.Scale=3.171607
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.031250,(255,162,36)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Vigaro1",-107216.575000,-23221.088000,-39841.132000,"Physic")
o.Scale=2.353088
o.Orientation=0.513069,-0.495465,0.486892,-0.504192
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Farol2",-113443.159000,-3127.287000,-78359.457000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.400000,(255,166,68)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Monjespada",-126443.785000,-5210.966000,8744.171000,"Physic")
o.Scale=2.678033
o.Orientation=0.500000,0.500000,-0.500000,0.500000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Monjespada",-125449.346000,-6431.841000,10707.757000,"Physic")
o.Scale=2.958216
o.Orientation=0.580552,0.611774,-0.369853,0.389743
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Monjespada",-125460.390000,-6463.633000,7033.990000,"Physic")
o.Scale=2.928926
o.Orientation=0.328029,0.377355,-0.568164,0.653598
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Lamparatecho",-120608.909000,-9327.543000,8665.024000,"Physic")
o.Scale=2.067571
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.031250,(219,115,0)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Roca1Aurelio",-82642.817000,4361.435000,-75757.932000,"Physic")
o.Scale=2.731862
o.Orientation=0.694088,-0.097548,0.706309,0.099265
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





o=Bladex.CreateEntity("NoName1","Cuerda",-86627.811000,-12603.043000,9363.993000,"Physic")
o.Scale=2.238882
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Cuerda",-86627.450000,-15923.413000,9365.026000,"Physic")
o.Scale=2.238882
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Viga",-111957.208000,-6488.424000,-46126.729000,"Physic")
o.Scale=2.216715
o.Orientation=0.500000,0.500000,-0.500000,0.500000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Viga",-112188.254000,-6282.441000,-43395.998000,"Physic")
o.Scale=2.731862
o.Orientation=0.500000,0.500000,-0.500000,0.500000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




rej11=Bladex.CreateEntity("Rej11","Reja",-101118.759000,-5903.650000,63275.404000,"Physic")
rej11.Scale=1.928460
rej11.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rej11")


rej12=Bladex.CreateEntity("Rej12","Reja",-111670.895000,-5755.676000,62688.579000,"Physic")
rej12.Scale=1.745810
rej12.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rej12")


o=Bladex.CreateEntity("NoName9","Varillaancha",-93559.171000,-10112.208000,36925.422000,"Physic")
o.Scale=0.555954
o.Orientation=0.504344,0.504344,-0.495618,-0.495618
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName10","Cuerda",-83757.244000,-12230.419000,39538.507000,"Physic")
o.Scale=1.138093
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName11","Cuerda",-83757.244000,-10440.419000,39538.507000,"Physic")
o.Scale=1.138093
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Farol2",-108931.999000,-1974.360000,-86259.390000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(177,250,254)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o=Bladex.CreateEntity("NoName0","Tronco",-113367.691000,-4647.138000,-77822.724000,"Physic")
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName2","Cuerda",-113434.792000,-4107.310000,-78405.280000,"Physic")
o.Scale=0.905287
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Cuerda",-108920.019000,-3199.766000,-86289.381000,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Cuerda",-120601.536000,-11763.782000,8672.631000,"Physic")
o.Scale=1.533978
o.Orientation=0.425547,0.425547,0.564721,-0.564721
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


rej13=Bladex.CreateEntity("Rej13","Reja",-99879.256000,2145.429000,-99642.975000,"Physic")
rej13.Scale=1.596263
rej13.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling("Rej13")


rej14=Bladex.CreateEntity("Rej14","Reja",-112986.401000,2122.844000,-96006.652000,"Physic")
rej14.Scale=2.088246
rej14.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling("Rej14")


rej15=Bladex.CreateEntity("Rej15","Reja",-108277.011000,2118.474000,-96011.981000,"Physic")
rej15.Scale=2.067570
rej15.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling("Rej15")

""" ### PLAGUE: Maybe restore? Massive rock in cliff by drawbridge
o=Bladex.CreateEntity("NoName3","Roca1Aurelio",-69924.092000,25005.126000,-64139.908000,"Physic")
o.Scale=8.838547
o.Orientation=0.930418,0.366501,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión
"""





o=Bladex.CreateEntity("NoName0","Lamparatecho",-125496.250000,-2513.557000,-106537.181000,"Physic")
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.170000,(255,156,47)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Lamparatecho",-140972.664000,-2586.927000,-91622.137000,"Physic")
o.Scale=2.151522
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.200000,(255,166,68)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



o=Bladex.CreateEntity("NoName5","Amuleto",-142682.915000,-20290.943000,-95203.433000,"Physic")
o.Scale=2.109128
o.Orientation=0.999391,-0.034899,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Roca1Aurelio",-115992.073000,5750.621000,-90268.399000,"Physic")
o.Scale=2.759181
o.Orientation=0.917060,0.398749,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-134168.948000,-16625.767000,-111642.927000,"Physic")
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.170000,(255,135,2)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Vigaro1",-127517.599000,8256.864000,-102517.457000,"Physic")
o.Scale=1.000000
o.Orientation=0.463904,0.463904,0.533660,-0.533660
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Vigaro1",-127664.593000,7981.262000,-94795.611000,"Physic")
o.Scale=1.000000
o.Orientation=0.459229,0.459229,0.537688,-0.537688
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName7","Vigaro1",-121699.511000,9464.109000,-89367.310000,"Physic")
o.Scale=1.503752
o.Orientation=0.170033,0.121892,-0.447130,0.869659
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName8","Vigaro1",-126593.423000,10126.342000,-89774.887000,"Physic")
o.Scale=1.295256
o.Orientation=0.049325,0.049325,0.705384,-0.705384
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Roca1Aurelio",-131178.184000,20540.392000,-111555.694000,"Physic")
o.Scale=2.987797
o.Orientation=0.800235,-0.307181,0.480829,0.184573
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName8","Braseroarana",-123394.011000,-5903.310000,-91629.323000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.070000,(255,149,32)) ]
Sparks.SetMetalSparkling(o.Name)        # Add








o=Bladex.CreateEntity("NoName0","Farol2",-133565.706000,-12597.569000,-101297.404000,"Physic")
o.Scale=1.093685
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,151,36)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Farol2",-133271.291000,-5480.563000,-100290.563000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Varillaancha",-133587.574000,-13430.817000,-101326.523000,"Physic")
o.Scale=0.632728
o.Orientation=0.495618,0.495618,-0.504344,-0.504344
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Cuerda",-87064.015000,-4606.380000,-18571.672000,"Physic")
o.Scale=1.947745
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-87064.015000,-2576.380000,-18571.672000,"Physic")
o.Scale=1.947745
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.031250,(255,168,72)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




ala1=Bladex.CreateEntity("Ala1","Alabarda",-135011.036302,-13036.605184,-107486.726762,"Weapon")
ala1.Scale=1.000000
ala1.Orientation=0.0253700278699,-0.156822443008,0.771470606327,0.616113781929



ala2=Bladex.CreateEntity("Ala2","Alabarda",-132468.175087,-12823.281434,-107518.086246,"Weapon")
ala2.Scale=1.000000
ala2.Orientation=0.442370,-0.806131,-0.342445,-0.192852





o=Bladex.CreateEntity("NoName8","Lamparatecho",-124703.582000,-17090.285000,-101919.426000,"Physic")
o.Scale=2.497850
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (30.000000,0.100000,(255,147,28)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Cuerda",-124703.582000,-19280.285000,-101919.426000,"Physic")
o.Scale=2.261271
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Farol2",-132541.796000,-18023.518000,-101373.075000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,146,26)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Lamparatecho",-141721.227000,-25858.273000,-109995.551000,"Physic")
o.Scale=1.763268
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.260000,(255,145,21)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Cuerda",-141721.227000,-26778.273000,-109995.551000,"Physic")
o.Scale=1.763268
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Cuerda",-124764.636000,-27227.805000,-110061.642000,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Lamparatecho",-124764.636000,-26157.805000,-110061.642000,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.070000,(173,112,29)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Farol2",-131104.620000,-23329.508000,-100923.999000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,153,40)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Varillaancha",-131118.520000,-24293.734000,-100959.744000,"Physic")
o.Scale=0.433516
o.Orientation=0.495618,0.495618,-0.504344,-0.504344
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Varillaancha",-124728.280000,-28115.146000,-104712.890000,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Varillaancha",-141661.643000,-27081.772000,-100400.633000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Lampcolg",-141699.174000,-26603.158000,-100363.734000,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.200000,(255,162,57)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión










o=Bladex.CreateEntity("NoName2","Varillaancha",-132552.956000,-19152.589000,-101404.299000,"Physic")
o.Scale=0.584313
o.Orientation=0.491198,0.491198,-0.508650,-0.508650
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Lamparatecho",-125569.285000,-9029.787000,-108668.778000,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.270000,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-141005.932000,-9135.706000,-108655.498000,"Physic")
o.Scale=1.459527
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.270000,(255,143,19)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






can8=Bladex.CreateEntity("Can8","Candelabro",-143738.170000,-6312.203000,-91775.771000,"Physic")
can8.Scale=1.000000
can8.Orientation=0.621418,0.621418,0.337402,-0.337402
can8.FiresIntensity=[ 8 ]
can8.Lights=[ (7.000000,0.231250,(255,196,128)) ]
Sparks.SetSparkling("Can8")


can9=Bladex.CreateEntity("Can9","Candelabro",-144040.469000,-6312.145000,-89209.382000,"Physic")
can9.Scale=1.000000
can9.Orientation=0.533660,0.533660,0.463904,-0.463904
can9.FiresIntensity=[ 18 ]
can9.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can9")








can10=Bladex.CreateEntity("Can10","Candelabro",-126293.036000,-23583.752000,-88236.616000,"Physic")
can10.Scale=1.000000
can10.Orientation=0.707107,0.707107,0.000000,0.000000
can10.FiresIntensity=[ 3 ]
can10.Lights=[ (7.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can10")


can11=Bladex.CreateEntity("Can11","Candelabro",-122813.625000,-23566.653000,-87937.882000,"Physic")
can11.Scale=1.000000
can11.Orientation=0.707107,0.707107,0.000000,0.000000
can11.FiresIntensity=[ 3 ]
can11.Lights=[ (5.000000,0.031250,(255,196,128)) ]
Sparks.SetSparkling("Can11")


o=Bladex.CreateEntity("NoName0","Lamparatecho",-147143.133000,-37021.414000,-113437.319000,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.200000,(255,149,32)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-120487.510000,-37041.250000,-113608.876000,"Physic")
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.100000,(255,146,26)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Tapiz2",-134859.019000,-15807.643000,-106303.532000,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Tapiz3",-132319.667000,-15763.147000,-106324.353000,"Physic")
o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Farol2",-133351.558000,-28928.987000,-101296.615000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,174,85)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Varillaancha",-133368.178000,-29568.785000,-101308.084000,"Physic")
o.Scale=0.545000
o.Orientation=0.491198,0.491198,-0.508650,-0.508650
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Garfio2",-133279.754000,-5985.575000,-100290.775000,"Physic")
o.Scale=1.000000
o.Orientation=0.055479,0.055479,-0.704927,0.704927
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName10","Viga",-133285.193000,-5914.011000,-99833.637000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName13","Lamparatecho",-122411.208000,-3158.586000,-34280.290000,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (30.000000,0.070000,(255,151,36)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName14","Cuerda",-122411.208000,-4308.586000,-34280.290000,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Farol2",-82544.879000,-9512.261000,-38496.446000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Varillaancha",-82546.408000,-10516.153000,-38522.990000,"Physic")
o.Scale=0.539604
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Varillaancha",-75030.557000,-4682.054000,-30358.936000,"Physic")
o.Scale=0.727304
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Farol2",-75080.557000,-3282.054000,-30348.936000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,169,74)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName2","Roca1Aurelio",-159954.419000,11802.635000,16961.380000,"Physic")
o.Scale=1.853212
o.Orientation=0.948324,-0.317305,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






o=Bladex.CreateEntity("NoName0","Lamparatecho",-88540.799000,-13049.269000,-2916.922000,"Physic")
o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.20000,(255,156,47)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






o=Bladex.CreateEntity("NoName2","Roca1Aurelio",-133566.766000,6064.177000,32258.877000,"Physic")
o.Scale=1.172579
o.Orientation=0.564863,-0.099601,0.806707,0.142244
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






o=Bladex.CreateEntity("NoName0","Cubo",-112193.503000,8780.941000,83742.553000,"Physic")
o.Scale=1.000000
o.Orientation=0.289526,0.040690,-0.955722,-0.033375
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



tab1=Bladex.CreateEntity("tab1","Taburete",-114305.839850,8649.969040,69255.033640,"Weapon")
tab1.Scale=1.000000
tab1.Orientation=0.602263,0.093429,-0.785597,0.106714



o=Bladex.CreateEntity("NoName1","Viga",-102472.049000,3553.616000,-69541.229000,"Physic")
o.Scale=2.109128
o.Orientation=0.018510,0.018510,-0.706864,0.706864
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Viga",-106325.884000,3618.987000,-69657.034000,"Physic")
o.Scale=2.151522
o.Orientation=0.018510,0.018510,-0.706864,0.706864
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






ras1=Bladex.CreateEntity("Ras1","Rastrillo",-89327.744000,-1142.983000,75761.184000,"Physic")
ras1.Scale=1.308209
ras1.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Ras1")


ras2=Bladex.CreateEntity("Ras2","Rastrillo",-100982.133000,-566.607000,76075.492000,"Physic")
ras2.Scale=1.115668
ras2.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Ras2")


ras3=Bladex.CreateEntity("Ras3","Rastrillo",-111635.362000,-905.238000,75242.329000,"Physic")
ras3.Scale=1.184304
ras3.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Ras3")


ras4=Bladex.CreateEntity("Ras4","Rastrillo",-78763.533000,-449.333000,76284.328000,"Physic")
ras4.Scale=1.172579
ras4.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Ras4")

""" ### PLAGUE: I actually quite like these, but not sure if I will restore them.
o=Bladex.CreateEntity("NoName1","Vigaro1",-134660.944000,-50452.611000,-105767.833000,"Physic")
o.Scale=2.497850
o.Orientation=0.968148,-0.250380,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Vigaro1",-134877.966000,-42531.090000,-111582.127000,"Physic")
o.Scale=2.306723
o.Orientation=0.390731,0.920505,0.000000,0.000000
# o.NodesOrientation=?  En la siguiente versión
# o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Vigaro1",-138190.706000,-41631.097000,-95496.094000,"Physic")
o.Scale=1.474123
o.Orientation=0.017399,-0.996765,-0.078447,-0.001369
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Vigaro1",-133679.496000,-38180.441000,-95759.442000,"Physic")
o.Scale=1.503752
o.Orientation=0.121869,-0.992546,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Vigaro1",-126097.481000,-36601.682000,-89695.639000,"Physic")
o.Scale=1.000000
o.Orientation=0.662620,-0.748956,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Vigaro1",-131919.624000,-36515.070000,-89527.911000,"Physic")
o.Scale=1.000000
o.Orientation=0.662620,-0.748956,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión
"""

o=Bladex.CreateEntity("NoName3","Varillaancha",-131932.811000,-36657.227000,-90017.379000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


rej16=Bladex.CreateEntity("Rej16","Reja",-103228.305000,-11785.363000,39197.878000,"Physic")
rej16.Scale=1.711410
rej16.Orientation=0.999962,-0.008727,0.000000,0.000000
Sparks.SetMetalSparkling("Rej16")


o=Bladex.CreateEntity("NoName1","Viga",-107172.239000,-24208.907000,37912.348000,"Physic")
o.Scale=4.675337
o.Orientation=0.508650,0.508650,-0.491198,0.491198
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Viga",-106389.774000,-24455.633000,41619.269000,"Physic")
o.Scale=4.027099
o.Orientation=0.521334,0.521334,-0.477714,0.477714
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



o=Bladex.CreateEntity("NoName0","Reja",-89163.321000,-7812.105000,47205.168000,"Physic")
o.Scale=2.400385
o.Orientation=0.495618,0.495618,0.504344,-0.504344
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión







ras5=Bladex.CreateEntity("Ras5","Rastrillo10",-152488.852000,8635.028000,22124.540000) # esteeeeeeeeeeeeeeeeeeeeeeeeeeeeee
ras5.Scale=1.909367
ras5.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Ras5")




o=Bladex.CreateEntity("NoName3","Reja",-114890.192000,9071.480000,82257.153000,"Physic")
o.Scale=1.334504
o.Orientation=0.999962,0.008727,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





o=Bladex.CreateEntity("NoName2","Reja",-101558.187000,-4810.465000,46884.039000,"Physic")
o.Scale=2.424389
o.Orientation=1.000000,0.000000,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




o=Bladex.CreateEntity("NoName0","Roca1Aurelio",-115106.039000,4609.818000,53795.798000,"Physic")
o.Scale=1.149474
o.Orientation=0.621418,0.621418,0.337402,-0.337402
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





ras6=Bladex.CreateEntity("Ras6","Rastrillo",-117466.067000,-10063.537000,69243.760000,"Physic")
ras6.Scale=1.160969
ras6.Orientation=0.512917,0.512917,0.486740,-0.486740
Sparks.SetMetalSparkling("Ras6")

### PLAGUE: Wtf was this supposed to be?
#o=Bladex.CreateEntity("NoName1","",-128506.556000,-9010.295000,60361.028000,"Physic")
#o.Scale=2.814640
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


ras7=Bladex.CreateEntity("Ras7","Rastrillo",-118159.206000,-416.182000,69302.137000,"Physic")
ras7.Scale=1.232392
ras7.Orientation=0.499924,-0.491274,0.508726,0.499924
Sparks.SetMetalSparkling("Ras7")


o=Bladex.CreateEntity("NoName3","Varillaancha",-126199.489000,892.060000,60559.480000,"Physic")
o.Scale=3.078330
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Varillaancha",-125911.404000,-290.452000,60364.893000,"Physic")
o.Scale=2.928926
o.Orientation=0.713250,0.700909,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName0","Varillaancha",-129926.626000,-33263.683000,-115758.862000,"Physic")
o.Scale=2.651518
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Caliz",-83281.716000,-6399.714000,37282.265000,"Weapon")
o.Scale=1.000000
o.Orientation=0.701752,0.683614,0.161187,-0.119311
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Caliz",-83451.344000,-6411.821000,37904.904000,"Weapon")
o.Scale=1.000000
o.Orientation=0.354868,0.688562,0.361812,0.518693
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Caliz",-83818.450000,-6396.275000,39141.647000,"Weapon")
o.Scale=1.000000
o.Orientation=0.698754,0.692993,0.123860,-0.127131
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Candelpeque",-83994.283000,-6573.909000,36914.059000,"Physic")
o.Scale=1.000000
o.Orientation=0.706062,0.708035,0.010720,-0.006925
o.FiresIntensity=[ 14 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Mortero",-83949.907000,-6650.553000,54306.807000,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName7","Mortero",-84452.283000,-6681.608000,54085.405000,"Weapon")
o.Scale=1.000000
o.Orientation=0.228171,0.816410,-0.529826,0.026417
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName8","Cazo",-83815.106000,-6677.493000,53897.541000,"Weapon")
o.Scale=1.000000
o.Orientation=0.852931,0.500386,-0.121225,0.086182
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName11","Caliz",-83569.204000,-6394.254000,39555.714000,"Weapon")
o.Scale=1.000000
o.Orientation=0.709960,0.703571,0.023895,-0.019348
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName12","Cuchillo",-83317.390000,-6409.049000,38873.681000,"Weapon")
o.Scale=1.000000
o.Orientation=0.434639,0.900047,0.016921,0.026798
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName13","Palangana",-83933.104000,-6446.048000,38004.481000,"Physic")
o.Scale=1.000000
o.Orientation=0.714709,0.699015,0.012852,-0.020099
o.FiresIntensity=[ 41 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName14","Tronco",-82882.050000,-5388.191000,54123.958000,"Physic")
o.Scale=0.811430
o.Orientation=0.704378,0.700160,-0.085147,-0.079856
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName15","Tronco",-83086.161000,-5365.169000,54135.310000,"Physic")
o.Scale=0.741923
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName16","Tronco",-82998.020000,-5553.169000,54145.568000,"Physic")
o.Scale=0.795442
o.Orientation=0.704818,0.699598,0.080516,0.085509
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName17","Tronco",-82667.010000,-5338.198000,54184.790000,"Physic")
o.Scale=0.741923
o.Orientation=0.350165,0.353545,-0.616227,-0.610454
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName18","Tronco",-82754.411000,-5535.018000,54171.505000,"Physic")
o.Scale=0.741923
o.Orientation=0.693668,0.689421,-0.153352,-0.141442
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName19","Tronco",-82856.414000,-5685.284000,54142.576000,"Physic")
o.Scale=0.741923
o.Orientation=0.685747,0.685437,-0.177834,-0.168231
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName20","Palangana",-84161.751000,-6448.760000,39888.848000,"Physic")
o.Scale=1.000000
o.Orientation=0.720104,0.693326,0.021944,-0.016377
o.FiresIntensity=[ 26 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName21","Femur",-113673.073000,8977.261000,83561.594000,"Weapon")
o.Scale=1.051010
o.Orientation=0.044825,0.913039,-0.071148,-0.399109
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName22","Femur",-114858.533000,8979.738000,83478.221000,"Weapon")
o.Scale=1.000000
o.Orientation=0.026234,0.938915,-0.018931,-0.342625
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName23","Femur",-114303.578000,8976.159000,83965.043000,"Weapon")
o.Scale=1.000000
o.Orientation=0.013527,0.821976,0.011310,-0.569249
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName24","Skull",-113666.278000,8900.937000,83880.435000,"Weapon")
o.Scale=1.000000
o.Orientation=0.758612,0.021883,-0.142220,0.635455
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName25","Skull",-113644.604000,8887.987000,84851.060000,"Weapon")
o.Scale=1.000000
o.Orientation=0.308649,0.678417,-0.560941,-0.360322
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName27","Varillaancha",-137373.995000,-33334.664000,-115698.348000,"Physic")
o.Scale=2.522829
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Lamparatecho",-94741.241000,-2789.847000,-74951.352000,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.031250,(255,167,70)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Cuerda",-94741.241000,-4879.847000,-74931.352000,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión




ala3=Bladex.CreateEntity("Ala3","Alabarda",-138454.953813,370.054609,-99203.261443,"Weapon")
ala3.Scale=1.000000
ala3.Orientation=0.089400,-0.492165,0.686857,0.527266







o=Bladex.CreateEntity("NoName18","Tapiz2",-125870.993000,-1953.974000,-21432.475000,"Physic")
o.Scale=1.564811
o.Orientation=0.495618,0.495618,-0.504344,0.504344
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





o=Bladex.CreateEntity("NoName28","Tapiz3",-125809.236000,-1988.213000,-27407.419000,"Physic")
o.Scale=1.661078
o.Orientation=0.495618,0.495618,-0.504344,0.504344
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión





o=Bladex.CreateEntity("NoName3","Femur",-98398.500000,8974.017000,83434.896000,"Weapon")
o.Scale=1.000000
o.Orientation=0.072258,0.987150,-0.091710,0.109097
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Femur",-98287.359000,8979.608000,83946.740000,"Weapon")
o.Scale=1.000000
o.Orientation=0.038617,0.956892,-0.091103,-0.273070
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Femur",-98842.815000,8976.739000,82870.209000,"Weapon")
o.Scale=1.000000
o.Orientation=0.004289,0.481403,-0.044739,-0.875346
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Femur",-97805.741000,8978.459000,83566.328000,"Weapon")
o.Scale=1.000000
o.Orientation=0.035036,0.947924,-0.030363,-0.315105
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


rej1=Bladex.CreateEntity("Rej1","Reja",-88690.094000,12974.865000,81888.668000,"Physic")
rej1.Scale=2.261271
rej1.Orientation=0.500000,0.500000,-0.500000,-0.500000
Sparks.SetMetalSparkling("Rej1")


rej2=Bladex.CreateEntity("Rej2","Reja",-78740.906000,12601.524000,81396.704000,"Physic")
rej2.Scale=1.986894
rej2.Orientation=0.500000,0.500000,-0.500000,-0.500000
Sparks.SetMetalSparkling("Rej2")


rej3=Bladex.CreateEntity("Rej3","Reja",-101717.098000,12325.590000,82000.335000,"Physic")
rej3.Scale=2.329790
rej3.Orientation=0.500000,0.500000,-0.500000,-0.500000
Sparks.SetMetalSparkling("Rej3")





o=Bladex.CreateEntity("NoName2","Candelpeque",-123423.377000,-23282.324000,-112717.571000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 16 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Candelpeque",-124401.753000,-23275.968000,-112610.646000,"Physic")
o.Scale=1.000000
o.Orientation=0.624338,0.624338,0.331967,-0.331967
o.FiresIntensity=[ 24 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Skull",-123826.544000,-23122.405000,-112448.701000,"Weapon")
o.Scale=1.000000
o.Orientation=0.708434,0.152872,0.562971,-0.397260
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


tab2=Bladex.CreateEntity("tab2","Taburete",-123645.828000,-22352.917000,-111828.643000,"Weapon")
tab2.Scale=1.000000
tab2.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName7","Candelpeque",-126573.450000,-23286.747000,-112346.992000,"Physic")
o.Scale=1.000000
o.Orientation=0.609264,0.609264,0.358884,-0.358884
o.FiresIntensity=[ 26 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión






o=Bladex.CreateEntity("NoName3","Peanapiedra",-140494.277000,-14376.629000,-91202.618000,"Physic")
o.Scale=3.078330
o.Orientation=0.018510,0.018510,0.706864,-0.706864
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Peanapiedra",-145027.417000,-14356.009000,-91304.744000,"Physic")
o.Scale=2.987797
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Peanapiedra",-140465.654000,-14372.596000,-105981.087000,"Physic")
o.Scale=3.171607
o.Orientation=0.006164,0.006171,-0.707080,0.707080
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Peanapiedra",-145008.502000,-14343.112000,-106019.553000,"Physic")
o.Scale=3.171607
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



"""
o=Bladex.CreateEntity("pollo1","Paletilla",-83369.301000,-6381.107000,40325.287000,"Physic")
o.Scale=1.000000
o.Orientation=0.625838,0.724239,0.216028,0.192708
pocimac.CreateFood("pollo1")


o=Bladex.CreateEntity("pollo2","Paletilla",-83427.303000,-6381.798000,38414.806000,"Physic")
o.Scale=1.000000
o.Orientation=0.144793,0.560567,0.648426,-0.494311
pocimac.CreateFood("pollo2")
"""

rej5=Bladex.CreateEntity("Rej5","Reja",-116262.791000,14371.087000,59206.072000,"Physic")
rej5.Scale=1.890462
rej5.Orientation=0.674380,0.247634,-0.212631,-0.662327
Sparks.SetMetalSparkling("Rej5")


rej6=Bladex.CreateEntity("Rej6","Reja",-116405.389000,11813.451000,57852.576000,"Physic")
rej6.Scale=1.474123
rej6.Orientation=0.000000,0.697474,0.003147,-0.716604
Sparks.SetMetalSparkling("Rej6")


esc2=Bladex.CreateEntity("RagnEsc2","Escudo5",-83770.891768,-8210.159890,60871.266182,"Weapon")
esc2.Scale=1.000000
esc2.Orientation=0.944651,0.271127,-0.066687,-0.172273
ItemTypes.ItemDefaultFuncs(esc2)


o=Bladex.CreateEntity("NoName0","LapidaCaballero",-123249.255791,-1172.925767,8773.853082,"Physic")
o.Scale=0.795442
o.Orientation=0.707107,0.707107,0.000000,0.000000



###########sala de ragnar#######

o=Bladex.CreateEntity("NoName2","Lamparatecho",-135336.522732,-38438.656308,-100131.047269,"Physic")
o.Scale=3.171607
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (50.000000,0.2750,(215,157,38)) ]        # Changed
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Cuerda",-135363.553918,-50614.819674,-100125.254324,"Physic")
o.Scale=3.109114
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Cuerda",-135363.553918,-45994.819674,-100125.254324,"Physic")
o.Scale=3.109114
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName5","Cuerda",-135363.553918,-42904.819674,-100125.254324,"Physic")
o.Scale=3.109114
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Lamparatecho",-104561.363000,-11606.778000,-44727.915000,"Physic")
o.Scale=3.869964
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (50.000000,0.031250,(255,163,60)) ]


o=Bladex.CreateEntity("NoName0","Piedra_01",-112239.012146,8608.827782,58051.704812,"Physic")
o.Scale=1.000000
o.Orientation=0.972061,-0.092587,-0.185017,0.110880
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName2","Piedra_03",-111815.157091,8577.901603,57630.278751,"Physic")
o.Scale=1.000000
o.Orientation=0.652072,0.753405,-0.038049,-0.075724
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName3","Piedra_04",-114431.363696,11544.710876,57096.747510,"Physic")
o.Scale=0.665003
o.Orientation=0.663146,0.660125,0.106380,-0.336385
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName4","Piedra_05",-112665.621989,8639.338104,57101.508079,"Physic")
o.Scale=0.523734
o.Orientation=0.693788,0.719920,-0.016775,-0.009586
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName6","Piedra_07",-113018.671624,8601.179849,58623.427285,"Physic")
o.Scale=0.285435
o.Orientation=0.640897,0.763741,-0.016577,0.075339
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



### Tabla sobre la que se apoya el caballero dormido

o=Bladex.CreateEntity("TablaSlpKgt","Tabla_rota",-76260.0, -6080.0, 53750.0,"Physic")
o.Scale=1.8
o.Orientation=0.540825068951, 0.540825068951, 0.455530703068, 0.455530703068
o.Solid=0


o=Bladex.CreateEntity("NoName7","Tabla_rota",-111696.096607,8136.066033,55815.372179,"Physic")
o.Scale=1.000000
o.Orientation=0.685267,0.169235,-0.158193,0.690466
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Tabla_rota",-113355.731109,8665.081773,56437.393471,"Physic")
o.Scale=1.000000
o.Orientation=0.666038,0.663360,0.238270,-0.244077
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName10","Tabla_xl",-109495.260916,8197.130720,57625.283704,"Physic")
o.Scale=1.947745
o.Orientation=0.421872,0.563641,0.578259,-0.412248
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName11","Piedra_07",-114530.531668,11582.132202,57704.720061,"Physic")
o.Scale=0.344836
o.Orientation=0.603408,0.781960,-0.054330,0.146580
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName13","Piedra_05",-114036.733617,11644.126390,58665.198867,"Physic")
o.Scale=0.503298
o.Orientation=0.660738,0.748308,-0.051852,-0.027789
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName14","Tabla_xl",-114996.328251,10927.342625,56082.203126,"Physic")
o.Scale=1.196147
o.Orientation=0.616184,0.618055,-0.342047,-0.348323
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName15","Tabla_rota",-116979.667824,11652.614184,56308.685250,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName16","Tabla_rota",-117421.303939,11573.467945,55854.354348,"Physic")
o.Scale=1.644632
o.Orientation=0.311128,0.352925,0.634447,-0.613287
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName17","Piedra_08",-75300.724981,8879.037402,70374.886332,"Physic")
o.Scale=0.341422
o.Orientation=0.519617,0.341887,0.124062,0.773124
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName18","Piedra_07",-74972.405940,8862.316946,71546.458018,"Physic")
o.Scale=0.392456
o.Orientation=0.622688,0.780190,0.034660,0.048594
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName19","Piedra_07",-74525.408827,8906.788940,70907.336410,"Physic")
o.Scale=0.285435
o.Orientation=0.566140,0.702910,0.267252,-0.337608
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName20","Piedra_03",-77626.072938,8937.738441,71874.796507,"Physic")
o.Scale=0.455629
o.Orientation=0.644769,0.760889,-0.059192,-0.042633
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName21","Tabla_rota",-76586.597180,8928.603424,72385.881297,"Physic")
o.Scale=1.834864
o.Orientation=0.653282,0.653282,0.270598,-0.270598
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName22","Tabla_xl",-72403.360987,7498.606720,72622.663751,"Physic")
o.Scale=1.402577
o.Orientation=0.705537,-0.152435,-0.054856,-0.689907
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



o=Bladex.CreateEntity("NoName0","Tabla_xl",-101143.648094,8951.588158,82991.745534,"Physic")
o.Scale=1.000000
o.Orientation=0.648459,0.648459,0.281958,-0.281958


o=Bladex.CreateEntity("NoName1","Tabla_rota",-101027.764544,8912.591167,83783.433208,"Physic")
o.Scale=1.000000
o.Orientation=0.701404,0.674083,-0.140303,0.184283


o=Bladex.CreateEntity("NoName2","Tabla_rota",-102509.826291,8940.555050,84251.756769,"Physic")
o.Scale=1.580459
o.Orientation=0.134922,0.134922,0.694115,-0.694115


o=Bladex.CreateEntity("NoName3","Tabla_rota",-104431.425720,8941.660291,79542.015730,"Physic")
o.Scale=1.334504
o.Orientation=0.599661,0.599661,0.374710,-0.374710


o=Bladex.CreateEntity("NoName4","Piedra_01",-103031.281918,8875.679232,80612.141225,"Physic")
o.Scale=0.665003
o.Orientation=0.872310,0.485393,-0.058007,-0.010221


o=Bladex.CreateEntity("NoName5","Piedra_01",-104792.215443,8870.311589,78140.453993,"Physic")
o.Scale=0.692005
o.Orientation=0.103741,0.845490,-0.451957,-0.264800


o=Bladex.CreateEntity("NoName6","Piedra_01",-103845.645469,8990.347620,81944.132764,"Physic")
o.Scale=0.534261
o.Orientation=0.950505,-0.215676,-0.024170,0.222352


o=Bladex.CreateEntity("NoName7","Piedra_01",-104375.710933,9020.134848,84734.213672,"Physic")
o.Scale=1.000000
o.Orientation=0.995396,-0.095846,0.000000,0.000000


o=Bladex.CreateEntity("NoName8","Piedra_01",-97274.875513,8967.727382,78345.206356,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName9","Piedra_03",-97400.444429,8924.543392,77761.773551,"Physic")
o.Scale=0.508331
o.Orientation=0.684490,0.726100,-0.010450,-0.064364


o=Bladex.CreateEntity("NoName10","Piedra_03",-98707.901045,8920.022353,81164.625275,"Physic")
o.Scale=0.464787
o.Orientation=0.764129,0.642191,-0.037204,-0.048094


o=Bladex.CreateEntity("NoName11","Tabla_rota",-97567.050554,8931.321770,79950.328801,"Physic")
o.Scale=1.694466
o.Orientation=0.638224,0.638224,0.304417,-0.304417


o=Bladex.CreateEntity("NoName12","Skull",-99630.320871,8899.287790,79229.579642,"Weapon")
o.Scale=1.000000
o.Orientation=0.865285,0.499503,0.029962,-0.029682


o=Bladex.CreateEntity("NoName13","Skull",-103307.026794,8908.705111,79729.702391,"Weapon")
o.Scale=1.000000
o.Orientation=0.801442,0.450656,-0.334664,0.206399


o=Bladex.CreateEntity("NoName14","Femur",-98680.540779,8924.697159,78224.445338,"Weapon")
o.Scale=1.308209
o.Orientation=0.995541,-0.017494,0.089234,-0.025101


o=Bladex.CreateEntity("NoName15","Femur",-103843.112989,8937.171407,80650.078457,"Weapon")
o.Scale=1.149474
o.Orientation=0.889867,0.018694,-0.449843,-0.073681


o=Bladex.CreateEntity("NoName16","Femur",-98287.484910,8976.111200,78651.669344,"Weapon")
o.Scale=1.000000
o.Orientation=0.007943,-0.588254,-0.023823,0.808286


o=Bladex.CreateEntity("NoName17","Femur",-104757.847662,8926.871707,81231.718601,"Weapon")
o.Scale=1.321291
o.Orientation=0.623785,0.007012,-0.781298,-0.020406


o=Bladex.CreateEntity("NoName18","Femur",-97353.006712,8943.769613,81220.275145,"Weapon")
o.Scale=1.000000
o.Orientation=0.945112,-0.003704,0.325785,0.024788


o=Bladex.CreateEntity("NoName19","Piedra_03",-97155.738776,9012.724048,83797.376193,"Physic")
o.Scale=0.764404
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName20","Piedra_03",-97311.374630,8905.009206,82280.775010,"Physic")
o.Scale=0.692005
o.Orientation=0.615380,0.784394,-0.057261,-0.052485


o=Bladex.CreateEntity("NoName21","Piedra_03",-92295.356223,8910.029154,81819.235595,"Physic")
o.Scale=0.614119
o.Orientation=0.601249,0.794954,-0.076367,-0.026757


o=Bladex.CreateEntity("NoName22","Piedra_03",-92704.320061,8909.415688,82883.029097,"Physic")
o.Scale=0.698925
o.Orientation=0.589229,0.591609,0.319733,-0.447861


o=Bladex.CreateEntity("NoName23","Tabla_rota",-91545.197127,8955.327346,82297.040565,"Physic")
o.Scale=1.000000
o.Orientation=0.304417,0.304417,-0.638224,0.638224


o=Bladex.CreateEntity("NoName24","Tabla_rota",-91404.192270,8896.383284,83097.029962,"Physic")
o.Scale=1.430769
o.Orientation=0.273628,0.235622,0.653429,-0.665312


o=Bladex.CreateEntity("NoName25","Piedra_01",-90237.240614,8947.834884,81027.780405,"Physic")
o.Scale=0.420766
o.Orientation=0.856239,-0.128125,-0.486959,0.115367


o=Bladex.CreateEntity("NoName26","Piedra_01",-90090.977398,8940.625248,81749.808217,"Physic")
o.Scale=0.550450
o.Orientation=0.717398,0.036678,0.683477,0.129825


o=Bladex.CreateEntity("NoName27","Piedra_01",-86694.041555,8939.990444,78177.748759,"Physic")
o.Scale=0.608039
o.Orientation=0.679078,-0.132597,-0.720710,0.043001


o=Bladex.CreateEntity("NoName28","Piedra_01",-87011.540099,8946.177967,78824.252484,"Physic")
o.Scale=0.596058
o.Orientation=0.932333,-0.181096,-0.285822,0.127538


o=Bladex.CreateEntity("NoName29","Tabla_rota",-86071.411837,8954.033764,79062.834195,"Physic")
o.Scale=1.000000
o.Orientation=0.650895,0.650895,-0.276289,0.276289


o=Bladex.CreateEntity("NoName30","Tabla_rota",-88395.215125,8952.394857,79566.425203,"Physic")
o.Scale=1.000000
o.Orientation=0.666548,0.666548,-0.236037,0.236037


o=Bladex.CreateEntity("NoName31","Skull",-89173.570664,8900.907082,81914.653973,"Weapon")
o.Scale=1.000000
o.Orientation=0.697255,0.427017,0.524216,-0.238093


o=Bladex.CreateEntity("NoName32","Skull",-92359.950678,8902.906066,83493.190992,"Weapon")
o.Scale=1.000000
o.Orientation=0.761819,0.439490,-0.456614,0.134103


o=Bladex.CreateEntity("NoName33","Femur",-89122.785475,8941.063109,80681.095685,"Weapon")
o.Scale=1.000000
o.Orientation=0.996731,-0.013225,-0.077656,0.017964


o=Bladex.CreateEntity("NoName34","Femur",-88826.276873,8943.541438,80976.793110,"Weapon")
o.Scale=1.000000
o.Orientation=0.830434,0.034106,-0.547697,-0.096145


o=Bladex.CreateEntity("NoName36","Restos",-89139.754983,8870.990618,81357.923761,"Physic")
o.Scale=1.000000
o.Orientation=0.671270,0.739617,0.047606,-0.009785

o=Bladex.CreateEntity("NoName0","Piedra_03",-70005.866158,-1854.633508,84205.990085,"Physic")
o.Scale=0.508331
o.Orientation=0.661848,0.746632,0.031284,0.059334


o=Bladex.CreateEntity("NoName1","Piedra_03",-70756.588658,-1857.371370,85057.500489,"Physic")
o.Scale=0.513414
o.Orientation=0.068326,0.235249,0.829252,0.502325


o=Bladex.CreateEntity("NoName2","Piedra_03",-70167.273251,-1836.878288,85237.901008,"Physic")
o.Scale=0.678370
o.Orientation=0.637661,0.764231,-0.024231,-0.093552


o=Bladex.CreateEntity("NoName3","Piedra_03",-69448.758423,-1827.235753,85412.255192,"Physic")
o.Scale=0.539604
o.Orientation=0.573932,0.682602,0.223037,-0.393588


o=Bladex.CreateEntity("NoName4","Tabla_rota",-69327.983480,-1793.614669,85834.293970,"Physic")
o.Scale=1.000000
o.Orientation=0.186754,0.182547,0.686926,-0.678183


o=Bladex.CreateEntity("NoName5","Tabla_rota",-65411.733776,-1580.398486,85974.646711,"Physic")
o.Scale=1.000000
o.Orientation=0.093535,0.685350,0.698800,-0.182276


o=Bladex.CreateEntity("NoName6","Piedra_03",-65008.790700,-1084.835216,85356.426223,"Physic")
o.Scale=0.555954
o.Orientation=0.632563,0.761312,-0.010240,-0.142001


o=Bladex.CreateEntity("NoName7","Piedra_03",-64555.679403,-1097.287407,84487.386162,"Physic")
o.Scale=0.400344
o.Orientation=0.632199,0.766493,0.018084,0.111739


o=Bladex.CreateEntity("NoName8","Piedra_03",-65837.163257,-1092.448051,83976.740002,"Physic")
o.Scale=0.720103
o.Orientation=0.487386,0.493145,0.420222,-0.585385


o=Bladex.CreateEntity("NoName9","Piedra_03",-65164.220323,659.127973,79426.600338,"Physic")
o.Scale=0.639055
o.Orientation=0.644857,0.756694,-0.073877,-0.078198


o=Bladex.CreateEntity("NoName10","Tabla_rota",-65463.454053,702.740909,77229.333788,"Physic")
o.Scale=1.000000
o.Orientation=0.270598,0.270598,0.653282,-0.653282


o=Bladex.CreateEntity("NoName11","Reja",-101759.942645,2262.559463,69240.277409,"Physic")
o.Scale=2.047099
o.Orientation=0.999962,0.008727,0.000000,0.000000



"""
alal1=Bladex.CreateEntity("Alal1","Alabarda",-89557.433400,1849.352622,-27349.159784,"Weapon")
alal1.Scale=1.000000
alal1.Orientation=0.706864,0.706864,-0.018510,-0.018510

### PLAGUE: Might restore
alal3=Bladex.CreateEntity("Alal3","Alabarda",-89495.897675,1859.848045,-28911.834395,"Weapon")
alal3.Scale=1.000000
alal3.Orientation=0.706676,0.706676,-0.024678,-0.024678
"""


o=Bladex.CreateEntity("NoName0","Piedra_03",-135003.746916,-8335.565149,-103429.381882,"Physic")
o.Scale=0.348285
o.Orientation=0.583939,0.800496,0.126971,-0.045835


o=Bladex.CreateEntity("NoName1","Piedra_03",-135896.837675,-8328.152212,-103890.156922,"Physic")
o.Scale=0.545000
o.Orientation=0.532876,0.520801,0.399022,-0.534407


o=Bladex.CreateEntity("NoName2","Piedra_03",-136418.647310,-8319.358546,-102775.779058,"Physic")
o.Scale=0.348285
o.Orientation=0.739986,0.671661,-0.009023,0.034797


o=Bladex.CreateEntity("NoName3","Piedra_03",-131250.359575,-8337.016172,-102316.468808,"Physic")
o.Scale=0.555954
o.Orientation=0.593567,0.801583,-0.033416,-0.063450


o=Bladex.CreateEntity("NoName4","Tabla_rota",-129922.052835,-8864.748726,-103650.429387,"Physic")
o.Scale=1.160969
o.Orientation=0.343611,0.329208,0.615771,0.627997


o=Bladex.CreateEntity("NoName5","Tabla_rota",-130120.184721,-8294.255029,-101870.436032,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.003339,-0.709633,-0.704563


o=Bladex.CreateEntity("NoName6","Tabla_rota",-129697.962525,-9376.394499,-102579.808543,"Physic")
o.Scale=1.853212
o.Orientation=0.494098,0.448488,0.501044,0.551073


o=Bladex.CreateEntity("NoName7","Tabla_rota",-132287.989576,-8292.907096,-104096.935872,"Physic")
o.Scale=1.000000
o.Orientation=0.484673,0.482280,-0.518649,0.513324


o=Bladex.CreateEntity("NoName8","Tabla_rota",-134058.767658,-9155.417622,-104208.074678,"Physic")
o.Scale=1.661078
o.Orientation=0.686007,0.179682,-0.177880,0.682251


o=Bladex.CreateEntity("NoName9","Tabla_rota",-135773.987867,-9221.032856,-104600.712736,"Physic")
o.Scale=1.596263
o.Orientation=0.703681,0.010798,-0.044272,0.709053


o=Bladex.CreateEntity("NoName10","Tabla_rota",-135794.620379,-9501.678153,-99123.769097,"Physic")
o.Scale=1.474123
o.Orientation=0.321163,0.525331,0.671256,-0.412669


o=Bladex.CreateEntity("NoName11","Piedra_03",-134674.354823,-11562.373662,-88601.454957,"Physic")
o.Scale=0.474129
o.Orientation=0.654461,0.751341,-0.029599,-0.079313


o=Bladex.CreateEntity("NoName12","Piedra_03",-134584.194012,-11586.871255,-87517.993370,"Physic")
o.Scale=0.645445
o.Orientation=0.628394,0.772058,-0.039296,-0.086622


o=Bladex.CreateEntity("NoName13","Piedra_03",-136622.133169,-11573.504987,-87977.206628,"Physic")
o.Scale=0.539604
o.Orientation=0.656121,0.743048,0.018823,-0.130499


o=Bladex.CreateEntity("NoName14","Piedra_03",-136419.782372,-11587.273595,-87311.910215,"Physic")
o.Scale=0.671653
o.Orientation=0.689985,0.722186,-0.010965,-0.047402


o=Bladex.CreateEntity("NoName15","Piedra_03",-140590.720316,-11580.405790,-87609.490345,"Physic")
o.Scale=0.584313
o.Orientation=0.683489,0.719003,-0.114540,0.052520


o=Bladex.CreateEntity("NoName16","Piedra_03",-141548.712375,-11579.975216,-89275.837424,"Physic")
o.Scale=0.626463
o.Orientation=0.641147,0.761468,-0.037644,-0.087634


o=Bladex.CreateEntity("NoName17","Tabla_rota",-136770.861447,-11642.666498,-87796.305029,"Physic")
o.Scale=1.000000
o.Orientation=0.608254,0.639265,0.255043,-0.395374


o=Bladex.CreateEntity("NoName18","Tabla_rota",-135080.642532,-12461.850227,-86540.959304,"Physic")
o.Scale=1.612226
o.Orientation=0.072353,0.701673,0.701937,-0.098507


o=Bladex.CreateEntity("NoName19","Tabla_rota",-136696.739675,-12698.113175,-86528.950201,"Physic")
o.Scale=1.763268
o.Orientation=0.080047,0.702561,0.702561,-0.080047


o=Bladex.CreateEntity("NoName20","Tabla_xl",-135442.891198,-11544.154536,-89886.812188,"Physic")
o.Scale=1.000000
o.Orientation=0.624338,0.624338,0.331967,-0.331967


o=Bladex.CreateEntity("NoName21","Tabla_xl",-139815.871670,-11719.217340,-88360.551271,"Physic")
o.Scale=1.000000
o.Orientation=0.703383,0.700766,-0.075127,-0.092388


o=Bladex.CreateEntity("NoName22","Tabla_xl",-127032.401452,-5547.894240,-91339.760856,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName23","Piedra_03",-125633.267700,-5582.266866,-89930.487739,"Physic")
o.Scale=0.639055
o.Orientation=0.641772,0.756563,-0.009558,-0.125101


o=Bladex.CreateEntity("NoName24","Piedra_03",-124412.685637,-5602.389445,-88813.484689,"Physic")
o.Scale=0.534261
o.Orientation=0.745436,0.650097,-0.001181,-0.147304


o=Bladex.CreateEntity("NoName25","Piedra_03",-131140.588662,-8374.856662,-103712.496460,"Physic")
o.Scale=0.513414
o.Orientation=0.724268,0.666586,0.140108,0.107091


o=Bladex.CreateEntity("NoName26","Piedra_03",-131942.774888,-5343.016488,-89731.082020,"Physic")
o.Scale=0.584313
o.Orientation=0.115013,0.037630,0.870918,0.476296

o=Bladex.CreateEntity("NoName0","Tabla_rota",-91648.532539,6316.054163,-87917.368136,"Physic")
o.Scale=1.947745
o.Orientation=0.483524,0.485333,0.518900,0.511272


o=Bladex.CreateEntity("NoName1","Tabla_rota",-92149.089767,6473.379320,-90373.620874,"Physic")
o.Scale=1.909366
o.Orientation=0.347864,0.353583,0.615968,0.612007


o=Bladex.CreateEntity("NoName2","Tabla_rota",-92810.702923,7441.595310,-88895.855220,"Physic")
o.Scale=1.503752
o.Orientation=0.662327,0.662327,0.247634,-0.247634


o=Bladex.CreateEntity("NoName3","Piedra_03",-95511.005833,7427.440381,-87142.697948,"Physic")
o.Scale=0.451118
o.Orientation=0.719652,0.684057,0.023863,-0.116607


o=Bladex.CreateEntity("NoName4","Piedra_03",-93135.772350,7415.114808,-86730.583530,"Physic")
o.Scale=0.608039
o.Orientation=0.640917,0.759727,0.010944,-0.109177


o=Bladex.CreateEntity("NoName5","Piedra_03",-94839.713676,7426.884868,-86965.541615,"Physic")
o.Scale=0.518548
o.Orientation=0.630533,0.767917,-0.011000,-0.112300


o=Bladex.CreateEntity("NoName6","Piedra_03",-99184.506653,7670.232047,-89667.371155,"Physic")
o.Scale=0.626463
o.Orientation=0.660658,0.746893,-0.029471,-0.069385


o=Bladex.CreateEntity("NoName7","Piedra_03",-99663.982932,7661.843910,-88148.629484,"Physic")
o.Scale=0.614119
o.Orientation=0.661380,0.734411,-0.144876,0.047204


o=Bladex.CreateEntity("NoName8","Tabla_xl",-101340.000382,7767.802341,-100439.934349,"Physic")
o.Scale=2.759181
o.Orientation=0.701353,0.084820,0.081265,-0.703068


o=Bladex.CreateEntity("NoName9","Piedra_03",-101396.739256,9683.152401,-97528.120660,"Physic")
o.Scale=0.503298
o.Orientation=0.536167,0.713415,-0.341300,0.295091


o=Bladex.CreateEntity("NoName10","Piedra_03",-100498.530967,9648.238911,-98109.377344,"Physic")
o.Scale=0.727304
o.Orientation=0.606463,0.789679,-0.032375,-0.086955


o=Bladex.CreateEntity("NoName11","Piedra_03",-101182.705513,7906.383813,-91645.027220,"Physic")
o.Scale=0.741923
o.Orientation=0.645704,0.758759,-0.074316,-0.042763


o=Bladex.CreateEntity("NoName12","Piedra_03",-100458.216195,7904.830000,-91823.786336,"Physic")
o.Scale=0.678370
o.Orientation=0.603251,0.793573,-0.043975,-0.066307


o=Bladex.CreateEntity("NoName13","Piedra_03",-101594.694763,7649.694133,-90563.363165,"Physic")
o.Scale=0.811430
o.Orientation=0.659643,0.748174,-0.040245,-0.059054


o=Bladex.CreateEntity("NoName14","Tabla_rota",-102631.056018,7702.253211,-90564.619640,"Physic")
o.Scale=1.000000
o.Orientation=0.564721,0.564721,0.425547,-0.425547


o=Bladex.CreateEntity("NoName15","Tabla_rota",-112042.946267,482.772504,-85838.624816,"Physic")
o.Scale=2.599273
o.Orientation=0.093966,0.691874,0.703517,-0.132455


o=Bladex.CreateEntity("NoName16","Piedra_03",-110894.494519,1916.097339,-88021.648699,"Physic")
o.Scale=0.561514
o.Orientation=0.710688,0.703131,-0.022523,0.004817



o=Bladex.CreateEntity("NoName0","Tabla_rota",-132708.015420,-12719.053394,-90108.470455,"Physic")
o.Scale=2.026831
o.Orientation=0.538353,0.547331,0.456981,0.449192


o=Bladex.CreateEntity("NoName1","Tabla_rota",-131998.493129,-11559.661777,-87971.006019,"Physic")
o.Scale=1.612226
o.Orientation=0.707237,0.706976,0.000451,0.000213


o=Bladex.CreateEntity("NoName2","Tabla_rota",-130647.302829,-13531.956820,-86777.112309,"Physic")
o.Scale=3.400392
o.Orientation=0.068838,0.702197,0.704618,-0.075453


o=Bladex.CreateEntity("NoName3","Piedra_03",-130357.760813,-11578.532972,-88658.969664,"Physic")
o.Scale=0.545000
o.Orientation=0.686992,0.722600,-0.022972,-0.073237


o=Bladex.CreateEntity("NoName4","Piedra_03",-131288.740172,-11604.195418,-90265.646703,"Physic")
o.Scale=0.408391
o.Orientation=0.680799,0.700337,0.187052,0.105128


o=Bladex.CreateEntity("NoName5","Piedra_03",-131477.010351,-11593.769902,-91213.376552,"Physic")
o.Scale=0.442229
o.Orientation=0.636446,0.758303,-0.051347,0.131438


o=Bladex.CreateEntity("NoName6","Piedra_03",-130430.610246,-11570.808234,-90684.476041,"Physic")
o.Scale=0.539604
o.Orientation=0.673088,0.735775,-0.015827,-0.073058


o=Bladex.CreateEntity("NoName7","Piedra_03",-132413.170197,-11331.407993,-93449.525472,"Physic")
o.Scale=0.523734
o.Orientation=0.691240,0.717145,-0.071859,0.052217


o=Bladex.CreateEntity("NoName8","Piedra_03",-131968.271268,-11336.487766,-94614.677170,"Physic")
o.Scale=0.602019
o.Orientation=0.711081,0.702456,-0.000607,-0.030305


o=Bladex.CreateEntity("NoName9","Piedra_03",-131552.930712,-11826.232355,-96159.028655,"Physic")
o.Scale=0.584313
o.Orientation=0.639409,0.763842,-0.036773,-0.079686


o=Bladex.CreateEntity("NoName10","Piedra_03",-130195.859456,-11341.510960,-94161.232635,"Physic")
o.Scale=0.602019
o.Orientation=0.600776,0.792589,-0.034527,-0.098380


o=Bladex.CreateEntity("NoName11","Piedra_03",-130950.746093,-11330.616447,-92911.166842,"Physic")
o.Scale=0.508331
o.Orientation=0.631419,0.764251,-0.028609,-0.128111


o=Bladex.CreateEntity("NoName12","Piedra_03",-131139.182896,-13825.146963,-102324.939705,"Physic")
o.Scale=0.464787
o.Orientation=0.598466,0.792887,-0.015004,-0.113766


o=Bladex.CreateEntity("NoName13","Piedra_03",-136208.192398,-14830.403025,-102129.440595,"Physic")
o.Scale=0.518548
o.Orientation=0.614334,0.777374,-0.020663,-0.133627


o=Bladex.CreateEntity("NoName14","Piedra_03",-136585.312891,-14832.766382,-101077.768472,"Physic")
o.Scale=0.602019
o.Orientation=0.680211,0.730915,-0.012166,-0.054123


o=Bladex.CreateEntity("NoName15","Piedra_03",-135063.227321,-14849.458608,-102157.773210,"Physic")
o.Scale=0.408391
o.Orientation=0.312000,0.543243,0.468086,-0.623249


o=Bladex.CreateEntity("NoName16","Piedra_03",-134034.713455,-14837.161695,-102725.800950,"Physic")
o.Scale=0.561514
o.Orientation=0.620905,0.760854,0.074256,0.173390


o=Bladex.CreateEntity("NoName17","Piedra_03",-134946.946060,-17326.546150,-94610.175529,"Physic")
o.Scale=0.555954
o.Orientation=0.676335,0.733059,-0.019711,-0.069332


o=Bladex.CreateEntity("NoName18","Piedra_03",-134882.553468,-17322.345061,-95076.725474,"Physic")
o.Scale=0.503298
o.Orientation=0.671975,0.735356,-0.050436,-0.071811


o=Bladex.CreateEntity("NoName19","Piedra_03",-136746.281969,-17318.516866,-91977.128128,"Physic")
o.Scale=0.469435
o.Orientation=0.648151,0.747788,-0.001129,-0.143918


o=Bladex.CreateEntity("NoName20","Tabla_rota",-136741.125540,-18015.856583,-93010.422892,"Physic")
o.Scale=1.430769
o.Orientation=0.606269,0.630909,0.351389,0.333043


o=Bladex.CreateEntity("NoName21","Tabla_rota",-137090.642522,-18408.695419,-92375.639689,"Physic")
o.Scale=1.853212
o.Orientation=0.481961,0.525084,0.331143,0.618341


o=Bladex.CreateEntity("NoName22","Piedra_03",-135766.256753,-17330.415104,-92509.121714,"Physic")
o.Scale=0.503298
o.Orientation=0.599101,0.794384,-0.030862,-0.095291


o=Bladex.CreateEntity("NoName23","Piedra_03",-131421.036077,-17324.542518,-92089.429162,"Physic")
o.Scale=0.561514
o.Orientation=0.642159,0.759754,-0.028229,-0.098028


o=Bladex.CreateEntity("NoName24","Piedra_03",-133579.370501,-17323.867833,-92085.321350,"Physic")
o.Scale=0.493381
o.Orientation=0.620676,0.776409,-0.031869,-0.104570


o=Bladex.CreateEntity("NoName25","Piedra_03",-130498.099361,-17324.294408,-93003.186272,"Physic")
o.Scale=0.518548
o.Orientation=0.639076,0.736677,-0.189297,0.114256


o=Bladex.CreateEntity("NoName26","Piedra_03",-130029.662272,-17328.665738,-91503.087415,"Physic")
o.Scale=0.602019
o.Orientation=0.640393,0.762307,-0.093302,-0.008948


o=Bladex.CreateEntity("NoName27","Tabla_rota",-130115.288220,-18321.069652,-91988.358397,"Physic")
o.Scale=1.947745
o.Orientation=0.368942,0.359437,0.603178,0.608985


o=Bladex.CreateEntity("NoName28","Piedra_03",-131440.174596,-17360.983087,-92739.029209,"Physic")
o.Scale=0.567129
o.Orientation=0.761459,-0.629590,-0.127791,0.086404


o=Bladex.CreateEntity("NoName29","Piedra_03",-131901.088956,-17323.154012,-91887.523733,"Physic")
o.Scale=0.539604
o.Orientation=0.638162,0.759260,-0.012127,-0.126989


o=Bladex.CreateEntity("NoName30","Piedra_03",-130822.756498,-20072.102683,-101637.311147,"Physic")
o.Scale=0.518548
o.Orientation=0.332376,-0.101909,0.828163,0.439644


o=Bladex.CreateEntity("NoName31","Piedra_03",-130075.510153,-20087.514910,-102705.437558,"Physic")
o.Scale=0.567129
o.Orientation=0.627959,0.768706,-0.084514,-0.087276


o=Bladex.CreateEntity("NoName32","Piedra_03",-131357.822894,-20077.181371,-102588.761762,"Physic")
o.Scale=0.513414
o.Orientation=0.656939,0.751113,-0.064227,0.011645


o=Bladex.CreateEntity("NoName33","Piedra_03",-130054.146602,-20073.699752,-100927.232030,"Physic")
o.Scale=0.478871
o.Orientation=0.627124,0.775377,-0.069542,-0.025885


o=Bladex.CreateEntity("NoName34","Tabla_rota",-131438.709133,-20167.279608,-102049.087174,"Physic")
o.Scale=1.871744
o.Orientation=0.470852,0.422559,-0.527748,0.566767


o=Bladex.CreateEntity("NoName35","Tabla_rota",-129951.642055,-21554.385675,-102233.236647,"Physic")
o.Scale=2.599273
o.Orientation=0.439080,0.442506,0.551869,0.553930


o=Bladex.CreateEntity("NoName36","Tabla_rota",-135550.136799,-16360.515213,-97632.031724,"Physic")
o.Scale=1.000000
o.Orientation=0.686329,0.685864,0.171103,-0.171072


o=Bladex.CreateEntity("NoName37","Piedra_03",-130367.056850,-20081.752091,-101529.522940,"Physic")
o.Scale=0.578528
o.Orientation=0.632685,0.768252,-0.030237,-0.092652


o=Bladex.CreateEntity("NoName38","Piedra_03",-135290.424591,-21082.621936,-102355.339847,"Physic")
o.Scale=0.596058
o.Orientation=0.662166,0.744496,-0.085003,0.006030


o=Bladex.CreateEntity("NoName39","Piedra_03",-134897.076082,-22073.151292,-92139.457260,"Physic")
o.Scale=0.539604
o.Orientation=0.625743,0.772937,-0.102692,-0.021648


o=Bladex.CreateEntity("NoName40","Piedra_03",-134189.326963,-22073.786710,-93302.404276,"Physic")
o.Scale=0.555954
o.Orientation=0.691710,0.718582,0.002606,-0.071901


o=Bladex.CreateEntity("NoName41","Piedra_03",-134646.776085,-21114.804333,-101105.513494,"Physic")
o.Scale=0.408391
o.Orientation=0.463120,0.751013,-0.441244,-0.163717


o=Bladex.CreateEntity("NoName42","Piedra_03",-132707.305532,-20361.346147,-102806.128592,"Physic")
o.Scale=0.602019
o.Orientation=0.748927,0.623458,-0.210459,0.078202


o=Bladex.CreateEntity("NoName43","Piedra_03",-132095.915262,-17342.188973,-92200.678256,"Physic")
o.Scale=0.534261
o.Orientation=0.581227,0.792337,-0.181007,0.040171


o=Bladex.CreateEntity("NoName0","Tabla_rota",-87516.187235,-15436.012900,-9223.779555,"Physic")
o.Scale=1.745810
o.Orientation=0.589646,0.420603,0.390278,-0.568413


o=Bladex.CreateEntity("NoName1","Tabla_rota",-85855.084982,-15064.048193,-6641.203260,"Physic")
o.Scale=2.573538
o.Orientation=0.486740,0.609264,-0.512917,0.358884


o=Bladex.CreateEntity("NoName2","Reja",-72980.559041,17826.899067,71152.499753,"Physic")
o.Scale=2.216715
o.Orientation=0.486740,0.486740,0.512917,-0.512917



o=Bladex.CreateEntity("NoName4","Piedra_03",-80332.822535,18365.805688,65752.117244,"Physic")
o.Scale=0.464787
o.Orientation=0.542145,-0.081871,0.459159,0.698963


o=Bladex.CreateEntity("NoName5","Piedra_03",-79674.002546,18416.798145,66929.342958,"Physic")
o.Scale=0.550450
o.Orientation=0.681396,0.730819,0.006547,-0.039502


o=Bladex.CreateEntity("NoName6","Piedra_03",-78525.522411,18421.856653,67904.968177,"Physic")
o.Scale=0.478871
o.Orientation=0.679539,0.730377,-0.062521,0.029453


o=Bladex.CreateEntity("NoName7","Piedra_03",-78761.538495,18413.689891,64991.941106,"Physic")
o.Scale=0.523734
o.Orientation=0.703507,0.706011,0.070808,-0.040158


o=Bladex.CreateEntity("NoName8","Piedra_03",-77628.351192,18419.681579,73417.522028,"Physic")
o.Scale=0.561514
o.Orientation=0.649909,0.755668,-0.008757,-0.080673


o=Bladex.CreateEntity("NoName9","Piedra_03",-81674.191930,18414.510143,72976.545303,"Physic")
o.Scale=0.429223
o.Orientation=0.151817,0.047889,-0.680108,-0.715619


o=Bladex.CreateEntity("NoName10","Piedra_03",-86767.709559,18541.773080,64736.136485,"Physic")
o.Scale=0.578528
o.Orientation=0.656985,0.742665,-0.129551,-0.006004




o=Bladex.CreateEntity("NoName0","Piedra_01",-109658.695718,9086.853629,83938.017301,"Physic")
o.Scale=0.665003
o.Orientation=0.328398,0.126976,0.061589,0.933937


o=Bladex.CreateEntity("NoName1","Piedra_01",-109052.684810,9172.795382,84800.547054,"Physic")
o.Scale=0.550450
o.Orientation=0.751384,-0.050535,-0.646133,0.124013


o=Bladex.CreateEntity("NoName2","Piedra_01",-110983.424787,8923.809194,84727.779145,"Physic")
o.Scale=0.590156
o.Orientation=0.886401,0.059041,-0.381869,0.254918


o=Bladex.CreateEntity("NoName3","Piedra_03",-110471.153931,9112.807351,83760.260910,"Physic")
o.Scale=0.513414
o.Orientation=0.405560,-0.911473,-0.059970,-0.033775


o=Bladex.CreateEntity("NoName4","Restos",-110334.442734,9141.993658,81484.684198,"Physic")
o.Scale=1.000000
o.Orientation=0.530476,0.665574,0.331097,-0.407409



o=Bladex.CreateEntity("Ragngladmort","Gladius",-153151.508147, 14223.9556277, 46118.353,"Weapon")
o.Scale=1.000000
o.Orientation=0.913412,-0.015668,0.406676,-0.006894

Breakings.SetBreakableWS("Ragngladmort")




o=Bladex.CreateEntity("NoName0","Tabla_rota",-118542.473624,-13356.571653,36226.934449,"Physic")
o.Scale=3.171607
o.Orientation=0.477714,0.477714,-0.521334,-0.521334





o=Bladex.CreateEntity("aver","Rastrillo2",-98344.515000,-14640.859000,39318.652000,"Physic")
o.Scale=0.712973
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("aver")



o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-112116.309380,8738.492052,84644.552751,"Physic")
o.Scale=1.000000
o.Orientation=0.995162,-0.000550,0.098244,0.000794


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-108343.374590,9006.837463,84999.282865,"Physic")
o.Scale=0.678370
o.Orientation=0.671189,0.524403,0.381585,-0.359026





o=Bladex.CreateEntity("NoName0","Altar",-89539.373106,6546.824979,-95945.054470,"Physic")
o.Scale=0.578528
o.Orientation=0.508650,0.508650,0.491198,-0.491198
Sparks.SetStoneSparkling(o.Name)        # Add
o.Static = 1                            #


o=Bladex.CreateEntity("NoName1","ArmaduraCaballeroLigera",-89378.955057,5755.690067,-95919.665862,"Physic")
o.Scale=1.000000
o.Orientation=0.194905,0.194905,-0.679715,0.679715
o.Solid=0
####################
##################




o=Bladex.CreateEntity("PergaminoFin","Pergamino",-136724.224762,-31582.323281,-93610.602398,"Physic")
o.Scale=1.445076
o.Orientation=0.212848,0.016887,0.973372,-0.083414
import Stars                                # Add
Stars.Twinkle(o.Name, DoNotReport = 1)      #       -LeadHead




####################
##################SALA DEL PRIMER CABALLERO

o=Bladex.CreateEntity("NoName2","Taburete",-122858.947183,2162.254202,52265.527724,"Weapon")
o.Scale=1.000000
o.Orientation=0.703863,0.703093,0.073922,-0.069092


o=Bladex.CreateEntity("NoName6","Caliz",-122624.729135,1388.690567,52196.904129,"Weapon")
o.Scale=1.000000
o.Orientation=0.030254,0.874278,0.015312,-0.484240

##################sala antes de los pendulos y 2kngt



o=Bladex.CreateEntity("NoName1","Taburete",-84214.219876,1661.142132,-98460.245048,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName2","Taburete",-82331.968112,1654.789360,-97397.100382,"Weapon")
o.Scale=1.000000
o.Orientation=0.991584,0.122291,0.042467,0.001765


o=Bladex.CreateEntity("NoName3","Jarra",-83609.647505,865.882091,-97917.140919,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName5","Caliz",-83471.497658,888.067732,-98626.129827,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName6","Tabla_xlpieza2",-82048.485991,1952.008153,-95425.826534,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName7","Tabla_xl",-80384.382071,-516.215425,-99095.442170,"Physic")
o.Scale=2.376619
o.Orientation=0.504344,0.504344,0.495618,-0.495618


o=Bladex.CreateEntity("NoName8","Jarra",-80503.909357,-723.860416,-98274.029527,"Weapon")
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName9","Jarrita",-80553.133180,-1005.268317,-99258.313717,"Weapon")
o.Scale=1.000000
o.Orientation=0.482246,0.482246,0.517145,-0.517145


o=Bladex.CreateEntity("NoName11","Jarra",-80672.618293,-709.711166,-98812.527183,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName12","Tabla_xlpieza2",-81264.153235,1951.848525,-99379.214474,"Physic")
o.Scale=1.000000
o.Orientation=0.643440,0.643440,-0.293232,0.293232


o=Bladex.CreateEntity("NoName13","Taburete",-81090.312688,1603.913967,-99408.103020,"Weapon")
o.Scale=1.000000
o.Orientation=0.979443,0.161789,0.042056,0.112902


o=Bladex.CreateEntity("NoName14","Tabla_xl",-80359.204654,-526.411674,-95338.134016,"Physic")
o.Scale=2.759181
o.Orientation=0.504344,0.504344,0.495618,-0.495618


o=Bladex.CreateEntity("NoName15","Tronco",-80094.324457,-334.862395,-94364.627972,"Physic")
o.Scale=1.388690
o.Orientation=0.504344,0.504344,0.495618,-0.495618
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName16","Tronco",-80044.719968,-353.202187,-97314.450004,"Physic")
o.Scale=1.334504
o.Orientation=0.504344,0.504344,0.495618,-0.495618
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName17","Tronco",-80030.716297,-329.290097,-95723.504143,"Physic")
o.Scale=1.402577
o.Orientation=0.529592,0.529592,0.468543,-0.468543
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName18","Tronco",-80286.353572,-330.374242,-99218.187828,"Physic")
o.Scale=1.172579
o.Orientation=0.529592,0.529592,0.468543,-0.468543
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName19","Perola",-80604.676515,-822.887309,-94675.416875,"Physic")
o.Scale=1.000000
o.Orientation=0.707087,0.707017,-0.011691,0.004393


o=Bladex.CreateEntity("NoName20","Mortero",-80560.786044,-824.445396,-95507.102978,"Weapon")
o.Scale=1.000000
o.Orientation=0.119863,0.887694,-0.031756,-0.443423


o=Bladex.CreateEntity("NoName21","Tabla_xlpieza2",-80308.687939,1185.081397,-93796.991162,"Physic")
o.Scale=1.430769
o.Orientation=0.459229,0.459229,0.537688,0.537688


o=Bladex.CreateEntity("NoName22","Tabla_xlpieza2",-115166.016444,13936.992275,80552.922720,"Physic")
o.Scale=1.780901
o.Orientation=0.557587,0.561517,0.436961,0.427621


#o=Bladex.CreateEntity("NoName23","Tabla_xlpieza2",-110545.276145,13827.001024,81372.337657,"Physic")
#o.Scale=1.947745
#o.Orientation=0.450594,0.449246,0.548138,0.542852



o=Bladex.CreateEntity("NoName25","Piedra_01",-109263.281196,10977.584515,91543.571984,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName26","Piedra_01",-110419.437287,11071.460935,91411.031583,"Physic")
o.Scale=1.149474
o.Orientation=0.281958,0.281958,0.648459,0.648459



o=Bladex.CreateEntity("NoName28","Tabla_xlpieza2",-109856.758075,10942.924781,92300.613011,"Physic")
o.Scale=1.518790
o.Orientation=0.497845,0.496578,0.502724,-0.502821


o=Bladex.CreateEntity("NoName29","Tabla_xlpieza2",-110831.852350,10874.107615,92362.474966,"Physic")
o.Scale=1.745810
o.Orientation=0.123186,0.162916,0.686093,-0.698255


o=Bladex.CreateEntity("NoName30","Tabla_xlpieza2",-111527.705859,13718.129209,78977.897237,"Physic")
o.Scale=2.194768
o.Orientation=0.418362,0.410320,0.570287,0.575659


o=Bladex.CreateEntity("NoName31","Skull",-109005.489993,10903.837308,90718.184531,"Weapon")
o.Scale=1.000000
o.Orientation=0.877000,0.475508,0.049906,-0.047666


o=Bladex.CreateEntity("NoName32","Tabla_xPieza1",-81751.291976,1957.021833,73825.037901,"Physic")
o.Scale=1.000000
o.Orientation=0.218508,0.218508,-0.672499,0.672499



o=Bladex.CreateEntity("NoName34","Tabla_xlpieza2",-82317.624597,313.618262,65148.318325,"Physic")
o.Scale=2.786772
o.Orientation=0.498185,0.525306,0.502035,0.473103

#####nueva sala de la armadura

o=Bladex.CreateEntity("NoName0","Tabla_xl",-81118.843451,4994.425867,-99345.542318,"Physic")
o.Scale=2.261271
o.Orientation=0.500000,0.500000,0.500000,-0.500000


o=Bladex.CreateEntity("NoName1","Tabla_xl",-81236.514118,4214.485513,-99281.079530,"Physic")
o.Scale=2.151522
o.Orientation=0.500000,0.500000,0.500000,-0.500000


o=Bladex.CreateEntity("NoName2","Jarra",-81051.067886,4758.569042,-98467.766930,"Weapon")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName3","Jarra",-81394.708879,4818.792926,-99053.419632,"Weapon")
o.Scale=1.000000
o.Orientation=0.617180,0.334625,-0.324498,-0.633890


o=Bladex.CreateEntity("NoName4","Jarrita",-81257.722571,5581.353061,-98299.781428,"Weapon")
o.Scale=1.000000
o.Orientation=0.615434,0.615434,0.348196,-0.348196


o=Bladex.CreateEntity("NoName5","Jarra",-81328.236404,4786.090142,-99743.576230,"Weapon")
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName6","Jarra",-81242.462657,4766.927339,-100081.468735,"Weapon")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000

########libritos en la sala de ragnar

o=Bladex.CreateEntity("NoName9","Tabla_xl",-136956.209876,-32718.869048,-94479.446759)
o.Scale=2.151522
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName10","Tabla_xl",-136898.384518,-33484.178025,-94465.109342)
o.Scale=2.261271
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName11","Libro",-135531.708992,-33014.898679,-94395.669595)
o.Scale=1.000000
o.Orientation=0.498097,0.456422,0.543578,-0.498097


o=Bladex.CreateEntity("NoName12","Libro",-135719.018016,-33076.414963,-94483.859102)
o.Scale=1.388690
o.Orientation=0.459229,0.459229,0.537688,-0.537688


o=Bladex.CreateEntity("NoName13","Libro2",-135832.649275,-33115.994140,-94441.101497)
o.Scale=1.430769
o.Orientation=0.473006,0.496257,0.521773,-0.507688


o=Bladex.CreateEntity("NoName14","Libro2",-136144.603639,-32869.800236,-94489.894481)
o.Scale=1.244716
o.Orientation=0.674977,-0.000043,-0.737824,0.004596


o=Bladex.CreateEntity("NoName15","Libro2",-136202.543133,-32945.273298,-94320.716157)
o.Scale=1.000000
o.Orientation=0.823163,-0.002453,0.567794,-0.002544


o=Bladex.CreateEntity("NoName16","Libro3",-136214.240383,-32967.831770,-94358.950704)
o.Scale=1.000000
o.Orientation=0.008161,0.702824,0.000202,-0.711317


o=Bladex.CreateEntity("NoName17","Libro3",-136493.643885,-33105.524158,-94439.263065)
o.Scale=1.474123
o.Orientation=0.538754,0.476649,0.520268,-0.460295


o=Bladex.CreateEntity("NoName18","Libro3",-137415.258643,-32813.232159,-94264.922739)
o.Scale=1.000000
o.Orientation=0.008965,-0.979615,-0.019219,0.199762


o=Bladex.CreateEntity("NoName19","Libro2",-137424.085398,-32951.280660,-94325.123404)
o.Scale=1.196147
o.Orientation=0.979245,0.009163,-0.201231,0.022373


o=Bladex.CreateEntity("NoName20","Libro2",-137104.921204,-32953.156329,-94448.872828)
o.Scale=1.347849
o.Orientation=0.079792,0.706095,0.198551,-0.675012

o=Bladex.CreateEntity("NoName18","Libro3",-136175.259000,-33583.232000,-94264.923000)
o.Scale=1.000000
o.Orientation=0.008965,-0.979615,-0.019218,0.199762


o=Bladex.CreateEntity("NoName19","Libro2",-136184.085000,-33721.281000,-94325.123000)
o.Scale=1.196147
o.Orientation=0.979245,0.009163,-0.201231,0.022373


o=Bladex.CreateEntity("NoName20","Libro2",-135864.921000,-33723.156000,-94448.873000)
o.Scale=1.347849
o.Orientation=0.079792,0.706095,0.198551,-0.675012

o=Bladex.CreateEntity("NoName9","Pluma",-137377.806784,-31526.292038,-93486.137768)
o.Scale=1.000000
o.Orientation=0.325444,0.039091,-0.944732,-0.006298


o=Bladex.CreateEntity("NoName10","Tintero",-137224.971018,-31553.519922,-93742.065067)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName11","Libro2",-137363.307879,-30516.011122,-92178.601253)
o.Scale=1.000000
o.Orientation=0.000000,0.724138,-0.005936,-0.689630
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName12","Libro3",-137848.141084,-30571.550397,-91606.202527)
o.Scale=1.000000
o.Orientation=0.926982,-0.007179,0.374988,0.006153
darfuncs.SetHint(o,"","",0.0,0.0)   # Add


o=Bladex.CreateEntity("NoName13","Taburete",-136601.402941,-30838.558941,-93298.849272,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"","",0.0,0.0)   # Add

#######palanca del puente

o=Bladex.CreateEntity("NoName6","Caja_i_i",-98043.521969,-8930.583867,-53761.452416,"Physic")
o.Scale=1.000000
o.Orientation=0.664463,0.664463,0.241845,-0.241845
Sparks.SetMetalSparkling(o.Name)    # add


o=Bladex.CreateEntity("palan1","Queso",-97843.109135,-9288.119588,-53701.445611,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("palan1")


o=Bladex.CreateEntity("palan2","Hogaza",-97740.311770,-9296.495438,-53997.690069,"Physic")
o.Scale=1.000000
o.Orientation=0.706633,0.707530,0.005799,-0.006091
pocimac.CreateFood("palan2")

######sala de la palanca2




o=Bladex.CreateEntity("NoName1","Taburete",-116801.280713,-7602.650272,-6965.791750,"Weapon")
o.Scale=1.000000
o.Orientation=0.978999,0.026014,-0.012227,-0.201827


o=Bladex.CreateEntity("NoName2","Taburete",-119162.297442,-7590.528341,-7232.916681,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("torre1","Queso",-117775.573611,-8339.303875,-7071.475800,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("torre1")


o=Bladex.CreateEntity("torre2","Paletilla",-117878.037819,-8336.239707,-6700.005095,"Physic")
o.Scale=1.000000
o.Orientation=0.646231,0.611838,0.134009,-0.435983
pocimac.CreateFood("torre2")


o=Bladex.CreateEntity("NoName5","Jarra",-117899.663495,-8395.023294,-7684.246327,"Weapon")
o.Scale=1.160969
o.Orientation=0.707107,0.707107,0.000000,0.000000

####Lo que habia detras de las cajas

o=Bladex.CreateEntity("NoName0","Tabla_xl",-93152.320776,25.623264,-92637.850765,"Physic")
o.Scale=2.261271
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName1","Tabla_xl",-93162.139042,-1231.165330,-92630.806931,"Physic")
o.Scale=2.473119
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName2","Palangana",-94023.128714,-172.466883,-92887.017692,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 29 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName3","Mortero",-93331.674235,-261.592403,-92707.426076,"Weapon")
o.Scale=1.000000
o.Orientation=0.100936,0.992923,-0.057870,-0.023797


o=Bladex.CreateEntity("NoName4","Jarra",-94177.797050,847.690009,-93001.171293,"Weapon")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName5","Jarra",-93754.079393,846.399714,-92887.806900,"Weapon")
o.Scale=1.334504
o.Orientation=0.401554,-0.005481,-0.915815,0.002853


o=Bladex.CreateEntity("NoName6","Jarra",-93184.667618,837.247168,-92696.913621,"Weapon")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName1","Caja_i_r",-84199.169914,2676.924585,51206.773718,"Physic")
o.Scale=1.388690
o.Orientation=0.477714,0.477714,0.521334,-0.521334
Sparks.SetWoodenSparkling(o.Name) # Add


o=Bladex.CreateEntity("NoName2","Caja_i_r",-84316.250803,2530.958204,48394.126224,"Physic")
o.Scale=1.628348
o.Orientation=0.521334,0.521334,0.477714,-0.477714
Sparks.SetWoodenSparkling(o.Name) # Add


o=Bladex.CreateEntity("NoName0","Antorcha",-109944.729497,9928.643264,48724.191434,"Weapon")
o.Scale=1.000000
o.Orientation=0.990702,0.010585,-0.115964,0.070355
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.331250,(249,131,0)) ]


o=Bladex.CreateEntity("NoName1","Reja",-111396.217680,7277.564856,48831.562101,"Physic")
o.Scale=2.424389
o.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling(o.Name)    # Add


###############
###############
#####NUBES Y TELARANYAS#####
###############
############### 
"""" ### PLAGUE: Would like to restore these, but making them actors crashes the game. Possibly because missing bones in mesh?
o=Bladex.CreateEntity("nubecaos1","Nube",-104264.685000,-15788.483000,-85296.830000)
o.Static = 1
o.Scale=2.759181
o.Orientation=0.688355,-0.725374,0.000000,0.000000
o.Actor=1
o.Animation="Nube_ocho"
o.FPS=10.0
darfuncs.ObjAlpha(o,0.99,0.0)
o.TurnOn()
o.SendSectorMsgs=0

o=Bladex.CreateEntity("nubecaos2","Nube",-94476.358000,-8679.311000,-88879.067000)
o.Static = 1
o.Scale=2.261271
o.Orientation=0.777146,-0.629320,0.000000,0.000000
o.Actor=1
o.Animation="Nube_churro"
o.FPS=10.0
darfuncs.ObjAlpha(o,0.99,0.0)
o.TurnOn()
o.SendSectorMsgs=0
"""

o=Bladex.CreateEntity("tela2bic1","TelaranyaCuadrada",-107531.190013,-1240.593958,38304.095165,"Physic")
o.Scale=2.599273
o.Orientation=0.153837,0.126814,0.623309,-0.756134
darfuncs.ObjAlpha(o,0.5,0.7)

o=Bladex.CreateEntity("tela2k1","TelaranyaCuadrada",-72258.851399,-2350.426273,70286.851503,"Physic")
o.Scale=1.596263
o.Orientation=0.648459,0.293232,0.281958,-0.643440
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("tela2k2","TelaranyaCuadrada",-72614.249045,-2868.281791,67462.302624,"Physic")
o.Scale=2.194768
o.Orientation=0.653282,-0.188966,-0.270598,-0.681390
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("tela2k3","TelaranyaCuadrada",-73091.044096,-2373.054210,67274.524875,"Physic")
o.Scale=2.194768
o.Orientation=0.666548,-0.067773,-0.236037,-0.703851
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("tela2k4","TelaranyaCuadrada",-72441.577000,-2739.703000,69038.100000,"Physic")
o.Scale=2.548057
o.Orientation=0.477714,0.477714,-0.521334,0.521334
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaantes2k2","TelaranyaCuadrada",-66631.449000,-4436.741000,85822.313000,"Physic")
o.Scale=2.109128
o.Orientation=0.706434,0.504344,0.030844,-0.495618
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaantes2k1","TelaranyaCuadrada",-67160.399000,-4322.238000,85393.238000,"Physic")
o.Scale=2.151522
o.Orientation=0.677988,0.281958,0.200829,-0.648459
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaclo1","TelaranyaCuadrada",-111208.255000,6896.018000,91468.604000,"Physic")
o.Scale=2.548057
o.Orientation=0.632814,0.632814,-0.315509,-0.315509
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaclo2","TelaranyaCuadrada",-110481.118000,6683.655000,92202.683000,"Physic")
o.Scale=2.353088
o.Orientation=0.705384,0.705384,-0.049325,-0.049325
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaclo3","TelaranyaCuadrada",-112831.336000,11743.364000,85952.950000,"Physic")
o.Scale=3.609585
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.ObjAlpha(o)

o=Bladex.CreateEntity("telaclo4","TelaranyaCuadrada",-113594.392000,11063.591000,85462.990000,"Physic")
o.Scale=1.909366
o.Orientation=0.662327,0.662327,-0.247634,-0.247634
darfuncs.ObjAlpha(o)
"""
o=Bladex.CreateEntity("telaclo6","TelaranyaCuadrada",-113685.208000,11650.356000,64384.206000,"Physic")
o.Scale=2.376619
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.ObjAlpha(o,0.3,0.4)

o=Bladex.CreateEntity("telaclo5","TelaranyaCuadrada",-111774.983000,11869.209000,64884.307000,"Physic")
o.Scale=2.708348
o.Orientation=0.706138,0.593030,0.037007,0.385118
darfuncs.ObjAlpha(o,0.3,0.4)
"""
o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-109714.386799,14734.638303,88302.505488,"Physic")
o.Scale=1.000000
o.Orientation=0.919504,0.000864,-0.393075,-0.002091


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-108588.982353,14455.847622,89276.346611,"Physic")
o.Scale=1.000000
o.Orientation=0.509364,0.456979,-0.514947,-0.516282


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-108503.131907,14645.422210,87880.099360,"Physic")
o.Scale=1.347849
o.Orientation=0.579228,0.579228,0.405580,-0.405580



o=Bladex.CreateEntity("CajaPat1","Caja_i_i",-88178.748164,-3306.217858,17769.659430)
o.Scale=1.890462
o.Orientation=0.454519,0.454519,-0.541675,0.541675
Sparks.SetMetalSparkling(o.Name)    # add
o.Static = 1                        #

o=Bladex.CreateEntity("CajaPat2","Caja_i_i",-87621.944072,-3375.219052,19705.380543)
o.Scale=2.047099
o.Orientation=0.477714,0.477714,0.521334,-0.521334
Sparks.SetMetalSparkling(o.Name)    # add
o.Static = 1                        #

o=Bladex.CreateEntity("CajaPat3","Caja_i_i",-87538.605178,-5122.105681,19807.039904)
o.Scale=2.306723
o.Orientation=0.999756,-0.000162,-0.021636,-0.004450
Sparks.SetMetalSparkling(o.Name)    # add
o.Static = 1                        # 



o=Bladex.CreateEntity("TabInvPat","Tabla_xl",-88263.053103,-6667.612949,18776.776160)
o.Scale=2.548057
o.Orientation=0.000000,0.707107,0.000000,-0.707107
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat1","Adoquinpulsador",-85000.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat2","Adoquinpulsador",-85250.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat3","Adoquinpulsador",-85500.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat4","Adoquinpulsador",-85750.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat5","Adoquinpulsador",-86000.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat6","Adoquinpulsador",-86250.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0

o=Bladex.CreateEntity("AdoqInvPat7","Adoquinpulsador",-86500.000000,-4625.000000,18750.000000)
o.Scale=7.316018
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0



### restos junto a pocima 50 cerca de puente levadizo

o=Bladex.CreateEntity("NoName1","Tabla_rota",-96105.451786,-13148.091771,-38145.780559,"Physic")
o.Scale=1.928460
o.Orientation=0.678423,0.352122,0.188624,0.616582

o=Bladex.CreateEntity("NoName2","Piedra_07",-97503.902396,-12215.087204,-36208.825190,"Physic")
o.Scale=0.734577
o.Orientation=0.632540,0.774128,0.010103,0.022731

o=Bladex.CreateEntity("NoName3","Piedra_05",-97751.920172,-12082.669873,-35518.298948,"Physic")
o.Scale=0.811430
o.Orientation=0.655826,0.635855,0.279391,-0.295840

o=Bladex.CreateEntity("NoName4","Tabla_rota",-97460.677232,-12181.738910,-35361.786897,"Physic")
o.Scale=1.834864
o.Orientation=0.767119,0.634107,0.090228,-0.035999

o=Bladex.CreateEntity("NoName5","Piedra_08",-95547.435555,-12104.607891,-37755.982048,"Physic")
o.Scale=1.000000
o.Orientation=0.705624,0.621620,0.012063,-0.339910



### armas en sala de armas

bicheroragnar=Bladex.CreateEntity("BicheroRagnar","Bichero",-89627.1307105, 2413.46463881, -27355.9111636,"Weapon")
bicheroragnar.Scale=1.000000
bicheroragnar.Orientation=0.706418693066, 0.707097709179, -0.0300956219435, -0.00892991479486
ItemTypes.ItemDefaultFuncs(bicheroragnar)

o=Bladex.CreateEntity("Gladius1ArmeriaRagnar","Gladius",-83696.299602,3030.545453,-25145.362267,"Weapon")
o.Scale=1.000000
o.Orientation=0.047146,0.260465,-0.564124,0.782113
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("Gladius2ArmeriaRagnar","Gladius",-83971.818068,3491.713616,-25383.570949,"Weapon")
o.Scale=1.000000
o.Orientation=0.427953,0.019659,0.903194,0.026651
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("Escudo5ArmeriaRagnar","Escudo5",-83775.605920,3280.490801,-26113.253715,"Weapon")
o.Scale=1.000000
o.Orientation=0.593763,0.049804,-0.778936,-0.195507
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("Escudo2ArmeriaRagnar","Escudo2",-83880.442945,3236.928920,-26745.765495,"Weapon")
o.Scale=1.000000
o.Orientation=0.627584,-0.013243,0.753534,-0.195318
ItemTypes.ItemDefaultFuncs(o)
