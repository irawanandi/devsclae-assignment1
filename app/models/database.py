import uuid
from sqlmodel import SQLModel, Field


class GroupTest(SQLModel, table=True):
    group_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    nama_group: str = Field(default="Group 1....")
    detail_group: str | None = Field(default=None)


class MetodeTest(SQLModel, table=True):
    metode_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    nama_metode: str = Field(default="Nama Metode Test...")
    jenis_metode: str = Field(default="Jenis Metode Test...")
    detail_metode: str | None = Field(default=None)
