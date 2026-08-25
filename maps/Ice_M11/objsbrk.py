##///
##||| Ice_M11/objsbrk.PY TITANIUM
##||| Change list:
##||| * Sparkpass
##\\\ 

import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac

####barril en la sala del minot

o=Bladex.CreateEntity("minba1","Barril",70779.801460,-394.515081,13773.644061,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("minba1",12,100)
Actions.SetBurnable("minba1",BoxBurnTime,BoxDestroyTime)

####cofres en la sala de la armadura

o=Bladex.CreateEntity("cofarma1","Cofre",14620.473000,-8441.317000,57399.280000,"Physic")
o.Scale=0.787566
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofarma1",12,100)
Actions.SetBurnable("cofarma1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("cofarma2","Cofre",14568.272000,-8435.270000,54845.583000,"Physic")
o.Scale=0.787566
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofarma2",12,100)
Actions.SetBurnable("cofarma2",BoxBurnTime,BoxDestroyTime)

####enric-barriles

o=Bladex.CreateEntity("EnricBarril1","Barril",101032.887202,-5624.240997,44974.539124,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("EnricBarril1",12,100)
Actions.SetBurnable("EnricBarril1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("EnricBarril2","Barril",101734.986510,-5828.513552,44187.085881,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("EnricBarril2",12,100)
Actions.SetBurnable("EnricBarril2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("EnricBarril3","Barril",101401.696765,-5563.890081,26634.164865,"Physic")
o.Scale=1.172579
o.Orientation=0.630370,-0.014216,-0.005160,0.776148
Breakings.SetBreakable("EnricBarril3",12,100)
Actions.SetBurnable("EnricBarril3",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("EnricBarril4","Barril",100416.152882,-5752.429507,26326.767383,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("EnricBarril4",12,100)
Actions.SetBurnable("EnricBarril4",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("enricpan0", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("enricpan0")
Breakings.SetBreakable("EnricBarril4",12,100,"enricpan0")
Actions.SetBurnable("EnricBarril4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("EnricBarril5","Barril",100594.365456,-5622.157484,27228.487971,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("enricpan1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("enricpan1")
Breakings.SetBreakable("EnricBarril5",12,100,"enricpan1")
Actions.SetBurnable("EnricBarril5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("EnricBarril6","Barril",101445.596953,-5735.305860,27761.225014,"Physic")
o.Scale=1.257163
o.Orientation=0.708184,0.704225,-0.037698,0.033488
pan=Breakings.CreateHiddenObject("enricpan2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("enricpan2")
Breakings.SetBreakable("EnricBarril6",12,100,"enricpan2")
Actions.SetBurnable("EnricBarril6",BoxBurnTime,BoxDestroyTime)


############BARRILES Y CAJAS A UN LADO DEL PUENTE LEVADIZO

o=Bladex.CreateEntity("CAJent1","Barril",-33521.817231,9072.546587,65966.397684,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan2")
Breakings.SetBreakable("CAJent1",12,100,"pan2")
Actions.SetBurnable("CAJent1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent2","Barril",-32136.981858,8708.205342,64823.902439,"Physic")
o.Scale=1.890462
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan1", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan1")
Breakings.SetBreakable("CAJent2",12,100,"pan1")
Actions.SetBurnable("CAJent2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent3","Barril",-32974.162094,9009.288453,63964.268508,"Physic")
o.Scale=1.612226
o.Orientation=0.918720,-0.064756,-0.343267,0.184195
Breakings.SetBreakable("CAJent3",12,100)
Actions.SetBurnable("CAJent3",BoxBurnTime,BoxDestroyTime)

""" ### --- Unused stuff, taken from Ice_back --- ###
o=Bladex.CreateEntity("CAJent4","Barril",-31037.046448,10578.127858,60205.287397,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan3")
Breakings.SetBreakable("CAJent4",12,100,"pan3")
Actions.SetBurnable("CAJent4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent5","Barril",-31475.401274,10595.802564,59051.829386,"Physic")
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent5",12,100)
Actions.SetBurnable("CAJent5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent6","Cajon2",-31233.847245,10416.007401,62246.688631,"Physic")
o.Scale=1.321291
o.Orientation=0.473147,0.473147,0.525483,-0.525483
Breakings.SetBreakable("CAJent6",12,100)
Actions.SetBurnable("CAJent6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent7","Cajon2",-24541.575429,10598.139727,60468.231202,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent7",12,100)
Actions.SetBurnable("CAJent7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent8","Barril",-24276.005962,10675.896798,59265.270943,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent8",12,100)
Actions.SetBurnable("CAJent8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent9","Barril",-29379.254819,10804.283898,64576.437615,"Physic")
o.Scale=1.257163
o.Orientation=0.880911,0.104158,-0.419216,-0.193400
Breakings.SetBreakable("CAJent9",12,100)
Actions.SetBurnable("CAJent9",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent10","Barril",-25485.398227,10682.379538,59050.705134,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent10",12,100)
Actions.SetBurnable("CAJent10",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent11","Cajon2",-30618.786909,946.891796,59595.566375,"Physic")
o.Scale=1.093685
o.Orientation=0.688128,0.689795,-0.158938,0.159375
Breakings.SetBreakable("CAJent11",12,100)
Actions.SetBurnable("CAJent11",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("CAJent12","Cajon2",-28285.854982,1075.859171,59683.517175,"Physic")
o.Scale=0.869963
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("ques113", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques113")
Breakings.SetBreakable("CAJent12",12,100,"ques113")
Actions.SetBurnable("CAJent12",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent13","Barril",-26794.090516,1088.609621,59294.340115,"Physic")
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent13",12,100)
Actions.SetBurnable("CAJent13",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent14","Barril",-30593.588420,1008.728978,62250.784470,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent14",12,100)
Actions.SetBurnable("CAJent14",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent15","Barril",-31094.835042,1042.480462,63370.826295,"Physic")
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent15",12,100)
Actions.SetBurnable("CAJent15",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent16","Barril",-29984.763901,1034.584045,63486.139094,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJent16",12,100)
Actions.SetBurnable("CAJent16",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJent17","Barril",-30807.722596,958.962328,64855.817825,"Physic")
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("ques111", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques111")
Breakings.SetBreakable("CAJent17",12,100,"ques111")
Actions.SetBurnable("CAJent17",BoxBurnTime,BoxDestroyTime)
"""





###BARRILES Y CAJAS MAZMORRAS



o=Bladex.CreateEntity("CAJEST0","Cajon2",84000.562155,-799.236216,-23055.849129,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan333", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan333")
Breakings.SetBreakable("CAJEST0",12,100,"pan333")
Actions.SetBurnable("CAJEST0",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CAJEST1","Cajon2",82923.930000,-771.249000,-25388.859000,"Physic")
o.Scale=1.295256
o.Orientation=0.645974,0.645974,0.287606,-0.287606
pan=Breakings.CreateHiddenObject("pan334", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan334")
Breakings.SetBreakable("CAJEST1",12,100,"pan334")
Actions.SetBurnable("CAJEST1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CAJEST2","Cajon2",82813.560000,-2033.044000,-25034.374000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJEST2",12,100)
Actions.SetBurnable("CAJEST2",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("BAREST3","Barril",83330.896000,-686.021000,-28277.865000,"Physic")
o.Scale=1.628348
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panobst3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panobst3")
Breakings.SetBreakable("BAREST3",12,100,"BAREST3")
Actions.SetBurnable("BAREST3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST4","Barril",84328.520000,-653.631000,-28978.815000,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST4",12,100)
Actions.SetBurnable("BAREST4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST5","Barril",84412.410000,-604.400000,-27816.763000,"Physic")
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST5",12,100)
Actions.SetBurnable("BAREST5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST6","Barril",85909.689000,-565.266000,-29002.676000,"Physic")
o.Scale=1.334504
o.Orientation=0.704746,0.709426,0.003960,-0.005693
Breakings.SetBreakable("BAREST6",12,100)
Actions.SetBurnable("BAREST6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST7","Barril",96418.310000,-699.344000,-23110.348000,"Physic")
o.Scale=1.661078
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST7",12,100)
Actions.SetBurnable("BAREST7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST8","Barril",96752.109000,-669.411000,-21670.708000,"Physic")
o.Scale=1.596263
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST8",12,100)
Actions.SetBurnable("BAREST8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST9","Barril",96615.703000,-731.944000,-20469.225000,"Physic")
o.Scale=1.745810
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST9",12,100)
Actions.SetBurnable("BAREST9",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST10","Barril",95184.912000,-632.634000,-21499.286000,"Physic")
o.Scale=1.503752
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST10",12,100)
Actions.SetBurnable("BAREST10",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST11","Barril",94389.593000,-552.219000,-20366.790000,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST11",12,100)
Actions.SetBurnable("BAREST11",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST12","Barril",95453.571000,-422.899000,-20615.160000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST12",12,100)
Actions.SetBurnable("BAREST12",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST13","Barril",82542.671000,-694.772000,-29667.971000,"Physic")
o.Scale=1.644632
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BAREST13",12,100)
Actions.SetBurnable("BAREST13",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BAREST14","Barril",83387.880000,-1357.039000,-29129.609000,"Physic")
o.Scale=1.402577
o.Orientation=0.850842,0.299552,0.388736,0.187672
Breakings.SetBreakable("BAREST14",12,100)
Actions.SetBurnable("BAREST14",BoxBurnTime,BoxDestroyTime)





##############BARRILES Y CAJAS DEL SEGUNDO GRANERO, DONDE ESTA UN MINOT. ENCERRADO

o=Bladex.CreateEntity("cajmin0","Cajon2",56279.004000,-717.171000,13331.997000,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cajmin0",12,100)
Actions.SetBurnable("cajmin0",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("cajmin1","Cajon2",56731.295000,-2114.133000,13424.982000,"Physic")
o.Scale=1.000000
o.Orientation=0.688984,0.688984,0.159064,-0.159064
Breakings.SetBreakable("cajmin1",12,100)
Actions.SetBurnable("cajmin1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("cajnr9","Caja_i_i",56511.639000,-671.373000,18351.012000,"Physic")
o.Scale=2.047099
o.Orientation=0.695266,0.695266,0.128860,-0.128860
Sparks.SetMetalSparkling(o.Name)                            # Add
# Actions.SetBurnable("cajnr9",BoxBurnTime,BoxDestroyTime)  #


o=Bladex.CreateEntity("barmin10","Barril",56579.737000,-1968.679000,17789.487000,"Physic")
o.Scale=1.728525
o.Orientation=0.706805,0.704948,-0.039979,0.043329
Breakings.SetBreakable("barmin10",12,100)
Actions.SetBurnable("barmin10",BoxBurnTime,BoxDestroyTime)

########################
########GRANERO DE LAS VIGAS########
###################
############################
########
o=Bladex.CreateEntity("BARVIG1","Cajon2",71016.320864,-600.316442,-31754.465470,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin18", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin18")
Breakings.SetBreakable("BARVIG1",12,100,"panfin18")
Actions.SetBurnable("BARVIG1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG2","Cajon2",71287.389808,-525.754027,-30124.323037,"Physic")
o.Scale=0.869963
o.Orientation=0.643440,0.643440,0.293232,-0.293232
pan=Breakings.CreateHiddenObject("panarac1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac1")
Breakings.SetBreakable("BARVIG2",12,100,"panarac1")
Actions.SetBurnable("BARVIG2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG3","Barril",70087.182305,-410.922293,-30291.504132,"Physic")
o.Scale=1.000000
o.Orientation=0.707386,0.706827,0.000901,-0.000785
Breakings.SetBreakable("BARVIG3",12,100)
Actions.SetBurnable("BARVIG3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG4","Barril",69390.636160,-425.675356,-30748.303854,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panarac2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac2")
Breakings.SetBreakable("BARVIG4",12,100,"panarac2")
Actions.SetBurnable("BARVIG4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG5","Barril",71660.441371,-326.781095,-28273.516982,"Physic")
o.Scale=1.000000
o.Orientation=0.985720,0.024313,0.008946,0.166385
Breakings.SetBreakable("BARVIG5",12,100)
Actions.SetBurnable("BARVIG5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG6","Barril",72823.432577,-310.369617,-28427.423157,"Physic")
o.Scale=1.000000
o.Orientation=0.856242,-0.090242,-0.479821,0.168757
Breakings.SetBreakable("BARVIG6",12,100)
Actions.SetBurnable("BARVIG6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG7","Barril",75510.785455,-465.424366,-28164.294335,"Physic")
o.Scale=1.093685
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG7",12,100)
Actions.SetBurnable("BARVIG7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG8","Barril",75428.469934,-468.790232,-29029.102094,"Physic")
o.Scale=1.104622
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG8",12,100)
Actions.SetBurnable("BARVIG8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG9","Barril",74711.260982,-488.369485,-28487.130247,"Physic")
o.Scale=1.149474
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG9",12,100)
Actions.SetBurnable("BARVIG9",BoxBurnTime,BoxDestroyTime)


###############################
#########cofres del patio antes cementerio
####################

o=Bladex.CreateEntity("cofc3","Cofre",9652.557578,-555.561321,56065.246725,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("cofc3",12,100)
Actions.SetBurnable("cofc3",BoxBurnTime,BoxDestroyTime)

###################
#####sala de las vidrieras
##############

o=Bladex.CreateEntity("cofv1","Cofre",-10982.302669,2194.958436,27161.795975,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o=Breakings.CreateHiddenObject("icepocimaCOFV1", "PocimaTodo",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
o.Solid=1
pocimac.CreatePotion("icepocimaCOFV1")
Breakings.SetBreakable("cofv1",12,100,"icepocimaCOFV1")
Actions.SetBurnable("cofv1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("cofv2","Cofre",-12292.665805,2197.344853,31712.023962,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofv2",12,100)
Actions.SetBurnable("cofv2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("cofv3","Cofre",-11776.935014,2200.728498,36979.430093,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cofv3",12,100)
Actions.SetBurnable("cofv3",BoxBurnTime,BoxDestroyTime)

################
######ARMEROS####
################
"""
Breakings.SetBreakable("ARM1",12,100)
Breakings.SetBreakable("ARM2",12,100)
Breakings.SetBreakable("ARM3",12,100)
Breakings.SetBreakable("ARM4",12,100)
Breakings.SetBreakable("ARM5",12,100)
Breakings.SetBreakable("ARM6",12,100)
"""
o=Bladex.CreateEntity("gar3","Barril",5337.557000,-598.885000,115875.601000,"Physic")
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("gar3",12,100)
Actions.SetBurnable("gar3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("gar2","Barril",5414.639000,-517.741000,114387.070000,"Physic")
o.Scale=1.232392
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("gar2",12,100)
Actions.SetBurnable("gar2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("gar1","Barril",3884.047000,-577.152000,115758.708000,"Physic")
o.Scale=1.890462
o.Orientation=0.944138,0.053535,-0.261028,-0.193913
Breakings.SetBreakable("gar1",12,100)
Actions.SetBurnable("gar1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("barro2","Barril",49369.570000,-3449.245000,68052.232000,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("barro2",12,100)
Actions.SetBurnable("barro2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("barro1","Barril",50543.228000,-1595.880000,69722.994000,"Physic")
o.Scale=1.564811
o.Orientation=0.893625,0.091475,-0.376540,-0.226461
Breakings.SetBreakable("barro1",12,100)
Actions.SetBurnable("barro1",BoxBurnTime,BoxDestroyTime)