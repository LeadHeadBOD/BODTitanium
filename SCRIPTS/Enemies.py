############################################################################################
#
# NOTES about how to chreate an enemy race
#	-Do it always on this file
#	-If you convert an entity into a personEntity , a race must be defined 
#	previously here
#	
#
#	The main funcion is "GetCharType"
#	It tries to find the enemy race . If it does not find it , it will create it
#	
#		
#	GetCharType(name1,name2)
#
#	---THE 3d MESH---
#
#		name2.BOD ->Name of the 3d mesh of the race (placed in the 3dchars directory)
#			name1->MUST be the internal name of the mesh defined by name1.BOD!
#		
#	----THE "BOING"---
#
#		The "boing" is the simplified model used for the collision detection) , will be :
#			File :  firstThreeLettersOfName2 + "_Bng.BOD"
#			(plcaed in the 3dchars directory)
#			InternalName : Exactly as the external name !
#			Example :  ("Troll_Dark","Tkn_Drk")
#				File : Tkn_Bng.BOD , with internal name "Tkn_Bng"	
#
#	---THE ANIMATION SET---
#		By default , ( unless stated otherwise in the Anm_Conv.py , scrips directory )
#		the first _three_ letters of the name2 will be used . 
#			Example :  ("Troll_Dark","Tkn_Drk")
#						  |||
#				The animations for relax will be Tkn_rlx_-... , Tkn_
#
#
#	Any undates required for these "rules" , please ask .
#
#
#	Last Updated 19-7-99 , Jose Raluy
#
############################################################################################

def Init():
    import math
    import Bladex

    ####################
    #                  #
    #    Barbarian     #
    #                  #
    ####################
    bar=Bladex.GetCharType("Barbarian_N","Bar")

    bar.NoArmour="Barbarian_N"
    bar.LowArmour="Barbarian_L"
    bar.MedArmour=""
    bar.HighArmour=""

    bar.TurnSpeed=3.4
    bar.Jcost=27000
    bar.MaxFall=5000
    bar.DieFall=14000
    bar.MaxStair=335
    bar.Fov=math.pi
    bar.MaxGrab=3500.0
    bar.MedGrab=2500.0
    bar.Min2Grab=1500.0    
    bar.MinTake=-500.0		# Min height above floor barbarian will take
    bar.MaxTake1=450.0	# Max height above floor for Take1 Anim
    bar.MaxTake2=550.0	# Max height above floor for Take2 Anim
    bar.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    bar.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    bar.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    bar.Reach=2000.0	# Max distance from bar centre to obj centre to take
    bar.MovFrwdSpeedInStrafe=1300  #Forwards speed when in strafe(combat mode only)
    bar.MovBkwdSpeedInStrafe=1300  #Idem backwards
    bar.MaxCombatDist=20000
    bar.MaxSeeDist=50000

    bar.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    bar.SetCDSphere(0,210.0,550.0)  #(numero de la espera, altura mm, radio mm)
    bar.SetCDSphere(1,-200.0,550.0)  #(numero de la espera, altura mm, radio mm)


    bar.NaturalWeapons=1

    ####################
    #                  #
    #     Knight       #
    #                  #
    ####################

    kgt=Bladex.GetCharType("Knight_N","Kgt")

    kgt.NoArmour="Knight_N"
    kgt.LowArmour="Knight_L"
    kgt.MedArmour="Knight_M"
    kgt.HighArmour="Knight_F"

    kgt.TurnSpeed=3.4
    kgt.Jcost=2700
    kgt.MaxFall=5000
    kgt.DieFall=14000
    kgt.MaxStair=335
    kgt.Fov=math.pi
    kgt.MaxGrab=3500.0
    kgt.MedGrab=2500.0
    kgt.Min2Grab=1500.0

    kgt.MinTake=-500.0		# Min height above floor barbarian will take
    kgt.MaxTake1=450.0	# Max height above floor for Take1 Anim
    kgt.MaxTake2=500.0	# Max height above floor for Take2 Anim
    kgt.MaxTake3=1100.0	# Max height above floor for Take3 Anim
    kgt.MaxTake4=1700.0	# Max height above floor for Take4 Anim
    kgt.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    kgt.Reach=2000.0	# Max distance from kgt centre to obj centre to take
    kgt.MovFrwdSpeedInStrafe=1400  #Forwards speed when in strafe(combat mode only)
    kgt.MovBkwdSpeedInStrafe=1400  #Idem backwards
    kgt.MaxCombatDist=20000
    kgt.MaxSeeDist=50000

    kgt.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    kgt.SetCDSphere(0,90.0,500.0)  #(numero de la espera, altura mm, radio mm)
    kgt.SetCDSphere(1,-240.0,500.0)  #(numero de la espera, altura mm, radio mm)


    kgt.NaturalWeapons=1

    ####################
    #                  #
    #     Amazon       #
    #                  #
    ####################

    amz=Bladex.GetCharType("Amazon_N","Amz")
    amz.IntName="Amz" # En realidad , es este por defecto ( las 3 primeras letras )

    amz.NoArmour="Amazon_N"
    amz.LowArmour="Amazon_L"
    amz.MedArmour=""
    amz.HighArmour=""


    amz.TurnSpeed=3.4
    amz.Jcost=2700
    amz.MaxFall=5000
    amz.DieFall=14000
    amz.MaxStair=335
    amz.Fov=math.pi
    amz.MaxGrab=3500.0
    amz.MedGrab=2500.0
    amz.Min2Grab=1500.0

    amz.MinTake=-500.0	# Min height above floor amazon will take
    amz.MaxTake1=450.0	# Max height above floor for Take1 Anim
    amz.MaxTake2=550.0	# Max height above floor for Take2 Anim
    amz.MaxTake3=1100.0	# Max height above floor for Take3 Anim
    amz.MaxTake4=1700.0	# Max height above floor for Take4 Anim
    amz.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    amz.Reach=2000.0	# Max distance from amz centre to obj centre to take
    amz.MovFrwdSpeedInStrafe=1400  #Forwards speed when in strafe(combat mode only)
    amz.MovBkwdSpeedInStrafe=1400  #Idem backwards
    amz.MaxCombatDist=20000
    amz.MaxSeeDist=50000

    amz.NaturalWeapons=1
    amz.SetNCDSpheres(2)
    amz.SetCDSphere(0,250.0,450.0)  #(numero de la espera, altura mm, radio mm)
    amz.SetCDSphere(1,-240.0,450.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    #     Dwarf        #
    #                  #
    ####################

    dwf=Bladex.GetCharType("Dwarf_N","Dwf")
    dwf.IntName="Dwf" # En realidad , es este por defecto ( las 3 primeras letras )

    dwf.NoArmour="Dwarf_N"
    dwf.LowArmour="Dwarf_L"
    dwf.MedArmour="Dwarf_M"
    dwf.HighArmour=""

    dwf.TurnSpeed=3.4
    dwf.Jcost=2700
    dwf.MaxFall=5000
    dwf.DieFall=14000
    dwf.MaxStair=335
    dwf.Fov=math.pi
    dwf.MaxGrab=3500.0
    dwf.MedGrab=2500.0
    dwf.Min2Grab=1500.0

    dwf.MinTake=-500.0		# Min height above floor dwfdwfian will take
    dwf.MaxTake1=450.0	# Max height above floor for Take1 Anim
    dwf.MaxTake2=550.0	# Max height above floor for Take2 Anim
    dwf.MaxTake3=1100.0	# Max height above floor for Take3 Anim
    dwf.MaxTake4=1700.0	# Max height above floor for Take4 Anim
    dwf.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    dwf.Reach=2000.0	# Max distance from dwf centre to obj centre to take
    dwf.MovFrwdSpeedInStrafe=1300  #Forwards speed when in strafe(combat mode only)
    dwf.MovBkwdSpeedInStrafe=1300  #Idem backwards
    dwf.MaxCombatDist=20000
    dwf.MaxSeeDist=50000

    dwf.NaturalWeapons=1

    dwf.SetNCDSpheres(1)
    dwf.SetCDSphere(0,-160.0,600.0)  #(numero de la espera, altura mm, radio mm)



    #dwf.NaturalWeapons=1

    ####################
    #                  #
    #     Dwarf 1      #
    #                  #
    ####################

    dwf=Bladex.GetCharType("Enano1","Enano1")
    dwf.IntName="Ena" # En realidad , es este por defecto ( las 3 primeras letras )

    dwf.TurnSpeed=3.4
    dwf.Jcost=2700
    dwf.MaxFall=5000
    dwf.DieFall=14000
    dwf.MaxStair=335
    dwf.Fov=math.pi/1.5
    dwf.MaxGrab=3500.0
    dwf.MedGrab=2500.0
    dwf.Min2Grab=1500.0

    dwf.MinTake=-500.0		# Min height above floor dwfdwfian will take
    dwf.MaxTake1=450.0	# Max height above floor for Take1 Anim
    dwf.MaxTake2=550.0	# Max height above floor for Take2 Anim
    dwf.MaxTake3=1100.0	# Max height above floor for Take3 Anim
    dwf.MaxTake4=1700.0	# Max height above floor for Take4 Anim
    dwf.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    dwf.Reach=2000.0	# Max distance from dwf centre to obj centre to take

    dwf.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    dwf.MovBkwdSpeedInStrafe=1000  #Idem backwards

    dwf.MaxCombatDist=18000

    dwf.MaxSeeDist=50000
    dwf.SetNCDSpheres(1)
    dwf.SetCDSphere(0,-120.0,575.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    #     Dwarf 2      #
    #                  #
    ####################

    dwf=Bladex.GetCharType("Enano2","Enano2")
    dwf.IntName="Ena" # En realidad , es este por defecto ( las 3 primeras letras )


    dwf.TurnSpeed=3.4
    dwf.Jcost=2700
    dwf.MaxFall=5000
    dwf.DieFall=14000
    dwf.MaxStair=335
    dwf.Fov=math.pi/1.5
    dwf.MaxGrab=3500.0
    dwf.MedGrab=2500.0
    dwf.Min2Grab=1500.0

    dwf.MinTake=-500.0		# Min height above floor dwfdwfian will take
    dwf.MaxTake1=450.0	# Max height above floor for Take1 Anim
    dwf.MaxTake2=550.0	# Max height above floor for Take2 Anim
    dwf.MaxTake3=1100.0	# Max height above floor for Take3 Anim
    dwf.MaxTake4=1700.0	# Max height above floor for Take4 Anim
    dwf.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    dwf.Reach=2000.0	# Max distance from dwf centre to obj centre to take

    dwf.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    dwf.MovBkwdSpeedInStrafe=1000  #Idem backwards

    dwf.MaxCombatDist=18000

    dwf.MaxSeeDist=50000
    dwf.SetNCDSpheres(1)
    dwf.SetCDSphere(0,-120.0,575.0)  #(numero de la espera, altura mm, radio mm)




    ####################
    #                  #
    # Traitor Knight   #
    #                  #
    ####################
    tkn=Bladex.GetCharType("Knight_Traitor","Tkn")
    tkn.IntName="Tkn" 


    tkn.TurnSpeed=4.5
    tkn.Jcost=2700
    tkn.MaxFall=4000
    tkn.DieFall=14000
    tkn.MaxStair=335
    tkn.Fov=math.pi/1.2
    tkn.MaxGrab=3500.0
    tkn.MedGrab=2500.0
    tkn.Min2Grab=1500.0

    tkn.MinTake=-500.0		# Min height above floor barbarian will take
    tkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    tkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    tkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    tkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    tkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    tkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    tkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    tkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    tkn.HearMinVolume=0.001
    tkn.MaxCombatDist=8000
    tkn.DistStop=2000.0
    tkn.DistStop2=6000.0
    tkn.MaxSeeDist=30000


    tkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    tkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    tkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    # Ork              #
    #                  #
    ####################
    ork=Bladex.GetCharType("Ork","Ork")
    ork.IntName="Ork" 


    ork.TurnSpeed=4.5
    ork.Jcost=2700
    ork.MaxFall=4000
    ork.DieFall=14000
    ork.MaxStair=505
    ork.Fov=math.pi/1.2
    ork.MaxGrab=3500.0
    ork.MedGrab=2500.0
    ork.Min2Grab=1500.0

    ork.MinTake=-500.0		# Min height above floor barbarian will take
    ork.MaxTake1=250.0	# Max height above floor for Take1 Anim
    ork.MaxTake2=550.0	# Max height above floor for Take2 Anim
    ork.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    ork.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    ork.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    ork.Reach=2000.0	# Max distance from ork centre to obj centre to take

    ork.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    ork.MovBkwdSpeedInStrafe=1000  #Idem backwards

    ork.MaxCombatDist=8000
    ork.DistStop=2000.0
    ork.DistStop2=5000.0
    ork.MaxSeeDist=30000

    ork.AddRouteAnim="Tkn_wai_01"
    ork.AddRouteAnim="Tkn_wai_02"

    ork.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    ork.SetCDSphere(0,170.0,350.0)  #(numero de la espera, altura mm, radio mm)
    ork.SetCDSphere(1,-150.0,500.0)  #(numero de la espera, altura mm, radio mm)


    ####################                                                           
    #                  #                                                           
    # Dark Ork         #                                                           
    #                  #                                                           
    ####################                                                           
    Dok=Bladex.GetCharType("Dark_Ork","Dok")                                            
    Dok.IntName="Dok"                                                              


    Dok.TurnSpeed=4.5                                                              
    Dok.Jcost=2700                                                                 
    Dok.MaxFall=4000
    Dok.DieFall=14000
    Dok.MaxStair=505                                                               
    Dok.Fov=math.pi/1.2                                                           
    Dok.MaxGrab=3500.0                                                             
    Dok.MedGrab=2500.0                                                             
    Dok.Min2Grab=1500.0                                                            

    Dok.MinTake=-500.0		# Min height above floor barbarian will take   
    Dok.MaxTake1=250.0	# Max height above floor for Take1 Anim                
    Dok.MaxTake2=550.0	# Max height above floor for Take2 Anim                
    Dok.MaxTake3=1300.0	# Max height above floor for Take3 Anim                
    Dok.MaxTake4=1900.0	# Max height above floor for Take4 Anim                
    Dok.MaxTake5=3000.0	# Max height above floor for Take5 Anim                
    Dok.Reach=2000.0	# Max distance from ork centre to obj centre to take   
                                                                                
    Dok.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Dok.MovBkwdSpeedInStrafe=1000  #Idem backwards                                 
                                                                                
    Dok.MaxCombatDist=8000                                                         
    Dok.DistStop=2000.0                                                            
    Dok.DistStop2=5000.0                                                           
    Dok.MaxSeeDist=30000                                                           
                                                                                
    Dok.AddRouteAnim="Tkn_wai_01"                                                  
    Dok.AddRouteAnim="Tkn_wai_02"                                                  

    Dok.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    Dok.SetCDSphere(0,170.0,350.0)  #(numero de la espera, altura mm, radio mm)
    Dok.SetCDSphere(1,-150.0,500.0)  #(numero de la espera, altura mm, radio mm)



    ####################                                                           
    #                  #                                                           
    # Gold Ork         #                                                           
    #                  #                                                           
    ####################                                                           
    Org=Bladex.GetCharType("Gold_Ork","Org")                                            
    Org.IntName="Org"                                                              
                                                                             
                                                                             
    Org.TurnSpeed=4.5                                                              
    Org.Jcost=2700                                                                 
    Org.MaxFall=4000
    Org.DieFall=14000
    Org.MaxStair=335                                                               
    Org.Fov=math.pi/1.2                                                           
    Org.MaxGrab=3500.0                                                             
    Org.MedGrab=2500.0                                                             
    Org.Min2Grab=1500.0                                                            

    Org.MinTake=-500.0		# Min height above floor barbarian will take   
    Org.MaxTake1=250.0	# Max height above floor for Take1 Anim                
    Org.MaxTake2=550.0	# Max height above floor for Take2 Anim                
    Org.MaxTake3=1300.0	# Max height above floor for Take3 Anim                
    Org.MaxTake4=1900.0	# Max height above floor for Take4 Anim                
    Org.MaxTake5=3000.0	# Max height above floor for Take5 Anim                
    Org.Reach=2000.0	# Max distance from ork centre to obj centre to take   
                                                                             
    Org.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Org.MovBkwdSpeedInStrafe=1000  #Idem backwards                                 
                                                                             
    Org.MaxCombatDist=8000                                                         
    Org.DistStop=2000.0                                                            
    Org.DistStop2=5000.0                                                           
    Org.MaxSeeDist=30000                                                           
                                                                             
    Org.AddRouteAnim="Tkn_wai_01"                                                  
    Org.AddRouteAnim="Tkn_wai_02"                                                  
    
    Org.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    Org.SetCDSphere(0,170.0,350.0)  #(numero de la espera, altura mm, radio mm)
    Org.SetCDSphere(1,-150.0,500.0)  #(numero de la espera, altura mm, radio mm)



    ####################
    #                  #
    # Great_Ork        #
    #                  #
    ####################
    gok=Bladex.GetCharType("Great_Ork","Gok")
    gok.IntName="Gok" 


    gok.TurnSpeed=4.5
    gok.Jcost=2700
    gok.MaxFall=4000
    gok.DieFall=14000
    gok.MaxStair=405
    gok.Fov=math.pi/1.2
    gok.MaxGrab=3500.0
    gok.MedGrab=2500.0
    gok.Min2Grab=1500.0

    gok.MinTake=-500.0	# Min height above floor great ork will take
    gok.MaxTake1=250.0	# Max height above floor for Take1 Anim
    gok.MaxTake2=550.0	# Max height above floor for Take2 Anim
    gok.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    gok.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    gok.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    gok.Reach=2000.0	# Max distance from gok centre to obj centre to take

    gok.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    gok.MovBkwdSpeedInStrafe=1000  #Idem backwards

    gok.MaxCombatDist=8000
    gok.DistStop=2000.0
    gok.DistStop2=6000.0
    gok.MaxSeeDist=40000

    gok.AddRouteAnim="Tkn_wai_01"
    gok.AddRouteAnim="Tkn_wai_02"

    gok.SetNCDSpheres(1)
    gok.SetCDSphere(0,-140.0,640.0)  #(numero de la espgok.SetCDSphere(1,-200.0,580.0)era, altura mm, radio mm)




    ####################
    #                  #
    # Skeleton         #
    #                  #
    ####################
    skl=Bladex.GetCharType("Skeleton","Skl")
    skl.IntName="Skl" 


    skl.TurnSpeed=4.5
    skl.Jcost=2700
    skl.MaxFall=4000
    skl.DieFall=14000
    skl.MaxStair=400
    skl.Fov=math.pi/1.2
    skl.MaxGrab=2500.0
    skl.MedGrab=1500.0
    skl.Min2Grab=1000.0

    skl.MinTake=-500.0		# Min height above floor barbarian will take
    skl.MaxTake1=250.0	# Max height above floor for Take1 Anim
    skl.MaxTake2=550.0	# Max height above floor for Take2 Anim
    skl.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    skl.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    skl.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    skl.Reach=2000.0	# Max distance from skl centre to obj centre to take

    skl.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    skl.MovBkwdSpeedInStrafe=1000  #Idem backwards

    skl.MaxCombatDist=8000
    skl.DistStop=2000.0
    skl.DistStop2=6000.0
    skl.MaxSeeDist=30000


    skl.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    skl.SetCDSphere(0,300.0,320.0)  #(numero de la espera, altura mm, radio mm)
    skl.SetCDSphere(1,-100.0,450.0)  #(numero de la espera, altura mm, radio mm)





    ####################
    #                  #
    # Dark Troll       #
    #                  #
    ####################
    trl=Bladex.GetCharType("Troll_Dark","Trl_dk")
    trl.IntName="Trl" 


    trl.TurnSpeed=4.5
    trl.Jcost=2700
    trl.MaxFall=4000
    trl.DieFall=14000
    trl.MaxStair=335
    trl.Fov=math.pi/1.2
    trl.MaxGrab=3500.0
    trl.MedGrab=2500.0
    trl.Min2Grab=1500.0

    trl.MinTake=-500.0		# Min height above floor barbarian will take
    trl.MaxTake1=250.0	# Max height above floor for Take1 Anim
    trl.MaxTake2=550.0	# Max height above floor for Take2 Anim
    trl.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    trl.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    trl.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    trl.Reach=2000.0	# Max distance from trl centre to obj centre to take

    trl.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    trl.MovBkwdSpeedInStrafe=1000  #Idem backwards

    trl.MaxCombatDist=8000
    trl.DistStop=1750.0
    trl.DistStop2=6000.0
    trl.MaxSeeDist=30000

    trl.SetNCDSpheres(1)
    trl.SetCDSphere(0,0.0,800.0)  #(numero de la espera, altura mm, radio mm)



    ####################
    #                  #
    # Snow Troll       #
    #                  #
    ####################
    trl=Bladex.GetCharType("Troll_snow","Trl_sn")

    trl.TurnSpeed=4.5
    trl.Jcost=2700
    trl.MaxFall=4000
    trl.DieFall=14000
    trl.MaxStair=500
    trl.Fov=math.pi/1.2
    trl.MaxGrab=3500.0
    trl.MedGrab=2500.0
    trl.Min2Grab=1500.0

    trl.MinTake=-500.0		# Min height above floor barbarian will take
    trl.MaxTake1=250.0	# Max height above floor for Take1 Anim
    trl.MaxTake2=550.0	# Max height above floor for Take2 Anim
    trl.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    trl.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    trl.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    trl.Reach=2000.0	# Max distance from trl centre to obj centre to take

    trl.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    trl.MovBkwdSpeedInStrafe=1000  #Idem backwards

    trl.MaxCombatDist=8000
    trl.DistStop=1750.0
    trl.DistStop2=6000.0
    trl.MaxSeeDist=30000

    trl.SetNCDSpheres(1)
    trl.SetCDSphere(0,0.0,800.0)  #(numero de la espera, altura mm, radio mm)



    ####################
    #                  #
    #     Ragnar       #
    #                  #
    ####################
    rgn=Bladex.GetCharType("Ragnar","Rgn")

    rgn.TurnSpeed=4.5
    rgn.Jcost=2700
    rgn.MaxFall=4000
    rgn.DieFall=14000
    rgn.MaxStair=335
    rgn.Fov=math.pi/1.2
    rgn.MaxGrab=3500.0
    rgn.MedGrab=2500.0
    rgn.Min2Grab=1500.0

    rgn.MinTake=-500.0		# Min height above floor barbarian will take
    rgn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    rgn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    rgn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    rgn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    rgn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    rgn.Reach=2000.0	# Max distance from rgn centre to obj centre to take

    rgn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    rgn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    rgn.DistStop=2000.0
    rgn.DistStop2=2100.0

    rgn.MaxCombatDist=10000

    rgn.MaxSeeDist=50000


    rgn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    rgn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    rgn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    #   Chaos Knight   #
    #                  #
    ####################
    chk=Bladex.GetCharType("ChaosKnight","Chk")

    chk.TurnSpeed=4.5
    chk.Jcost=2700
    chk.MaxFall=4000
    chk.DieFall=14000
    chk.MaxStair=335
    chk.Fov=math.pi*1.5
    chk.MaxGrab=3500.0
    chk.MedGrab=2500.0
    chk.Min2Grab=1500.0

    chk.MinTake=-500.0		# Min height above floor barbarian will take
    chk.MaxTake1=250.0	# Max height above floor for Take1 Anim
    chk.MaxTake2=550.0	# Max height above floor for Take2 Anim
    chk.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    chk.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    chk.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    chk.Reach=2000.0	# Max distance from chk centre to obj centre to take

    chk.MovFrwdSpeedInStrafe=800  #Forwards speed when in strafe(combat mode only)
    chk.MovBkwdSpeedInStrafe=800  #Idem backwards

    chk.DistStop=2600.0
    chk.DistStop2=6000.0
    chk.DistStopMaxFactor=0.6

    chk.MaxCombatDist=10000
    chk.MaxSeeDist=50000


    chk.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    chk.SetCDSphere(0,50.0,825.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    #   Little Demon   # 
    #                  #
    ####################
    ldm=Bladex.GetCharType("Little_Demon","Ldm")

    ldm.TurnSpeed=4.5
    ldm.Jcost=2700
    ldm.MaxFall=5000
    ldm.DieFall=14000
    ldm.MaxStair=335
    ldm.Fov=math.pi*1.5
    ldm.MaxGrab=3500.0
    ldm.MedGrab=2500.0
    ldm.Min2Grab=1500.0

    ldm.MinTake=-500.0		# Min height above floor barbarian will take
    ldm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    ldm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    ldm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    ldm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    ldm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    ldm.Reach=2000.0	# Max distance from ldm centre to obj centre to take

    ldm.MovFrwdSpeedInStrafe=800  #Forwards speed when in strafe(combat mode only)
    ldm.MovBkwdSpeedInStrafe=800  #Idem backwards

    ldm.DistStop=2600.0
    ldm.DistStop2=6000.0

    ldm.MaxCombatDist=10000
    ldm.MaxSeeDist=30000

    ldm.SetNCDSpheres(1)
    ldm.SetCDSphere(0,-300.0,850.0)  #(numero de la espera, altura mm, radio mm)
    ldm.HeadControlled=0
    ldm.NaturalWeapons=1

    ####################
    #                  #
    #   Great  Demon   # 
    #                  #
    ####################
    gdm=Bladex.GetCharType("Great_Demon","Gdm")

    gdm.TurnSpeed=4.5
    gdm.Jcost=2700
    gdm.MaxFall=4000
    gdm.DieFall=14000
    gdm.MaxStair=700
    gdm.Fov=math.pi*1.5
    gdm.MaxGrab=3500.0
    gdm.MedGrab=2500.0
    gdm.Min2Grab=1500.0

    gdm.MinTake=-500.0		# Min height above floor barbarian will take
    gdm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    gdm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    gdm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    gdm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    gdm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    gdm.Reach=2000.0	# Max distance from ldm centre to obj centre to take

    gdm.MovFrwdSpeedInStrafe=800  #Forwards speed when in strafe(combat mode only)
    gdm.MovBkwdSpeedInStrafe=800  #Idem backwards

    gdm.DistStop=4000.0
    gdm.DistStop2=4001.0
    gdm.DistStopMaxFactor=0.8
    gdm.MaxCombatDist=50000
    gdm.MaxSeeDist=50000
    gdm.NaturalWeapons=1

    gdm.SetNCDSpheres(2)
    gdm.SetCDSphere(0,-2500.0,1500.0)
    gdm.SetCDSphere(1,-1000.0,2200.0)
    
    gdm.HeadControlled=0




    ####################
    #                  #
    #   Prisioner_1    #
    #                  #
    ####################
    pr1=Bladex.GetCharType("Prisoner_1","Prs_1")

    pr1.MaxStair=335
    pr1.Fov=math.pi/1.5


    ####################
    #                  #
    #   Prisioner_3    #
    #                  #
    ####################
    pr3=Bladex.GetCharType("Prisoner_3","Prs_3")


    pr3.MaxStair=335
    pr3.Fov=math.pi/1.5


    ####################
    #                  #
    #   Prisioner_5    #
    #                  #
    ####################
    pr5=Bladex.GetCharType("Prisoner_5","Prs_5")

    pr5.MaxStair=335
    pr5.Fov=math.pi/1.5


    ####################
    #                  #
    #   Prisioner_6    #
    #                  #
    ####################
    pr6=Bladex.GetCharType("Prisoner_6","Prs_6")

    pr6.MaxStair=335
    pr6.Fov=math.pi/1.5



    ####################
    #                  #
    # Cos              #
    #                  #
    ####################
    Cos=Bladex.GetCharType("Cos","Cos")

    Cos.TurnSpeed=4.5
    Cos.Jcost=2700
    Cos.MaxFall=4000
    Cos.DieFall=14000
    Cos.MaxStair=300
    Cos.Fov=math.pi
    Cos.MaxGrab=1500.0
    Cos.MedGrab=1500.0
    Cos.Min2Grab=800.0

    Cos.MinTake=-500.0		# Min height above floor barbarian will take
    Cos.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Cos.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Cos.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Cos.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Cos.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Cos.Reach=2000.0	# Max distance from cos centre to obj centre to take

    Cos.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Cos.MovBkwdSpeedInStrafe=1000  #Idem backwards

    Cos.MaxCombatDist=6000
    Cos.DistStop=1900.0
    Cos.DistStop2=2600.0
    Cos.NaturalWeapons=1
    Cos.HeadControlled=0



    Cos.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Cos.SetCDSphere(0,-160.0,500.0)#(numero de la espera, altura mm, radio mm)




    ####################
    #                  #
    # Small Spider     #
    #                  #
    ####################
    spd=Bladex.GetCharType("Spidersmall","Spd")

    spd.TurnSpeed=4.5
    spd.Jcost=2700
    spd.MaxFall=4000
    spd.DieFall=14000
    #The following is to make them climb rock and similar stuff. Problems otherwise!
    spd.MaxStair=400
    spd.Fov=math.pi
    spd.MaxGrab=3500.0
    spd.MedGrab=2500.0
    spd.Min2Grab=1500.0

    spd.MinTake=-500.0	# Min height above floor spider will take
    spd.MaxTake1=250.0	# Max height above floor for Take1 Anim
    spd.MaxTake2=550.0	# Max height above floor for Take2 Anim
    spd.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    spd.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    spd.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    spd.Reach=2000.0	# Max distance from cos centre to obj centre to take

    spd.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    spd.MovBkwdSpeedInStrafe=1000  #Idem backwards

    spd.MaxCombatDist=6000
    spd.DistStop=1100.0
    spd.DistStop2=2600.0
    spd.NaturalWeapons=1


    spd.SetNCDSpheres(1)
    spd.SetCDSphere(0,-100.0,500.0)
    spd.HeadControlled=0



    ####################
    #                  #
    #     Vampyre      #
    #                  #
    ####################

    vmp=Bladex.GetCharType("Vamp","Vmp")

    vmp.TurnSpeed=4.5
    vmp.Jcost=2700
    vmp.MaxFall=4000
    vmp.DieFall=14000
    vmp.MaxStair=335
    vmp.Fov=math.pi*1.5
    vmp.MaxGrab=3500.0
    vmp.MedGrab=2500.0
    vmp.Min2Grab=1500.0

    vmp.MinTake=-500.0	# Min height above floor vampire will take
    vmp.MaxTake1=250.0	# Max height above floor for Take1 Anim
    vmp.MaxTake2=550.0	# Max height above floor for Take2 Anim
    vmp.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    vmp.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    vmp.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    vmp.Reach=2000.0	# Max distance from vmp centre to obj centre to take
    vmp.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    vmp.MovBkwdSpeedInStrafe=1000  #Idem backwards
    vmp.MaxCombatDist=20000
    vmp.MaxSeeDist=50000

    vmp.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    vmp.SetCDSphere(0,500.0,340.0)  #(numero de la espera, altura mm, radio mm)
    vmp.SetCDSphere(1,100.0,520.0)  #(numero de la espera, altura mm, radio mm)

    vmp.DistStop=2500.0
    vmp.DistStop2=6000.0
    vmp.DistStopMaxFactor=0.2


    ####################
    #                  #
    #     Lich         #
    #                  #
    ####################

    lch=Bladex.GetCharType("Lich","Lch")

    lch.TurnSpeed=4.5
    lch.Jcost=2700
    lch.MaxFall=4000
    lch.DieFall=14000
    lch.MaxStair=335
    lch.DieFall=335
    lch.Fov=math.pi/1.2
    lch.MaxGrab=3500.0
    lch.MedGrab=2500.0
    lch.Min2Grab=1500.0

    lch.MinTake=-500.0	# Min height above floor lich will take
    lch.MaxTake1=250.0	# Max height above floor for Take1 Anim
    lch.MaxTake2=550.0	# Max height above floor for Take2 Anim
    lch.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    lch.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    lch.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    lch.Reach=2000.0	# Max distance from lch centre to obj centre to take
    lch.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    lch.MovBkwdSpeedInStrafe=1000  #Idem backwards
    lch.MaxCombatDist=10000
    lch.MaxSeeDist=15000
    lch.NaturalWeapons=1

    lch.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    lch.SetCDSphere(0,360.0,320.0)  #(numero de la espera, altura mm, radio mm)
    lch.SetCDSphere(1,-50.0,475.0)  #(numero de la espera, altura mm, radio mm)



    ####################
    #                  #
    #    Minotaur      #
    #                  #
    ####################
    Min=Bladex.GetCharType("Minotaur","Min")
    Min.IntName="Min" # En realidad , es este por defecto ( las 3 primeras letras )

    Min.TurnSpeed=4.5
    Min.Jcost=27000
    Min.MaxFall=4000
    Min.DieFall=14000
    Min.MaxStair=600
    Min.Fov=math.pi
    Min.MaxGrab=3500.0
    Min.MedGrab=2500.0
    Min.Min2Grab=1500.0

    Min.MinTake=-500.0	# Min height above floor MinMinian will take
    Min.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Min.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Min.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Min.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Min.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Min.Reach=2000.0	# Max distance from Min centre to obj centre to take
    Min.DistStop=3000.0
    Min.DistStop2=4000.0
    Min.MaxCombatDist=6000
    Min.DistStopMaxFactor=0.2
    Min.MaxSeeDist=30000
    Min.HeadControlled=0

    Min.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Min.SetCDSphere(0,-200.0,1000.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    #    Salamander    #
    #                  #
    ####################
    Slm=Bladex.GetCharType("Salamander","Slm")
    Slm.IntName="Slm" # En realidad , es este por defecto ( las 3 primeras letras )

    Slm.TurnSpeed=4.5
    Slm.Jcost=27000
    Slm.MaxFall=4000
    Slm.DieFall=14000
    Slm.MaxStair=700
    Slm.Fov=math.pi*1.5
    Slm.MaxGrab=3500.0
    Slm.MedGrab=2500.0
    Slm.Min2Grab=1500.0

    Slm.MinTake=-500.0		# Slm height above floor SlmSlmian will take
    Slm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Slm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Slm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Slm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Slm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Slm.Reach=2000.0	# Max distance from Slm centre to obj centre to take
    Slm.MaxCombatDist=10000
    Slm.DistStop=3700.0
    Slm.DistStop2=6000.0
    Slm.DistStopMaxFactor=0.05
    Slm.NaturalWeapons=1
    Slm.HeadControlled=0
    Slm.MaxSeeDist=40000

    Slm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Slm.SetCDSphere(0,-500.0,900.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    # Zombie  Knight   #
    #                  #
    ####################
    Zkn=Bladex.GetCharType("Knight_Zombie","Zkn")
    Zkn.IntName="Zkn" 


    Zkn.TurnSpeed=4.5
    Zkn.Jcost=2700
    Zkn.MaxFall=4000
    Zkn.DieFall=14000
    Zkn.MaxStair=335
    Zkn.Fov=math.pi/1.2
    Zkn.MaxGrab=3500.0
    Zkn.MedGrab=2500.0
    Zkn.Min2Grab=1500.0

    Zkn.MinTake=-500.0		# Min height above floor barbarian will take
    Zkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Zkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Zkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Zkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Zkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Zkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Zkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Zkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Zkn.HearMinVolume=0.001
    Zkn.MaxCombatDist=8000
    Zkn.DistStop=2000.0
    Zkn.DistStop2=6000.0
    Zkn.MaxSeeDist=15000
    Zkn.NaturalWeapons=1

    Zkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    Zkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    Zkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    # Dark Knight      #
    #                  #
    ####################
    Dkn=Bladex.GetCharType("Dark_Knight","Dkn")
    Dkn.IntName="Dkn" 

    Dkn.TurnSpeed=4.5
    Dkn.Jcost=2700
    Dkn.MaxFall=5000
    Dkn.DieFall=14000
    Dkn.MaxStair=335
    Dkn.Fov=math.pi/1.3
    Dkn.MaxGrab=3500.0
    Dkn.MedGrab=2500.0
    Dkn.Min2Grab=1500.0

    Dkn.MinTake=-500.0		# Min height above floor barbarian will take
    Dkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Dkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Dkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Dkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Dkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Dkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    Dkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Dkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Dkn.HearMinVolume=0.001
    Dkn.MaxCombatDist=8000
    Dkn.DistStop=2000.0
    Dkn.DistStop2=6000.0
    Dkn.MaxSeeDist=40000


    Dkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    Dkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    Dkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)


    ####################
    #                  #
    # Dal Gurak        #
    #                  #
    ####################
    Dgk=Bladex.GetCharType("DalGurak","Dgk")
    Dgk.IntName="Dgk" 

    Dgk.TurnSpeed=4.5
    Dgk.Jcost=2700
    Dgk.MaxFall=4000
    Dkn.DieFall=14000
    Dgk.MaxStair=335
    Dgk.Fov=math.pi
    Dgk.MaxGrab=3500.0
    Dgk.MedGrab=2500.0
    Dgk.Min2Grab=1500.0

    Dgk.MinTake=-500.0		# Min height above floor barbarian will take
    Dgk.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Dgk.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Dgk.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Dgk.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Dgk.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Dgk.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    Dgk.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Dgk.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Dgk.HearMinVolume=0.001
    Dgk.MaxCombatDist=120000
    Dgk.DistStop=8000.0
    Dgk.DistStop2=9000.0
    Dgk.DistStopMaxFactor=0.1
    Dgk.MaxSeeDist=120000
    Dgk.NaturalWeapons=1


    Dgk.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    Dgk.SetCDSphere(0,450.0,450.0)  #(numero de la espera, altura mm, radio mm)
    Dgk.SetCDSphere(1,50.0,650.0)  #(numero de la espera, altura mm, radio mm)



    ####################
    #                  #
    # An-Akhard        #
    #                  #
    ####################
    Ank=Bladex.GetCharType("DarkLord","Ank")
    Ank.IntName="Ank" 

    Ank.TurnSpeed=4.5
    Ank.Jcost=2700
    Ank.MaxFall=4000
    Ank.DieFall=14000
    Ank.MaxStair=335
    Ank.Fov=math.pi
    Ank.MaxGrab=3500.0
    Ank.MedGrab=2500.0
    Ank.Min2Grab=1500.0

    Ank.MinTake=-500.0		# Min height above floor barbarian will take
    Ank.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Ank.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Ank.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Ank.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Ank.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Ank.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    Ank.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Ank.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Ank.HearMinVolume=0.001
    Ank.MaxCombatDist=30000
    Ank.DistStop=2500.0
    Ank.DistStopMaxFactor=0.75
    Ank.DistStop2=8000.0
    Ank.MaxSeeDist=115000
    Ank.NaturalWeapons=1

    Ank.SetNCDSpheres(1)
    Ank.SetCDSphere(0,-50.0,1400.0)
    Ank.HeadControlled=0

    ####################
    #                  #
    # Golems           #
    #                  #
    ####################
    Glm=Bladex.GetCharType("Golem_stone","Glm_st")
    Glm.IntName="Glm" 

    Glm.TurnSpeed=4.5
    Glm.Jcost=2700
    Glm.MaxFall=4000
    Glm.DieFall=14000
    Glm.MaxStair=500
    Glm.Fov=math.pi
    Glm.MaxGrab=3500.0
    Glm.MedGrab=2500.0
    Glm.Min2Grab=1500.0

    Glm.MinTake=-500.0		# Min height above floor barbarian will take
    Glm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Glm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Glm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Glm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Glm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Glm.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Glm.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Glm.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Glm.HearMinVolume=0.001
    Glm.MaxCombatDist=12000
    Glm.DistStop=2000.0
    Glm.DistStopMaxFactor=0.3
    Glm.DistStop2=8000.0
    Glm.MaxSeeDist=50000
    Glm.NaturalWeapons=1

    Glm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Glm.SetCDSphere(0,-25.0,1000.0)  #(numero de la espera, altura mm, radio mm)


    Glm=Bladex.GetCharType("Golem_clay","Glm_cl")
    Glm.IntName="Glm" 

    Glm.TurnSpeed=4.5
    Glm.Jcost=2700
    Glm.MaxFall=4000
    Glm.DieFall=14000
    Glm.MaxStair=500
    Glm.Fov=math.pi
    Glm.MaxGrab=3500.0
    Glm.MedGrab=2500.0
    Glm.Min2Grab=1500.0

    Glm.MinTake=-500.0		# Min height above floor barbarian will take
    Glm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Glm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Glm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Glm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Glm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Glm.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Glm.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Glm.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Glm.HearMinVolume=0.001
    Glm.MaxCombatDist=12000
    Glm.DistStop=2000.0
    Glm.DistStopMaxFactor=0.3
    Glm.DistStop2=8000.0
    Glm.MaxSeeDist=50000
    Glm.NaturalWeapons=1

    Glm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Glm.SetCDSphere(0,-25.0,1000.0)  #(numero de la espera, altura mm, radio mm)



    Glm=Bladex.GetCharType("Golem_lava","Glm_lv")
    Glm.IntName="Glm" 

    Glm.TurnSpeed=4.5
    Glm.Jcost=2700
    Glm.MaxFall=4000
    Glm.DieFall=14000
    Glm.MaxStair=500
    Glm.Fov=math.pi
    Glm.MaxGrab=3500.0
    Glm.MedGrab=2500.0
    Glm.Min2Grab=1500.0

    Glm.MinTake=-500.0		# Min height above floor barbarian will take
    Glm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Glm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Glm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Glm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Glm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Glm.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Glm.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Glm.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Glm.HearMinVolume=0.001
    Glm.MaxCombatDist=12000
    Glm.DistStop=2000.0
    Glm.DistStopMaxFactor=0.3
    Glm.DistStop2=8000.0
    Glm.MaxSeeDist=50000
    Glm.NaturalWeapons=1

    Glm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Glm.SetCDSphere(0,-25.0,1000.0)  #(numero de la espera, altura mm, radio mm)



    Glm=Bladex.GetCharType("Golem_metal","Glm_mt")
    Glm.IntName="Glm" 

    Glm.TurnSpeed=4.5
    Glm.Jcost=2700
    Glm.MaxFall=4000
    Glm.DieFall=14000
    Glm.MaxStair=500
    Glm.Fov=math.pi
    Glm.MaxGrab=3500.0
    Glm.MedGrab=2500.0
    Glm.Min2Grab=1500.0

    Glm.MinTake=-500.0		# Min height above floor barbarian will take
    Glm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Glm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Glm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Glm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Glm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Glm.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Glm.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Glm.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Glm.HearMinVolume=0.001
    Glm.MaxCombatDist=12000
    Glm.DistStop=2000.0
    Glm.DistStopMaxFactor=0.3
    Glm.DistStop2=8000.0
    Glm.MaxSeeDist=50000
    Glm.NaturalWeapons=1

    Glm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Glm.SetCDSphere(0,-25.0,1000.0)  #(numero de la espera, altura mm, radio mm)




    Glm=Bladex.GetCharType("Golem_ice","Glm_ic")
    Glm.IntName="Glm" 

    Glm.TurnSpeed=4.5
    Glm.Jcost=2700
    Glm.MaxFall=4000
    Glm.DieFall=14000
    Glm.MaxStair=500
    Glm.Fov=math.pi
    Glm.MaxGrab=3500.0
    Glm.MedGrab=2500.0
    Glm.Min2Grab=1500.0

    Glm.MinTake=-500.0		# Min height above floor barbarian will take
    Glm.MaxTake1=250.0	# Max height above floor for Take1 Anim
    Glm.MaxTake2=550.0	# Max height above floor for Take2 Anim
    Glm.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    Glm.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    Glm.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    Glm.Reach=2000.0	# Max distance from tkn centre to obj centre to take
    Glm.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    Glm.MovBkwdSpeedInStrafe=1000  #Idem backwards
    Glm.HearMinVolume=0.001
    Glm.MaxCombatDist=12000
    Glm.DistStop=2000.0
    Glm.DistStopMaxFactor=0.3
    Glm.DistStop2=8000.0
    Glm.MaxSeeDist=50000
    Glm.NaturalWeapons=1

    Glm.SetNCDSpheres(1)  #Numero de esferas en el modelo de colisiones
    Glm.SetCDSphere(0,-25.0,1000.0)  #(numero de la espera, altura mm, radio mm)

    
    
    
    ####################
    #                  #
    # NPK	       #
    #                  #
    ####################
    
    
    tkn=Bladex.GetCharType("Duque","Duk")
    tkn.IntName="Tkn" 


    tkn.TurnSpeed=4.5
    tkn.Jcost=2700
    tkn.MaxFall=4000
    tkn.DieFall=14000
    tkn.MaxStair=335
    tkn.Fov=math.pi/1.2
    tkn.MaxGrab=3500.0
    tkn.MedGrab=2500.0
    tkn.Min2Grab=1500.0

    tkn.MinTake=-500.0		# Min height above floor barbarian will take
    tkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    tkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    tkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    tkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    tkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    tkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    tkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    tkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    tkn.HearMinVolume=0.001
    tkn.MaxCombatDist=8000
    tkn.DistStop=2000.0
    tkn.DistStop2=6000.0
    tkn.MaxSeeDist=30000


    tkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    tkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    tkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)
    
    
    
    
    
    tkn=Bladex.GetCharType("Mortimer","Mor")
    tkn.IntName="Tkn" 


    tkn.TurnSpeed=4.5
    tkn.Jcost=2700
    tkn.MaxFall=4000
    tkn.DieFall=14000
    tkn.MaxStair=335
    tkn.Fov=math.pi/1.2
    tkn.MaxGrab=3500.0
    tkn.MedGrab=2500.0
    tkn.Min2Grab=1500.0

    tkn.MinTake=-500.0		# Min height above floor barbarian will take
    tkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    tkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    tkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    tkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    tkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    tkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    tkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    tkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    tkn.HearMinVolume=0.001
    tkn.MaxCombatDist=8000
    tkn.DistStop=2000.0
    tkn.DistStop2=6000.0
    tkn.MaxSeeDist=30000


    tkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    tkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    tkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)





    tkn=Bladex.GetCharType("NP_Knight","npk")
    tkn.IntName="Tkn" 


    tkn.TurnSpeed=4.5
    tkn.Jcost=2700
    tkn.MaxFall=4000
    tkn.DieFall=14000
    tkn.MaxStair=335
    tkn.Fov=math.pi/1.2
    tkn.MaxGrab=3500.0
    tkn.MedGrab=2500.0
    tkn.Min2Grab=1500.0

    tkn.MinTake=-500.0		# Min height above floor barbarian will take
    tkn.MaxTake1=250.0	# Max height above floor for Take1 Anim
    tkn.MaxTake2=550.0	# Max height above floor for Take2 Anim
    tkn.MaxTake3=1300.0	# Max height above floor for Take3 Anim
    tkn.MaxTake4=1900.0	# Max height above floor for Take4 Anim
    tkn.MaxTake5=3000.0	# Max height above floor for Take5 Anim
    tkn.Reach=2000.0	# Max distance from tkn centre to obj centre to take

    tkn.MovFrwdSpeedInStrafe=1000  #Forwards speed when in strafe(combat mode only)
    tkn.MovBkwdSpeedInStrafe=1000  #Idem backwards
    tkn.HearMinVolume=0.001
    tkn.MaxCombatDist=8000
    tkn.DistStop=2000.0
    tkn.DistStop2=6000.0
    tkn.MaxSeeDist=30000


    tkn.SetNCDSpheres(2)  #Numero de esferas en el modelo de colisiones
    tkn.SetCDSphere(0,200.0,350.0)  #(numero de la espera, altura mm, radio mm)
    tkn.SetCDSphere(1,-110.0,490.0)  #(numero de la espera, altura mm, radio mm)




