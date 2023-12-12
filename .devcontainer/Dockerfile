ARG ROS_DISTRO=humble
FROM althack/ros2:$ROS_DISTRO-gazebo

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update --fix-missing \
    && apt-get -y install --no-install-recommends \
    ros-$ROS_DISTRO-xacro ros-$ROS_DISTRO-ros2-control \
    ros-$ROS_DISTRO-gazebo-ros2-control \
    ros-$ROS_DISTRO-ros2-controllers ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    ros-$ROS_DISTRO-moveit ros-$ROS_DISTRO-moveit-ros-perception \
    ros-$ROS_DISTRO-moveit-planners ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-rviz-common ros-$ROS_DISTRO-rviz-default-plugins \
    ros-$ROS_DISTRO-rviz-visual-tools ros-$ROS_DISTRO-rviz-rendering \
    ros-$ROS_DISTRO-octomap-rviz-plugins \
    ros-$ROS_DISTRO-gripper-controllers\
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set up auto-source of workspace for ros user
ARG WORKSPACE
RUN echo "if [ -f ${WORKSPACE}/install/setup.bash ]; then source ${WORKSPACE}/install/setup.bash; fi" >> /home/ros/.bashrc
