# Robotic AGV 

The modelling of the robot has been done using solidworks. The model consists of a chassis to which four motors with quadrature encoders have been attached. **Mecanum wheels have been used to provide Omni-directional movement**, a BeagleBone Blue is placed on the chassis, and the LIDAR is mounted on the top.

The URDF (Universal Robot Description Format) model is a collection of ﬁles that describe a robots physical description to ROS. These ﬁles are used by ROS to tell the computer what the robot actually looks like in real life. URDF ﬁles are needed in order for ROS to understand and be able to simulate situations with the robot before a researcher or engineer actually acquires the robot. It is the standard ROS XML representation of the robot model.Here individual parts have been designed and assembled as a whole, and once the model is ready a SW2URDF addin was installed for exporting the model to a URDF ﬁle (Uniﬁed Robot Description Format), this ﬁle is used to perform simulation in ROS.

Here is the guide to run the SLAM Simulation of the Robotic AGV  on ROS 

1. **roslaunch mybot_gazebo final6_world.launch**  
    The Gazebo world opens 
2. **roslaunch mybot_navigation final6_gmapping_demo.launch**
    Launch Gmapping SLAM
3. **roslaunch mybot_description final6_rviz_gmapping.launch**
    Launch RVIZ and obtain Laser scan data and map in Rviz

4. **roslaunch mybot_navigation simple_tele_top.launch**
        launch teletop and move the robot through the world and generate the complete map 
        
5. **rosrun map_server map_saver -f ~/{ws_name}/src/mybot_navigation/{add_remanaing_path}**
  Save the map using the above command 

The locomotion of the Robot can be controlled remotely using mobile phone using bletooth refer to the Robotic AGV.pdf for the details.
    
