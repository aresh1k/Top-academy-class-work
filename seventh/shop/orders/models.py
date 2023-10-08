from django.db import models
from users.models import User
from products.models import Basket


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email_name = models.EmailField(max_length=200, verbose_name='Email')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    basket_history = models.JSONField(default=dict, verbose_name='История заказов')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')

    def __str__(self):
        return f'Заказ №{self.id}. {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        baskets.delete()
        self.save()
