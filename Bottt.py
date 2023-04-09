import random

from BotPrimer import token
import telebot
from bs4 import BeautifulSoup as bs
import requests
import time

bot = telebot.TeleBot(token)
name = ''
spisok_films = []
spisok_pop = []
sp_com = []
sp_garrem = []
sp_fant = []
sp_horr = []

def spisok_500():
    global spisok_films
    if len(spisok_films) == 0:
        for i in range(1):
            response_get = requests.get(f'https://animego.org/anime')
            soup = bs(response_get.text, features='html.parser')
            quotes_film = soup.find_all('div', class_='h5 font-weight-normal mb-1')
            for film in quotes_film:
                spisok_films.append(film.text)
        return random.choice(spisok_films)
    else:
        return random.choice(spisok_films)


def spisok_pupular():
    global spisok_pop
    if len(spisok_pop) == 0:
        for i in range(1):
            response_get = requests.get("https://animego.org/manga")
            manga = bs(response_get.text, features="html.parser")
            popular_film = manga.find_all('div', class_='h5 font-weight-normal mb-1')
            for film in popular_film:
                spisok_pop.append(film.text)
        return random.choice(spisok_pop)
    else:
        return random.choice(spisok_pop)


def comedy_():
    global sp_com
    if len(sp_com) == 0:
        for i in range(1):
            response_get = requests.get("https://animego.org/manga/filter/genres-is-comedy/apply")
            manga = bs(response_get.text, features="html.parser")
            com_manga = manga.find_all('div', class_="h5 font-weight-normal mb-1")
            for man in com_manga:
                sp_com.append(man.text)
            return random.choice(sp_com)
        else:
            return random.choice(sp_com)

def garrem_():
    global sp_garrem
    if len(sp_garrem):
        for i in range(1):
            response_get = requests.get("https://animego.org/manga/filter/genres-is-harem/apply")
            manga = bs(response_get.text, features="html.parser")
            gar_manga = manga.find_all('div', class_='h5 font-weight-normal mb-1')
            for man in gar_manga:
                sp_garrem.append(man.text)
            return random.choice(sp_garrem)


def fantasy_():
    global sp_fant
    if len(sp_fant):
        for i in range(1):
            response_get = requests.get("https://animego.org/manga/filter/genres-is-sci-fi/apply")
            manga = bs(response_get.text, features="html.parser")
            fant_manga = manga.find_all('div', class_='h5 font-weight-normal mb-1')
            for man in fant_manga:
                sp_fant.append(man.text)
                return random.choice(sp_fant)


def horror_():
    global sp_horr
    if len(sp_horr):
        for i in range(1):
            response_get = requests.get("https://animego.org/manga/filter/genres-is-horror/apply")
            manga = bs(response_get.text, features='html.perser')
            horr_man = manga.find_all('div', class_='h5 font-weight-normal mb-1')
            for man in horr_man:
                sp_horr.append(man.text)
                return random.choice(sp_horr)



@bot.message_handler(commands=['start'])
def start_com(message):
    poem = 'Приветствуем в нашем боте!!!\nКак тебя зовут?'
    bot.send_message(message.chat.id, poem)
    bot.register_next_step_handler(message, reg_name)


@bot.message_handler(commands=['help'])
def help_com(message):
    help_text = '''
    "Для того чтобы начать введите команду /pusk" \
    "Для получения помощи введите команду /help" \
    "Для того чтобы заново запустить бота введите /start" \
    "При работе с ботом используйте клавиатуру, которая появится после отправки команды pusk"
    '''
    bot.send_message(message.chat.id, help_text)


def keyboard_pusk():
    keyb_markup = telebot.types.ReplyKeyboardMarkup()
    button_genre = telebot.types.KeyboardButton('Жанры фильмов')
    button_rand_popular = telebot.types.KeyboardButton('Случайный фильм из популярного')
    button_rand_500 = telebot.types.KeyboardButton('Случайный фильм из 500 лучших')
    keyb_markup.row(button_genre)
    keyb_markup.row(button_rand_popular)
    keyb_markup.row(button_rand_500)
    return keyb_markup


def keyboard_genre():
    keyb_genre_reply = telebot.types.InlineKeyboardMarkup()
    key_comedy = telebot.types.InlineKeyboardButton(text='Комедии', callback_data='comedy')
    key_garrem = telebot.types.InlineKeyboardButton(text='Гаррем', callback_data='garrem')
    key_fantasy = telebot.types.InlineKeyboardButton(text='Фэнтези', callback_data='fantasy')
    key_horror = telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='horror')
    keyb_genre_reply.add(key_comedy, key_garrem, key_fantasy, key_horror)
    return keyb_genre_reply


@bot.message_handler(commands=['pusk'])
def pusk_com(message):
    bot.send_message(message.chat.id, 'Поехали!', reply_markup=keyboard_pusk())


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Приятно познакомиться {name} \nЧтобы начать отправь /pusk\n'
                                      f'Если тебе нужна помощь, то отправь /help')


@bot.message_handler(content_types=['text'])
def genre_repl(message):
    if message.text == 'Жанры фильмов':
        bot.send_message(message.chat.id, 'Выберите один из жанров:', reply_markup=keyboard_genre())
    if message.text == 'Случайный фильм из популярного':
        bot.send_message(message.chat.id, spisok_pupular())
    if message.text == 'Случайный фильм из 500 лучших':
        bot.send_message(message.chat.id, spisok_500())



@bot.callback_query_handler(func=lambda call: True)
def genre_reply_but(call):
    if call.data == 'comedy':
        bot.send_message(call.message.chat.id, comedy_())
    if call.data == 'garrem':
        bot.send_message(call.message.chat.id, garrem_())
    if call.data == 'fantasy':
        bot.send_message(call.message.chat.id, fantasy_())
    if call.data == 'horror':
        bot.send_message(call.message.chat.id, horror_())


bot.polling()
