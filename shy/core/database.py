import os
import asyncpg

class DatabaseHandler(object):

    @staticmethod
    async def run_setup_schema(pool):

        with open('./static/schema.sql', 'r', encoding='utf-8') as schema:
            __script = schema.read() 

        async with pool.acquire() as connection:
            await connection.execute(
                __script
            )

    @classmethod
    async def init_database(cls, *args, **kwargs):

        DATABASE_ADDRESS = os.environ.get("DATABASE_ADDRESS")
        DATABASE_USER = os.environ.get("DATABASE_USER")
        DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
        DATABASE_NAME = os.environ.get("DATABASE_NAME")

        pool = await asyncpg.create_pool(
            database = DATABASE_NAME,
            user = DATABASE_USER,
            password = DATABASE_PASSWORD,
            host = DATABASE_ADDRESS
        )

        await cls.run_setup_schema(pool)
        return pool