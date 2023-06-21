# https://www.reddit.com/r/RenPy/comments/rtijpe/centering_a_renpy_input/
screen custom_input_modal(label_text, variable_name):
    style_prefix "custom_input_modal"
    modal True
    zorder 100
#    add Solid("#777777") alpha 0.8
    frame:
        has vbox:
            xalign 0.5
            spacing 20

        label label_text:
            text_color gui.hover_color
            xalign 0.5
        null height 2
        input size 40 color gui.hover_color default globals()[variable_name] value VariableInputValue(variable_name, returnable=True) length 25 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ":
            yalign 0.5
            xalign 0.5
            xysize (450, 30)
        textbutton _("Enter"):
            xalign 0.5
            action If(renpy.get_screen("statistics"), true=Hide("custom_input_modal"), false=Return())


style custom_input_modal_frame:
    padding gui.confirm_frame_borders.padding
    xsize 550
    xalign 0.5
    yalign 0.5
