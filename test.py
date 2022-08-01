import aiohttp
import asyncio

url = 'https://raw.githubusercontent.com/Arthurs21/matrix_from_web/master/samples/sample1.txt'

async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.text(encoding='utf-8')
        status = response.status
        print(status)


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete()
  loop.close()