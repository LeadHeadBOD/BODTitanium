import Bladex
import AuxFuncs
import EnemyTypes
import Actions
import Objects
import Sounds
import LevelFuncs
import copy
import CharStats

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)



### Objetos

ptronco1=Bladex.CreateEntity("PTronco1","TroncoTrampa",42800.0,-33450.0,92200.0,"Physic")
ptronco1.Scale=1.000000
ptronco1.Orientation=0.500000,0.500000,-0.500000,-0.500000
ptronco1=Sparks.SetWoodenSparkling("PTronco1")
ptronco1.Frozen=1

ptronco2=Bladex.CreateEntity("PTronco2","TroncoTrampa",43575.0,-33400.0,91732.0,"Physic")
ptronco2.Scale=1.000000
ptronco2.Orientation=0.500000,0.500000,-0.500000,-0.500000
ptronco2=Sparks.SetWoodenSparkling("PTronco2")
ptronco2.Frozen=1

ptronco3=Bladex.CreateEntity("PTronco3","TroncoTrampa",44245.0,-33650.0,91109.0,"Physic")
ptronco3.Scale=1.000000
ptronco3.Orientation=0.500000,0.500000,-0.500000,-0.500000
ptronco3=Sparks.SetWoodenSparkling("PTronco3")
ptronco3.Frozen=1

ptronco4=Bladex.CreateEntity("PTronco4","TroncoTrampa",44997.0,-33540.0,90563.0,"Physic")
ptronco4.Scale=1.000000
ptronco4.Orientation=0.500000,0.500000,0.500000,0.500000
ptronco4=Sparks.SetWoodenSparkling("PTronco4")
ptronco4.Frozen=1

ptronco1din=Objects.CreateDinamicObject("PTronco1")
ptronco2din=Objects.CreateDinamicObject("PTronco2")
ptronco3din=Objects.CreateDinamicObject("PTronco3")
ptronco4din=Objects.CreateDinamicObject("PTronco4")


### Sonidos

desliztronco1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizTronco1")
#desliztronco2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizTronco2")
#desliztronco3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizTronco3")
desliztronco4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizTronco4")

GeneradorGlm=Bladex.CreateSound('../../sounds/M-GENERADOR-ENTIERRA3.wav', 'GeneradorGolem')
GeneradorGlm.Volume=1
GeneradorGlm.MinDistance=5000
GeneradorGlm.MaxDistance=20000

### Funcionamiento

ejey=(0.0, 1.0, 0.0)

######## Funcion: NieveTroncos()

######## Funcion: BajaTroncos(person)

######## Funcion: ParaCamaraGolem(camera, frame)

######## Funcion: GolemListo(person)

######## Funcion: LevantaGolem()

######## Funcion: AparicionGolem(tr_sector, ent_name)

Bladex.SetTriggerSectorFunc("SalidaFort", "OnEnter", AparicionGolem)


### Creacion del Golem

golem=Bladex.CreateEntity("Golem", "Golem_ice", 0, 0, 0, "Person")
golem.Angle=3.14159
golem.Level=lvl_control.GiveLevel(3,8)
EnemyTypes.EnemyDefaultFuncs(golem)
golem.Blind=1
golem.Deaf=1


""" Not needed anymore, since golem is a valid enemy type and does not need this king of hackery
ag=Bladex.CreateEntity("AuraGolem", "Entity Aura", 0, 0, 0)
ag.SetAuraParams(50, 1, 1, 0, 0, 1)
ag.SetAuraGradient(2, 0.9, 1.0, 1.0, 0.2, 0.1, 0.4, 0.8, 1.0, 0.0, 0.8)
golem.Link(ag)
ag.SetAuraActive(1)"""

golem.ImDeadFunc=BajaTroncos
golem.Freeze()
golem.RemoveFromWorld()


######## Funcion: repgolem()


######## Funcion: CierraPorton(sec_index, ent_name)

sectorcierraporton=Bladex.GetSector(49000.0, -33000.0, 98000.0)

sectorcierraporton.OnEnter=CierraPorton
