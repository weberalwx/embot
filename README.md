# Telegram-бот: извлечение custom_emoji_id

Минимальный бот на Python + aiogram 3. Отвечает нумерованным списком `custom_emoji_id` из входящего сообщения.

## Запуск

```bash
pip install -r requirements.txt
cp .env.example .env
# Укажите BOT_TOKEN в .env
python bot.py
```

Отправьте боту сообщение с premium/custom emoji — в ответ получите список ID. Если custom emoji нет, бот ответит: «В сообщении нет custom emoji.»
