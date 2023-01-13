from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Note
from dependencies import get_session
from pydantic import BaseModel

router = APIRouter()


class AddRequest(BaseModel):
    title: str


class EditRequest(BaseModel):
    title: str
    id: int
    checked: bool


class DeleteRequest(BaseModel):
    id: int


@router.get("/items")
async def root(session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Note)
    )
    notes = result.fetchall()
    return notes


@router.post("/items/delete")
async def delete(req: DeleteRequest, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Note).filter(
            Note.id == req.id
        )
    )
    note = result.fetchone()
    if not note:
        raise HTTPException(status_code=204, detail='To-do-item не найден')
    await session.delete(note[0])
    await session.commit()
    return {"message": "Успешное удаление"}


@router.post("/items/create")
async def create(req: AddRequest, session: AsyncSession = Depends(get_session)):
    note = Note(title=req.title, checked=False)
    session.add(note)
    await session.commit()
    return {'message': 'Успешное добавление'}


@router.post("/items/update")
async def update(req: EditRequest, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Note).filter(
            Note.id == req.id
        )
    )
    note = result.fetchone()
    if not note:
        raise HTTPException(status_code=404, detail='To-do-item не найден')
    setattr(note[0], 'title', req.title)
    setattr(note[0], 'checked', req.checked)
    await session.commit()
    return {'message': 'Успешное изменение'}
