import aiohttp
import asyncio
import json

async def main(data_req):
	async with aiohttp.ClientSession() as session:
		async with session.post('http://127.0.0.1:8080/post', data=data_req) as resp:
			return await resp.json()


original_utterance = 'пять умножить на восемь плюс тридцать восемь'

data = '''
{
  "meta": {
    "locale": "ru-RU",
    "timezone": "UTC",
    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
    "interfaces": {
      "screen": {},
      "payments": {},
      "account_linking": {}
    }
  },
  "session": {
    "message_id": 0,
    "session_id": "fd04f944-d617-40ae-b829-a2a143cd658c",
    "skill_id": "ac30f89a-ba04-46af-a115-56260a2499dc",
    "user": {
      "user_id": "3165E021D1D365AF222CDE0C287B0A1B847958301B482E6EB5B581E9F11D03C5"
    },
    "application": {
      "application_id": "D890B82A98B42E34B95D2FFA30D1F5AFE160FC31E6C8EA5182A91F8FC6E4942A"
    },
    "new": true,
    "user_id": "D890B82A98B42E34B95D2FFA30D1F5AFE160FC31E6C8EA5182A91F8FC6E4942A"
  },
  "request": {
    "command": "",
    "original_utterance": "{0}",
    "nlu": {
      "tokens": [],
      "entities": [],
      "intents": {}
    },
    "markup": {
      "dangerous_context": false
    },
    "type": "SimpleUtterance"
  },
  "version": "1.0"
}
'''

original_utterance
asd = json.loads(data)
asd['request']['original_utterance'] = original_utterance
reqsef = json.dumps(asd)

loop = asyncio.get_event_loop()
req = loop.run_until_complete(main(reqsef))
print(req)