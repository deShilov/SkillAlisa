from aiohttp import web
import asyncpg
import json


async def get_groups(db):
    """"""
    resp = await db.exec_(query="""SELECT "group" FROM timetable GROUP BY "group" """)
    return resp


async def groups_handler(request):
    #response_data = await get_groups(request.app['db'])

    return web.json_response('get')