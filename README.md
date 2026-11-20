This is a fun mini-game built using ROS2 and the turtlesim simulator, made as part of the Udemy ROS2 Level 1 course by Edouard Renard.
The idea is simple: you control one turtle (the default turtle1) using your keyboard, and your goal is to catch other turtles that randomly spawn on the screen.

Every couple of seconds, a new turtle spawns at a random position on the map. These turtles just sit there, waiting to be “caught.”
You move your turtle using the arrow keys and try to drive it close enough to touch another turtle.
Once your turtle gets close enough to a spawned turtle (within a small distance), that turtle automatically gets killed (removed) from the simulation, and a message is logged in the terminal confirming the catch.

This keeps happening in a loop — new turtles keep spawning, and you keep hunting them down, so it feels a bit like a simple chase/catch game.

Behind the scenes, this project demonstrates some core ROS2 concepts like nodes, topics, services, publishers/subscribers, and timers, which makes it a great beginner-friendly way to understand how ROS2 systems talk to each other.

How to Play

1. Make sure you have ROS2 and turtlesim installed on your system.
2. Create a new ros2 package and colcon build that package.
3. Inside the src folder create a new python file and paste this code.
4. Go to setup.py and in the console scripts add an executable of the file where you have written the souce code.
5. Then colcon build that package again in your terminal.
6. Open three separate terminals (and source your workspace in each, if needed).
7. In the first terminal, run the followign command:
     ros2 run turtlesim turtlesim_node
8. In the second terminal, run the follwowing command:
     ros2 run turtlesim turtle_teleop_key
10. In the third terminal, run the following command where replace the placeholders with your package and executable name which you wrote inside setup.py:
     ros2 run <your_package_name> <your_executable_name>
11. Then split your screen in one side put the newly created turtlesim screen and on the other your third terminal, now inside that third terminal use arrow keys to move your turtle.
12. Make the turtle close to newly spawned turtles and see the newly turtles getting despawning and new ones spawning.
13. See the video for the gameplay for better understanding. 

Gameplay:
https://github.com/user-attachments/assets/a201b7ed-e47b-429e-99dc-954077927d43



