##///
##||| Barb_M1/OBJETOS.PY TITANIUM
##||| Change list:
##||| * added sparks for stones
##||| * Changed some light sources for more consistent shadows
##\\\

##############	PUENTE ROTO EN LAS ROCAS

o=Bladex.CreateEntity("NoName10","Viga",-12729.635000,-17281.984000,6532.844000,"Physic")
o.Scale=2.400385
o.Orientation=0.018510,0.018510,-0.706864,0.706864
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName11","Viga",-14325.295000,-17463.197000,6898.382000,"Physic")
o.Scale=2.088246
o.Orientation=0.024678,0.024678,-0.706676,0.706676
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName12","Tabla_xl",-13680.834000,-18421.761000,6501.978000,"Physic")
o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName13","Tabla_rota",-13238.627000,-18351.044000,5847.312000,"Physic")
o.Scale=1.677689
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName14","Tabla_rota",-13866.871000,-18454.922000,7390.658000,"Physic")
o.Scale=2.006763
o.Orientation=0.006164,0.006171,0.707080,0.707080
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



###########PUENTE COLGANTE

o=Bladex.CreateEntity("NoName6","Puenteau_Plano",-2999.382000,-18715.434000,36389.081000,"Physic")
o.Scale=0.550450
o.Orientation=0.396139,0.362994,-0.621813,0.569788
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName8","Tabla_xl",-44.144000,-18991.244000,36529.285000,"Physic")
o.Scale=3.645680
o.Orientation=0.488894,0.687319,0.313424,-0.436281
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Tabla_xl",783.559000,-19462.433000,36888.303000,"Physic")
o.Scale=3.869963
o.Orientation=0.609264,0.609264,0.358884,-0.358884
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


##################CASETA SECRETA DECORACION


o=Bladex.CreateEntity("NoName0","Antorchaenpared",13253.047000,-23297.152000,52166.954000,"Physic")
o.Scale=1.000000
o.Orientation=0.691655,0.691655,-0.147016,0.147016
o.FiresIntensity=[ 0 ]
o.Lights=[ (4.000000,0.060000,(255,153,40)) ]   # Changed
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName1","Viga",14495.307000,-26095.858000,53222.831000,"Physic")
o.Scale=2.958215
o.Orientation=0.541675,0.541675,-0.454519,0.454519
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajabse5","Caja_i_r",16791.710000,-21601.896000,56335.429000)
o.Scale=1.000000
o.Orientation=0.632814,0.632814,-0.315509,0.315509
Sparks.SetWoodenSparkling(o.Name)
o.Static=1
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajabse6","Caja_i_r",16307.677000,-21602.025000,58053.968000)
o.Scale=1.000000
o.Orientation=0.606109,0.606109,-0.364187,0.364187
Sparks.SetWoodenSparkling(o.Name)
o.Static=1
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajase2","Cajon2",16923.239000,-22714.350000,56493.380000,"Physic")
o.Scale=1.000000
o.Orientation=0.481446,0.481857,-0.517690,0.517708
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajase3","Cajon2",16489.595000,-22561.225000,58012.449000,"Physic")
o.Scale=0.741923
o.Orientation=0.704416,0.704416,0.061628,-0.061628
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajase1","Cajon2",17004.391000,-23759.687000,57731.265000,"Physic")
o.Scale=1.000000
o.Orientation=0.519659,0.398474,-0.443384,0.612032
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("cajase4","Cajon2",17947.463000,-21963.298000,57901.504000,"Physic")
o.Scale=1.104622
o.Orientation=0.341358,0.616259,0.621510,0.342674
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión



o=Bladex.CreateEntity("NoName8","Piedra_01",13289.992000,-21091.048000,53993.090000,"Physic")
o.Scale=1.000000
o.Orientation=0.985086,-0.086115,-0.060629,0.136065
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("NoName9","Piedra_01",13711.305000,-21087.081000,52773.712000,"Physic")
o.Scale=1.000000
o.Orientation=0.974436,-0.124735,0.038499,0.182846
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


### LA P... PIEDRA 

o=Bladex.CreateEntity("NoName0","Roca2",-172337.038643,385.496155,-69411.242121)
o.Scale=2.026831
o.Orientation=0.160430,-0.909844,0.066452,-0.376870