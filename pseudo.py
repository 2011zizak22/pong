table = {"height": 20, "width": 30}
ball = {"y": table['height']/2,"x": table['width']/2, "dx":1, "dy":-1}
paddleL = {"length": 4, "x": 0, "y": 0, "dy": 2}
paddleR = {"length": 4, "x": table['width'], "y": 0, "dy": 2}

game_config = {"playerL": "human", "playerR": "cpu", "game_win": 11, "scoreL": 0, "scoreR": 0, "serve": "playerL"} # pause?
def move_paddle (paddle):
    if "x" in paddle  and "y" in paddle: # smyčka uspořádaných dvojic hodnot proměnných x, y, je-li obsažena ve slovníku paddle_left
#       if keystroke[x] != trochucokoliv[x]: # pokud je hodnota proměnné x ve slovníku trochucokoliv různá od předchozí
#                keystroke[x] = trochucokoliv[x] # hodnota proměnné x se nemění
        if keystroke.get_pressed(K_UP) or keystroke.get_pressed(K_W): # v případě stisknutí šipky nahoru nebo klávesy W na klávesnici
            paddle["y"] = paddle["y"] + 1 # přičti jedničku k hodnotě proměnné y slovníku trochucokoliv
        if keystroke.get_pressed(K_DOWN) or keystroke.get_pressed(K_S): # zmáčkne-li uživatel na klávesnici šipku dolů nebo klávesu S
            paddle["y"] = paddle["y"] - 1 # přičti mínus jedničku k hodnotě proměnné slovníku trochucokoliv
        if paddle["y"] > table["height"]: # je-li hodnota proměnné y ve slovníku trochucokoliv větší než hodnota proměnné výšky hřiště či záporná
            paddle["y"] = table["height"] # hodnota proměnné y zůstává stejná
        if paddle["y"] < 0:
            paddle["y"] = 0