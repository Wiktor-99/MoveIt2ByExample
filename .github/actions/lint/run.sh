#!/bin/bash
set -e

./setup.sh
source /opt/ros/iron/setup.bash
ament_${LINTER} src/
