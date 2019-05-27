"""
Utilities Module
"""

from cryptosignals.models import Currency
from cryptosignals.settings import CHANGE


def get_threshold(value):
    """Calculates Higher and Lower boundaries for a value"""
    return ((100 + CHANGE) * value) / 100, ((100 - CHANGE) * value) / 100


def get_dashboard_data(subscribed=None):
    """Provides Dashboard data"""
    if not subscribed:
        subscribed = []
    data = Currency.objects.all()
    dashboard_data = []
    for currency in data:
        subscription = currency.coin in subscribed
        currency_data = dict(
            id=currency.coin,
            value=float(currency.value),
            subscription=subscription,
            name=currency.get_stats()['currency_full_form'],
        )
        dashboard_data.append(currency_data)
    return sorted(dashboard_data, key=lambda x: x['id'])
