#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
# systemctl --user stop xdg-desktop-portal&
# trayer --align right --widthtype request --height 20 --margin 400  --expand true --transparent true --edge top  --tint 0x000000 --alpha 0 --iconspacing 25  --padding 15 &

nitrogen --restore &
run clipit -n &
run redshift &
run dunst &
/usr/libexec/xfce-polkit &
run nm-applet &

# picom --config /etc/xdg/picom.conf &
# xsetroot -cursor_name left_ptr &
# xset s off -dpms &
# numlockx on &
# run nm-tray &
# $HOME/.screenlayout/laptop.sh&
# blueberry-tray &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
