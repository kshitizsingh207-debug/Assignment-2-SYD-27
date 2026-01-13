
import turtle

# Create turtle object
t = turtle.Turtle()
t.speed(3)  # controls drawing speed

def draw_edge(length, depth):
    """
    Recursive function to draw one edge of the pattern.
    
    length : length of the line
    depth  : level of recursion
    """

    # BASE CASE
    # If depth is 0, draw a straight line (no modification)
    if depth == 0:
        t.forward(length)   # moves turtle forward by 'length'
        return              # stops recursion

# ---- MAIN PROGRAM ----
draw_edge(300, 0)  # Depth 0: straight line
turtle.done()