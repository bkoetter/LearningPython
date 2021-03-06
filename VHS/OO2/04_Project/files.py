from pathlib import Path


def get_files_in_dir(path: str, selector: str) -> list:
    if not path.strip():
        path = ""
    if not selector.strip():
        selector = "*.txt"
    files = []
    location = Path(path)
    for f in location.glob(selector):
        files.append(f"{path}/{f.name}")

    return files


def read_file_content(path: str, count: int) -> list:
    with open(path, mode='r', encoding="utf-8") as file:
        content = file.read().splitlines()

    return content[:count]
