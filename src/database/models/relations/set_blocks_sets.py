from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class SetBlockSet(Base):
    __tablename__ = "set_blocks_sets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    set_block_id = Column(UUID(as_uuid=True), ForeignKey("set_blocks.id"))
    set_id = Column(UUID(as_uuid=True), ForeignKey("sets.id"))

    set_block = relationship("SetBlock", backref="parent_sets_blocks")
    set = relationship("Set", backref="assigned_sets")
