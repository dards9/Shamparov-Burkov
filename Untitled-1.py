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

def delete_note(index, user_id):
    notes = read_notes()
    if 0 <= index < len(notes) and notes[index]['user_id'] == user_id:
        notes.pop(index)
        with open(NOTE_FILE, 'w', encoding='utf-8') as f:
            json.dump(notes, f, ensure_ascii=False, indent=4)
        return True
    return False

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
    note_text = message.text
    user_id = message.from_user.id
    note = {
        'text': note_text,
        'user_id': user_id  
    }
    write_note(note)
    bot.send_message(message.chat.id, "Заметка добавлена!")
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == "Просмотреть заметки")
def view_notes_command(message):
    user_id = message.from_user.id
    notes = read_notes()
    
    user_notes = [note for note in notes if isinstance(note, dict) and note.get('user_id') == user_id]
    
    if user_notes:
        response = "Ваши заметки:\n"
        for i, note in enumerate(user_notes):
            response += f"{i + 1}. {note['text']}\n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "У вас нет заметок.")

@bot.message_handler(func=lambda message: message.text == "Удалить заметку")
def delete_note_command(message):
    user_id = message.from_user.id
    notes = read_notes()
    
    user_notes = [note for note in notes if isinstance(note, dict) and note.get('user_id') == user_id]
    
    if not user_notes:
        bot.send_message(message.chat.id, "У вас нет заметок для удаления.")
        return
    
    response = "Ваши заметки:\n"
    for i, note in enumerate(user_notes):
        response += f"{i + 1}. {note['text']}\n"
    
    msg = bot.send_message(message.chat.id, response + "Введите номер заметки для удаления:")
    bot.register_next_step_handler(msg, lambda m: process_note_deletion(m, user_notes))

def process_note_deletion(message, user_notes):
    try:
        index = int(message.text.strip()) - 1  
        user_id = message.from_user.id
        
        
        note_to_delete_index = next((i for i, note in enumerate(read_notes()) if note['user_id'] == user_id and note in user_notes), None)
        
        if delete_note(note_to_delete_index, user_id):
            bot.send_message(message.chat.id, "Заметка удалена!")
        else:
            bot.send_message(message.chat.id, "Заметка с таким номером не найдена.")
        
        main_menu(message)  
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный номер заметки.")
        main_menu(message)

@bot.message_handler(commands=['start'])
def help_command(message):
    start_text = (
        "/start - начать работу с ботом\n"
    )
    bot.send_message(message.chat.id, start_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
