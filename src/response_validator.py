from ast import Dict
import re
from typing_extensions import Annotated
from typing import List, Iterator, AsyncIterator
from pydantic import BaseModel, StringConstraints, constr, conlist

class ProjectResponse(BaseModel):
    project_title: Annotated[str, StringConstraints(min_length=1)]
    description: Annotated[str, StringConstraints(min_length=1)]
    technical_requirements: conlist(item_type=Annotated[str, StringConstraints(min_length=1)], min_length=1)
    user_stories: conlist(item_type=Annotated[str, StringConstraints(min_length=1)], min_length=1)

class TechList(BaseModel):
    unknown_tech: List[str]
    known_tech: List[str]
    topics: List[str]

def parse_project_data(input: str):
    lines = input.strip().split('\n')
    project_title = description = ""
    technical_requirements = []
    user_stories = []
    current_section = None

    for line in lines:
        if line.lower().startswith("project title:"):
            project_title = line.split(":", 1)[1].strip()
            current_section = None
        elif line.lower().startswith("description:"):
            description = line.split(":", 1)[1].strip()
            current_section = "description"
        elif line.lower().startswith("technical requirements:"):
            current_section = "technical_requirements"
        elif line.lower().startswith("user stories:"):
            current_section = "user_stories"
        elif current_section == "description" and not line.lower().startswith("description:"):
            description += " " + line.strip()
        elif current_section in ["technical_requirements", "user_stories"]:
            if re.match(r"(\d+\)|\d+\.\s|[\•\*\-])", line.strip()):
                item = re.sub(r"^\d+\)|^\d+\.\s|[\•\*\-]", "", line).strip()
                if current_section == "technical_requirements":
                    technical_requirements.append(item)
                else:
                    user_stories.append(item)
    return {
        "project_title": project_title,
        "description": description,
        "technical_requirements": technical_requirements,
        "user_stories": user_stories
    }


def parse_project_data_streaming(chunk: Iterator[str]) -> Iterator[ProjectResponse]:
    line = ""
    project_title = description = ""
    technical_requirements = []
    user_stories = []
    current_section = None

    lines = chunk.split("\n")

    line += lines[0]
    if line.lower().startswith("project title:") and len(lines) > 1:
        project_title = line.split(":", 1)[1].strip()
        current_section = None
    elif line.lower().startswith("description:"):
        description = line.split(":", 1)[1].strip()
        current_section = "description"
    elif line.lower().startswith("technical requirements:"):
        current_section = "technical_requirements"
    elif line.lower().startswith("user stories:"):
        current_section = "user_stories"
    elif current_section == "description" and not line.lower().startswith("description:"):
        description += " " + line.strip()
    elif current_section in ["technical_requirements", "user_stories"]:
        if re.match(r"(\d+\)|\d+\.\s|[\•\*\-])", line.strip()):
            item = re.sub(r"^\d+\)|^\d+\.\s|[\•\*\-]", "", line).strip()
            if current_section == "technical_requirements":
                technical_requirements.append(item)
            else:
                user_stories.append(item)
        if current_section == "user_stories" and line == "":
            yield ProjectResponse(
                                project_title=project_title,
                                description=description,
                                technical_requirements=technical_requirements,
                                user_stories=user_stories
                            )
            project_title = description = ""
            technical_requirements = []
            user_stories = []
            current_section = None
        if len(lines) > 1:
            line = lines[1]

def validate_response(input: str) -> ProjectResponse:
    parsed_data = parse_project_data(input)
    response = ProjectResponse(**parsed_data)
    return response

# test_data = """
# Project Title: DanceRecipe

# Description: Create a web app that combines dancing and cooking by providing users with dance tutorials and recipes to follow, allowing them to learn new dance moves while preparing delicious dishes.

# Technical Requirements:

# • Implement the front end using React and Typescript to build a user-friendly interface for accessing dance tutorials and cooking recipes.
# • Incorporate Vue for interactive elements such as rating dance difficulty and recipe tastiness.
# • Utilize JavaScript to enable seamless transitions between the dance and cooking sections of the app.

# User Stories:

# • As a user, I want to be able to browse through a variety of dance tutorials for different styles.
# • As a user, I want to search for recipes based on ingredients and cuisine types to try out while I dance.
# • As a user, I want to watch video demonstrations of dance moves while simultaneously viewing the steps of a recipe.
# • As a user, I want to be able to save my favorite dance tutorials and recipes to access them later.
# • As a user, I want to provide feedback and ratings on both the dance tutorials and cooking recipes.
# """

# parsed_response = validate_response(test_data)
# print(parsed_response.model_dump_json(indent=4))
