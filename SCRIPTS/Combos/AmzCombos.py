##///
##||| AMZCOMBOS.PY TITANIUM
##||| Change list:
##||| * Changed IceWand trail
##\\\ 

######################################################
#
# Create sets of attacks
#
#        - AMZ -
#
######################################################


import Bladex


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Amz","g_01","ATTACKING")
Bladex.SetActionEventTable("Amz","g_02","ATTACKING")
Bladex.SetActionEventTable("Amz","g_05","ATTACKING")
Bladex.SetActionEventTable("Amz","g_06","ATTACKING")
Bladex.SetActionEventTable("Amz","g_07","ATTACKING")
Bladex.SetActionEventTable("Amz","g_09","ATTACKING")
Bladex.SetActionEventTable("Amz","g_01a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_02a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_05a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_06a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_07a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_09a","ATTACKING")
Bladex.SetActionEventTable("Amz","g_13","ATTACKING")
Bladex.SetActionEventTable("Amz","g_14","ATTACKING")
Bladex.SetActionEventTable("Amz","g_16","ATTACKING")
Bladex.SetActionEventTable("Amz","g_17","ATTACKING")
Bladex.SetActionEventTable("Amz","g_21","ATTACKING")
Bladex.SetActionEventTable("Amz","g_22","ATTACKING")
Bladex.SetActionEventTable("Amz","g_23","ATTACKING")
Bladex.SetActionEventTable("Amz","g_26","ATTACKING")
Bladex.SetActionEventTable("Amz","g_27","ATTACKING")
Bladex.SetActionEventTable("Amz","g_31","ATTACKING")
Bladex.SetActionEventTable("Amz","g_punch2","ATTACKING")
Bladex.SetActionEventTable("Amz","g_kick1","ATTACKING")
Bladex.SetActionEventTable("Amz","g_kick2","ATTACKING")
Bladex.SetActionEventTable("Amz","g_kick3","ATTACKING")
Bladex.SetActionEventTable("Amz","g_kick5","ATTACKING")
Bladex.SetActionEventTable("Amz","g_magic","ATTACKING")
Bladex.SetActionEventTable("Amz","g_magic2","ATTACKING")

Bladex.SetActionEventTable("Amz","g_spears1","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_sb11","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear26kata","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear08","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear17","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear16","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear19_13","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear19","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_b06","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_bs21","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear111","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_kata23","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_b6_26","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear33","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_21","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear13","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear09","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_b29","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spears8","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear12","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear22","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear02","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spears6","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear3s2","ATTACKING")
Bladex.SetActionEventTable("Amz","g_3s9_6new","ATTACKING")
Bladex.SetActionEventTable("Amz","g_12_7_s1new","ATTACKING")
Bladex.SetActionEventTable("Amz","g_28new","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear19_bs1","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear32kata_b2","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear16low","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_2katab6low","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear02low","ATTACKING")
Bladex.SetActionEventTable("Amz","g_spear_back","ATTACKING")
Bladex.SetActionEventTable("Amz","g_27kata_new","ATTACKING")
Bladex.SetActionEventTable("Amz","g_06lowkata_new","ATTACKING")


# clumsy attacks
Bladex.SetActionEventTable("Amz","g_bad_axe", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_spear", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_sword", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_no", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_1h", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_sword2","ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Amz","g_bad_sword3","ATTACKING_NOMOVE")

# Draw attacks
Bladex.SetActionEventTable("Amz","g_draw_rlx", "ATTACKING")
Bladex.SetActionEventTable("Amz","g_draw_run", "ATTACKING")

# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Amz","D_r", "DODGING")
Bladex.SetActionEventTable("Amz","D_l", "DODGING")
Bladex.SetActionEventTable("Amz","D_b", "DODGING")

amz=Bladex.GetCharType("Amazon_N","Amz_N")

#GI "group"
amz.AddAttack("GI_SP","Amz_g_spears1")
amz.AttackWindow("Amz_g_spears1",0.334,0.642,"GI_SP_Window")
#amz.AttackTypeFlag("GI_SP",ATK_UNIQUE) #If only one attack given , UNIQUE flag is applied


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################


#COMBO1 group
amz.AddAttack("GM1_SP","Amz_g_spear08")
amz.AttackWindow("Amz_g_spear08",0.121,0.496,"GM1_SP_Window")
amz.AddLevels("Amz_g_spear08",0,40)

#COMBO2 group
amz.AddAttack("GM3_SP","Amz_g_spear12")
amz.AttackWindow("Amz_g_spears12",0.183,0.448,"GM3_SP_Window")
amz.AddLevels("Amz_g_spears12",0,40)


#COMBO3 group
amz.AddAttack("GM6_SP","Amz_g_spears6")
amz.AttackWindow("Amz_g_spears6",0.345,0.454,"GM6_SP_Window")
amz.AddLevels("Amz_g_spears6",0,40)


#COMBO4 group
amz.AddAttack("GM8_SP","Amz_g_spear16low")
amz.AttackWindow("Amz_g_spear16low",0.341,0.475,"GM8_SP_Window")
amz.AddLevels("Amz_g_spear16low",0,40)



#EXTRAGOLPE1 group
amz.AddAttack("GM15_SP","Amz_g_spear26kata")
amz.AttackWindow("Amz_g_spear26kata",0.626,0.781,"GM15_SP_Window")
amz.AssignTrail("GM15_SP","","EstelaAmarilla1")
amz.AddLevels("Amz_g_spear26kata",1,40)



#COMBOHACHATORPE group
amz.AddAttack("GM11_AXE","Amz_g_bad_axe")
amz.AttackWindow("Amz_g_bad_axe",0.435,0.643,"GM11_AXE_Window")
amz.AssignTrail("GM11_AXE","","EstelaAmarilla1")
amz.AddLevels("Amz_g_bad_axe",0,12)

#COMBOESPADATORPE1 group
amz.AddAttack("GM12_2W","Amz_g_bad_sword")
amz.AttackWindow("Amz_g_bad_sword",0.225,0.575,"GM12_2W_Window")
amz.AddLevels("Amz_g_bad_sword",0,40)

#COMBOESPADATORPE2 group
amz.AddAttack("GM13_2W","Amz_g_bad_sword2")
amz.AttackWindow("Amz_g_bad_sword2",0.464,0.741,"GM13_2W_Window")
amz.AddLevels("Amz_g_bad_sword2",0,40)

#COMBOESPADATORPE2 group
amz.AddAttack("GM14_2W","Amz_g_bad_sword3")
amz.AttackWindow("Amz_g_bad_sword3",0.427,0.807,"GM14_2W_Window")
amz.AddLevels("Amz_g_bad_sword3",0,40)



#GOLPEARMA1MANO1 group
amz.AddAttack("GM16_1H","Amz_g_09")
amz.AddLevels("Amz_g_09",0,40)

#GOLPEARMA1MANOARRIBA1 group
amz.AddAttack("GM17_1H","Amz_g_05")
amz.AddLevels("Amz_g_05",0,40)

#GOLPEARMA1MANODERECHA1 group
amz.AddAttack("GM18_1H","Amz_g_02")
amz.AddLevels("Amz_g_02",0,40)

#GOLPEARMA1MANOIZQUIERDA1 group
amz.AddAttack("GM19_1H","Amz_g_06")
amz.AddLevels("Amz_g_06",0,40)

#GOLPEARMA1MANOABAJO1 group
amz.AddAttack("GM20_1H","Amz_g_07")
amz.AddLevels("Amz_g_07",0,40)



#COMBO BO
amz.AddAttack("GM2_SP","Amz_g_spears8")
amz.AttackWindow("Amz_g_spears8",0.265,0.538,"GM2_SP_Window")
amz.AssignTrail("GM2_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spears8",2,40)

#COMBO BICHERO
amz.AddAttack("GM10_SP","Amz_g_spear_2katab6low")
amz.AttackWindow("Amz_g_spear_2katab6low",0.424,0.655,"GM10_SP_Window")
amz.AssignTrail("GM10_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_2katab6low",6,40)

#COMBO TRIDENTE
amz.AddAttack("GM4_SP","Amz_g_spear09")
amz.AttackWindow("Amz_g_spear09",0.418,0.569,"GM4_SP_Window")
amz.AssignTrail("GM4_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear09",9,40)

#COMBO CROSSPEAR
amz.AddAttack("GM7_SP","Amz_g_spear13")
amz.AttackWindow("Amz_g_spear13",0.287,0.532,"GM7_SP_Window")
amz.AssignTrail("GM7_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear13",13,40)

#COMBO HACHACUCHILLA
amz.AddAttack("GM5_SP","Amz_g_spear3s2")
amz.AttackWindow("Amz_g_spear3s2",0.608,0.779,"GM5_SP_Window")
amz.AssignTrail("GM5_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear3s2",14,40)

#GOLPE CRUSHBO
amz.AddAttack("GM26_SP","Amz_g_spear_21")
amz.AttackWindow("Amz_g_spear_21",0.313,0.547,"GM26_SP_Window")
amz.AssignTrail("GM26_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_21",15,40)

#GOLPE NAGINATA
amz.AddAttack("GM27_SP","Amz_g_spear22")
amz.AttackWindow("Amz_g_spear22",0.343,0.656,"GM27_SP_Window")
amz.AssignTrail("GM27_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear22",8,40)

#COMBO NAGINATA2
amz.AddAttack("GM24_SP","Amz_g_spear33")
amz.AttackWindow("Amz_g_spear33",0.404,0.613,"GM24_SP_Window")
amz.AssignTrail("GM24_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear33",17,40)

#GOLPE LANZAHANCHA
amz.AddAttack("GM28_SP","Amz_g_spear_sb11")
amz.AttackWindow("Amz_g_spear_sb11",0.564,0.718,"GM28_SP_Window")
amz.AssignTrail("GM28_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_sb11",18,40)

#GOLPE DEATHBO
amz.AddAttack("GM25_SP","Amz_g_spear_kata23")
amz.AttackWindow("Amz_g_spear_kata23",0.426,0.613,"GM25_SP_Window")
amz.AssignTrail("GM25_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_kata23",11,40)

#GOLPE FIREBO
amz.AddAttack("GM30_SP","Amz_g_spear_b6_26")
amz.AttackWindow("Amz_g_spear_b6_26",0.467,0.670,"GM30_SP_Window")
amz.AssignTrail("GM30_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_b6_26",13,40)

#GOLPE AXPEAR
amz.AddAttack("GM31_SP","Amz_g_spear32kata_b2")
amz.AttackWindow("Amz_g_spear32kata_b2",0.553,0.674,"GM31_SP_Window")
amz.AssignTrail("GM31_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear32kata_b2",10,40)

#GOLPE LANZA
amz.AddAttack("GM32_SP","Amz_g_spear19")
amz.AttackWindow("Amz_g_spear19",0.001,0.999,"GM32_SP_Window")
amz.AssignTrail("GM32_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear19",7,40)

#GOLPE ARPON
amz.AddAttack("GM33_SP","Amz_g_spear_b29")
amz.AttackWindow("Amz_g_spear_b29",0.077,0.602,"GM33_SP_Window")
amz.AssignTrail("GM33_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear_b29",16,40)

#GOLPE STEELFEATHER
amz.AddAttack("GM34_SP","Amz_g_spear19_bs1")
amz.AttackWindow("Amz_g_spear19_bs1",0.020,0.900,"GM34_SP_Window")
amz.AssignTrail("GM34_SP","","EstelaRoja1")
amz.AddLevels("Amz_g_spear19_bs1",17,40)

#GOLPE ICEWAND
amz.AddAttack("GM36_SP","Amz_g_spear16")
amz.AttackWindow("Amz_g_spear16",0.020,0.900,"GM36_SP_Window")
amz.AssignTrail("GM36_SP","","EstelaAzul1")                         #Was "EstelaRoja1" -LeadHead
amz.AddLevels("Amz_g_spear16",12,40)

#GOLPE QUEENSWORD
amz.AddAttack("GM37_1H","Amz_g_06lowkata_new")
amz.AttackWindow("Amz_g_06lowkata_new",0.020,0.900,"GM37_1H_Window")
amz.AssignTrail("GM37_1H","","EstelaRoja1")
amz.AddLevels("Amz_g_06lowkata_new",10,40)

#GOLPESINARMA1 "group"
amz.AddAttack("GM21_NO","Amz_g_kick2")
amz.AddLevels("Amz_g_kick2",0,40)

#GOLPESINARMA2 "group"
amz.AddAttack("GM22_NO","Amz_g_kick1")
amz.AddLevels("Amz_g_kick1",0,40)

#GOLPESINARMA3 "group"
amz.AddAttack("GM23_NO","Amz_g_kick5")
amz.AddLevels("Amz_g_kick5",0,40)


#COMBOGIRO180 group
amz.AddAttack("GM35_SP","Amz_g_spear_back")
amz.AddLevels("Amz_g_spear_back",3,40)
amz.AddEnergyLevel("Amz_g_spear_back", 0)

#COMBO LANZAESTELA
amz.AddAttack("GM80_1H","Amz_g_magic2")
amz.AssignTrail("GM80_1H","","EstelaRoja1")
amz.AddLevels("Amz_g_magic2",18,40)
amz.AddEnergyLevel("Amz_g_magic2", 0)

#COMBO CONCENTRACION
amz.AddAttack("GM81_1H","Amz_g_magic")
amz.AssignTrail("GM81_1H","","EstelaRoja1")
amz.AddLevels("Amz_g_magic",19,40)
amz.AddEnergyLevel("Amz_g_magic", 0)

#########################################################################
#GAI meta-group
amz.MetaAttack("GIM_SP","GI_SP")
amz.MetaAttack("GIM_SP","GM1_SP")
amz.MetaAttack("GIM_SP","GM2_SP")
amz.MetaAttack("GIM_SP","GM3_SP")
amz.MetaAttack("GIM_SP","GM4_SP")
amz.MetaAttack("GIM_SP","GM5_SP")
amz.MetaAttack("GIM_SP","GM6_SP")
amz.MetaAttack("GIM_SP","GM7_SP")
amz.MetaAttack("GIM_SP","GM8_SP")
amz.MetaAttack("GIM_SP","GM10_SP")
amz.MetaAttack("GIM_AXE","GM11_AXE")
amz.MetaAttack("GIM_2W","GM12_2W")
amz.MetaAttack("GIM_2W","GM13_2W")
amz.MetaAttack("GIM_2W","GM14_2W")
amz.MetaAttack("GIM_SP","GM15_SP")
amz.MetaAttack("GIM_1H","GM16_1H")
amz.MetaAttack("GIM_1H","GM17_1H")
amz.MetaAttack("GIM_1H","GM18_1H")
amz.MetaAttack("GIM_1H","GM19_1H")
amz.MetaAttack("GIM_1H","GM20_1H")
amz.MetaAttack("GIM_NO","GM21_NO")
amz.MetaAttack("GIM_NO","GM22_NO")
amz.MetaAttack("GIM_NO","GM23_NO")
amz.MetaAttack("GIM_SP","GM24_SP")
amz.MetaAttack("GIM_SP","GM25_SP")
amz.MetaAttack("GIM_SP","GM26_SP")
amz.MetaAttack("GIM_SP","GM27_SP")
amz.MetaAttack("GIM_SP","GM28_SP")
amz.MetaAttack("GIM_SP","GM30_SP")
amz.MetaAttack("GIM_SP","GM31_SP")
amz.MetaAttack("GIM_1H","GM32_SP")
amz.MetaAttack("GIM_1H","GM33_SP")
amz.MetaAttack("GIM_1H","GM34_SP")
amz.MetaAttack("GIM_SP","GM35_SP")
amz.MetaAttack("GIM_SP","GM36_SP")
amz.MetaAttack("GIM_1H","GM37_1H")
amz.MetaAttack("GIM_1H","GM80_1H")
amz.MetaAttack("GIM_1H","GM81_1H")


amz.MetaAttack("GOLPEINICIAL","GI_SP")

#GM meta-group
amz.MetaAttack("COMBO1","GM1_SP")
amz.MetaAttack("COMBO1","GM2_SP")
amz.MetaAttack("COMBO1","GM3_SP")
amz.MetaAttack("COMBO1","GM4_SP")
amz.MetaAttack("COMBO1","GM4_SP")
amz.MetaAttack("COMBO1","GM5_SP")
amz.MetaAttack("COMBO1","GM6_SP")
amz.MetaAttack("COMBO1","GM7_SP")
amz.MetaAttack("COMBO1","GM8_SP")
amz.MetaAttack("COMBO1","GM10_SP")
amz.MetaAttack("COMBO1","GM11_AXE")
amz.MetaAttack("COMBO1","GM12_2W")
amz.MetaAttack("COMBO1","GM13_2W")
amz.MetaAttack("COMBO1","GM14_2W")
amz.MetaAttack("COMBO1","GM15_SP")
amz.MetaAttack("COMBO1","GM16_1H")
amz.MetaAttack("COMBO1","GM17_1H")
amz.MetaAttack("COMBO1","GM18_1H")
amz.MetaAttack("COMBO1","GM19_1H")
amz.MetaAttack("COMBO1","GM20_1H")
amz.MetaAttack("COMBO1","GM21_NO")
amz.MetaAttack("COMBO1","GM22_NO")
amz.MetaAttack("COMBO1","GM23_NO")
amz.MetaAttack("COMBO1","GM24_SP")
amz.MetaAttack("COMBO1","GM25_SP")
amz.MetaAttack("COMBO1","GM26_SP")
amz.MetaAttack("COMBO1","GM27_SP")
amz.MetaAttack("COMBO1","GM28_SP")
amz.MetaAttack("COMBO1","GM30_SP")
amz.MetaAttack("COMBO1","GM31_SP")
amz.MetaAttack("COMBO1","GM32_SP")
amz.MetaAttack("COMBO1","GM33_SP")
amz.MetaAttack("COMBO1","GM34_SP")
amz.MetaAttack("COMBO1","GM35_SP")
amz.MetaAttack("COMBO1","GM36_SP")
amz.MetaAttack("COMBO1","GM37_1H")
amz.MetaAttack("COMBO1","GM80_1H")
amz.MetaAttack("COMBO1","GM81_1H")

amz.MetaAttack("COMBOEXTRA","GM15_SP")

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
######################################################

#COMBOGIRO180
amz.AllowAttack("GM35_SP","L+R+B","","","","SP")

#COMBO LANZAESTELA
amz.AllowAttack("GM80_1H","&B","GM16_1H","","","BladeSword2")

#COMBO CONCENTRACION
amz.AllowAttack("GM81_1H","&A+F","GM16_1H","","","BladeSword2")

#COMBOHACHATORPE
amz.AllowAttack("GM11_AXE","A","","","","AXE")

#COMBOESPADATORPE3
amz.AllowAttack("GM14_2W","A","GM13_2W","","GM13_2W_Window","2W")

#COMBOESPADATORPE1
amz.AllowAttack("GM13_2W","A","","COMBO1,COMBO1,COMBO1","GM14_2W_Window","2W")



#GOLPESINARMA1
amz.AllowAttack("GM23_NO","A","","COMBO1","","NO")

#GOLPESINARMA2
amz.AllowAttack("GM22_NO","A+F","","COMBO1","","NO")
amz.AllowAttack("GM22_NO","&A+F","","COMBO1","","NO")

#GOLPESINARMA3
amz.AllowAttack("GM21_NO","A+B","","COMBO1","","NO")
amz.AllowAttack("GM21_NO","&A+B","","COMBO1","","NO")

#COMBO TRIDENTE
amz.AllowAttack("GM4_SP","B+L","GI_SP","","GI_SP_Window","Tridente")

#COMBO NAGINATA2
amz.AllowAttack("GM24_SP","F+B","GM15_SP","","","Naginata2")

#GOLPE FIREBO
amz.AllowAttack("GM30_SP","F+R","GI_SP","","GI_SP_Window","FireBo")

#GOLPE LANZA
amz.AllowAttack("GM32_SP","B+R","GI_SP","","GI_SP_Window","Lanza")

#GOLPE ARPON
amz.AllowAttack("GM33_SP","F+B","GI_SP","","GI_SP_Window","Arpon")

#GOLPE ICEWAND
amz.AllowAttack("GM36_SP","F+L","GI_SP","","GI_SP_Window","IceWand")

#COMBO QUEENSWORD
amz.AllowAttack("GM37_1H","R+B","GM19_1H","","","QueenSword")	


#EXTRAGOLPE1
amz.AllowAttack("GM15_SP","R+L","GI_SP","COMBOEXTRA","GM15_SP_Window","SP")

#GOLPEARMA1MANOINICIAL
amz.AllowAttack("GM16_1H","A","","COMBO1","","1H")

#GOLPEARMA1MANOARRIBA
amz.AllowAttack("GM17_1H","A+F","","COMBO1","","1H")
amz.AllowAttack("GM17_1H","&A+F","","COMBO1","","1H")

#GOLPEARMA1MANODERECHA
amz.AllowAttack("GM18_1H","A+R","","COMBO1","","1H")
amz.AllowAttack("GM18_1H","&A+R","","COMBO1","","1H")

#GOLPEARMA1MANOIZQUIERDA
amz.AllowAttack("GM19_1H","A+L","","COMBO1","","1H")
amz.AllowAttack("GM19_1H","&A+L","","COMBO1","","1H")

#GOLPEARMA1MANOABAJO
amz.AllowAttack("GM20_1H","A+B","","COMBO1","","1H")
amz.AllowAttack("GM20_1H","&A+B","","COMBO1","","1H")


#COMBO TECLA ARRIBA1
amz.AllowAttack("GM1_SP","A+F","","GM1_SP","","SP")
amz.AllowAttack("GM1_SP","&A+F","","GM1_SP","","SP")

#COMBO BICHERO
amz.AllowAttack("GM10_SP","B","GM1_SP","","","Bichero")

#GOLPE DEATHBO
amz.AllowAttack("GM25_SP","F+R","GM1_SP","","GM1_SP_Window","DeathBo")

#GOLPE CRUSHBO
amz.AllowAttack("GM26_SP","A+F","GM1_SP","","GM1_SP_Window","CrushBo")

#GOLPE STEELFEATHER
amz.AllowAttack("GM34_SP","F+B","GM1_SP","","GM1_SP_Window","SteelFeather")


#COMBO TECLA DERECHA1
amz.AllowAttack("GM3_SP","A+R","","GM3_SP","","SP")
amz.AllowAttack("GM3_SP","&A+R","","GM3_SP","","SP")

#GOLPE NAGINATA
amz.AllowAttack("GM27_SP","L","GM3_SP","","","Naginata")

#COMBO HACHACUCHILLA
amz.AllowAttack("GM5_SP","L+R","GM3_SP","","GM3_SP_Window","Hachacuchilla")


#COMBO TECLA IZQUIERDA1
amz.AllowAttack("GM6_SP","A+L","","GM6_SP","","SP")
amz.AllowAttack("GM6_SP","&A+L","","GM6_SP","","SP")

#GOLPE AXPEAR
amz.AllowAttack("GM31_SP","L","GM6_SP","","","Axpear")

#COMBO CROSSPEAR
amz.AllowAttack("GM7_SP","F+L","GM6_SP","","GM6_SP_Window","Crosspear")

#COMBO TECLA ABAJO1
amz.AllowAttack("GM8_SP","A+B","","GM8_SP","GM10_SP_Window","SP")
amz.AllowAttack("GM8_SP","&A+B","","GM8_SP","GM10_SP_Window","SP")

#COMBO BO
amz.AllowAttack("GM2_SP","F","GM8_SP","","","Bo")

#GOLPE LANZAANCHA
amz.AllowAttack("GM28_SP","A+B","GM8_SP","","","LanzaAncha")


#GI
amz.AllowAttack("GI_SP","A","","GIM_SP","GI_SP_Window","SP")







