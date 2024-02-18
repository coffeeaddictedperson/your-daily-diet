from typing import Union

from aiogram.client.session import aiohttp

import os
request_url = os.getenv('SERVER_ROUTE')
IS_LOCAL = os.getenv('IS_LOCAL') == 'True'
verify_route = f'{request_url}/api/verify'
verify_request_route = f'{request_url}/api/verify-user'

# for local development: ignore certificate issue
IGNORE_CERTIFICATE_ISSUE = not IS_LOCAL

async def verify_user_code(code: str = '', user_id: Union[str, int] = None):
    try:
        params = {"code": code.strip(), "user_id": user_id}
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    verify_route,
                    params=params,
                    ssl=IGNORE_CERTIFICATE_ISSUE
            ) as resp:
                response = await resp.json()
                await session.close()
                return response.get('user_status')
    except:
        return None


async def verify_user_request(user_id: Union[str, int] = None):
    try:
        params = {"user_id": user_id}
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    verify_request_route,
                    params=params,
                    ssl=IGNORE_CERTIFICATE_ISSUE
            ) as resp:
                response = await resp.json()
                await session.close()
                return response.get('user_status')
    except:
        return None
