##///
##||| Dwarf_M3/pira1.PY TITANIUM
##||| Change list:
##||| * Shadowpass
##\\\ 

import Breakings

###########################################################################
#-------------------------LUZ DE-LA-HOGUERA1----------------------#########
###########################################################################

luz1=Bladex.CreateEntity("Luz1","Entity Spot",67104.489334,-600,-51714.310555)
luz1.Color=250,110,0
luz1.Intensity=10
luz1.Precission=0.05    # was 0.1



H11=Bladex.CreateEntity("H11","Barril",67104.489334,-434.292282,-51714.310555)
H11.Static=1
H11.Scale=1.533978
H11.Orientation=0.087822,-0.869340,0.166844,-0.456836
H11.CatchOnFire (0,0,0)
H11.CastShadows=0

H12=Bladex.CreateEntity("H12","Barril",68017.568422,-434.765604,-52538.572799)
H12.Static=1
H12.Scale=1.295256
H12.Orientation=0.971038,0.068282,-0.104420,0.203763
H12.CatchOnFire (0,0,0)
H12.CastShadows=0

H13=Bladex.CreateEntity("H13","Cajon2",67153.444438,-536.420767,-52567.977603)
H13.Static=0
H13.Scale=0.503298
H13.Orientation=0.256913,0.294817,0.649582,0.652013
H13.CatchOnFire (0,0,0)
H13.CastShadows=0

H14=Bladex.CreateEntity("H14","Barril",67794.224798,-1110.345407,-52096.084729)
H14.Static=1
H14.Scale=1.000000
H14.Orientation=0.216534,0.363191,0.905826,-0.026162
H14.CatchOnFire (0,0,0)
H14.CastShadows=0

H15=Bladex.CreateEntity("H15","Hoguera",67392.027404,-280.857469,-53193.813664)
H15.Static=1
H15.Scale=1.208109
H15.Orientation=0.707107,0.707107,0.000000,0.000000
H15.FiresIntensity=[ 11 ]
H15.Lights=[ (0.000000,0.031250,(255,196,128)) ]



H16=Bladex.CreateEntity("H16","Hoguera",66373.510710,-268.618987,-52486.857855)
H16.Static=1
H16.Scale=1.115668
H16.Orientation=0.706999,0.706676,0.024678,-0.012341
H16.FiresIntensity=[ 9 ]
H16.Lights=[ (0.000000,0.031250,(255,196,128)) ]


H17=Bladex.CreateEntity("H17","Astillas1",65681.865812,-359.841885,-52229.218775)
H17.Static=1
H17.Scale=0.614119
H17.Orientation=0.436294,0.485500,-0.641511,0.402991


H18=Bladex.CreateEntity("H18","Astillas1",66414.116324,-333.964103,-53205.240415)
H18.Static=1
H18.Scale=0.827740
H18.Orientation=0.083667,0.134546,-0.604874,-0.780400



H19=Bladex.CreateEntity("H19","Astillas2",62431.665023,-138.468905,-52563.373900)
H19.Static=1
H19.Scale=1.000000
H19.Orientation=0.144152,0.656857,0.655622,0.343393



H110=Bladex.CreateEntity("H110","Astillas3",64642.494004,-241.820016,-48220.620390)
H110.Static=0
H110.Scale=1.000000
H110.Orientation=0.612423,0.612423,-0.353466,0.353466



H111=Bladex.CreateEntity("H111","Astillas3",66398.855526,-171.762517,-51228.361311)
H111.Static=0
H111.Scale=0.678370
H111.Orientation=0.684572,0.684572,0.177092,-0.177092



H112=Bladex.CreateEntity("H112","Astillas2",67832.311317,-212.932902,-53404.281539)
H112.Static=0
H112.Scale=0.561514
H112.Orientation=0.311829,0.082582,0.459566,0.827492



H113=Bladex.CreateEntity("H113","Astillas2",63521.593985,-309.924544,-57684.443279)
H113.Static=0
H113.Scale=1.000000
H113.Orientation=0.179486,0.259306,0.673155,-0.668886



H114=Bladex.CreateEntity("H114","Barril",58988.026465,-615.752584,-53370.591992)
H114.Static=0
H114.Scale=1.459527
H114.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("H114",10,60)


H115=Bladex.CreateEntity("H115","Barril",58855.562996,-299.193362,-54370.881112)
H115.Static=0
H115.Scale=1.000000
H115.Orientation=0.124659,-0.819930,0.204519,-0.519950
Breakings.SetBreakable("H115",10,60)
