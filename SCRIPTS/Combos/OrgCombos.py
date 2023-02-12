##///
##||| ORGCOMBOS.PY TITANIUM
##||| Change list:
##||| * Created (effectively copy-paste of regular orc)
##||| 
##\\\ 

######################################################
#
# Create sets of attacks
#
#        - GOLD ORC -
#
######################################################



import Bladex


ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Org","g_01","ATTACKING")
Bladex.SetActionEventTable("Org","g_02","ATTACKING")
Bladex.SetActionEventTable("Org","g_06","ATTACKING")
Bladex.SetActionEventTable("Org","g_15","ATTACKING")
Bladex.SetActionEventTable("Org","g_16","ATTACKING")
Bladex.SetActionEventTable("Org","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Org","D_r", "DODGING")
Bladex.SetActionEventTable("Org","D_l", "DODGING")
Bladex.SetActionEventTable("Org","D_b", "DODGING")

org=Bladex.GetCharType("Gold_Ork","Org")

####################
# GRUPOS DE GOLPES #
####################
org.AddAttack("g_01","Ork_g_01")
org.AttackTypeFlag("g_01",ATK_UNIQUE)

org.AddAttack("g_02","Ork_g_02")
org.AttackTypeFlag("g_02",ATK_UNIQUE)

org.AddAttack("g_06","Ork_g_06")
org.AttackTypeFlag("g_06",ATK_UNIQUE)

org.AddAttack("g_15","Ork_g_15")
org.AssignTrail("g_15","","EstelaAmarilla1")
org.AttackTypeFlag("g_15",ATK_UNIQUE)

org.AddAttack("g_16","Ork_g_16")
org.AssignTrail("g_16","","EstelaAmarilla1")
org.AttackTypeFlag("g_16",ATK_UNIQUE)

org.AddAttack("g_18","Ork_g_18")
org.AssignTrail("g_18","","EstelaRoja1")
org.AttackTypeFlag("g_18",ATK_UNIQUE)

org.AttackTypeFlag("COMBO1",ATK_SEQUENTIAL)
org.AddAttack("COMBO1","Ork_g_06")
org.AddAttack("COMBO1","Ork_g_02")
org.AddAttack("COMBO1","Ork_g_18")

org.AttackTypeFlag("COMBO2",ATK_SEQUENTIAL)
org.AddAttack("COMBO2","Ork_g_16")
org.AddAttack("COMBO2","Ork_g_01")

org.AttackTypeFlag("COMBO3",ATK_SEQUENTIAL)
org.AddAttack("COMBO3","Ork_g_02")
org.AddAttack("COMBO3","Ork_g_06")
org.AddAttack("COMBO3","Ork_g_01")

###############################
# GRUPO PARA ESCALERAS        #
###############################
org.AddAttack("STAIRS","Ork_g_16")
org.AssignTrail("STAIRS","","EstelaAmarilla1")
org.AddAttack("STAIRS","Ork_g_18")
org.AssignTrail("STAIRS","","EstelaRoja1")
org.AttackTypeFlag("STAIRS",ATK_RANDOM)






