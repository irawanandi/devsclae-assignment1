from app.models.database import GroupTest
from sqlmodel import select
from app.models.engine import get_db
from app.schema.test_psikologi import GroupTestRequest
from fastapi import APIRouter, status, Depends, HTTPException

group_router = APIRouter(tags=["GroupTest"])


@group_router.get(path="/group-test", status_code=status.HTTP_200_OK)
def get_group_test(db=Depends(get_db)):
    stmt = select(GroupTest)
    result = db.exec(stmt)
    group_test = result.all()
    return group_test


@group_router.post(path="/group-test", status_code=status.HTTP_201_CREATED)
def add_group_test(body: GroupTestRequest, db=Depends(get_db)):
    try:
        new_group = GroupTest(
            nama_group=body.nama_group, detail_group=body.detail_group
        )
        db.add(new_group)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

    return {f"✅️ Group Baru {body.nama_group} Berhasil Ditambahkan!"}
