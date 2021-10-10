from aiohttp import web
from routes import setup_routes
from external.postgres import PostgresEngine
import yaml
import pathlib

from helpers.init_nn import BasicModel


async def init_pg(app):
    database_config = app['config']['postgres']
    postgres = PostgresEngine()
    await postgres.setup({
        'min_con': database_config['minsize'],
        'max_con': database_config['maxsize'],
        'name': database_config['database'],
        'username': database_config['user'],
        'password': database_config['password'],
        'host': database_config['host'],
        'port': database_config['port'],})
    app['db'] = postgres


async def init_app(config=None):
    app = web.Application()
    conf = load_config(str(pathlib.Path('.') / 'config' / 'default.yaml'))
    app['config'] = conf
    app.on_startup.append(init_pg)
    setup_routes(app)
    return app


def load_config(path):
    with open(path, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg


def start():
    app = init_app()
    web.run_app(app, host='127.0.0.1', port=8080)


if __name__ == '__main__':
    start()
