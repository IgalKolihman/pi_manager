import os
import subprocess
from urllib import request

from pi_manager.consts import MANAGER_MEDIA_DIR

ARG_MAP = {
    'feh': ['feh', ['--bg-center'], '%s'],
    'gnome': ['gsettings',
              ['set', 'org.gnome.desktop.background', 'picture-uri'],
              'file://%s']
}

WM_BKG_SETTERS = {
    'spectrwm': ARG_MAP['feh'],
    'scrotwm': ARG_MAP['feh'],
    'wmii': ARG_MAP['feh'],
    'i3': ARG_MAP['feh'],
    'awesome': ARG_MAP['feh'],
    'awesome-gnome': ARG_MAP['gnome'],
    'gnome': ARG_MAP['gnome'],
    'ubuntu': ARG_MAP['gnome']
}


# TODO: check that this way of setting the wallpaper works on the raspberry
def get_image(image_url: str):
    request.urlretrieve(image_url, MANAGER_MEDIA_DIR)


def set_wallpaper(color: str):
    if color not in ["yellow", "green", "blue", "red"]:
        raise ValueError(f'Color "{color}" does not exist. Requires: "yellow", "green", "blue" or "red.')

    get_image(f"https://raw.githubusercontent.com/IgalKolihman/pi_manager/main/wallpapers/{color}.jpg")

    # Try to find background setter
    desktop_environ = os.environ.get('DESKTOP_SESSION', '')

    if desktop_environ and desktop_environ in WM_BKG_SETTERS:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS.get(
            desktop_environ, [None, None])

    else:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS['spectrwm']

    pargs = [bkg_setter] + args + [pic_arg % f"{MANAGER_MEDIA_DIR}{color}.jpg"]
    subprocess.call(pargs)
