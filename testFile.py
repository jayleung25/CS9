from lab04 import solveMaze


def shouldFailTest():
    maze = [
        ["+","+"," "," ", " "],
        ["+"," "," ","+"," "],
        ["+"," ","+"," "," "],
        ["G","+","+"," ","+"]]
    assert solveMaze(maze,3,3) == False
    assert maze == [
        ["+","+",7,6, 5],
        ["+",9,8,"+",4],
        ["+",10,"+",2,3],
        ["G","+","+",1,"+"]]

def shouldPassTest():
    maze = [
        ["+"," "," "," "],
        [" "," ","+","G"],
        [" ","+","+","+"]]
    assert solveMaze(maze,2,0) == True
    assert maze == [
        ["+",4,5,6],
        [2,3,"+","G"],
        [1,"+","+","+"]]
shouldFailTest()
shouldPassTest()
    
    
