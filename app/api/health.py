from aiohttp import web


async def health_check(request):
    return web.json_response('Hello!') #web.Response()
