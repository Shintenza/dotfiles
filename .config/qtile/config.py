# -*- coding: utf-8 -*-


##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401


##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
# The Qtile config file location
myConfig = "/home/kamil/.config/qtile/config.py"

##### KEYBINDINGS #####
keys = [
    # Audio
    Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),


    # Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([], "XF86ScreenSaver", lazy.spawn("./.scripts/darklight")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([mod], "d", lazy.spawn("./.scripts/menu")),


    # The essentials
    Key([mod], "Print", lazy.spawn("spectacle")),
    Key(
        [mod], "Return",
        lazy.spawn(myTerm+" -e zsh"),
        desc='Launches My Terminal With zsh Shell'
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Dmenu Run Launcher'
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod, "shift"], "q",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key(
        [mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "shift"], "t",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),
    # Window controls
    Key(
        [mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key(
        [mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),
    Key(
        [mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key(
        [mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key(
        [mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),
    # Stack controls
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key(
        [mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),

    # My applications launched with SUPER + SHIFT + KEY
    Key([mod, "shift"], "b", lazy.spawn("brave")),
    Key([mod, "shift"], "d", lazy.spawn("discord")),
    Key([mod, "shift"], "v", lazy.spawn("code")),

]

##### GROUPS #####
group_names = [("", {'layout': 'monadtall'}),
               ("爵", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("﬏", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'})]

groups = [
    Group(""),
    Group("爵", matches=[Match(wm_class=["Brave-browser"])]),
    Group("", matches=[Match(wm_class=["discord"])]),
    Group("﬏", matches=[Match(wm_class=["Code"])]),
    Group(""),
]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 1,
                "margin": 5,
                "border_focus": "#ff0000",
                "border_normal": "#050505"
                }

##### THE LAYOUTS #####
layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND"],
    #      section_fontsize = 11,
    #      bg_color = "141414",
    #      active_bg = "90C435",
    #      active_fg = "000000",
    #      inactive_bg = "384323",
    #      inactive_fg = "a0a0a0",
    #      padding_y = 5,
    #      section_top = 10,
    #      panel_width = 320
    #      ),
    # layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [
    ["#0d0d0d"],  # background
    ["#ffffff"],  # foreground
    ["#919191"],  # inactive
    ["#1c1c1c"],  # highlight color
    ["#ff5555"],
    ["#d43939"],
    ["#668bd7"],
    ["#e1acff"]
]

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


##### MOUSE CALLBACKS #####

def open_menu(qtile):
    qtile.cmd_spawn("./.scripts/menu")


def open_smenu(qtile):
    qtile.cmd_spawn("./.scripts/sysmenu")

##### WIDGETS #####


widget_defaults = dict(
    font="Hack",
    fontsize=10,
    padding=2,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()
arrowSize = 30
arrowPadding = -9
arrowLeft = ""

# Arrows colors
arrowColors = [
    ["#000000"],
    ["#121212"],
    ["#171717"],
    ["#222222"],
    ["#272727"],
    ["#323232"],
    ["#373737"],
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',
                    background=arrowColors[1],
                    foreground=colors[1],
                    padding=5,
                    fontsize=14,
                    mouse_callbacks={"Button1": open_menu},
                ),
                widget.TextBox(
                    text="",
                    foreground=arrowColors[1],
                    background=arrowColors[5],
                    fontsize=29,
                    padding=arrowPadding,
                ),
                widget.TextBox(
                    background=arrowColors[5],
                    foreground=colors[1],
                    text="",
                    padding=5,
                    fontsize=14,
                    mouse_callbacks={"Button1": open_smenu},
                ),
                widget.TextBox(
                    text="",
                    foreground=arrowColors[5],
                    fontsize=29,
                    padding=arrowPadding,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=colors[0],
                ),
                widget.GroupBox(
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[1],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[3],
                    highlight_method="line",
                    this_current_screen_border=colors[1],
                    this_screen_border=colors[1],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[1],
                    background=colors[0]
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors[0],
                    background=colors[0],
                ),
                widget.Systray(
                    padding=3,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=30,
                    foreground=colors[0],
                    background=colors[0],
                ),
                widget.WindowName(
                    fontsize=1,
                    foreground=colors[0],
                    background=colors[0],
                ),
                widget.TextBox(
                    text=arrowLeft,
                    #background = "031926",
                    foreground=arrowColors[6],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    foreground=colors[1],
                    background=arrowColors[6],
                    padding=1,
                    fontsize=13,
                    text="",
                ),
                widget.Battery(
                    foreground=colors[1],
                    background=arrowColors[6],
                    format="{percent:2.0%}",
                    padding=5,
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[6],
                    foreground=arrowColors[5],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    foreground=colors[1],
                    background=arrowColors[5],
                    fontsize=14
                ),
                widget.ThermalSensor(
                    foreground=colors[1],
                    background=arrowColors[5],
                    threshold=90,
                    padding=5
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[5],
                    foreground=arrowColors[4],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    foreground=colors[1],
                    background=arrowColors[4],
                    fontsize=14
                ),
                widget.CPU(
                    foreground=colors[1],
                    background=arrowColors[4],
                    padding=5,
                    format="{load_percent}%"
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[4],
                    foreground=arrowColors[3],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    foreground=colors[1],
                    background=arrowColors[3],
                    fontsize=15

                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    foreground=colors[1],
                    background=arrowColors[3],
                    padding=5
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[3],
                    foreground=arrowColors[2],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[1],
                    background=arrowColors[2],
                    padding=0,
                    fontsize=15,
                ),
                widget.PulseVolume(
                    foreground=colors[1],
                    background=arrowColors[2],
                    padding=5
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[2],
                    foreground=arrowColors[1],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors[0],
                    background=arrowColors[1],
                    padding=0,
                    scale=0.7
                ),
                widget.CurrentLayout(
                    foreground=colors[1],
                    background=arrowColors[1],
                    padding=5,
                ),
                widget.TextBox(
                    text=arrowLeft,
                    background=arrowColors[1],
                    foreground=arrowColors[0],
                    padding=arrowPadding,
                    fontsize=arrowSize,
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[1],
                    background=arrowColors[0],
                    padding=0,
                    fontsize=15,
                ),
                widget.Clock(
                    foreground=colors[1],
                    background=arrowColors[0],
                    format="%d %B %H:%M"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors[0],
                    background=arrowColors[0],
                ),
            ],
            size=19,
        ),
    ),
]

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'GtkFileChooserDialog'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wname': 'Discord Updater'},
    {'wmclass': 'winecfg.exe'},
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


# Steam floating rules
@hook.subscribe.client_new
def float_steam(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("Steam", "Steam")
        and (
            w_name != "Steam"
            or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
        )
    ):
        window.floating = True

##### STARTUP APPLICATIONS #####


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
