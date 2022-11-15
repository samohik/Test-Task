import os
import smtplib
from email.mime.text import MIMEText

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    balance = models.IntegerField(verbose_name='Balance', default=200, null=True, blank=False)

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def send_email(message=None):
        sender = Profile.objects.get(id=1)
        your_password = "your password"
        password = os.getenv("EMAIL_PASSWORD")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)
            msg = MIMEText(message)
            msg["Subject"] = "Static information!"
            server.sendmail(sender, sender, msg.as_string())
            return "The message was sent successfully!"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password please!"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Category(models.Model):
    default_category = [
        "Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование",
        "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд"
    ]
    profile = models.ForeignKey('Profile', related_name='category', on_delete=models.CASCADE, )
    name = models.CharField(verbose_name='Name', max_length=255, default=default_category[0], )

    def __str__(self):
        return f'{self.name}'


class TransactionHistory(models.Model):
    transactions = models.ForeignKey(
        'Profile', verbose_name='Profile', related_name='transactions', on_delete=models.CASCADE
    )
    amount = models.IntegerField(verbose_name='Amount', null=True, )
    time = models.DateTimeField(verbose_name='Time', auto_now_add=True, )
    category = models.CharField(verbose_name='Category', max_length=255, )
    organization = models.CharField(verbose_name='Organization', max_length=255, )
    description = models.CharField(verbose_name='Description', max_length=255, )

    def __str__(self):
        return f'amount: {self.amount}, category: {self.category}'

    class Meta:
        ordering = ('time', )
        verbose_name = 'history'
        verbose_name_plural = 'history\'s'
