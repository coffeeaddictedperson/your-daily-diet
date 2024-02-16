import aiohttp
import os

request_url = os.getenv('SERVER_ROUTE')
request_path = 'api/meal-types'
meal_types_route = f'{request_url}/{request_path}'


async def get_meal_types():
    try:
        async with (aiohttp.ClientSession() as session):
            async with session.get(meal_types_route) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal_types')
    except:
        return None
