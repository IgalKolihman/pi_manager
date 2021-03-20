import os

from pi_manager.common import exec_command


def set_wallpaper(color: str):
    if color not in ["yellow", "green", "blue", "red"]:
        print(f'color type does not exist. needs "yellow", "green", "blue", "red" not "{color}"')

    # TODO: this command doesn't work, check why. maybe a new approach is needed
    gsettings_path = exec_command(["which", "gsettings"])
    command = f"{gsettings_path} set org.gnome.desktop.background picture-uri /home/user/Pictures/wallpapers/X"

