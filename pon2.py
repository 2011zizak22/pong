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
         current_ball_position["x"] += w