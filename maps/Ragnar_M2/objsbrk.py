##///
##||| Ragnar_M2/objsbrk.PY TITANIUM
##||| Change list:
##||| * spark pass
##||| * Eclipse no longer stuck in floor
##||| * Some chest orientation swapped
##\\\ 

import Breakings
import Actions
import Bladex
import Torchs
import pocimac
import Reference
import MenuText


BoxBurnTime = 6
BoxDestroyTime = 12


############Caja que se quema en el NBurning

### Funcion: QuemaLaDichosaCajita(ObjectName,use_from)

cajapatard=Bladex.CreateEntity("Burning","Caja_i_r",-88281.125713,-4945.727844,17929.830733)
cajapatard.Scale=1.374941
cajapatard.Orientation=0.548983,0.445137,-0.446649,-0.548613
Reference.EntitiesSelectionData[cajapatard.Name]=(8.0,6000.0,MenuText.GetMenuText("Box"))
Actions.SetBurnable("Burning",BoxBurnTime,BoxDestroyTime)
cajapatard.UseFunc=QuemaLaDichosaCajita



############BARRILES Y CAJAS A UN LADO DEL PUENTE LEVADIZO


###BARRILES Y CAJAS MAZMORRAS

o=Bladex.CreateEntity("BarrMaz1","Barril",-116324.080047,8433.070452,72368.935912,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrMaz1",12,100)
Actions.SetBurnable("BarrMaz1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("BarrMaz2","Barril",-116370.659703,8482.438734,71526.638382,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrMaz2",12,100)
Actions.SetBurnable("BarrMaz2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrMaz3","Barril",-115414.595660,8629.243894,71676.382551,"Physic")
o.Scale=1.282432
o.Orientation=0.100731,0.855638,0.169887,0.478409

Breakings.SetBreakable("BarrMaz3",12,100)
Actions.SetBurnable("BarrMaz3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrMaz4","Barril",-114742.720864,8346.808377,64717.930371,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
panmaz4=Breakings.CreateHiddenObject("Panmaz4", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
panmaz4.Solid=1
pocimac.CreateFood("Panmaz4")
Breakings.SetBreakable("BarrMaz4",12,100,"Panmaz4")
Actions.SetBurnable("BarrMaz4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrMaz5","Barril",-115134.757479,7352.576234,64335.596966,"Physic")
o.Scale=1.000000
o.Orientation=0.558766,0.576360,-0.540898,0.251037
Breakings.SetBreakable("BarrMaz5",12,100)
Actions.SetBurnable("BarrMaz5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrMaz6","Barril",-80695.983101,8478.999150,83925.689826,"Physic")
o.Scale=1.232392
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pan1")
Breakings.SetBreakable("BarrMaz6",12,100,"pan1")
Actions.SetBurnable("BarrMaz6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrMaz7","Barril",-81583.487721,8459.061191,84447.803108,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pan2")
Breakings.SetBreakable("BarrMaz7",12,100,"pan2")
Actions.SetBurnable("BarrMaz7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrMaz8","Barril",-81674.576831,8478.307766,83251.769551,"Physic")
o.Scale=1.232392
o.Orientation=0.706924,0.707226,-0.006482,0.006936
Breakings.SetBreakable("BarrMaz8",12,100)
Actions.SetBurnable("BarrMaz8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajMaz1","Cajon2",-76064.733685,8403.422588,77641.017109,"Physic")
o.Scale=1.000000
o.Orientation=0.708215,0.705906,0.007917,-0.008118
Breakings.SetBreakable("CajMaz1",12,100)
Actions.SetBurnable("CajMaz1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajMaz2","Cajon2",-75721.227159,8575.537354,78836.074885,"Physic")
o.Scale=0.705914
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("CajMaz2",12,100)
Actions.SetBurnable("CajMaz2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajMaz3","Cajon2",-77160.111054,8491.176006,79247.911958,"Physic")
o.Scale=0.844377
o.Orientation=0.298836,0.298836,-0.640856,0.640856
Breakings.SetBreakable("CajMaz3",12,100)
Actions.SetBurnable("CajMaz3",BoxBurnTime,BoxDestroyTime)


##6 BARRILES Y 4 CAJAS EN SALIDA DE CLOACAS


o=Bladex.CreateEntity("CajaCl1","Cajon2",-130918.332526,1708.375940,54420.404875,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pancl1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pancl1")
Breakings.SetBreakable("CajaCl1",12,100,"pancl1")
Actions.SetBurnable("CajaCl1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajaCl2","Cajon2",-130927.136142,476.131621,53756.857140,"Physic")
o.Scale=1.000000
o.Orientation=0.003064,0.914433,-0.000055,-0.404725
Breakings.SetBreakable("CajaCl2",12,100)
Actions.SetBurnable("CajaCl2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajaCl3","Cajon2",-127947.937332,1710.978828,54344.217635,"Physic")
o.Scale=1.321291
o.Orientation=0.212631,0.212631,-0.674380,0.674380
Breakings.SetBreakable("CajaCl3",12,100)
Actions.SetBurnable("CajaCl3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCl1","Barril",-122485.291362,1793.433810,47283.391556,"Physic")
o.Scale=1.677689
o.Orientation=0.707691,0.706305,0.010762,-0.013827
queso=Breakings.CreateHiddenObject("queso1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
pocimac.CreateFood("queso1")
Breakings.SetBreakable("BarrCl1",12,100,"queso1")
Actions.SetBurnable("BarrCl1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCl2","Barril",-123727.258601,1931.257734,47202.698527,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCl2",12,100)
Actions.SetBurnable("BarrCl2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCl3","Barril",-122316.281417,1947.317956,48521.975283,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCl3",12,100)
Actions.SetBurnable("BarrCl3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCl4","Barril",-123441.806209,2106.621853,48064.517902,"Physic")
o.Scale=1.295256
o.Orientation=0.740046,-0.248449,-0.375422,0.499664
Breakings.SetBreakable("BarrCl4",12,100)
Actions.SetBurnable("BarrCl4",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCl5","Barril",-126700.578899,9443.659413,58720.873921,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCl5",12,100)
Actions.SetBurnable("BarrCl5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCl6","Barril",-126696.298716,9429.437064,57861.216256,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCl6",12,100)
Actions.SetBurnable("BarrCl6",BoxBurnTime,BoxDestroyTime)

##9 BARRILES Y 4 CAJAS EN ZONA PREVIA AL COMEDOR


o=Bladex.CreateEntity("Barrprev1","Barril",-90690.330619,2899.090728,44334.714915,"Physic")
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panprev1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panprev1")
Breakings.SetBreakable("Barrprev1",12,100,"panprev1")
Actions.SetBurnable("Barrprev1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("Barrprev2","Barril",-89421.484998,2735.379132,44483.874649,"Physic")
o.Scale=1.834864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barrprev2",12,100)
Actions.SetBurnable("Barrprev2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajprev1","Cajon2",-86977.656804,2903.924351,45207.231696,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,-0.521334,0.521334
Breakings.SetBreakable("Cajprev1",12,100)
Actions.SetBurnable("Cajprev1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barrprev4","Barril",-88774.306373,2940.160152,45339.022259,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barrprev4",12,100)
Actions.SetBurnable("Barrprev4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajprev3","Cajon2",-90216.531562,2902.322631,55327.210675,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Cajprev3",12,100)
Actions.SetBurnable("Cajprev3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barrprev7","Barril",-88772.330766,2935.173322,55363.174151,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barrprev7",12,100)
Actions.SetBurnable("Barrprev7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barrprev8","Barril",-87937.944925,3024.840270,55492.086227,"Physic")
o.Scale=1.115668
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barrprev8",12,100)
Actions.SetBurnable("Barrprev8",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajprev4","Cajon2",-90190.554382,1976.208823,55369.028884,"Physic")
o.Scale=0.678370
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panprev4", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panprev4")
Breakings.SetBreakable("Cajprev4",12,100,"panprev4")
Actions.SetBurnable("Cajprev4",BoxBurnTime,BoxDestroyTime)



###BARRILES Y CAJONES ZONA COMEDOR

###BARRIL Y CAJA EN LA ENTRADA

o=Bladex.CreateEntity("CajCom2","Cajon2",-84406.615986,-8472.894257,59777.047910,"Physic")
o.Scale=0.779768
o.Orientation=0.212631,0.212631,-0.674380,0.674380
Breakings.SetBreakable("CajCom2",12,100)
Actions.SetBurnable("CajCom2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCom1","Barril",-84435.343994,-7345.629586,57843.489349,"Physic")
o.Scale=2.026831
o.Orientation=0.905332,0.375001,-0.076295,0.184192
Breakings.SetBreakable("BarrCom1",12,100)
Actions.SetBurnable("BarrCom1",BoxBurnTime,BoxDestroyTime)

###BARRILES ACUMULADOS A LA DERECHA DE LA VENTANA


o=Bladex.CreateEntity("BarrCom2","Barril",-87762.021888,-5903.060711,50017.593334,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCom2",12,100)
Actions.SetBurnable("BarrCom2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCom3","Barril",-87467.662923,-5806.640933,49029.207045,"Physic")
o.Scale=1.321291
o.Orientation=0.708914,0.705229,-0.007900,0.005552
Breakings.SetBreakable("BarrCom3",12,100)
Actions.SetBurnable("BarrCom3",BoxBurnTime,BoxDestroyTime)

#o=Bladex.CreateEntity("BarrCom4","Barril",-86465.230715,-5496.879713,49635.337175,"Physic")
#o.Scale=0.756836
#o.Orientation=0.069381,-0.819764,-0.233015,0.518533
#Breakings.SetBreakable("BarrCom4",12,100)
#Actions.SetBurnable("BarrCom4",BoxBurnTime,BoxDestroyTime)

#o=Bladex.CreateEntity("BarrCom5","Barril",-82987.770998,-5858.296104,60620.121087,"Physic")
#o.Scale=1.445076
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#Breakings.SetBreakable("BarrCom5",12,100)
#Actions.SetBurnable("BarrCom5",BoxBurnTime,BoxDestroyTime)

###BARRILES ACUMULADOS A LA IZQUIERDA DE LA VENTANA


o=Bladex.CreateEntity("BarrCom6","Barril",-87786.163032,-5826.433186,45066.739647,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pancom6", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pancom6")
Breakings.SetBreakable("BarrCom6",12,100,"pancom6")
Actions.SetBurnable("BarrCom6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCom7","Barril",-87372.731170,-5804.320126,43996.015244,"Physic")
o.Scale=1.308209
o.Orientation=0.707220,0.706975,0.003452,-0.003685
Breakings.SetBreakable("BarrCom7",12,100)
Actions.SetBurnable("BarrCom7",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCom8","Barril",-87313.145905,-6761.490133,44020.022589,"Physic")
o.Scale=1.000000
o.Orientation=0.707749,0.703605,-0.053625,0.033988
queso=Breakings.CreateHiddenObject("quesocom8", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
pocimac.CreateFood("quesocom8")
Breakings.SetBreakable("BarrCom8",12,100,"quesocom8")
Actions.SetBurnable("BarrCom8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCom9","Barril",-87015.886917,-5814.930911,44740.272366,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCom9",12,100)
Actions.SetBurnable("BarrCom9",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrCom10","Barril",-86989.747277,-6781.001479,44751.623491,"Physic")
o.Scale=1.000000
o.Orientation=0.699943,0.697978,-0.114214,0.099300
Breakings.SetBreakable("BarrCom10",12,100)
Actions.SetBurnable("BarrCom10",BoxBurnTime,BoxDestroyTime)

#o=Bladex.CreateEntity("BarrCom11","Barril",-87800.020371,-6887.883338,44988.900706,"Physic")
#o.Scale=1.172579
#o.Orientation=0.696518,0.700885,-0.121997,0.093487
#Breakings.SetBreakable("BarrCom11",12,100)
#Actions.SetBurnable("BarrCom11",BoxBurnTime,BoxDestroyTime)


#o=Bladex.CreateEntity("BarrCom12","Barril",-86642.474283,-5677.274067,44096.640490,"Physic")
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#Breakings.SetBreakable("BarrCom12",12,100)
#Actions.SetBurnable("BarrCom12",BoxBurnTime,BoxDestroyTime)


#o=Bladex.CreateEntity("BarrCom13","Barril",-87141.368691,-5672.195558,45560.508900,"Physic")
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#Breakings.SetBreakable("BarrCom13",12,100)
#Actions.SetBurnable("BarrCom13",BoxBurnTime,BoxDestroyTime)


###CAJONES Y BARRILES EN ZONA ADYACENTE A PATIO PATRULLAS

## 3 CAJAS JUNTAS

o=Bladex.CreateEntity("CajPat1","Cajon2",-74623.720000,-7477.316000,64566.001000,"Physic")
o.Scale=1.220190
o.Orientation=0.707052,0.707160,0.000645,-0.000855
pan=Breakings.CreateHiddenObject("panpat1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panpat1")
Breakings.SetBreakable("CajPat1",12,100,"panpat1")
Actions.SetBurnable("CajPat1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajPat2","Cajon2",-74192.348000,-7296.752000,66155.859000,"Physic")
o.Scale=0.896324
o.Orientation=0.504946,0.495639,0.505361,-0.493945
Breakings.SetBreakable("CajPat2",12,100)
Actions.SetBurnable("CajPat2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajPat3","Cajon2",-75459.895000,-7560.123000,66040.739000,"Physic")
o.Scale=1.000000
o.Orientation=0.693811,-0.136090,0.138671,-0.693452
Breakings.SetBreakable("CajPat3",12,100)
Actions.SetBurnable("CajPat3",BoxBurnTime,BoxDestroyTime)



##5 CAJAS BAJO ANTORCHA

o=Bladex.CreateEntity("CajAnt1","Cajon2",-85733.934000,-7599.591000,64529.828000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panant1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panant1")
Breakings.SetBreakable("CajAnt1",12,100,"panant1")
Actions.SetBurnable("CajAnt1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajAnt2","Cajon2",-85627.671000,-7638.270000,65744.401000,"Physic")
o.Scale=0.779768
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
Breakings.SetBreakable("CajAnt2",12,100)
Actions.SetBurnable("CajAnt2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajAnt3","Cajon2",-86564.783134,-7464.164384,65876.423349,"Physic")
o.Scale=0.764404
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("CajAnt3",12,100)
Actions.SetBurnable("CajAnt3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajAnt4","Cajon2",-86549.265610,-8569.072359,65857.974212,"Physic")
o.Scale=0.749342
o.Orientation=0.679169,0.676048,-0.196967,-0.207107
Breakings.SetBreakable("CajAnt4",12,100)
Actions.SetBurnable("CajAnt4",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajAnt5","Cajon2",-85007.901096,-9044.595191,65634.674754,"Physic")
o.Scale=0.844377
o.Orientation=0.471154,0.486713,0.514787,0.525470
Breakings.SetBreakable("CajAnt5",12,100)
Actions.SetBurnable("CajAnt5",BoxBurnTime,BoxDestroyTime)



###3 BARRILES EN HABITACION LATERAL A PATIO

o=Bladex.CreateEntity("BarrLat1","Barril",-122467.662468,-6177.719252,57738.809810,"Physic")
o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrLat1",12,100)
Actions.SetBurnable("BarrLat1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrLat2","Barril",-123742.546169,-6043.488481,57791.468995,"Physic")
o.Scale=1.890462
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrLat2",12,100)
Actions.SetBurnable("BarrLat2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrLat3","Barril",-124017.994902,-5652.593921,55226.194680,"Physic")
o.Scale=1.321291
o.Orientation=0.700780,0.304065,0.447943,0.464542
Breakings.SetBreakable("BarrLat3",12,100)
Actions.SetBurnable("BarrLat3",BoxBurnTime,BoxDestroyTime)



#2 BARRILES Y 3 CAJAS EN ZONA VIGIA

o=Bladex.CreateEntity("CajVig1","Cajon2",-107138.358362,-12883.387515,35879.299710,"Physic")
o.Scale=1.000000
o.Orientation=0.004985,-0.715591,-0.698488,0.004435
Breakings.SetBreakable("CajVig1",12,100)
Actions.SetBurnable("CajVig1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajVig2","Cajon2",-105524.145021,-12506.489413,35842.943164,"Physic")
o.Scale=0.836017
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajVig2",12,100)
Actions.SetBurnable("CajVig2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrVig1","Barril",-107344.951198,-12577.517312,36934.497024,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrVig1",12,100)
Actions.SetBurnable("BarrVig1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrVig2","Barril",-106344.243424,-12364.414135,36973.805794,"Physic")
o.Scale=1.257163
o.Orientation=0.037915,0.958798,0.165625,0.227680
Breakings.SetBreakable("BarrVig2",12,100)
Actions.SetBurnable("BarrVig2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVig3","Cajon2",-103930.528922,-12872.951968,35576.857220,"Physic")
o.Scale=1.000000
o.Orientation=0.361593,0.607147,0.605882,0.365417
Breakings.SetBreakable("CajVig3",12,100)
Actions.SetBurnable("CajVig3",BoxBurnTime,BoxDestroyTime)







##BARRILES Y CAJAS EN ZONA FRENTE A ZONA INCENDIO

o=Bladex.CreateEntity("Barrfr1","Barril",-107297.949317,-3484.030592,41087.979537,"Physic")
o.Scale=1.745810
o.Orientation=0.696364,0.696364,0.122788,-0.122788
Breakings.SetBreakable("Barrfr1",12,100)
Actions.SetBurnable("Barrfr1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barrfr2","Barril",-106188.539539,-3475.826135,41192.575483,"Physic")
o.Scale=1.728525
o.Orientation=0.674380,0.674380,-0.212631,0.212631
pan=Breakings.CreateHiddenObject("panfr2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panfr2")
Breakings.SetBreakable("Barrfr2",12,100,"panfr2")
Actions.SetBurnable("Barrfr2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("Barrfr3","Barril",-104828.225274,-3464.266768,41249.133467,"Physic")
o.Scale=1.711410
o.Orientation=0.627211,0.627211,-0.326506,0.326506
Breakings.SetBreakable("Barrfr3",12,100)
Actions.SetBurnable("Barrfr3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("Barrfr4","Barril",-103502.741255,-3459.348633,41241.928512,"Physic")
o.Scale=1.694466
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfr4", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panfr4")
Breakings.SetBreakable("Barrfr4",12,100,"panfr4")
Actions.SetBurnable("Barrfr4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Cajafr1","Cajon2",-101608.735049,-3441.918139,35004.870892,"Physic")
o.Scale=1.160969
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Cajafr1",12,100)
Actions.SetBurnable("Cajafr1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Cajafr2","Cajon2",-101109.734077,-4519.215995,35000.373184,"Physic")
o.Scale=0.795442
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("Cajafr2",12,100)
Actions.SetBurnable("Cajafr2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajafr3","Cajon2",-103358.155248,-3620.762936,34857.540092,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,-0.500000,-0.500000,0.500000
Breakings.SetBreakable("Cajafr3",12,100)
Actions.SetBurnable("Cajafr3",BoxBurnTime,BoxDestroyTime)





##GRAN ACUMULACION DE BARRILES Y CAJAS EN ZONA INCENDIO




o=Bladex.CreateEntity("CajInc1","Cajon2",-83016.087375,-3099.972638,30109.830354,"Physic")
o.Scale=1.000000
o.Orientation=0.701836,0.701836,0.086175,-0.086175
Breakings.SetBreakable("CajInc1",12,100)
Actions.SetBurnable("CajInc1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajInc2","Cajon2",-84833.180836,-3291.701884,30122.369777,"Physic")
o.Scale=1.334504
o.Orientation=0.557208,0.557208,-0.435338,0.435338
Breakings.SetBreakable("CajInc2",12,100)
Actions.SetBurnable("CajInc2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajInc3","Cajon2",-83063.828074,-4211.339953,30355.648979,"Physic")
o.Scale=1.000000
o.Orientation=0.698602,0.701026,0.100868,-0.101699
pan=Breakings.CreateHiddenObject("paninc3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("paninc3")
Breakings.SetBreakable("CajInc3",12,100,"paninc3")
Breakings.SetBreakable("CajInc3",12,100)
Actions.SetBurnable("CajInc3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajInc5","Cajon2",-80452.951567,-3098.183347,24827.939996,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("paninc5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("paninc5")
Breakings.SetBreakable("CajInc5",12,100,"paninc5")
Breakings.SetBreakable("CajInc5",12,100)
Actions.SetBurnable("CajInc5",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("CajInc6","Cajon2",-80151.359498,-3356.442988,22808.208053,"Physic")
o.Scale=1.445076
o.Orientation=0.521334,0.521334,-0.477714,0.477714
Breakings.SetBreakable("CajInc6",12,100)
Actions.SetBurnable("CajInc6",BoxBurnTime,BoxDestroyTime)







o=Bladex.CreateEntity("BarrInc1","Barril",-86413.091630,-3564.062703,30922.657567,"Physic")
o.Scale=2.548057
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInc1",12,100)
Actions.SetBurnable("BarrInc1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInc2","Barril",-83815.964273,-3046.016189,29084.332306,"Physic")
o.Scale=1.282432
o.Orientation=0.701057,0.701057,0.092296,-0.092296
Breakings.SetBreakable("BarrInc2",12,100)
Actions.SetBurnable("BarrInc2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrInc3","Barril",-83002.604590,-2923.226011,28869.157544,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInc3",12,100)
Actions.SetBurnable("BarrInc3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrInc4","Barril",-86435.839755,-3145.491808,28107.510185,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInc4",12,100)
Actions.SetBurnable("BarrInc4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInc5","Barril",-86416.870246,-3047.501744,26993.248615,"Physic")
o.Scale=1.295256
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInc5",12,100)
Actions.SetBurnable("BarrInc5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrInc6","Barril",-86657.549316,-3118.298460,25820.614832,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInc6",12,100)
Actions.SetBurnable("BarrInc6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInc7","Barril",-86772.187748,-2787.652544,29403.280581,"Physic")
o.Scale=1.000000
o.Orientation=0.174822,0.431287,-0.084285,-0.881093
Breakings.SetBreakable("BarrInc7",12,100)
Actions.SetBurnable("BarrInc7",BoxBurnTime,BoxDestroyTime)




##BARRILES EN ULTIMA SALA ANTES DEL PUENTE LEVADIZO

o=Bladex.CreateEntity("BarrUlt1","Barril",-116058.514149,-7968.113355,1097.554214,"Physic")
o.Scale=1.711410
o.Orientation=0.707421,0.706790,0.000137,0.001792
pan=Breakings.CreateHiddenObject("panult1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panult1")
Breakings.SetBreakable("BarrUlt1",12,100,"panult1")



o=Bladex.CreateEntity("BarrUlt2","Barril",-117061.250112,-7874.357512,1156.488154,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panult2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panult2")
Breakings.SetBreakable("BarrUlt2",12,100,"panult2")




o=Bladex.CreateEntity("BarrUlt3","Barril",-116193.470487,-7983.880494,-199.070076,"Physic")
o.Scale=1.745810
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrUlt3",12,100)




o=Bladex.CreateEntity("BarrUlt4","Barril",-117391.119432,-7611.770494,157.535116,"Physic")
o.Scale=1.257163
o.Orientation=0.013604,-0.947454,-0.193822,-0.254125
Breakings.SetBreakable("BarrUlt4",12,100)




o=Bladex.CreateEntity("BarrUlt6","Barril",-118201.035937,-7844.577059,1076.221244,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrUlt6",12,100)




o=Bladex.CreateEntity("BarrUlt7","Barril",-119135.771117,-7995.075952,1155.954527,"Physic")
o.Scale=1.564811
o.Orientation=0.701840,0.583939,-0.079171,0.400209
Breakings.SetBreakable("BarrUlt7",12,100)



o=Bladex.CreateEntity("BarrUlt10","Barril",-116963.933403,-7833.236422,-879.714801,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrUlt10",12,100)




o=Bladex.CreateEntity("BarrUlt11","Barril",-116278.139905,-7610.854373,-2220.181029,"Physic")
o.Scale=1.220190
o.Orientation=0.123632,0.806401,-0.553195,-0.168547
Breakings.SetBreakable("BarrUlt11",12,100)


































############BARRILES Y CAJAS AL OTRO LADO DEL PUENTE LEVADIZO



##CAJAS EN SALA SOSA


o=Bladex.CreateEntity("CajSos1","Cajon2",-96978.443536,4658.123043,-75829.659934,"Physic")
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajSos1",12,100)



o=Bladex.CreateEntity("CajSos2","Cajon2",-96809.205187,3331.148827,-75789.270592,"Physic")
o.Scale=1.000000
o.Orientation=0.298836,0.298836,-0.640856,0.640856
Breakings.SetBreakable("CajSos2",12,100)



o=Bladex.CreateEntity("CajSos3","Cajon2",-96012.079911,4767.985788,-72831.076904,"Physic")
o.Scale=1.232392
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("CajSos3",12,100)



o=Bladex.CreateEntity("CajSos4","Cajon2",-95775.161748,3631.871453,-73246.760713,"Physic")
o.Scale=0.836017
o.Orientation=0.640856,0.640856,-0.298836,0.298836
Breakings.SetBreakable("CajSos4",12,100)



o=Bladex.CreateEntity("CajSos5","Cajon2",-94841.093044,5043.744452,-73899.196733,"Physic")
o.Scale=0.756836
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("CajSos5",12,100)



o=Bladex.CreateEntity("CajSos6","Cajon2",-94986.031943,5032.729825,-75796.243976,"Physic")
o.Scale=0.772048
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajSos6",12,100)




o=Bladex.CreateEntity("CajSos7","Cajon2",-95291.032869,4289.156922,-75077.236033,"Physic")
o.Scale=0.779768
o.Orientation=0.627211,0.326506,-0.326506,0.627211
Breakings.SetBreakable("CajSos7",12,100)




##BARRILES JUNTO A ESCALERAS



o=Bladex.CreateEntity("Barresc1","Barril",-96385.472322,1378.277795,-93834.983976,"Physic")
o.Scale=1.474123
o.Orientation=0.707053,0.704676,-0.039948,0.043724
Breakings.SetBreakable("Barresc1",12,100)



o=Bladex.CreateEntity("Barresc2","Barril",-96431.011263,1440.551588,-97371.101141,"Physic")
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc2",12,100)


o=Bladex.CreateEntity("Barresc3","Barril",-82464.949367,1134.539961,-102839.286657,"Physic")
o.Scale=2.067570
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc3",12,100)



o=Bladex.CreateEntity("Barresc4","Barril",-82509.748838,1347.347207,-104251.004496,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc4",12,100)



o=Bladex.CreateEntity("Barresc5","Barril",-82577.203961,-105.850841,-102800.131651,"Physic")
o.Scale=1.295256
o.Orientation=0.101355,-0.494437,-0.861170,0.060384
Breakings.SetBreakable("Barresc5",12,100)



o=Bladex.CreateEntity("Barresc6","Barril",-83470.498486,1371.491501,-103571.899773,"Physic")
o.Scale=1.612226
o.Orientation=0.612222,0.683769,0.353338,0.181098
Breakings.SetBreakable("Barresc6",12,100)


o=Bladex.CreateEntity("Barresc7","Barril",-83649.605181,1577.263254,-102735.186219,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc7",12,100)


o=Bladex.CreateEntity("Barresc8","Barril",-95967.998969,1271.020187,-96355.773980,"Physic")
o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc8",12,100)



o=Bladex.CreateEntity("Barresc9","Barril",-96202.977282,1574.425369,-95394.523602,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barresc9",12,100)





##BARRILES Y CAJAS ZONAS ADYACENTES A TRAMPA BOLAS DE FUEGO



o=Bladex.CreateEntity("Cajatram1","Cajon2",-86399.974648,6517.494574,-94775.286611,"Physic")
o.Scale=0.795442
o.Orientation=0.664463,0.664463,-0.241845,0.241845
pan=Breakings.CreateHiddenObject("pantram1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pantram1")
Breakings.SetBreakable("Cajatram1",12,100,"pantram1")
Actions.SetBurnable("Cajatram1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barrtram1","Barril",-103883.023686,7156.986432,-86043.571577,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pantrmm1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pantrmm1")
Breakings.SetBreakable("Barrtram1",12,100,"pantrmm1")
Actions.SetBurnable("Barrtram1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barrtram2","Barril",-102652.653283,7064.118757,-86216.429804,"Physic")
o.Scale=1.628348
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barrtram2",12,100)
Actions.SetBurnable("Barrtram2",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barrtram3","Barril",-102886.819391,7370.422972,-88156.644686,"Physic")
o.Scale=1.321291
o.Orientation=0.101471,-0.852086,-0.175336,0.482607
Breakings.SetBreakable("Barrtram3",12,100)
Actions.SetBurnable("Barrtram3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajatram3","Cajon2",-82927.027639,6397.202122,-94150.603507,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Cajatram3",12,100)
Actions.SetBurnable("Cajatram3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Cajatram4","Cajon2",-82666.986656,6526.440192,-95686.921111,"Physic")
o.Scale=0.779768
o.Orientation=0.521334,0.521334,-0.477714,0.477714
Breakings.SetBreakable("Cajatram4",12,100)
Actions.SetBurnable("Cajatram4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajatram6","Cajon2",-92513.356368,6401.817998,-98437.883568,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Cajatram6",12,100)
Actions.SetBurnable("Cajatram6",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajatram7","Cajon2",-92597.535494,5017.634844,-99009.059678,"Physic")
o.Scale=1.000000
o.Orientation=0.353553,0.612372,0.612372,0.353553
Breakings.SetBreakable("Cajatram7",12,100)
Actions.SetBurnable("Cajatram7",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajatram8","Cajon2",-92351.882618,6397.685768,-99880.580824,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Cajatram8",12,100)
Actions.SetBurnable("Cajatram8",BoxBurnTime,BoxDestroyTime)







###########################
###########################
###########BARRILES EN EL ALMACEN ANTES DEL CABALERO KAOS. SALA DE LOS CHORROS.

o=Bladex.CreateEntity("BARK1","Barril",-114034.727983,1472.471727,-92738.643555,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARK1",12,100)
Actions.SetBurnable("BARK1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARK2","Barril",-115488.942774,1429.737728,-92823.297512,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panKK2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panKK2")
Breakings.SetBreakable("BARK2",12,100,"panKK2")
Actions.SetBurnable("BARK2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARK3","Barril",-115601.658172,1343.845424,-91364.092737,"Physic")
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARK3",12,100)
Actions.SetBurnable("BARK3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARK4","Barril",-112839.631163,1395.653481,-92935.467171,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panKK4", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panKK4")
Breakings.SetBreakable("BARK4",12,100,"panKK4")
Actions.SetBurnable("BARK4",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARK5","Barril",-114170.580770,1381.408838,-91672.609459,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panKK5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panKK5")
Breakings.SetBreakable("BARK5",12,100,"panKK5")
Actions.SetBurnable("BARK5",BoxBurnTime,BoxDestroyTime)




Bladex.AddCombustionDataFor("Caja_i_r", "BigFire", 750, 950, 2, 2, 2, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("Cajon2", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("CajonPieza1", "LargeFire", 500,1100, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza2",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza3",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza4",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza5",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza6",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza7",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza8",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza9",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza10", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza11", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza12", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza13", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza14", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza15", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza16", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza17", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza18", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("Barril", "LargeFire", 250, 400, 4, 1.5, 1, (BoxBurnTime+BoxDestroyTime)*3)
Bladex.AddCombustionDataFor("BarrilPieza1", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza2", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza3", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza4", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza5", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza6", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)

#########Mesas###########
##################SALA DEL PRIMER CABALLERO
o=Bladex.CreateEntity("MM2","Mesa",-122262.642275,1932.240638,51871.331361,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("MM2",12,100)

o=Bladex.CreateEntity("MM1","Mesa",-136793.362622,-31068.136687,-93677.659784)
o.Scale=1.000000
o.Orientation=0.495618,0.495618,0.504344,-0.504344
darfuncs.SetHint(o,"","",0.0,0.0)   # Add
#Breakings.SetBreakable("MM1",12,100)

o=Bladex.CreateEntity("MM3","Mesa",-117903.524095,-7818.885900,-6953.228435,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("MM3",12,100)

o=Bladex.CreateEntity("MM4","Mesa",-83340.020366,1428.675910,-98130.658495,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("MM4",12,100)

o=Bladex.CreateEntity("Mesa2","Mesa",-113437.461000,8413.330000,69004.723000,"Physic")
o.Scale=1.000000
o.Orientation=0.701836,0.701836,0.086175,-0.086175
Breakings.SetBreakable("Mesa2",12,100)

o=Bladex.CreateEntity("Mesa3","Mesa",-123604.260000,-22566.685000,-112577.699000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("Mesa3",12,100)


o=Bladex.CreateEntity("Mesa4","Mesa",-125977.655000,-22569.484000,-112586.896000,"Physic")
o.Scale=1.000000
o.Orientation=0.500111,0.499950,0.500982,-0.498955
Breakings.SetBreakable("Mesa4",12,100)


o=Bladex.CreateEntity("Meson1","Meson",-83648.823000,-5867.947000,38467.452000) #,"Physic")
o.Scale=1.000000
o.Orientation=0.707169,0.707028,-0.002400,0.004150
Sparks.SetWoodenSparkling(o.Name) # Add
o.Static = 1                      #
#Breakings.SetBreakable("Meson1",12,100)


##############
#######MESITAS

o=Bladex.CreateEntity("MESITA1","Mesita",-101795.378000,-335.243000,12433.789000,"Physic")
o.Scale=1.000000
o.Orientation=0.707879,0.705696,-0.023525,0.018657
Breakings.SetBreakable("MESITA1",12,100)


o=Bladex.CreateEntity("MESITA2","Mesita",-108812.594000,-448.077000,4506.503000,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("MESITA2",12,100)


o=Bladex.CreateEntity("MESITA3","Mesita",-106814.586000,-430.078000,12752.685000,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("MESITA3",12,100)



##########ARMEROS
#################


o=Bladex.CreateEntity("ARMERO1","Armero",-134972.732000,-12331.810000,-107309.416000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARMERO1",12,100)


o=Bladex.CreateEntity("ARMERO2","Armero",-132143.876000,-12335.524000,-107265.008000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("ARMERO2",12,100)

o=Bladex.CreateEntity("ARMERO3","Armero",-138143.876000,860.788000,-99365.008000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("ARMERO3",12,100)


o=Bladex.CreateEntity("ARMERO77","Armero",-89683.891419,2664.656629,-28924.096750,"Physic")
o.Scale=1.000000
o.Orientation=0.504344,0.504344,-0.495618,0.495618
Breakings.SetBreakable("ARMERO77",12,100)


o=Bladex.CreateEntity("ARMERO88","Armero",-89764.289394,2660.769569,-27285.295857,"Physic")
o.Scale=1.000000
o.Orientation=0.568413,0.568413,-0.420603,0.420603
Breakings.SetBreakable("ARMERO88",12,100)

############
######COFRES#######
#########


o=Bladex.CreateEntity("COFRE1","Cofre",-84490.574875,2950.656638,-15786.475586,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,-0.707107,0.707107      # Was facing wrong dir
ragnarpocima50c1=Breakings.CreateHiddenObject("ragnarpocima50c1", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima50c1.Solid=1
pocimac.CreatePotion("ragnarpocima50c1")
Breakings.SetBreakable("COFRE1",12,100,"ragnarpocima50c1")

o=Bladex.CreateEntity("COFRE2","Cofre",-84608.087493,2944.515774,-20633.395001,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("COFRE2",12,100)

o=Bladex.CreateEntity("COFRE3","Cofre",-84668.025898,3048.243088,-22755.280026,"Physic")
o.Scale=0.803396
o.Orientation=0.647958,0.641210,-0.288926,0.292443
ragnarpocima50c3=Breakings.CreateHiddenObject("ragnarpocima50c3", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima50c3.Solid=1
pocimac.CreatePotion("ragnarpocima50c3")
Breakings.SetBreakable("COFRE3",12,100,"ragnarpocima50c3")


### Cofre lateral patio cercano puente levadizo

o=Bladex.CreateEntity("COFRE4","Cofre",-122120.523910,1448.172104,-13166.439119,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
ragnarpocima25c4=Breakings.CreateHiddenObject("ragnarpocima25c4", "Pocima25",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima25c4.Solid=1
pocimac.CreatePotion("ragnarpocima25c4")
Breakings.SetBreakable("COFRE4",12,100,"ragnarpocima25c4")


### Cofres torre final

o=Bladex.CreateEntity("COFRE5","Cofre",-144042.318927,-5802.026612,-90501.841014,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
ragnarpocima100b=Breakings.CreateHiddenObject("ragnarpocima100b", "Pocima100",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima100b.Solid=1
pocimac.CreatePotion("ragnarpocima100b")
Breakings.SetBreakable("COFRE5",12,100,"ragnarpocima100b")

o=Bladex.CreateEntity("COFRE6","Cofre",-132031.635291,-12053.496611,-116252.941361,"Physic")
o.Scale=1.000000
o.Orientation=0.495618,0.495618, -0.504344, 0.504344    # Were facing wrong dir
ragnarpocima25c6=Breakings.CreateHiddenObject("ragnarpocima25c6", "Pocima25",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima25c6.Solid=1
pocimac.CreatePotion("ragnarpocima25c6")
Breakings.SetBreakable("COFRE6",12,100,"ragnarpocima25c6")

o=Bladex.CreateEntity("COFRE7","Cofre",-135433.949746,-12047.511231,-116156.648834,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000, -0.500000, 0.500000    # Were facing wrong dir
ragnarpocima50c7=Breakings.CreateHiddenObject("ragnarpocima50c7", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima50c7.Solid=1
pocimac.CreatePotion("ragnarpocima50c7")
Breakings.SetBreakable("COFRE7",12,100,"ragnarpocima50c7")

o=Bladex.CreateEntity("COFRE8","Cofre",-121740.225420,-12053.242182,-100688.075958,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("COFRE8",12,100)

o=Bladex.CreateEntity("COFRE9","Cofre",-121750.815746,-12053.005125,-102939.313172,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
ragnarpocima25c9=Breakings.CreateHiddenObject("ragnarpocima25c9", "Pocima25",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima25c9.Solid=1
pocimac.CreatePotion("ragnarpocima25c9")
Breakings.SetBreakable("COFRE9",12,100,"ragnarpocima25c9")

o=Bladex.CreateEntity("COFRE10","Cofre",-121987.990111,-22551.723328,-109934.462172,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
ragnarpocima50c10=Breakings.CreateHiddenObject("ragnarpocima50c10", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima50c10.Solid=1
pocimac.CreatePotion("ragnarpocima50c10")
Breakings.SetBreakable("COFRE10",12,100,"ragnarpocima50c10")

o=Bladex.CreateEntity("COFRE11","Cofre",-132338.105063,-22506.004663,-112366.755410,"Physic")
o.Scale=0.914340
o.Orientation=0.504344,0.504344,-0.495618,0.495618
ragnarpocima25c11=Breakings.CreateHiddenObject("ragnarpocima25c11", "Pocima25",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima25c11.Solid=1
pocimac.CreatePotion("ragnarpocima25c11")
Breakings.SetBreakable("COFRE11",12,100,"ragnarpocima25c11")

o=Bladex.CreateEntity("COFRE12","Cofre",-134452.532623,-22552.883790,-112254.640254,"Physic")
o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491198,0.491198
Breakings.SetBreakable("COFRE12",12,100)


### Cofre Ragnar

o=Bladex.CreateEntity("COFRE17","Cofre",-124082.933580,-31298.900153,-91096.287650,"Physic")
o.Scale=1.000000
o.Orientation=0.012341,0.012341,0.706999,-0.706999
ragnarpocima100cc=Breakings.CreateHiddenObject("ragnarpocima100cc", "Pocima100",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
ragnarpocima100cc.Solid=1
pocimac.CreatePotion("ragnarpocima100cc")
Breakings.SetBreakable("COFRE17",12,100,"ragnarpocima100cc")


################################################	ARMAS DEL BARBARO DE MOSQUEO

o=Bladex.CreateEntity("RagnarDeathSword","DeathSword",-122417.671529,-875.017774,8300.726749,"Weapon")
o.Scale=1.000000
o.Orientation=0.537435,0.614202,0.345269,-0.463367
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("RagnarEclipse","Eclipse",-101900.039666,1139.903918,65135.443746,"Weapon")   # moved up by 100   -LeadHead
o.Scale=1.000000
o.Orientation=0.381420,-0.201968,0.545403,0.718515
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("barmero2","Armero",-101562.780716,1163.449125,64867.725835,"Physic")
o.Scale=1.000000
o.Orientation=0.030844,0.030844,0.706434,-0.706434
Breakings.SetBreakable("barmero2",12,100)


### ARMAS DE RECOMPENSA QUE SI LE SIRVEN AL CABALLERO

o=Bladex.CreateEntity("RagnarMaza","Maza",-90243.688186,3085.386091,-19727.434993,"Weapon")
o.Scale=1.000000
o.Orientation=0.507168,-0.645739,-0.215627,-0.528494
ItemTypes.ItemDefaultFuncs(o)



################################################	NUEVA REVISION MAYO
########ZONA DE LOS BICHITOS


o=Bladex.CreateEntity("BARRR1","Barril",-84925.527000,1326.058000,50357.455000,"Physic")
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARRR1",12,100)

o=Bladex.CreateEntity("BARRR2","Barril",-84448.658000,1441.309000,51391.238000,"Physic")
o.Scale=1.503752
o.Orientation=0.591775,0.476988,-0.216624,-0.612666
Breakings.SetBreakable("BARRR2",12,100)

o=Bladex.CreateEntity("BARRR3","Barril",-84474.787000,1048.103000,49164.546000,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARRR3",12,100)
