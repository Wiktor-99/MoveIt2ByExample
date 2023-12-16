from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    open_manipulator_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory("open_manipulator_control"), "/launch/control.launch.py"]
        ))
    open_manipulator_moveit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory("open_manipulator_moveit"), "/launch/move_group_with_rviz.launch"]
        ))

    return LaunchDescription([
        open_manipulator_control,
        open_manipulator_moveit])