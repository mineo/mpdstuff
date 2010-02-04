#!/bin/bash
mpc clear
echo $1 | sed 's/\/media\/pinky\/Musik\///g' | mpc add
mpc play
