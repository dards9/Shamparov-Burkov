import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка уровня логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Структура для хранения заметок (пример на словаре)
notes = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я записная книжка. Используй /add для добавления заметки, /view для просмотра всех заметок и /delete для удаления заметки.')

# Команда /add для добавления заметки
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        note_id = len(notes) + 1
        notes[note_id] = ' '.join(context.args)
        await update.message.reply_text(f'Заметка добавлена: {note_id} - {notes[note_id]}')
    else:
        await update.message.reply_text('Пожалуйста, укажите текст заметки после команды /add.')

# Команда /view для отображения всех заметок
async def view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if notes:
        notes_list = '\n'.join([f'{note_id}: {text}' for note_id, text in notes.items()])
        await update.message.reply_text(f'Ваши заметки:\n{notes_list}')
    else:
        await update.message.reply_text('Нет заметок.')

# Команда /delete для удаления заметки
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            note_id = int(context.args[0])
            if note_id in notes:
                del notes[note_id]
                await update.message.reply_text(f'Заметка {note_id} удалена.')
            else:
                await update.message.reply_text('Нет заметки с таким ID.')
        except ValueError:
            await update.message.reply_text('Пожалуйста, укажите ID заметки для удаления.')
    else:
        await update.message.reply_text('Пожалуйста, укажите ID заметки после команды /delete.')

# Основная функция для запуска бота
if __name__ == '__main__':
    # Вставьте токен вашего бота
    TELEGRAM_TOKEN = '8079891550:AAFNQ6iC1ZAZA4PJVpZkY5Fr5fan4hEH2MA'
    
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add))
    application.add_handler(CommandHandler("view", view))
    application.add_handler(CommandHandler("delete", delete))

    logger.info("Бот запущен...")
    application.run_polling()