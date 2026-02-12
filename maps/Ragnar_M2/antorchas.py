##///
##||| Ragnar_M2/antorchas.PY TITANIUM
##||| Change list:
##||| * Shadow pass
##||| * Restored one of the un-used torches near the cosita cave
##\\\ 

import Torchs
import Bladex







"""
o=Bladex.CreateEntity("ant2","Antorcha",-106915.512000,-4183.108000,43149.311000,"Weapon")
o.Scale=1.000000
o.Orientation=0.693330,0.077988,-0.667740,-0.259490
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,20)


o=Bladex.CreateEntity("ant3","Antorcha",-107559.689000,-4091.013000,42710.977000,"Weapon")
o.Scale=1.000000
o.Orientation=0.020347,-0.732396,-0.024843,0.680121
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,20)


o=Bladex.CreateEntity("ant4","Antorcha",-105800.303000,-4098.243000,42388.118000,"Weapon")
o.Scale=1.000000
o.Orientation=0.449242,0.527759,-0.359646,-0.624745
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,20)


o=Bladex.CreateEntity("ant5","Antorcha",-106220.117000,-4072.446000,43082.742000,"Weapon")
o.Scale=1.000000
o.Orientation=0.999667,0.025579,0.002552,-0.002189
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,20)

o=Bladex.CreateEntity("ant6","Antorcha",-106494.817000,-2838.836000,39355.015000,"Weapon")
o.Scale=1.000000
o.Orientation=0.817998,0.203219,-0.401802,-0.357962
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,20)
"""

o=Bladex.CreateEntity("ant7","Antorcha",-107133.931000,-2829.959000,39620.375000,"Weapon")
o.Scale=1.000000
o.Orientation=0.463919,0.392803,0.202350,0.767815
o.FiresIntensity=[ 46 ]
o.Lights=[ (0.000000,0.031250,(255,170,30)) ]
Torchs.SetUsable(o.Name,3,3,-1)




#######en pared########


o=Bladex.CreateEntity("ap1","Antorchaenpared",-81028.835000,-319.009000,75595.781000,"Physic")
o.Scale=1.000000
o.Orientation=0.706138,0.706138,-0.037007,-0.037007
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap2","Antorchaenpared",-102367.209000,-14123.199000,35026.557000,"Physic")
o.Scale=1.196147
o.Orientation=0.553388,0.553388,-0.440184,0.440184
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.031250,(255,165,13)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap3","Antorchaenpared",-121736.368000,531.057000,48256.761000,"Physic")
o.Scale=1.072135
o.Orientation=0.006170,0.030844,-0.707080,0.706434
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.031250,(255,141,15)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap4","Antorchaenpared",-74652.420000,7318.144000,72777.026000,"Physic")
o.Scale=1.072135
o.Orientation=0.449775,0.430459,0.545621,-0.560986
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.131250,(255,156,47)) ]
Torchs.SetUsable(o.Name,3,3,-1)

""" ### PLAGUE: Kinda nice, but also makes the room too busy with lights. Not worth it.
o=Bladex.CreateEntity("ap5","Antorchaenpared",-73605.876000,-9195.945000,71187.262000,"Physic")
#o.Static=1
o.Scale=1.257163
o.Orientation=0.092296,0.116706,-0.701057,0.697409
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,165,64)) ]
Torchs.SetUsable(o.Name,3,3,-1)
"""

o=Bladex.CreateEntity("ap6","Antorchaenpared",-85800.617000,-8834.057000,63954.203000,"Physic")
o.Scale=1.000000
o.Orientation=0.517145,0.525483,-0.482245,0.473146
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,193,66)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap8","Antorchaenpared",-98052.975000,374.974000,-35609.521000,"Physic")
o.Scale=1.000000
o.Orientation=0.706676,0.706676,-0.024678,-0.024678
o.FiresIntensity=[ 3 ]
o.Lights=[ (15.000000,0.070000,(255,159,53)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap9","Antorchaenpared",-97118.373000,-10881.985000,-52158.644000,"Physic")
o.Scale=1.000000
o.Orientation=0.670566,0.648460,0.224368,-0.281958
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.070000,(255,163,60)) ]

Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap10","Antorchaenpared",-115696.029000,-10328.003000,-54798.907000,"Physic")
o.Scale=1.000000
o.Orientation=0.626817,0.637800,-0.340334,0.290662
o.FiresIntensity=[ 3 ]
o.Lights=[ (6.800000,0.312500,(255,223,74)) ]       # Changed
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap11","Antorchaenpared",-85967.692000,3735.975000,-78226.408000,"Physic")
o.Scale=1.000000
o.Orientation=0.012593,-0.001125,0.682263,-0.730997
o.FiresIntensity=[ 3 ]
o.Lights=[ (3.000000,0.031250,(173,245,254)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap12","Antorchaenpared",-108315.891000,4354.005000,-95470.229000,"Physic")
o.Scale=1.000000
o.Orientation=0.521334,0.449775,0.477714,-0.545621
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.070000,(253,114,0)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap13","Antorchaenpared",-99877.745000,4196.642000,-100820.792000,"Physic")
o.Scale=1.082857
o.Orientation=0.540143,0.599805,-0.490709,0.328154
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.070000,(236,124,0)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap14","Antorchaenpared",-91690.580496,395.080810,-96112.805885,"Physic")
o.Scale=1.000000
o.Orientation=0.006171,-0.104517,0.707080,-0.699340
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.131250,(255,166,68)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap15","Antorchaenpared",-81935.220000,4644.892000,-103256.476000,"Physic")
o.Scale=1.000000
o.Orientation=0.049324,0.122788,-0.705384,0.696364
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,142,17)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("ap16","Antorchaenpared",-129440.268000,-6269.548000,-38959.218000,"Physic")
o.Scale=1.000000
o.Orientation=0.073913,0.122788,-0.703233,0.696364
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(244,129,0)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap17","Antorchaenpared",-90042.917000,-349.398000,-96207.371000,"Physic")
o.Scale=1.000000
o.Orientation=0.706434,0.706434,-0.030844,-0.030844
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,157,49)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap18","Antorchaenpared",-81951.118000,-238.027000,-103674.925000,"Physic")
o.Scale=1.000000
o.Orientation=0.012340,0.049326,-0.706999,0.705384
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable(o.Name,3,3,-1)

# Restored unused torch, but made it unlit at first.    -LeadHead
o=Bladex.CreateEntity("ap19","Antorchaenpared",-143810.756000,6361.342000,31323.698000,"Physic")
o.Scale=1.000000
o.Orientation=0.586218,0.572061,0.395409,-0.415627
o.FiresIntensity=[ 25 ]
o.Lights=[ (0.000000,0.031250,(255,139,11)) ]
Torchs.SetUsable(o.Name,7,3,-1)


o=Bladex.CreateEntity("ap20","Antorchaenpared",-129066.790557,4404.970562,27951.896519,"Physic")
o.Scale=1.000000
o.Orientation=0.463904,0.508650,-0.533660,0.491198
o.FiresIntensity=[ 22 ]
o.Lights=[ (0.000000,0.080000,(255,160,20)) ]
Torchs.SetUsable(o.Name,10,3,-1)


o=Bladex.CreateEntity("ap21","Antorchaenpared",-117720.945000,-8844.599000,-9987.684000,"Physic")
o.Scale=1.000000
o.Orientation=0.504344,0.504344,-0.495618,0.495618
o.FiresIntensity=[ 0 ]
o.Lights=[ (30.000000,0.131250,(255,158,51)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap22","Antorchaenpared",-119220.132241,-13327.747202,42010.816356,"Physic")
o.Scale=1.000000
o.Orientation=0.043168,-0.055479,0.705788,-0.704927
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.131250,(255,153,40)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap23","Antorchaenpared",-146723.452000,15449.711000,72151.397000,"Physic")
o.Scale=1.000000
o.Orientation=0.618450,0.564721,0.342812,-0.425547
o.FiresIntensity=[ 0 ]
o.Lights=[ (30.000000,0.231250,(255,155,45)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap24","Antorchaenpared",-115273.724000,12175.135000,82479.923000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.131250,(255,150,34)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap25","Antorchaenpared",-113992.491000,7958.255000,58783.649000,"Physic")
o.Scale=1.000000
o.Orientation=0.482246,0.463904,0.517145,-0.533660
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.131250,(255,141,15)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap26","Antorchaenpared",-107716.752126,3153.968058,43524.911589,"Physic")
o.Scale=1.0
o.Orientation=0.086175,0.206738,-0.701836,0.676210
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.131250,(255,138,9)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap27","Antorchaenpared",-92288.859775,1959.966526,53368.533868,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (17.000000,0.10,(255,151,36)) ]      # Changed
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap28","Antorchaenpared",-127311.054000,7839.942000,52389.967000,"Physic")
o.Scale=1.000000
o.Orientation=0.706138,0.706138,-0.037007,-0.037007
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.031250,(255,137,6)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("ap29","Antorchaenpared",-115278.472000,7514.992000,73545.487000,"Physic")
o.Scale=1.000000
o.Orientation=0.707080,0.707080,0.006171,-0.006171
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.131250,(244,129,0)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("ap30","Antorchaenpared",-81290.038000,-4238.538000,25326.263000,"Physic")
o.Scale=1.000000
o.Orientation=0.473147,0.395409,0.525483,-0.586218
o.FiresIntensity=[ 3 ]                          #   Changed
o.Lights=[ (5.000000,0.100000,(255,156,47)) ]   #
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap31","Antorchaenpared",-97525.116000,7162.596000,77213.303000,"Physic")
o.Scale=1.000000
o.Orientation=0.553388,0.553388,-0.440184,0.440184
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.031250,(255,165,66)) ]
Torchs.SetUsable(o.Name,3,3,-1)




o=Bladex.CreateEntity("ap32","Antorchaenpared",-92811.447000,7343.724000,77215.973000,"Physic")
o.Scale=1.000000
o.Orientation=0.529592,0.560986,-0.468543,0.430459
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.131250,(255,158,51)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap33","Antorchaenpared",-108044.112000,-4303.996000,40248.424000,"Physic")
o.Scale=1.000000
o.Orientation=0.706999,0.706999,-0.012341,-0.012341
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.031250,(255,137,6)) ]
Torchs.SetUsable(o.Name,3,3,-1)



o=Bladex.CreateEntity("ap335","Antorchaenpared",-130014.019000,-6696.609000,32959.205000,"Physic")
o.Scale=1.000000
o.Orientation=0.553388,0.553388,-0.440184,0.440184
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.21250,(249,140,43)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("ap336","Antorchaenpared",-98210.950000,5998.029000,-91036.873000,"Physic")
o.Scale=1.000000
o.Orientation=0.440184,0.560986,-0.553388,0.430459
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.031250,(255,138,9)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("ap337","Antorchaenpared",-85474.957000,5533.575000,-100556.582000,"Physic")
o.Scale=1.000000
o.Orientation=0.459229,0.504344,-0.537688,0.495618
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.031250,(255,145,21)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("ap33434","Antorchaenpared",-116938.233711, -3889.25989102, 34372.4423,"Physic")
o.Scale=1.000000
o.Orientation=0.553388,0.553388,-0.440184,0.440184
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.21250,(249,140,43)) ]
Torchs.SetUsable(o.Name,3,3,-1)

##############antorcha en los subterraneos del canalillo

o=Bladex.CreateEntity("ap338","Antorchaenpared",-75203.511630,16839.892122,67107.353123,"Physic")
o.Scale=1.000000
o.Orientation=0.043168,0.104517,-0.705788,0.699340
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.031250,(255,138,10)) ]
Torchs.SetUsable(o.Name,3,3,-1)

######en el suelo#######

o=Bladex.CreateEntity("ant4593","Antorcha",-154690.403000,14146.757000,46102.324000,"Weapon")
o.Scale=1.000000
o.Orientation=0.999048,0.043619,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.031250,(255,160,55)) ]
Torchs.SetUsable(o.Name,3,3,-1)

########lamparedes########

o=Bladex.CreateEntity("l1","Lampared",-123429.638000,-7873.764000,46523.197000,"Physic")
o.Scale=1.000000
o.Orientation=0.006164,0.006171,0.707080,-0.707080
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.081250,(255,157,49)) ]
Torchs.SetUsable(o.Name,3,3,-1)


o=Bladex.CreateEntity("l2","Lampared",-132226.383000,-7505.307000,52610.285000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,139,11)) ]
Torchs.SetUsable(o.Name,3,3,-1)

o=Bladex.CreateEntity("l3","Lampared",-78775.404000,-7399.442000,59650.859000,"Physic")
o.Scale=1.000000
o.Orientation=0.491198,0.491198,0.508650,-0.508650
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,168,72)) ]
Torchs.SetUsable("l3",3,3,-1)

o=Bladex.CreateEntity("l4","Lampared",-110292.816000,-87.687000,-35483.085000,"Physic")
o.Scale=1.072135
o.Orientation=0.504344,0.504344,0.495618,-0.495618
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable("l4",3,3,-1)

o=Bladex.CreateEntity("l5","Lampared",-134017.883997,-7347.541000,-90029.277000,"Physic")
o.Scale=1.000000
o.Orientation=0.493854,0.493854,0.506071,-0.506071
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.31250,(255,156,47)) ]
Torchs.SetUsable("l5",3,3,-1)

o=Bladex.CreateEntity("l6","Lampared",-135357.169000,-13973.665000,-86522.172000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.331250,(255,151,36)) ]
Torchs.SetUsable("l6",3,3,-1)

o=Bladex.CreateEntity("l7","Lampared",-121772.251000,-14164.101000,-88406.155000,"Physic")
o.Scale=1.000000
o.Orientation=0.517145,0.517145,0.482246,-0.482246
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.131250,(255,162,57)) ]
Torchs.SetUsable("l7",3,3,-1)

o=Bladex.CreateEntity("l8","Lampared",-132731.414000,-7608.831000,-93254.495000,"Physic")
o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491197,0.491197
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable("l8",3,3,-1)

o=Bladex.CreateEntity("l9","Lampared",-132722.835000,-13590.081000,-92104.389000,"Physic")
o.Scale=1.000000
o.Orientation=0.486893,0.504192,-0.495465,0.513069
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.031250,(255,153,40)) ]
Torchs.SetUsable("l9",3,3,-1)

o=Bladex.CreateEntity("l10","Lampared",-133645.588000,-19171.151000,-91275.070000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable("l10",3,3,-1)

o=Bladex.CreateEntity("l11","Lampared",-136297.583000,-23906.559000,-91777.584000,"Physic")
o.Scale=1.000000
o.Orientation=0.694658,0.719340,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (7.000000,0.031250,(255,196,128)) ]
Torchs.SetUsable("l11",3,3,-1)

o=Bladex.CreateEntity("l12","Lampared",-80030.703999,-201.146000,-31954.641000,"Physic")
o.Scale=1.000000
o.Orientation=0.487269,0.477170,0.522532,-0.511701
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(255,151,36)) ]
Torchs.SetUsable("l12",3,3,-1)
""" ### Don't know why this torch was comented out, but it doesnt really fit, so prob just leave it
o=Bladex.CreateEntity("l13","Lampared",-81024.802000,-9504.065000,-976.191000,"Physic")
o.Scale=1.000000
o.Orientation=0.030844,0.030844,0.706434,-0.706434
o.FiresIntensity=[ 3 ]
o.Lights=[ (5.000000,0.060000,(255,149,32)) ]
Torchs.SetUsable("l13",3,3,-1)
"""
o=Bladex.CreateEntity("l14","Lampared",-67220.449093,-303.531925,73958.842973,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,-0.521334,0.521334
o.FiresIntensity=[ 3 ]
o.Lights=[ (20.000000,0.131250,(255,148,30)) ]
Torchs.SetUsable("l14",3,3,-1)

o=Bladex.CreateEntity("l15","Lampared",-143728.672000,-30612.908000,-90098.175000,"Physic")
o.Scale=1.000000
o.Orientation=0.512917,0.512917,-0.486740,0.486740
o.FiresIntensity=[ 3 ]
o.Lights=[ (10.000000,0.031250,(244,129,0)) ]
Torchs.SetUsable("l15",3,3,-1)

o=Bladex.CreateEntity("l16","Lampared",-139778.702000,-13255.034000,-107783.240000,"Physic")
o.Scale=1.000000
o.Orientation=0.491274,0.499924,0.499924,-0.508726
o.FiresIntensity=[ 0 ]
o.Lights=[ (10.000000,0.100000,(255,196,128)) ]     # Change
Torchs.SetUsable("l16",3,3,-1)


######baja a las mazmorras#########
######arroja luz
o=Bladex.CreateEntity("antmaz","Antorchaenpared",-69988.794397,-8236.588783,72929.619026,"Physic")
o.Scale=1.000000
o.Orientation=0.463219,0.548537,-0.542360,0.436326
o.FiresIntensity=[ 0 ]
o.Lights=[ (15.000000,0.031250,(255,138,9)) ]
Torchs.SetUsable("antmaz",3,3,-1)

######Sala de las dos puertas
######

o=Bladex.CreateEntity("dosp","Antorchaenpared",-75580.986374,-9761.619397,63936.650652,"Physic")
o.Scale=1.000000
o.Orientation=0.459229,0.545621,-0.537688,0.449775
o.FiresIntensity=[ 0 ]
o.Lights=[ (8.000000,0.031250,(255,140,13)) ]
Torchs.SetUsable("dosp",3,3,-1)


o=Bladex.CreateEntity("NoName0","Antorcha2",-137883.348000,-33086.790000,-89840.292000,"Physic")
o.Scale=1.000000
o.Orientation=0.638224,0.638224,-0.304417,0.304417
o.FiresIntensity=[ 0 ]
o.Lights=[ (25.000000,0.9,(225,118,0)) ]


############################################

ApagalaSec = Bladex.GetSector(-129236.271992, 3749.67144786, 41636.75887)
ApagalaSec.OnEnter = Apagala

############################################


ApagalaSec2 = Bladex.GetSector(-77210.0465377, -7869.66067668, 72284.624)
ApagalaSec2.OnEnter = Apagala2

############################################

ApagalaSec3 = Bladex.GetSector(-80302.3691273, -3850.7562537, 13446.10073)
ApagalaSec3.OnEnter = Apagala3


































































