import aiohttp
import os

request_url = os.getenv('SERVER_ROUTE')
IS_LOCAL = os.getenv('IS_LOCAL') == 'True'

# for local development: ignore certificate issue
IGNORE_CERTIFICATE_ISSUE = not IS_LOCAL

meal_types_route = f'{request_url}/api/meal-types'
meal_route = f'{request_url}/api/meal'


async def get_meal_types():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(meal_types_route,
                                   ssl=IGNORE_CERTIFICATE_ISSUE) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal_types')
    except:
        return None


async def get_random_meal(meal_type: str = None, user_id: int = None):
    try:
        params = {"type": meal_type, "user_id": user_id}
        async with (aiohttp.ClientSession() as session):
            async with session.get(meal_route, params=params, ssl=IGNORE_CERTIFICATE_ISSUE) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal')
    except:
        return None
