import telebot
from telebot import types
import json
import os


BOT_TOKEN = '8079891550:AAFNQ6iC1ZAZA4PJVpZkY5Fr5fan4hEH2MA'
bot = telebot.TeleBot(BOT_TOKEN)


NOTE_FILE = 'notes.json'



if not os.path.exists(NOTE_FILE):
    with open(NOTE_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f)  
    print(f"Файл {NOTE_FILE} был создан.")

def read_notes():
    """Чтение заметок из файла JSON."""
    with open(NOTE_FILE, 'r', encoding='utf-8') as f:
        notes = json.load(f)
    return notes

def write_note(note):
    notes = read_notes()
    notes.append(note)
    with open(NOTE_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def delete_note(index):
    notes = read_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        with open(NOTE_FILE, 'w', encoding='utf-8') as f:
            json.dump(notes, f, ensure_ascii=False, indent=4)
        return True
    return False

def handler_new_member(message):
    get_user = message.reply_to_message.from_user
    bot.send_message(message.chat.id, f'User: {get_user.first_name}\nID{get_user.id}')



def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add = types.KeyboardButton("Добавить заметку")
    btn_view = types.KeyboardButton("Просмотреть заметки")
    btn_delete = types.KeyboardButton("Удалить заметку")
    markup.add(btn_add, btn_view, btn_delete)
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Используйте меню ниже.")
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == "Добавить заметку")
def add_note_command(message):
    """Запрос текста для добавления заметки."""
    msg = bot.send_message(message.chat.id, "Введите текст заметки:")
    bot.register_next_step_handler(msg, process_note_addition)

def process_note_addition(message):
    """Обработка добавления заметки."""
    note_text = message.text.strip()
    if note_text:
        write_note(note_text)
        bot.send_message(message.chat.id, "Заметка добавлена!")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите текст заметки.")

@bot.message_handler(func=lambda message: message.text == "Просмотреть заметки")
def view_notes_command(message):
    notes = read_notes()
    if notes:
        response = "Ваши заметки:\n"
        for i, note in enumerate(notes):
            response += f"{i + 1}. {note}\n"
    else:
        response = "У вас нет заметок."
    
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: message.text == "Удалить заметку")
def delete_note_command(message):
    msg = bot.send_message(message.chat.id, "Введите номер заметки для удаления:")
    bot.register_next_step_handler(msg, process_note_deletion)

def process_note_deletion(message):
    try:
        index = int(message.text.strip()) - 1  
        if delete_note(index):
            bot.send_message(message.chat.id, "Заметка удалена!")
        else:
            bot.send_message(message.chat.id, "Заметка с таким номером не найдена.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный номер заметки.")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "/start - начать работу с ботом\n"
        "/help - показать это сообщение"
    )
    bot.send_message(message.chat.id, help_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
