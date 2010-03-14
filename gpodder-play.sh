#!/bin/bash
mpc clear
echo $1 | sed 's/\/home\/wieland\/Musik//g' | mpc add
mpc play
