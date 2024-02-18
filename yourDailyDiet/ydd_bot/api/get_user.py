from typing import Union

from aiogram.client.session import aiohttp

import os
request_url = os.getenv('SERVER_ROUTE')
verify_route = f'{request_url}/api/verify'


async def verify_user_code(code: str = '', user_id: Union[str, int] = None):
    try:
        params = {"code": code.strip(), "user_id": user_id}
        async with (aiohttp.ClientSession() as session):
            async with session.get(verify_route, params=params) as resp:
                response = await resp.json()
                await session.close()
                return response.get('meal')
    except:
        return None
