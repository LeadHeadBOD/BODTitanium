##///
##||| Ice_M11/jema.PY TITANIUM
##||| * Added twinkly effect to amulets so they they draw attention (and can actually be spotted on 4k resolutions)
##\\\ 
import darfuncs
import Sounds
import Ontake
import Stars

SndPosaMedallon=Sounds.CreateEntitySound("../../Sounds/Posa-medallon.wav","PosaMedallon")
SndPosaMedallon.MaxDistance=10000.0
SndPosaMedallon.Volume = 1.0

SndCreceLuz=Sounds.CreateEntitySound("../../Sounds/Blom5.wav","CreceLuz")
SndCreceLuz.MaxDistance=10000.0
SndCreceLuz.Volume = 1.0

punteromuro=Bladex.CreateEntity("DiscoMecanoGP","GhostPointer", 38330.902533,-9499.782781,-12002.560071)
punteromuro.Scale=1.000000
punteromuro.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(punteromuro,"Sacred Recess")
punteromuro.UseFunc = useInD1GhostP

punteromuro2=Bladex.CreateEntity("DiscoLocomiaGP","GhostPointer", -548.693162,-9480.186137,-12033.768141)
punteromuro2.Scale=1.000000
punteromuro2.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(punteromuro2,"Unholy Recess")
punteromuro2.UseFunc = useInD2GhostP


o=Bladex.CreateEntity("DiscoMecano","Amuletofantasma",26024.509359,-205.953120,2005.757495,"Physic")
o.Scale=1.000000
o.Orientation=0.024371,0.492730,-0.039419,-0.868947
darfuncs.SetHint(o,"Sacred Amulet")
Stars.Twinkle(o.Name)       # Add

o=Bladex.CreateEntity("DiscoLocomia","Amuleto",8872.661087,-38.401305,30163.854348,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.936990,-0.004181,-0.349331
darfuncs.SetHint(o,"Unholy Amulet")
Stars.Twinkle(o.Name)       # Add

Discografia = 2
CreatePartilcesMedallon()
AuraColor1=1.0, 0.7, 0.4
AuraColor2=1.0, 0.5, 0.3


Ontake.AddOnTakeEvent("DiscoLocomia", DetieneMusica)
