##///
##||| Ragnar_M2/pocimas.PY TITANIUM
##||| Change list:
##||| * spark pass
##||| * 500 life potion no longer stuck inside the gravestone in chapel
##\\\ 

import pocimac
import Ontake

## pocion 100 en habitacion con llave justo antes de puente levadizo

ragnarpocima100a=Bladex.CreateEntity("ragnarpocima100a","Pocima100",-122925.952125,-1418.87877109,8758.883719, "Physic")
ragnarpocima100a.Scale=1.000000
ragnarpocima100a.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("ragnarpocima100a")

## POCIMA TODO CERCA DE TRAMPA BOLAS DE FUEGO

o=Bladex.CreateEntity("ragnarpobolas","PocimaTodo",-81243.767885,5783.881910,-99921.271660, "Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("ragnarpobolas")



#######POWER POTION########

o=Bladex.CreateEntity("NoName0","Columna",-133189.016815,12653.427626,-98665.734525, "Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetStoneSparkling(o.Name) # Add
o.Static = 1


powp_PP=Bladex.CreateEntity("Ragnarpowp_PP","PowerPotion",-133164.352712,11720.650997,-98637.402867, "Physic")
powp_PP.Solid=1
powp_PP.Scale=1.321291
powp_PP.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePowerPotion("Ragnarpowp_PP")



###  POCIMA EN REPISA cercana a puente levadizo

poc50puente=Bladex.CreateEntity("poc50puente","Pocima50",-96350.590217,-12079.555047,-37234.815697, "Physic")
poc50puente.Scale=1.232392
poc50puente.Orientation=0.995087,-0.071664,-0.066593,-0.015237
pocimac.CreatePotion("poc50puente")
