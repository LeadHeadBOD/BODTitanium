##///
##||| DOKCOMBOS.PY TITANIUM
##||| Change list:
##||| * Adjusted to prevent console spam and have combo attacks (effectively copy-paste of regular orc)
##||| 
##\\\ 

######################################################
#
# Create sets of attacks
#
#        - DARK ORK -
#
######################################################



import Bladex


ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Dok","g_01","ATTACKING")
Bladex.SetActionEventTable("Dok","g_02","ATTACKING")
Bladex.SetActionEventTable("Dok","g_06","ATTACKING")
Bladex.SetActionEventTable("Dok","g_15","ATTACKING")
Bladex.SetActionEventTable("Dok","g_16","ATTACKING")
Bladex.SetActionEventTable("Dok","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Dok","D_r", "DODGING")
Bladex.SetActionEventTable("Dok","D_l", "DODGING")
Bladex.SetActionEventTable("Dok","D_b", "DODGING")

dok=Bladex.GetCharType("Dark_Ork","Dok")

####################
# GRUPOS DE GOLPES #
####################
dok.AddAttack("g_01","Ork_g_01")
dok.AttackTypeFlag("g_01",ATK_UNIQUE)

dok.AddAttack("g_02","Ork_g_02")
dok.AttackTypeFlag("g_02",ATK_UNIQUE)

dok.AddAttack("g_06","Ork_g_06")
dok.AttackTypeFlag("g_06",ATK_UNIQUE)

dok.AddAttack("g_15","Ork_g_15")
dok.AssignTrail("g_15","","EstelaAmarilla1")
dok.AttackTypeFlag("g_15",ATK_UNIQUE)

dok.AddAttack("g_16","Ork_g_16")
dok.AssignTrail("g_16","","EstelaAmarilla1")
dok.AttackTypeFlag("g_16",ATK_UNIQUE)

dok.AddAttack("g_18","Ork_g_18")
dok.AssignTrail("g_18","","EstelaRoja1")
dok.AttackTypeFlag("g_18",ATK_UNIQUE)

dok.AttackTypeFlag("COMBO1",ATK_SEQUENTIAL)
dok.AddAttack("COMBO1","Ork_g_06")
dok.AddAttack("COMBO1","Ork_g_02")
dok.AddAttack("COMBO1","Ork_g_18")

dok.AttackTypeFlag("COMBO2",ATK_SEQUENTIAL)
dok.AddAttack("COMBO2","Ork_g_16")
dok.AddAttack("COMBO2","Ork_g_01")

dok.AttackTypeFlag("COMBO3",ATK_SEQUENTIAL)
dok.AddAttack("COMBO3","Ork_g_02")
dok.AddAttack("COMBO3","Ork_g_06")
dok.AddAttack("COMBO3","Ork_g_01")

###############################
# GRUPO PARA ESCALERAS        #
###############################
dok.AddAttack("STAIRS","Ork_g_16")
dok.AssignTrail("STAIRS","","EstelaAmarilla1")
dok.AddAttack("STAIRS","Ork_g_18")
dok.AssignTrail("STAIRS","","EstelaRoja1")
dok.AttackTypeFlag("STAIRS",ATK_RANDOM)




