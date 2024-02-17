import json
from json import JSONEncoder

import aiohttp
import os

from aiogram.types import Message

request_url = os.getenv('SERVER_ROUTE')

login_view_route = f'{request_url}/login/'

login_route = f'{request_url}/api/bot-user/login/'
logout_route = f'{request_url}/api/bot-user/logout/'
delete_route = f'{request_url}/api/bot-user/delete/'
signup_route = f'{request_url}/api/bot-user/sign-up/'

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
    async def verify_user_id(message: Message):
        try:
            user_id = message.from_user.id
            print('Call user api: login_user', user_id)

            async with aiohttp.ClientSession() as session:
                async with session.get(f'{login_route}/{user_id}') as resp:
                    response = await resp.json()
                    await session.close()
                    return response.get('user_status')
        except Exception as e:
            return None

    @staticmethod
    async def get_token():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(login_view_route) as resp:
                    csrf_token_value = resp.cookies['csrftoken'].value
                    await session.close()
                    return csrf_token_value
        except Exception as e:
            return None


    @staticmethod
    async def signup_user(message: Message):
        # try:
            print(message.from_user)

            csrf_token = await BotUser.get_token()

            header = {
                "X-CSRFToken": csrf_token,
                "Content-Type": "application/json"
            }

            user_data = {
                "user_id": message.from_user.id,
                "username":  message.from_user.username,
                "csrfmiddlewaretoken": csrf_token
            }
            #
            # async with aiohttp.ClientSession() as session:
            #     async with session.get(login_view_route) as resp:
            #         csrf_token = resp.cookies['csrftoken']


            async with aiohttp.ClientSession() as session:
                async with session.post(
                        signup_route,
                        data=user_data,
                        headers={}
                ) as resp:
                    print('>>> Call user api: signup_user', user_data, resp)
                    # response = await resp.json()

                    # print('.........', response)
                    await session.close()

                    # if response.get('user_status') == USER_CREATED:
                    #     return BotUser.(message)

                    # return response.get('user_status')


        #
        #     async with aiohttp.ClientSession() as session:
        #         async with session.get(f'{login_route}/{user_id}') as resp:
        #             response = await resp.json()
        #             await session.close()
        #             print('>>>>>>', response.get('user_status'))
        #             return response.get('user_status')
        # except Exception as e:
        #     return None



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


