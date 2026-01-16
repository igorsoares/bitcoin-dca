from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / "settings.yaml"

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)