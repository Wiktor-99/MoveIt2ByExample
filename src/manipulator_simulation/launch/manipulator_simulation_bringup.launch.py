import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_open_manipulator = DeclareLaunchArgument(
        "use_open_manipulator",
        default_value="False",
        description="Launch simulation with open manipulator.",
    )

    use_6dof_manipulator = DeclareLaunchArgument(
        "use_6dof_manipulator",
        default_value="False",
        description="Launch simulation with custom 6DoF manipulator.",
    )

    open_manipulator_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory("open_manipulator_bringup"),
                "/launch/open_manipulator_bringup.launch.py",
            ]
        ),
        condition=IfCondition(LaunchConfiguration("use_open_manipulator")),
    )
    manipulator_6dof_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory("manipulator_6dof_bringup"),
                "/launch/manipulator_6dof_bringup.launch.py",
            ]
        ),
        condition=IfCondition(LaunchConfiguration("use_6dof_manipulator")),
    )

    world_argument = DeclareLaunchArgument(
        "world",
        default_value=os.path.join(
            get_package_share_directory("manipulator_simulation"), "worlds", "default_world.sdf"
        ),
        description="Robot controller to start.",
    )

    gazebo = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("ros_gz_sim"), "launch", "gz_sim.launch.py"),
        launch_arguments=[("gz_args", ["-r -v 4 ", LaunchConfiguration("world")])],
    )

    ign_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="gz_bridge",
        arguments=[
            "/clock" + "@rosgraph_msgs/msg/Clock" + "[ignition.msgs.Clock",
            "/conveyor/cmd_vel" + "@std_msgs/msg/Float64" + "]gz.msgs.Double",
        ],
        output="screen",
    )

    gazebo_spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        name="spawn_manipulator",
        arguments=["-name", "manipulator", "-topic", "robot_description"],
        output="screen",
    )

    return LaunchDescription(
        [
            use_open_manipulator,
            use_6dof_manipulator,
            world_argument,
            gazebo,
            ign_bridge,
            gazebo_spawn_robot,
            open_manipulator_bringup,
            manipulator_6dof_bringup,
        ]
    )
