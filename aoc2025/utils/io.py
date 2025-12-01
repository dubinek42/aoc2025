from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # root of the project
INPUTS_DIR = BASE_DIR / "inputs"


def load_input(day: int, sample: bool = False) -> str:
    filename = f"{day:02d}{'_sample' if sample else ''}.txt"
    path = INPUTS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Input file {path} does not exist")
    return path.read_text(encoding="utf-8").rstrip("\n")
