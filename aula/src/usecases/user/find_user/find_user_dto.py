from uuid import UUID
from pydantic import BaseModel


class FindUserInputDto(BaseModel):
    id: UUID


class FindUserOutpudDto(BaseModel):
    id: UUID
    name: str
