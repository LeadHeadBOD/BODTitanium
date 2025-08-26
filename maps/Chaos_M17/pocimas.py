##///
##||| CHAOS_M17/pocimas.PY TITANIUM
##||| Change list:
##||| * Power potions no longer float above surface.
##\\\ 

import pocimac


o=Bladex.CreateEntity("PowerChaos1","PowerPotion",362967.423909, 48796.1618598, -40086.3391115,"Physic")
o.Scale=1.000000
o.Orientation=0.105317,-0.989789,0.012771,-0.095203
pocimac.CreatePowerPotion("PowerChaos1")

o=Bladex.CreateEntity("TodoChaos1","PocimaTodo",351399.770000,44785.790579,-84921.519875,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("TodoChaos1")