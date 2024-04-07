##///
##||| Barb_M1/TOTEM.PY TITANIUM
##||| Change list:
##||| * Changed sound events for totem cutscene.
##\\\ 

import Actions
import Sounds
import Scorer       # PLAGUE: Why are you even importing this?
import B3DLib       #           
import darfuncs

#char.Position = -97065.856439,-27037.893892,155774.699829

soundtotemhit=Sounds.CreateEntitySound('../../Sounds/golpe-madera-pesada.wav', 'SoundTotemHit')
soundtotemhit.Volume=0.9
soundtotemhit.MinDistance=10000
soundtotemhit.MaxDistance=20000

### Addedd soundtotemhit[2-3]   -LeadHead
soundtotemhit2=Sounds.CreateEntitySound('../../Sounds/golpe-roca-1.wav', 'SoundTotemHit2')
soundtotemhit2.Volume=1
soundtotemhit2.MinDistance=10000
soundtotemhit2.MaxDistance=20000

soundtotemhit3=Sounds.CreateEntitySound('../../Sounds/drawbridge-door-close.wav', 'SoundTotemHit3')
soundtotemhit3.Volume=0.9
soundtotemhit3.MinDistance=10000
soundtotemhit3.MaxDistance=20000

soundesfuerzo1=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-corto.wav', 'SoundEsfuerzo1')
soundesfuerzo1.Volume=0.5
soundesfuerzo1.MinDistance=10000
soundesfuerzo1.MaxDistance=20000

soundesfuerzo2=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-mediano.wav', 'SoundEsfuerzo2')
soundesfuerzo2.Volume=0.5
soundesfuerzo2.MinDistance=10000
soundesfuerzo2.MaxDistance=20000

soundesfuerzo3=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-largo.wav', 'SoundEsfuerzo3')
soundesfuerzo3.Volume=0.5
soundesfuerzo3.MinDistance=10000
soundesfuerzo3.MaxDistance=20000

soundcrujido1=Sounds.CreateEntitySound('../../Sounds/wood-bridge-creak2.wav', 'SoundCrujido1')  # was wood-bridge-creak.wav
soundcrujido1.Volume=0.6            # Was 1
soundcrujido1.MinDistance=10000
soundcrujido1.MaxDistance=20000

# soundcrujido2=Sounds.CreateEntitySound('../../Sounds/wood-bridge-creak2.wav', 'SoundCrujido2')    # Replaced sound
soundcrujido2=Sounds.CreateEntitySound('../../Sounds/m-subirmadera.wav', 'SoundCrujido2')           #       -LeadHead
soundcrujido2.Volume=1
soundcrujido2.MinDistance=10000
soundcrujido2.MaxDistance=20000


boingtotem=Bladex.CreateEntity("Totem","Boingtotem2",-95065.856439,-27037.893892,155774.699829)
boingtotem.RotateRel(0,0,0,1,0,0,1.57)
boingtotem.Alpha = 0.0

totem=Bladex.CreateEntity("Totem","Totem2",-95065.856439,-27037.893892,155774.699829)
totem.Orientation = (0.631790161133, 0.604139924049, -0.350825279951, -0.335824012756)
totem.Static=1

punterototem=Bladex.CreateEntity("Puntero Totem","GhostPointer",-95065.856439,-28527.893892,155774.699829)
punterototem.Static = 0
punterototem.Scale = 0.1
punterototem.UseFunc = ThrowTotem
darfuncs.SetHint(punterototem,"Totem Pole")