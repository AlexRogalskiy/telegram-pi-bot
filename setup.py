from distutils.core import setup

setup(
    name = 'telegram-pi-bot',
    packages = ['telegram_pi_bot'],
    version = '0.2.2',
    description = 'A python-telegram-bot setup to run on Raspberry pi',
    author = 'Ruy Adorno',
    author_email = 'ruyadorno@hotmail.com',
    url = 'https://github.com/ruyadorno/telegram-pi-bot',
    download_url = 'https://github.com/ruyadorno/telegram-pi-bot/tarball/0.2.2',
    keywords = ['telegram', 'raspberrypi', 'bot', 'python-telegram-bot'],
    install_requires=['python-telegram-bot>=5,<6'],
    data_files=[('telegram_pi_bot', ['telegram_pi_bot/messages.json'])],
    classifiers = [],
    entry_points = {
        'console_scripts': [
            'telegram-pi-bot = telegram_pi_bot.command_line:main'
        ]
    }
)

