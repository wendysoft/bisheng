# Path: src/backend/bisheng/database/models/flowstyle.py

from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from bisheng.database.models.base import SQLModelSerializable
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from bisheng.database.models.flow import Flow


class FlowStyleBase(SQLModelSerializable):
    color: str
    emoji: str
    flow_id: UUID = Field(default=None, foreign_key='flow.id')


class FlowStyle(FlowStyleBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    flow: 'Flow' = Relationship(back_populates='style')


class FlowStyleUpdate(SQLModelSerializable):
    color: Optional[str] = None
    emoji: Optional[str] = None


class FlowStyleCreate(FlowStyleBase):
    pass


class FlowStyleRead(FlowStyleBase):
    id: UUID
