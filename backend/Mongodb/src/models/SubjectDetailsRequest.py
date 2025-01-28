import uuid
from typing import Optional, List

from fastapi import File
from pydantic import BaseModel, Field

from src.models.EvaluationProbe import EvaluationProbe
from src.models.FileMaterial import FileMaterial

class SubjectDetailsRequest(BaseModel):
    title : str = Field(...)
    subject_code : str = Field(...)
    evaluation_probes: List[EvaluationProbe]
    course_materials: Optional[List[FileMaterial]]
    lab_materials: Optional[List[FileMaterial]]