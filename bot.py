import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан. Скопируйте .env.example в .env и укажите токен.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def on_text(message: Message) -> None:
    entities = message.entities or []
    custom_emoji_ids = [
        e.custom_emoji_id
        for e in entities
        if e.type == "custom_emoji" and e.custom_emoji_id
    ]

    if not custom_emoji_ids:
        await message.answer("В сообщении нет custom emoji.")
        return

    lines = [f"{i}. {eid}" for i, eid in enumerate(custom_emoji_ids, start=1)]
    await message.answer("\n".join(lines))


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
