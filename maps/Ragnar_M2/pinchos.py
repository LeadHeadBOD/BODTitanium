##///
##||| Rangar_M2/pinchos.PY TITANIUM
##||| Change list:
##||| * Scaled all of the ceiling trap spikes to be same size
##||| * Added one of the spikes that was missing for its respective hole
##||| * Moved some of the ceiling trap spikes to not appear floating
##\\\ 

import Reference
import Bladex
import InitDataField


B_SOLID_MASK_PERSON          =1

#-------------------pendulos---------------------

o=Bladex.CreateEntity("Pendulo1","Pendulo",-119290.798000,8137.952000,-98661.444000,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.Static=0

o.FiresIntensity=[ 40 ]
o.Lights=[ (10.000000,0.031250,(255,166,88)) ]
o.Solid = 0
o.ContinuousDamage=1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1
#if o.ExclusionMask & B_SOLID_MASK_PERSON:
#	o.ExclusionMask= o.ExclusionMask-B_SOLID_MASK_PERSON


#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pendulo2","Pendulo",-123423.824000,8132.099000,-98647.575000,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.Static=0

o.FiresIntensity=[ 40 ]
o.Lights=[ (10.000000,0.031250,(255,166,88)) ]
o.Solid = 0
o.ContinuousDamage=1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1
#if o.ExclusionMask & B_SOLID_MASK_PERSON:
#	o.ExclusionMask= o.ExclusionMask-B_SOLID_MASK_PERSON


#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

#-------------------pinchos de sala del pendulo--------------------


o=Bladex.CreateEntity("PinPen1","PinchoMiguel",-120506.492000,30370.514000,-95013.859000,"Weapon")
o.Static = 1
o.Scale=2.067570
o.Orientation=0.622515,0.782608,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen2","PinchoMiguel",-123564.723000,30365.151000,-102793.487000,"Weapon")
o.Static = 1
o.Scale=2.026831
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen3","PinchoMiguel",-120488.235000,30370.072000,-103638.500000,"Weapon")
o.Static = 1
o.Scale=1.834864
o.Orientation=0.793353,0.608761,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen4","PinchoMiguel",-116794.014000,30557.063000,-102246.846000,"Weapon")
o.Static = 1
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen5","PinchoMiguel",-124644.854000,30960.066000,-104100.534000,"Weapon")
o.Static = 1
o.Scale=1.533978
o.Orientation=0.887011,0.461749,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0


o=Bladex.CreateEntity("PinPen6","PinchoMiguel",-120745.594000,31006.711000,-101280.238000,"Weapon")
o.Static = 1
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen7","PinchoMiguel",-119188.884000,31127.289000,-102528.195000,"Weapon")
o.Static = 1
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen8","PinchoMiguel",-124611.053000,31022.414000,-96614.719000,"Weapon")
o.Static = 1
o.Scale=1.138093
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen9","PinchoMiguel",-122457.513000,30883.960000,-94253.684000,"Weapon")
o.Static = 1
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen10","PinchoMiguel",-119366.707000,31321.560000,-97172.628000,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0


o=Bladex.CreateEntity("PinPen11","PinchoMiguel",-121812.639000,30996.198000,-96019.646000,"Weapon")
o.Static = 1
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen12","PinchoMiguel",-119036.288000,30844.360000,-94583.991000,"Weapon")
o.Static = 1
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen13","PinchoMiguel",-122049.141000,30943.589000,-92162.449000,"Weapon")
o.Static = 1
o.Scale=1.503752
o.Orientation=0.492424,0.870356,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen14","PinchoMiguel",-124353.874000,30726.635000,-90952.764000,"Weapon")
o.Static = 1
o.Scale=1.503752
o.Orientation=0.656059,0.754710,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0


o=Bladex.CreateEntity("PinPen15","PinchoMiguel",-117270.774000,30721.847000,-99613.508000,"Weapon")
o.Static = 1
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen16","PinchoMiguel",-122114.341000,30667.250000,-101797.167000,"Weapon")
o.Static = 1
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen17","PinchoMiguel",-117535.493000,27859.693000,-104170.843000,"Weapon")
o.Static = 1
o.Scale=1.269735
o.Orientation=0.861629,0.507538,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0


o=Bladex.CreateEntity("PinPen18","PinchoMiguel",-125049.738000,31078.986000,-106111.306000,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0


o=Bladex.CreateEntity("PinPen19","PinchoMiguel",-114898.409544,30898.600566,-103465.143914,"Weapon")
o.Static = 1
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen20","PinchoMiguel",-115042.528098,31190.786150,-100986.668586,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen21","PinchoMiguel",-118000.604361,30779.491350,-103522.033216,"Weapon")
o.Static = 1
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen22","PinchoMiguel",-119282.498852,31358.645203,-101108.956731,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen23","PinchoMiguel",-117237.651219,31135.271075,-100554.873839,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen24","PinchoMiguel",-115460.415548,31179.972500,-99873.467906,"Weapon")
o.Static = 1
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen25","PinchoMiguel",-113058.324510,28925.938811,-103894.147297,"Weapon")
o.Static = 1
o.Scale=1.518790
o.Orientation=0.692911,0.692911,-0.140974,-0.140974
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen26","PinchoMiguel",-116076.258069,29582.418026,-104075.455120,"Weapon")
o.Static = 1
o.Scale=1.549318
o.Orientation=0.902585,0.430511,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen27","PinchoMiguel",-120538.958719,30758.876262,-102542.136427,"Weapon")
o.Static = 1
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen28","PinchoMiguel",-118064.907374,30725.475348,-102053.286409,"Weapon")
o.Static = 1
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen29","PinchoMiguel",-124759.658929,30970.324516,-101856.104796,"Weapon")
o.Static = 1
o.Scale=1.172579
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen30","PinchoMiguel",-123630.981987,30736.282141,-100136.998526,"Weapon")
o.Static = 1
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen31","PinchoMiguel",-120307.806040,28858.005706,-105976.815854,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.976296,0.216440,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen32","PinchoMiguel",-123105.612323,30966.454899,-95778.287976,"Weapon")
o.Static = 1
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen33","PinchoMiguel",-120499.128349,30929.495099,-96479.880815,"Weapon")
o.Static = 1
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen34","PinchoMiguel",-121375.688157,30981.549379,-100400.565488,"Weapon")
o.Static = 1
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen35","PinchoMiguel",-122112.233883,29442.436917,-104155.834523,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.920505,0.390731,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen36","PinchoMiguel",-118956.619336,30693.960397,-90626.312879,"Weapon")
o.Static = 1
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen37","PinchoMiguel",-121633.266452,30728.542565,-93299.035174,"Weapon")
o.Static = 1
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen38","PinchoMiguel",-124335.422893,30665.047868,-95124.380465,"Weapon")
o.Static = 1
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen39","PinchoMiguel",-122745.569939,28577.572776,-90228.279304,"Weapon")
o.Static = 1
o.Scale=1.853212
o.Orientation=0.422618,0.906308,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen40","PinchoMiguel",-125214.947872,28618.106952,-90330.415135,"Weapon")
o.Static = 1
o.Scale=1.564811
o.Orientation=0.374607,0.927184,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen41","PinchoMiguel",-120125.787854,28723.400374,-90316.191364,"Weapon")
o.Static = 1
o.Scale=1.533978
o.Orientation=0.317305,0.948324,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen42","PinchoMiguel",-122333.974229,31009.059896,-90359.026433,"Weapon")
o.Static = 1
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen43","PinchoMiguel",-118418.460246,28951.372815,-93516.397839,"Weapon")
o.Static = 1
o.Scale=1.644632
o.Orientation=0.681390,0.681390,-0.188966,-0.188966
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen44","PinchoMiguel",-118249.116836,28337.646136,-92064.198210,"Weapon")
o.Static = 1
o.Scale=1.816697
o.Orientation=0.643440,0.643440,-0.293232,-0.293232
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen45","PinchoMiguel",-125294.677510,28338.063254,-96031.974708,"Weapon")
o.Static = 1
o.Scale=1.361327
o.Orientation=0.640856,0.640856,0.298836,0.298836
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen46","PinchoMiguel",-125685.929479,27773.464869,-93769.713939,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.635543,0.635543,0.309975,0.309975
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen47","PinchoMiguel",-124229.591261,27440.414931,-94752.141965,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.500000,0.866025,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen48","PinchoMiguel",-120237.862414,29834.785288,-92715.025272,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen49","PinchoMiguel",-119910.279836,31102.999385,-106056.986443,"Weapon")
o.Static = 1
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen50","PinchoMiguel",-122082.220511,29430.788578,-106147.058600,"Weapon")
o.Static = 1
o.Scale=1.244716
o.Orientation=0.958820,0.284015,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen51","PinchoMiguel",-122963.215823,30855.463398,-97803.634697,"Weapon")
o.Static = 1
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen52","PinchoMiguel",-115356.764195,31352.138693,-101938.015767,"Weapon")
o.Static = 1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0



o=Bladex.CreateEntity("PinPen53","PinchoMiguel",-115525.092103,25493.968372,-95815.117749,"Weapon")
o.Static = 1
o.Scale=1.518790
o.Orientation=0.446198,0.894934,0.000000,0.000000
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión

o.Solid=0




#-------------------------------------
#-------------------pinchos de la trampa de arriba-------------

o=Bladex.CreateEntity("Pincho1","PinchoMiguel",-125798,-26100,-104205,"Weapon")
o.Static=1
o.Scale=0.960980
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho2","PinchoMiguel",-123692,-26100,-104202,"Weapon")
o.Static=1
o.Scale=0.942045
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho3","PinchoMiguel",-124814,-26100,-103091,"Weapon")
o.Static=1
o.Scale=0.960981
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho4","PinchoMiguel",-123687,-26100,-102089,"Weapon")
o.Static=1
o.Scale=0.951466
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho5","PinchoMiguel",-124812,-26100,-100297,"Weapon")
o.Static=1
o.Scale=0.914340
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho6","PinchoMiguel",-125809,-26100,-102096,"Weapon")
o.Static=1
o.Scale=0.905287
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho7","PinchoMiguel",-123700,-26100,-99568,"Weapon")
o.Static=1
o.Scale=0.926324
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho8","PinchoMiguel",-125805,-26100,-99709,"Weapon")
o.Static=1
o.Scale=0.917449
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho9","PinchoMiguel",-124825,-26100,-98429,"Weapon")
o.Static=1
o.Scale=0.961349
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho10","PinchoMiguel",-123699,-26100,-97451,"Weapon")
o.Static=1
o.Scale=0.903396
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


o=Bladex.CreateEntity("Pincho11","PinchoMiguel",-125793,-26100,-97459,"Weapon")
o.Static=1
o.Scale=0.939963
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0


o=Bladex.CreateEntity("Pincho12","PinchoMiguel",-124808,-26100,-96319,"Weapon")
o.Static=1
o.Scale=0.975
o.Orientation=0.700909,-0.713250,0.000000,0.000000

o.Solid = 0
#o.NodesOrientation=?  En la siguiente versión
#o.Scripts=?  En la siguiente versión


ActivatePinchos("PinPen",1,53)
ActivatePinchos("Pincho",1,12)
