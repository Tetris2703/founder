import logging
from aiogram import Bot, Dispatcher

API_TOKEN = '7502013178:AAGSaqeF2ZyvzqXM1Ond8oln0QK8TMbA6hE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
