from django.http import JsonResponse

from ..models.bot_data import BotUserData

STATUS_OK = "ok"
STATUS_ERROR = "error"

USER_LOGGED_IN = "logged_in"
USER_LOGGED_OUT = "logged_out"
USER_NOT_FOUND = "user_not_found"

USER_ALREADY_EXIST = "user_already_exists"
USER_CREATED = "user_created"

USER_VERIFIED = "user_verified"
USER_EXPIRED = "user_expired"
USER_NON_VERIFIED = "user_non_verified"

class BotUserAPI:
    @staticmethod
    def verify_user_code(request):
        code = request.GET.get('code')
        user_id = request.GET.get('user_id')

        bot_user = BotUserData.objects.filter(bot_user_id=user_id).first()

        if bot_user:
            if bot_user.is_valid_code(code) and not bot_user.is_expired:
                bot_user.set_is_verified()
                status = USER_VERIFIED
            elif bot_user.is_valid_code(code) and bot_user.is_expired:
                status = USER_EXPIRED
            else:
                status = USER_NON_VERIFIED
        else:
            status = USER_NOT_FOUND

        return JsonResponse({
            "status": STATUS_OK,
            "user_status": status
        }, safe=False)

    @staticmethod
    def verify_user(user_id):
        bot_user = BotUserData.objects.filter(bot_user_id=user_id).first()

        if bot_user:
            if bot_user.is_still_valid:
                status = USER_VERIFIED
            else:
                status = USER_NON_VERIFIED
        else:
            status = USER_NOT_FOUND
        return status
