import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    xacro_file = os.path.join(
        get_package_share_directory('open_manipulator_description'), 'urdf',
                              'open_manipulator_robot.xacro')

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': xacro.process_file(xacro_file).toxml()}],
        emulate_tty=True
    )

    return LaunchDescription([robot_state_publisher])
