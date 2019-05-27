"""Module for Slack notifications"""
from django.utils.timesince import timesince
from slackclient import SlackClient
from multiprocessing import Process
from cryptosignals.settings import USERNAME, ICON


def get_emoji_and_percent_change(current_value, previous_value):
    """Provides emoji and percent change based on the current and previous value"""
    rate = current_value * 100 / previous_value
    if current_value <= previous_value:
        return ':small_red_triangle_down:', round(100 - rate, 2)
    return ':arrow_up:', round(rate - 100, 2)


def get_slack_message(currency, current_value, stats, time_of_update, old_values):
    """Provides message for notifying users"""
    time_difference = timesince(old_values['updated'], time_of_update)

    emoji, percent_change = get_emoji_and_percent_change(
        current_value=current_value,
        previous_value=float(old_values['value']),
    )

    status_update = "*{0}* Treading at Rs *{1}*, *{2}* {3}% in *{4}*, Previously Rs *{5}*".format(
        currency,
        current_value,
        emoji,
        percent_change,
        time_difference,
        old_values['value']
    )

    trade_stats = "`Buyers from Rs {0} Sellers from Rs {1}`".format(
        stats['highest_bid'],
        stats['lowest_ask']
    )

    message = '\n'.join([status_update, trade_stats])

    return message


def send_slack_message(token, message, channel):
    """function for sending slack messages"""
    process = Process(target=slack_async_api, args=[token, message, channel])
    process.start()


def slack_async_api(token, message, channel):
    """Threaded function for sending slack messages"""
    sc = SlackClient(token)
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=message,
        as_user=False,
        username=USERNAME,
        icon_emoji=ICON,
    )
