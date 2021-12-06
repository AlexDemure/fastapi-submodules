import asyncio
from typing import AnyStr

import aioredis
import ujson

from backend.core.config import settings


class RedisService:

    pool = None

    async def redis_init(self):
        """Инициализация редиса и получение его пула."""
        self.pool = await aioredis.create_redis_pool(settings.REDIS_URI, password=settings.REDIS_PASSWORD)

    @staticmethod
    async def register_service(service):
        """Регистрация сервисов."""
        asyncio.create_task(service())

    async def get_task(self, queue_name: AnyStr):
        serialized_task = await self.pool.rpop(queue_name)
        if serialized_task:
            return ujson.loads(serialized_task)

    async def get_tasks(self, queue_name: AnyStr):
        for i in range(await self.pool.llen(queue_name)):
            serialized_task = await self.pool.rpop(queue_name)
            if serialized_task:
                yield ujson.loads(serialized_task)

    async def append_task(self, queue_name: AnyStr, task: dict):
        serialized_task = ujson.dumps(task)
        await self.pool.lpush(queue_name, serialized_task)

    async def append_task_first(self, queue_name: AnyStr, task: dict):
        serialized_task = ujson.dumps(task)
        await self.pool.rpush(queue_name, serialized_task)


redis = RedisService()

