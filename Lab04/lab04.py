from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    s.push([startX, startY])
    count = 1
    maze[startX][startY] = count
    while not s.isEmpty():
        if startX - 1 >= 0 and startY >= 0 and startX - 1 < len(maze) and startY < len(maze[0]) and maze[startX - 1][startY] == " ":
            s.push([startX - 1,startY])
            count = count + 1
            maze[startX - 1][startY] = count
            startX = startX - 1
        elif startX - 1 >= 0 and startY >= 0 and startX - 1 < len(maze) and startY < len(maze[0]) and maze[startX - 1][startY] == "G":
            return True
        elif startX >= 0 and startY - 1 >= 0 and startX < len(maze) and startY - 1 < len(maze[0]) and maze[startX][startY - 1] == " ":
            s.push([startX, startY - 1])
            count = count + 1
            maze[startX][startY - 1] = count
            startY = startY - 1
        elif startX >= 0 and startY - 1 >= 0 and startX < len(maze) and startY - 1 < len(maze[0]) and maze[startX][startY - 1] == "G":
            return True
        elif startX + 1 >= 0 and startY >= 0 and startX + 1 < len(maze) and startY < len(maze[0]) and maze[startX + 1][startY] == " ":
            s.push([startX + 1, startY])
            count = count + 1
            maze[startX + 1][startY] = count
            startX = startX + 1
        elif startX + 1 >= 0 and startY >= 0 and startX + 1 < len(maze) and startY < len(maze[0]) and maze[startX + 1][startY] == "G":
            return True
        elif startX >= 0 and startY + 1 >= 0 and startX < len(maze) and startY + 1 < len(maze[0]) and maze[startX][startY + 1] == " ":
            s.push([startX, startY + 1])
            count = count + 1
            maze[startX][startY + 1] = count
            startY = startY + 1
        elif startX >= 0 and startY + 1 >= 0 and startX < len(maze) and startY + 1 < len(maze[0]) and maze[startX][startY + 1] == "G":
            return True
        else:
            s.pop()
            if s.isEmpty():
                return False
            value = s.peek()
            startX = value[0]
            startY = value[1]
    return False
        
