# Robotic AGV 

The modelling of the robot has been done using solidworks. The model consists of a chassis to which four motors with quadrature encoders have been attached. Mecanum wheels have been used to provide Omni-directional movement, a BeagleBone Blue is placed on the chassis, and the LIDAR is mounted on the top.

The URDF (Universal Robot Description Format) model is a collection of ﬁles that describe a robots physical description to ROS. These ﬁles are used by ROS to tell the computer what the robot actually looks like in real life. URDF ﬁles are needed in order for ROS to understand and be able to simulate situations with the robot before a researcher or engineer actually acquires the robot. It is the standard ROS XML representation of the robot model.Here individual parts have been designed and assembled as a whole, and once the model is ready a SW2URDF addin was installed for exporting the model to a URDF ﬁle (Uniﬁed Robot Description Format), this ﬁle is used to perform simulation in ROS.

Here is the guide to run the SLAM Simulation on ROS 

1. **roslaunch mybot_gazebo mybot_world.launch**  
    The Gazebo world opens 
