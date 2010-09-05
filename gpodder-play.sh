#!/bin/bash
MPD_MUSIC_DIR="/home/wieland/Musik"
mpc clear
echo $1 | sed "s|$MPD_MUSIC_DIR||g" | mpc add
mpc play
