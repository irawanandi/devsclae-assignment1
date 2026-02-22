from pydantic import BaseModel


class GroupTestRequest(BaseModel):
    nama_group: str
    detail_group: str | None = None


class GroupTestResponse(BaseModel):
    group_id: str
    nama_group: str
    detail_group: str | None = None


class MetodeTestRequest(BaseModel):
    nama_metode: str
    jenis_metode: str
    detail_metode: str | None = None


class MetodeTestResponse(BaseModel):
    metode_id: str
    nama_metode: str
    jenis_metode: str
    detail_metode: str | None = None
