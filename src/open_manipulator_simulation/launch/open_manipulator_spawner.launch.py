from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'open_manipulator', '-topic', 'robot_description'],
        output='screen',
        emulate_tty=True)])
