from typing import List
from pydantic import BaseModel

class ProjectResponse(BaseModel):
    project_title: str
    description: str
    technical_requirements: List[str]
    user_stories: List[str]
    

def validate_response(input):
    return ProjectResponse.model_validate_json(input)