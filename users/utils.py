from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenObtainCustom(TokenObtainPairView):
    """Напоминалка обновить токен в запросах коллекции + мем для поднятия настроения"""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        custom_data = {
            "НАПОМИНАНИЕ": "Убедитесь, что вы поменяли токен в следующих запросах коллекции!"
        }
        response.data.update(custom_data)
        custom_data = {"Мем": "Здесь могла бы быть ваша реклама"}
        response.data.update(custom_data)

        return response
