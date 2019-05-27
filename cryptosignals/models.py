"""
Models
"""
import json

from django.contrib.auth.models import AbstractUser
from django.db import models

from cryptosignals.services.slack import send_slack_message


class Currency(models.Model):
    """Currency Model Class"""
    coin = models.CharField(max_length=20, primary_key=True)
    value = models.DecimalField(max_digits=13, decimal_places=3)
    stats = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def get_stats(self):
        """Returns dictionary of stats"""
        return json.loads(self.stats)

    def send_slack_notification(self, message):
        """Filters the user with token, channel, subscription and sends the notification"""
        slack_tokens = self.users.filter(
            subscription=True
        ).exclude(
            models.Q(token__exact='') |
            models.Q(token__isnull=True) |
            models.Q(channel__exact='') |
            models.Q(channel__isnull=True)
        ).values_list(
            'token',
            'channel',
        )
        for token, channel in slack_tokens:
            send_slack_message(token, message, channel)

    def __str__(self):
        return "{0}".format(self.coin)


class User(AbstractUser):
    """Custom User Model Class"""
    currency = models.ManyToManyField(Currency, related_name='users')
    token = models.CharField(default='', max_length=255)
    channel = models.CharField(default='', max_length=32)
    subscription = models.BooleanField(default=False)

    def get_subscription_list(self):
        """Provides subscribed coin list"""
        subscribed = self.currency.values_list('coin', flat=True)
        return subscribed

    def toggle_subscription(self, coin):
        """Toggles the subscription of the user for a particular coin"""
        if coin in self.get_subscription_list():
            self.currency.remove(coin)
        else:
            self.currency.add(coin)
