##///
##||| Ice_M11/objs.PY TITANIUM
##||| Change list:
##||| * Enabled sparks for stuff that was missing it
##||| * Removed selectiondata for stuff where it doesn't make sense
##||| * Shadowpass
##\\\ 


import Reference
import Bladex
import Sparks
import pocimac
import time
import Bladex
import Breakings
import OnOff
import AuxFuncs

o=Bladex.CreateEntity("NoName4","Monjespada",9351.773000,-9542.042000, -9092.173000,Reference.ObjType("Monjespada"))

o.Scale=1.661078
o.Orientation=0.714371,0.699745,-0.004024,0.003941
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Monjecaliz",7387.265000,-9542.042000, -9092.173000,Reference.ObjType("Monjecaliz"))

o.Scale=1.644632
o.Orientation=0.704386,0.709727,0.007934,-0.007994
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Monjecaliz",11397.485000,-9542.042000, -9092.173000,Reference.ObjType("Monjecaliz"))

o.Scale=1.644632
o.Orientation=0.704386,0.709727,0.007934,-0.007994
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Monjecaliz",32390.795000,-9542.042000, -9092.173000,Reference.ObjType("Monjecaliz"))

o.Scale=1.661078
o.Orientation=0.704386,0.709727,0.007934,-0.007994
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Monjespada",30326.619000,-9542.042000, -9092.173000,Reference.ObjType("Monjespada"))

o.Scale=1.644632
o.Orientation=0.714371,0.699745,-0.004024,0.003941
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Monjespada",26389.980000,-9542.042000, -9092.173000,Reference.ObjType("Monjespada"))

o.Scale=1.644632
o.Orientation=0.714371,0.699745,-0.004024,0.003941
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Monjecaliz",28347.130000,-9542.042000, -9092.173000,Reference.ObjType("Monjecaliz"))

o.Scale=1.694466
o.Orientation=0.704386,0.709727,0.007934,-0.007994
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Monjespada",34396.981000,-9542.042000, -9092.173000,Reference.ObjType("Monjespada"))

o.Scale=1.677689
o.Orientation=0.714371,0.699745,-0.004024,0.003941
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Monjespada",5357.124000,-9542.042000, -9092.173000,Reference.ObjType("Monjespada"))

o.Scale=1.612226
o.Orientation=0.714371,0.699745,-0.004024,0.003941
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Monjecaliz",3350.963000,-9542.042000, -9092.173000,Reference.ObjType("Monjecaliz"))

o.Scale=1.677689
o.Orientation=0.704386,0.709727,0.007934,-0.007994
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName16","Gancho",81586.230000,-2458.426000,-21708.40900,Reference.ObjType("Gancho"))

o.Scale=1.321291
o.Orientation=0.473867,0.504367,-0.494269,0.526082



o=Bladex.CreateEntity("NoName18","Monjespada",46654.175000,-13892.237000,59160.04100,Reference.ObjType("Monjespada"))

o.Scale=2.283884
o.Orientation=0.705385,0.691539,0.111099,-0.108918
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName19","Monjecaliz",43127.177000,-13987.625000,59169.91700,Reference.ObjType("Monjecaliz"))

o.Scale=2.376619
o.Orientation=0.701451,0.695180,-0.111608,0.110610
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName20","Lampcolg",44794.059000,-16328.538000,52737.33300,Reference.ObjType("Lampcolg"))

o.Scale=2.047099
o.Orientation=0.698805,0.714999,0.014781,-0.015123
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.401247,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("bra1","Braseroarana",30777.699000,-321.593000,54431.54800,Reference.ObjType("Braseroarana"))

o.Scale=1.000000
o.Orientation=0.710494,0.703578,-0.009453,0.009361
o.FiresIntensity=[ 3 ]
o.Lights=[ (14.321917,0.031250,(255,160,55)) ]



o=Bladex.CreateEntity("bra2","Braseroarana",6997.560000,-315.316000,54295.51600,Reference.ObjType("Braseroarana"))

o.Scale=1.000000
o.Orientation=0.709345,0.704818,-0.005576,0.005541
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.000000,0.031250,(255,196,128)) ]


"""
o=Bladex.CreateEntity("bra3","Braseroarana",1077.142000,-8463.218000,-12114.06300,Reference.ObjType("Braseroarana"))

o.Scale=1.220190
o.Orientation=0.501211,0.502808,-0.497189,0.498773
o.FiresIntensity=[ 3 ]
o.Lights=[ (2.925246,0.031250,(255,159,53)) ]



o=Bladex.CreateEntity("bra4","Braseroarana",37627.946000,-8447.335000,-12094.45900,Reference.ObjType("Braseroarana"))

o.Scale=1.000000
o.Orientation=0.497166,0.493135,0.506850,-0.502740
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149622,0.031250,(255,172,81)) ]
"""


o=Bladex.CreateEntity("NoName30","Lampared",37753.375000,4253.815000,-2435.70100,Reference.ObjType("Lampared"))

o.Scale=1.257163
o.Orientation=0.705778,0.708359,0.007269,-0.007296
o.FiresIntensity=[ 3 ]
o.Lights=[ (16.942511,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp1","Antorchaenpared",36823.639000,7102.525000,35627.14200,Reference.ObjType("Antorchaenpared"))

o.Scale=1.196147
o.Orientation=0.007380,0.043072,0.709812,-0.703034
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.642778,0.031250,(255,196,128)) ]





o=Bladex.CreateEntity("NoName38","Columnaestrecha",41545.435000,10246.904000,43117.42800,Reference.ObjType("Columnaestrecha"))

o.Scale=1.000000
o.Orientation=0.512251,0.505778,0.493920,-0.487679
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName39","Columnaestrecha",41543.491000,10213.208000,37862.68800,Reference.ObjType("Columnaestrecha"))

o.Scale=1.000000
o.Orientation=0.493069,0.497049,0.502855,-0.506914
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName40","Velon",13662.469000,4715.196000,13130.15000,Reference.ObjType("Velon"))

o.Scale=1.871744
o.Orientation=0.499481,0.515868,-0.484131,0.500016
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName42","Lampcolg",61120.434000,-5452.532000,18357.82300,Reference.ObjType("Lampcolg"))

o.Scale=1.295256
o.Orientation=0.709354,0.704364,0.018618,-0.018487
o.FiresIntensity=[ 3 ]
o.Lights=[ (18.000000,0.209521,(255,193,125)) ]



o=Bladex.CreateEntity("NoName43","Lamparatecho",26759.790000,-14584.391000,53518.85300,Reference.ObjType("Lamparatecho"))

o.Scale=2.216716
o.Orientation=0.710081,0.704106,0.003163,-0.003136
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.015032,(255,149,32)) ]



o=Bladex.CreateEntity("NoName44","Lamparatecho",11641.537000,-15380.208000,53672.99900,Reference.ObjType("Lamparatecho"))

o.Scale=2.573537
o.Orientation=0.706779,0.707260,0.011106,-0.011114
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.003004,(255,183,102)) ]



o=Bladex.CreateEntity("NoName45","Lampared",19558.172000,-3613.270000,30840.49500,Reference.ObjType("Lampared"))

o.Scale=1.184304
o.Orientation=0.007026,0.006979,-0.709775,0.704359
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]





o=Bladex.CreateEntity("NoName47","Monjespada",47080.521000,8333.334000,17551.61300,Reference.ObjType("Monjespada"))

o.Scale=1.967222
o.Orientation=0.314347,0.308246,0.641081,-0.628638
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName48","Monjespada",47440.237000,8202.797000,22618.87400,Reference.ObjType("Monjespada"))

o.Scale=2.173037
o.Orientation=0.645586,0.643782,0.290597,-0.290373
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName49","Lamparatecho",18908.635000,-17184.025000,-11964.78400,Reference.ObjType("Lamparatecho"))

o.Scale=1.763268
o.Orientation=0.533788,0.497541,-0.500173,0.466209
o.FiresIntensity=[ 3 ]
o.Lights=[ (18.679117,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName51","Lampared",29273.043000,-1480.900000,-8632.85400,Reference.ObjType("Lampared"))

o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149637,0.300000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName52","PeleleNevado",76628.038000,-2409.269000,78765.98800,Reference.ObjType("PeleleNevado"))

o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)


o=Bladex.CreateEntity("antp2","Antorchaenpared",40326.818000,-3666.154000,39692.00300,Reference.ObjType("Antorchaenpared"))

o.Scale=1.196147
o.Orientation=0.063070,0.046669,-0.698749,0.711052
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp3","Antorchaenpared",77014.019000,-6720.728000,-28543.69400,Reference.ObjType("Antorchaenpared"))

o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName58","Lampcolg",70199.386000,-8383.251000,-24185.25200,Reference.ObjType("Lampcolg"))

o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (25,0.331250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName61","Lampared",99577.632000,-7602.059000,25136.59500,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,156,47)) ]



o=Bladex.CreateEntity("NoName62","Lampared",99485.371000,-7542.986000,46346.65200,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,160,55)) ]




o=Bladex.CreateEntity("cand1","Candelabro",43276.809000,-9798.611000,58588.92200,Reference.ObjType("Candelabro"))

o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (0.200000,0.031250,(255,196,128)) ]  # now visible lights
AuxFuncs.GetSpot(o).Visible=0                   #
AuxFuncs.GetSpot(o).CastShadows=0               #   -LeadHead



o=Bladex.CreateEntity("cand2","Candelabro",46372.755000,-9757.552000,58188.54100,Reference.ObjType("Candelabro"))

o.Scale=1.661078
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 3 ]
o.Lights=[ (0.300000,0.031250,(255,196,128)) ]  # now visible lights
AuxFuncs.GetSpot(o).Visible=0                   #
AuxFuncs.GetSpot(o).CastShadows=0               #   -LeadHead




o=Bladex.CreateEntity("antp5","Antorchaenpared",80628.489000,-1922.796000,29567.29800,Reference.ObjType("Antorchaenpared"))

o.Scale=1.000000
o.Orientation=0.517145,0.435338,0.482246,-0.557208
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,176,89)) ]



o=Bladex.CreateEntity("antp6","Antorchaenpared",99171.653000,-6992.157000,-19953.39700,Reference.ObjType("Antorchaenpared"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp7","Antorchaenpared",28040.619000,-2790.708000,90322.71900,Reference.ObjType("Antorchaenpared"))

o.Scale=1.564811
o.Orientation=0.415627,0.482246,-0.572062,0.517145
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName74","Lamparatecho",18918.925000,-16234.401000,-36662.47700,Reference.ObjType("Lamparatecho"))

o.Scale=1.661078
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (17.000000,0.600000,(255,151,36)) ]



o=Bladex.CreateEntity("NoName75","Lamparatecho",18502.320000,-16377.101000,-31372.50400,Reference.ObjType("Lamparatecho"))

o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 11 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName86","Semipuxero",25119.292000,9111.669000,5674.55300,Reference.ObjType("Semipuxero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (4.000000,0.011778,(171,121,95)) ]



o=Bladex.CreateEntity("NoName87","Semipuxero",12867.552000,9104.368000,5655.05200,Reference.ObjType("Semipuxero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (4.000000,0.031250,(250,185,78)) ]



o=Bladex.CreateEntity("NoName88","Semipuxero",24896.080000,7636.800000,-2344.13900,Reference.ObjType("Semipuxero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (14.635594,0.075207,(255,196,128)) ]



o=Bladex.CreateEntity("antp8","Antorchaenpared",-2759.616000,-3891.203000,31437.43400,Reference.ObjType("Antorchaenpared"))

o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName95","Semipuxero",18911.048000,-1166.115000,-14962.67600,Reference.ObjType("Semipuxero"))

o.Scale=1.000000
o.Orientation=0.012342,0.012341,0.706999,-0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (13.000000,0.100000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName96","Roca2",66965.456000,-498.892000,-16623.00700,Reference.ObjType("Roca2"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName97","Roca2",89859.744000,-557.481000,-16255.01300,Reference.ObjType("Roca2"))

o.Scale=1.295256
o.Orientation=0.635860,0.771360,0.016651,-0.020199
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName98","Lamparatecho",-7255.723000,-7981.683000,22318.64800,Reference.ObjType("Lamparatecho"))

o.Scale=1.596263
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (22.000000,0.031250,(255,177,91)) ]



o=Bladex.CreateEntity("NoName99","Pendon3",18491.044000,-13567.816000,-41793.34900,Reference.ObjType("Pendon3"))

o.Scale=1.763268
o.Orientation=0.000000,0.000000,0.008727,-0.999962



o=Bladex.CreateEntity("NoName100","Pendon3",11329.622000,-9174.528000,18613.75000,Reference.ObjType("Pendon3"))

o.Scale=1.763268
o.Orientation=0.000000,0.000000,0.000000,1.000000



o=Bladex.CreateEntity("NoName101","Pendon3",25824.058000,-9336.141000,18526.46200,Reference.ObjType("Pendon3"))

o.Scale=1.711410
o.Orientation=0.008693,0.000761,-0.000000,-0.999962



o=Bladex.CreateEntity("NoName102","Cuerda",26762.057000,-16076.729000,53526.99600,Reference.ObjType("Cuerda"))

o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName104","Cuerda",61129.443000,-6985.007000,18367.80300,Reference.ObjType("Cuerda"))

o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName105","Lampcolg",78519.624000,-5936.975000,16945.16000,Reference.ObjType("Lampcolg"))

o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (17.000000,0.325000,(254,237,158)) ]     # precision 0.4 -> 0.325



o=Bladex.CreateEntity("NoName106","Cuerda",78495.492000,-7616.791000,16959.86200,Reference.ObjType("Cuerda"))

o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName107","Lampcolg",88209.891000,-7954.362000,-28233.66900,Reference.ObjType("Lampcolg"))

o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.131250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName108","Cuerda",70192.158000,-9945.927000,-24194.61600,Reference.ObjType("Cuerda"))

o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName109","Cuerda",18516.077000,-20184.982000,-31356.96900,Reference.ObjType("Cuerda"))

o.Scale=3.573847
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName113","Skeleton_Optimiced",-6193.634000,9394.129000,31422.68500,Reference.ObjType("Skeleton_Optimiced"))

o.Scale=1.295256
o.Orientation=0.999848,0.017452,0.000000,0.000000



"""
o=Bladex.CreateEntity("NoName122","Blason3",24534.937000,7320.618000,43982.56200,Reference.ObjType("Blason3"))

o.Scale=0.878663
o.Orientation=0.707107,0.707107,0.000000,0.000000
"""



o=Bladex.CreateEntity("NoName126","Cuerda",76409.868000,-7042.680000,-1505.47900,Reference.ObjType("Cuerda"))

o.Scale=2.238882
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName127","GargolaFernando",35585.447000,-20116.040000,30044.48200,Reference.ObjType("GargolaFernando"))

o.Scale=1.459527
o.Orientation=0.000000,0.000000,0.688355,-0.725374



o=Bladex.CreateEntity("NoName128","GargolaFernando",24207.956000,-20539.535000,44077.91200,Reference.ObjType("GargolaFernando"))

o.Scale=1.711410
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName129","GargolaFernando",13507.027000,-20679.733000,44024.09500,Reference.ObjType("GargolaFernando"))

o.Scale=1.909366
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName130","GargolaFernando",31610.143000,-9369.284000,101350.69700,Reference.ObjType("GargolaFernando"))

o.Scale=2.130220
o.Orientation=0.486740,0.486740,-0.512917,0.512917



o=Bladex.CreateEntity("NoName131","GargolaFernando",77293.398000,-11066.426000,73974.97100,Reference.ObjType("GargolaFernando"))

o.Scale=1.474123
o.Orientation=0.043168,0.043168,-0.705788,0.705788



o=Bladex.CreateEntity("NoName132","GargolaFernando",69096.499000,-11083.545000,73742.28300,Reference.ObjType("GargolaFernando"))

o.Scale=1.459527
o.Orientation=0.030844,0.030844,-0.706434,0.706434



o=Bladex.CreateEntity("NoName133","GargolaFernando",66824.466000,-11082.149000,71646.82100,Reference.ObjType("GargolaFernando"))

o.Scale=1.644632
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName134","GargolaFernando",-29354.602000,-19650.859000,70968.31800,Reference.ObjType("GargolaFernando"))

o.Scale=3.756148
o.Orientation=0.110616,0.110616,0.698401,-0.698401



o=Bladex.CreateEntity("NoName135","GargolaFernando",15082.487000,-6632.515000,136127.25500,Reference.ObjType("GargolaFernando"))

o.Scale=2.306723
o.Orientation=0.504344,0.504344,-0.495618,0.495618



o=Bladex.CreateEntity("NoName136","GargolaFernando",14483.757000,-7671.527000,118880.77800,Reference.ObjType("GargolaFernando"))

o.Scale=1.580459
o.Orientation=0.468543,0.468543,-0.529592,0.529592



o=Bladex.CreateEntity("NoName137","GargolaFernando",65069.903000,-4213.131000,-12207.73900,Reference.ObjType("GargolaFernando"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName138","Lampared",95471.420000,-6878.196000,8095.56200,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,183,102)) ]



o=Bladex.CreateEntity("NoName139","Lampared",67319.445000,-6697.916000,6071.51500,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.003693,0.003703,0.707097,-0.707097
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("mesa2","Mesa",25861.062000,-8527.988000,53912.32700,Reference.ObjType("Mesa"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("mesa1","Mesa",28677.762000,-8531.297000,53946.05900,Reference.ObjType("Mesa"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("meson1","Meson",-7145.529000,2240.834000,41609.09200,Reference.ObjType("Meson"))

o.Scale=0.887449
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName150","Candelpeque",-7334.612000,1589.707000,40752.92600,Reference.ObjType("Candelpeque"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 11 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName151","Tapiz3",-12257.660000,-809.346000,36695.98700,Reference.ObjType("Tapiz3"))

o.Scale=1.763268
o.Orientation=0.512917,0.512917,-0.486740,0.486740



o=Bladex.CreateEntity("NoName153","Tapiz",-7243.772000,-1457.584000,44761.42300,Reference.ObjType("Tapiz"))

o.Scale=1.115668
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName154","Taburete",-8551.346000,2421.550000,42677.87100,Reference.ObjType("Taburete"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName155","Taburete",-8520.575000,2439.923000,40806.93500,Reference.ObjType("Taburete"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



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


o=Bladex.CreateEntity("rast1","Rastrillo",-18627.012000,-1943.293000,57806.68700,Reference.ObjType("Rastrillo"))

o.Scale=1.172579
o.Orientation=0.719340,-0.694658,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)        # Add



o=Bladex.CreateEntity("NoName164","Lampcolg",76417.626000,-4880.519000,-1499.01800,Reference.ObjType("Lampcolg"))

o.Scale=1.184304
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.000000,0.200000,(255,154,43)) ]  # precision 0.7 -> 0.2



o=Bladex.CreateEntity("NoName165","Lampared",4244.903000,-1710.389000,-8485.78600,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.149651,0.200000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName168","Lampared",30817.517000,-10187.595000,-24728.17800,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.012342,0.012341,-0.706999,0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("lamp1","Antorchaenpared",46227.492000,-3276.597000,25397.39500,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
o.FiresIntensity=[ 3 ]
o.Lights=[ (12.0,0.200000,(255,145,23)) ]  # precision 0.5 -> 0.2 , intens 13.22 -> 12.0



o=Bladex.CreateEntity("NoName173","Lampared",73081.722000,-3898.882000,61278.91100,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.225097,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName184","Cuerda",-7264.384000,-9642.281000,22323.70200,Reference.ObjType("Cuerda"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName185","Cuerda",-7262.890000,-12104.491000,22328.18000,Reference.ObjType("Cuerda"))

o.Scale=2.329790
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName186","Lampared",88606.174000,-11568.073000,62513.37300,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491198,0.491198
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.253340,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName187","Lampared",88601.606000,-4894.892000,55586.30200,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.512917,0.512917,-0.486740,0.486740
o.FiresIntensity=[ 3 ]
o.Lights=[ (6.081397,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antp9","Antorchaenpared",87529.877000,-1861.412000,4035.72900,Reference.ObjType("Antorchaenpared"))

o.Scale=1.000000
o.Orientation=0.486740,0.486740,0.512917,-0.512917
o.FiresIntensity=[ 3 ]
o.Lights=[ (16.000000,1.800000,(255,196,128)) ]



o=Bladex.CreateEntity("NoName195","Skeleton_Optimiced",40945.887000,5856.769000,3837.72100,Reference.ObjType("Skeleton_Optimiced"))

o.Scale=1.115668
o.Orientation=0.999848,0.017452,0.000000,0.000000



o=Bladex.CreateEntity("NoName196","Skeleton_Optimiced",41105.645000,5830.270000,8847.20400,Reference.ObjType("Skeleton_Optimiced"))

o.Scale=1.126825
o.Orientation=0.031370,-0.001421,0.998993,-0.032040



o=Bladex.CreateEntity("NoName198","Varillaancha",44758.841000,-17093.184000,52705.56900,Reference.ObjType("Varillaancha"))

o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName0","Roca1Aurelio",12460.735000,10471.325000,26081.65600,Reference.ObjType("Roca1Aurelio"))

o.Scale=1.000000
o.Orientation=0.643440,0.643440,0.293232,-0.293232
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Roca1Aurelio",26848.966000,10670.622000,25223.86000,Reference.ObjType("Roca1Aurelio"))

o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Roca1Aurelio",24947.191000,2686.884000,26268.30200,Reference.ObjType("Roca1Aurelio"))

o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Roca1Aurelio",9171.728000,10565.428000,44968.79100,Reference.ObjType("Roca1Aurelio"))

o.Scale=1.000000
o.Orientation=0.668583,0.668583,0.230211,-0.230211
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Columnaestrecha",13566.764000,9655.122000,27176.96800,Reference.ObjType("Columnaestrecha"))

o.Scale=1.612226
o.Orientation=0.641514,0.725100,0.187524,0.165907



o=Bladex.CreateEntity("NoName12","Columnaestrecha",20941.546000,9980.168000,27916.73600,Reference.ObjType("Columnaestrecha"))

o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName14","Roca1Aurelio",32720.199000,7511.212000,23071.51000,Reference.ObjType("Roca1Aurelio"))

o.Scale=1.000000
o.Orientation=0.353553,0.353553,0.612372,-0.612373
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName0","Lampcolg",18645.782000,-14257.400000,21751.81000,Reference.ObjType("Lampcolg"))

o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,137,6)) ]



o=Bladex.CreateEntity("NoName1","Varilla",18601.561000,-16416.733000,21752.93800,Reference.ObjType("Varilla"))

o.Scale=1.000000
o.Orientation=0.491198,0.491198,-0.508650,-0.508650



o=Bladex.CreateEntity("NoName2","Lampared",11786.905000,-9992.735000,-25228.73500,Reference.ObjType("Lampared"))

o.Scale=1.000000
o.Orientation=0.012342,0.012341,0.706999,-0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,165,66)) ]



o=Bladex.CreateEntity("NoName1","Cuerda",18841.421000,-19122.294000,-11964.19600,Reference.ObjType("Cuerda"))

o.Scale=1.082857
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName0","Cuerda",18929.935000,-21304.843000,-36646.07900,Reference.ObjType("Cuerda"))

o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName1","Cuerda",18929.935000,-18654.843000,-36646.07900,Reference.ObjType("Cuerda"))

o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("antp10","Antorcha",20900.482000,10908.661000,-15762.35900,Reference.ObjType("Antorcha"))

o.Scale=1.000000
o.Orientation=0.999391,0.034899,0.000000,0.000000
o.FiresIntensity=[ 47 ]
o.Lights=[ (0.000000,0.031250,(255,147,28)) ]



o=Bladex.CreateEntity("NoName1","Gargola",36041.545000,-16508.716000,37051.357000,Reference.ObjType("Gargola"))

o.Scale=3.203323
o.Orientation=0.473147,0.473147,0.525483,-0.525483



o=Bladex.CreateEntity("NoName2","Gargola",-68364.312000,10442.585000,41374.742000,Reference.ObjType("Gargola"))

o.Scale=5.537023
o.Orientation=0.383874,0.289286,-0.633913,0.605895



o=Bladex.CreateEntity("NoName3","Gargola",-67422.650000,2638.176000,91441.019000,Reference.ObjType("Gargola"))

o.Scale=6.055760
o.Orientation=0.687569,0.687569,-0.165071,0.165071



o=Bladex.CreateEntity("NoName4","Gargola",5791.407000,-21590.573000,75889.368000,Reference.ObjType("Gargola"))

o.Scale=4.913826
o.Orientation=0.517145,0.517145,0.482246,-0.482246



o=Bladex.CreateEntity("NoName1","Piedra_09",39440.287000,10185.039000,-10041.607000,Reference.ObjType("Piedra_09"))

o.Scale=0.614119
o.Orientation=0.838026,-0.070242,0.487911,0.233926
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Piedra_08",39938.218000,10233.496000,-10346.238000,Reference.ObjType("Piedra_08"))

o.Scale=0.400344
o.Orientation=0.737925,0.654760,-0.135781,-0.091206
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Piedra_08",42080.836000,10217.281000,-15161.331000,Reference.ObjType("Piedra_08"))

o.Scale=0.412475
o.Orientation=0.503737,-0.311211,-0.568165,-0.571476
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Piedra_01",42032.293000,7878.537000,-9366.744000,Reference.ObjType("Piedra_01"))

o.Scale=0.626463
o.Orientation=0.064310,-0.907792,0.389180,-0.142540
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Piedra_03",41240.905000,7904.631000,-9004.997000,Reference.ObjType("Piedra_03"))

o.Scale=0.756836
o.Orientation=0.650870,0.754143,-0.041130,-0.077104
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Piedra_03",43472.262000,7869.760000,-8178.348000,Reference.ObjType("Piedra_03"))

o.Scale=1.000000
o.Orientation=0.757654,-0.649838,-0.016274,-0.058357
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Piedra_03",46505.137000,6378.835000,-3553.161000,Reference.ObjType("Piedra_03"))

o.Scale=1.000000
o.Orientation=0.638005,0.764985,-0.051933,-0.071066
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Piedra_03",47088.700000,6396.470000,-2471.642000,Reference.ObjType("Piedra_03"))

o.Scale=0.779768
o.Orientation=0.629766,0.771274,-0.054076,-0.074881
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Piedra_03",43195.775000,3148.128000,5973.518000,Reference.ObjType("Piedra_03"))

o.Scale=0.734577
o.Orientation=0.626156,0.776029,-0.023149,-0.071917
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Piedra_03",44444.858000,3172.819000,4409.355000,Reference.ObjType("Piedra_03"))

o.Scale=0.534261
o.Orientation=0.680728,0.726759,-0.003191,-0.091767
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Piedra_03",44044.000000,3168.812000,4889.425000,Reference.ObjType("Piedra_03"))

o.Scale=0.632728
o.Orientation=0.580536,0.554098,0.400097,-0.442578
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Tabla_rota",45368.723000,3180.421000,3230.493000,Reference.ObjType("Tabla_rota"))

o.Scale=1.834864
o.Orientation=0.382688,0.383962,-0.592596,0.595779
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Piedra_08",43283.847000,6395.996000,-98.012000,Reference.ObjType("Piedra_08"))

o.Scale=0.392456
o.Orientation=0.229941,-0.843134,0.103388,0.474935
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName16","Piedra_02",43337.990000,6425.429000,-2164.373000,Reference.ObjType("Piedra_02"))

o.Scale=0.408391
o.Orientation=0.681394,-0.137667,-0.603692,-0.390265
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("lamparaenciende","Lamparatecho",31380.406000,5423.344000,40437.497000,Reference.ObjType("Lamparatecho"))

o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
OnOff.AddLightData("lamparaenciende",25,0.1,(255,155,45))
o.Lights=[ (0,0,(255,155,45)) ]



o=Bladex.CreateEntity("antp11","Antorchaenpared",37953.094860,8296.850435,23945.574580,Reference.ObjType("Antorchaenpared"))

o.Scale=1.00
o.Orientation=0.454519,0.525483,-0.541675,0.473147
o.FiresIntensity=[ 20 ]
o.Lights=[ (0.000000,0.031250,(255,142,17)) ]



o=Bladex.CreateEntity("NoName2","Piedra_04",29895.204000,10848.005000,37922.793000,Reference.ObjType("Piedra_04"))

o.Scale=0.626463
o.Orientation=0.487832,0.367607,0.442270,-0.656721
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Piedra_03",29672.981000,10936.438000,36897.495000,Reference.ObjType("Piedra_03"))

o.Scale=0.478871
o.Orientation=0.656851,0.744354,-0.002488,-0.120322
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Piedra_02",29901.927000,10894.081000,34457.305000,Reference.ObjType("Piedra_02"))

o.Scale=0.671653
o.Orientation=0.887171,-0.428683,-0.141364,-0.095786
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Piedra_06",30800.882000,10942.567000,35733.591000,Reference.ObjType("Piedra_06"))

o.Scale=0.460185
o.Orientation=0.508155,0.782730,-0.222210,0.282372
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Piedra_01",34856.391000,10914.847000,41465.476000,Reference.ObjType("Piedra_01"))

o.Scale=0.705914
o.Orientation=0.819906,-0.067501,-0.558863,0.104256
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Piedra_01",36066.107000,10913.965000,40937.095000,Reference.ObjType("Piedra_01"))

o.Scale=1.000000
o.Orientation=0.956023,-0.164803,0.080757,0.228775
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Piedra_01",36190.818000,10829.846000,40124.565000,Reference.ObjType("Piedra_01"))

o.Scale=1.000000
o.Orientation=0.083949,-0.814015,0.568076,0.087302
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Piedra_08",37974.471000,11071.546000,39606.350000,Reference.ObjType("Piedra_08"))

o.Scale=1.000000
o.Orientation=0.584076,-0.686819,0.268481,0.339195
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Piedra_08",39439.386000,11160.714000,41375.980000,Reference.ObjType("Piedra_08"))

o.Scale=0.614119
o.Orientation=0.710353,0.685870,-0.144326,-0.064430
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Piedra_08",38881.743000,10902.211000,42853.803000,Reference.ObjType("Piedra_08"))

o.Scale=0.685153
o.Orientation=0.645648,0.706853,-0.151228,-0.246226
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName15","Femur",39636.241000,11226.066000,39103.324000,Reference.ObjType("Femur"))

o.Scale=1.184304
o.Orientation=0.010025,0.194699,-0.023848,0.980522
o.CastShadows=0


o=Bladex.CreateEntity("NoName16","Femur",37787.245000,11192.903000,40841.801000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.142110,0.079887,-0.985986,-0.035410
o.CastShadows=0


o=Bladex.CreateEntity("NoName17","Femur",37011.130000,10944.127000,40535.155000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.651146,0.034637,-0.755697,-0.061083
o.CastShadows=0


o=Bladex.CreateEntity("NoName18","Skull",40722.644000,11151.897000,40398.139000,Reference.ObjType("Skull"))

o.Scale=1.000000
o.Orientation=0.585854,-0.324341,-0.558283,0.489794
o.CastShadows=0


o=Bladex.CreateEntity("NoName19","Skull",36889.152000,10900.708000,39566.738000,Reference.ObjType("Skull"))

o.Scale=1.000000
o.Orientation=0.861572,0.487122,-0.135275,0.045905
o.CastShadows=0


o=Bladex.CreateEntity("NoName20","Femur",39125.919000,10945.045000,38079.038000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.996664,-0.025645,-0.022900,-0.074014
o.CastShadows=0


o=Bladex.CreateEntity("NoName21","Femur",38596.165000,11192.311000,38446.659000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.388402,0.012550,-0.921135,-0.022298
o.CastShadows=0


o=Bladex.CreateEntity("NoName22","Tabla_rota",38717.772000,11207.508000,38974.923000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.655300,0.661789,0.256793,-0.258214
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName23","Tabla_rota",39277.165000,11209.290000,39551.584000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName24","Tabla_rota",34855.992000,10100.748000,40153.335000,Reference.ObjType("Tabla_rota"))

o.Scale=1.533978
o.Orientation=0.408625,0.407772,0.578136,0.576634
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName25","Tabla_rota",37637.055000,9993.316000,28352.547000,Reference.ObjType("Tabla_rota"))

o.Scale=1.798710
o.Orientation=0.701890,0.328140,0.014108,0.632041
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName26","Piedra_09",37151.404000,10874.220000,29671.249000,Reference.ObjType("Piedra_09"))

o.Scale=0.658419
o.Orientation=0.836907,-0.525437,0.132074,0.077838
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName28","Piedra_01",38764.895000,11173.447000,30060.318000,Reference.ObjType("Piedra_01"))

o.Scale=1.000000
o.Orientation=0.928314,-0.254330,-0.204037,0.178658
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName29","Piedra_01",38806.279000,9896.195000,27190.445000,Reference.ObjType("Piedra_01"))

o.Scale=1.416603
o.Orientation=0.952096,-0.200748,0.014967,0.230196
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName30","Piedra_01",38904.614000,9879.553000,25573.893000,Reference.ObjType("Piedra_01"))

o.Scale=1.000000
o.Orientation=0.200225,-0.716910,-0.135430,0.653918
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName31","Tabla_xl",34613.328000,10043.143000,38830.357000,Reference.ObjType("Tabla_xl"))

o.Scale=1.430769
o.Orientation=0.594077,0.609917,-0.382959,-0.358352
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName32","Piedra_01",37432.739000,10854.848000,31477.225000,Reference.ObjType("Piedra_01"))

o.Scale=1.000000
o.Orientation=0.028455,-0.981410,-0.080413,0.171923
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName33","Costilla",42258.430000,10990.705000,32225.714000,Reference.ObjType("Costilla"))

o.Scale=1.000000
o.Orientation=0.562790,0.275572,-0.236600,-0.742528



o=Bladex.CreateEntity("NoName34","Skull",41948.770000,10906.065000,31428.175000,Reference.ObjType("Skull"))

o.Scale=1.000000
o.Orientation=0.842358,0.471593,0.253004,-0.063420



o=Bladex.CreateEntity("NoName35","Femur",42245.559000,10944.792000,30797.570000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.995404,-0.022242,0.032809,-0.087181
o.CastShadows=0


o=Bladex.CreateEntity("NoName36","Femur",42608.044000,10694.097000,30674.956000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.842611,-0.013681,-0.538336,-0.003697
o.CastShadows=0


o=Bladex.CreateEntity("NoName37","Femur",42682.420000,10728.284000,31515.403000,Reference.ObjType("Femur"))

o.Scale=1.184304
o.Orientation=0.068789,-0.023993,0.018661,-0.997168
o.CastShadows=0




o=Bladex.CreateEntity("NoName39","Femur",36200.494000,10979.965000,37870.822000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.007918,0.942077,-0.038027,0.333139



o=Bladex.CreateEntity("NoName41","Piedra_03",42882.466000,9846.411000,20364.060000,Reference.ObjType("Piedra_03"))
o.Scale=1.334504
o.Orientation=0.641255,0.762424,-0.054364,-0.067428
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName42","Piedra_03",42309.537000,9876.368000,19783.178000,Reference.ObjType("Piedra_03"))
o.Scale=1.000000
o.Orientation=0.509059,0.514529,0.399413,-0.562662
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName43","Piedra_03",44533.766000,10130.006000,21534.647000,Reference.ObjType("Piedra_03"))
o.Scale=1.000000
o.Orientation=0.657604,0.749527,-0.049722,-0.057400
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName44","Femur",49823.916000,8437.806000,19512.579000,Reference.ObjType("Femur"))
o.Scale=1.082857
o.Orientation=0.988108,-0.013349,-0.152977,0.007892
o.CastShadows=0


o=Bladex.CreateEntity("NoName45","Femur",49662.412000,8475.828000,19657.661000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.007424,0.071767,0.017120,-0.997247
o.CastShadows=0


o=Bladex.CreateEntity("NoName0","Piedra_01",6118.523000,10939.784000,43222.056000,Reference.ObjType("Piedra_01"))
o.Scale=0.727304
o.Orientation=0.580596,0.033825,0.740905,0.335892
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)



o=Bladex.CreateEntity("NoName2","Piedra_01",4543.086000,10853.543000,39950.390000,Reference.ObjType("Piedra_01"))
o.Scale=0.584313
o.Orientation=0.283617,0.776721,-0.508730,-0.239708
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)




o=Bladex.CreateEntity("NoName7","Piedra_09",4079.773000,10892.111000,33824.705000,Reference.ObjType("Piedra_09"))
o.Scale=0.483659
o.Orientation=0.403124,0.396452,0.551818,-0.613036
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName8","Piedra_09",6428.690000,10878.554000,31144.584000,Reference.ObjType("Piedra_09"))
o.Scale=0.396380
o.Orientation=0.288820,0.849225,-0.014680,-0.441797
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName9","Tabla_rota",3948.506000,10930.245000,43006.798000,Reference.ObjType("Tabla_rota"))

o.Scale=1.763268
o.Orientation=0.211649,0.211343,0.673992,-0.675480



o=Bladex.CreateEntity("NoName10","Tabla_rota",3882.468000,10146.131000,44065.151000,Reference.ObjType("Tabla_rota"))

o.Scale=1.416603
o.Orientation=0.558511,0.546740,0.443466,0.438725



o=Bladex.CreateEntity("NoName11","Piedra_01",7681.104000,10913.721000,37775.852000,Reference.ObjType("Piedra_01"))
o.Scale=0.344836
o.Orientation=0.471764,-0.697441,0.256297,0.474686
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName12","Piedra_01",9905.808000,10816.914000,29031.764000,Reference.ObjType("Piedra_01"))
o.Scale=1.000000
o.Orientation=0.268290,-0.941415,-0.093500,0.181701
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)



o=Bladex.CreateEntity("NoName1","Piedra_01",-1850.096000,11185.034000,39426.638000,Reference.ObjType("Piedra_01"))
o.Scale=0.678370
o.Orientation=0.785911,-0.340660,-0.514005,0.045766
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName2","Piedra_01",-3577.577000,10926.629000,38195.466000,Reference.ObjType("Piedra_01"))
o.Scale=0.795442
o.Orientation=0.983486,-0.092047,-0.071258,0.138582
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)
o=Bladex.CreateEntity("NoName3","Piedra_01",857.893000,10910.749000,39422.421000,Reference.ObjType("Piedra_01"))
o.Scale=1.000000
o.Orientation=0.986832,-0.085500,-0.049253,0.128163
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Skull",-178.693000,11146.864000,38925.194000,Reference.ObjType("Skull"))
o.Scale=1.000000
o.Orientation=0.359356,-0.450866,0.667130,-0.471721
o.CastShadows=0


o=Bladex.CreateEntity("NoName6","Skull",-4526.682000,10899.748000,38829.239000,Reference.ObjType("Skull"))
o.Scale=1.000000
o.Orientation=0.098047,0.018727,-0.863327,0.494674
o.CastShadows=0


o=Bladex.CreateEntity("NoName7","Tabla_rota",645.932000,10948.945000,38232.724000,Reference.ObjType("Tabla_rota"))

o.Scale=1.269735
o.Orientation=0.673723,0.680595,0.202387,-0.204761



o=Bladex.CreateEntity("NoName8","Femur",-1680.264000,11194.818000,38893.822000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.986684,-0.035429,0.130761,-0.090001
o.CastShadows=0


o=Bladex.CreateEntity("NoName9","Femur",-2606.610000,11224.806000,38790.198000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.046646,-0.874826,0.115913,-0.468047
o.CastShadows=0


o=Bladex.CreateEntity("NoName10","Femur",-2345.576000,10978.919000,37926.741000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.062787,-0.126053,0.021793,-0.989795
o.CastShadows=0


o=Bladex.CreateEntity("NoName11","Piedra_01",721.186000,10922.316000,43173.815000,Reference.ObjType("Piedra_01"))
o.Scale=0.620260
o.Orientation=0.062821,-0.971984,-0.225588,-0.020272
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName12","Piedra_01",-146.919000,11116.573000,42287.204000,Reference.ObjType("Piedra_01"))
o.Scale=0.645445
o.Orientation=0.188914,-0.503129,0.196860,-0.820012
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName13","Tabla_rota",-1050.656000,11083.896000,42308.814000,Reference.ObjType("Tabla_rota"))
o.Scale=1.000000
o.Orientation=0.543222,0.743882,-0.306373,0.240178
Sparks.SetWoodenSparkling(o.Name)



o=Bladex.CreateEntity("NoName16","Piedra_09",3283.312000,10885.007000,28963.297000,Reference.ObjType("Piedra_09"))
o.Scale=0.498315
o.Orientation=0.672245,0.722446,0.119303,-0.109202
o.CastShadows=0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName17","Caja_i_r",66223.685000,-1084.352000,-29297.273000,Reference.ObjType("Caja_i_r"))

o.Scale=1.890462
o.Orientation=0.963630,0.000000,0.267238,0.000000
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName18","Caja_i_r",65518.250358,-783.731294,-26477.044517,Reference.ObjType("Caja_i_r"))

o.Scale=1.257163
o.Orientation=0.717732,0.696065,-0.017356,0.007273
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName19","Tabla_rota",68448.365000,-46.527000,-31708.330000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.703233,0.703233,0.073913,-0.073913
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName20","Tabla_rota",67659.173000,-48.093000,-27781.641000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.055479,0.055479,0.704927,-0.704927
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName21","Tabla_rota",67072.452000,-41.775000,-26809.759000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.270598,0.270598,0.653282,-0.653282
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName22","Tabla_rota",74649.905000,-47.745000,-31211.357000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.529592,0.529592,0.468543,-0.468543
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName23","Tabla_rota",74560.840000,-46.048000,-29726.712000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName24","Tabla_rota",75443.603000,-158.819000,-24207.841000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.076760,-0.057359,-0.713430,0.694144
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName25","Tabla_rota",87822.026000,-5046.406000,-25001.651000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.030844,0.030844,0.706434,-0.706434
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName26","Tabla_rota",86932.816000,-5056.920000,-24236.667000,Reference.ObjType("Tabla_rota"))

o.Scale=1.308209
o.Orientation=0.110616,0.110616,0.698401,-0.698401
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName27","Tabla_rota",95372.808000,-5059.007000,-24211.362000,Reference.ObjType("Tabla_rota"))

o.Scale=1.503752
o.Orientation=0.700225,0.700225,0.098410,-0.098410
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName28","Tabla_rota",91984.710000,-52.127000,-25412.223000,Reference.ObjType("Tabla_rota"))

o.Scale=1.321291
o.Orientation=0.241845,0.241845,0.664463,-0.664463
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName29","Tabla_rota",90864.966000,-45.782000,-25034.175000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.672499,0.672499,0.218508,-0.218508
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName30","Tabla_rota",92308.320000,-123.343000,-24485.522000,Reference.ObjType("Tabla_rota"))

o.Scale=2.088246
o.Orientation=0.094536,0.110479,-0.645152,0.750091
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName31","Tabla_rota",93844.959000,-63.333000,-25889.685000,Reference.ObjType("Tabla_rota"))

o.Scale=1.628348
o.Orientation=0.698401,0.698401,-0.110616,0.110616
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName32","Tabla_rota",90717.642000,-44.176000,-27914.553000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.612373,0.612373,0.353553,-0.353553
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName33","Tabla_rota",90584.693000,-1039.122000,-30197.964000,Reference.ObjType("Tabla_rota"))

o.Scale=1.711410
o.Orientation=0.683934,-0.102666,-0.176112,0.700484
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Tabla_xl",82392.496000,-48.277000,1056.678000,Reference.ObjType("Tabla_xl"))

o.Scale=1.000000
o.Orientation=0.264887,0.264887,0.655618,-0.655618
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Tabla_rota",83697.103000,-47.982000,1449.958000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Tabla_rota",82942.754000,-45.971000,-868.804000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.662327,0.662327,0.247634,-0.247634
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Tabla_rota",71715.609000,-48.096000,571.357000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.650895,0.650895,0.276289,-0.276289
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Skull",88464.715000,-91.100000,2605.541000,Reference.ObjType("Skull"))

o.Scale=1.000000
o.Orientation=0.867067,0.498004,0.012647,-0.005242



o=Bladex.CreateEntity("NoName5","Femur",87806.105000,-57.354000,2708.702000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.999298,-0.012365,-0.027879,0.021748



o=Bladex.CreateEntity("NoName6","Femur",87007.205000,-55.661000,2619.283000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.322923,0.091110,-0.940547,-0.052825



o=Bladex.CreateEntity("NoName7","Tabla_rota",86349.235000,-709.481000,3930.602000,Reference.ObjType("Tabla_rota"))

o.Scale=1.232392
o.Orientation=0.127117,0.696750,0.688987,-0.153875
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Tabla_rota",86582.228000,-48.185000,1525.918000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.353553,0.353553,-0.612372,0.612373
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Taburete",27518.988000,-8352.525000,54469.491000,Reference.ObjType("Taburete"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName1","Taburete",26977.527000,-8346.304000,53536.498000,Reference.ObjType("Taburete"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName2","Pergamino",25651.571000,-9021.145000,53743.305000,Reference.ObjType("Pergamino"))

o.Scale=1.000000
o.Orientation=0.997097,0.028015,-0.070775,0.001726



o=Bladex.CreateEntity("NoName3","Pergamino",25768.516000,-9021.054000,54158.245000,Reference.ObjType("Pergamino"))

o.Scale=1.196147
o.Orientation=0.779970,0.576099,0.199117,-0.141804



o=Bladex.CreateEntity("NoName4","Pergamino",25904.111000,-9026.920000,54450.524000,Reference.ObjType("Pergamino"))

o.Scale=1.361327
o.Orientation=0.858921,0.488128,0.134571,-0.076665



o=Bladex.CreateEntity("NoName5","Tintero",25907.372000,-9019.177000,53219.361000,Reference.ObjType("Tintero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName6","Caliz",28690.801000,-9068.825000,54621.517000,Reference.ObjType("Caliz"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName7","Caliz",28859.607000,-9058.796000,53821.356000,Reference.ObjType("Caliz"))

o.Scale=1.000000
o.Orientation=0.824653,-0.023910,0.101171,-0.556004



o=Bladex.CreateEntity("NoName10","Candelpeque",28745.446000,-9240.161000,53311.878000,Reference.ObjType("Candelpeque"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 18 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName11","Candelpeque",26040.197000,-9250.839000,53692.822000,Reference.ObjType("Candelpeque"))

o.Scale=1.000000
o.Orientation=0.652989,0.695967,-0.211657,0.210800
o.FiresIntensity=[ 19 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("ARM4","Armero",17703.728000,-8849.266000,55062.216000,Reference.ObjType("Armero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARM4",12,100)


o=Bladex.CreateEntity("ARM3","Armero",20121.708000,-8835.704000,55040.836000,Reference.ObjType("Armero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARM3",12,100)


o=Bladex.CreateEntity("NoName23","Tapiz",-5193.572000,165.780000,37884.034000,Reference.ObjType("Tapiz"))

o.Scale=1.334504
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName24","Tapiz2",-5244.699000,181.449000,35563.534000,Reference.ObjType("Tapiz2"))

o.Scale=1.220190
o.Orientation=0.500000,0.500000,0.500000,-0.500000



o=Bladex.CreateEntity("NoName25","Tapiz2",-5212.190000,82.848000,43053.751000,Reference.ObjType("Tapiz2"))

o.Scale=1.220190
o.Orientation=0.500000,0.500000,0.500000,-0.500000



o=Bladex.CreateEntity("NoName26","Tapiz3",-5249.089000,60.712000,41460.131000,Reference.ObjType("Tapiz3"))

o.Scale=1.196147
o.Orientation=0.495618,0.495618,0.504344,-0.504344



o=Bladex.CreateEntity("NoName27","Caliz",-7454.310000,1761.996000,42222.750000,Reference.ObjType("Caliz"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName28","Caliz",-7379.293000,1763.693000,42757.884000,Reference.ObjType("Caliz"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName29","Caliz",-6910.114000,1758.445000,41548.861000,Reference.ObjType("Caliz"))

o.Scale=1.000000
o.Orientation=0.494858,0.015713,-0.868396,0.027495



o=Bladex.CreateEntity("NoName30","Velon",-7766.649000,1712.476000,41549.105000,Reference.ObjType("Velon"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 19 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("ARM2","Armero",13396.859000,-840.086000,56244.287000,Reference.ObjType("Armero"))

o.Scale=1.000000
o.Orientation=0.710682,0.702798,0.021107,-0.023668
Breakings.SetBreakable("ARM2",12,100)


o=Bladex.CreateEntity("ARM1","Armero",11713.621000,-835.063000,56254.024000,Reference.ObjType("Armero"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARM1",12,100)


o=Bladex.CreateEntity("NoName10","Tabla_rota",12026.714000,-47.817000,54592.895000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.688984,0.688984,0.159064,-0.159064
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Tabla_rota",14172.362000,-46.013000,54682.587000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.430459,0.430459,-0.560986,0.560986
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Tabla_xl",14726.200000,-731.113000,55988.219000,Reference.ObjType("Tabla_xl"))

o.Scale=1.000000
o.Orientation=0.703880,-0.079565,-0.068527,-0.702515
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Tabla_rota",2823.192000,-45.321000,54860.503000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.321020,0.321020,-0.630037,0.630037
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Tabla_rota",4633.041000,-47.976000,54981.892000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.618450,0.618450,-0.342812,0.342812
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName15","Tabla_rota",9039.127000,-45.993000,54018.508000,Reference.ObjType("Tabla_rota"))

o.Scale=1.000000
o.Orientation=0.374710,0.374710,-0.599660,0.599660
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Peanapiedra",41043.555000,-3357.950000,23407.974000,Reference.ObjType("Peanapiedra"))

o.Scale=3.203323
o.Orientation=0.504344,0.504344,0.495618,-0.495618



o=Bladex.CreateEntity("NoName1","Peanapiedra",41092.022000,-3399.101000,20436.709000,Reference.ObjType("Peanapiedra"))

o.Scale=3.109114
o.Orientation=0.486740,0.486740,-0.512917,0.512917



o=Bladex.CreateEntity("NoName2","Peanapiedra",40650.658000,-11332.161000,54738.321000,Reference.ObjType("Peanapiedra"))

o.Scale=4.232522
o.Orientation=0.517145,0.517145,-0.482246,0.482246



o=Bladex.CreateEntity("NoName3","Peanapiedra",40697.934000,-11306.381000,57761.391000,Reference.ObjType("Peanapiedra"))

o.Scale=4.232522
o.Orientation=0.491198,0.491198,0.508650,-0.508650



o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-59714.604000,23610.505000,49084.340000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.518790
o.Orientation=0.662327,0.662327,0.247634,-0.247634
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-54272.438000,20573.091000,47033.439000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.644632
o.Orientation=0.521334,0.521334,0.477714,-0.477714
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-46833.883000,18597.770000,51664.973000,Reference.ObjType("Adoquinpulsador"))

o.Scale=2.497850
o.Orientation=0.356614,0.370311,0.609234,-0.603763
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",-61785.247000,23613.491000,47711.902000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.474123
o.Orientation=0.444997,0.444997,0.549525,-0.549525
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",-52059.127000,20496.843000,46633.535000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.947745
o.Orientation=0.674380,0.674380,0.212631,-0.212631
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Adoquinpulsador",-41337.590000,18587.708000,41533.269000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.596263
o.Orientation=0.624338,0.624338,0.331967,-0.331967
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Adoquinpulsador",-39814.149000,18187.040000,41633.963000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.711410
o.Orientation=0.699684,0.580580,-0.066622,0.411012
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Adoquinpulsador",-61075.305000,23692.694000,52920.124000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.184304
o.Orientation=0.695266,0.695266,0.128860,-0.128860
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Adoquinpulsador",-56977.564000,23581.278000,85248.539000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.628348
o.Orientation=0.655618,0.655618,0.264887,-0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Adoquinpulsador",-57155.425000,23509.143000,74801.239000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.890462
o.Orientation=0.635543,0.635543,0.309975,-0.309975
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Adoquinpulsador",-66353.804000,23602.727000,88373.065000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.533978
o.Orientation=0.582745,0.582745,0.400510,-0.400510
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Adoquinpulsador",-17106.446000,1248.493000,43519.075000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.334504
o.Orientation=0.627211,0.627211,0.326506,-0.326506
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Adoquinpulsador",-16555.415000,1344.401000,41362.085000,Reference.ObjType("Adoquinpulsador"))

o.Scale=0.932718
o.Orientation=0.656599,0.681538,-0.221696,0.235022
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName13","Adoquinpulsador",-20203.864000,1324.629000,30587.968000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.040604
o.Orientation=0.608148,-0.603359,0.365953,0.363584
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName14","Adoquinpulsador",-20626.535000,1224.723000,32895.985000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.430769
o.Orientation=0.545621,0.545621,0.449775,-0.449775
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName15","Adoquinpulsador",-16664.697000,94.352000,13960.022000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.549318
o.Orientation=0.579228,0.579228,0.405580,-0.405580
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName16","Adoquinpulsador",-16093.575000,258.047000,11387.464000,Reference.ObjType("Adoquinpulsador"))

o.Scale=0.896324
o.Orientation=0.348196,0.348196,0.615434,-0.615434
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName17","Adoquinpulsador",-15482.606000,240.019000,-5097.095000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName18","Adoquinpulsador",13577.308000,9051.129000,138830.416000,Reference.ObjType("Adoquinpulsador"))

o.Scale=4.913826
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",83064.777000,213.861000,34068.929000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.986894
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",82439.667000,521.483000,34855.288000,Reference.ObjType("Adoquinpulsador"))

o.Scale=2.448633
o.Orientation=0.999848,0.017452,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",81677.777000,960.911000,35542.023000,Reference.ObjType("Adoquinpulsador"))

o.Scale=3.300387
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",86269.799000,-17.848000,35324.934000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",84619.860000,-74.225000,35176.487000,Reference.ObjType("Adoquinpulsador"))

o.Scale=1.257163
o.Orientation=0.410619,0.410619,0.575667,-0.575667
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Skull",18203.974000,9901.477000,39886.865000,Reference.ObjType("Skull"))

o.Scale=1.072135
o.Orientation=0.874661,0.468002,0.085074,-0.093298



o=Bladex.CreateEntity("NoName1","Skull",14352.903000,9899.738000,41979.656000,Reference.ObjType("Skull"))

o.Scale=1.000000
o.Orientation=0.689821,0.155249,0.153570,0.690262



o=Bladex.CreateEntity("NoName3","Femur",12885.110000,9977.161000,41238.611000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.022252,-0.173159,0.019280,-0.984454



o=Bladex.CreateEntity("NoName4","Femur",13559.802000,9976.453000,42135.280000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.003523,-0.527243,-0.036064,0.848942



o=Bladex.CreateEntity("NoName5","Femur",12311.350000,9976.436000,41569.655000,Reference.ObjType("Femur"))

o.Scale=1.000000
o.Orientation=0.023031,0.354605,0.006219,-0.934712



o=Bladex.CreateEntity("NoName6","Restos",18376.765000,9919.058000,39353.387000,Reference.ObjType("Restos"))

o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName7","Femur",18900.978000,9933.287000,38912.721000,Reference.ObjType("Femur"))
o.Scale=1.220190
o.Orientation=0.884350,0.004415,-0.463586,-0.054720



o=Bladex.CreateEntity("ant1","Antorcha",39172.568526,7179.298233,8671.649070,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.022930,0.976981,-0.211561,0.014995
o.FiresIntensity=[ 43 ]
o.Lights=[ (0.000000,0.031250,(255,146,26)) ]



o=Bladex.CreateEntity("antj21","Antorcha",37353.534568,7181.237040,8713.195738,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.907006,0.026734,0.413806,0.073421
o.FiresIntensity=[ 40 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]  # PLAGUE: maybe should match colour with ant1?



o=Bladex.CreateEntity("antj22","Antorcha",6826.616000,10909.064000,38302.013000,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.119320,0.446086,0.884867,0.061490
o.FiresIntensity=[ 41 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj21","Antorcha",45332.620000,3177.610000,6838.013000,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.998980,0.017240,0.009372,-0.040663
o.FiresIntensity=[ 39 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj22","Antorcha",43994.348000,3170.987000,6955.544000,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.023556,0.483866,-0.006845,-0.874798
o.FiresIntensity=[ 36 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antjj23","Antorcha",44164.250000,6436.470000,-372.178000,Reference.ObjType("Antorcha"))
o.Scale=1.000000
o.Orientation=0.372292,0.614889,-0.321387,-0.616459
o.FiresIntensity=[ 43 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("antpj1","Antorchaenpared",15507.157000,9505.489000,-8570.579000,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.614294,0.680743,0.301968,-0.260858
o.FiresIntensity=[ 42 ]
o.Lights=[ (0.000000,0.031250,(223,117,0)) ]



o=Bladex.CreateEntity("NoName1","Skull",18066.228000,10898.409000,-10712.052000,Reference.ObjType("Skull"))
o.Scale=1.000000
o.Orientation=0.600676,0.508682,-0.428476,-0.443665
o.CastShadows=0


o=Bladex.CreateEntity("NoName2","Skull",21036.617000,10897.083000,-12797.725000,Reference.ObjType("Skull"))
o.Scale=1.000000
o.Orientation=0.884924,0.431914,0.167546,0.047830
o.CastShadows=0


o=Bladex.CreateEntity("NoName3","Femur",20626.334000,10980.322000,-10462.539000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.015727,-0.050592,0.021895,-0.998356
o.CastShadows=0


o=Bladex.CreateEntity("NoName4","Femur",20238.855000,10945.407000,-8846.865000,Reference.ObjType("Femur"))
o.Scale=1.000000
o.Orientation=0.754719,0.036384,-0.651395,-0.068993
o.CastShadows=0


o=Bladex.CreateEntity("ARM5","Armero",13479.827000,-8839.293000,47946.189000,Reference.ObjType("Armero"))

o.Scale=1.000000
o.Orientation=0.006167,0.006171,0.707080,-0.707080
Breakings.SetBreakable("ARM5",12,100)

o=Bladex.CreateEntity("NoName2","Columna",-1665.300176,11082.835481,9603.946610,Reference.ObjType("Columna"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("ARM6","Armero",99527.540417,-6038.513996,45493.497085,Reference.ObjType("Armero"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARM6",12,100)


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",21241.250449,-2477.105488,86329.466115,Reference.ObjType("Adoquinpulsador"))
o.Scale=1.745810
o.Orientation=0.719479,0.694506,-0.002406,0.002327
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",16639.649230,-2726.278912,86303.130065,Reference.ObjType("Adoquinpulsador"))
o.Scale=1.000000
o.Orientation=0.517145,0.517145,0.482246,-0.482246
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",17637.172825,-2737.494712,86398.919747,Reference.ObjType("Adoquinpulsador"))
o.Scale=1.082857
o.Orientation=0.396108,0.398970,0.589933,-0.579570
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",17004.168039,-3281.233417,86612.402003,Reference.ObjType("Adoquinpulsador"))
o.Scale=1.104622
o.Orientation=0.701196,0.712421,-0.017054,-0.022134
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("NoName1","Adoquinpulsador",20315.668382,-3254.426923,86415.121206,Reference.ObjType("Adoquinpulsador"))
o.Scale=1.321291
o.Orientation=0.718787,0.694851,0.015780,-0.016698
Sparks.SetStoneSparkling(o.Name)
##antorcha dentro del elevador##

o=Bladex.CreateEntity("antcrip1","Antorchaenpared",30849.288000,5379.545000,9292.320000,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.549525,0.444997,0.444997,-0.549525
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.312500,(206,108,0)) ]


o=Bladex.CreateEntity("antcrip2","Antorchaenpared",38158.802000,6135.132000,15103.625000,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.061628,-0.024678,0.704416,-0.706676
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.231250,(255,145,23)) ]
################################

rassn1=Bladex.CreateEntity("Rassn1","Rastrillo",15764.171927,-10520.440035,49982.498048,Reference.ObjType("Rastrillo"))
rassn1.Scale=1.072135
rassn1.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("Rassn1")



o=Bladex.CreateEntity("NoName1","Antorchaenpared",63277.155000,-5876.235000,-27959.513000,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.049325,-0.061628,0.705384,-0.704416
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000, 0.100000, (255,158,51)) ]  # precision 0.131250 -> 0.1



o=Bladex.CreateEntity("NoName1","ArmaduraCaballeroMedia",13478.834838,-8345.082413,56276.428405,Reference.ObjType("ArmaduraCaballeroMedia"))
o.Scale=1.000000
o.Solid=0
o.Orientation=0.612059,0.597219,-0.365750,0.367341



o=Bladex.CreateEntity("NoName2","ArmaduraEnanoMedia",62191.568965,-4497.729161,-28070.700946,Reference.ObjType("ArmaduraEnanoMedia"))
o.Scale=1.000000
o.Solid=0
o.Orientation=0.704951,0.709243,-0.000835,0.004141



o=Bladex.CreateEntity("NoName3","ArmaduraAmazonaLigera",62534.291961,-4400.983198,-29674.329347,Reference.ObjType("ArmaduraAmazonaLigera"))
o.Scale=1.000000
o.Solid=0
o.Orientation=0.704719,0.709471,-0.002304,-0.004060



o=Bladex.CreateEntity("NoName5","Escudo2",60326.225299,-4511.271341,-27147.093048,Reference.ObjType("Escudo2"))
o.Scale=1.000000
o.Orientation=0.974513,-0.122371,0.143550,-0.121418



o=Bladex.CreateEntity("NoName7","Escudo2",59322.058222,-4502.568572,-27303.293313,Reference.ObjType("Escudo2"))
o.Scale=1.000000
o.Orientation=0.076942,-0.130331,0.972769,0.175538



o=Bladex.CreateEntity("NoName8","Tabla_xl",57778.663831,-4294.883289,-28951.729198,Reference.ObjType("Tabla_xl"))
o.Scale=1.000000
o.Orientation=0.564705,0.573575,0.417165,-0.422010
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Tabla_rota",57594.380244,-4327.010155,-29681.742374,Reference.ObjType("Tabla_rota"))
o.Scale=1.000000
o.Orientation=0.581449,0.752262,0.189442,-0.245214
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Tabla_rota",60045.653899,-4295.636013,-32619.842834,Reference.ObjType("Tabla_rota"))
o.Scale=1.000000
o.Orientation=0.572679,-0.562392,-0.423838,-0.419662
Sparks.SetWoodenSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Tabla_rota",59362.728962,-4338.767714,-32541.703078,Reference.ObjType("Tabla_rota"))
o.Scale=1.160969
o.Orientation=0.362858,-0.450389,-0.511443,-0.635539
Sparks.SetWoodenSparkling(o.Name)
adoq=Bladex.CreateEntity("Adice1","Adoquinpulsador",89051.158765,-10344.732901,67701.517490,Reference.ObjType("Adoquinpulsador"))
adoq.Scale=8.243872
adoq.Orientation=0.495618,0.495618,-0.504344,-0.504344
adoq.CastShadows=0
adoq.Alpha = 0


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",38678.530992,-714.449155,40791.939184,Reference.ObjType("Adoquinpulsador"))
o.Scale=2.814640
o.Orientation=0.363860,0.363559,0.606632,-0.606159
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",40013.899720,-732.161975,40491.292930,Reference.ObjType("Adoquinpulsador"))
o.Scale=2.376619
o.Orientation=0.449775,0.449775,0.545621,-0.545621
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","LapidaCaballero",25782.415271,-215.716500,859.753527,Reference.ObjType("LapidaCaballero"))
o.Scale=1.000000
o.Orientation=0.737277,0.675590,0.000000,0.000000
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Lapida3",28936.718299,-237.255312,-928.916282,Reference.ObjType("Lapida3"))
o.Scale=1.745810
o.Orientation=0.198276,0.974557,-0.008201,-0.104206
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Lapida3",26401.920594,-99.360057,10123.505969,Reference.ObjType("Lapida3"))
o.Scale=1.503752
o.Orientation=0.994522,0.104528,0.000000,0.000000
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Lapida",31763.195480,-28.179462,12347.127847,Reference.ObjType("Lapida"))
o.Scale=1.967222
o.Orientation=0.904169,0.121203,0.393285,-0.114518
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","LapidaBarbaro",12023.898378,-135.466260,11993.982624,Reference.ObjType("LapidaBarbaro"))
o.Scale=1.115668
o.Orientation=0.152057,0.141795,0.715372,-0.667095
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)



o=Bladex.CreateEntity("NoName8","EsqueletoPieza4",24961.148564,-48.134811,3540.449646,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.231166,0.606696,-0.197308,-0.734542



o=Bladex.CreateEntity("NoName10","EsqueletoPieza2",26449.455850,-54.240432,3293.702603,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.857167,0.515038,0.000000,0.000000



o=Bladex.CreateEntity("NoName11","EsqueletoPieza10",27320.619445,-44.121572,2030.430322,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.988991,0.035035,-0.058727,-0.131229


o=Bladex.CreateEntity("NoName12","EsqueletoPieza10",25375.717304,-28.565552,3397.690109,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.991445,0.130526,0.000000,0.000000


o=Bladex.CreateEntity("NoName13","EsqueletoPieza1",25935.621122,-4.180115,3646.164789,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.429970,0.119241,0.894628,-0.023427


o=Bladex.CreateEntity("NoName14","EsqueletoPieza1",24270.122269,-70.260932,9946.819227,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.072135
o.Orientation=0.990268,0.139173,0.000000,0.000000


o=Bladex.CreateEntity("NoName15","EsqueletoPieza10",23737.935696,-41.008631,10339.894657,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.949021,0.088251,-0.186292,-0.238465

o=Bladex.CreateEntity("NoName16","EsqueletoPieza10",24699.606700,-43.289672,8850.795362,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.308209
o.Orientation=0.772655,0.215261,-0.558164,-0.212415

o=Bladex.CreateEntity("NoName17","EsqueletoPieza10",23777.698712,-38.060877,9505.947527,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.671729,0.179405,-0.709078,-0.117484

o=Bladex.CreateEntity("NoName18","EsqueletoPieza2",24107.941581,-46.330566,10804.664279,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.853888,0.473318,0.104932,-0.189302

o=Bladex.CreateEntity("NoName19","EsqueletoPieza2",34012.121825,-67.245476,880.994790,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.072135
o.Orientation=0.734660,0.450200,0.432748,-0.265188


o=Bladex.CreateEntity("NoName20","EsqueletoPieza1",33282.539120,-20.038950,235.535112,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.220190
o.Orientation=0.916993,0.112593,-0.379831,-0.046637



o=Bladex.CreateEntity("NoName21","EsqueletoPieza4",34032.840660,-35.699835,-469.208535,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.374091,-0.390675,-0.801971,0.253518



o=Bladex.CreateEntity("NoName22","EsqueletoPieza4",33466.707075,-46.695589,-824.242349,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.283597,0.529451,-0.196723,-0.774954



o=Bladex.CreateEntity("NoName23","EsqueletoPieza4",32814.409166,-44.727198,-393.928855,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.096711,0.889943,-0.369109,-0.249815



o=Bladex.CreateEntity("NoName24","EsqueletoPieza4",36361.992971,-46.873761,4452.111528,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.135531,0.852658,-0.401555,-0.305547



o=Bladex.CreateEntity("NoName25","EsqueletoPieza4",37348.154188,-40.035835,4451.841308,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.308209
o.Orientation=0.682686,-0.234390,-0.575084,0.385072



o=Bladex.CreateEntity("NoName26","EsqueletoPieza1",36711.495612,-57.366776,5248.812748,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.991445,0.130526,0.000000,0.000000




o=Bladex.CreateEntity("NoName2","EsqueletoPieza2",25255.269657,-370.098049,949.659552,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.846930,0.153440,0.274047,-0.429027



o=Bladex.CreateEntity("NoName3","EsqueletoPieza4",25626.885760,-294.048641,1087.786872,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.793573,0.063324,-0.595929,-0.105357



o=Bladex.CreateEntity("NoName4","EsqueletoPieza4",28836.026818,-33.783895,2034.935817,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.864697,-0.023222,-0.176709,0.469610



o=Bladex.CreateEntity("NoName5","EsqueletoPieza4",29361.063346,-52.701629,1262.977997,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.022229,0.729111,-0.007079,-0.683998



o=Bladex.CreateEntity("NoName6","EsqueletoPieza2",29628.809021,-102.985746,2367.375075,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.082857
o.Orientation=0.566431,0.479382,-0.535876,-0.402723



o=Bladex.CreateEntity("NoName7","EsqueletoPieza2",36655.559569,-56.006407,5788.225563,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.945849,-0.092422,-0.255517,0.177594



o=Bladex.CreateEntity("NoName8","EsqueletoPieza2",10949.497717,-30.671943,11196.832195,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.919559,0.312789,-0.195099,0.136052



o=Bladex.CreateEntity("NoName9","EsqueletoPieza1",11099.381154,-33.707898,10498.797389,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.998630,0.052336,0.000000,0.000000



o=Bladex.CreateEntity("NoName10","LapidaBarbaro",29794.510201,-257.214004,33836.172794,Reference.ObjType("LapidaBarbaro"))
o.Scale=1.220190
o.Orientation=0.709475,0.685132,-0.118725,0.114652
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Lapida3",32458.152768,-321.183836,38738.783526,Reference.ObjType("Lapida3"))
o.Scale=1.967222
o.Orientation=0.871924,0.068622,0.483315,0.038038
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","EsqueletoPieza1",26971.085014,-53.441223,34699.805280,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.082857
o.Orientation=0.999048,0.043619,0.000000,0.000000



o=Bladex.CreateEntity("NoName13","EsqueletoPieza2",26950.641175,-32.961738,35285.641788,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.975367,0.042585,-0.216234,-0.009441



o=Bladex.CreateEntity("NoName14","EsqueletoPieza4",26807.596413,-40.788269,33991.998707,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.447408,-0.212025,-0.166310,0.852767



o=Bladex.CreateEntity("NoName15","EsqueletoPieza10",27284.750238,-53.231596,33715.213241,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.977458,0.020471,0.181744,0.105477



o=Bladex.CreateEntity("NoName16","EsqueletoPieza10",27356.595602,-38.513564,34900.089573,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.520377,-0.090236,0.146547,-0.836415



o=Bladex.CreateEntity("NoName17","EsqueletoPieza10",23291.058791,-54.265869,40629.804470,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.763926,0.129529,0.604546,0.184833



o=Bladex.CreateEntity("NoName18","EsqueletoPieza10",23219.910013,-56.393971,41320.516573,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.600159,0.321077,0.380885,0.625815



o=Bladex.CreateEntity("NoName19","EsqueletoPieza2",22869.844265,-64.138988,41043.790930,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.104622
o.Orientation=0.917060,0.398749,0.000000,0.000000



o=Bladex.CreateEntity("NoName20","EsqueletoPieza1",23767.140908,-45.675015,39976.477134,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.866025,-0.000000,-0.498782,0.034878



o=Bladex.CreateEntity("NoName21","EsqueletoPieza1",19029.915455,-80.686319,31650.347767,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.115668
o.Orientation=0.917454,0.004449,0.393299,0.059784



o=Bladex.CreateEntity("NoName22","EsqueletoPieza2",19421.876295,-61.430879,32137.601106,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.974370,0.224951,0.000000,0.000000



o=Bladex.CreateEntity("NoName23","EsqueletoPieza4",18786.646896,-46.347492,32109.963633,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.219919,0.760099,-0.461708,-0.400887



o=Bladex.CreateEntity("NoName24","EsqueletoPieza4",17777.409127,-35.768598,32122.875932,Reference.ObjType("EsqueletoPieza4"))
o.Scale=1.000000
o.Orientation=0.477103,-0.341874,-0.749162,0.307004



o=Bladex.CreateEntity("NoName25","EsqueletoPieza10",17063.462781,-40.255141,32261.141957,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.374460,0.695911,-0.420139,-0.446061



o=Bladex.CreateEntity("NoName26","EsqueletoPieza2",16896.835945,-99.886760,31274.510725,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.608821,-0.365759,0.383989,-0.590009



o=Bladex.CreateEntity("NoName27","Lapida",7924.296763,-47.744581,31130.239994,Reference.ObjType("Lapida"))
o.Scale=1.503752
o.Orientation=0.071081,0.778835,-0.039164,-0.621956
Reference.EntitiesSelectionData[o.Name]=[0,0,""]
Sparks.SetStoneSparkling(o.Name)



o=Bladex.CreateEntity("NoName28","EsqueletoPieza1",8170.355128,-51.829723,29578.040757,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.196147
o.Orientation=0.999048,0.043619,0.000000,0.000000



o=Bladex.CreateEntity("NoName29","EsqueletoPieza2",8099.080444,-23.088642,30259.419266,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.949326,0.091410,-0.299321,-0.028821



o=Bladex.CreateEntity("NoName31","Adoquinpulsador",12541.764721,298.609124,29254.380915,Reference.ObjType("Adoquinpulsador"))
o.Scale=2.026831
o.Orientation=0.664463,0.688984,0.159064,-0.241845
Sparks.SetStoneSparkling(o.Name)




o=Bladex.CreateEntity("NoName4","BarrilPieza6",4131.179111,-48.645591,113750.270363,Reference.ObjType("BarrilPieza6"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName5","BarrilPieza4",4185.414987,-47.684572,114319.095526,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.391260,0.486612,-0.737755,-0.256595



o=Bladex.CreateEntity("NoName6","BarrilPieza4",3539.845227,-57.182872,114668.998679,Reference.ObjType("BarrilPieza4"))
o.Scale=1.269735
o.Orientation=0.824692,0.071252,-0.105614,-0.551047



o=Bladex.CreateEntity("NoName7","BarrilPieza4",1920.051401,-50.409808,114689.929189,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.619258,0.363078,-0.566228,-0.405067



o=Bladex.CreateEntity("NoName8","BarrilPieza4",2683.332334,-55.858381,115319.395570,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.801553,0.122073,-0.192275,-0.552848



o=Bladex.CreateEntity("NoName9","BarrilPieza4",3759.489034,-49.198789,112687.354481,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.674525,0.325598,-0.478824,-0.457962



o=Bladex.CreateEntity("NoName10","BarrilPieza4",4543.696302,-56.321027,112971.661367,Reference.ObjType("BarrilPieza4"))
o.Scale=1.244716
o.Orientation=0.764335,-0.217331,0.325688,-0.512334



o=Bladex.CreateEntity("NoName11","BarrilPieza6",2056.639681,-44.909080,112540.229026,Reference.ObjType("BarrilPieza6"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000




o=Bladex.CreateEntity("NoName12","Caja_i_r",7724.018772,-602.016841,115790.574062)
o.Scale=1.000000
o.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetWoodenSparkling(o.Name)
o.Static=1



o=Bladex.CreateEntity("NoName15","Hoguera",1604.858220,-196.690820,110888.486192,Reference.ObjType("Hoguera"))
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 13 ]
o.Lights=[ (1.000000,0.331250,(239,189,143)) ]



o=Bladex.CreateEntity("NoName16","BarrilPieza4",920.978264,-52.881266,107351.717403,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.684900,0.299400,-0.477216,-0.462099



o=Bladex.CreateEntity("NoName17","BarrilPieza4",1052.745974,-48.488641,108265.468807,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.820416,-0.093729,0.141372,-0.546028



o=Bladex.CreateEntity("NoName19","BarrilPieza4",1992.386716,-49.881469,109407.818545,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.827484,-0.001498,-0.010468,-0.561390



o=Bladex.CreateEntity("NoName20","BarrilPieza4",2597.257927,-46.905012,109407.805560,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.801218,-0.144941,0.219336,-0.537525



o=Bladex.CreateEntity("NoName21","BarrilPieza4",1392.448414,-50.582323,110135.778432,Reference.ObjType("BarrilPieza4"))
o.Scale=1.000000
o.Orientation=0.695961,0.299410,-0.461341,-0.461688



o=Bladex.CreateEntity("NoName0","Antorchaenpared",59200.588222,-1891.683260,88222.229891,Reference.ObjType("Antorchaenpared"))
o.Scale=1.000000
o.Orientation=0.485751,0.560887,-0.520522,0.422503
o.FiresIntensity=[ 0 ]
o.Lights=[ (6.000000,0.102000,(255,154,43)) ]   # precision 0.23 -> 0.102, intens 5.0 -> 6.0


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


o=Bladex.CreateEntity("NoName3","EsqueletoPieza1",76824.420485,119.795756,35041.108654,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.993884,0.052579,0.008932,0.096697


o=Bladex.CreateEntity("NoName4","EsqueletoPieza2",76472.125009,156.509428,35282.402369,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.875550,0.475633,-0.084039,-0.011047


o=Bladex.CreateEntity("NoName5","EsqueletoPieza2",77811.339036,117.510021,34990.524009,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.045537,-0.341058,0.076598,0.935809


o=Bladex.CreateEntity("NoName6","EsqueletoPieza2",77934.798255,153.117284,35295.879978,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.075920,0.641969,-0.762952,0.003966


o=Bladex.CreateEntity("NoName7","EsqueletoPieza2",78659.382682,154.575586,35686.402473,Reference.ObjType("EsqueletoPieza2"))
o.Scale=1.000000
o.Orientation=0.507692,0.575370,-0.564571,-0.304070


o=Bladex.CreateEntity("NoName8","EsqueletoPieza10",77159.781120,213.032527,34574.474419,Reference.ObjType("EsqueletoPieza10"))
o.Scale=1.000000
o.Orientation=0.093412,-0.819085,0.449994,-0.343336


o=Bladex.CreateEntity("NoName10","EsqueletoPieza1",75054.092553,118.679538,36015.713945,Reference.ObjType("EsqueletoPieza1"))
o.Scale=1.000000
o.Orientation=0.821206,0.131594,-0.548070,-0.089012


o=Bladex.CreateEntity("NoName11","EsqueletoPieza6",77567.829835,203.537363,36427.831450,Reference.ObjType("EsqueletoPieza6"))
o.Scale=1.000000
o.Orientation=0.806183,0.079003,0.155829,0.565283

icebloque=Bladex.CreateEntity("Icebloque","Bloque",-22646.140706,9352.146791,64762.641156)
icebloque.Static=1
icebloque.Scale=2.958215
icebloque.Orientation=0.507948,0.496397,-0.494077,-0.501465
icebloque.CastShadows=0
icebloque.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]



o=Bladex.CreateEntity("NoName0","Bloque",30000.580405,-10838.434604,-28585.142850)
o.Scale=5.062720
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName1","Bloque",29995.467558,-10856.727656,-34055.076910)
o.Scale=5.062720
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName2","Bloque",29810.191382,-10836.362961,-39485.696961)
o.Scale=5.113347
o.Orientation=0.502587,0.503106,-0.496327,-0.497945
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName3","Bloque",7697.349547,-10717.262553,-39548.570294)
o.Scale=5.164481
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName4","Bloque",7755.538820,-10709.060635,-33989.459579)
o.Scale=5.012594
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]

o=Bladex.CreateEntity("NoName5","Bloque",7777.943623,-10861.316608,-28456.784378)
o.Scale=5.012594
o.Orientation=0.497663,0.503860,-0.503208,-0.495216
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


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


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",117719.429408,-9935.286170,58254.504378)
o.Scale=12.396742
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName5","Adoquinpulsador",91131.385376,-6662.104164,-27741.444058)
o.Scale=5.819466
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName6","Adoquinpulsador",91465.700678,-6758.541449,-21467.220006)
o.Scale=5.995802
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha=0
Reference.EntitiesSelectionData[o.Name]=[0,0,""]


o=Bladex.CreateEntity("NoName7","Adoquinpulsador",69980.784395,-8540.138335,-31301.868901)
o.Scale=6.177481
o.Orientation=0.707107,0.707107,0.000000,0.000000
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
