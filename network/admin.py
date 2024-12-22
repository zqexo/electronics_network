from django.contrib import admin
from django.core.exceptions import PermissionDenied

from network.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "city", "supplier", "debt", "created_at"]
    list_filter = ["city", "country"]
    search_fields = ["name", "email"]
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        # Проверяем, является ли пользователь staff или superuser
        if not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("Вы не имеете прав для выполнения этого действия.")

        # Обновляем задолженность выбранных объектов
        queryset.update(debt=0)
        self.message_user(
            request, f"Задолженность очищена для {queryset.count()} объектов."
        )

    clear_debt.short_description = (
        "Очистить задолженность перед поставщиком (только staff/superuser)"
    )
