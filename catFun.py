import runWorld as rw
import drawWorld as dw
import pygame as pg

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
#
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Cat Fun. Press the mouse (but not too fast)!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")
myimage2 = dw.loadImage("hat.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(myimage, (state.x, state.y))
    dw.draw(myimage2, (state.x, state.y-50))
    dw.draw(dw.makeLabel("SPEED: "+ str(counter), "Helvetica", 50, dw.black), (12, 12))
    dw.draw(dw.makeLabel("Try to reach max speed!", "Helvetica", 50, dw.black), (50, 50))
    

################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state.x, and delta-pos
# as state.xvel. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    # Make changes to `state`
    state.x = state.x + state.xvel
    state.y = state.y - state.yvel
    return state
   # return(state.x+state.xvel,state.xvel,state.y-state.yvel,state.yvel)


################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state.x > width or state.x < 0 or state.y > height or state.y < 0):
        return True
    else:
        return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
counter = 0
score = 0
def handleEvent(state, event):
    global counter
    global score
    score = score + 0.5
    if event.type == pg.KEYDOWN:
        counter = counter + 1
        if event.key == pg.K_LEFT:
            counter = counter + 1
            state.x = state.x
            state.xvel = state.xvel - counter
            state.y = state.y
            state.yvel = 0
            return state
            #return((state.x,state.xvel-counter, state.y, 0))
        if event.key == pg.K_RIGHT:
            counter = counter + 1
            state.x = state.x
            state.xvel = state.xvel + counter
            state.y = state.y
            state.yvel = 0
            return state            
           # return((state.x,state.xvel+counter, state.y, 0))
        if event.key == pg.K_UP:
            counter = counter + 1
            state.x = state.x
            state.xvel = 0
            state.y = state.y
            state.yvel = state.yvel + counter
            return state
           # return((state.x,0, state.y, state.yvel+counter))
        if event.key == pg.K_DOWN:
            counter = counter + 1
            state.x = state.x
            state.xvel = 0
            state.y = state.y
            state.yvel = state.yvel - counter
            return state
            
           # return((state.x,0, state.y, state.yvel-counter))
    else:
        return(state)


#    print("Handling event: " + str(event)) .
#    if (event.type == pg.K):
#        if (state.xvel) == 1:
#            newState = -1
#        else:
#            newState = 1
#        return((state.x,-state.xvel, state.y, -state.yvel))
#    else:
#        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right
#initState = (500,1,500,0)

# Run the simulation no faster than 60 frames per second
frameRate = 45

# Run the simulation!


class State:
    def __init__(self, x, xvel, y, yvel):
        self.x = x
        self.xvel = xvel
        self.y = y
        self.yvel = yvel

myState = State(500, 1, 500, 0)

rw.runWorld(myState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
