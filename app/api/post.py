from aiohttp import web
import asyncpg
import json
from helpers.forward_num import parser_and_calculator
from nltk.tokenize import WordPunctTokenizer
from helpers.init_nn import responce_nn


async def post_handler(request):

    post = await request.post()
    event = await request.json()


    if event['request']['original_utterance'] == '':
        text = 'Я рада тебя тут видеть!'

    else:
        try:
    	    text = str(parser_and_calculator(event['request']['original_utterance']))
        except:
            text = 'Что-то пошло не так! {}'.format(responce_nn(event['request']['original_utterance']))

    response = {'version':  event['version'], 'response': {'text': text, 'end_session': 'false'}}

    return web.json_response(response)
