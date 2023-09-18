from typing import List
from models import Clip

def __read_file(filename) -> str:
    
    data: str = ""
    with open(filename, 'r') as f:
        data = f.read()
    
    return data

def __get_sections(data: str) -> List[str]:
    sections: List[str] = data.split("\n\n")

    return sections

def __parse_section(data: str) -> Clip:
    lines = data.split("\n")

    line_split = [line.split(": ", 1) for line in lines if line]

    line_data = {split[0]: split[1] for split in line_split}

    clip: Clip = Clip()

    clip.clipper = line_data.get("User", "Unknown")
    clip.title = line_data.get("Title")
    clip.link = line_data.get("Link")

    return clip

def __parse_sections(sections: List[str]) -> List[Clip]:
    return [__parse_section(section) for section in sections]


def parse_data(filename: str) -> List[Clip]:
    data: str = __read_file(filename)
    sections: List[str] = __get_sections(data)
    return __parse_sections(sections)