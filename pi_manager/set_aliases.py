import json
from pathlib import Path

from pi_manager.consts import DEFAULT_ALIAS_PATH, BASH_ALIASES_PATH


def set_aliases(alias_path: str = None):
    if alias_path is None:
        alias_path = DEFAULT_ALIAS_PATH

    alias_path = Path(alias_path)
    alias_data = json.load(open(alias_path))

    bash_aliases_file = open(BASH_ALIASES_PATH, "a")

    for alias, phrase in alias_data:
        bash_aliases_file.write(f"alias {alias}={phrase}\n")
