import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    xacro_file = os.path.join(
        get_package_share_directory('manipulator_6dof_description'), 'urdf',
                              'manipulator_6dof_description.xacro')

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': xacro.process_file(xacro_file).toxml()}],
        emulate_tty=True
    )
    start_joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui')

    return LaunchDescription([robot_state_publisher, start_joint_state_publisher_gui_node])