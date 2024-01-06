from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    manipulator_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory("manipulator_6dof_control"), "/launch/control.launch.py"]
        ))
    manipulator_moveit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory("manipulator_6dof_moveit"), "/launch/move_group_with_rviz.launch.py"]
        ))

    return LaunchDescription([
        manipulator_control,
        manipulator_moveit])