##///
##||| Btomb_M12/Collaps.PY TITANIUM
##||| Change list:
##||| * Break sound louder
##||| * Breakpieces have material now
##\\\ 

import Bladex


MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8
MESSAGE_SETSTATICWEPONMODE=13

# char.Position = 326290,-3119,-149061

########################
#     Muros falsos     #
########################

### Sonidos

sonidoroturamurofalso=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaMuroFalso")
sonidoroturamurofalso.Volume=1.0
sonidoroturamurofalso.MinDistance=10000
sonidoroturamurofalso.MaxDistance=40000


#sectores dentro del derrum
sectorbarrote=Bladex.GetSector(340000,1000,-157000)
sectorbarrote.Active=0
sectorsecreto=Bladex.GetSector(342000,0,-148000)
sectorsecreto.Active=0
sectorbarrote2=Bladex.GetSector(329500,0,-181500)
sectorbarrote2.Active=0
#sectorbarrote3=Bladex.GetSector(335000,4000,-234500)
#sectorbarrote3.Active=0
#sectorbarrote4=Bladex.GetSector(333500,0,-183000)
#sectorbarrote4.Active=0


#sectores fuera del derrumb
sectorrompebarrote=Bladex.GetSector(339753.3,0,-156939.3)
sectorrompebarroteb=Bladex.GetSector(340000,0,-156000)
sectorrompebarrotec=Bladex.GetSector(340000,0,-158000)
sectorrompesecreto=Bladex.GetSector(341500,0,-148000)
sectorrompebarrote2=Bladex.GetSector(329100,0,-181500)
sectorrompebarrote2b=Bladex.GetSector(329500,0,-182250)
sectorrompebarrote2c=Bladex.GetSector(329500,0,-181125)
#sectorrompebarrote3=Bladex.GetSector(335400,4000,-234500)
#sectorrompebarrote4=Bladex.GetSector(333100,0,-183000)

## que narices es esto???
sectorrompebarrote.ActiveSurface=-1.0, 0.0, 0.0
sectorrompebarroteb.ActiveSurface=-1.0, 0.0, 0.0
sectorrompebarrotec.ActiveSurface=-1.0, 0.0, 0.0
sectorrompesecreto.ActiveSurface=-1.0, 0.0, 0.0
sectorrompebarrote2.ActiveSurface=-1.0, 0.0, 0.0
sectorrompebarrote2b.ActiveSurface=-1.0, 0.0, 0.0
sectorrompebarrote2c.ActiveSurface=-1.0, 0.0, 0.0
#sectorrompebarrote3.ActiveSurface=1.0, 0.0, 0.0
#sectorrompebarrote4.ActiveSurface=-1.0, 0.0, 0.0


### Added materials to these -LeadHead
sectorbarrote.InitBreak(  (250.0, 0.0, 0.0), (0.0, 200.0, 800.0), (-200.0, 800.0, 0.0), 'piedra ligera')
sectorsecreto.InitBreak(  (250.0, 0.0, 0.0), (0.0, 200.0, 800.0), (-200.0, 800.0, 0.0), 'piedra mediana')
sectorbarrote2.InitBreak( (250.0, 0.0, 0.0), (0.0, 200.0, 800.0), (-200.0, 800.0, 0.0), 'piedra ligera')
# sectorbarrote3.InitBreak( (250.0, 0.0, 0.0), (0.0, 200.0, 800.0), (-200.0, 800.0, 0.0), 'piedra ligera')
# sectorbarrote4.InitBreak( (250.0, 0.0, 0.0), (0.0, 200.0, 800.0), (-200.0, 800.0, 0.0), 'piedra ligera')

### Optimization -LeadHead
sectorGroupBarrote  = (sectorrompebarrote.Index,  sectorrompebarroteb.Index,  sectorrompebarrotec.Index)
sectorGroupBarrote2 = (sectorrompebarrote2.Index, sectorrompebarrote2b.Index, sectorrompebarrote2c.Index)

sectorrompebarrote.OnHit=RompeMuroFalso
sectorrompebarroteb.OnHit=RompeMuroFalso
sectorrompebarrotec.OnHit=RompeMuroFalso
sectorrompesecreto.OnHit=RompeMuroFalso
sectorrompebarrote2.OnHit=RompeMuroFalso
sectorrompebarrote2b.OnHit=RompeMuroFalso
sectorrompebarrote2c.OnHit=RompeMuroFalso
#sectorrompebarrote3.OnHit=RompeMuroFalso
#sectorrompebarrote4.OnHit=RompeMuroFalso