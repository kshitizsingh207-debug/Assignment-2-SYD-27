import turtle

# Create turtle object
t = turtle.Turtle()
t.speed(3)   # Controls drawing speed (1 = slow, 10 = fast)

def draw_edge(length, depth):
    """
    Recursive function to draw one edge of the geometric pattern.
    Indentation (V shape) points DOWNWARD.
    
    length : length of the edge
    depth  : recursion level
    """

    # BASE CASE (Depth 0)
    if depth == 0:
        t.forward(length)
        return

    # Divide the line into 3 equal parts
    part = length / 3

    # First segment
    draw_edge(part, depth - 1)

    # TURN RIGHT instead of LEFT → flips V downward
    t.right(60)

    # Second segment
    draw_edge(part, depth - 1)

    # TURN LEFT instead of RIGHT → inward indentation
    t.left(120)

    # Third segment
    draw_edge(part, depth - 1)

    # Restore original direction
    t.right(60)

    # Fourth segment
    draw_edge(part, depth - 1)


# ---- MAIN PROGRAM ----
draw_edge(300, 1)  # Depth 1 pattern
turtle.done()