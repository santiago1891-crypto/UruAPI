from pydantic import BaseModel

class GetHTMLSchema(BaseModel):
    endpoint : str
