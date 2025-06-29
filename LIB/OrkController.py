"""
                                                  ####################
                                                  # OrkController.py #
                                                  ####################

    /#######################################################################################################################\
    #Usage:                                                                                                                 #
    # Written on basis of LevelFuncs.py                                                                                     #
    #                                                                                                                       #
    # Import OrkController.py in the relevant map module where you are spawning enemies, usually enemigos.py                #
    #                                                                                                                       #
    # When using Bladex.CreateEntity(...) replace "Kind" with "OrkController.MinorOrk" to spawn a regular orc variation     #
    # or "OrkController.BigOrk" to spawn a Great Ork variation                                                              #
    #                                                                                                                       #
    #   Arguments:                                                                                                          #
    #     1 - level threshold to spawn a dark ork                                                                           #
    #     2 - level thershold to spawn a gold ork                                                                           #
    #                                                                                                                       #
    # These arguments can be defined at the start of the enemy module                                                       #
    # or adjusted on a per-enemy basis                                                                                      #
    # set the OrgThreshold impossibly high if you do not want Gold_Ork to spawn                                             #
    # set the OrgThreshold below the DokThreshold if you want to make Gold_Ork spawning to take priority                    #
    #                                                                                                                       #
    # The function will run an easy calculation to see                                                                      #
    # where the character's level fits within the thresholds                                                                #
    # and return "Kind" value that corresponds to the relevant ork                                                          #
    #                                                                                                                       #
    #                                                                                               -LeadHead               #
    #                                                                                                                       #
    \#######################################################################################################################/
    
    
"""

import Bladex
import CharStats
import BBLib

DEBUG_ORK_CONTROLLER = 0

BBLib.ReadMMP('../../3dChars/Ork.mmp')    ### Need to load these manually, otherwise most orks will have incorrect textures.
BBLib.ReadMMP('../../3dChars/Dork.mmp')
BBLib.ReadMMP('../../3dchars/Org.mmp')

player=Bladex.GetEntity("Player1")
OrkLimit=1.0*CharStats.GetCharExperienceCost(player.CharType, player.Level)     ## We are retrieving level-up progress (experience) and then rounding the number up/down
ork_adjusted_lvl= round(player.Level + player.PartialLevel/OrkLimit)            ## If a player is close to leveling up, they might still trigger the threshold

if DEBUG_ORK_CONTROLLER: print "player name is "+player.Name+" and their actual level is "+`ork_adjusted_lvl`

def MinorOrk(DokThreshold, OrgThreshold):

    try:
        if ork_adjusted_lvl>=OrgThreshold:
            if DEBUG_ORK_CONTROLLER: print "player level is "+`ork_adjusted_lvl`+" and so we spawn GOLD ork"
            return "Gold_Ork"
        elif ork_adjusted_lvl>=DokThreshold:
            if DEBUG_ORK_CONTROLLER: print "player level is "+`ork_adjusted_lvl`+" and so we spawn DARK ork"
            return "Dark_Ork"
        else:
            if DEBUG_ORK_CONTROLLER: print "player is weak so we spawn your average neighborhood ork"
            return "Ork"                                    ### If neither threshold is reached, spawn a regular orc
    except:
        print "!ERROR! in OrkController - Player1 may not be accessible"
        return "Ork"

def AnyOrk(AnyGoThreshold, AnyDokThreshold, AnyOrgThreshold):   ### TO DO 
    return "Ork"
    print "!~WARNING~! in OrkController - AnyOrk called, not implemented yet"

def BigOrk(): ### TO DO - there are no GreatOrk variations implemented yet
    return "Great_Ork"
    print "!~WARNING~! in OrkController - BigOrk variation not implemented yet"


#############################################################################################
#                             ~~ For custom maps/mods ~~ 
#
#   - We want to retain compatibility across any version of the game, even if Titanium
#     and subsequently OrkController is not installed. As such, I highly recommend that
#     the py func "try" is used before importing OrkController.
#     If it fails, make sure that the game still returns some kind of value,
#     otherwise you WILL crash the game.
#     
#     See "../MAPS/+map_name+/ENEMIGOS.PY" for examples
#
#   - AnyOrk is used when you don't know what kind of Orc should be best.
#     As long as the relevant "AnyOrk" threshold is met, it will spawn
#     the most suitable type of orc, whether that be regular, great, dark, gold.
#
#   - Remember that Ork thresholds can be tied to functions as well
#     As such, it's possible to dynamically increase/decrease the threshold if certain
#     conditions are met - locations visited, items picked up, random number generators, etc.
#     This might be useful in making your map more unique.
#
##############################################################################################