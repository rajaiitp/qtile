#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

run picom &
run redshift &
run dunst &
run nm-applet &
/usr/libexec/xfce-polkit &
run seapplet &
xset s off -dpms &
/usr/libexec/geoclue-2.0/demos/agent &
# xset s 300 &
xss-lock -n /usr/lib/xsecurelock/dimmer -l -- xsecurelock &


# xss-lock --transfer-sleep-lock -- i3lock -i /usr/share/backgrounds/arcolinux-dual/wall.png --nofork  &
# run clipit -n &
# picom --config /etc/xdg/picom.conf &
# xsetroot -cursor_name left_ptr &
# numlockx on &
# run nm-tray &
# $HOME/.screenlayout/laptop.sh&
# blueberry-tray &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# /usr/bin/snap userd --autostart
# imsettings-switch -n -q -x
# dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
# systemctl --user stop xdg-desktop-portal&
# trayer --align right --widthtype request --height 20 --margin 400  --expand true --transparent true --edge top  --tint 0x000000 --alpha 0 --iconspacing 25  --padding 15 &
# nitrogen --restore &
