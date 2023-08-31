####################################################################################
#
#
#
#               T A B L E S   O F   T H E   P E R S O N   S T A T E
#
#
#
####################################################################################




# 
#	Bladex.SetEventTableFuncC("Rlx","ActionEnd","Cycle")
#		1->Nombre tabla ( crea nueva si no existe)
#		2->Evento que ocurre
#		   Tipicos:
#			ActionEnd
#			FloorFail
#			FloorFailAd
#			Jump
#			Sneak
#			Walk
#			Stop
#			Etc...
#			
#		3->Respuesta a ese evento. Puede ser por codigo ( como aqui ) , o en python
#
#
#




def Init():

    import time
    firstTime= time.time()
    print "Creating tables for the bipeds..."
    import Bladex
    import Actions
    
    ## Titanium Config Fuctions ##
    TiCfgFound=0
    try:
        import TitaniumConfig
        TiCfgFound=1
    except:
        print "ActionTables.py --- Could not find Titanium Configurator"
        
    ## - - - - - - - - - - - - - ##
    
    ####################################################################################
    #
    # Relax .
    #
    ####################################################################################


    Bladex.SetEventTableFunc("Rlx","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("Rlx","ActionEnd","RlxCycle")
    #Bladex.SetEventTableFuncC("Rlx","Jump","TestJump")                     ###
    if TiCfgFound and (TitaniumConfig.TitaniumSetting("DodgeFix") == 1):    ###
        Bladex.SetEventTableFunc("Rlx","Jump",Actions.JumpHandler)          ### Changed 
        Bladex.SetEventTableFuncC("Rlx","Dodge","TestDodge")                ###
        Bladex.SetEventTableFuncC("Rlx","JumpWrap","TestJump")              ###
        print "~~~ DODGE FIX ENABLED ~~~"                                   ###
    else:                                                                   ###
        Bladex.SetEventTableFuncC("Rlx","Jump","TestJump")                  ###
        print "~~~ Titanium DodgeFix disabled ~~~"                          ###     -LeadHead
    Bladex.SetEventTableFuncC("Rlx","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("Rlx","StartBlock","StartBlockAndUpdate")
    Bladex.SetEventTableFuncC("Rlx","StopBlock","StopBlockAndUpdate")
    Bladex.SetEventTableFuncC("Rlx","Jog","StartJog")
    Bladex.SetEventTableFuncC("Rlx","Sneak","StartSneak")
    Bladex.SetEventTableFuncC("Rlx","Walk","StartWalk")
    Bladex.SetEventTableFuncC("Rlx","Back","StartBack")
    Bladex.SetEventTableFuncC("Rlx","JogBack","StartBackJogging")
    Bladex.SetEventTableFuncC("Rlx","SlipNeeded","SlipNeeded")    


    Bladex.SetEventTableFunc("Rlx","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("Rlx","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("Rlx","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("Rlx","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("Rlx","Turn180","RelaxTurn")
    #Bladex.SetEventTableFuncC("Rlx","2Right4Combat","2Right4Combat")
    #Bladex.SetEventTableFuncC("Rlx","2Left4Combat","2Left4Combat")
    Bladex.SetEventTableFunc("Rlx","TransitionEnded",Actions.GraspString)

    ####################################################################################
    #
    # Relax v. tired.
    #
    ####################################################################################
    Bladex.SetEventTableFunc("Rlx_vt","ActionStart",Actions.UnGraspString)
    #Bladex.SetEventTableFuncC("Rlx_vt","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("Rlx_vt","ActionEnd","EndGenericAction")    
    Bladex.SetEventTableFuncC("Rlx_vt","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFunc("Rlx_vt","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("Rlx_vt","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("Rlx_vt","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("Rlx_vt","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("Rlx_vt","Recover","EndGenericAction")


    ####################################################################################
    #
    # Pasos.- Andares
    #
    ####################################################################################

    # Para paso modificado con la pierna izquierda.
    ##Bladex.SetEventTableFuncC("LStepS","ActionEnd","RStep")
    #Bladex.SetEventTableFuncC("LStepS","Stop","StopWalk")
    #Bladex.SetEventTableFuncC("LStepS","FloorFail","FloorFail")

    # Para paso modificado con la pierna derecha.
    ##Bladex.SetEventTableFuncC("RStepS","ActionEnd","LStep")
    #Bladex.SetEventTableFuncC("RStepS","Stop","StopWalk")
    #Bladex.SetEventTableFuncC("RStepS","FloorFail","FloorFail")


    #Andar hacia detras
    Bladex.SetEventTableFunc("WBK","ActionStart",Actions.GraspString)
    Bladex.SetEventTableFunc("WBK","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("WBK","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("WBK","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("WBK","Jump","TestDodge")
    Bladex.SetEventTableFuncC("WBK","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("WBK","StopBackwards","CS_GoBackwards")
    Bladex.SetEventTableFuncC("WBK","JogBack","StartBackJogging")
    #Bladex.SetEventTableFuncC("WBK","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("WBK","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("WBK","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("WBK","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("WBK","StopTest","StopBack")
    Bladex.SetEventTableFuncC("WBK","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("WBK","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("WBK","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("WBK","StopTurn","StopTurn")
    Bladex.SetEventTableFuncC("WBK","Walk","StartWalk")
    Bladex.SetEventTableFuncC("WBK","Jog","StartJog")

    Bladex.SetEventTableFuncC("WBK","Turn180","RelaxTurn")


    Bladex.SetEventTableFunc("WBK","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("WBK","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("WBK","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("WBK","FloorFailAd","FloorFailAd")



    #Correr hacia detras
    Bladex.SetEventTableFunc("WBK_JOG","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFunc("WBK_JOG","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("WBK_JOG","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("WBK_JOG","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("WBK_JOG","Jump","TestDodge")
    Bladex.SetEventTableFuncC("WBK_JOG","Back","StartBack")
    Bladex.SetEventTableFuncC("WBK_JOG","Walk","StartWalk")

    Bladex.SetEventTableFuncC("WBK_JOG","Jog","StartJogBacking")
    Bladex.SetEventTableFuncC("WBK_JOG","StopJog","CS_Jog")


    Bladex.SetEventTableFuncC("WBK_JOG","StopBackwards","CS_GoBackwards")	
    #Bladex.SetEventTableFuncC("WBK_JOG","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("WBK_JOG","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("WBK_JOG","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("WBK_JOG","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("WBK_JOG","StopTest","StopBackJogging")	
    Bladex.SetEventTableFuncC("WBK_JOG","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("WBK_JOG","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("WBK_JOG","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("WBK_JOG","StopTurn","StopTurn")

    Bladex.SetEventTableFuncC("WBK_JOG","Turn180","RelaxTurn")

    Bladex.SetEventTableFunc("WBK_JOG","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("WBK_JOG","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("WBK_JOG","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("WBK_JOG","FloorFailAd","FloorFailAd")



    # Andar hacia delante , WLK

    Bladex.SetEventTableFunc("WLK","ActionStart",Actions.GraspString)
    Bladex.SetEventTableFunc("WLK","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("WLK","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("WLK","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("WLK","Jump","TestJump")
    #Bladex.SetEventTableFuncC("WLK","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("WLK","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("WLK","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("WLK","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("WLK","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("WLK","Jog","StartJogFromWalk")
    Bladex.SetEventTableFuncC("WLK","Sneak","StartSneakFromWalk")
    Bladex.SetEventTableFuncC("WLK","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("WLK","StopTest","StopWalk")
    Bladex.SetEventTableFuncC("WLK","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("WLK","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("WLK","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("WLK","StopTurn","StopTurn")
    Bladex.SetEventTableFuncC("WLK","Back","StartBack")
    Bladex.SetEventTableFuncC("WLK","JogBack","StartBackJogging")

    Bladex.SetEventTableFuncC("WLK","Turn180","WalkTurn")

    Bladex.SetEventTableFunc("WLK","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("WLK","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("WLK","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("WLK","FloorFailAd","FloorFailAd")


    # Andar hacia delante , JOG
    Bladex.SetEventTableFunc("JOG","ActionStart",Actions.GraspString)
    Bladex.SetEventTableFunc("JOG","InstantAttack",Actions.InstantAttackRun)
    Bladex.SetEventTableFuncC("JOG","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("JOG","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("JOG","Jump","TestJump")
    Bladex.SetEventTableFuncC("JOG","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("JOG","Walk","StartWalk")
    Bladex.SetEventTableFuncC("JOG","StopForwards","CS_Jog")
    Bladex.SetEventTableFuncC("JOG","StopTest","StopJog")
    #Bladex.SetEventTableFuncC("JOG","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("JOG","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("JOG","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("JOG","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("JOG","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("JOG","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("JOG","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("JOG","StopTurn","StopTurn")
    Bladex.SetEventTableFuncC("JOG","Back","StartBack")
    Bladex.SetEventTableFuncC("JOG","JogBack","StartBackJogging")

    Bladex.SetEventTableFuncC("JOG","Turn180","JogTurn")


    Bladex.SetEventTableFunc("JOG","DthFllArrivedWarper",Actions.DthFllArrivedWarper)
    Bladex.SetEventTableFuncC("JOG","DthFllArrived","DthFllArrived")
    Bladex.SetEventTableFuncC("JOG","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("JOG","FloorFailAd","FloorFailAd")

    # Andar hacia delante ,SNEAK
    Bladex.SetEventTableFunc("SNK","ActionStart",Actions.GraspString)
    Bladex.SetEventTableFunc("SNK","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("SNK","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("SNK","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("SNK","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("SNK","Walk","StartWalk")
    Bladex.SetEventTableFuncC("SNK","StopForwards","CS_Sneak")
    #Bladex.SetEventTableFuncC("SNK","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("SNK","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("SNK","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("SNK","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("SNK","StopTest","StopSneak")
    Bladex.SetEventTableFuncC("SNK","ActionEnd","Cycle")
    Bladex.SetEventTableFuncC("SNK","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("SNK","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("SNK","StopTurn","StopTurn")
    Bladex.SetEventTableFuncC("SNK","Back","StartBack")
    Bladex.SetEventTableFuncC("SNK","JogBack","StartBackJogging")

    Bladex.SetEventTableFuncC("SNK","Turn180","SneakTurn")


    Bladex.SetEventTableFuncC("SNK","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("SNK","FloorFailAd","FloorFailAd")


    ####################################################################################
    #
    # Turning 180 degrees
    #
    ####################################################################################

    Bladex.SetEventTableFunc("TURNING","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("TURNING","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("TURNING","TransitionEnded","TestIfSlipNeeded")
    Bladex.SetEventTableFuncC("TURNING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("TURNING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("TURNING","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("TURNING","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("TURNING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("TURNING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("TURNING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("TURNING","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("TURNING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("TURNING","JogBack","SS_GoBackwards")
    Bladex.SetEventTableFuncC("TURNING","StopBackwards","CS_GoBackwards")	

    #Bladex.SetEventTableFuncC("TURNING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("TURNING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("TURNING","FloorFailAd","FloorFailAd")



    ####################################################################################
    #
    # Falling
    #
    ####################################################################################

    Bladex.SetEventTableFunc("Fll","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("Fll","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("Fll","TransitionEnded","FllTransitionEnded")
    Bladex.SetEventTableFuncC("Fll","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("Fll","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("Fll","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("Fll","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("Fll","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("Fll","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("Fll","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("Fll","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("Fll","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("Fll","StopBackwards","CS_GoBackwards")
    Bladex.SetEventTableFuncC("Fll","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("Fll","StopStrafeRight","CS_StrafeRight")
    Bladex.SetEventTableFuncC("Fll","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("Fll","StopStrafeLeft","CS_StrafeLeft")

    Bladex.SetEventTableFuncC("Fll","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("Fll","ConstraintsChanged","Fall")

    Bladex.SetEventTableFunc("Dth_Fll2","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("Dth_Fll2","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("Dth_Fll2","TransitionEnded","FllTransitionEnded")
    Bladex.SetEventTableFuncC("Dth_Fll2","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("Dth_Fll2","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("Dth_Fll2","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("Dth_Fll2","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("Dth_Fll2","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopBackwards","CS_GoBackwards")
    Bladex.SetEventTableFuncC("Dth_Fll2","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopStrafeRight","CS_StrafeRight")
    Bladex.SetEventTableFuncC("Dth_Fll2","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("Dth_Fll2","StopStrafeLeft","CS_StrafeLeft")
    Bladex.SetEventTableFuncC("Dth_Fll2","ActionEnd","EndDthFll2")
    Bladex.SetEventTableFuncC("Dth_Fll2","DthFllArrived","DthFllArrived")

    #Bladex.SetEventTableFunc("Dth","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("Dth","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("Dth","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("Dth","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("Dth","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("Dth","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("Dth","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("Dth","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("Dth","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("Dth","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("Dth","StopBackwards","CS_GoBackwards")
    Bladex.SetEventTableFuncC("Dth","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("Dth","StopStrafeRight","CS_StrafeRight")
    Bladex.SetEventTableFuncC("Dth","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("Dth","StopStrafeLeft","CS_StrafeLeft")
    Bladex.SetEventTableFuncC("Dth","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("Dth","ConstraintsChanged","Fall")





    Bladex.SetEventTableFunc("Dth_Fll","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("Dth_Fll","ActionEnd","EndDthFll")
    Bladex.SetEventTableFunc("Dth_Fll","Interrupt",Actions.InterruptFllHugeHandler)
    Bladex.SetEventTableFunc("Dth_Fll","TransitionEnded",Actions.EndTransitionFllHugeHandler)
    Bladex.SetEventTableFuncC("Dth_Fll","DthFllArrived","DthFllArrived")




    ####################################################################################
    #
    # Animaciones en combate
    #
    ####################################################################################

    #Relax facing 
    Bladex.SetEventTableFunc("FING_RLX","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_RLX","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_RLX","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_RLX","Jump","TestDodge")
    Bladex.SetEventTableFuncC("FING_RLX","StartBlock","StartBlockAndUpdate")
    Bladex.SetEventTableFuncC("FING_RLX","StopBlock","StopBlockAndUpdate")
    #Bladex.SetEventTableFuncC("FING_RLX","Jog","StartJog")
    Bladex.SetEventTableFuncC("FING_RLX","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_RLX","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_RLX","Sneak","StartSneak")
    Bladex.SetEventTableFuncC("FING_RLX","Walk","StartWalkFacing")
    Bladex.SetEventTableFuncC("FING_RLX","Back","StartBackFacing")
    Bladex.SetEventTableFuncC("FING_RLX","StrafeRight","StartStrafeRight")
    Bladex.SetEventTableFuncC("FING_RLX","StrafeLeft","StartStrafeLeft")
    Bladex.SetEventTableFuncC("FING_RLX","ActionEnd","Cycle")
    #Bladex.SetEventTableFuncC("FING_RLX","2Right4Combat","2Right4Combat")
    #Bladex.SetEventTableFuncC("FING_RLX","2Left4Combat","2Left4Combat")

    Bladex.SetEventTableFuncC("FING_RLX","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_RLX","FloorFailAd","FloorFailAd")


    #Turning while in fac
    Bladex.SetEventTableFuncC("FING_TURN","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_TURN","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("FING_TURN","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_TURN","ActionEnd","TransferAngle")
    Bladex.SetEventTableFuncC("FING_TURN","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("FING_TURN","StopBlock","StopBlock")


    Bladex.SetEventTableFuncC("FING_TURN","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_TURN","FloorFailAd","FloorFailAd")


    # Facinf , forwards , with shield 
    Bladex.SetEventTableFunc("FING_FRW_S","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_FRW_S","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_FRW_S","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_FRW_S","Back","StartBackFacing")
    Bladex.SetEventTableFuncC("FING_FRW_S","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("FING_FRW_S","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_FRW_S","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_FRW_S","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("FING_FRW_S","StopTest","StopWalkFacing")
    #Bladex.SetEventTableFuncC("FING_FRW_S","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_FRW_S","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_FRW_S","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_FRW_S","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_FRW_S","StrafeRight","StartStrafeRight")
    Bladex.SetEventTableFuncC("FING_FRW_S","StrafeLeft","StartStrafeLeft")
    Bladex.SetEventTableFuncC("FING_FRW_S","ActionEnd","Cycle")

    #3 sigus -> Internam. fuiltro por si encarado nada
    Bladex.SetEventTableFuncC("FING_FRW_S","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("FING_FRW_S","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("FING_FRW_S","StopTurn","StopTurn")


    Bladex.SetEventTableFuncC("FING_FRW_S","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_FRW_S","FloorFailAd","FloorFailAd")


    # Facinf , forwards , without shield
    Bladex.SetEventTableFunc("FING_FRW","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_FRW","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_FRW","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_FRW","Back","StartBackFacing")
    Bladex.SetEventTableFuncC("FING_FRW","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("FING_FRW","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_FRW","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_FRW","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("FING_FRW","StopTest","StopWalkFacing")
    #Bladex.SetEventTableFuncC("FING_FRW","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_FRW","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_FRW","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_FRW","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_FRW","StrafeRight","StartStrafeRight")
    Bladex.SetEventTableFuncC("FING_FRW","StrafeLeft","StartStrafeLeft")
    Bladex.SetEventTableFuncC("FING_FRW","ActionEnd","Cycle")

    Bladex.SetEventTableFuncC("FING_FRW","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_FRW","FloorFailAd","FloorFailAd")

    Bladex.SetEventTableFuncC("FING_FRW","Sneak","SS_Sneak")          # Added
    Bladex.SetEventTableFuncC("FING_FRW","StopSneak","CS_Sneak")

    #Facing , backwards , with shield
    Bladex.SetEventTableFunc("FING_BWD_S","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_BWD_S","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_BWD_S","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_BWD_S","Walk","StartWalkFacing")
    Bladex.SetEventTableFuncC("FING_BWD_S","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_BWD_S","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_BWD_S","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("FING_BWD_S","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("FING_BWD_S","StopTest","StopBackFacing")
    #Bladex.SetEventTableFuncC("FING_BWD_S","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_BWD_S","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_BWD_S","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_BWD_S","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_BWD_S","StrafeRight","StartStrafeRight")
    Bladex.SetEventTableFuncC("FING_BWD_S","StrafeLeft","StartStrafeLeft")
    Bladex.SetEventTableFuncC("FING_BWD_S","ActionEnd","Cycle")

    #3 sigus -> Internam. fuiltro por si encarado nada
    Bladex.SetEventTableFuncC("FING_BWD_S","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("FING_BWD_S","TurnLeft","TurnLeft")
    Bladex.SetEventTableFuncC("FING_BWD_S","StopTurn","StopTurn")


    Bladex.SetEventTableFuncC("FING_BWD_S","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_BWD_S","FloorFailAd","FloorFailAd")



    #Facing , backwards , without shield
    Bladex.SetEventTableFunc("FING_BWD","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_BWD","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_BWD","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_BWD","Jump","TestDodge")
    Bladex.SetEventTableFuncC("FING_BWD","Walk","StartWalkFacing")
    Bladex.SetEventTableFuncC("FING_BWD","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_BWD","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_BWD","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("FING_BWD","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("FING_BWD","StopTest","StopBackFacing")
    #Bladex.SetEventTableFuncC("FING_BWD","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_BWD","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_BWD","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_BWD","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_BWD","StrafeRight","StartStrafeRight")
    Bladex.SetEventTableFuncC("FING_BWD","StrafeLeft","StartStrafeLeft")
    Bladex.SetEventTableFuncC("FING_BWD","ActionEnd","Cycle")

    Bladex.SetEventTableFuncC("FING_BWD","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_BWD","FloorFailAd","FloorFailAd")

    #Facing , strafe right , without shield
    Bladex.SetEventTableFunc("FING_RIGHT","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_RIGHT","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_RIGHT","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_RIGHT","Jump","TestDodge")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopTest","StopStrafeRight")
    #Bladex.SetEventTableFuncC("FING_RIGHT","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_RIGHT","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_RIGHT","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_RIGHT","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopStrafeRight","CS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_RIGHT","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopStrafeLeft","CS_StrafeLeft")

    Bladex.SetEventTableFuncC("FING_RIGHT","TransitionEnded","StrafeTranEnded")
    Bladex.SetEventTableFuncC("FING_RIGHT","ActionEnd","Cycle")

    Bladex.SetEventTableFuncC("FING_RIGHT","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_RIGHT","Walk","SS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopForwards","CS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT","Back","SS_BackwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT","StopBackwards","CS_BackwardsInStrafe")	

    #Bladex.SetEventTableFuncC("FING_RIGHT","2Right4Combat","2Right4Combat")
    Bladex.SetEventTableFuncC("FING_RIGHT","2Left4Combat","2Left4Combat")

    Bladex.SetEventTableFuncC("FING_RIGHT","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_RIGHT","FloorFailAd","FloorFailAd")


    #Facing , strafe right , with shield
    Bladex.SetEventTableFunc("FING_RIGHT_S","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_RIGHT_S","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopTest","StopStrafeRight")
    #Bladex.SetEventTableFuncC("FING_RIGHT_S","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_RIGHT_S","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopStrafeRight","CS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopStrafeLeft","CS_StrafeLeft")

    Bladex.SetEventTableFuncC("FING_RIGHT_S","TransitionEnded","StrafeTranEnded")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","ActionEnd","Cycle")

    #Bladex.SetEventTableFuncC("FING_RIGHT_S","2Right4Combat","2Right4Combat")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","2Left4Combat","2Left4Combat")


    Bladex.SetEventTableFuncC("FING_RIGHT_S","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","Walk","SS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopForwards","CS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","Back","SS_BackwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","StopBackwards","CS_BackwardsInStrafe")	

    Bladex.SetEventTableFuncC("FING_RIGHT_S","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_RIGHT_S","FloorFailAd","FloorFailAd")



    #Facing , strafe left , without shield
    Bladex.SetEventTableFunc("FING_LEFT","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_LEFT","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_LEFT","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_LEFT","Jump","TestDodge")
    Bladex.SetEventTableFuncC("FING_LEFT","StopTest","StopStrafeLeft")
    #Bladex.SetEventTableFuncC("FING_LEFT","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_LEFT","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_LEFT","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_LEFT","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_LEFT","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_LEFT","StopStrafeLeft","CS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_LEFT","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_LEFT","StopStrafeRight","CS_StrafeRight")

    Bladex.SetEventTableFuncC("FING_LEFT","TransitionEnded","StrafeTranEnded")
    Bladex.SetEventTableFuncC("FING_LEFT","ActionEnd","Cycle")

    Bladex.SetEventTableFuncC("FING_LEFT","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_LEFT","StopJog","CS_Jog")

    Bladex.SetEventTableFuncC("FING_LEFT","Walk","SS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT","StopForwards","CS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT","Back","SS_BackwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT","StopBackwards","CS_BackwardsInStrafe")	

    Bladex.SetEventTableFuncC("FING_LEFT","2Right4Combat","2Right4Combat")
    #Bladex.SetEventTableFuncC("FING_LEFT","2Left4Combat","2Left4Combat")


    Bladex.SetEventTableFuncC("FING_LEFT","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_LEFT","FloorFailAd","FloorFailAd")




    #Facing , strafe left , with shield
    Bladex.SetEventTableFunc("FING_LEFT_S","InstantAttack",Actions.InstantAttackSlow)
    Bladex.SetEventTableFuncC("FING_LEFT_S","ToggleFacing","ToggleFacing")
    Bladex.SetEventTableFuncC("FING_LEFT_S","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopTest","StopStrafeLeft")
    #Bladex.SetEventTableFuncC("FING_LEFT_S","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("FING_LEFT_S","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StrafeLeft","SS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopStrafeLeft","CS_StrafeLeft")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StrafeRight","SS_StrafeRight")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopStrafeRight","CS_StrafeRight")

    Bladex.SetEventTableFuncC("FING_LEFT_S","TransitionEnded","StrafeTranEnded")
    Bladex.SetEventTableFuncC("FING_LEFT_S","ActionEnd","Cycle")

    Bladex.SetEventTableFuncC("FING_LEFT_S","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopJog","CS_Jog")

    Bladex.SetEventTableFuncC("FING_LEFT_S","Walk","SS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopForwards","CS_ForwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT_S","Back","SS_BackwardsInStrafe")
    Bladex.SetEventTableFuncC("FING_LEFT_S","StopBackwards","CS_BackwardsInStrafe")	

    Bladex.SetEventTableFuncC("FING_LEFT_S","2Right4Combat","2Right4Combat")
    #Bladex.SetEventTableFuncC("FING_LEFT_S","2Left4Combat","2Left4Combat")


    Bladex.SetEventTableFuncC("FING_LEFT_S","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("FING_LEFT_S","FloorFailAd","FloorFailAd")

    ####################################################################################
    #
    # Muertes estancadas
    #
    ####################################################################################


    Bladex.SetEventTableFuncC("DTH_STUCK","ActionEnd","EventStop")

    Bladex.SetEventTableFuncC("dth_rock","ActionEnd","EventStop")
    Bladex.SetEventTableFuncC("dth_rockfront","ActionEnd","EventStop")





    ####################################################################################
    #
    # Escalar + Salto + Slip
    #
    ####################################################################################


    # Escalar
    Bladex.SetEventTableFunc("CLIMBING","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("CLIMBING","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("CLIMBING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("CLIMBING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("CLIMBING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("CLIMBING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("CLIMBING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("CLIMBING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("CLIMBING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("CLIMBING","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("CLIMBING","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("CLIMBING","StopBlock","StopBlock")


    #Bladex.SetEventTableFuncC("CLIMBING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("CLIMBING","FloorFailAd","FloorFailAd")


    # Salto...
    Bladex.SetEventTableFunc("JUMPING","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("JUMPING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("JUMPING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("JUMPING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("JUMPING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("JUMPING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("JUMPING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("JUMPING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("JUMPING","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("JUMPING","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("JUMPING","StopBlock","StopBlock")

    Bladex.SetEventTableFuncC("JUMPING","SlipNeeded","SlipNeeded")

    Bladex.SetEventTableFuncC("JUMPING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("JUMPING","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("JUMPING","ConstraintsChanged","Fall")
    Bladex.SetEventTableFuncC("JUMPING","FallTest","FallTest")


    Bladex.SetEventTableFuncC("SLIPPING","SlipNeeded","SlipNeeded") #If slope change...
    Bladex.SetEventTableFuncC("SLIPPING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("SLIPPING","Stop","CS_GoForwards")
    Bladex.SetEventTableFuncC("SLIPPING","Jump","TestJumpInSlip")
    Bladex.SetEventTableFuncC("SLIPPING","SlipStop","SlipStop")
    Bladex.SetEventTableFuncC("SLIPPING","ActionEnd","Cycle")
    #Bladex.SetEventTableFuncC("SLIPPING","TransitionEnded","SlipTransitionEnded")
    Bladex.SetEventTableFuncC("SLIPPING","AnmChange","SlipChange")

    Bladex.SetEventTableFuncC("SLIPPING","FloorFailAd","FloorFailAd")  
    Bladex.SetEventTableFuncC("SLIPPING","FloorFail","FloorFail")



    Bladex.SetEventTableFunc("SLIP_END","ActionStart",Actions.GraspString)
    Bladex.SetEventTableFuncC("SLIP_END","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("SLIP_END","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("SLIP_END","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("SLIP_END","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("SLIP_END","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("SLIP_END","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("SLIP_END","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("SLIP_END","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("SLIP_END","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("SLIP_END","StopBlock","StopBlock")
    

    Bladex.SetEventTableFuncC("SLIP_END","FloorFailAd","FloorFailAd")  
    Bladex.SetEventTableFuncC("SLIP_END","FloorFail","FloorFail")



    ####################################################################################
    #
    # Bowing...
    #
    ####################################################################################


    Bladex.SetEventTableFunc("BOWING","ActionEnd",Actions.EndDrawBowEventHandler)
    Bladex.SetEventTableFuncC("BOWING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("BOWING","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("BOWING","SlipNeeded","SlipNeeded")

    Bladex.SetEventTableFunc("RELOADING","ActionEnd",Actions.EndReloadBowEventHandler)
    Bladex.SetEventTableFuncC("RELOADING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("RELOADING","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("RELOADING","SlipNeeded","SlipNeeded")




    ####################################################################################
    #
    # Parry(2Handed) + Ataques + Esquivas
    #
    ####################################################################################

    Bladex.SetEventTableFuncC("PARRYING","SlipNeeded","SlipNeeded")

    Bladex.SetEventTableFuncC("PARRYING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("PARRYING","FloorFailAd","FloorFailAd")

    Bladex.SetEventTableFuncC("PARRYING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("PARRYING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("PARRYING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("PARRYING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("PARRYING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("PARRYING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("PARRYING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("PARRYING","StopSneak","CS_Sneak")

    Bladex.SetEventTableFuncC("PARRYING","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("PARRYING","StopBlock","StopBlock")






    Bladex.SetEventTableFunc("HURT","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("HURT","SlipNeeded","SlipNeeded")

    Bladex.SetEventTableFuncC("HURT","HurtFinalItp","NextMoveIfKey")
    Bladex.SetEventTableFuncC("HURT","HitFinalItp","NextMoveIfKeyOrAttack")


    Bladex.SetEventTableFuncC("HURT","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("HURT","FloorFailAd","FloorFailAd")

    Bladex.SetEventTableFuncC("HURT","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("HURT","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("HURT","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("HURT","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("HURT","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("HURT","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("HURT","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("HURT","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("HURT","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("HURT","StopBlock","StopBlock")




    ####################################################################################
    #
    # Attacking
    #
    ####################################################################################

    Bladex.SetEventTableFuncC("ATTACKING","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFunc("ATTACKING","HitFinalItp",Actions.LinkNextAttack)
    Bladex.SetEventTableFuncC("ATTACKING","HitFinalItpC","LinkNextAttack")
    Bladex.SetEventTableFunc("ATTACKING","ActionEnd",Actions.EndOfAttack)
    Bladex.SetEventTableFuncC("ATTACKING","ActionEndC","EndOfAttack")
    Bladex.SetEventTableFuncC("ATTACKING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("ATTACKING","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("ATTACKING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("ATTACKING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("ATTACKING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("ATTACKING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("ATTACKING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("ATTACKING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("ATTACKING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("ATTACKING","StopSneak","CS_Sneak")
    Bladex.SetEventTableFunc("ATTACKING","TransitionEnded",Actions.BackUpEnemy)
    Bladex.SetEventTableFunc("ATTACKING","Swap180",Actions.Swap180Handler)
    Bladex.SetEventTableFuncC("ATTACKING","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("ATTACKING","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("ATTACKING","Jump","BreakAndTestDodge")
    Bladex.SetEventTableFuncC("ATTACKING","Interrupt","EndGenericAction")

    ####################################################################################

    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","HitFinalItp","LinkNextAttack")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","ActionEnd","EndOfAttack")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","FloorFailAd","FloorFailAd")
    Bladex.SetEventTableFuncC("ATTACKING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("ATTACKING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("ATTACKING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("ATTACKING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","StopSneak","CS_Sneak")
    Bladex.SetEventTableFunc("ATTACKING_NOMOVE","TransitionEnded",Actions.BackUpEnemy)
    Bladex.SetEventTableFunc("ATTACKING_NOMOVE","Swap180",Actions.Swap180Handler)
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","StopBlock","StopBlockAndChange")
    Bladex.SetEventTableFuncC("ATTACKING_NOMOVE","Interrupt","EndGenericAction")

    ####################################################################################


    Bladex.SetEventTableFunc("DODGING","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("DODGING","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("DODGING","HitFinalItp","LinkNextAttack")

    Bladex.SetEventTableFuncC("DODGING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("DODGING","FloorFailAd","FloorFailAd")

    Bladex.SetEventTableFuncC("DODGING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("DODGING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("DODGING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("DODGING","StopBackwards","CS_GoBackwards")	
    Bladex.SetEventTableFuncC("DODGING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("DODGING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("DODGING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("DODGING","StopSneak","CS_Sneak")


    #Bladex.SetEventTableFuncC("DODGING","StartBlock","StartBlock")
    #Bladex.SetEventTableFuncC("DODGING","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("DODGING","StartBlock","StartBlockAndChange")
    Bladex.SetEventTableFuncC("DODGING","StopBlock","StopBlockAndChange")


    Bladex.SetEventTableFuncC("DODGING","TurnRight","TurnRight")
    Bladex.SetEventTableFuncC("DODGING","TurnLeft","TurnLeft")

    Bladex.SetEventTableFuncC("DODGING","ActionEnd","EndOfAttack")



    ####################################################################################
    #
    # INSULT
    #
    ####################################################################################

    Bladex.SetEventTableFunc("INSULTING","ActionStart",Actions.UnGraspString)
    Bladex.SetEventTableFuncC("INSULTING","SlipNeeded","SlipNeeded")
    Bladex.SetEventTableFuncC("INSULTING","TransitionEnded","TestIfSlipNeeded")
    Bladex.SetEventTableFuncC("INSULTING","Walk","SS_GoForwards")
    Bladex.SetEventTableFuncC("INSULTING","StopForwards","CS_GoForwards")
    Bladex.SetEventTableFuncC("INSULTING","StartBlock","StartBlock")
    Bladex.SetEventTableFuncC("INSULTING","StopBlock","StopBlock")
    Bladex.SetEventTableFuncC("INSULTING","Jog","SS_Jog")
    Bladex.SetEventTableFuncC("INSULTING","StopJog","CS_Jog")
    Bladex.SetEventTableFuncC("INSULTING","Sneak","SS_Sneak")
    Bladex.SetEventTableFuncC("INSULTING","StopSneak","CS_Sneak")
    Bladex.SetEventTableFuncC("INSULTING","Back","SS_GoBackwards")
    Bladex.SetEventTableFuncC("INSULTING","JogBack","SS_GoBackwards")
    Bladex.SetEventTableFuncC("INSULTING","StopBackwards","CS_GoBackwards")	

    Bladex.SetEventTableFuncC("INSULTING","FloorFail","FloorFail")
    Bladex.SetEventTableFuncC("INSULTING","FloorFailAd","FloorFailAd")




    ####################################################################################
    #
    # Interactive Various Actions (IVA)
    #
    ####################################################################################




    Bladex.SetEventTableFunc("IVA","ActionStart",Actions.UnGraspString)

    nowTime= time.time()
    print "tables created ("+`nowTime-firstTime`+" seconds)"