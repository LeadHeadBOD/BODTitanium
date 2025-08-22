##///
##||| VOLCANO_M14/ARMAS.PY TITANIUM
##||| Change list:
##||| * Spear no longer stuck in ground
##\\\ 

import Breakings
import Sparks
import Ontake



o=Bladex.CreateEntity("volcweap1","FireBo",54861.661574,3513.555545,41842.458382,"Weapon")
o.Scale=1.000000
o.Orientation=0.852931,0.515395,-0.037323,0.074046
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap2","FireBigSword",-37402.841303,19220.567429,-64659.905004,"Weapon")
o.Scale=1.000000
o.Orientation=0.713223,-0.700883,0.006636,0.005667
ItemTypes.ItemDefaultFuncs(o)

Ontake.AddOnTakeEvent("volcweap2",subelavera)


o=Bladex.CreateEntity("volcweap3","Lanza",-27218.103030,6684.342635,8902.091030,"Weapon")   # slightly moved up so that it no longer is static
o.Scale=1.000000
o.Orientation=0.675590,0.737277,0.000000,0.000000
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap4","Hacha2",-26781.642358,7950.292272,9829.534286,"Weapon")
o.Scale=1.000000
o.Orientation=0.663498,-0.223958,0.216482,-0.680256
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap5","Garrote",-29579.782108,7904.382556,16343.522406,"Weapon")
o.Scale=1.000000
o.Orientation=0.999687,0.009758,0.018195,0.014137
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap6","FireSword",-47287.864546,-9159.307884,31468.516466,"Weapon")
o.Scale=1.000000
o.Orientation=0.604709,0.394621,0.386723,-0.573626
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap7","Naginata2",-42754.852103,-11893.244721,10944.882427,"Weapon")
o.Scale=1.000000
o.Orientation=0.754234,0.645998,-0.069602,0.094730
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap8","Espadafilo",-49815.580243,-12028.420248,-13724.409759,"Weapon")
o.Scale=1.000000
o.Orientation=0.710364,0.703239,0.017240,0.023231
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("volcweap9","FireAxe",28485.585187,-5285.544888,-101545.860149,"Weapon")
o.Scale=1.000000
o.Orientation=0.906890,-0.001299,0.421248,-0.009901
ItemTypes.ItemDefaultFuncs(o)


o=Bladex.CreateEntity("VolcanArmorKF","ArmaduraCaballeroCompleta",-27964.999080,7050.162503,19906.909286,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Solid=0

