from django.db import models


class NetworkNode(models.Model):
    """
    Модель элемента торговой сети электроники.
    """

    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=20, verbose_name="Номер дома")
    product_name = models.CharField(max_length=255, verbose_name="Название продукта")
    product_model = models.CharField(max_length=255, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")
    supplier = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="clients",
        verbose_name="Поставщик",
    )
    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    responsible_user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="network_nodes",
        verbose_name="Ответственный пользователь",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Элемент сети"
        verbose_name_plural = "Элементы сети"


class Network(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0)
    supplier = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="supplied_networks",
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    network = models.ForeignKey(
        Network, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.model})"
