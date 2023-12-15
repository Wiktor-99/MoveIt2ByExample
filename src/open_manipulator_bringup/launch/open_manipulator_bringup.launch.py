from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    open_manipulator_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory("open_manipulator_control"), "/launch/control.launch.py"]
        ))

    return LaunchDescription([open_manipulator_control])