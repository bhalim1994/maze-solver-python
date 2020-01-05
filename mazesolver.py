import queue

# First maze
def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "X", "#", "#", "#", "#"])
    return maze

# Second maze
def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "X", "#", "#", "#", "#", "#", "#", "#"])
    return maze


def printMaze(maze, path=""):
    # Loops over the maze and enumerates through them, starting at index 0.
    for x, pos in enumerate(maze[0]):  # x is the index, pos is the value.
        # Finds O for pos.
        if pos == "O":
            # Set index to start position.
            start = x

    # j is column position.
    j = start
    # i is row position.
    i = 0

    # Let pos now be a new empty set object.
    pos = set()
    for move in path:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

        # Add movement to position.
        pos.add((i, j))

    # For row position and value, enumerate over maze.
    for i, row in enumerate(maze):
        #For column position and value, enumerate over the rows.
        for j, col in enumerate(row):
            # If current pos, set to "+ ".
            if (i, j) in pos:
                print("+ ", end="")
            # If not current pos, leave as is.
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    # for x (index) and pos (value), enumerate over maze starting at index 0.
    for x, pos in enumerate(maze[0]):
        # Finds O for pos.
        if pos == "O":
            # Set index to start position.
            start = x

    # j is column position.
    j = start
    # i is row position.
    i = 0

    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

        # If the column or row position is NOT more than or equal to 0 and less than the column or row position, it is in an invalid position.
        if not(0 <= i < len(maze) and 0 <= j < len(maze[0])):
            return False
        # If the position has a "#", it is in an invalid position.
        elif (maze[i][j] == "#"):
            return False
    # Otherwise, return true for valid position.
    return True


def findEnd(maze, moves):
    # for x (index) and pos (value), enumerate over maze starting at index 0.
    for x, pos in enumerate(maze[0]):
        # Finds 0 for pos.
        if pos == "O":
            # Set index to start position.
            start = x

    # j is column position.
    j = start
    # i is row position.
    i = 0
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

    # If position has an X
    if maze[i][j] == "X":
        # Print out the path
        print("Found: " + moves)
        # Print the maze with inputed maze and moves made
        printMaze(maze, moves)
        return True

    return False


# Breadth-first algorithm

# Create a queue
nums = queue.Queue()
# Start by putting blank string into queue
nums.put("")
# Add represents the first path that we have, initialize here
add = ""
# Create maze
maze = createMaze2()

# While we haven't found the end of the maze, continue updating path
while not findEnd(maze, add):
    # Get and dequeue first element of queue
    add = nums.get()

    for i in ["L", "R", "U", "D"]:
        # Create new queue (temp) and add the first element we get, then potentially add L, R, U, P
        temp = add + i
        # Make sure path is valid
        if valid(maze, temp):
            # If valid, then add to the queue
            nums.put(temp)
