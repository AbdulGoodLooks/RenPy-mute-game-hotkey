## By Abdul

## When False, the mute indicator will not show. Useful when you want to add the ability for the
## mute indicator to be disabled from preferences.
default persistent.show_mute_indicator = True

## If you want to do that then you should add this to the preferences screen, inside the first hbox.
## Check the indentation.

#                 vbox:
#                     style_prefix "radio"
#                     label _("Show mute indicator?")
#                     textbutton _("Yes") action SetVariable("persistent.show_mute_indicator", True)
#                     textbutton _("No") action SetVariable("persistent.show_mute_indicator", False)
                



init python:
    def toggle_mute():
        if preferences.get_mute("main"):
            ## This unmutes the game.
            renpy.run(Preference("all mute", "toggle")),
            renpy.restart_interaction()
            ## `renpy.restart_interaction` to ensure that the mute indicator is updated.
        else:
            ## This mutes the game.
            renpy.run(Preference("all mute", "toggle")),
            renpy.restart_interaction()
            ## `renpy.restart_interaction` to ensure that the mute indicator is updated.

    ## Append the 'M' key to the RenPy keymap, and call toggle_mute() when pressed.
    ## This can be changed to whatever key of your choosing.
    ##
    ## The key combination Shift+M would be `shift_K_m`
    ## Alt + M would be `alt_K_m`
    ## M is `K_m`
    ##
    ## See https://www.renpy.org/doc/html/keymap.html for all the keysms you can set it to.
    
    config.underlay.append(renpy.Keymap(K_m = toggle_mute))

    ## Tell RenPy to always show our indicator screen in game when the overlay has not been hidden.
    ## (Just like the quick menu)
    config.overlay_screens.append("mute_indicator")

    ## You might also want to add this new keybind to the list of keybinds in the help menu under
    ## `keyboard_help()` in screens.rpy
    ##
    ## On a default, unaltered screens.rpy, simply insert the following on screens.rpy at line 1050
    ## Keep an eye on the indentation.
    #    hbox:
    #        label "M"
    #        text _("Mutes the game.")
    ##


## Mute indicator.
## This shows a small little icon in the top left, when the game is muted.
## This only shows when in game, and not in the menus, but you can modify screens.rpy to show in
## menus (Which I recommend you do.)
## To do that insert the statement `use mute_indicator` inside the main_menu and game_menu screen.
screen mute_indicator():
    if persistent.show_mute_indicator:
        if preferences.get_mute("main"):
            ## Change the path below to the path to your icon.
            image "images/mute_icon.png":
                xalign 1.0
                yalign 0.0