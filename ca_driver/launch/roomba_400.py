import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

import pathlib

def generate_launch_description():
    parameters_file = pathlib.Path(__file__).resolve().parent.parent / 'config' / 'default.yaml'

    return LaunchDescription([
        Node(node_name='ca_driver', package='ca_driver', node_executable='ca_driver', output='screen',
             parameters = [
                 parameters_file,
                 {
                     'robot_model' : 'ROOMBA_400'
                 }
             ])
    
        ])

