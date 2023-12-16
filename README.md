# MoveIt2ByExample

This repository is an example of the basic setup of MoveIt2 for a custom manipulator. This project shows an example of integrating an existing robot with MoveIt. The configuration contains:
* Robot description
* Simulation in Gazebo
* ROS2 control setup
* MoveIt setup that launches move_group and Rviz2
* Mimic joints setup

## Launching Example

To launch the example, you need to open the repository in VSCode using Dev Container. After setting up the container, you only need to run the commands below.

```bash
./build.sh &&
source install/setup.bash &&
ros2 launch open_manipulator_simulation open_manipulator_simulation_bringup.launch.py
```

To plan a path for the open manipulator in rviz, you need to check the **Allow Approximate IK Solutions** checkbox, as MoveIt does not support IK for manipulators with less than 6 DoF.

### Remarks
When integrating a manipulator with MoveIt, you should be aware of the following:

#### MoveIt supports IK by default only for manipulators with 6 DoF (or more)
If you want to use it with a manipulator with less than 6 DoF, you need to use **Allow Approximate IK Solutions** or create your own IK plugin, e.g., using IK fast.

#### ROS2 control configuration
The names of controllers configured for MoveIt should match the names of your controllers configured for the ROS2 control package.

#### Using mimic joints
This one could be tricky; there is an issue when mimic joints are used in simulation. ROS2 control gazebo plugin creates an extra interface with the **_mimic** suffix. This leads to errors in the move_group node. To fix this issue, you need to add the following lines to your URDF for your mimic joint (below is an example for open_manipulator).

```xml
  <link name="gripper_sub_mimic_link"/>
  <joint name="gripper_sub_mimic" type="fixed">
    <origin xyz="0 0 0" rpy="0 0 0"/>
    <parent link="world"/>
    <child link="gripper_sub_mimic_link"/>
  </joint>
```

#### Fixed joint in center of your end effector
If you want to have an interactive marker in the center of your end effector, you need to add an extra link and joint that will connect the last joint and the center of the end effector. This joint needs to be added to the planning group and set as the end_effector in the **srdf file**. Here's an example modification of the URDF file (for open_manipulator):
```xml
  <link name="end_efector_link" />
  <joint name="end_efector" type="fixed">
    <parent link="link5"/>
    <child link="end_efector_link"/>
    <origin xyz="0.1 0.0 0.0" rpy="0 0 0"/>
  </joint>
```
And corresponding setup in the **srdf file**:
```xml
<end_effector name="end_efector" parent_link="end_efector_link" group="open_manipulator" parent_group="open_manipulator"/>

```
