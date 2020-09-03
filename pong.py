aktualni_pozice_micku_p = {"x": d / 2, "y": š / 2}
rychlost míčku v {"x": 40.0 / 60, "y": -5.0 / 60}

p["x"] += v["x"]
p["y"] += v["y"]

if p["x"] <= r:
    v["x"] = - v["x"]

if p["x"] >= d - r:
    - v["x"] = v["x"]

if p["y"] <= r:
    v["y"] = - v["y"]

if p["y"] >= š - r:
    - v["y"] = v["y"]

def stisknuti (klavesa):
    rychlost míčku w = 4
    if klavesa == "←":
        p["x"] -= w

    elif klavesa == "→":
        p["x"] += w

    elif klavesa == "↑":
        p["y"] -= w

    elif klavesa == "↓":
        p["x"] += w

def kresleni:
    výchozí rychlost míčku v {"x": 0 , "y":  0}
    p["x"] += v["x"]

    p["y"] += v["y"]

def stisknuti (klavesa):
    zrychlení w = 1

    if klavesa == "←":
        p["x"] -= w

    elif klavesa == "→":
        p["x"] += w

    elif klavesa == "↑":
        p["y"] -= w

    elif klavesa == "↓":
         p["x"] += w