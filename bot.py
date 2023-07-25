#библиотеки, которые загружаем из вне
import telebot


from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 My repository")
	item2 = types.KeyboardButton("😋 Send me message")
	item3 = types.KeyboardButton("🌐 My VK")
	item4 = types.KeyboardButton("🎶")

	markup.add(item1, item2,item3,item4)

	bot.send_message(message.chat.id, "Держи вкусняшку, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def connector(message):
	if message.chat.type == 'private':
		if message.text == '🧡 My repository':
			bot.send_message(message.chat.id, 'https://github.com/AntonAktaevQA')
		elif message.text == '🌐 My VK':
			bot.send_message(message.chat.id, 'https://vk.com/id118770058')
		elif message.text == '🎶':
			bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
		elif message.text == '😋 Send me message':
			bot.send_message(message.chat.id, 'https://t.me/Ntony_Soulja')
		else:
			bot.send_message(message.chat.id, 'Шо это?😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
