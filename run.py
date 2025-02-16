import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings

from handlers import user.user, buttons.user
from middlewares.CheckingSubscribe import CheckSubscription


async def main():
  load_dotenv()
  bot = Bot(token=settings.TOKEN)
  dp = Dispatcher(storage=MemoryStorage())

  dp.message.middleware(CheckSubscription())
  
  dp.include_routers(
    user.user
    buttons.user
    )
    
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)
  
  
if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    return