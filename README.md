# Optitrack to gazebo 

This package track a posetamped topic and update a associated rigidbody position in the gazebo simulation.

**Table of Contents**
---------------------

1. [Installation](#Installation)

2. [Usage](#Usage)

<a name="Installation"></a>
## Installation

Preparation of the workspace with ***optitrack_to_gazebo*** :

    mkdir -p ~/optitrack_to_gazebo_ws/src
    cd ~/optitrack_to_gazebo_ws/src
    git clone http://192.168.1.101/infrastructure/optitrack_to_gazebo
    cd ~/optitrack_to_gazebo_ws
    catkin build


 <a name="Usage"></a>
## Usage

Launch a gazebo simulation with one rigidbody in it. Source  the ***optitrack_to_gazebo*** package:

    cd ~/optitrack_to_gazebo_ws
    source devel/setup.bash
    roslaunch optitrack_to_gazebo basic.launch

Before launching that, you will to specify extrinsec rigidbody translation calibration (from mocap marker to the rigidbody translation) inside the ***params/basic_param.yaml***. 
Then in ***basic.launch*** file change:

    <node pkg="optitrack_to_gazebo" type="optitrack_to_gazebo_node.py" name="optitrack_to_gazebo" >
        <param name="rigidbody_name" value="***YOUR_RIGIDBODY_NAME***" type="str"/>
    <remap from="pose_stamped" to="***THE_POSESTAMPED_MOCAP_TOPIC***"/>
    <rosparam file="$(arg param_file)" command="load"/>
    </node>

On top of that, the ***follower*** rigidbody must be change to your mocap rigidbody (in mocap) in the launch file and gazebo should be launch beforehand:

    roslaunch gazebo_ros empty_world.launch



