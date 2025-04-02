THIS IS A BASIC BEGINEER LEVEL CODES TO LEARN THE ROS2 :
___________________________________________________________________________________________________________________
# ROS2_Level1 Repository

This repository contains ROS 2 packages and configurations that can be utilized on any system for robotic simulations and development.

## Prerequisites
Ensure that you have the following installed on your system:
- **Ubuntu 22.04** (recommended)
- **ROS 2 Humble**
- **Gazebo (Fortress or Garden, based on project needs)**
- **colcon** (ROS 2 build tool)
- **Git**

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/chandrakantpatel044/ROS2_Level1.git
   cd ROS2_Level1
   ```

2. Install dependencies:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   ```

3. Build the workspace:
   ```bash
   colcon build --symlink-install
   ```

4. Source the workspace:
   ```bash
   source install/setup.bash
   ```

## Running the System

### Running a Node
To run an individual ROS 2 node:
```bash
ros2 run <package_name> <node_executable>
examples:
>> ros2 run turtlesim turtle_node #terminal 1
>> ros2 run my_robot_controller draw_circle
```
![image](https://github.com/user-attachments/assets/78802013-d562-4e39-93b8-fe6beda6b6a6)


## Contribution
If you want to contribute to this repository:
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push and create a Pull Request (PR)

## Issues
If you encounter any issues, feel free to open an issue in the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

