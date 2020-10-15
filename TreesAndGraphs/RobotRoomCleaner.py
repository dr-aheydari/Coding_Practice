"""


"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):       
    
    def __init__(self):
        # make a set for containing all the visited cells... we use this as an obstacle
        self.visited_rooms = set();
        # here we have the set of directions in 2D 
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        self.Traverse(robot)
            
    def Traverse(self,robot,cell = (0, 0), d = 0):
        self.visited_rooms.add(cell)
        robot.clean()
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        for i in range(4):
            # getting the new direction
            new_d = (d + i) % 4
            new_cell = (cell[0] + self.directions[new_d][0], cell[1] + self.directions[new_d][1])

            if not new_cell in self.visited_rooms and robot.move():
                self.Traverse(robot, new_cell, new_d)
                self.MoveBack(robot)
            # turn the robot following chosen direction : clockwise
            robot.turnRight()
    
    # prioritize moving to the right
    def MoveBack(self, robot):
        robot.turnRight();
        robot.turnRight()
        robot.move();
        robot.turnRight();
        robot.turnRight();
