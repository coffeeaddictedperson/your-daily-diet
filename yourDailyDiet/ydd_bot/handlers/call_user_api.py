import aiohttp
import os

from aiogram.types import Message

request_url = os.getenv('SERVER_ROUTE')

login_route = f'{request_url}/api/bot-user/login'
logout_route = f'{request_url}/api/bot-user/logout'
delete_route = f'{request_url}/api/bot-user/delete'
signup_route = f'{request_url}/api/bot-user/signup'

# async def get_admin_keyboards():
#     try:
#         async with (aiohttp.ClientSession() as session):
#             async with session.get(meal_types_route, auth=aiohttp.BasicAuth(
#                     user='admin', password='admin')) as resp:
#                 response = await resp.json()
#                 await session.close()
#                 return response.get('meal_types')
#     except:
#         return None


# async def store_user(meal_type: str = None):
#     try:
#         async with (aiohttp.ClientSession() as session):
#             async with session.get(meal_route, params={"type": meal_type}) as resp:
#                 response = await resp.json()
#                 await session.close()
#                 return response.get('meal')
#     except Exception as e:
#         return None

class BotUser:

    @staticmethod
    async def login_user(message: Message):
        try:
            user_id = message.from_user.id
            print('>>>>>> BOT: login_user', user_id)

            async with aiohttp.ClientSession() as session:
                async with session.get(f'{login_route}/{user_id}') as resp:
                    response = await resp.json()
                    await session.close()
                    print('>>>>>>', response.get('user_status'))
                    return response.get('user_status')
        except Exception as e:
            print(e)
            return None



async def logout_user(meal_type: str = None):
    pass

async def delete_user(meal_type: str = None):
    pass
#     try:
#         async with (aiohttp.ClientSession() as session):
#             async with session.get(meal_route, params={"type": meal_type}) as resp:
#                 response = await resp.json()
#                 await session.close()
#                 return response.get('meal')
#     except Exception as e:
#         return None


