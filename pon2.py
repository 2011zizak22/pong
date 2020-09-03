
table = {"height": 20, "width": 30}
ball = {"y": table['height']/2,"x": table['width']/2, "dx":1, "dy":-1}
paddleL = {"length": 4, "x": 0, "y": 0, "dy": 2}
paddleR = {"length": 4, "x": table['width'], "y": 0, "dy": 2}

def draw_table(table):
    pass
def draw_ball(ball):
    pass
def draw_paddle(paddle):
    pass


current_ball_position = {"x": height / 2, "y": width / 2}
ball_velocity {"x": 40.0 / 60, "y": -5.0 / 60}

current_ball_position["x"] += current_ball_position["x"]
current_ball_position["y"] += current_ball_position["y"]

if current_ball_position["x"] <= ball_radius:
    variable_ball_velocity["x"] = - variable_ball_velocity["x"]

if current_ball_position["x"] >= height - ball_velocity:
    variable_ball_velocity["x"] = - variable_ball_velocity["x"]

if current_ball_position["y"] <= ball_radius:
    variable_ball_velocity["y"] = - variable_ball_velocity["y"]

if current_ball_position["y"] >= width - ball_radius:
    variable_ball_velocity["y"] = - variable_ball_velocity["y"]

def click (keystroke):
    constant_ball_velocity = 4
    if klavesa == "←":
        current_ball_position["x"] -= w

    elif klavesa == "→":
        current_ball_position["x"] += w

    elif klavesa == "↑":
        current_ball_position["y"] -= w

    elif klavesa == "↓":
        current_ball_position["x"] += w

def drawing:
    implicit_ball_radius{"x": 0 , "y":  0}
    current_ball_position["x"] += variable_ball_velocity["x"]

    current_ball_position["y"] += variable_ball_velocity["y"]

def click (keystroke):
    constant_ball_velocity = 1

    if klavesa == "←":
        current_ball_position["x"] -= w

    elif klavesa == "→":
        current_ball_position["x"] += w

    elif klavesa == "↑":
        current_ball_position["y"] -= w

    elif klavesa == "↓":
    current_ball_position["y"] -= w

    elif klavesa == "↓":
         current_ball_position["x"] += w