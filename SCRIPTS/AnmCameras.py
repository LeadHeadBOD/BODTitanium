##///
##||| ANMCAMERAS.PY TITANIUM
##||| Change list:
##||| * Spear backattack animations now turn camera around
##||| * Made g2h_back slightly faster
##||| * Better synchronized camera turning for "turning around" animations
##||| * Dwarf turn animation camera rotation direction should now be correct.
##\\\ 


####################################################################################
#
#
#
#               T A B L E S   O F   T H E   C A M E R A   A N G L E S
#
#
#    USAGE:
#   Bladex.SetActionCameraMovement(char* action_name,double angle,double start_pos,double end_pos)
#     Interpolates the camera in the given action , the given angle in the given gap
#
#    * anm_name - name of the character animation without biped internal name prefix
#                 If the characters have vastly different animations, check the Kind first
#    
####################################################################################


def Init():
    import Bladex

    PI=3.14159

    #
    #Golpes
    #
    Bladex.SetActionCameraMovement("g_back",-1.0*PI,0.25,0.8)      ### Default value 0.1,0.5
    Bladex.SetActionCameraMovement("g2h_back",-1.0*PI,0.22,0.7)    ### Default value 0.25,1.0, was too slow in my opinion -LeadHead
    Bladex.SetActionCameraMovement("g_spear_back",-1.0*PI,0.1,0.3) ### Added -LeadHead

    #
    #Giros 180 grados
    #
        
    ###
    ### The character animations are NOT equal length
    ### Dwarf's animations even turn the opposite direction in some cases
    ### 
    ### This is disorienting, so we want to check what is the character type first -LeadHead
    ###
    player = Bladex.GetEntity("Player1")
    if player and player.Kind[0] == "D":
        Bladex.SetActionCameraMovement("jog_turn",PI,0.35,0.9)
        Bladex.SetActionCameraMovement("wlk_turn",-1.0*PI,0.3,0.9)
        Bladex.SetActionCameraMovement("snk_turn",-1.0*PI,0.1,0.9)
        Bladex.SetActionCameraMovement("rlx_turn",-1.0*PI,0.25,0.85)
    
    else:       ### if character is not a Dwarf or we fail to load a character at all
        Bladex.SetActionCameraMovement("jog_turn",-1.0*PI,0.3,0.9)
        Bladex.SetActionCameraMovement("wlk_turn",-1.0*PI,0.25,0.9)
        Bladex.SetActionCameraMovement("snk_turn",-1.0*PI,0.6,0.9)
        Bladex.SetActionCameraMovement("rlx_turn",PI,0.3,0.95)    

    #
    #Scripts puntuales
    #


    ########  Gay Ragnar Guy  ########
    Bladex.SetActionCameraMovement("end_ragnar",0.25*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("end_ragnar_ragnar",-0.25*PI,0.1,0.5)    ### PLAGUE: This animation doesn't exist?
    Bladex.SetActionCameraMovement("inicio_ragnar",PI,0.1,0.5)


    ########  Gold Mine  ########
    Bladex.SetActionCameraMovement("start_mina",PI,0.1,0.5)
    Bladex.SetActionCameraMovement("ambush_mine",0.5*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("escena01_mina",-0.5*PI,0.1,0.5)


    ######## The lost Labyrinth  ########
    Bladex.SetActionCameraMovement("inicio_laberinto",0.25*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("tablilla_laberinto",0.5*PI,0.1,0.5)


    ########  7th Dwarf    ########
    Bladex.SetActionCameraMovement("entrada", 0.5*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("masacre",-0.5*PI,0.1,0.5)

    ########  Dammed Tomb    ########
    Bladex.SetActionCameraMovement("reina_start",PI,0.1,0.5)
    Bladex.SetActionCameraMovement("tumba_rey",0.5*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("abrirsarcofago",0.25*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("tablilla_tumba",0.5*PI,0.1,0.5)

 
    ########  Dark Tower  ########
    Bladex.SetActionCameraMovement("dalgurak_appears3",-1.55,0.1,0.5)
    Bladex.SetActionCameraMovement("demoniogurak",2.33,0.1,0.5)
    Bladex.SetActionCameraMovement("gdemoniogurak",-PI/2,0.1,0.5)    
    Bladex.SetActionCameraMovement("inicio_torre",-PI/3,0.1,0.5)
    

    #######  Blade Tomb  #######
    Bladex.SetActionCameraMovement("start_oasis",PI,0.1,0.5)

    #######  Blade Btomb  #######
    Bladex.SetActionCameraMovement('tablilla_btomb',PI,0.1,0.5)


    #######  Orc fortress  #######
    Bladex.SetActionCameraMovement("prisionero",PI,0.1,0.5)
    Bladex.SetActionCameraMovement("start_orks",PI,0.1,0.5)

    #######  Monkey Island #######
    Bladex.SetActionCameraMovement("sala_tablillas",0.5*PI,0.1,0.5)
    Bladex.SetActionCameraMovement("start_isla",PI,0.1,0.5)

    #######  Ice palace #######
    Bladex.SetActionCameraMovement("tablilla_hielo",PI,0.1,0.5)

    #######  Chaos dimension #######
    Bladex.SetActionCameraMovement("fall_kaos",PI,0.1,0.5)
    Bladex.SetActionCameraMovement("jog_kaos01",-PI/2,0.1,0.5)
    Bladex.SetActionCameraMovement("jog_kaos02",-PI/2,0.1,0.5)
    Bladex.SetActionCameraMovement("jog_kaos03",-PI/2,0.1,0.5)
    Bladex.SetActionCameraMovement("jog_kaos04",-PI/2,0.1,0.5)
    
    Bladex.SetActionCameraMovement("sombra",        PI/2,0.1,0.5)
    Bladex.SetActionCameraMovement("demonio_kaos",  PI  ,0.1,0.5)
    
    #######  Inside Volcano #######
    Bladex.SetActionCameraMovement("start_volcan", -PI/2,0.1,0.5)
    



