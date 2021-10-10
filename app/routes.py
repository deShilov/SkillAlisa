import aiohttp_cors
from api import post


def setup_routes(app):
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })
    cors.add(app.router.add_post('/post', post.post_handler))