##///
##||| DWFCOMBOS.PY TITANIUM
##||| Change list:
##||| * Changed Icehammer attack animation 
##\\\ 

######################################################
#
# Create sets of attacks
#
#        - DWF -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Dwf","g_08","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_01","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_01low_new","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_02","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_05","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_06","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_07","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_09","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_01a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_02a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_05a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_06a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_07a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_09a","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_18","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_15","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_14","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_13","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_16","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_11","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_12","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_17","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_21","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_22","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_23","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_26","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_27","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_31","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_punch1","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_punch2","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_kick","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_back","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_magic","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_magic2","ATTACKING")

Bladex.SetActionEventTable("Dwf","g_bad_sword1","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_bad_sword2","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_bad_sword3","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_bad_spear2","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_s18_2h","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_06lowkata_new","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_s3_new","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_s22low_new","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_32_5_3new","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_27kata","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_12low","ATTACKING")
Bladex.SetActionEventTable("Dwf","g_s11","ATTACKING")

# clumsy attacks
Bladex.SetActionEventTable("Dwf","g_bad_axe", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Dwf","g_bad_spear", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Dwf","g_bad_sword", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Dwf","g_bad_no", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Dwf","g_bad_1h", "ATTACKING_NOMOVE")

# Draw attacks
Bladex.SetActionEventTable("Dwf","g_draw_rlx", "ATTACKING")
Bladex.SetActionEventTable("Dwf","g_draw_run", "ATTACKING")

#Dodge->attacks
Bladex.SetActionEventTable("Dwf","g_d_r", "ATTACKING")
Bladex.SetActionEventTable("Dwf","g_d_l", "ATTACKING")

# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Dwf","D_r", "DODGING")
Bladex.SetActionEventTable("Dwf","D_l", "DODGING")
Bladex.SetActionEventTable("Dwf","D_b", "DODGING")

dwf=Bladex.GetCharType("Dwarf_N","Dwf_N")

#
#Dodge groups
#

#Dodges themselves
dwf.AddAttack("DR","D_r")
#dwf.AttackWindow("D_r",0.315,0.510,"GI_1H_Window") # O lo que sea
dwf.AttackTypeFlag("DR",ATK_UNIQUE) 

dwf.AddAttack("DL","D_l")
dwf.AttackTypeFlag("DL",ATK_UNIQUE) 

dwf.AddAttack("DB","D_b")
dwf.AttackTypeFlag("DB",ATK_UNIQUE) 

#Dodge attacks
dwf.AddAttack("DR_G_1H","g_d_r")
dwf.AssignTrail("DR_G_1H","","EstelaAmarilla1")
dwf.AddLevels("g_d_r",1,40)
dwf.AttackTypeFlag("DR",ATK_UNIQUE) 

dwf.AddAttack("DL_G_1H","g_d_l")
dwf.AssignTrail("DL_G_1H","","EstelaAmarilla1")
dwf.AddLevels("g_d_l",1,40)
dwf.AttackTypeFlag("DL",ATK_UNIQUE) 

#dwf.AddAttack("DB_G_1H","D_b_g")
#dwf.AttackTypeFlag("DB",ATK_UNIQUE) 




#GI "group"
dwf.AddAttack("GI_1H","Dwf_g_01")
dwf.AttackWindow("Dwf_g_01",0.001,0.999,"GI_1H_Window")

#dwf.AttackTypeFlag("GI_1H",ATK_SEQUENTIAL) #If only one attack given , UNIQUE flag is applied


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#COMBOALEATORIO1
dwf.AddAttack("GM43_1H","Dwf_g_26")
dwf.AttackWindow("Dwf_g_26",0.445,0.668,"GM43_1H_Window")
dwf.AssignTrail("GM43_1H","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_26",4,40)

#COMBOHACHATORPE group
dwf.AddAttack("GM1_AXE","Dwf_g_bad_axe")
dwf.AttackWindow("Dwf_g_bad_axe",0.435,0.643,"GM1_AXE_Window")
dwf.AssignTrail("GM1_AXE","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_axe",0,8)

#COMBOHACHATORPE2 group
dwf.AddAttack("GM7_AXE","Dwf_g_bad_spear")
dwf.AttackWindow("Dwf_g_bad_spear",0.461,0.748,"GM7_AXE_Window")
dwf.AssignTrail("GM7_AXE","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_spear",0,20)

#COMBOESPADATORPE1 group
dwf.AddAttack("GM2_2W","Dwf_g_bad_sword1")
dwf.AttackWindow("Dwf_g_bad_sword1",0.225,0.575,"GM2_2W_Window")
dwf.AssignTrail("GM2_2W","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_sword1",0,40)

#COMBOESPADATORPE2 group
dwf.AddAttack("GM3_2W","Dwf_g_bad_sword2")
dwf.AttackWindow("Dwf_g_bad_sword2",0.464,0.741,"GM3_2W_Window")
dwf.AssignTrail("GM3_2W","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_sword2",0,40)

#COMBOESPADATORPE2 group
dwf.AddAttack("GM4_2W","Dwf_g_bad_sword3")
dwf.AttackWindow("Dwf_g_bad_sword3",0.427,0.807,"GM4_2W_Window")
dwf.AssignTrail("GM4_2W","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_sword3",0,40)

#COMBOLANZATORPE1 group
dwf.AddAttack("GM5_SP","Dwf_g_bad_spear")
dwf.AttackWindow("Dwf_g_bad_spear",0.283,0.519,"GM5_SP_Window")
dwf.AssignTrail("GM5_SP","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_spear",0,40)

#COMBOLANZATORPE2 group
dwf.AddAttack("GM6_SP","Dwf_g_bad_spear2")
dwf.AttackWindow("Dwf_g_bad_spear2",0.461,0.748,"GM6_SP_Window")
dwf.AssignTrail("GM6_SP","","EstelaAmarilla1")
dwf.AddLevels("Dwf_g_bad_spear2",0,40)



##########################

#COMBO1
dwf.AddAttack("GM12_1H","Dwf_g_08")
dwf.AttackWindow("Dwf_g_08",0.408,0.725,"GM12_1H_Window")
dwf.AddLevels("Dwf_g_08",0,40)


#COMBO2
dwf.AddAttack("GM14_1H","Dwf_g_02")
dwf.AttackWindow("Dwf_g_02",0.265,0.586,"GM14_1H_Window")
dwf.AddLevels("Dwf_g_02",0,40)


#COMBO3
dwf.AddAttack("GM16_1H","Dwf_g_06")
dwf.AttackWindow("Dwf_g_06",0.391,0.661,"GM16_1H_Window")
dwf.AddLevels("Dwf_g_06",0,40)


#COMBO4
dwf.AddAttack("GM18_1H","Dwf_g_01low_new")
dwf.AttackWindow("Dwf_g_01low_new",0.001,0.900,"GM18_1H_Window")
dwf.AddLevels("Dwf_g_01low_new",0,40)



#GOLPESINARMA1 "group"
dwf.AddAttack("GM19_NO","Dwf_g_punch1")
dwf.AddLevels("Dwf_g_punch1",0,40)

#GOLPESINARMA2 "group"
dwf.AddAttack("GM20_NO","Dwf_g_punch2")
dwf.AddLevels("Dwf_g_punch2",0,40)

#GOLPESINARMA3 "group"
dwf.AddAttack("GM21_NO","Dwf_g_kick")
dwf.AddLevels("Dwf_g_kick",0,40)


#GOLPE GARROTE
dwf.AddAttack("GM30_1H","Dwf_g_14")
dwf.AttackWindow("Dwf_g_14",0.394,0.633,"GM30_1H_Window")
dwf.AssignTrail("GM30_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_14",2,40)

#GOLPE HACHA
dwf.AddAttack("GM31_1H","Dwf_g_15")
dwf.AttackWindow("Dwf_g_15",0.489,0.750,"GM31_1H_Window")
dwf.AssignTrail("GM31_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_15",3,40)

#GOLPE HACHA4
dwf.AddAttack("GM15_1H","Dwf_g_16")
dwf.AttackWindow("Dwf_g_16",0.471,0.784,"GM15_1H_Window")
dwf.AssignTrail("GM15_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_16",8,40)

#GOLPE MARTILLO
dwf.AddAttack("GM17_1H","Dwf_g_12")
dwf.AttackWindow("Dwf_g_12",0.420,0.656,"GM17_1H_Window")
dwf.AssignTrail("GM17_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_12",10,40)

#GOLPE MARTILLO2
dwf.AddAttack("GM13_1H","Dwf_g_18")
dwf.AttackWindow("Dwf_g_18",0.417,0.768,"GM13_1H_Window")
dwf.AssignTrail("GM13_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_18",11,40)

#GOLPE HACHA2
dwf.AddAttack("GM32_1H","Dwf_g_17")
dwf.AttackWindow("Dwf_g_17",0.454,0.668,"GM32_1H_Window")
dwf.AssignTrail("GM32_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_17",17,40)

#GOLPE MARTILLO3
dwf.AddAttack("GM22_1H","Dwf_g_31")
dwf.AttackWindow("Dwf_g_31",0.001,0.999,"GM22_1H_Window")
dwf.AssignTrail("GM22_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_31",18,40)

#GOLPE FIREAXE
dwf.AddAttack("GM24_1H","Dwf_g_22")
dwf.AttackWindow("Dwf_g_22",0.480,0.662,"GM24_1H_Window")
dwf.AssignTrail("GM24_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_22",17,40)

#GOLPE HACHA5
dwf.AddAttack("GM25_1H","Dwf_g_07")
dwf.AttackWindow("Dwf_g_07",0.001,0.900,"GM24_1H_Window")
dwf.AssignTrail("GM25_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_07",6,40)

#GOLPE GARROPIN
dwf.AddAttack("GM26_1H","Dwf_g_11")
dwf.AttackWindow("Dwf_g_11",0.001,0.900,"GM26_1H_Window")
dwf.AssignTrail("GM26_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_11",7,40)

#GOLPE HACHA3
dwf.AddAttack("GM27_1H","Dwf_g_05")
dwf.AttackWindow("Dwf_g_05",0.001,0.900,"GM27_1H_Window")
dwf.AssignTrail("GM27_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_05",9,40)

#GOLPE GARROTE2
dwf.AddAttack("GM28_1H","Dwf_g_13")
dwf.AttackWindow("Dwf_g_13",0.001,0.900,"GM28_1H_Window")
dwf.AssignTrail("GM28_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_13",13,40)

#GOLPE MAZADOBLE
dwf.AddAttack("GM29_1H","Dwf_g_21")
dwf.AttackWindow("Dwf_g_21",0.001,0.900,"GM29_1H_Window")
dwf.AssignTrail("GM29_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_21",14,40)

#GOLPE HACHA6
dwf.AddAttack("GM11_1H","Dwf_g_s3_new")
dwf.AttackWindow("Dwf_g_s3_new",0.001,0.900,"GM11_1H_Window")
dwf.AssignTrail("GM11_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_s3_new",15,40)

#GOLPE CRUSHHAMMER
dwf.AddAttack("GM10_1H","Dwf_g_s22low_new")
dwf.AttackWindow("Dwf_g_s22low_new",0.001,0.900,"GM10_1H_Window")
dwf.AssignTrail("GM10_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_s22low_new",16,40)

#GOLPE ICEHAMMER
dwf.AddAttack("GM9_1H","g_s18_2h")                          # Was "g_09"
dwf.AttackWindow("g_s18_2h",0.001,0.900,"GM9_1H_Window")    #
dwf.AssignTrail("GM9_1H","","EstelaAzul1")                  # was "EstelaRoja1"
dwf.AddLevels("g_s18_2h",12,40)                             #           -LeadHead

#GOLPE QUEENSWORD
dwf.AddAttack("GM8_1H","Dwf_g_06lowkata_new")
dwf.AttackWindow("Dwf_g_06lowkata_new",0.001,0.900,"GM8_1H_Window")
dwf.AssignTrail("GM8_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_06lowkata_new",10,40)

#COMBOGIRO180 group
dwf.AddAttack("GM33_1H","Dwf_g_back")
dwf.AddLevels("Dwf_g_back",3,40)
dwf.AddEnergyLevel("Dwf_g_back", 0)

#COMBO CONCENTRACION
dwf.AddAttack("GM70_1H","Dwf_g_magic")
dwf.AssignTrail("GM70_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_magic",19,40)
dwf.AddEnergyLevel("Dwf_g_magic", 0)

#COMBO LANZAESTELA
dwf.AddAttack("GM71_1H","Dwf_g_magic2")
dwf.AssignTrail("GM71_1H","","EstelaRoja1")
dwf.AddLevels("Dwf_g_magic2",18,40)
dwf.AddEnergyLevel("Dwf_g_magic2", 0)




#GAI meta-group
dwf.MetaAttack("GIM_1H","GI_1H")
dwf.MetaAttack("GIM_AXE","GM1_AXE")
dwf.MetaAttack("GIM_2W","GM2_2W")
dwf.MetaAttack("GIM_2W","GM3_2W")
dwf.MetaAttack("GIM_2W","GM4_2W")
dwf.MetaAttack("GIM_SP","GM5_SP")
dwf.MetaAttack("GIM_SP","GM6_SP")
dwf.MetaAttack("GIM_SP","GM7_AXE")
dwf.MetaAttack("GIM_1H","GM8_1H")
dwf.MetaAttack("GIM_1H","GM9_1H")
dwf.MetaAttack("GIM_1H","GM10_1H")
dwf.MetaAttack("GIM_1H","GM11_1H")
dwf.MetaAttack("GIM_1H","GM12_1H")
dwf.MetaAttack("GIM_1H","GM13_1H")
dwf.MetaAttack("GIM_1H","GM14_1H")
dwf.MetaAttack("GIM_1H","GM15_1H")
dwf.MetaAttack("GIM_1H","GM16_1H")
dwf.MetaAttack("GIM_1H","GM17_1H")
dwf.MetaAttack("GIM_1H","GM18_1H")
dwf.MetaAttack("GIM_NO","GM19_NO")
dwf.MetaAttack("GIM_NO","GM20_NO")
dwf.MetaAttack("GIM_NO","GM21_NO")
dwf.MetaAttack("GIM_1H","GM22_1H")
dwf.MetaAttack("GIM_1H","GM43_1H")
dwf.MetaAttack("GIM_1H","GM24_1H")
dwf.MetaAttack("GIM_1H","GM25_1H")
dwf.MetaAttack("GIM_1H","GM26_1H")
dwf.MetaAttack("GIM_1H","GM27_1H")
dwf.MetaAttack("GIM_1H","GM28_1H")
dwf.MetaAttack("GIM_1H","GM29_1H")
dwf.MetaAttack("GIM_1H","GM30_1H")
dwf.MetaAttack("GIM_1H","GM31_1H")
dwf.MetaAttack("GIM_1H","GM32_1H")
dwf.MetaAttack("GIM_1H","GM33_1H")
dwf.MetaAttack("GIM_1H","GM70_1H")
dwf.MetaAttack("GIM_1H","GM71_1H")


dwf.MetaAttack("COMBO1","GM1_AXE")
dwf.MetaAttack("COMBO1","GM2_2W")
dwf.MetaAttack("COMBO1","GM3_2W")
dwf.MetaAttack("COMBO1","GM4_2W")
dwf.MetaAttack("COMBO1","GM5_SP")
dwf.MetaAttack("COMBO1","GM6_SP")
dwf.MetaAttack("COMBO1","GM7_AXE")
dwf.MetaAttack("COMBO1","GM8_1H")
dwf.MetaAttack("COMBO1","GM9_1H")
dwf.MetaAttack("COMBO1","GM10_1H")
dwf.MetaAttack("COMBO1","GM11_1H")
dwf.MetaAttack("COMBO1","GM12_1H")
dwf.MetaAttack("COMBO1","GM13_1H")
dwf.MetaAttack("COMBO1","GM14_1H")
dwf.MetaAttack("COMBO1","GM15_1H")
dwf.MetaAttack("COMBO1","GM16_1H")
dwf.MetaAttack("COMBO1","GM17_1H")
dwf.MetaAttack("COMBO1","GM18_1H")
dwf.MetaAttack("COMBO1","GM19_NO")
dwf.MetaAttack("COMBO1","GM20_NO")
dwf.MetaAttack("COMBO1","GM21_NO")
dwf.MetaAttack("COMBO1","GM22_1H")
dwf.MetaAttack("COMBO1","GM43_1H")
dwf.MetaAttack("COMBO1","GM24_1H")
dwf.MetaAttack("COMBO1","GM25_1H")
dwf.MetaAttack("COMBO1","GM26_1H")
dwf.MetaAttack("COMBO1","GM27_1H")
dwf.MetaAttack("COMBO1","GM28_1H")
dwf.MetaAttack("COMBO1","GM29_1H")
dwf.MetaAttack("COMBO1","GM30_1H")
dwf.MetaAttack("COMBO1","GM31_1H")
dwf.MetaAttack("COMBO1","GM32_1H")
dwf.MetaAttack("COMBO1","GM33_1H")
dwf.MetaAttack("COMBO1","GM70_1H")
dwf.MetaAttack("COMBO1","GM71_1H")


######################################################
#
#        - Attacks themselves -
#
######################################################

# *Name of NEW attack (anm name itself , group name or metagroup)
# *Keys
#       R , L , F , B -> Control keys
#       A -> Attack 
#       D -> Defense(block)
#     
# -->Keys Modifiers
#       a+b . Simultaneous press
#       !c . Should not be pressed
#       &d . Should be already pressed
# *Previous Historial
#       "GA,GA,GM,GGF"
# *Previous NEGATIVE historial
#       +/- idem b4
#
#

#COMBOGIRO180
dwf.AllowAttack("GM33_1H","L+R+B","","","","1H")

#COMBO LANZAESTELA
dwf.AllowAttack("GM71_1H","&B","GI_1H","","","BladeSword2")

#COMBO CONCENTRACION
dwf.AllowAttack("GM70_1H","&A+F","GI_1H","","","BladeSword2")

#Golpes en esquiva
dwf.AllowAttack("DL_G_1H","A","DL","","","1H")

dwf.AllowAttack("DR_G_1H","A","DR","","","1H")

dwf.AllowAttack("DB_G_1H","A","DB","","","1H")

#COMBOHACHATORPE2
dwf.AllowAttack("GM7_AXE","A+R","","","GM7_AXE_Window","AXE")
dwf.AllowAttack("GM7_AXE","&A+R","","","GM7_AXE_Window","AXE")

#COMBOHACHATORPE1
dwf.AllowAttack("GM1_AXE","A","","","GM1_AXE_Window","AXE")

#COMBOESPADATORPE3
dwf.AllowAttack("GM4_2W","A","GM3_2W","","GM3_2W_Window","2W")

#COMBOESPADATORPE2
dwf.AllowAttack("GM3_2W","A","","COMBO1,COMBO1,COMBO1","GM4_2W_Window","2W")

#COMBOLANZATORPE2
dwf.AllowAttack("GM6_SP","A","GM5_SP","","GM5_SP_Window","SP")

#COMBOLANZATORPE1
dwf.AllowAttack("GM5_SP","A","","COMBO1,COMBO1,COMBO1","GM6_SP_Window","SP")


#GOLPESINARMA1
dwf.AllowAttack("GM19_NO","A","","COMBO1,COMBO1","","NO")

#GOLPESINARMA2
dwf.AllowAttack("GM20_NO","A+B","","COMBO1","","NO")
dwf.AllowAttack("GM20_NO","&A+B","","COMBO1","","NO")

#GOLPESINARMA3
dwf.AllowAttack("GM21_NO","A+F","","COMBO1","","NO")
dwf.AllowAttack("GM21_NO","&A+F","","COMBO1","","NO")



#GOLPEICEHAMMER
dwf.AllowAttack("GM9_1H","B+R","GI_1H","","GI_1H_Window","IceHammer")

#GOLPEFIREAXE
dwf.AllowAttack("GM24_1H","B+F","GM43_1H","","GM43_1H_Window","FireAxe")

#GOLPEHACHA6
dwf.AllowAttack("GM11_1H","&F","GI_1H","","GI_1H_Window","Hacha6")

#GOLPEMARTILLO
dwf.AllowAttack("GM17_1H","&B","GI_1H","","GI_1H_Window","Martillo")



#COMBOALEATORIO1
dwf.AllowAttack("GM43_1H","R+L","GI_1H","","GI_1H_Window","1H")



#COMBOARRIBA1
dwf.AllowAttack("GM12_1H","A+F","","GM12_1H","","1H")
dwf.AllowAttack("GM12_1H","&A+F","","GM12_1H","","1H")

#GOLPEHACHA
dwf.AllowAttack("GM31_1H","&B","GM12_1H","","GM12_1H_Window","Hacha")

#GOLPEGARROPIN
dwf.AllowAttack("GM26_1H","L+B","GM12_1H","","GM12_1H_Window","Garropin")

#GOLPEGARROTE2
dwf.AllowAttack("GM28_1H","&F","GM12_1H","","GM12_1H_Window","Garrote2")

#GOLPEMAZADOBLE
dwf.AllowAttack("GM29_1H","B+F","GM12_1H","","GM12_1H_Window","MazaDoble")

#GOLPE MARTILLO3
dwf.AllowAttack("GM22_1H","B+R","GM12_1H","","GM12_1H_Window","Martillo3")


#COMBODERECHA1
dwf.AllowAttack("GM14_1H","A+R","","GM14_1H","","1H")
dwf.AllowAttack("GM14_1H","&A+R","","GM14_1H","","1H")

#GOLPEHACHA5
dwf.AllowAttack("GM25_1H","L+B","GM14_1H","","GM14_1H_Window","Hacha5")

#GOLPEHACHA4
dwf.AllowAttack("GM15_1H","&L","GM14_1H","","GM14_1H_Window","Hacha4")

#GOLPEHACHA3
dwf.AllowAttack("GM27_1H","L+F","GM14_1H","","GM14_1H_Window","Hacha3")


#COMBOIZQUIERDA1
dwf.AllowAttack("GM16_1H","A+L","","GM16_1H","","1H")
dwf.AllowAttack("GM16_1H","&A+L","","GM16_1H","","1H")

#GOLPE HACHA2
dwf.AllowAttack("GM32_1H","&R","GM16_1H","","GM16_1H_Window","Hacha2")

#GOLPEQUEENSWORD
dwf.AllowAttack("GM8_1H","B+R","GM16_1H","","GM16_1H_Window","QueenSword")


#COMBOABAJO1
dwf.AllowAttack("GM18_1H","A+B","","GM18_1H","","1H")
dwf.AllowAttack("GM18_1H","&A+B","","GM18_1H","","1H")

#GOLPEGARROTE
dwf.AllowAttack("GM30_1H","&F","GM18_1H","","GM18_1H_Window","Garrote")

#GOLPEMARTILLO2
dwf.AllowAttack("GM13_1H","&B","GM18_1H","","GM18_1H_Window","Martillo2")

#GOLPECRUSHHAMMER
dwf.AllowAttack("GM10_1H","F+B","GM18_1H","","GM18_1H_Window","CrushHammer")


#GI
dwf.AllowAttack("GI_1H","A","","GIM_1H","GI_1H_Window","1H")










