##///
##||| SPDCOMBOS.PY TITANIUM
##||| Change list:
##||| * Attacks can no longer instantly break shields
##\\\ 

######################################################
#
# Create sets of attacks
#
#        - Spidersmall -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Spd","g_01","ATTACKING")
Bladex.SetActionEventTable("Spd","g_spit","ATTACKING")


spd=Bladex.GetCharType("Spidersmall","Spd")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

spd.AddAttack("GA","Spd_g_01")
spd.AttackWindow("Spd_g_01",5,15,"GA_Window")
spd.AttackTypeFlag("GA",ATK_UNIQUE)
#spd.AddLevels("Spd_g_01",0,0)          # Commented out to prevent from instantly breaking shields. -LeadHead
spd.AllowAttack("GA","A","","","")

#SP group
spd.AddAttack("SP","Spd_g_spit")
spd.AttackWindow("Spd_g_spit",5,15,"GA_Window")
spd.AttackTypeFlag("SP",ATK_UNIQUE)
#spd.AddLevels("Spd_g_spit",0,0)        # Commented out to prevent from instantly breaking shields. -LeadHead
