#! /bin/bash

cd ~/catkin_ws/src/
git clone https://github.com/tom-howard/com2009_actions.git

cd com2009_actions/src/
chmod +x camera_sweep.py

cd ~/catkin_ws/
catkin_make