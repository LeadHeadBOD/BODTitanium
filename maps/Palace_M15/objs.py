##///
##||| PALACE_M15/objs.PY TITANIUM
##||| Change list:
##||| * Added sparks for metal bars
##||| 
##\\\ 

import pocimac
import Ontake
import ItemTypes
import Reference




powp_PP1=Bladex.CreateEntity("Palacepowp_PP1","PowerPotion",40334.401331,-1725.937584,91291.483344,"Physic")
powp_PP1.Scale=1.072135
powp_PP1.Orientation=0.500000,0.500000,0.500000,-0.500000
powp_PP1.Solid=0
pocimac.CreatePowerPotion("Palacepowp_PP1")

powp_PP2=Bladex.CreateEntity("Palacepowp_PP2","PowerPotion",-24500.452967,14915.952950,106436.075116,"Physic")
powp_PP2.Scale=1.000000
powp_PP2.Orientation=0.098774,-0.629936,0.040599,0.769270
powp_PP2.Solid=0
pocimac.CreatePowerPotion("Palacepowp_PP2")

brpalace=Bladex.CreateEntity("BrazaletePalace","Brazalete",-23606.349565,14921.113694,106725.833466,"Physic")
brpalace.Scale=1.000000
brpalace.Orientation=0.776464,0.270138,-0.492191,-0.286142
brpalace.Solid=0
ItemTypes.ItemDefaultFuncs(brpalace)

o=Bladex.CreateEntity("Palace1Pocima1000","Pocima200",-32240.7301974, 808.607909556, 12638.5406515, "Physic")
o.Scale=1.15
o.Orientation=0.992415726185, -0.122635796666, 0.00843547843397, -0.000619392318185
o.Solid=0
pocimac.CreatePotion("Palace1Pocima1000")

o=Bladex.CreateEntity("Palace2Pocima500","Pocima100",18038.8587955, -111.609523307, 76043.2615296, "Physic")
o.Scale=1.15
o.Orientation=0.511739969254, 0.287767827511, -0.289227813482, -0.756081461906
o.Solid=0
pocimac.CreatePotion("Palace2Pocima500")

o=Bladex.CreateEntity("Palace3PocimaFull","PocimaTodo",-4851.52418264, 1406.30035575, 192802.667201, "Physic")
o.Scale=1.15
o.Orientation=0.991474866867, -0.122779980302, -0.0407349132001, -0.0155974654481
o.Solid=0
pocimac.CreatePotion("Palace3PocimaFull")

o=Bladex.CreateEntity("Palace4Pocima500","Pocima100",114776.580446, -1478.69399027, 233594.603574, "Physic")
o.Scale=1.15
o.Orientation=0.669609248638, 0.672966718674, 0.222276166081, -0.222109362483
o.Solid=0
pocimac.CreatePotion("Palace4Pocima500")

o=Bladex.CreateEntity("Palace5Pocima500","Pocima100",74659.320615, -983.1691245, 224354.474847, "Physic")
o.Scale=1.15
o.Orientation=0.680220067501, 0.677684307098, 0.197463735938, -0.197617515922
o.Solid=0
pocimac.CreatePotion("Palace5Pocima500")


arcopalace=Bladex.CreateEntity("ArcoPalace","Arco",-8794.936915,1287.894347,77218.174372,"Weapon")
arcopalace.Scale=1.000000
arcopalace.Orientation=0.800471,-0.312476,-0.416459,0.296928
ItemTypes.ItemDefaultFuncs(arcopalace)




o=Bladex.CreateEntity("NoName0","LamparaAurelio",-80983.225000,-3498.807000,70283.250000,"Physic")
o.Scale=1.072135
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.391966,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName2","Cebolla",-4689.125000,-7985.730000,67016.026000,"Physic")
o.Scale=2.283884
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Cebolla",-8670.804000,-8104.120000,67062.673000,"Physic")
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Cebolla",-12685.680000,-8130.549000,67010.990000,"Physic")
o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Cebolla",7317.185000,-2818.052000,67120.890000,"Physic")
o.Scale=2.173037
o.Orientation=0.706864,0.706864,-0.018510,-0.018510
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Antorcha2",-30847.650000,-7741.687000,100870.620000,"Physic")
o.Scale=1.430769
o.Orientation=0.504344,0.504344,0.495618,-0.495618
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName17","Elefante",-17181.221000,-2102.008000,194030.517000,"Physic")
o.Scale=1.388690
o.Orientation=0.508650,0.508650,-0.491198,0.491198
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName18","Elefante",-17156.648000,-2316.057000,203523.649000,"Physic")
o.Scale=1.564811
o.Orientation=0.508650,0.508650,-0.491198,0.491198
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName19","LamparaAurelio",27561.736000,-10250.010000,120814.329000,"Physic")
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (9.434238,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName20","LamparaAurelio",27449.600000,-10348.792000,133962.647000,"Physic")
o.Scale=1.082857
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.885648,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName21","Antorcha2",-29411.152000,-3058.995000,110232.728000,"Physic")
o.Scale=1.093685
o.Orientation=0.055479,0.055479,0.704927,-0.704927
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,140,13)) ]


o=Bladex.CreateEntity("NoName23","Columna",20174.326000,-6982.208000,69793.353000,"Physic")
o.Scale=2.329790
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName24","Columna",20235.463000,-6948.414000,76533.359000,"Physic")
o.Scale=2.353088
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName26","Columna",-82086.082000,-6984.111000,178289.491000,"Physic")
o.Scale=2.376619
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName27","Columna",-82005.443000,-6912.227000,171659.120000,"Physic")
o.Scale=2.283884
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName29","Cebolla",59763.405000,6753.906000,116713.191000,"Physic")
o.Scale=1.402577
o.Orientation=0.655618,0.655618,0.264887,0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName31","Columna",53173.786000,6719.113000,117078.445000,"Physic")
o.Scale=1.612226
o.Orientation=0.374607,0.927184,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName32","Cebolla",44583.850000,6670.912000,119018.246000,"Physic")
o.Scale=1.402577
o.Orientation=0.852640,0.522499,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName39","Varilla",27511.802000,-11098.808000,133962.407000,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName40","Varilla",27403.719000,-10925.771000,120787.935000,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("NoName41","Roca1",31905.121000,6790.892000,126641.990000,"Physic")
o.Scale=1.763268
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName43","LamparaMiguelSinPeana",41994.093000,-5501.807000,73096.945000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,183,102)) ]


o=Bladex.CreateEntity("NoName44","LamparaMiguelSinPeana",-96904.047000,-6135.714000,174968.534000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.11,(255,196,128)) ]


o=Bladex.CreateEntity("NoName47","Roca1",-17681.645000,14777.032000,135053.878000,"Physic")
o.Scale=2.151522
o.Orientation=0.030177,-0.579700,0.806428,0.112745
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName48","Roca2Aurelio",-15174.919000,14417.837000,124079.549000,"Physic")
o.Scale=1.644632
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName49","Roca1Aurelio",-32181.023000,14241.351000,124387.960000,"Physic")
o.Scale=1.853212
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName51","Rama2",-30444.765000,14282.309000,145576.484000,"Physic")
o.Scale=1.628348
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName58","CandilAurelio",29325.392000,-7162.671000,68476.080000,"Physic")
o.Scale=1.104622
o.Orientation=0.504344,0.504344,0.495618,-0.495618
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,145,23)) ]


o=Bladex.CreateEntity("NoName59","CandilAurelio",-7793.222000,3104.886000,-64426.287000,"Physic")
o.Scale=1.000000
o.Orientation=0.370729,0.378662,-0.594911,0.604365
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.157619,0.000000,(255,151,36)) ]


o=Bladex.CreateEntity("NoName60","CandilAurelio",-73490.600000,-1707.037000,64898.875000,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,0.521334,-0.521334
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.733440,0.100000,(255,196,128)) ]


o=Bladex.CreateEntity("NoName62","CandilAurelio",-19109.491000,-2876.693000,106225.896000,"Physic")
o.Scale=0.960980
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.FiresIntensity=[ 10 ]
o.Lights=[ (1.000000,0.015032,(240,126,0)) ]


o=Bladex.CreateEntity("NoName63","Roca1Aurelio",-61523.456000,6354.302000,73731.509000,"Physic")
o.Scale=1.000000
o.Orientation=0.425547,0.425547,-0.564721,0.564721
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName64","Roca1Aurelio",-53974.180000,6774.550000,70445.841000,"Physic")
o.Scale=0.887449
o.Orientation=0.609264,0.609264,-0.358884,0.358884
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName65","Columnaestrecha",-54668.332000,6260.406000,69286.304000,"Physic")
o.Scale=1.000000
o.Orientation=0.965926,0.258819,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName70","Varillaancha",-80963.006000,-5887.623000,70265.478000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
Sparks.SetMetalSparkling(o.Name)    #Add


o=Bladex.CreateEntity("NoName71","CandilAurelio",-11147.803000,-560.242000,225112.661000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.209523,(255,163,60)) ]


o=Bladex.CreateEntity("NoName72","Roca1Aurelio",-90065.101000,2413.336000,198673.214000,"Physic")
o.Scale=1.430769
o.Orientation=0.572061,0.572061,0.415627,-0.415627
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName73","Roca1",-97480.103000,2495.571000,204466.487000,"Physic")
o.Scale=1.160969
o.Orientation=0.643440,0.643440,0.293232,-0.293232
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName74","Roca1Aurelio",-88851.677000,2868.830000,170969.619000,"Physic")
o.Scale=1.220190
o.Orientation=0.655618,0.655618,0.264887,-0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName75","Timon",-88019.675000,588.263000,185279.432000,"Physic")
o.Scale=2.306723
o.Orientation=0.504344,0.504344,-0.495618,0.495618


o=Bladex.CreateEntity("NoName76","Timon",-115487.926000,469.853000,214850.222000,"Physic")
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName77","Gema",-91499.869000,2895.278000,192630.882000,"Physic")
o.Scale=1.816697
o.Orientation=0.999657,0.026177,0.000000,0.000000


o=Bladex.CreateEntity("NoName78","Skull",-89717.951000,2564.215000,192580.718000,"Weapon")
o.Scale=1.232392
o.Orientation=0.768478,0.434784,0.408607,-0.231179


o=Bladex.CreateEntity("NoName79","Skeleton_Optimiced",-91488.941000,3018.375000,191570.434000,"Physic")
o.Scale=1.402577
o.Orientation=0.831706,0.207368,-0.505575,0.098274


o=Bladex.CreateEntity("NoName82","CandilAurelio",19633.381000,-224.279000,205706.052000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,168,72)) ]


o=Bladex.CreateEntity("NoName83","Antorcha2",-17859.354000,-6276.235000,-41473.470000,"Physic")
o.Scale=1.612226
o.Orientation=0.012342,0.012341,0.706999,-0.706999
o.FiresIntensity=[ 3 ]
o.Lights=[ (2.292017,0.643553,(255,196,128)) ]


o=Bladex.CreateEntity("NoName84","Antorcha2",-30406.056000,-6473.000000,-41467.656000,"Physic")
o.Scale=1.763268
o.Orientation=0.088401,0.083889,-0.683224,0.719968
o.FiresIntensity=[ 3 ]
o.Lights=[ (2.078927,0.612908,(255,156,47)) ]


o=Bladex.CreateEntity("NoName87","Antorchaenpared",2351.254000,-1808.922000,257822.113000,"Physic")
o.Scale=1.000000
o.Orientation=0.557208,0.557208,-0.435338,0.435338
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.642778,0.100784,(238,155,64)) ]


o=Bladex.CreateEntity("NoName88","Roca1Aurelio",-7591.706000,-735.428000,241761.004000,"Physic")
o.Scale=1.745810
o.Orientation=0.963630,-0.267238,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName89","Roca1Aurelio",21983.474000,-98.460000,276551.233000,"Physic")
o.Scale=1.072135
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName91","Columnaestrecha",23269.448000,-760.809000,275628.784000,"Physic")
o.Scale=1.871744
o.Orientation=0.461749,0.887011,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName92","Columnaestrecha",34114.540000,-1000.847000,270922.779000,"Physic")
o.Scale=2.704814
o.Orientation=0.870356,0.492424,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName93","Antorchaenpared",43969.222000,-1203.028000,261143.579000,"Physic")
o.Scale=1.000000
o.Orientation=0.560986,0.560986,-0.430459,0.430459
o.FiresIntensity=[ 3 ]
o.Lights=[ (52.039326,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName94","Columnaestrecha",41862.834000,-1858.097000,241259.628000,"Physic")
o.Scale=2.731862
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName95","Roca1Aurelio",33649.050000,-648.473000,241978.085000,"Physic")
o.Scale=1.780901
o.Orientation=0.213775,0.964276,-0.152726,0.033859
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName96","Roca1Aurelio",37062.296000,-552.372000,260166.395000,"Physic")
o.Scale=1.677689
o.Orientation=0.471321,0.816351,-0.166903,0.289085
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName97","Columnaestrecha",36454.630000,-954.801000,257210.051000,"Physic")
o.Scale=2.216715
o.Orientation=0.690346,0.690346,0.153046,0.153046
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName98","Antorchaenpared",43208.410000,-1884.464000,236709.230000,"Physic")
o.Scale=1.000000
o.Orientation=0.159064,0.159064,-0.688984,0.688984
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.031250,(255,158,51)) ]


o=Bladex.CreateEntity("NoName99","Roca1Aurelio",17289.716000,1199.669000,241265.524000,"Physic")
o.Scale=2.497850
o.Orientation=0.537688,0.537688,0.459229,-0.459229
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName100","Roca1Aurelio",9278.382000,-290.306000,238242.156000,"Physic")
o.Scale=1.986894
o.Orientation=0.230211,0.230211,-0.668583,0.668583
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName101","Columnaestrecha",17360.327000,-2069.859000,241138.992000,"Physic")
o.Scale=2.473119
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName102","Roca1Aurelio",11013.703000,-1092.429000,250584.484000,"Physic")
o.Scale=1.816697
o.Orientation=0.551448,0.379000,0.612445,-0.420922
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName103","Roca1Aurelio",15907.435000,-343.325000,246282.983000,"Physic")
o.Scale=1.780901
o.Orientation=0.521334,0.521334,0.477714,-0.477714
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName104","Roca1Aurelio",21459.546000,862.343000,250226.050000,"Physic")
o.Scale=3.047852
o.Orientation=0.699340,0.699340,0.104517,-0.104517
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName105","Roca1Aurelio",29708.552000,-857.454000,251897.183000,"Physic")
o.Scale=1.388690
o.Orientation=0.627211,0.627211,0.326506,-0.326506
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName106","Columnaestrecha",13116.089000,-1197.352000,251659.800000,"Physic")
o.Scale=3.017675
o.Orientation=0.683013,0.683013,0.183013,0.183013
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName116","Roca1Aurelio",-43059.880000,1951.204000,229588.800000,"Physic")
o.Scale=1.503752
o.Orientation=0.687569,0.687569,-0.165071,0.165071
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName119","Antorchaenpared",-48491.422000,-103.841000,230220.005000,"Physic")
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (22.704601,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName120","Columnaestrecha",-12655.914000,-5731.062000,244289.629000,"Physic")
o.Scale=1.269735
o.Orientation=0.848048,0.529919,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName121","Roca1Aurelio",-12042.673000,-4988.178000,243421.485000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName122","Roca1Aurelio",-49041.345000,1756.521000,231629.347000,"Physic")
o.Scale=1.402577
o.Orientation=0.655618,0.655618,0.264887,-0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName123","Gancholamp",6654.444000,-2705.888000,216517.826000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,1.000000,0.000000,0.000000


o=Bladex.CreateEntity("NoName124","LamparaAurelio",6656.029000,-1793.394000,216391.718000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.921309,0.148904,(255,171,79)) ]


o=Bladex.CreateEntity("NoName125","LamparaAurelio",42858.510000,-7144.892000,208533.167000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (9.434233,0.111115,(255,196,128)) ]


o=Bladex.CreateEntity("NoName126","LamparaAurelio",43040.109000,-6819.319000,224536.275000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (8.557133,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName127","Varillaancha",43018.759000,-7498.943000,224535.372000,"Physic")
o.Scale=1.503752
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName128","Varillaancha",43070.003000,-7743.296000,208535.173000,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName0","Cebolla",-96749.903000,2145.100000,172851.015000,"Physic")
o.Scale=1.416603
o.Orientation=0.389015,0.417931,0.214205,-0.792539
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Columnaestrecha",-96467.522000,2467.101000,176870.951000,"Physic")
o.Scale=1.763268
o.Orientation=0.574536,0.004627,-0.818390,-0.011149
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Columnaestrecha",-92418.785000,2482.039000,171132.520000,"Physic")
o.Scale=1.711410
o.Orientation=0.011702,0.973060,0.003305,-0.230233
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Roca1Aurelio",-86665.508000,5053.907000,153085.898000,"Physic")
o.Scale=2.109128
o.Orientation=0.655618,0.655618,0.264887,-0.264887
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Roca1Aurelio",-884.755000,9628.439000,190536.379000,"Physic")
o.Scale=1.763268
o.Orientation=0.612373,0.612373,0.353553,-0.353553
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Cebolla",3081.601000,8900.304000,191345.775000,"Physic")
o.Scale=2.067570
o.Orientation=0.508908,0.745302,0.339171,0.265518
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","CandilAurelio",-23163.337000,-59.352000,198755.635000,"Physic")
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (6.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName0","Elefante",-17087.748000,-2201.102000,198859.792000,"Physic")
o.Scale=1.459527
o.Orientation=0.503119,0.501730,-0.497213,0.497914
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Antorchaenpared",14203.125000,-1339.458000,272468.580000,"Physic")
o.Scale=1.000000
o.Orientation=0.529592,0.529592,-0.468543,0.468543
o.FiresIntensity=[ 0 ]
o.Lights=[ (11.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName1","Antorchaenpared",-26118.124000,-3390.378000,240281.316000,"Physic")
o.Scale=1.000000
o.Orientation=0.670566,0.670566,0.224368,-0.224368
o.FiresIntensity=[ 0 ]
o.Lights=[ (11.000000,0.031250,(255,156,47)) ]


o=Bladex.CreateEntity("NoName2","Antorchaenpared",53108.002000,-1723.607000,243812.464000,"Physic")
o.Scale=1.172579
o.Orientation=0.618450,0.618450,-0.342812,0.342812
o.FiresIntensity=[ 0 ]
o.Lights=[ (11.000000,0.031250,(255,164,62)) ]


o=Bladex.CreateEntity("NoName2","Piedra_01",-11944.448000,4924.159000,58150.733000,"Physic")
o.Scale=1.000000
o.Orientation=0.936781,-0.246725,-0.157051,0.192103


o=Bladex.CreateEntity("NoName11","Piedra_01",81184.297000,1885.626000,105809.105000,"Physic")
o.Scale=1.564811
o.Orientation=0.953506,-0.203100,-0.005491,0.222592


o=Bladex.CreateEntity("NoName12","Piedra_01",82411.455000,1912.047000,106008.686000,"Physic")
o.Scale=1.000000
o.Orientation=0.676650,0.032967,0.696553,0.236375


o=Bladex.CreateEntity("NoName13","Piedra_01",82471.699000,1910.371000,103802.687000,"Physic")
o.Scale=1.000000
o.Orientation=0.978606,-0.116784,-0.087884,0.144803


o=Bladex.CreateEntity("NoName14","Piedra_08",79880.346000,1891.170000,103139.390000,"Physic")
o.Scale=1.000000
o.Orientation=0.691701,0.679008,-0.124817,-0.211939


o=Bladex.CreateEntity("NoName15","Piedra_08",83249.657000,1835.505000,102300.783000,"Physic")
o.Scale=1.612226
o.Orientation=0.696494,0.686770,-0.167185,-0.123660


o=Bladex.CreateEntity("NoName16","Antorchaenpared",85267.594000,2368.786000,45207.740000,"Physic")
o.Scale=1.000000
o.Orientation=0.704416,0.704416,-0.061628,-0.061628
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-26978.972000,2278.143000,65383.818000,"Physic")
o.Scale=6.177481
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-10935.699000,-13163.987000,172622.987000,"Physic")
o.Scale=5.648317
o.Orientation=0.517145,0.517145,0.482246,-0.482246


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",8672.068000,4622.867000,156180.495000,"Physic")
o.Scale=4.537836
o.Orientation=0.000000,0.000000,0.707107,0.707107


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",12965.349000,-7239.047000,154869.221000,"Physic")
o.Scale=5.592393
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",9506.461000,-5184.060000,154617.168000,"Physic")
o.Scale=6.301648
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName0","Baldosa_01",7725.525000,125.901000,76764.272000,"Physic")
o.Scale=2.731862
o.Orientation=0.708142,0.704984,-0.036585,-0.013939


o=Bladex.CreateEntity("NoName1","Baldosa_01",9794.697000,137.516000,75874.697000,"Physic")
o.Scale=2.871214
o.Orientation=0.705605,0.699327,0.044601,-0.105234


o=Bladex.CreateEntity("NoName2","Baldosa_01",8350.849000,139.488000,75293.458000,"Physic")
o.Scale=2.067570
o.Orientation=0.674312,0.728904,0.102517,0.059093


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",-13520.900000,4883.612000,58569.845000,"Physic")
o.Scale=2.026831
o.Orientation=0.664463,0.664463,0.241845,-0.241845
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",51844.546000,-10076.380000,61704.655000,"Physic")
o.Scale=4.492907
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Adoquinpulsador",65889.989000,-7052.204000,35722.970000,"Physic")
o.Scale=8.578606
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Adoquinpulsador",60674.780000,-8566.381000,30752.665000,"Physic")
o.Scale=10.677927
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Adoquinpulsador",43015.021000,-5415.974000,59770.462000,"Physic")
o.Scale=4.274847
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName8","Adoquinpulsador",87047.699000,-9280.818000,149307.997000,"Physic")
o.Scale=5.216126
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","Adoquinpulsador",90757.572000,-10661.072000,149678.809000,"Physic")
o.Scale=6.364665
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName10","Adoquinpulsador",77718.412000,2872.572000,143753.424000,"Physic")
o.Scale=4.817005
o.Orientation=0.662620,0.748956,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName11","Adoquinpulsador",59890.286000,1754.754000,117451.887000,"Physic")
o.Scale=3.987227
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName12","Adoquinpulsador",48357.175000,-9854.132000,149552.904000,"Physic")
o.Scale=4.108044
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",49674.855000,1333.691000,177668.273000,"Physic")
o.Scale=5.374180
o.Orientation=0.508650,0.508650,0.491198,-0.491198
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",49566.852000,-1116.084000,179997.667000,"Physic")
o.Scale=4.722091
o.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",50343.605000,64.238000,168243.532000,"Physic")
o.Scale=8.162250
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName3","Adoquinpulsador",53446.389000,771.119000,172675.835000,"Physic")
o.Scale=6.428311
o.Orientation=0.512917,0.512917,0.486740,-0.486740
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName4","Adoquinpulsador",52476.074000,-3619.157000,165738.415000,"Physic")
o.Scale=6.557520
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName5","Adoquinpulsador",90682.850000,-2201.662000,232392.661000,"Physic")
o.Scale=5.482201
o.Orientation=0.000000,0.000000,0.707107,0.707107
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName6","Adoquinpulsador",90769.882000,-450.711000,229436.777000,"Physic")
o.Scale=4.769311
o.Orientation=0.491198,0.491198,0.508650,-0.508650
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName7","Adoquinpulsador",78033.585000,-2262.739000,246717.538000,"Physic")
o.Scale=5.164481
o.Orientation=0.688355,-0.725374,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName9","TinajaPieza2",-29911.609000,-1063.429000,150943.082000,"Physic")
o.Scale=1.000000
o.Orientation=0.966929,0.158433,-0.092829,-0.177003


o=Bladex.CreateEntity("NoName10","TinajaPieza3",-28350.069000,-1089.085000,150660.706000,"Physic")
o.Scale=1.000000
o.Orientation=0.056769,0.974241,-0.205414,0.073729


o=Bladex.CreateEntity("NoName11","TinajaPieza4",-27103.579000,-1296.969000,151075.064000,"Physic")
o.Scale=1.000000
o.Orientation=0.977776,0.104608,-0.026163,-0.179795


o=Bladex.CreateEntity("NoName12","TinajaPieza2",-29740.602000,-1064.198000,147959.167000,"Physic")
o.Scale=1.000000
o.Orientation=0.533063,-0.082455,0.812394,-0.221498


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",-15488.295000,-4651.789000,90153.199000,"Physic")
o.Scale=2.928926
o.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",-15677.113000,-4672.539000,82842.510000,"Physic")
o.Scale=2.842787
o.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName2","Adoquinpulsador",-17320.010000,-16015.493000,83938.008000,"Physic")
o.Scale=4.274847
o.Orientation=0.504344,0.504344,-0.495618,0.495618
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("ap1","Antorchaenpared",-17639.009000,9320.493000,74535.424000,"Physic")
o.Scale=1.000000
o.Orientation=0.018510,0.018510,0.706864,-0.706864
o.FiresIntensity=[ 6 ]
o.Lights=[ (3.000000,0.009690,(255,134,0)) ]


o=Bladex.CreateEntity("ap2","Antorchaenpared",-30631.405000,8871.042000,74825.019000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 41 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("ap3","Antorchaenpared",-27947.266000,14672.072000,96389.658000,"Physic")
o.Scale=1.104622
o.Orientation=0.705384,0.705384,-0.049325,-0.049325
o.FiresIntensity=[ 30 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("ap4","Antorchaenpared",-20382.209000,14729.385000,96395.418000,"Physic")
o.Scale=1.000000
o.Orientation=0.043168,-0.080047,0.705788,-0.702561
o.FiresIntensity=[ 20 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("a1","Antorcha",-21100.360000,10820.441000,73839.080000,"Weapon")
o.Scale=1.000000
o.Orientation=0.517526,-0.271563,-0.196614,0.787250
o.FiresIntensity=[ 41 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName0","Gozne",98392.434000,-7496.835000,195038.719000,"Physic")
o.Scale=2.842787
o.Orientation=0.500000,0.500000,0.500000,-0.500000


o=Bladex.CreateEntity("NoName1","Gozne",90178.276000,-7493.772000,195032.968000,"Physic")
o.Scale=2.842787
o.Orientation=0.495618,0.495618,-0.504344,0.504344


o=Bladex.CreateEntity("NoName2","Gozne",98438.408000,-16391.227000,195030.647000,"Physic")
o.Scale=2.842787
o.Orientation=0.508650,0.508650,0.491198,-0.491198


o=Bladex.CreateEntity("NoName3","Gozne",90219.988000,-16390.481000,195038.641000,"Physic")
o.Scale=2.842787
o.Orientation=0.495618,0.495618,-0.504344,0.504344



o=Bladex.CreateEntity("NoName5","Garfio2",75339.915000,-5454.747000,73930.969000,"Physic")
o.Scale=2.928926
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName6","Antorchaenpared",69091.501000,1638.140000,60344.335000,"Physic")
o.Scale=1.232392
o.Orientation=0.553388,0.495618,0.440184,-0.504344
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.031250,(206,108,0)) ]


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",33471.195000,1131.908000,181441.820000,"Physic")
o.Scale=4.962965
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("a2","Antorcha",-19780.191000,10835.831000,74335.186000,"Weapon")
o.Scale=1.000000
o.Orientation=0.999483,0.031846,0.003920,-0.002182
o.FiresIntensity=[ 31 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName0","Baldosa_01",20871.311000,2343.128000,172334.654000,"Physic")
o.Scale=4.027099
o.Orientation=0.687769,0.547077,0.297038,-0.373428


o=Bladex.CreateEntity("NoName1","Baldosa_01",21643.221000,2204.657000,174155.172000,"Physic")
o.Scale=4.492907
o.Orientation=0.687569,0.702561,0.165071,-0.080047


o=Bladex.CreateEntity("NoName2","Baldosa_01",27460.802000,2194.383000,169684.827000,"Physic")
o.Scale=3.756148
o.Orientation=0.757512,0.646977,0.056603,-0.066274


o=Bladex.CreateEntity("NoName3","Baldosa_01",25395.158000,2267.097000,169922.751000,"Physic")
o.Scale=2.871214
o.Orientation=0.706434,0.707080,0.030844,0.006171


o=Bladex.CreateEntity("NoName4","Baldosa_01",27909.608000,7885.207000,172286.224000,"Physic")
o.Scale=3.047852
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName5","Baldosa_01",32655.305000,2360.448000,178007.442000,"Physic")
o.Scale=5.320970
o.Orientation=0.707080,0.707080,-0.006171,-0.006171


o=Bladex.CreateEntity("NoName6","Baldosa_01",29010.421000,2263.119000,178884.635000,"Physic")
o.Scale=5.819466
o.Orientation=0.666050,0.739724,0.064133,-0.071227


o=Bladex.CreateEntity("NoName7","Baldosa_01",26109.481000,2306.087000,179633.502000,"Physic")
o.Scale=3.908663
o.Orientation=0.703233,0.703233,-0.073913,-0.073913


o=Bladex.CreateEntity("ant55","Antorchaenpared",-20397.981000,14445.962000,101435.832000,"Physic")
o.Scale=1.149474
o.Orientation=0.061628,0.171065,-0.704416,0.686103
o.FiresIntensity=[ 40 ]
o.Lights=[ (0.000000,0.031250,(242,128,0)) ]


o=Bladex.CreateEntity("a3","Antorcha",-21793.250000,10793.252000,75405.798000,"Weapon")
o.Scale=1.000000
o.Orientation=0.315722,0.191458,0.069414,0.926739
o.FiresIntensity=[ 37 ]
o.Lights=[ (0.000000,0.031250,(255,149,32)) ]


o=Bladex.CreateEntity("NoName2","Baldosa_01",-26204.210000,10877.874000,82090.596000,"Physic")
o.Scale=3.017675
o.Orientation=0.719340,0.694658,0.000000,0.000000


o=Bladex.CreateEntity("NoName3","Baldosa_01",-28186.852000,10852.999000,87353.276000,"Physic")
o.Scale=2.814640
o.Orientation=0.737277,0.675590,0.000000,0.000000


o=Bladex.CreateEntity("NoName4","Baldosa_01",-26090.674000,10812.653000,87026.981000,"Physic")
o.Scale=2.497850
o.Orientation=0.736787,0.663406,0.087339,-0.097000


o=Bladex.CreateEntity("NoName0","Varillaancha",-11263.283000,167.862000,206570.315000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName1","Varillaancha",-11281.681000,-659.201000,206612.178000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName2","Varillaancha",-11261.098000,-1493.696000,206623.018000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName3","Varillaancha",-11257.708000,-2353.974000,206576.437000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add


o=Bladex.CreateEntity("NoName0","Adoquinpulsador",105591.548000,-2249.709000,234472.167000,"Physic")
o.Scale=6.623096
o.Orientation=0.517145,0.517145,0.482246,-0.482246
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName1","Adoquinpulsador",105762.754000,-4815.127000,233966.081000,"Physic")
o.Scale=3.538461
o.Orientation=0.508650,0.508650,0.491198,-0.491198
Sparks.SetStoneSparkling(o.Name)


o=Bladex.CreateEntity("NoName0","Baldosa_01",113630.364000,-1057.993000,237412.185000,"Physic")
o.Scale=3.718959
o.Orientation=0.669131,0.743145,0.000000,0.000000


o=Bladex.CreateEntity("NoName1","Baldosa_01",113545.943000,-906.666000,241697.365000,"Physic")
o.Scale=4.865175
o.Orientation=0.732953,0.659954,0.110438,-0.122654


o=Bladex.CreateEntity("NoName0","Piedra_03",16672.332000,7900.918000,172901.291000,"Physic")
o.Scale=0.749342
o.Orientation=0.629701,0.771980,-0.050144,-0.070777


o=Bladex.CreateEntity("NoName1","Piedra_03",13423.687000,8067.927000,177042.613000,"Physic")
o.Scale=0.990099
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName2","Piedra_03",14826.782000,7888.878000,172663.407000,"Physic")
o.Scale=0.772048
o.Orientation=0.611132,0.787440,-0.054332,-0.059185


o=Bladex.CreateEntity("NoName3","Baldosa_01",16136.715000,7919.527000,176180.270000,"Physic")
o.Scale=1.928460
o.Orientation=0.681390,0.681390,0.188966,-0.188966


o=Bladex.CreateEntity("NoName4","Piedra_01",26195.199000,7907.208000,177766.733000,"Physic")
o.Scale=1.072135
o.Orientation=0.983559,-0.098467,0.007690,0.151182


o=Bladex.CreateEntity("NoName5","Femur",17899.489000,7978.925000,176317.623000,"Weapon")
o.Scale=1.000000
o.Orientation=0.048416,-0.047735,0.016077,-0.997556


o=Bladex.CreateEntity("NoName6","Femur",19281.270000,7927.684000,175860.924000,"Weapon")
o.Scale=1.361327
o.Orientation=0.909607,-0.012794,-0.415269,-0.001622


o=Bladex.CreateEntity("NoName7","TinajaPieza4",18473.575000,7940.642000,172226.884000,"Physic")
o.Scale=1.000000
o.Orientation=0.660110,0.365417,-0.655014,0.041008


o=Bladex.CreateEntity("NoName8","TinajaPieza4",21575.908000,8168.747000,174126.626000,"Physic")
o.Scale=1.000000
o.Orientation=0.104528,0.994522,0.000000,0.000000


o=Bladex.CreateEntity("NoName9","TinajaPieza3",15605.728000,7912.045000,172165.256000,"Physic")
o.Scale=1.000000
o.Orientation=0.089995,0.973384,-0.194548,-0.081093


o=Bladex.CreateEntity("NoName0","Antorcha2",55213.354000,-6564.841000,115044.124000,"Physic")
o.Scale=1.000000
o.Orientation=0.609264,0.609264,-0.358884,0.358884
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.131250,(255,140,13)) ]


o=Bladex.CreateEntity("NoName0","Skull",14682.317000,-76.874000,70518.523000,"Weapon")
o.Scale=1.000000
o.Orientation=0.821510,0.323601,0.436805,-0.172062


o=Bladex.CreateEntity("NoName1","Femur",13938.626000,-55.237000,70503.506000,"Weapon")
o.Scale=1.000000
o.Orientation=0.995701,-0.020286,-0.017833,-0.088603


o=Bladex.CreateEntity("NoName2","Femur",13880.719000,-31.071000,70217.911000,"Weapon")
o.Scale=1.000000
o.Orientation=0.017434,0.503916,0.004200,-0.863566


o=Bladex.CreateEntity("NoName3","Femur",14651.235000,-56.966000,69450.494000,"Weapon")
o.Scale=1.000000
o.Orientation=0.974609,-0.011616,-0.221740,-0.028887


o=Bladex.CreateEntity("NoName4","Femur",14912.766000,-54.493000,69715.073000,"Weapon")
o.Scale=1.000000
o.Orientation=0.995708,-0.015774,-0.060434,-0.068291


o=Bladex.CreateEntity("NoName5","Restos",14481.558000,-38.422000,70083.461000,"Physic")
o.Scale=1.000000
o.Orientation=0.470320,0.678438,0.319282,-0.465380


o=Bladex.CreateEntity("NoName6","Flecha",14642.935000,-560.344000,70528.684000)
o.Arrow=1
o.Scale=1.000000
o.Orientation=0.737277,0.675590,0.000000,0.000000


o=Bladex.CreateEntity("NoName7","Flecha",15769.044000,-24.776000,69803.553000)
o.Arrow=1
o.Scale=1.000000
o.Orientation=0.917627,0.037348,0.385109,0.090867


adoq=Bladex.CreateEntity("Adoq1","Adoquinpulsador",20995.694998,-6873.468844,70121.562547,"Physic")
adoq.Scale=4.108044
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq2","Adoquinpulsador",20871.837862,-6972.539955,76373.770535,"Physic")
adoq.Scale=3.987227
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq3","Adoquinpulsador",-83160.451689,-7082.221332,171492.672672,"Physic")
adoq.Scale=4.913826
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

adoq=Bladex.CreateEntity("Adoq4","Adoquinpulsador",-82725.192226,-6717.032591,178160.997193,"Physic")
adoq.Scale=4.067370
adoq.Orientation=0.707107,0.707107,0.000000,0.000000
adoq.CastShadows=0
adoq.Alpha = 0

o=Bladex.CreateEntity("NoName0","Antorchaenpared",37247.427000,-4028.492000,85369.007000,"Physic")
o.Scale=1.000000
o.Orientation=0.705384,0.705384,-0.049325,-0.049325
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.231250,(255,159,53)) ]

o=Bladex.CreateEntity("Adoq1ZonaPul","Adoquinpulsador",-26153.5770825, 6387.48262748, 52673.9611366)
o.Scale=2.5
o.Orientation=0.707107245922, 0.0, -0.707106292248, 0.0
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("Adoq2ZonaPul","Adoquinpulsador",-31073.5770825, 2627.60762748, 53673.9611366)
o.Scale=2.6
o.Orientation=0.698075592518, 0.112654909492, -0.698074638844, -0.112655058503
Sparks.SetStoneSparkling(o.Name)

o=Bladex.CreateEntity("VarillaVent1","Varillaancha",-15250.000000,-500.000000,225750.000000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add

o=Bladex.CreateEntity("VarillaVent2","Varillaancha",-7250.000000,-500.000000,225750.000000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add

o=Bladex.CreateEntity("VarillaVent3","Varillaancha",-15250.000000,250.000000,225750.000000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add

o=Bladex.CreateEntity("VarillaVent4","Varillaancha",-7250.000000,250.000000,225750.000000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name) #Add



# Bloqueadores invisibles con las varillas

o=Bladex.CreateEntity("Varillas12Bloque","Bloque",-15390.000000,-950.000000,226980.000000)
o.Scale=6.055760
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0
o.ExclusionMask=2
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("Varillas34Bloque","Bloque",-7113.440000,-950.000000,226980.000000)
o.Scale=6.055760
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha=0
o.ExclusionMask=2
Reference.EntitiesSelectionData[o.Name]=(0,0,"")
