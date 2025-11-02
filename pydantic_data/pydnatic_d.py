from pydantic import  BaseModel,Field
from typing import Annotated,Optional
class student_details(BaseModel):
    student_id:Annotated[int,Field(...,description="enter the roll no",example=5000)]
    name:Annotated[str,Field(...,description="enter the name",example="firdosh")]
    age:Annotated[int,Field(...,description="enter the age ",example=50,gt=0,lt=120)]
    gender:Annotated[str,Field(...,description="enter the gender",example="Male")]
    p_class:Annotated[str,Field(...,description="enter the p_calss",example="10th")]
    study_hours:Annotated[float,Field(...,description="enter the study hours",example=5.9,gt=0,lt=24)]
    attendance:Annotated[int,Field(...,description="enter the attendence persentage",example=90,gt=0,lt=100)]
    math_score:Annotated[int,Field(...,description="enter the math persentage ",example=90,gt=0,lt=100)]
    science_score:Annotated[int,Field(...,description="enter the science presentage",example=90,gt=0,lt=100)]
    english_score:Annotated[int,Field(...,description="enter the english presentage",example=90,gt=0,lt=100)]
    passed:bool
    