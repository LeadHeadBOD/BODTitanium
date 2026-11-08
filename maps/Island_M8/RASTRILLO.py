import Objects

#o=Bladex.CreateEntity("NoName0","Rastrillo",-156289.875595,-2653.0,12203.090752)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.621418,0.621418,0.337402,-0.337402
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


############################################################
#####--RASTRILLO---entrada----#########################
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja3=Bladex.CreateEntity("Reja3","Rastrillo",-156289.875595,-2653.0,12203.090752)
reja3.Static=1
reja3.Scale=1.0
reja3.Orientation=0.621418,0.621418,0.337402,-0.337402
Sparks.SetMetalSparkling("Reja3")

reja3din=Objects.CreateDinamicObject("Reja3")

##funciones abrir-cerrar##


ladosCerrados=1


s1=Bladex.GetSector(-150000,0,17000)
s1.OnEnter=Cierralados