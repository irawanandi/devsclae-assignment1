from app.schema.test_psikologi import MetodeTestRequest
from app.models.database import MetodeTest
from sqlmodel import select
from app.models.engine import get_db
from fastapi import APIRouter, status, Depends, HTTPException


metode_test_router = APIRouter(tags=["Metode Test"])


@metode_test_router.get(path="/metode-test", status_code=status.HTTP_200_OK)
def get_metode_test(db=Depends(get_db)):
    stmt = select(MetodeTest)
    result = db.exec(stmt)
    metode_test = result.all()

    return metode_test


@metode_test_router.post(path="/metode-test", status_code=status.HTTP_201_CREATED)
def add_metode_test(body: MetodeTestRequest, db=Depends(get_db)):
    try:
        new_metode_test = MetodeTest(
            nama_metode=body.nama_metode,
            jenis_metode=body.jenis_metode,
            detail_metode=body.detail_metode,
        )

        db.add(new_metode_test)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

    return {f"Berhasil Menambahkan {body.nama_metode} sebagai alat test baru"}
