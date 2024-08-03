#!/bin/bash
set -e

./setup.sh
export AMENT_CPPCHECK_ALLOW_SLOW_VERSIONS=true
source /opt/ros/iron/setup.bash
ament_${LINTER} src/
