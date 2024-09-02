from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'UAV_model',
            default_value='./src/livox_laser_simulation/models/Livox_mid360/model.sdf',
            description='Path to the UAV model file'
        ),
        DeclareLaunchArgument('x', default_value='0', description='Initial x position'),
        DeclareLaunchArgument('y', default_value='0', description='Initial y position'),
        DeclareLaunchArgument('z', default_value='0', description='Initial z position'),
        DeclareLaunchArgument(
            'world',
            default_value='./src/livox_laser_simulation/worlds/test_pattern.world',
            description='World file for simulation'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource('/opt/ros/humble/share/gazebo_ros/launch/gazebo.launch.py'),
            launch_arguments={
                'world_name': LaunchConfiguration('world'),
                'paused': 'false',
                'use_sim_time': 'true',
                'gui': 'true',
                'headless': 'false',
                'debug': 'false',
                'verbose': 'true',
            }.items(),
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_model',
            output='screen',
            arguments=[
                '-file', LaunchConfiguration('UAV_model'),
                '-x', LaunchConfiguration('x'),
                '-y', LaunchConfiguration('y'),
                '-z', LaunchConfiguration('z'),
                '-entity', 'iris_demo'
            ],
        ),
    ])
