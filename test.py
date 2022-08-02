import aiohttp
import asyncio

url = 'https://raw.githubusercontent.com/Arthurs21/matrix_from_web/master/samples/sample1.txt'
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text(encoding='utf-8')
            status = response.status
            s = []
            for t in data.split():
                try:
                    s.append(int(t))
                except ValueError:
                    pass
            print(s)


asyncio.run(main())
