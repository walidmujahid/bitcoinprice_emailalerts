"""Send daily Bitcoin price alerts to inbox."""
from time import sleep

from requests import get
import schedule
from gmail import GMail, Message


def get_bitcoin_price():
    """Get current Bitcoin price in USD using Coindesk's real-time API"""
    response = get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    return response['bpi']['USD']['rate']


def send_email(recipient: str= 'walid.mujahid.dev@gmail.com'):
    bitcoin_price = get_bitcoin_price()

    # enter actual password, otherwise, nothing happens.
    gmail = GMail('Price Alert <walid.mujahid.open@gmail.com>',
                  password='password')
    message = Message(f'Bitcoin is at {bitcoin_price} right now!',
                      to=recipient,
                      text=f'The current Bitcoin price is {bitcoin_price}.')

    gmail.send(message)


if __name__ == '__main__':
    schedule.every().day.at("06:30").do(send_email)

    while True:
        schedule.run_pending()
        sleep(1)
