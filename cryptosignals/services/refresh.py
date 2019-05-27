"""
Helpers and Procedures for refreshing the data
"""
import json

from cryptosignals.models import Currency
from cryptosignals.services.koinex import koinex
from cryptosignals.services.slack import get_slack_message
from cryptosignals.services.utils import get_threshold


def update_currency(currency, value, stats):
    """Creates or Updates the currency table with the new values"""
    defaults = dict(
        value=value,
        stats=json.dumps(stats),
    )
    return Currency.objects.update_or_create(coin=currency, defaults=dict(**defaults))


def update_currencies_and_send_notification():
    """Verifies the changes, Updates the Database and Sends Notifications"""
    data, time_of_update = koinex.get_latest_updates()
    old_data = {
        currency['coin']: currency
        for currency in Currency.objects.values('coin', 'value', 'updated',)
    }

    for currency, current_value in data['prices']['inr'].items():
        current_value = float(current_value)
        old_values = old_data.get(currency)
        stats = data['stats']['inr'][currency]

        if not old_values:
            update_currency(currency, current_value, stats)
            continue

        high, low = get_threshold(float(old_values['value']))
        if not low < current_value < high:
            obj, is_created = update_currency(currency, current_value, stats)
            message = get_slack_message(
                currency,
                current_value,
                stats,
                time_of_update,
                old_values
            )
            obj.send_slack_notification(message)


