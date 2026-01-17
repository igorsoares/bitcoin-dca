from pathlib import Path
import schedule.configuration.user_environment as us
import yaml

_data = None

def getenvs():
    global _data
    if _data is None:
        settings_file = "settings.yaml"
        if(us.settings_yaml_file is not None):
            settings_file = us.settings_yaml_file
        PROJECT_ROOT = Path(__file__).parent.parent.parent #Path(__file__).resolve().parents[2]
        with open(f"{PROJECT_ROOT}/{settings_file}") as f:
            _data = yaml.safe_load(f)
    return _data

