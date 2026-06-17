import Bladex
import EnemyTypes
import Damage
import math
import B3DLib



#######################
#     Preparacion     #
#######################


chaosk1=Bladex.CreateEntity("ChaosK1", "ChaosKnight", -114000.0, 0.0, -99500.0,"Person")
chaosk1.Angle=-3.14159/2.0
EnemyTypes.EnemyDefaultFuncs(chaosk1)
chaosk1.Blind=1
chaosk1.Deaf=1
chaosk1.Life=1000
chaosk1.DamageFunc=ChaosDamage

chaosk1.ActionAreaMin=pow(2,0)
chaosk1.ActionAreaMax=pow(2,1)

chaosk1.Data.DamageFactorNone=0.15
chaosk1.Data.DamageFactorLight=0.35
chaosk1.Data.DamageFactorHeavy=0.35
chaosk1.Data.PrepareWeapons("Espadon", "Escudon")
chaosk1.Data.PrepareDisappearance()
# chaosk1.Freeze()                          # commented out so he isn't floating mid-air and actually plays his idle anim -LeadHead




sectorcamarachk=Bladex.GetSector(-101500.0, 750.0, -94300.0)

sectorcamarachk.OnEnter=MueveCamaraChk


##################
#     Muerte     #
##################

TOTAL_TIME=8.0
TOTAL_STEPS=TOTAL_TIME*60.0
ANGLE_VARIATION=2.0*3.14159/TOTAL_STEPS


chaosk1.ImDeadFunc=MuereChaosK1

