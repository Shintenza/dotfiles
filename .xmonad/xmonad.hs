-- IMPORTS
import XMonad
import Data.Monoid
import System.Exit

import XMonad.Layout.LayoutModifier
import XMonad.Layout.Renamed
import XMonad.Layout.Spacing
import XMonad.Layout.LimitWindows (limitWindows, increaseLimit, decreaseLimit)
import XMonad.Layout.NoBorders
import XMonad.Layout.ResizableTile
import XMonad.Layout.Fullscreen as F


import Graphics.X11.ExtraTypes.XF86

import XMonad.Hooks.DynamicLog 
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.ManageHelpers


import qualified XMonad.StackSet as W
import qualified Data.Map        as M

import XMonad.Util.SpawnOnce
import XMonad.Util.EZConfig (additionalKeysP)

import XMonad.Actions.CycleWS

-- VARS
myTerminal = "alacritty"

myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

myClickJustFocuses :: Bool
myClickJustFocuses = False

myBorderWidth   = 2

myModMask       = mod4Mask

myWorkspaces    = ["\59285","\63288","ﭮ","\64271","\61884","\63507"]

myNormalBorderColor  = "#161616"
myFocusedBorderColor = "#026edb"

------------------------------------------------------------------------
-- Key bindings. Add, modify or remove key bindings here.

myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    [ ((modm,               xK_Return), spawn $ XMonad.terminal conf)
    , ((modm,               xK_d     ), spawn "dmenu_run -h 25 -p 'Run:' -f")
    , ((modm,               xK_q     ), kill)
    , ((modm,               xK_space ), sendMessage NextLayout)
    , ((modm .|. shiftMask, xK_space ), setLayout $ XMonad.layoutHook conf)

    , ((modm,               xK_n     ), refresh)
    , ((modm,               xK_Tab),     toggleWS)
    , ((modm,               xK_j     ), windows W.focusDown)
    , ((modm,               xK_k     ), windows W.focusUp  )
    , ((modm,               xK_m     ), windows W.focusMaster  )
    , ((modm .|. shiftMask, xK_Return), windows W.swapMaster)
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown  )
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp    )
    , ((modm,               xK_h     ), sendMessage Shrink)
    , ((modm,               xK_l     ), sendMessage Expand)
    , ((modm,               xK_t     ), withFocused $ windows . W.sink)

    -- Increment the number of windows in the master area
    , ((modm              , xK_comma ), sendMessage (IncMasterN 1))
    -- Deincrement the number of windows in the master area
    , ((modm              , xK_period), sendMessage (IncMasterN (-1)))

    , ((modm .|. shiftMask, xK_q     ), io (exitWith ExitSuccess))
    , ((modm .|. shiftMask, xK_x     ), spawn "xmonad --recompile; xmonad --restart")

    -- My programs
    , ((modm .|. shiftMask, xK_b     ), spawn "brave")
    , ((modm .|. shiftMask, xK_s     ), spawn "spotify")
    , ((modm .|. shiftMask, xK_d     ), spawn "discord")
    , ((modm .|. shiftMask, xK_v     ), spawn "code")
    , ((modm .|. shiftMask, xK_f     ), spawn "alacritty -e ranger")
    , ((modm .|. shiftMask, xK_t     ), spawn "thunar")
    , ((modm .|. shiftMask, xK_t     ), spawn "thunar")
    , ((modm .|. shiftMask, xK_Print ), spawn "io.elementary.screenshot-tool")
    , ((modm,               xK_Print ), spawn "scrot ~/Pictures/screenshot-$(date +%F_%T).png")

    -- Multimedia keys
    , ((0, xF86XK_AudioLowerVolume   ), spawn "pactl set-sink-volume @DEFAULT_SINK@ -10%")
    , ((0, xF86XK_AudioRaiseVolume   ), spawn "pactl set-sink-volume @DEFAULT_SINK@ +10%")
    , ((0, xF86XK_AudioMute   ),        spawn "pactl set-sink-mute @DEFAULT_SINK@ toggle")
    , ((0, xF86XK_MonBrightnessDown  ), spawn "xbacklight -dec 10")
    , ((0, xF86XK_MonBrightnessUp  ),   spawn "xbacklight -inc 10")
    , ((0, xF86XK_AudioPlay  ),         spawn "playerctl play-pause")
    , ((0, xF86XK_AudioNext  ),         spawn "playerctl next")
    , ((0, xF86XK_AudioPrev  ),         spawn "playerctl prev")
    ]
    ++

    --
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
        , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    ++

    --
    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    --
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]


------------------------------------------------------------------------
-- Mouse bindings: default actions bound to mouse events
--
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))
    ]

------------------------------------------------------------------------
-- Layouts:

mySpacing :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
mySpacing i = spacingRaw False (Border i i i i) True (Border i i i i) True

tall = renamed [Replace "tall"]
    $ mySpacing 5
    $ ResizableTall 1 (3/100) (1/2) []

monocle = renamed [Replace "monocle"]
    $ limitWindows 5 Full

myLayout = smartBorders $ avoidStruts $ myDefaultLayout
  where
        myDefaultLayout = tall |||
            monocle |||
            noBorders Full

------------------------------------------------------------------------
-- Window rules:

myManageHook = composeAll
    [ className =? "MPlayer"        --> doFloat
    , className =? "Brave-browser"  --> doShift ( myWorkspaces !! 1 )
    , className =? "discord"        --> doShift ( myWorkspaces !! 2 )
    , className =? "code-oss"       --> doShift ( myWorkspaces !! 3 )
    , className =? "Spotify"        --> doShift ( myWorkspaces !! 4 )
    , className =? "Gimp"           --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore 
    , isDialog --> doCenterFloat
    ]

------------------------------------------------------------------------
-- Event handling

-- * EwmhDesktops users should change this to ewmhDesktopsEventHook
--
-- Defines a custom handler function for X Events. The function should
-- return (All True) if the default handler is to be run afterwards. To
-- combine event hooks use mappend or mconcat from Data.Monoid.
--
myEventHook = mempty

------------------------------------------------------------------------
-- Status bars and logging

-- Perform an arbitrary action on each internal state change or X event.
-- See the 'XMonad.Hooks.DynamicLog' extension for examples.
--
-- myLogHook = return ()

------------------------------------------------------------------------
-- Startup hook

-- Perform an arbitrary action each time xmonad starts or is restarted
-- with mod-q.  Used by, e.g., XMonad.Layout.PerWorkspace to initialize
-- per-workspace layout choices.
--
-- By default, do nothing.
myStartupHook = do
    spawnOnce "bash .config/polybar/launch.sh"
    spawnOnce "setxkbmap pl &"
    spawnOnce "feh --bg-fill ~/Pictures/wallpaper.png &"
    spawnOnce "picom &"
    spawnOnce "redshift -l 50.60705:22.10381 & "
    spawnOnce "/usr/bin/lxpolkit &"
------------------------------------------------------------------------
-- Now run xmonad with all the defaults we set up.

-- Run xmonad with the settings you specify. No need to modify this.
--
main = xmonad $ ewmh $docks $ fullscreenSupport defaults

-- A structure containing your configuration settings, overriding
-- fields in the default config. Any you don't override, will
-- use the defaults defined in xmonad/XMonad/Config.hs
--
-- No need to modify this.
--
defaults = def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = myLayout,
        manageHook         = myManageHook <+> manageDocks <+> F.fullscreenManageHook,
        handleEventHook    = myEventHook <+> F.fullscreenEventHook,
        logHook            = ewmhDesktopsLogHook,
        startupHook        = myStartupHook
}



