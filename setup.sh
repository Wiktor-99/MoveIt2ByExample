#!/bin/bash
set -e

source /opt/ros/iron/setup.bash
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -y
