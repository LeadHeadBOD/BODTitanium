##///
##||| Ruins_M4/BladeTraps.PY TITANIUM
##||| Change list:
##||| * Blade trap now 60fps
##\\\ 

import Bladex
import Sounds
import Objects
import InitDataField



MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8



###################
#     Objetos     #
###################


cuchilla1piramidenorte=Bladex.CreateEntity("Cuchilla1PiramideNorte","CuchillaFernando",6500.0,370.0,36450.0,"Weapon")
cuchilla1piramidenorte.Scale=0.96
cuchilla1piramidenorte.Orientation=1.000000,0.000000,0.000000,0.000000
cuchilla1piramidenorte.Frozen=1
cuchilla1piramidenorte.Solid=0
cuchilla1piramidenorte.CastShadows=0
InitDataField.Initialise(cuchilla1piramidenorte)
cuchilla1piramidenorte.Data.NoFXOnHit=1

cuchilla2piramidenorte=Bladex.CreateEntity("Cuchilla2PiramideNorte","CuchillaFernando",6500.0,1370.0,43550.0,"Weapon")
cuchilla2piramidenorte.Scale=0.96
cuchilla2piramidenorte.Orientation=1.000000,0.000000,0.000000,0.000000
cuchilla2piramidenorte.Frozen=1
cuchilla2piramidenorte.Solid=0
cuchilla2piramidenorte.CastShadows=0
InitDataField.Initialise(cuchilla2piramidenorte)
cuchilla2piramidenorte.Data.NoFXOnHit=1

cuchilla3piramidenorte=Bladex.CreateEntity("Cuchilla3PiramideNorte","CuchillaFernando",-6500.0,1370.0,43550.0,"Weapon")
cuchilla3piramidenorte.Scale=0.96
cuchilla3piramidenorte.Orientation=1.000000,0.000000,0.000000,0.000000
cuchilla3piramidenorte.Frozen=1
cuchilla3piramidenorte.Solid=0
cuchilla3piramidenorte.CastShadows=0
InitDataField.Initialise(cuchilla3piramidenorte)
cuchilla3piramidenorte.Data.NoFXOnHit=1

cuchilla4piramidenorte=Bladex.CreateEntity("Cuchilla4PiramideNorte","CuchillaFernando",-6500.0,370.0,36450.0,"Weapon")
cuchilla4piramidenorte.Scale=0.96
cuchilla4piramidenorte.Orientation=1.000000,0.000000,0.000000,0.000000
cuchilla4piramidenorte.Frozen=1
cuchilla4piramidenorte.Solid=0
cuchilla4piramidenorte.CastShadows=0
InitDataField.Initialise(cuchilla4piramidenorte)
cuchilla4piramidenorte.Data.NoFXOnHit=1



###################
#     Sonidos     #
###################


sonidoactivacioncuchillas=Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActivacionCuchillas')
sonidoactivacioncuchillas.Volume=1.0
sonidoactivacioncuchillas.MinDistance=2000
sonidoactivacioncuchillas.MaxDistance=20000

sonidosalidacuchilla=Sounds.CreateEntitySound('../../Sounds/blade-trap.wav', 'SonidoSalidaCuchilla')
sonidosalidacuchilla.Volume=1.0
sonidosalidacuchilla.MinDistance=2000
sonidosalidacuchilla.MaxDistance=20000



##########################################
#     Cuchillas de la piramide norte     #
##########################################


VUELTASDURANTE=100*(2*3.14159)
VUELTASINICIO=3*(2*3.14159)
VUELTASFIN=6*(2*3.14159)
VELGIRO=16.0

cuchilla1piramidenortedin=Objects.CreateDinamicObject("Cuchilla1PiramideNorte")
cuchilla2piramidenortedin=Objects.CreateDinamicObject("Cuchilla2PiramideNorte")
cuchilla3piramidenortedin=Objects.CreateDinamicObject("Cuchilla3PiramideNorte")
cuchilla4piramidenortedin=Objects.CreateDinamicObject("Cuchilla4PiramideNorte")
cuchilla1piramidenortedin.Timer="Timer60"       # was timer30
cuchilla2piramidenortedin.Timer="Timer60"       #       -LeadHead
cuchilla3piramidenortedin.Timer="Timer60"
cuchilla4piramidenortedin.Timer="Timer60"

######### Funcion: GiraCuchillas()

######### Funcion: IniciaGiraCuchillas()

######### Funcion: TerminaGiraCuchillas()

######### Funcion: LanzaCuchilla(ncuchilla)

######### Funcion: RecogeCuchilla(ncuchilla)

######### Funcion: LanzaTrampaCuchillas()

######### Funcion: ParaTrampaCuchillas(sector_index, entity_name)

sector1paracuchillas=Bladex.GetSector(12750, -1000.0, 40000.0)
sector2paracuchillas=Bladex.GetSector(-12750, -1000.0, 40000.0)
