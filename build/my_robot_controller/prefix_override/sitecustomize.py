import sys
if sys.prefix == '/home/chandrakant/miniconda3/envs/rosenv':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/chandrakant/ros2_wsck/install/my_robot_controller'
