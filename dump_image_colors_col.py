import pickle
colors = pickle.load(open("colors_exoplanet", "rb"))

def get_col_color_value(col):
    red = 0
    green = 0
    blue = 0
    totalBrightness = 0

    for c in range(col, col + ((238144) - 487), 488):

        red = colors[c][0] + red
        green = colors[c][1] + green
        blue = colors[c][2] + blue
        totalBrightness += 0.2126*colors[c][0] + 0.7152*colors[c][1] + 0.0722*colors[c][2]
    
    
    return (red, green, blue, totalBrightness)

def get_total_color():
    color = (0, 0, 0, 0)
    colors = []
    for col in range(488):
        color = tuple(map(lambda i, j: i + j, color, get_col_color_value(col)))
        colors.append(get_col_color_value(col))

    return colors
    
colors_col = get_total_color()

for i in range(len(colors_col)): colors_col[i] = tuple(map(lambda x: x / 488, colors_col[i]))
    
pickle.dump(colors_col, open("colors_col_exoplanet", "wb"))
