import pickle
from colorthief import ColorThief
colors = []
for i in range(0, 238144):

    try:
        color_thief = ColorThief(f"Exoplanet/{i}.png")

        dominant_color = color_thief.get_color(quality=1)

        colors.append(dominant_color)
    except:
        dominant_color = (255, 255, 255)

        colors.append(dominant_color)

    
pickle.dump(colors, open("colors_exoplanet", "wb"))
