##///
##||| TOMB_M7/BGATES.PY TITANIUM
##||| Change list:
##||| * Changed the breaking sound of the 2 secret walls.
##\\\ 

##################################################################
# Puertas que se rompen
#
# YUio
##################################################################

import Reference
import Select
import Change
import Actions
#import AniSound
import Sounds

# break_sound=Sounds.CreateEntitySound('../../Sounds/madera-rotura-pesada.wav', 'SonidoDesprendimiento')
break_sound=Sounds.CreateEntitySound('../../Sounds/Stone-floor-collapse.wav', 'SonidoDesprendimiento') # Original was basically inaudible and boring -LeadHead
break_sound.Volume=1.0
break_sound.MinDistance=5000
break_sound.MaxDistance=10000

### PLAGUE: Literally unused sounds, wtf
# hit_sound=Sounds.CreateEntitySound('../../Sounds/golpe-madera-pesada.wav', 'SonidoHit')
# hit_sound.Volume=1.0
# hit_sound.MinDistance=5000
# hit_sound.MaxDistance=10000

bgateA1=Bladex.GetSector(31000,-2000,53875)
bgateA2=Bladex.GetSector(32000,-2000,53875)
bgateB1=Bladex.GetSector(41000,-2000,53875)
bgateB2=Bladex.GetSector(42000,-2000,53875)
bgateA1.Active=0
bgateA2.Active=0
bgateB1.Active=0
bgateB2.Active=0
bgateA1.InitBreak( (0,0,250),(600,120,0),(0,1000,0),'piedra ligera')    # Added
bgateA2.InitBreak( (0,0,250),(600,0,0),(0,1200,0),'piedra pesada')
bgateB1.InitBreak( (0,0,250),(600,0,0),(0,1000,0),'piedra ligera')      # Added -LeadHead
bgateB2.InitBreak( (0,0,250),(600,120,0),(0,1200,0),'piedra pesada')



vidapuertaA = 3
vidapuertaB = 3

bgateA=Bladex.GetSector(31000,-2000,53000)
bgateB=Bladex.GetSector(41000,-2000,53000)


bgateA.ActiveSurface= 0, 0.0, -1
bgateA.OnHit=revientaPuertaA
bgateB.ActiveSurface= 0, 0.0, -1
bgateB.OnHit=revientaPuertaB