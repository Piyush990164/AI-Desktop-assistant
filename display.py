import os
import random
import ctypes

def change_wallpaper():
    wallpaper_path = r"C:\Users\piyus_\Downloads\mpl keliye pics"  

    wallpapers = [f for f in os.listdir(wallpaper_path) if f.endswith(('.jpg', '.png', '.bmp'))]
    wallpaper = random.choice(wallpapers)
    full_path = os.path.join(wallpaper_path, wallpaper)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 3)

    return "Wallpaper changed successfully!"  # <-- RETURN this, not print



 