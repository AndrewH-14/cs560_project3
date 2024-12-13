# CS 560 Project 3

## Execution Instructions

To run the the `webots_ros2_project3_python` controller and few steps must be taken which are detailed below.

### Step 1: Build the package
```
cd cs560_project3/
colcon build
```

### Step 2: Launch the environment
```
source install/setup.bash
ros2 launch webots_ros2_project3_python f23_robotics_1_launch.py
```

### Step 3: Run the controller
```
ros2 launch webots_ros2_project3_python f23_robotics_1_launch.py
```

### Step 4 (Optional): Run the cartographer
```
ros2 launch turtlebot3_cartographer cartographer.launch.py
```

## Test Runs

Additional information regarding the test rusn can be located in the `map_runs/small_maze` and `maps_runs/large_maze` `README.md` files.
