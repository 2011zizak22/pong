table = {"height": 20, "width": 30}
ball = {"y": table['height']/2,"x": table['width']/2, "dx":1, "dy":-1}
paddleL = {"length": 4, "x": 0, "y": 0, "dy": 2}
paddleR = {"length": 4, "x": table['width'], "y": 0, "dy": 2}

    if "x" in paddleL  and "y" in paddleL: # smyčka uspořádaných dvojic hodnot proměnných x, y, je-li obsažena ve slovníku paddle_left
#        if trochucokoliv[x] != trochucokoliv[x]: # pokud je hodnota proměnné x ve slovníku trochucokoliv různá od předchozí
#                trochucokoliv[x] = trochucokoliv[x] # hodnota proměnné x se nemění
        if trochucokoliv.get_pressed(K_UP) or trochucokoliv.get_pressed(K_W): # v případě stisknutí šipky nahoru nebo klávesy W na klávesnici
            paddleL["y"] = paddleL["y"] + 1 # přičti jedničku k hodnotě proměnné y slovníku trochucokoliv
        if trochucokoliv.get_pressed(K_DOWN) or trochucokoliv.get_pressed(K_S): # zmáčkne-li uživatel na klávesnici šipku dolů nebo klávesu S
            paddleL["y"] = paddleL["y"] - 1 # přičti mínus jedničku k hodnotě proměnné slovníku trochucokoliv
        if paddleL["y"] > table["height"]: # je-li hodnota proměnné y ve slovníku trochucokoliv větší než hodnota proměnné výšky hřiště či záporná
                paddleL["y"] = table["height"] # hodnota proměnné y zůstává stejná
        if paddleL["y"] < 0:
                paddleL["y"] = 0


    if "x" in paddleR and "y" in paddleR: # smyčka uspořádaných dvojic hodnot proměnných x, y, je-li obsažena ve slovníku paddle_right
        
        if trochucokoliv[x] != trochucokoliv[x]: # pokud je hodnota proměnné x ve slovníku trochucokoliv různá od předchozí
                trochucokoliv[x] = trochucokoliv[x] # hodnota proměnné x se nemění
        if trochucokoliv[y] > display_height or trochucokoliv[y] < 0: # je-li hodnota proměnné y ve slovníku trochucokoliv větší než hodnota proměnné výšky hřiště či záporná
                trochucokoliv[y] = trochucokoliv[y] # hodnota proměnné y zůstává stejná
        if trochucokoliv.get_pressed(K_UP) or trochucokoliv.get_pressed(K_W): # v případě stisknutí šipky nahoru nebo klávesy W na klávesnici
                trochucokoliv[y] = trochucokoliv[y] + 1 # přičti jedničku k hodnotě proměnné y slovníku trochucokoliv
        if trochucokoliv.get_pressed(K_DOWN) or trochucokoliv.get_pressed(K_S): # zmáčkne-li uživatel na klávesnici šipku dolů nebo klávesu S
                trochucokoliv[y] = trochucokoliv[y] - 1 # přičti mínus jedničku k hodnotě proměnné slovníku trochucokoliv
