from django.http import JsonResponse

from ..models.telegram_user import BotUser

STATUS_OK = "ok"

USER_LOGGED_IN = "logged_in"
USER_LOGGED_OUT = "logged_out"
USER_NOT_FOUND = "user_not_found"
USER_ALREADY_EXIST = "user_already_exists"
USER_CREATED = "user_created"


class BotUserAPI:

    @staticmethod
    def _check_user_exists(user_id: str):
        return BotUser.objects.filter(bot_user_id=user_id).first()

    @staticmethod
    def _create_user(user_id, username):
        user = BotUserAPI._check_user_exists(user_id)
        if user is None:
            user = BotUser.objects.create(bot_user_id=user_id,
                                          username=username)
            user.save()
            return USER_CREATED

        return USER_ALREADY_EXIST

    @staticmethod
    def _login_user(user_id: str):
        user = BotUserAPI._check_user_exists(user_id)
        if user is not None:
            user.logged_in = False
            user.save()
            return USER_LOGGED_IN

        return USER_NOT_FOUND

    @staticmethod
    def _logout_user(user_id: str):
        user = BotUserAPI._check_user_exists(user_id)
        if user is not None:
            user.logged_in = False
            user.last_login = user.last_login.now()
            user.save()
            return USER_LOGGED_OUT

        return USER_NOT_FOUND

    # Public methods
    @staticmethod
    def login_bot_user(request, user_id):
        resp = BotUserAPI._login_user(user_id)
        print('>>>>login_bot_user', resp, request, user_id)
        return JsonResponse({
            "status": STATUS_OK,
            "user_status": resp
        }, safe=False)

    @staticmethod
    def logout_bot_user(request, user_id):
        return JsonResponse({
            "status": STATUS_OK,
            "user_status": BotUserAPI._logout_user(user_id)
        }, safe=False)


    @staticmethod
    def create_bot_user(request, user_id, username):
        return JsonResponse({
            "status": STATUS_OK,
            "user_status": BotUserAPI._create_user(user_id, username)
        }, safe=False)

    @staticmethod
    def delete_bot_user():
        pass
