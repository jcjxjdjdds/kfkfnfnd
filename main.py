import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
##################################
bot = telebot.TeleBot("6494235642:AAEnW0tK5dZpMulN6WPUi-m5Q_aoCBNTy3s")
##################################
'''
@DuDrD
@iq_python
'''
S = '''@DuDrD
@iq_python
البوت اشتغل .'''
##################################

               # S          A          I                 F
               # F          A          R                S
                               
                               # @DuDrD
                               # @iq_python

##################################
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    text = ""
    if call.data == "a1":
        text = """للاستفسار - @cEbot


❨ اوامر الرفع والتنزيل ❩

⌯ رفع ↣ ↢ تنزيل مشرف
⌯ رفع ↣ ↢ تنزيل مالك اساسي
⌯ رفع ↣ ↢ تنزيل مالك
⌯ رفع ↣ ↢ تنزيل مدير
⌯ رفع ↣ ↢ تنزيل ادمن
⌯ رفع ↣ ↢ تنزيل مميز
⌯ تنزيل الكل  ↢ بالرد  ↢ لتنزيل الشخص من جميع رتبه
⌯ تنزيل الكل  ↢ بدون رد  ↢ لتنزيل كل رتب المجموعة

❨ اوامر المسح ❩

⌯ مسح المالكيين
⌯ مسح المدراء
⌯ مسح الادمنيه
⌯ مسح المميزين
⌯ مسح المحظورين
⌯ مسح المكتومين
⌯ مسح قائمة المنع
⌯ مسح رتبه
⌯ مسح الرتب
⌯ مسح الردود
⌯ مسح الاوامر
⌯ مسح + العدد
⌯ مسح بالرد
⌯ مسح الترحيب
⌯ مسح قائمة التثبيت

❨ اوامر الطرد الحظر الكتم ❩

⌯ حظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ طرد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ كتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ تقيد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الحظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الكتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء التقييد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ رفع القيود ↢ لحذف الكتم,الحظر,التقييد
⌯ منع الكلمة
⌯ منع بالرد على قيف او ستيكر
⌯ الغاء منع الكلمة
⌯ طرد البوتات
⌯ كشف البوتات

❨ اوامر النطق ❩

⌯ انطقي + الكلمة
⌯ وش يقول؟ + بالرد على فويس لترجمه المحتوى

❨ اوامر اخرى ❩

⌯ الرابط
⌯ معلومات الرابط
⌯ انشاء رابط
⌯ بايو
⌯ بايو عشوائي
⌯ ايدي
⌯ الانشاء
⌯ مجموعاتي
⌯ @admin
⌯ نقل ملكية
⌯ صوره
⌯ افتاري
⌯ افتار + باليوزر او الرد
⌯ مين ضافني؟"""
    elif call.data == "a2":
        text = """للاستفسار - @cEbot


❨ اوامر الوضع ❩

⌯ وضع ترحيب
⌯ وضع قوانين
⌯ تغيير رتبه
⌯ تغيير امر

❨ اوامر رؤية الاعدادات ❩

⌯ المطورين
⌯ المالكيين الاساسيين
⌯ المالكيين 
⌯ الادمنيه
⌯ المدراء
⌯ المشرفين
⌯ المميزين
⌯ القوانين
⌯ قائمه المنع
⌯ المكتومين
⌯ المطور 
⌯ معلوماتي 
⌯ الاعدادت
⌯ المجموعه
⌯ الساعه
⌯ التاريخ
⌯ صلاحياتي
⌯ لقبي
⌯ صلاحياته + بالرد"""
    elif call.data == "a3":
        text = """للاستفسار - @cEbot


❨ اوامر الردود ❩

⌯ الردود ↢ تشوف كل الردود المضافه
⌯ اضف رد ↢ عشان تضيف رد
⌯ مسح رد ↢ عشان تمسح الرد
⌯ مسح الردود ↢ تمسح كل الردود
⌯ الرد + كلمة الرد
-

❨ اوامر القفل والفتح بالمسح ❩

⌯ قفل ↣ ↢ فتح  التعديل  
⌯ قفل ↣ ↢ فتح  الفويسات 
⌯ قفل ↣ ↢ فتح  الفيديو 
⌯ قفل ↣ ↢ فتح  الـصــور 
⌯ قفل ↣ ↢ فتح  الملصقات 
⌯ قفل ↣ ↢ فتح  الدخول 
⌯ قفل ↣ ↢ فتح  الفارسية
⌯ قفل ↣ ↢ فتح  الملفات  
⌯ قفل ↣ ↢ فتح  المتحركات 
⌯ قفل ↣ ↢ فتح  تعديل الميديا
⌯ قفل ↣ ↢ فتح  تعديل الميديا بالتقييد
⌯ قفل ↣ ↢ فتح  الدردشه 
⌯ قفل ↣ ↢ فتح  الروابط 
⌯ قفل ↣ ↢ فتح  الهشتاق 
⌯ قفل ↣ ↢ فتح  البوتات 
⌯ قفل ↣ ↢ فتح  اليوزرات 
⌯ قفل ↣ ↢ فتح  الاشعارات 
⌯ قفل ↣ ↢ فتح  الكلام الكثير
⌯ قفل ↣ ↢ فتح  التكرار 
⌯ قفل ↣ ↢ فتح  التوجيه 
⌯ قفل ↣ ↢ فتح  الانلاين 
⌯ قفل ↣ ↢ فتح  الجهات 
⌯ قفل ↣ ↢ فتح  الــكـــل 
⌯ قفل ↣ ↢ فتح  السب
⌯ قفل ↣ ↢ فتح  الاضافه
⌯ قفل ↣ ↢ فتح  الصوت
⌯ قفل ↣ ↢ فتح  القنوات 

❨ اوامر التفعيل والتعطيل ❩

⌯ تفعيل ↣ ↢ تعطيل الترحيب 
⌯ تفعيل ↣ ↢ تعطيل الردود 
⌯ تفعيل ↣ ↢ تعطيل الايدي
⌯ تفعيل ↣ ↢ تعطيل الرابط
⌯ تفعيل ↣ ↢ تعطيل اطردني
⌯ تفعيل ↣ ↢ تعطيل الحماية
⌯ تفعيل ↣ ↢ تعطيل المنشن
⌯ تفعيل ↣ ↢ تعطيل التحقق 
⌯ تفعيل ↣ ↢ تعطيل ردود المطور 
⌯ تفعيل ↣ ↢ تعطيل التحذير 
⌯ تفعيل ↣ ↢ تعطيل البايو 
⌯ تفعيل ↣ ↢ تعطيل انطقي"""
    elif call.data == "a4":
        text = """☤ تفعيل الالعاب 
☤ تعطيل الالعاب 
    ╼╾
✽ جمل
✽ كلمات
✽ اغاني
✽ دين
✽ عربي
✽ اكمل
✽ صور
✽ كت تويت
✽ مؤقت
✽ اعلام
✽ معاني
✽ تخمين
✽ احكام
✽ ارقام
✽ احسب
✽ خواتم
✽ انقليزي
✽ ترتيب
✽ انمي
✽ تركيب
✽ تفكيك
✽ عواصم
✽ روليت
✽ سيارات
✽ ايموجي
✽ حجره
✽ ديمون
╼╾
❖ فلوسي ↼ عشان تشوف فلوسك
❖ بيع فلوسي + العدد ↼ للأستبدال"""
    elif call.data == "a5":
        text = """⚘ اليـوتيوب

تفعيل اليوتيوب 
تعطيل اليوتيوب

❋ البـحث عن اغنية ↓

بحث اسم الاغنية

يوت اسم الاغنية
⚘ الساوند كلاود ( قريبًا )

تفعيل الساوند 
تعطيل الساوند 

❋ البـحث عن اغنية ↓

رابط الاغنية"""
    elif call.data == "a6":
        text = """✜ اوامر البنك

⌯ انشاء حساب بنكي  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ مسح حساب بنكي  ↢ تلغي حسابك البنكي

⌯ تحويل ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ حسابي  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ فلوسي ↢ يعلمك كم فلوسك

⌯ راتب ↢ يعطيك راتبك كل ٢٠ دقيقة

⌯ بخشيش ↢ يعطيك بخشيش كل ١٠ دقايق

⌯ زرف ↢ تزرف فلوس اشخاص كل ١٠ دقايق

⌯ استثمار ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜

⌯ حظ ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك

⌯ مضاربه ↢ تضارب بأي مبلغ تبيه والنسبة من ٩٠٪؜ الى -٩٠٪؜ انت وحظك

⌯ توب الفلوس ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ توب الحراميه ↢ يطلع لك اكثر ناس زرفوا"""

    elif call.data == "a7":
        text = """للاستفسار - @cEbot

🍰 ⌯ رفع ↣ ↢ تنزيل كيكه
🍯 ⌯ رفع ↣ ↢ تنزيل عسل
💩 ⌯ رفع ↣ ↢ تنزيل زق
🦓 ⌯ رفع ↣ ↢ تنزيل حمار
🐄 ⌯ رفع ↣ ↢ تنزيل بقره
🐩 ⌯ رفع ↣ ↢ تنزيل كلب
🐒 ⌯ رفع ↣ ↢ تنزيل قرد
🐐 ⌯ رفع ↣ ↢ تنزيل تيس
🐂 ⌯ رفع ↣ ↢ تنزيل ثور
🏅 ⌯ رفع ↣ ↢ تنزيل باعوص
🐓 ⌯ رفع ↣ ↢ تنزيل دجاجه
🧱 ⌯ رفع ↣ ↢ تنزيل هطف
🔫 ⌯ رفع ↣ ↢ تنزيل صياد
🐏 ⌯ رفع ↣ ↢ تنزيل خاروف
❤️ ⌯ رفع لقلبي ↣ ↢ تنزيل من قلبي

⌯ قائمة الكيك
⌯ قائمة العسل
⌯ قائمة الزق
⌯ قائمة الحمير
⌯ قائمة البقر
⌯ قائمة الكلاب
⌯ قائمة القرود
⌯ قائمة التيس
⌯ قائمة الثور
⌯ قائمة البواعيص
⌯ قائمة الدجاج
⌯ قائمة الهطوف
⌯ قائمة الصيادين
⌯ قائمة الخرفان"""
    keyboard =InlineKeyboardMarkup(row_width=2)
    A = InlineKeyboardButton("م1", callback_data="a1")
    S = InlineKeyboardButton("م2", callback_data="a2")
    D = InlineKeyboardButton("م3", callback_data="a3")
    F = InlineKeyboardButton("الالعاب", callback_data="a4")
    G = InlineKeyboardButton("اليوتيوب", callback_data="a5")
    H = InlineKeyboardButton("البنك", callback_data="a6")
    J = InlineKeyboardButton("التسلية", callback_data="a7")
    keyboard.add(A, S, D, F, G, H, J)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == "الاوامر")
def handle_text(message):
    chat_id = message.chat.id
    text = '''⇜ اهلين فيك باوامر البوت

للاستفسار - @cEbot'''
    keyboard = InlineKeyboardMarkup(row_width=2)
    A = InlineKeyboardButton("م1", callback_data="a1")
    S = InlineKeyboardButton("م2", callback_data="a2")
    D = InlineKeyboardButton("م3", callback_data="a3")
    F = InlineKeyboardButton("الالعاب", callback_data="a4")
    G = InlineKeyboardButton("اليوتيوب", callback_data="a5")
    H = InlineKeyboardButton("البنك", callback_data="a6")
    J = InlineKeyboardButton("التسلية", callback_data="a7")
    keyboard.add(A, S, D, F, G, H, J)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)

print('bot run :) enjoy')
print(S)
bot.infinity_polling()
