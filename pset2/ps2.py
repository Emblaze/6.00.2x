# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import matplotlib.pyplot as pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.11:
from ps2_verify_movement311 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.11

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        # Initialising a default tiles dict, with tuples representing the origin coordinates of each tile as keys and a default value for cleaned set to False
        self.tiles = {(x,y): bool() for x in range(width) for y in range(height)}

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.x = pos.getX()
        self.y = pos.getY()
        self.tiles[(int(self.x), int(self.y))] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m,n)] == True

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return sum(1 for value in self.tiles.values() if value == True)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.random() * self.width
        y = random.random() * self.height
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        #print("Debug:", str(position), position.getX(), position.getY(), type(position))
        #self.position = position.getX(), position.getY()
        self.position = str(position)

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = str(direction)

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Get a new position with the same direction
        self.next_position = self.position.getNewPosition(angle=self.direction, speed=1.0)
        # Check if next position would be in the room
        valid_next_position = bool(self.room.isPositionInRoom(self.next_position))
        if valid_next_position == False:
            # Get a new direction
            self.direction = random.randint(0, 359)
            # Recheck if new position is in the room
            valid_next_position
        else:
            # Next position is in the room, let's move to it
            self.position = self.next_position
        # Clean tile at new position
        self.room.cleanTileAtPosition(self.position)
            

# Uncomment this line to see your implementation of StandardRobot in action!
testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or RandomWalkRobot)
    """
    # Run 1 simulation
    def runOneSimulation():
      # Create an instance of a room  
      room = RectangularRoom(width, height)
      # Create an instance of a robot of robot_type with initial random position and direction
      robot = robot_type(room, room.getRandomPosition())
      # Get these initials values
      robot.getRobotPosition()
      robot.getRobotDirection()

    num_robots = num_robots
    
    0 <= min_coverage <= 1.0
    num_trials = num_trials
    robot_type = StandardRobot
    

# Build-Debug
random.seed(0)
# whiteRoom = RectangularRoom(5, 5)
# cleanedTiles = [tile for tile,state in whiteRoom.tiles.items() if state == True]
# print("Room is an instance of RectangularRoom:", isinstance(whiteRoom, RectangularRoom), end = ". ")
# print("# of tiles:", f"{whiteRoom.getNumTiles()}", end = ". ")
# print("Clean tiles:", whiteRoom.getNumCleanedTiles())
# Walter = Robot(whiteRoom, whiteRoom.getRandomPosition())
# print("Robot is an instance of Robot:", isinstance(Walter, Robot), end = ". ")
# print("Initial position:", f"{Walter.getRobotPosition()}", "| Heading:", f"{Walter.getRobotDirection()}" + '°', end = ". ")
# print("# of clean tiles:", whiteRoom.getNumCleanedTiles())
# position = whiteRoom.getRandomPosition()
# print(f"{position}", "is an instance of Position:", isinstance(position, Position), vars(position))
# Walter.setRobotPosition(position)
# direction = random.randint(0, 359)
# Walter.setRobotDirection(direction)
# print("Position now set to", Walter.getRobotPosition(), "| Heading:", f"{Walter.getRobotDirection()}" + '°', end = ". ")
# print("Tile is clean:", whiteRoom.isTileCleaned(int(position.x), int(position.y)))
# whiteRoom.cleanTileAtPosition(position)
# print("Tile", f"{position}", "is clean:", whiteRoom.isTileCleaned(int(position.x), int(position.y)))
# cleanedTiles = [tile for tile,state in whiteRoom.tiles.items() if state == True]
# print("Clean tiles:", whiteRoom.getNumCleanedTiles(), cleanedTiles)
# position =  position.getNewPosition(direction, 1)
# print("Position:", f"{position}", "is in the room:", whiteRoom.isPositionInRoom(position))
# print("Position variables:", vars(position))
# print(vars(Walter))
# print(vars(whiteRoom))

# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # self.position = self.room.getRandomPosition() # This should be implemented in the RandomWalkRobot
        raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
