import asyncio
import aiohttp
import requests
import time

websites = [
    "https://example.com",
    "https://python.org",
    "https://example.org"
]

async def download_page(client, website):
    for _ in range(3):
        try:
            async with client.get(website) as response:
                print("Async Request:", website, response.status)
                return
        except:
            await asyncio.sleep(1)

async def async_crawler():
    async with aiohttp.ClientSession() as client:
        await asyncio.gather(
            *(download_page(client, site) for site in websites)
        )

def sequential_crawler():
    for site in websites:
        response = requests.get(site)
        print("Sequential Request:", site, response.status_code)

if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(async_crawler())

    print("Async Execution Time:", time.time() - start_time)

    start_time = time.time()

    sequential_crawler()

    print("Sequential Execution Time:", time.time() - start_time)