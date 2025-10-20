FROM osrf/ros:jazzy-desktop-full-noble
ARG ROS_DISTRO=jazzy
ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive
RUN userdel $(getent passwd 1000 | cut -d: -f1)
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip
RUN pip3 install --break-system-packages "numpy<2.0" ultralytics open3d
ENV DEBIAN_FRONTEND=dialog
ENV SHELL=/bin/bash


RUN rm /usr/share/glvnd/egl_vendor.d/50_mesa.json
RUN mkdir -p /usr/share/glvnd/egl_vendor.d/ && echo '\
{\
    "file_format_version" : "1.0.0",\
    "ICD" : {\
        "library_path" : "libEGL_nvidia.so.0"\
    }\
}' > /usr/share/glvnd/egl_vendor.d/10_nvidia.json

RUN apt-get update && \
    sudo apt-get install -y lsb-release wget gnupg

ENV DEBIAN_FRONTEND=noninteractive
RUN sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null && \
    apt-get update --fix-missing && \
    apt-get -y install \
    git-core \
    bash-completion \
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    ros-$ROS_DISTRO-cyclonedds \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-ros2-control \
    ros-$ROS_DISTRO-ament-cmake \
    ros-$ROS_DISTRO-ros2-control-cmake \
    ros-$ROS_DISTRO-ros2-controllers \
    ros-$ROS_DISTRO-moveit ros-$ROS_DISTRO-moveit-ros-perception \
    ros-$ROS_DISTRO-moveit-planners ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-rviz-common ros-$ROS_DISTRO-rviz-default-plugins \
    ros-$ROS_DISTRO-rviz-visual-tools ros-$ROS_DISTRO-rviz-rendering \
    ros-$ROS_DISTRO-moveit-planners-chomp \
    ros-$ROS_DISTRO-octomap-rviz-plugins \
    ros-$ROS_DISTRO-gripper-controllers \
    pre-commit \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog
ENV GZ_VERSION=harmonic
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    mkdir -p /ros2_deps_ws/src && \
    cd /ros2_deps_ws/src && \
    git clone https://github.com/gazebosim/ros_gz.git -b ${ROS_DISTRO} && \
    git clone --branch $ROS_DISTRO https://github.com/ros-controls/gz_ros2_control && \
    cd /ros2_deps_ws && \
    apt update && rosdep update && \
    rosdep install -r --from-paths src -i -y --rosdistro $ROS_DISTRO && \
    colcon build --merge-install --install-base /opt/ros/overlay_jazzy
ENV DEBIAN_FRONTEND=dialog

ENV LD_LIBRARY_PATH=/opt/ros/overlay_jazzy/lib/x86_64-linux-gnu:/opt/ros/overlay_jazzy/lib:$LD_LIBRARY_PATH
ENV AMENT_PREFIX_PATH=/opt/ros/overlay_jazzy:$AMENT_PREFIX_PATH

ARG WORKSPACE
RUN echo "source /opt/ros/jazzy/setup.bash && source /opt/ros/overlay_jazzy/setup.bash" >> /root/.bashrc
RUN echo "if [ -f /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash ]; then source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash; fi" >> /home/$USERNAME/.bashrc \
    && echo "if [ -f ${WORKSPACE}/install/setup.bash ]; then source ${WORKSPACE}/install/setup.bash; fi" >> /home/$USERNAME/.bashrc
