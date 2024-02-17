import aiohttp
import os

request_url = os.getenv('SERVER_ROUTE')

meal_types_route = f'{request_url}/api/meal-types'
meal_route = f'{request_url}/api/meal'


async def get_meal_types():
    try:
        async with (aiohttp.ClientSession() as session):
            async with session.get(meal_types_route) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal_types')
    except:
        return None


async def get_random_meal(meal_type: str = None):
    try:
        async with (aiohttp.ClientSession() as session):
            async with session.get(meal_route, params={"type": meal_type}) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal')
    except Exception as e:
        return None
