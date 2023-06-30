from sqlalchemy import func, insert, select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def add_not_repeated(cls, records):
        async with async_session_maker() as session:
            count_saved_records = 0
            for record in records:
                existing_record = await cls.find_one_or_none(
                    id_source=record['id_source']
                )
                if not existing_record:
                    count_saved_records += 1
                    query = (
                        insert(cls.model)
                        .values(**record)
                        .returning(
                            cls.model.id,
                            cls.model.question,
                            cls.model.answer,
                            cls.model.airdate,
                            cls.model.created_at,
                            cls.model.id_source,
                        )
                    )
                    await session.execute(query)
                    await session.commit()
            return count_saved_records

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filter_by)
                .order_by(cls.model.id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def get_last_record(cls):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .where(
                    cls.model.id ==
                    select(func.max(cls.model.id)).scalar_subquery()
                )
            )
            result = await session.execute(query)
            return result.mappings().one_or_none()
