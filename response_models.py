from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, field_validator, ConfigDict


class ResourceRequest(BaseModel):
    id_: int = Field(alias="id", strict=True)
    project_tasks_resource_id: int
    volume: float
    cost: float
    batch_number: Optional[int] = None
    batch_parent_request_id: Optional[int] = None
    is_over_budget: bool
    created_at: int
    updated_at: int
    user_id: int
    needed_at: int
    created_by: int

    @field_validator('id_', 'updated_at')
    @classmethod
    def id_must_be_7_chars(cls, value: int):
        if len(str(value)) < 7:
            raise ValueError('ID less then 7 chars')
        return value


class ResourceRequestResponse(BaseModel):
    project_tasks: List[ResourceRequest]


class CreateResourceRequestBody(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: str
    needed_at: int
    project_id: int
    type_: int = Field(alias="type")
    volume: int
