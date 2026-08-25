##///
##||| AniSoundGdmX.PY TITANIUM
##||| Change list:
##||| * added gdm-quake
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************



TajoEmpalanteGdm=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteGdm')
TajoEmpalanteGdm.SendNotify=0
TajoCortanteGdm=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteGdm')
TajoCortanteGdm.SendNotify=0
TajoMutilacionGdm=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionGdm')
TajoMutilacionGdm.SendNotify=0

GolpeContundenteGdm=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteGdm')
GolpeContundenteGdm.SendNotify=0

SesgadoCortoGrave=Bladex.CreateSound('../../sounds/Sesgado-golem-11.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/Sesgado-golem-11.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0

EsfuerzoLargo1Gdm=Bladex.CreateSound('../../sounds/rugido-demon5.wav', 'EsfuerzoLargo1Gdm')
EsfuerzoLargo1Gdm.Volume=1
EsfuerzoLargo1Gdm.MinDistance=1000
EsfuerzoLargo1Gdm.MaxDistance=25000
EsfuerzoLargo1Gdm.SendNotify=0
EsfuerzoLargo2Gdm=Bladex.CreateSound('../../sounds/rugido-demon6.wav', 'EsfuerzoLargo2Gdm')
EsfuerzoLargo2Gdm.SendNotify=0
EsfuerzoLargo2Gdm.Volume=1
EsfuerzoLargo2Gdm.MinDistance=1000
EsfuerzoLargo2Gdm.MaxDistance=25000
EsfuerzoLargo3Gdm=Bladex.CreateSound('../../sounds/rugido-demon1.wav', 'EsfuerzoLargo3Gdm')
EsfuerzoLargo3Gdm.SendNotify=0
EsfuerzoLargo3Gdm.Volume=1
EsfuerzoLargo3Gdm.MinDistance=1000
EsfuerzoLargo3Gdm.MaxDistance=25000

EsfuerzoCorto1Gdm=Bladex.CreateSound('../../sounds/rugido-demon.wav', 'EsfuerzoCorto1Gdm')
EsfuerzoCorto1Gdm.SendNotify=0
EsfuerzoCorto1Gdm.Volume=1
EsfuerzoCorto1Gdm.MinDistance=1000
EsfuerzoCorto1Gdm.MaxDistance=25000
EsfuerzoCorto2Gdm=Bladex.CreateSound('../../sounds/rugido-demon2.wav', 'EsfuerzoCorto2Gdm')
EsfuerzoCorto2Gdm.SendNotify=0
EsfuerzoCorto2Gdm.Volume=1
EsfuerzoCorto2Gdm.MinDistance=1000
EsfuerzoCorto2Gdm.MaxDistance=25000
EsfuerzoCorto3Gdm=Bladex.CreateSound('../../sounds/rugido-demon3.wav', 'EsfuerzoCorto3Gdm')
EsfuerzoCorto3Gdm.SendNotify=0
EsfuerzoCorto3Gdm.Volume=1
EsfuerzoCorto3Gdm.MinDistance=1000
EsfuerzoCorto3Gdm.MaxDistance=25000

herida1Gdm=Bladex.CreateSound('../../sounds/herida-demon3.wav', 'herida1Gdm')
herida1Gdm.SendNotify=0
herida1Gdm.Volume=1
herida1Gdm.MinDistance=1000
herida1Gdm.MaxDistance=25000
herida2Gdm=Bladex.CreateSound('../../sounds/herida-demon2.wav', 'herida2Gdm')
herida2Gdm.SendNotify=0
herida2Gdm.Volume=1
herida2Gdm.MinDistance=1000
herida2Gdm.MaxDistance=25000

LanzarFuego1Gdm=Bladex.CreateSound('../../sounds/lanzar-fuego2.wav', 'LanzarFuego1Gdm')
LanzarFuego1Gdm.SendNotify=0
LanzarFuego1Gdm.Volume=1
LanzarFuego1Gdm.MinDistance=1000
LanzarFuego1Gdm.MaxDistance=25000
LanzarFuego2Gdm=Bladex.CreateSound('../../sounds/lanzar-fuego3.wav', 'LanzarFuego2Gdm')
LanzarFuego2Gdm.SendNotify=0
LanzarFuego2Gdm.Volume=1
LanzarFuego2Gdm.MinDistance=1000
LanzarFuego2Gdm.MaxDistance=25000

LanzarFuego3Gdm=Bladex.CreateSound('../../sounds/Gdm-lanzarfuego.wav', 'LanzarFuego3Gdm')
LanzarFuego3Gdm.SendNotify=0
LanzarFuego3Gdm.Volume=1
LanzarFuego3Gdm.MinDistance=1000
LanzarFuego3Gdm.MaxDistance=25000


MuerteGdm=Bladex.CreateSound('../../sounds/Gdm-muerte.wav', 'MuerteGdm')
MuerteGdm.SendNotify=0
MuerteGdm.Volume=1
MuerteGdm.MinDistance=1000
MuerteGdm.MaxDistance=25000

Fuego1=Bladex.CreateSound('../../sounds/fuego-boo.wav', 'Fuego1')
Fuego1.SendNotify=0
Fuego1.Volume=1
Fuego1.MinDistance=1000
Fuego1.MaxDistance=25000

Fuego2=Bladex.CreateSound('../../sounds/fuego-ascende.wav', 'Fuego2')
Fuego2.SendNotify=0
Fuego2.Volume=1
Fuego2.MinDistance=1000
Fuego2.MaxDistance=25000

# Add -LeadHead
gQuake=Bladex.CreateSound('../../sounds/gdm-quake3.wav', 'gQuake')
gQuake.SendNotify=0
gQuake.Volume=1
gQuake.MinDistance=15000
gQuake.MaxDistance=30000

RespiracionGdm1=Bladex.CreateSound('../../sounds/respira-demon.wav', 'RespiracionGdm1')
RespiracionGdm1.SendNotify=0
RespiracionGdm2=Bladex.CreateSound('../../sounds/respira-demon2.wav', 'RespiracionGdm2')
RespiracionGdm2.SendNotify=0

print "Sounds for the great demon created..."
