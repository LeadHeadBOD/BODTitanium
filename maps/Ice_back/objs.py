##///
##||| Ice_back/objs.PY TITANIUM
##||| Change list:
##||| * Added some of the missing statues from Ice_M11 to make the level look less empty
##||| * Shadowpass
##\\\ 

import Sparks
import pocimac
import time
import Bladex
import Breakings
import Reference
import OnOff
import AuxFuncs


###
# Decorations missing from Ice_back that were present in Ice_M11

o=Bladex.CreateEntity("NoName18","Monjespada",46654.175000,-13892.237000,59160.04100,Reference.ObjType("Monjespada"))

o.Scale=2.283884
o.Orientation=0.705385,0.691539,0.111099,-0.108918
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName19","Monjecaliz",43127.177000,-13987.625000,59169.91700,Reference.ObjType("Monjecaliz"))

o.Scale=2.376619
o.Orientation=0.701451,0.695180,-0.111608,0.110610
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName156","Monjespada",45941.561000,-13022.491000,78983.88000,Reference.ObjType("Monjespada"))

o.Scale=2.424389
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName157","Monjespada",38487.870000,-13206.700000,78984.65900,Reference.ObjType("Monjespada"))

o.Scale=2.625266
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName158","Monjespada",42174.498000,-13195.542000,78961.76000,Reference.ObjType("Monjespada"))

o.Scale=2.651518
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName159","Monjespada",45802.388000,-13007.453000,87350.42700,Reference.ObjType("Monjespada"))

o.Scale=2.376619
o.Orientation=0.037007,0.037007,-0.706138,0.706138
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName160","Monjecaliz",38214.109000,-13242.412000,87348.49500,Reference.ObjType("Monjecaliz"))

o.Scale=2.678033
o.Orientation=0.018510,0.018510,0.706864,-0.706864
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName161","Monjecaliz",34360.780000,-13232.501000,87217.38500,Reference.ObjType("Monjecaliz"))

o.Scale=2.678033
o.Orientation=0.073913,0.073913,0.703233,-0.703233
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName162","Monjescudo",42242.322000,-13174.812000,87311.76500,Reference.ObjType("Monjescudo"))

o.Scale=2.625266
o.Orientation=0.030844,0.030844,-0.706434,0.706434
Sparks.SetStoneSparkling(o.Name)


#           -LeadHead
###


o=Bladex.CreateEntity("NoName16","Gancho",81586.230000,-2458.426000,-21708.40900,"Physic")

o.Scale=1.321291
o.Orientation=0.473867,0.504367,-0.494269,0.526082



o=Bladex.CreateEntity("NoName20","Lampcolg",44794.059000,-16328.538000,52737.33300,"Physic")

o.Scale=2.047099
o.Orientation=0.698805,0.714999,0.014781,-0.015123
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.401247,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("bra1","Braseroarana",30777.699000,-321.593000,54431.54800,"Physic")

o.Scale=1.000000
o.Orientation=0.710494,0.703578,-0.009453,0.009361
o.FiresIntensity=[ 3 ]
o.Lights=[ (14.321917,0.031250,(255,160,55)) ]



o=Bladex.CreateEntity("bra2","Braseroarana",6997.560000,-315.316000,54295.51600,"Physic")

o.Scale=1.000000
o.Orientation=0.709345,0.704818,-0.005576,0.005541
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.000000,0.031250,(255,196,128)) ]


"""
o=Bladex.CreateEntity("bra3","Braseroarana",1077.142000,-8463.218000,-12114.06300,"Physic")

o.Scale=1.220190
o.Orientation=0.501211,0.502808,-0.497189,0.498773
o.FiresIntensity=[ 3 ]
o.Lights=[ (2.925246,0.031250,(255,159,53)) ]



o=Bladex.CreateEntity("bra4","Braseroarana",37627.946000,-8447.335000,-12094.45900,"Physic")

o.Scale=1.000000
o.Orientation=0.497166,0.493135,0.506850,-0.502740
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149622,0.031250,(255,172,81)) ]
"""


o=Bladex.CreateEntity("NoName30","Lampared",37753.375000,4253.815000,-2435.70100,"Physic")

o.Scale=1.257163
o.Orientation=0.705778,0.708359,0.007269,-0.007296
o.FiresIntensity=[ 3 ]
o.Lights=[ (16.942511,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp1","Antorchaenpared",36823.639000,7102.525000,35627.14200,"Physic")

o.Scale=1.196147
o.Orientation=0.007380,0.043072,0.709812,-0.703034
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.642778,0.031250,(255,196,128)) ]





o=Bladex.CreateEntity("NoName38","Columnaestrecha",41545.435000,10246.904000,43117.42800,"Physic")

o.Scale=1.000000
o.Orientation=0.512251,0.505778,0.493920,-0.487679



o=Bladex.CreateEntity("NoName39","Columnaestrecha",41543.491000,10213.208000,37862.68800,"Physic")

o.Scale=1.000000
o.Orientation=0.493069,0.497049,0.502855,-0.506914



o=Bladex.CreateEntity("NoName40","Velon",13662.469000,4715.196000,13130.15000,"Physic")

o.Scale=1.871744
o.Orientation=0.499481,0.515868,-0.484131,0.500016
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName42","Lampcolg",61120.434000,-5452.532000,18357.82300,"Physic")

o.Scale=1.295256
o.Orientation=0.709354,0.704364,0.018618,-0.018487
o.FiresIntensity=[ 3 ]
o.Lights=[ (18.000000,0.209521,(255,193,125)) ]



o=Bladex.CreateEntity("NoName43","Lamparatecho",26759.790000,-14584.391000,53518.85300,"Physic")

o.Scale=2.216716
o.Orientation=0.710081,0.704106,0.003163,-0.003136
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.015032,(255,149,32)) ]



o=Bladex.CreateEntity("NoName44","Lamparatecho",11641.537000,-15380.208000,53672.99900,"Physic")

o.Scale=2.573537
o.Orientation=0.706779,0.707260,0.011106,-0.011114
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.003004,(255,183,102)) ]



o=Bladex.CreateEntity("NoName45","Lampared",19558.172000,-3613.270000,30840.49500,"Physic")

o.Scale=1.184304
o.Orientation=0.007026,0.006979,-0.709775,0.704359
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]





o=Bladex.CreateEntity("NoName49","Lamparatecho",18908.635000,-17184.025000,-11964.78400,"Physic")

o.Scale=1.763268
o.Orientation=0.533788,0.497541,-0.500173,0.466209
o.FiresIntensity=[ 3 ]
o.Lights=[ (18.679117,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName51","Lampared",29273.043000,-1480.900000,-8632.85400,"Physic")

o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149637,0.300000,(255,196,128)) ]





o=Bladex.CreateEntity("antp2","Antorchaenpared",40326.818000,-3666.154000,39692.00300,"Physic")

o.Scale=1.196147
o.Orientation=0.063070,0.046669,-0.698749,0.711052
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp3","Antorchaenpared",77014.019000,-6720.728000,-28543.69400,"Physic")

o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName58","Lampcolg",70199.386000,-8383.251000,-24185.25200,"Physic")

o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (25,0.331250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName61","Lampared",99577.632000,-7602.059000,25136.59500,"Physic")

o.Scale=1.000000
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,156,47)) ]



o=Bladex.CreateEntity("NoName62","Lampared",99485.371000,-7542.986000,46346.65200,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,160,55)) ]




o=Bladex.CreateEntity("cand1","Candelabro",43276.809000,-9798.611000,58588.92200,"Physic")

o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (0.200000,0.031250,(255,196,128)) ]  # now visible lights
AuxFuncs.GetSpot(o).Visible=0                   #
AuxFuncs.GetSpot(o).CastShadows=0               #   -LeadHead



o=Bladex.CreateEntity("cand2","Candelabro",46372.755000,-9757.552000,58188.54100,"Physic")

o.Scale=1.661078
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 3 ]
o.Lights=[ (0.300000,0.031250,(255,196,128)) ]  # now visible lights
AuxFuncs.GetSpot(o).Visible=0                   #
AuxFuncs.GetSpot(o).CastShadows=0               #   -LeadHead




o=Bladex.CreateEntity("antp5","Antorchaenpared",80628.489000,-1922.796000,29567.29800,"Physic")

o.Scale=1.000000
o.Orientation=0.517145,0.435338,0.482246,-0.557208
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,176,89)) ]



o=Bladex.CreateEntity("antp6","Antorchaenpared",99171.653000,-6992.157000,-19953.39700,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp7","Antorchaenpared",28040.619000,-2790.708000,90322.71900,"Physic")

o.Scale=1.564811
o.Orientation=0.415627,0.482246,-0.572062,0.517145
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName74","Lamparatecho",18918.925000,-16234.401000,-36662.47700,"Physic")

o.Scale=1.661078
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (17.000000,0.600000,(255,151,36)) ]



o=Bladex.CreateEntity("NoName75","Lamparatecho",18502.320000,-16377.101000,-31372.50400,"Physic")

o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 11 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName86","Semipuxero",25119.292000,9111.669000,5674.55300,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (4.000000,0.011778,(171,121,95)) ]



o=Bladex.CreateEntity("NoName87","Semipuxero",12867.552000,9104.368000,5655.05200,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (4.000000,0.031250,(250,185,78)) ]



o=Bladex.CreateEntity("NoName88","Semipuxero",24896.080000,7636.800000,-2344.13900,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (14.635594,0.075207,(255,196,128)) ]



o=Bladex.CreateEntity("antp8","Antorchaenpared",-2759.616000,-3891.203000,31437.43400,"Physic")

o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName95","Semipuxero",18911.048000,-1166.115000,-14962.67600,"Physic")

o.Scale=1.000000
o.Orientation=0.012342,0.012341,0.706999,-0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (13.000000,0.100000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName96","Roca2",66965.456000,-498.892000,-16623.00700,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName97","Roca2",89859.744000,-557.481000,-16255.01300,"Physic")

o.Scale=1.295256
o.Orientation=0.635860,0.771360,0.016651,-0.020199



o=Bladex.CreateEntity("NoName98","Lamparatecho",-7255.723000,-7981.683000,22318.64800,"Physic")

o.Scale=1.596263
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (22.000000,0.031250,(255,177,91)) ]



o=Bladex.CreateEntity("NoName99","Pendon3",18491.044000,-13567.816000,-41793.34900,"Physic")

o.Scale=1.763268
o.Orientation=0.000000,0.000000,0.008727,-0.999962



o=Bladex.CreateEntity("NoName100","Pendon3",11329.622000,-9174.528000,18613.75000,"Physic")

o.Scale=1.763268
o.Orientation=0.000000,0.000000,0.000000,1.000000



o=Bladex.CreateEntity("NoName101","Pendon3",25824.058000,-9336.141000,18526.46200,"Physic")

o.Scale=1.711410
o.Orientation=0.008693,0.000761,-0.000000,-0.999962



o=Bladex.CreateEntity("NoName102","Cuerda",26762.057000,-16076.729000,53526.99600,"Physic")

o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName104","Cuerda",61129.443000,-6985.007000,18367.80300,"Physic")

o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName105","Lampcolg",78519.624000,-5936.975000,16945.16000,"Physic")

o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (17.000000,0.325000,(254,237,158)) ]     # precision 0.4 -> 0.325



o=Bladex.CreateEntity("NoName106","Cuerda",78495.492000,-7616.791000,16959.86200,"Physic")

o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName107","Lampcolg",88209.891000,-7954.362000,-28233.66900,"Physic")

o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.131250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName108","Cuerda",70192.158000,-9945.927000,-24194.61600,"Physic")

o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName109","Cuerda",18516.077000,-20184.982000,-31356.96900,"Physic")

o.Scale=3.573847
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName113","Skeleton_Optimiced",-6193.634000,9394.129000,31422.68500,"Physic")

o.Scale=1.295256
o.Orientation=0.999848,0.017452,0.000000,0.000000



"""
o=Bladex.CreateEntity("NoName122","Blason3",24534.937000,7320.618000,43982.56200,"Physic")

o.Scale=0.878663
o.Orientation=0.707107,0.707107,0.000000,0.000000
"""



o=Bladex.CreateEntity("NoName126","Cuerda",76409.868000,-7042.680000,-1505.47900,"Physic")

o.Scale=2.238882
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName127","GargolaFernando",35585.447000,-20116.040000,30044.48200,"Physic")

o.Scale=1.459527
o.Orientation=0.000000,0.000000,0.688355,-0.725374



o=Bladex.CreateEntity("NoName128","GargolaFernando",24207.956000,-20539.535000,44077.91200,"Physic")

o.Scale=1.711410
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName129","GargolaFernando",13507.027000,-20679.733000,44024.09500,"Physic")

o.Scale=1.909366
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName130","GargolaFernando",31610.143000,-9369.284000,101350.69700,"Physic")

o.Scale=2.130220
o.Orientation=0.486740,0.486740,-0.512917,0.512917



o=Bladex.CreateEntity("NoName131","GargolaFernando",77293.398000,-11066.426000,73974.97100,"Physic")

o.Scale=1.474123
o.Orientation=0.043168,0.043168,-0.705788,0.705788



o=Bladex.CreateEntity("NoName132","GargolaFernando",69096.499000,-11083.545000,73742.28300,"Physic")

o.Scale=1.459527
o.Orientation=0.030844,0.030844,-0.706434,0.706434



o=Bladex.CreateEntity("NoName133","GargolaFernando",66824.466000,-11082.149000,71646.82100,"Physic")

o.Scale=1.644632
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName134","GargolaFernando",-29354.602000,-19650.859000,70968.31800,"Physic")

o.Scale=3.756148
o.Orientation=0.110616,0.110616,0.698401,-0.698401



o=Bladex.CreateEntity("NoName135","GargolaFernando",15082.487000,-6632.515000,136127.25500,"Physic")

o.Scale=2.306723
o.Orientation=0.504344,0.504344,-0.495618,0.495618



o=Bladex.CreateEntity("NoName136","GargolaFernando",14483.757000,-7671.527000,118880.77800,"Physic")

o.Scale=1.580459
o.Orientation=0.468543,0.468543,-0.529592,0.529592



o=Bladex.CreateEntity("NoName137","GargolaFernando",65069.903000,-4213.131000,-12207.73900,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName138","Lampared",95471.420000,-6878.196000,8095.56200,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,183,102)) ]



o=Bladex.CreateEntity("NoName139","Lampared",67319.445000,-6697.916000,6071.51500,"Physic")

o.Scale=1.000000
o.Orientation=0.003693,0.003703,0.707097,-0.707097
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.000000,0.031250,(255,196,128)) ]








o=Bladex.CreateEntity("NoName151","Tapiz3",-12257.660000,-809.346000,36695.98700,"Physic")

o.Scale=1.763268
o.Orientation=0.512917,0.512917,-0.486740,0.486740



o=Bladex.CreateEntity("NoName153","Tapiz",-7243.772000,-1457.584000,44761.42300,"Physic")

o.Scale=1.115668
o.Orientation=0.707107,0.707107,0.000000,0.000000





o=Bladex.CreateEntity("rast1","Rastrillo",-18434.386317,1450.339521,52836.813984,"Physic")

o.Scale=1.172579
o.Orientation=0.011966,-0.999910,-0.000765,0.005936
Sparks.SetMetalSparkling(o.Name)        # Add


o=Bladex.CreateEntity("NoName164","Lampcolg",76417.626000,-4880.519000,-1499.01800,"Physic")

o.Scale=1.184304
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.000000,0.200000,(255,154,43)) ]  # precision 0.7 -> 0.2



o=Bladex.CreateEntity("NoName165","Lampared",4244.903000,-1710.389000,-8485.78600,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149651,0.200000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName168","Lampared",30817.517000,-10187.595000,-24728.17800,"Physic")

o.Scale=1.000000
o.Orientation=0.012342,0.012341,-0.706999,0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("lamp1","Antorchaenpared",46227.492000,-3276.597000,25397.39500,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.0,0.200000,(255,145,23)) ]  # precision 0.5 -> 0.2 , intens 13.22 -> 12.0



o=Bladex.CreateEntity("NoName173","Lampared",73081.722000,-3898.882000,61278.91100,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.225097,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName184","Cuerda",-7264.384000,-9642.281000,22323.70200,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName185","Cuerda",-7262.890000,-12104.491000,22328.18000,"Physic")

o.Scale=2.329790
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName186","Lampared",88606.174000,-11568.073000,62513.37300,"Physic")

o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491198,0.491198
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.253340,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName187","Lampared",88601.606000,-4894.892000,55586.30200,"Physic")

o.Scale=1.000000
o.Orientation=0.512917,0.512917,-0.486740,0.486740
o.FiresIntensity=[ 3 ]
o.Lights=[ (6.081397,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp9","Antorchaenpared",87529.877000,-1861.412000,4035.72900,"Physic")

o.Scale=1.000000
o.Orientation=0.486740,0.486740,0.512917,-0.512917
o.FiresIntensity=[ 3 ]
o.Lights=[ (16.135740,1.800000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName195","Skeleton_Optimiced",40945.887000,5856.769000,3837.72100,"Physic")

o.Scale=1.115668
o.Orientation=0.999848,0.017452,0.000000,0.000000



o=Bladex.CreateEntity("NoName196","Skeleton_Optimiced",41105.645000,5830.270000,8847.20400,"Physic")

o.Scale=1.126825
o.Orientation=0.031370,-0.001421,0.998993,-0.032040



o=Bladex.CreateEntity("NoName198","Varillaancha",44758.841000,-17093.184000,52705.56900,"Physic")

o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName0","Roca1Aurelio",12460.735000,10471.325000,26081.65600,"Physic")

o.Scale=1.000000
o.Orientation=0.643440,0.643440,0.293232,-0.293232



o=Bladex.CreateEntity("NoName3","Roca1Aurelio",26848.966000,10670.622000,25223.86000,"Physic")

o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName4","Roca1Aurelio",24947.191000,2686.884000,26268.30200,"Physic")

o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName7","Roca1Aurelio",9171.728000,10565.428000,44968.79100,"Physic")

o.Scale=1.000000
o.Orientation=0.668583,0.668583,0.230211,-0.230211



o=Bladex.CreateEntity("NoName10","Columnaestrecha",13566.764000,9655.122000,27176.96800,"Physic")

o.Scale=1.612226
o.Orientation=0.641514,0.725100,0.187524,0.165907



o=Bladex.CreateEntity("NoName12","Columnaestrecha",20941.546000,9980.168000,27916.73600,"Physic")

o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName14","Roca1Aurelio",32720.199000,7511.212000,23071.51000,"Physic")

o.Scale=1.000000
o.Orientation=0.353553,0.353553,0.612372,-0.612373
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName18","PiedraNevada",40048.379000,-760.955000,29541.04400,"Physic")

o.Scale=1.160969
o.Orientation=0.332154,0.320758,0.638062,-0.616170



o=Bladex.CreateEntity("NoName0","Lampcolg",18645.782000,-14257.400000,21751.81000,"Physic")

o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,137,6)) ]



o=Bladex.CreateEntity("NoName1","Varilla",18601.561000,-16416.733000,21752.93800,"Physic")

o.Scale=1.000000
o.Orientation=0.491198,0.491198,-0.508650,-0.508650



o=Bladex.CreateEntity("NoName2","Lampared",11786.905000,-9992.735000,-25228.73500,"Physic")

o.Scale=1.000000
o.Orientation=0.012342,0.012341,0.706999,-0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName1","Cuerda",18841.421000,-19122.294000,-11964.19600,"Physic")

o.Scale=1.082857
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName0","Cuerda",18929.935000,-21304.843000,-36646.07900,"Physic")

o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName1","Cuerda",18929.935000,-18654.843000,-36646.07900,"Physic")

o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("antp10","Antorcha",20900.482000,10908.661000,-15762.35900,"Physic")

o.Scale=1.000000
o.Orientation=0.999391,0.034899,0.000000,0.000000
o.FiresIntensity=[ 47 ]
o.Lights=[ (0.000000,0.031250,(255,147,28)) ]



o=Bladex.CreateEntity("NoName1","Gargola",36041.545000,-16508.716000,37051.357000,"Physic")

o.Scale=3.203323
o.Orientation=0.473147,0.473147,0.525483,-0.525483



o=Bladex.CreateEntity("NoName2","Gargola",-68364.312000,10442.585000,41374.742000,"Physic")

o.Scale=5.537023
o.Orientation=0.383874,0.289286,-0.633913,0.605895



o=Bladex.CreateEntity("NoName3","Gargola",-67422.650000,2638.176000,91441.019000,"Physic")

o.Scale=6.055760
o.Orientation=0.687569,0.687569,-0.165071,0.165071



o=Bladex.CreateEntity("NoName4","Gargola",5791.407000,-21590.573000,75889.368000,"Physic")

o.Scale=4.913826
o.Orientation=0.517145,0.517145,0.482246,-0.482246



o=Bladex.CreateEntity("NoName1","Piedra_09",39440.287000,10185.039000,-10041.607000,"Physic")

o.Scale=0.614119
o.Orientation=0.838026,-0.070242,0.487911,0.233926



o=Bladex.CreateEntity("NoName2","Piedra_08",39938.218000,10233.496000,-10346.238000,"Physic")

o.Scale=0.400344
o.Orientation=0.737925,0.654760,-0.135781,-0.091206



o=Bladex.CreateEntity("NoName3","Piedra_08",42080.836000,10217.281000,-15161.331000,"Physic")

o.Scale=0.412475
o.Orientation=0.503737,-0.311211,-0.568165,-0.571476



o=Bladex.CreateEntity("NoName4","Piedra_01",42032.293000,7878.537000,-9366.744000,"Physic")

o.Scale=0.626463
o.Orientation=0.064310,-0.907792,0.389180,-0.142540



o=Bladex.CreateEntity("NoName6","Piedra_03",41240.905000,7904.631000,-9004.997000,"Physic")

o.Scale=0.756836
o.Orientation=0.650870,0.754143,-0.041130,-0.077104



o=Bladex.CreateEntity("NoName7","Piedra_03",43472.262000,7869.760000,-8178.348000,"Physic")

o.Scale=1.000000
o.Orientation=0.757654,-0.649838,-0.016274,-0.058357



o=Bladex.CreateEntity("NoName8","Piedra_03",46505.137000,6378.835000,-3553.161000,"Physic")

o.Scale=1.000000
o.Orientation=0.638005,0.764985,-0.051933,-0.071066



o=Bladex.CreateEntity("NoName9","Piedra_03",47088.700000,6396.470000,-2471.642000,"Physic")

o.Scale=0.779768
o.Orientation=0.629766,0.771274,-0.054076,-0.074881



o=Bladex.CreateEntity("NoName10","Piedra_03",43195.775000,3148.128000,5973.518000,"Physic")

o.Scale=0.734577
o.Orientation=0.626156,0.776029,-0.023149,-0.071917



o=Bladex.CreateEntity("NoName11","Piedra_03",44444.858000,3172.819000,4409.355000,"Physic")

o.Scale=0.534261
o.Orientation=0.680728,0.726759,-0.003191,-0.091767



o=Bladex.CreateEntity("NoName12","Piedra_03",44044.000000,3168.812000,4889.425000,"Physic")

o.Scale=0.632728
o.Orientation=0.580536,0.554098,0.400097,-0.442578



o=Bladex.CreateEntity("NoName13","Tabla_rota",45368.723000,3180.421000,3230.493000,"Physic")

o.Scale=1.834864
o.Orientation=0.382688,0.383962,-0.592596,0.595779
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Piedra_08",43283.847000,6395.996000,-98.012000,"Physic")

o.Scale=0.392456
o.Orientation=0.229941,-0.843134,0.103388,0.474935



o=Bladex.CreateEntity("NoName16","Piedra_02",43337.990000,6425.429000,-2164.373000,"Physic")

o.Scale=0.408391
o.Orientation=0.681394,-0.137667,-0.603692,-0.390265


o=Bladex.CreateEntity("lamparaenciende","Lamparatecho",31380.406000,5423.344000,40437.497000,"Physic")

o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
OnOff.AddLightData("lamparaenciende",25,0.1,(255,155,45))
o.Lights=[ (0,0,(255,155,45)) ]



o=Bladex.CreateEntity("antp11","Antorchaenpared",37953.094860,8296.850435,23945.574580,"Physic")

o.Scale=1.00
o.Orientation=0.454519,0.525483,-0.541675,0.473147
o.FiresIntensity=[ 20 ]
o.Lights=[ (0.000000,0.031250,(255,142,17)) ]



o=Bladex.CreateEntity("NoName2","Piedra_04",29895.204000,10848.005000,37922.793000,"Physic")

o.Scale=0.626463
o.Orientation=0.487832,0.367607,0.442270,-0.656721



o=Bladex.CreateEntity("NoName3","Piedra_03",29672.981000,10936.438000,36897.495000,"Physic")

o.Scale=0.478871
o.Orientation=0.656851,0.744354,-0.002488,-0.120322



o=Bladex.CreateEntity("NoName4","Piedra_02",29901.927000,10894.081000,34457.305000,"Physic")

o.Scale=0.671653
o.Orientation=0.887171,-0.428683,-0.141364,-0.095786



o=Bladex.CreateEntity("NoName7","Piedra_06",30800.882000,10942.567000,35733.591000,"Physic")

o.Scale=0.460185
o.Orientation=0.508155,0.782730,-0.222210,0.282372



o=Bladex.CreateEntity("NoName9","Piedra_01",34856.391000,10914.847000,41465.476000,"Physic")

o.Scale=0.705914
o.Orientation=0.819906,-0.067501,-0.558863,0.104256



o=Bladex.CreateEntity("NoName10","Piedra_01",36066.107000,10913.965000,40937.095000,"Physic")

o.Scale=1.000000
o.Orientation=0.956023,-0.164803,0.080757,0.228775



o=Bladex.CreateEntity("NoName11","Piedra_01",36190.818000,10829.846000,40124.565000,"Physic")

o.Scale=1.000000
o.Orientation=0.083949,-0.814015,0.568076,0.087302



o=Bladex.CreateEntity("NoName12","Piedra_08",37974.471000,11071.546000,39606.350000,"Physic")

o.Scale=1.000000
o.Orientation=0.584076,-0.686819,0.268481,0.339195



o=Bladex.CreateEntity("NoName13","Piedra_08",39439.386000,11160.714000,41375.980000,"Physic")

o.Scale=0.614119
o.Orientation=0.710353,0.685870,-0.144326,-0.064430



o=Bladex.CreateEntity("NoName14","Piedra_08",38881.743000,10902.211000,42853.803000,"Physic")

o.Scale=0.685153
o.Orientation=0.645648,0.706853,-0.151228,-0.246226





o=Bladex.CreateEntity("NoName26","Piedra_09",37151.404000,10874.220000,29671.249000,"Physic")

o.Scale=0.658419
o.Orientation=0.836907,-0.525437,0.132074,0.077838



o=Bladex.CreateEntity("NoName28","Piedra_01",38764.895000,11173.447000,30060.318000,"Physic")

o.Scale=1.000000
o.Orientation=0.928314,-0.254330,-0.204037,0.178658



o=Bladex.CreateEntity("NoName29","Piedra_01",38806.279000,9896.195000,27190.445000,"Physic")

o.Scale=1.416603
o.Orientation=0.952096,-0.200748,0.014967,0.230196



o=Bladex.CreateEntity("NoName30","Piedra_01",38904.614000,9879.553000,25573.893000,"Physic")

o.Scale=1.000000
o.Orientation=0.200225,-0.716910,-0.135430,0.653918






o=Bladex.CreateEntity("NoName32","Piedra_01",37432.739000,10854.848000,31477.225000,"Physic")

o.Scale=1.000000
o.Orientation=0.028455,-0.981410,-0.080413,0.171923



o=Bladex.CreateEntity("NoName41","Piedra_03",42882.466000,9846.411000,20364.060000,"Physic")
o.Scale=1.334504
o.Orientation=0.641255,0.762424,-0.054364,-0.067428
o.CastShadows=0


o=Bladex.CreateEntity("NoName42","Piedra_03",42309.537000,9876.368000,19783.178000,"Physic")
o.Scale=1.000000
o.Orientation=0.509059,0.514529,0.399413,-0.562662
o.CastShadows=0


o=Bladex.CreateEntity("NoName43","Piedra_03",44533.766000,10130.006000,21534.647000,"Physic")
o.Scale=1.000000
o.Orientation=0.657604,0.749527,-0.049722,-0.057400
o.CastShadows=0


o=Bladex.CreateEntity("NoName0","Piedra_01",6118.523000,10939.784000,43222.056000,"Physic")
o.Scale=0.727304
o.Orientation=0.580596,0.033825,0.740905,0.335892
o.CastShadows=0




o=Bladex.CreateEntity("NoName2","Piedra_01",4543.086000,10853.543000,39950.390000,"Physic")
o.Scale=0.584313
o.Orientation=0.283617,0.776721,-0.508730,-0.239708
o.CastShadows=0






o=Bladex.CreateEntity("NoName7","Piedra_09",4079.773000,10892.111000,33824.705000,"Physic")
o.Scale=0.483659
o.Orientation=0.403124,0.396452,0.551818,-0.613036
o.CastShadows=0


o=Bladex.CreateEntity("NoName8","Piedra_09",6428.690000,10878.554000,31144.584000,"Physic")
o.Scale=0.396380
o.Orientation=0.288820,0.849225,-0.014680,-0.441797
o.CastShadows=0


o=Bladex.CreateEntity("NoName11","Piedra_01",7681.104000,10913.721000,37775.852000,"Physic")
o.Scale=0.344836
o.Orientation=0.471764,-0.697441,0.256297,0.474686
o.CastShadows=0


o=Bladex.CreateEntity("NoName12","Piedra_01",9905.808000,10816.914000,29031.764000,"Physic")
o.Scale=1.000000
o.Orientation=0.268290,-0.941415,-0.093500,0.181701
o.CastShadows=0




o=Bladex.CreateEntity("NoName1","Piedra_01",-1850.096000,11185.034000,39426.638000,"Physic")
o.Scale=0.678370
o.Orientation=0.785911,-0.340660,-0.514005,0.045766
o.CastShadows=0


o=Bladex.CreateEntity("NoName2","Piedra_01",-3577.577000,10926.629000,38195.466000,"Physic")
o.Scale=0.795442
o.Orientation=0.983486,-0.092047,-0.071258,0.138582
o.CastShadows=0

o=Bladex.CreateEntity("NoName3","Piedra_01",857.893000,10910.749000,39422.421000,"Physic")
o.Scale=1.000000
o.Orientation=0.986832,-0.085500,-0.049253,0.128163
o.CastShadows=0




o=Bladex.CreateEntity("NoName7","Tabla_rota",645.932000,10948.945000,38232.724000,"Physic")

o.Scale=1.269735
o.Orientation=0.673723,0.680595,0.202387,-0.204761
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Piedra_01",721.186000,10922.316000,43173.815000,"Physic")
o.Scale=0.620260
o.Orientation=0.062821,-0.971984,-0.225588,-0.020272
o.CastShadows=0


o=Bladex.CreateEntity("NoName12","Piedra_01",-146.919000,11116.573000,42287.204000,"Physic")
o.Scale=0.645445
o.Orientation=0.188914,-0.503129,0.196860,-0.820012
o.CastShadows=0




o=Bladex.CreateEntity("NoName16","Piedra_09",3283.312000,10885.007000,28963.297000,"Physic")
o.Scale=0.498315
o.Orientation=0.672245,0.722446,0.119303,-0.109202
o.CastShadows=0


o=Bladex.CreateEntity("NoName23","Tapiz",-5193.572000,165.780000,37884.034000,"Physic")

o.Scale=1.334504
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName24","Tapiz2",-5244.699000,181.449000,35563.534000,"Physic")

o.Scale=1.220190
o.Orientation=0.500000,0.500000,0.500000,-0.500000



o=Bladex.CreateEntity("NoName25","Tapiz2",-5212.190000,82.848000,43053.751000,"Physic")

o.Scale=1.220190
o.Orientation=0.500000,0.500000,0.500000,-0.500000



o=Bladex.CreateEntity("NoName26","Tapiz3",-5249.089000,60.712000,41460.131000,"Physic")

o.Scale=1.196147
o.Orientation=0.495618,0.495618,0.504344,-0.504344





o=Bladex.CreateEntity("NoName30","Velon",-7766.649000,1712.476000,41549.105000,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 19 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName0","Peanapiedra",41043.555000,-3357.950000,23407.974000,"Physic")

o.Scale=3.203323
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName1","Peanapiedra",41092.022000,-3399.101000,20436.709000,"Physic")

o.Scale=3.109114
o.Orientation=0.486740,0.486740,-0.512917,0.512917



o=Bladex.CreateEntity("NoName2","Peanapiedra",40650.658000,-11332.161000,54738.321000,"Physic")

o.Scale=4.232522
o.Orientation=0.517145,0.517145,-0.482246,0.482246



o=Bladex.CreateEntity("NoName3","Peanapiedra",40697.934000,-11306.381000,57761.391000,"Physic")

o.Scale=4.232522
o.Orientation=0.491198,0.491198,0.508650,-0.508650



o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-59714.604000,23610.505000,49084.340000,"Physic")

o.Scale=1.518790
o.Orientation=0.662327,0.662327,0.247634,-0.247634
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-54272.438000,20573.091000,47033.439000,"Physic")

o.Scale=1.644632
o.Orientation=0.521334,0.521334,0.477714,-0.477714
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-46833.883000,18597.770000,51664.973000,"Physic")

o.Scale=2.497850
o.Orientation=0.356614,0.370311,0.609234,-0.603763
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",-61785.247000,23613.491000,47711.902000,"Physic")

o.Scale=1.474123
o.Orientation=0.444997,0.444997,0.549525,-0.549525
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",-52059.127000,20496.843000,46633.535000,"Physic")

o.Scale=1.947745
o.Orientation=0.674380,0.674380,0.212631,-0.212631
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Adoquinpulsador",-41337.590000,18587.708000,41533.269000,"Physic")

o.Scale=1.596263
o.Orientation=0.624338,0.624338,0.331967,-0.331967
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Adoquinpulsador",-39814.149000,18187.040000,41633.963000,"Physic")

o.Scale=1.711410
o.Orientation=0.699684,0.580580,-0.066622,0.411012
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Adoquinpulsador",-61075.305000,23692.694000,52920.124000,"Physic")

o.Scale=1.184304
o.Orientation=0.695266,0.695266,0.128860,-0.128860
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Adoquinpulsador",-56977.564000,23581.278000,85248.539000,"Physic")

o.Scale=1.628348
o.Orientation=0.655618,0.655618,0.264887,-0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Adoquinpulsador",-57155.425000,23509.143000,74801.239000,"Physic")

o.Scale=1.890462
o.Orientation=0.635543,0.635543,0.309975,-0.309975
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Adoquinpulsador",-66353.804000,23602.727000,88373.065000,"Physic")

o.Scale=1.533978
o.Orientation=0.582745,0.582745,0.400510,-0.400510
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Adoquinpulsador",-17106.446000,1248.493000,43519.075000,"Physic")

o.Scale=1.334504
o.Orientation=0.627211,0.627211,0.326506,-0.326506
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Adoquinpulsador",-16555.415000,1344.401000,41362.085000,"Physic")

o.Scale=0.932718
o.Orientation=0.656599,0.681538,-0.221696,0.235022
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Adoquinpulsador",-20203.864000,1324.629000,30587.968000,"Physic")

o.Scale=1.040604
o.Orientation=0.608148,-0.603359,0.365953,0.363584
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Adoquinpulsador",-20626.535000,1224.723000,32895.985000,"Physic")

o.Scale=1.430769
o.Orientation=0.545621,0.545621,0.449775,-0.449775
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName15","Adoquinpulsador",-16664.697000,94.352000,13960.022000,"Physic")

o.Scale=1.549318
o.Orientation=0.579228,0.579228,0.405580,-0.405580
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName16","Adoquinpulsador",-16093.575000,258.047000,11387.464000,"Physic")

o.Scale=0.896324
o.Orientation=0.348196,0.348196,0.615434,-0.615434
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName17","Adoquinpulsador",-15482.606000,240.019000,-5097.095000,"Physic")

o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName18","Adoquinpulsador",13577.308000,9051.129000,138830.416000,"Physic")

o.Scale=4.913826
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",83064.777000,213.861000,34068.929000,"Physic")

o.Scale=1.986894
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",82439.667000,521.483000,34855.288000,"Physic")

o.Scale=2.448633
o.Orientation=0.999848,0.017452,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",81677.777000,960.911000,35542.023000,"Physic")

o.Scale=3.300387
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",86269.799000,-17.848000,35324.934000,"Physic")

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",84619.860000,-74.225000,35176.487000,"Physic")

o.Scale=1.257163
o.Orientation=0.410619,0.410619,0.575667,-0.575667
Sparks.SetStoneSparkling(o.Name)



o=Bladex.CreateEntity("ant1","Antorcha",39172.568526,7179.298233,8671.649070,"Physic")
o.Scale=1.000000
o.Orientation=0.022930,0.976981,-0.211561,0.014995
o.FiresIntensity=[ 43 ]
o.Lights=[ (0.000000,0.031250,(255,146,26)) ]



o=Bladex.CreateEntity("antj21","Antorcha",37353.534568,7181.237040,8713.195738,"Physic")
o.Scale=1.000000
o.Orientation=0.907006,0.026734,0.413806,0.073421
o.FiresIntensity=[ 40 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]  # PLAGUE: maybe should match colour with ant1?



o=Bladex.CreateEntity("antj22","Antorcha",6826.616000,10909.064000,38302.013000,"Physic")
o.Scale=1.000000
o.Orientation=0.119320,0.446086,0.884867,0.061490
o.FiresIntensity=[ 41 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj21","Antorcha",45332.620000,3177.610000,6838.013000,"Physic")
o.Scale=1.000000
o.Orientation=0.998980,0.017240,0.009372,-0.040663
o.FiresIntensity=[ 39 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj22","Antorcha",43994.348000,3170.987000,6955.544000,"Physic")
o.Scale=1.000000
o.Orientation=0.023556,0.483866,-0.006845,-0.874798
o.FiresIntensity=[ 36 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj23","Antorcha",44164.250000,6436.470000,-372.178000,"Physic")
o.Scale=1.000000
o.Orientation=0.372292,0.614889,-0.321387,-0.616459
o.FiresIntensity=[ 43 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antpj1","Antorchaenpared",15507.157000,9505.489000,-8570.579000,"Physic")
o.Scale=1.000000
o.Orientation=0.614294,0.680743,0.301968,-0.260858
o.FiresIntensity=[ 42 ]
o.Lights=[ (0.000000,0.031250,(223,117,0)) ]





o=Bladex.CreateEntity("NoName2","Columna",-1665.300176,11082.835481,9603.946610,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000




o=Bladex.CreateEntity("NoName0","Adoquinpulsador",21241.250449,-2477.105488,86329.466115,"Physic")
o.Scale=1.745810
o.Orientation=0.719479,0.694506,-0.002406,0.002327
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",16639.649230,-2726.278912,86303.130065,"Physic")
o.Scale=1.000000
o.Orientation=0.517145,0.517145,0.482246,-0.482246
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",17637.172825,-2737.494712,86398.919747,"Physic")
o.Scale=1.082857
o.Orientation=0.396108,0.398970,0.589933,-0.579570
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",17004.168039,-3281.233417,86612.402003,"Physic")
o.Scale=1.104622
o.Orientation=0.701196,0.712421,-0.017054,-0.022134
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",20315.668382,-3254.426923,86415.121206,"Physic")
o.Scale=1.321291
o.Orientation=0.718787,0.694851,0.015780,-0.016698
Sparks.SetStoneSparkling(o.Name)
##antorcha dentro del elevador##

o=Bladex.CreateEntity("antcrip1","Antorchaenpared",30849.288000,5379.545000,9292.320000,"Physic")
o.Scale=1.000000
o.Orientation=0.549525,0.444997,0.444997,-0.549525
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.312500,(206,108,0)) ]


o=Bladex.CreateEntity("antcrip2","Antorchaenpared",38158.802000,6135.132000,15103.625000,"Physic")
o.Scale=1.000000
o.Orientation=0.061628,-0.024678,0.704416,-0.706676
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.231250,(255,145,23)) ]
################################

rassn1=Bladex.CreateEntity("Rassn1","Rastrillo",15764.171927,-10520.440035,49982.498048,"Physic")
rassn1.Scale=1.072135
rassn1.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("Rassn1")



o=Bladex.CreateEntity("NoName1","Antorchaenpared",63277.155000,-5876.235000,-27959.513000,"Physic")
o.Scale=1.000000
o.Orientation=0.049325,-0.061628,0.705384,-0.704416
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000, 0.100000, (255,158,51)) ]  # precision 0.131250 -> 0.1


adoq=Bladex.CreateEntity("Adice1","Adoquinpulsador",89051.158765,-10344.732901,67701.517490,"Physic")
adoq.Scale=8.243872
adoq.Orientation=0.495618,0.495618,-0.504344,-0.504344
adoq.CastShadows=0
adoq.Alpha = 0
Reference.EntitiesSelectionData["Adice1"]=[0, 0,""]


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",38678.530992,-714.449155,40791.939184,"Physic")
o.Scale=2.814640
o.Orientation=0.363860,0.363559,0.606632,-0.606159
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",40013.899720,-732.161975,40491.292930,"Physic")
o.Scale=2.376619
o.Orientation=0.449775,0.449775,0.545621,-0.545621
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","LapidaCaballero",25782.415271,-215.716500,859.753527,"Physic")
o.Scale=1.000000
o.Orientation=0.737277,0.675590,0.000000,0.000000




o=Bladex.CreateEntity("NoName3","Lapida3",28936.718299,-237.255312,-928.916282,"Physic")
o.Scale=1.745810
o.Orientation=0.198276,0.974557,-0.008201,-0.104206




o=Bladex.CreateEntity("NoName4","Lapida3",26401.920594,-99.360057,10123.505969,"Physic")
o.Scale=1.503752
o.Orientation=0.994522,0.104528,0.000000,0.000000




o=Bladex.CreateEntity("NoName5","Lapida",31763.195480,-28.179462,12347.127847,"Physic")
o.Scale=1.967222
o.Orientation=0.904169,0.121203,0.393285,-0.114518




o=Bladex.CreateEntity("NoName7","LapidaBarbaro",12023.898378,-135.466260,11993.982624,"Physic")
o.Scale=1.115668
o.Orientation=0.152057,0.141795,0.715372,-0.667095





o=Bladex.CreateEntity("NoName10","LapidaBarbaro",29794.510201,-257.214004,33836.172794,"Physic")
o.Scale=1.220190
o.Orientation=0.709475,0.685132,-0.118725,0.114652




o=Bladex.CreateEntity("NoName11","Lapida3",32458.152768,-321.183836,38738.783526,"Physic")
o.Scale=1.967222
o.Orientation=0.871924,0.068622,0.483315,0.038038




o=Bladex.CreateEntity("NoName31","Adoquinpulsador",12541.764721,298.609124,29254.380915,"Physic")
o.Scale=2.026831
o.Orientation=0.664463,0.688984,0.159064,-0.241845
Sparks.SetStoneSparkling(o.Name)




o=Bladex.CreateEntity("NoName4","BarrilPieza6",4131.179111,-48.645591,113750.270363,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName5","BarrilPieza4",4185.414987,-47.684572,114319.095526,"Physic")
o.Scale=1.000000
o.Orientation=0.391260,0.486612,-0.737755,-0.256595



o=Bladex.CreateEntity("NoName6","BarrilPieza4",3539.845227,-57.182872,114668.998679,"Physic")
o.Scale=1.269735
o.Orientation=0.824692,0.071252,-0.105614,-0.551047



o=Bladex.CreateEntity("NoName7","BarrilPieza4",1920.051401,-50.409808,114689.929189,"Physic")
o.Scale=1.000000
o.Orientation=0.619258,0.363078,-0.566228,-0.405067



o=Bladex.CreateEntity("NoName8","BarrilPieza4",2683.332334,-55.858381,115319.395570,"Physic")
o.Scale=1.000000
o.Orientation=0.801553,0.122073,-0.192275,-0.552848



o=Bladex.CreateEntity("NoName9","BarrilPieza4",3759.489034,-49.198789,112687.354481,"Physic")
o.Scale=1.000000
o.Orientation=0.674525,0.325598,-0.478824,-0.457962



o=Bladex.CreateEntity("NoName10","BarrilPieza4",4543.696302,-56.321027,112971.661367,"Physic")
o.Scale=1.244716
o.Orientation=0.764335,-0.217331,0.325688,-0.512334



o=Bladex.CreateEntity("NoName11","BarrilPieza6",2056.639681,-44.909080,112540.229026,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000




o=Bladex.CreateEntity("NoName12","Caja_i_r",7724.018772,-602.016841,115790.574062,"Physic")
o.Scale=1.000000
o.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetWoodenSparkling(o.Name)
o.Static=1



o=Bladex.CreateEntity("NoName15","Hoguera",1604.858220,-196.690820,110888.486192,Reference.ObjType("Hoguera"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 44 ]
o.Lights=[ (0.000000,0.331250,(239,189,143)) ]



o=Bladex.CreateEntity("NoName16","BarrilPieza4",920.978264,-52.881266,107351.717403,"Physic")
o.Scale=1.000000
o.Orientation=0.684900,0.299400,-0.477216,-0.462099



o=Bladex.CreateEntity("NoName17","BarrilPieza4",1052.745974,-48.488641,108265.468807,"Physic")
o.Scale=1.000000
o.Orientation=0.820416,-0.093729,0.141372,-0.546028



o=Bladex.CreateEntity("NoName19","BarrilPieza4",1992.386716,-49.881469,109407.818545,"Physic")
o.Scale=1.000000
o.Orientation=0.827484,-0.001498,-0.010468,-0.561390



o=Bladex.CreateEntity("NoName20","BarrilPieza4",2597.257927,-46.905012,109407.805560,"Physic")
o.Scale=1.000000
o.Orientation=0.801218,-0.144941,0.219336,-0.537525



o=Bladex.CreateEntity("NoName21","BarrilPieza4",1392.448414,-50.582323,110135.778432,"Physic")
o.Scale=1.000000
o.Orientation=0.695961,0.299410,-0.461341,-0.461688



o=Bladex.CreateEntity("NoName0","Antorchaenpared",59200.588222,-1891.683260,88222.229891,"Physic")
o.Scale=1.000000
o.Orientation=0.485751,0.560887,-0.520522,0.422503
o.FiresIntensity=[ 0 ]
o.Lights=[ (6.000000,0.102000,(255,154,43)) ]   # precision 0.23 -> 0.102, intens 5.0 -> 6.0

### Missing stuff from Ice_M11 start
o=Bladex.CreateEntity("NoName1","Caja_i_r",49810.999824,-2014.085634,67799.248010,Reference.ObjType("Caja_i_r"))
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetWoodenSparkling(o.Name)





o=Bladex.CreateEntity("NoName4","BarrilPieza4",48272.407291,-1152.636360,70365.776859,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.671665,0.314692,-0.480860,-0.467556



o=Bladex.CreateEntity("NoName5","BarrilPieza4",48762.721209,-1152.340378,69900.342015,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.645131,-0.353699,0.515080,-0.439768



o=Bladex.CreateEntity("NoName6","BarrilPieza6",48643.695934,-1175.329819,70333.902391,Reference.ObjType("BarrilPieza6"))
o.Scale=1.000000
o.Orientation=0.722168,0.689675,0.046374,0.025906



o=Bladex.CreateEntity("NoName7","BarrilPieza4",47578.088994,-1152.013273,70071.997214,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.310839,0.523016,-0.763399,-0.216922



o=Bladex.CreateEntity("NoName8","BarrilPieza4",47494.827259,-1186.566635,69873.197595,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.194088,0.746481,0.587840,0.244009



o=Bladex.CreateEntity("NoName9","BarrilPieza4",49884.657656,-1156.619611,69283.546076,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.637812,0.334450,-0.545057,-0.429245



o=Bladex.CreateEntity("NoName10","BarrilPieza4",42864.922132,-1149.578610,69277.094851,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.297262,0.512761,-0.778350,-0.207081



o=Bladex.CreateEntity("NoName11","BarrilPieza6",43047.497523,-1174.824630,69607.768942,Reference.ObjType("BarrilPieza6"))
o.Scale=1.000000
o.Orientation=0.733926,0.677260,-0.004957,0.051441



o=Bladex.CreateEntity("NoName12","BarrilPieza5",43934.270119,-1133.722058,70163.248479,Reference.ObjType("BarrilPieza5"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName13","BarrilPieza4",42428.767308,-1152.033521,70217.727046,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.642517,0.347373,-0.519761,-0.443116



o=Bladex.CreateEntity("NoName14","BarrilPieza4",43765.075091,-1157.518642,69183.690080,Reference.ObjType("BarrilPieza4"))
o.Scale=1.257163
o.Orientation=0.780547,0.195186,-0.286531,-0.520144
### End of stuff

icebloqueback=Bladex.CreateEntity("Icebloqueback","Bloque",-22646.140706,9352.146791,64762.641156)
icebloqueback.Static=1                                                                          
icebloqueback.Scale=2.958215                                                                    
icebloqueback.Orientation=0.507948,0.496397,-0.494077,-0.501465                                 
icebloqueback.CastShadows=0
icebloqueback.Alpha=0
Reference.EntitiesSelectionData[icebloqueback.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-23214.237170,-2325.974403,51857.467553)
o.Scale=8.557520
o.Orientation=0.504344,0.504344,0.495618,-0.495618
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-23207.776219,-2334.442133,41788.047756)
o.Scale=8.557520
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-23139.029425,-2343.816234,31662.706728)
o.Scale=8.557520
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName3","Adoquinpulsador",-23317.173097,-2515.609363,21875.439149)
o.Scale=8.557520
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName5","Varilla",-31513.929000,1336.273000,62456.409000)
o.Scale=2.625266
o.Orientation=0.500000,0.500000,0.500000,-0.500000


o=Bladex.CreateEntity("NoName6","LamparaAurelio",-31542.615000,1996.494000,62173.858000,"Physic")
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.180000,(234,123,0)) ]       # precision 0.3 -> 0.18
