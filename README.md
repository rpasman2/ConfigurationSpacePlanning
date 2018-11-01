#ConFiguration Space Planning
Transforms a 2D planning problem for a robotic arm into a configuration space, and then searches for a path in that space

Problem Statement:
Given a two-link arm in 2D space. This arm has two links of length L1 and L2 respectively. The arm is free to rotate 
about its base that is pivoted on the ground and link-2 can rotate about the joint where it connects with link-1. 
We use α for the angle between the link-1 and the ground (equivalent to θ1). We use β for the angle between link-2 and 
link-1 (equivalent to θ2). Note that the angles are measured counter-clockwise.

For each planning problem, the given information is:
The starting angles for the robotic arm.
The location (x,y) and radius r of a circular goal.
The locations (x,y) and radius r of various circular obstacles.

The objective is to find a shortest path for the robotic arm from its starting position to the goal so that the open tip of the arm touches or is inside the goal.

I do my path planning in two steps:
1. Compute a configuration space map (Maze) that shows which joint angles are blocked by obstacles or by the window.
2. Use search algorithms to compute a shortest path in this configuration space map.
