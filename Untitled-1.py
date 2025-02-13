import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

notes = {}
notes_file = 'note.txt'  


def load_notes():
    
    if os.path.exists(notes_file):
        with open(notes_file, 'r', encoding='utf-8') as f:
            for line in f:
                note_id, text = line.strip().split(' - ', 1)
                notes[int(note_id)] = text


def save_notes():
    
    with open(notes_file, 'w', encoding='utf-8') as f:
        for note_id, text in notes.items():
            f.write(f'{note_id} - {text}\n')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я записная книжка. Используй /add для добавления заметки, /view для просмотра всех заметок и /delete для удаления заметки.')


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        note_id = len(notes) + 1
        notes[note_id] = ' '.join(context.args)
        save_notes() 
        await update.message.reply_text(f'Заметка добавлена: {note_id} - {notes[note_id]}')
    else:
        await update.message.reply_text('Пожалуйста, укажите текст заметки после команды /add.')


async def view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if notes:
        notes_list = '\n'.join([f'{note_id}: {text}' for note_id, text in notes.items()])
        await update.message.reply_text(f'Ваши заметки:\n{notes_list}')
    else:
        await update.message.reply_text('Нет заметок.')


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            note_id = int(context.args[0])
            if note_id in notes:
                del notes[note_id]
                save_notes()  
                await update.message.reply_text(f'Заметка {note_id} удалена.')
            else:
                await update.message.reply_text('Нет заметки с таким ID.')
        except ValueError:
            await update.message.reply_text('Пожалуйста, укажите ID заметки для удаления.')
    else:
        await update.message.reply_text('Пожалуйста, укажите ID заметки после команды /delete.')


if __name__ == '__main__':
    load_notes()  

    TELEGRAM_TOKEN = '8079891550:AAFNQ6iC1ZAZA4PJVpZkY5Fr5fan4hEH2MA'
    
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add))
    application.add_handler(CommandHandler("view", view))
    application.add_handler(CommandHandler("delete", delete))

    logger.info("Бот запущен...")
    application.run_polling()
