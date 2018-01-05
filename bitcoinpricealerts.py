"""Send Bitcoin price alerts to inbox."""
from requests import get
from gmail import GMail, Message

from config import (COINDESK_CRYPTOPRICE, RECIPIENT,
                    USERNAME, PASSWORD, SENDER_TITLE)


def get_bitcoin_price():
    """Get current Bitcoin price in USD using Coindesk's real-time API"""
    response = get(COINDESK_CRYPTOPRICE).json()

    return response['bpi']['USD']['rate']


def send_email():
    bitcoin_price = get_bitcoin_price()

    # enter actual password, otherwise, nothing happens.
    gmail = GMail(f"{SENDER_TITLE} <{USERNAME}>",
                  password=f'{PASSWORD}')
    message = Message(f'Bitcoin is at {bitcoin_price} right now!',
                      to=RECIPIENT,
                      text=f'The current Bitcoin price is {bitcoin_price}.')

    gmail.send(message)


if __name__ == '__main__':
    send_email()
