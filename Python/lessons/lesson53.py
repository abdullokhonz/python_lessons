# import tkinter
#
# root = tkinter.Tk()
#
# root.title("Приложение на Tkinter")
# root.geometry("300x250+500+300")
#
# root.resizable(False, False)
#
# root.update_idletasks()
# print(root.geometry())
#
# label = tkinter.Label(text="Hello METANIT.COM")
# label.pack()
#
# root.mainloop()

# https://drive.google.com/drive/folders/1KWW0bl_DwjOwZnbeAEMtHNtShvZx_fyp

# 1.) Define the playing screen
# 2.) Create an iterable list that will become the walls of the maze
#     We will use the built in turtle.stamp() feature, which
#     places an unmoving "stamp" of the turtle. Can use different colors or shapes.
# 3.) Create a nested loop to iterate through the list "maze" and actually stamp the screen
#     The positions are x, y coordinates, which is why we need the nested loop
# 4.) Create the player
#       - This involves getting input from the user for the SHAPE of the turtle
#       -This also involves getting input from the user for the OUTLINE color of the turtle.
# 5.) Create a way to move the player on the screen. We can move in four directions - up, down, right, left
#       This function needs 'sub functions' to define those directions and what to do (how far to move, using coordinate system)
#       we also needed to use the turtle.listen() command to allow for input from a keyboard
#       the turtle.onkey(function, 'keyboard item you want to use') utilizes those sub functions defining the directions and what do do
# 6.) Output a message of encouragement to the player at the bottom of the maze


import turtle


# createmaze coded by Ashley Szpanelewski.
# contains: function, list, loop
def CreateMaze():
    # Below we are defining what the window looks like, including the size
    # it also defines the turtle shape, which will be used to construct the maze
    wn = turtle.Screen()
    wn.bgcolor('purple')
    wn.title('Can You Escape the Maze?')
    wn.setup(700, 700)
    turtle.shape("square")
    turtle.color("yellow")
    turtle.penup()
    turtle.speed(0)

    # the list below will define the maze "walls"
    maze = [
        "xxxxxxP xxxxxxxxxxxxxxxxx", "xxxxxxx xxxxxxxxxxxxxxxxx",
        "xxxxxxx           xxxxxxx", "xxxxxxxxxxxxxxx  xxxxxxxx",
        "xxxxxxxxxxxxxxx  xxxxxxxx", "xxxxxxxxxxx       xxxxxxx",
        "xxxx   xxxx xxxxxxxxxxxxx", "xxxxxx xxxx xxxxxxxxxxxxx",
        "xxxxxx xxxx xxxxxxxxxxxxx", "xxxxxx xxxx xxxxxxxxxxxxx",
        "xxxxxx          xxxxxxxxx", "xxxxxx xxxxxxxxxxxxxxxxxx",
        "xxxxxx xxxxxxxxxxxxxxxxxx", "xxxxxx xxxxxxxxxxxxxxxxxx",
        "xxxxxx	xxxxxxxxxxxxxxxxxx", "xxxxxx	xxxxxxxxxxxxxxxxxx",
        "xxxxx             xxxxxxx", "xxxxxxxxx xxxxxxxx xxxxxx",
        "xxxxxxxxx xxxxxxxx	xxxxxx", "xx                 xxxxxx",
        "xxxxxxxxxxxxxxxxxx	xxxxxx", "xxxxxxxxxxxxxxxxxx	     x",
        "xxxxxxxxxxxxxxxxxxxxx xxx", "xxxxxxxxxxxxxxxxxxxxx xxx",
        "xxxxxxxxxxxxxxxxxxxxx xxx"
    ]

    # This list is meant to hold the x, y position of our walls
    # In the loop below, we iterate through the "maze" list, looking
    # for the character x. when found, that position is recorded and
    # appended to our list "walls
    walls = []

    # this loop iterates through the items in the list "maze"
    # where it finds "x" in the list, it stamps a square, stationary turtle (walls)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            # get the character at each x y coord
            character = maze[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # walls.append coded by Mariah Hogan
            # check if x and stamp(represents maze wall) -- Stamp portion Ashley Szpanelewski
            if character == "x":
                turtle.goto(screen_x, screen_y)
                turtle.stamp()
                # add ability to recognize walls Mariah Hogan

                walls.append((screen_x, screen_y))

    CreatePlayer(walls)  # to pass walls variale to stop touching the walls - Mohua added walls


# Create Player coded by Garrett Coletti
# contains: inputs, nested multi alternative statement, and is a function

def CreatePlayer(walls):
    player = turtle.Turtle()
    player_shape = turtle.textinput("What Shape would you like?", "T for Turtle, S for Square, or C for Circle")
    player_color = turtle.textinput("What color?", "[B]lack, [P]ink, or[G]reen?")
    if player_shape == 'T':
        player.shape('turtle')
        if player_color == 'B':
            player.color('black')
            player.fillcolor('light blue')
        if player_color == 'P':
            player.color('pink')
            player.fillcolor('orange')
        if player_color == 'G':
            player.color('green')
            player.fillcolor('light green')
    elif player_shape == 'S':
        player.shape('square')
        if player_color == 'B':
            player.color('black')
            player.fillcolor('dark brown')
        if player_color == 'P':
            player.color('pink')
            player.fillcolor('red')
        if player_color == 'G':
            player.color('green')
            player.fillcolor('forest green')
    else:
        player.shape('circle')
        player.color('green')

    player.penup()
    player.speed(0)
    player.goto(0, 312)  # change the y cordinate from 315 to 312 to determine the turtle's location --- Mohua Das

    MovePlayer(player, walls)


# Move Player coded by Mariah Hogan
# contains functions to define player movement using the keys w,s,a,d
# It contains code to check the x, y coordinates of where the player is moving
# if there is a yellow square there, the turtle cannot pass through it
# Mohua Das figured out how to get the wall detection functional
# Mohua Das also added the IF statement to get the ShowMessage function to be called
# if the turtle reached a certain coordinate just outside the maze.

# added the parameter walls to the function called MovePlayer by Mohua Das
def MovePlayer(player, walls_ip):
    walls = walls_ip

    # determining movement within the maze
    def go_up():
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # check for walls coded by Mariah Hogan
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
        # show the message only if the new cordinate is outside the maze coded by Mohua Das
        if (move_to_x == 216 and move_to_y == -312):
            ShowMessage();

    def go_down():
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)

        if (move_to_x == 216 and move_to_y == -312):
            ShowMessage();

    def go_left():
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)

        if (move_to_x == 216 and move_to_y == -312):
            ShowMessage();

    def go_right():
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)

        if (move_to_x == 216 and move_to_y == -312):
            ShowMessage();

    # assigning commands to keys coded by Mariah Hogan
    turtle.listen()
    turtle.onkey(go_up, "w")
    turtle.onkey(go_down, "s")
    turtle.onkey(go_left, "a")
    turtle.onkey(go_right, "d")


# ShowMessage function was written by Mariah Hogan
def ShowMessage():
    message = turtle.Turtle()
    turtle.setup(700, 700)
    message.penup()
    message.goto(200, -335)

    message.pencolor("pink")
    message.write("Yay! You Did It!", move=False, align="center", font=("Arial", 18, "bold"))


def main():
    CreateMaze()


main()
turtle.done()
