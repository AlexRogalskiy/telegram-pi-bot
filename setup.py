from distutils.core import setup

setup(
  name = 'telegram-pi-bot',
  packages = ['telegram-pi-bot'],
  version = '0.1.0',
  description = 'A python-telegram-bot setup to run on Raspberry pi',
  author = 'Ruy Adorno',
  author_email = 'ruyadorno@hotmail.com',
  url = 'https://github.com/ruyadorno/telegram-pi-bot',
  download_url = 'https://github.com/ruyadorno/telegram-pi-bot/tarball/0.1.0',
  keywords = ['telegram', 'raspberrypi', 'bot', 'python-telegram-bot'],
  install_requires=['python-telegram-bot>=5,<6'],
  classifiers = [],
)

