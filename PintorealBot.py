import os , logging , requests ,telegram
from telegram import InlineKeyboardButton,InlineKeyboardMarkup , KeyboardButton , ReplyKeyboardMarkup , Update
from telegram.ext import PicklePersistence,Application,CallbackQueryHandler,CommandHandler,MessageHandler,ContextTypes, ConversationHandler,CallbackContext, filters
import re

# os.environ['HTTP_PROXY'] = '127.0.0.1:9119'
# os.environ['HTTPS_PROXY'] = '127.0.0.1:9119'
# os.environ['SOCKS_PROXY'] = '127.0.0.1:9150'
token = "6217084586:AAEwIqqQjfSyKlxxmTGUSWrCoJyhV7q_wko"
bot = telegram.Bot(token=token)

logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO)
logger = logging.getLogger(__name__)

# For Data

END = ConversationHandler.END

# callback datas 

( SEFR_TA_SAD,
  TERM_1,
  TERM_2,
  TERM_3,
  FULL_SEFR_TA_SAD,
  BACK_TO_SHOW_PACKAGES,
  CHESHM_3ROKH,
  BINI_3ROKH,
  BINI_PIR,
  LAB_ASALI,
  LAB_ALMASI,
  BUY,
  BACK,
  BINI,
  LAB,
  TONAZH_MOO_SIAH,
  TONAZH_MOO_GHAHVEI,
  MOO_TAYLOR,
  MOO_SHINION,
  MOO_PESAR,
  SELECTION,
  TAK_CHEHRE,
  POOST,
  STARTER,
  PISHRAFTE,
  SHOW_PACKAGES,
  ABOUT_US,
  HOME,
  SELECT_PACKAGE,
  START_OVER,
  BUY_SEFR_TA_SAD,
  ADMIN_RESPONSE,
  FORWARD_TO_ADMIN,
  REJECT,
  PACKAGE,
  PRICE,
  URL,
  STOP,
  PRICE_T)=map(chr,range(0,39))
  
( BUY_TERM_1,
  BUY_TERM2,
  BUY_TERM3,
  BUY_CHESHM_3ROKH,
  BUY_BINI_PIR,
  BUY_BINI_3ROKH,
  BUY_LAB_ASALI,
  BUY_LAB_ALMASI,
  BUY_BINI,
  BUY_LAB,
  BUY_TONAZH_MOO_GHAHVEI,
  BUY_TONAZH_MOO_SIAH,
  BUY_MOO_TAYLOR,
  BUY_MOO_SHINION,
  BUY_MOO_PESAR,
  BUY_TAK_CHEHRE,
  BUY_POOST,
  BUY_STARTER,
  BUY_PISHRAFTE,
  LINKS,
  ACCEPT,
  SHOW_LINKS,
  USER_ID,
  CODE,
  ID,
  ZEIN,
  BUY_ZEIN,) = map(chr,range(0,27))


# PAGES :
#   start = line 92
#   start_over = 129
#   term_1_home = 164
#   term_2_home = 206
#   term_3_home = 249
#   cheshm_3rokh = 305
#   bini = 335
#   bini-3rokh = 363
#   bini_pir = 390
#   lab = 424
#   lab_almasi = 453
#   lab_asali = 484
#   tonazh_moo_ghahvei = 520
#   tonazh_moo_siah = 552
#   moo_taylor = 588
#   moo_shinion = 620
#   moo_pesar = 650
#   starter_home = 680
#   pishrafte_home = 697
#   show_packages = 715
#   sefr_ta_sad_home 750
#   tak_chehre_home = 819
#   poost_package_home = 854


async def start(update:Update, context: ContextTypes.DEFAULT_TYPE) -> str :
    keyboard = [
        [
          InlineKeyboardButton("فهرست پکیج ",callback_data=str(SHOW_PACKAGES))
        ],
        [
          InlineKeyboardButton("پشتیبانی",url="https://t.me/DadeCrimson"),
          InlineKeyboardButton("پشتیبانی ۲",url="https://t.me/pintoreal"),
          InlineKeyboardButton("خروج", callback_data=str(END))
        ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = """
    سلام هنرجوی عزیز✨ 
خیلی خوش حالیم که تیم آموزشی ما رو انتخاب کردی 😍🌱
 
🔸از بخش فهرست پکیج میتونی لیست دوره هامونو ببینی✨  

🔸برای ثبت نام و اطلاعات راجع به هر دوره روی اسمش کلیک کن و مراحل ثبت نام رو دنبال کن✨

🔸اگر مشکلی در اجرای ربات پیدا کردی و یا دکمه ای رو زدی کار نکرد میتونی دکمه ***** برگشت ***** رو بزنی و یا با نوشتن /start ربات رو دوباره اجرا کنی

🔸برای ارتباط با ادمین ها هم میتونی از  طریق دکمه های پشتیبانی اقدام کنی🍓
"""
    user = update.message.from_user
    context.user_data[ID] = user.id
    logger.info("user %s start the bot",user.first_name)
    chat_id = update.message.chat_id
    await update.message.reply_text(text=text,reply_markup=reply_markup)
    
      
      
    return HOME

 
async def start_over(update:Update, context: ContextTypes.DEFAULT_TYPE) -> str :
  
  keyboard = [
      [
        InlineKeyboardButton("فهرست پکیج ",callback_data=str(SHOW_PACKAGES))
      ],
      [
        InlineKeyboardButton("پشتیبانی",url="https://t.me/DadeCrimson"),
        InlineKeyboardButton("پشتیبانی ۲",url="https://t.me/pintoreal"),
        InlineKeyboardButton("خروج", callback_data=str(END))
      ]  
  ]
  query = update.callback_query
     
  text = """
    سلام هنرجوی عزیز✨ 
خیلی خوش حالیم که تیم آموزشی ما رو انتخاب کردی 😍🌱
 
🔸از بخش فهرست پکیج میتونی لیست دوره هامونو ببینی✨  

🔸برای ثبت نام و اطلاعات راجع به هر دوره روی اسمش کلیک کن و مراحل ثبت نام رو دنبال کن✨

🔸اگر مشکلی در اجرای ربات پیدا کردی و یا دکمه ای رو زدی کار نکرد میتونی دکمه ***** برگشت ***** رو بزنی و یا با نوشتن /start ربات رو دوباره اجرا کنی

🔸برای ارتباط با ادمین ها هم میتونی از  طریق دکمه های پشتیبانی اقدام کنی🍓
  """   
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.answer()
  await query.message.reply_text(text=text,reply_markup=reply_markup)
      
      
  return HOME

async def term_1_home(update:Update, context: ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [[InlineKeyboardButton("ثبت نام ترم اول",callback_data="BUY")],
    [InlineKeyboardButton("چشم سه رخ",callback_data=str(CHESHM_3ROKH))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
  ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  
  text = '''
  ترم اول صفر تا صد 1⃣

جلسات آموزش :
_آشنایی با روشهای رنگامیزی
_انواع فشار دست 
_ایجاد تنالیته 
_تناژ های مختلف پوست 
_حجمدهی 
_روشهای انقال طرح و کشیدن طراحی اولیه 
_آموزش تخصصی 3 رنگ عنبیه 
_چشم دختر 
_چشم خیس 
_چشم پیر 
_چشم سه رخ 
_ابرو ، مژه و بافت پوست 
به همراه آپدیت و 3 ماه رفع اشکال رایگان. 
. 
. 
تو این ترم مباحث پایه مدادرنگی و  انواع چشم رو یاد میگیرید  
با بافتها و تنهاژ های پوست آشنا میشید، ترکیب و تشخیص رنگ رو یاد میگیرید
ینی هر چیزی که برای استارت نقاشی لازمه توی این ترم هست✨

قیمت : 600,000 تومان
  
  '''
  
  query = update.callback_query
  await query.answer()
  await update.callback_query.message.reply_photo(photo="term1.jpg",caption=text,reply_markup=reply_markup)
  
  return TERM_1

async def term_2_home(update:Update , context:ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [[InlineKeyboardButton("ثبت نام ترم دوم", callback_data=str(BUY_TERM2))],
    [InlineKeyboardButton(text="بینی ساده",callback_data=str(BINI)),InlineKeyboardButton("لب ساده",callback_data=str(LAB))],
    [InlineKeyboardButton(text="بینی سه رخ",callback_data=str(BINI_3ROKH)),InlineKeyboardButton(text="لب الماسی",callback_data=str(LAB_ALMASI))],
    [InlineKeyboardButton(text="بینی پیر",callback_data=str(BINI_PIR)),InlineKeyboardButton(text="لب عسلی",callback_data=str(LAB_ASALI))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
  ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ترم دوم آموزش صفرتاصد2️⃣

جلسات:
-بینی تمام رخ 
-بینی سه رخ 
-لب الماس
-لب عسلی
-بینی پیر تمام‌رخ
-لب خندان
...
مباحث:
-سایه زنی و فرم‌دهی بینی 
-آموزش نقاشی الماس 
-بافت انواع لب 
-نحوه نقاشی و سایه زنی دندان 
-جنسیت سازی عسل 
-پوست پیر و زمخت 
...

تو این ترم بیشتر روی دو مبحث مهم فرم دهی و بافت فوکوس کردیم و از اجزای صورت بینی و لب به طور مفصل با مدل های جذاب آموزش داده شده 🌙

...

قیمت :680,000تومان🔥😱
  '''
  
  await update.callback_query.answer()
  await update.callback_query.message.reply_photo(photo="term2.jpg",caption=text,reply_markup=reply_markup)
  
  return TERM_2

async def term_3_home(update:Update , context: ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [[InlineKeyboardButton("ثبت نام ترم سوم",callback_data=str(BUY_TERM3))],
    [InlineKeyboardButton( "تناژ مو سیاه", callback_data=str(TONAZH_MOO_SIAH)),InlineKeyboardButton("تناژ مو قهوه ای",callback_data=str(TONAZH_MOO_GHAHVEI))],
    [InlineKeyboardButton("مو تیلور", callback_data=str(MOO_TAYLOR))],
    [InlineKeyboardButton("مو شینیون", callback_data=str(MOO_SHINION)),InlineKeyboardButton("مو پسر", callback_data=str(MOO_PESAR))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
  ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ترم سوم آموزش صفرتاصد3️⃣

جلسات: 
دو تناژ مو(پر کلاغی و قهوه‌ای)
موی لخت و کوتاه تیلور 
مدل موی شینیون شده بلوند 
موی مردانه کوتاه 
گوش 
ته ریش 
ریش سفید 
مدل موی فانتزی

...


مباحث:
تناژ های مختلف مو
نحوه نقاشی دسته و تار موها 
نحوه کشیدن موی بلوند و لخت 
ترکیب رنگ موی بلوند 
فرم موی شینیون شده 
ترکیب رنگ موی فانتزی 
موی مردانه کوتاه 
فرم‌دهی‌ و سایه زنی گوش 
نحوه ایجاد ته ریش و ریشِ سفید 


...

این ترم تمرکزش بیشتر روی تناژ های مختلف مو،اندازه های مختلفش و ترکیب رنگشونه؛
در کنارش انواع ریش هم آموزش داده میشه.

این ترم شامل نه جلسه است که تا جلسه ششم تکمیله و سه جلسه آخر در حال تکمیله🍓


قیمت : 980,000تومان
  
  '''
  query = update.callback_query
  await query.answer()
  await update.callback_query.message.reply_photo(photo="term3.jpg",caption=text,reply_markup=reply_markup)

  return TERM_3



async def cheshm_3rokh(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام چشم سه رح", callback_data=str(BUY_CHESHM_3ROKH))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''آموزش نقاشی صفر تاصد چشم سه رخ 👇🏻
مباحث آموزشی:
عنبیه طوسی،آبی 
آموزش تخصصی مژه✨ 
آموزش تخصصی پوستِ اطراف چشم 
آموزش لثه چشم 
آموزش ایجاد روشنائی‌ها
***
تو این مدل بیشتر به آموزش مژه ها و پوست اطراف چشم پرداخته شده.

زمان آموزش :3:00 (3 ساعت) 

هزینه پکیج : 🔥 170,000 تومان 🔥
'''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="cheshme3rokh2.jpg",caption="عکس مدل")
  await query.message.reply_photo(photo="cheshme3rokh.jpg",reply_markup=reply_markup,caption=text)
  return CHESHM_3ROKH

async def bini(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام بینی", callback_data=str(BUY_BINI))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''آموزش تخصصی نقاشی بینی 
مباحث 👇🏻
سایه زنی و فرم‌دهی درست بینی 
بافتدهی سایه اکلیلی 
***

این جلسه بهت کمک میکنه تو مبحث فرم‌دهی کاملا پیشرفت کنی و بتونی سایه‌هات رو درست کنار هم قرار بدی .

زمان آموزش : یک ساعت و نیم

هزینه آموزش:  🔥 180,000 تومن 🔥
'''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="bini.jpg")
  await query.message.reply_photo(photo="bini2.jpg",reply_markup=reply_markup,caption=text)
  return BINI
  
async def bini_3rokh(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام بینی سه رخ", callback_data=str(BUY_BINI_3ROKH))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''آموزش بینی سه رخ 
سایه‌زنی‌و ایجاد فرم درست بینی 
آموزش بافت پرزدار 
***
با این آموزش هم فرم‌دهی بینی رو یاد میگیری هم ایجاد پرز‌های روی  پوست رو.

زمان آموزش:1:20 (یک ساعت و 20دقیقه)
 
هزینه آموزش: 🔥 170,000 تومان 🔥
'''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="bini_3rokh.jpg")
  await query.message.reply_photo(photo="bini_3rokh2.jpg",reply_markup=reply_markup,caption=text)
  return BINI_3ROKH

  
async def bini_pir(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام بینی پیر", callback_data=str(BUY_BINI_PIR))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  👈آموزش بینی پیر و زمخت 
مباحثِ مهمِ این مدل:
.فرم‌دهی
.سایه‌زنی
.بافتِ پرتقالی
.زمختیِ پوستِ پیر
.بافت و پف زیر‌چشم

...
این مدل بهت کمک میکنه بتونی از پس مدل های سخت بر بیای و بافت پوست پیر رو کامل با دیدنش یاد میگیری .


زمان:5 ساعت 
قیمت : 200,000 تومان
  
  '''
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="bini_pir.jpg")
  await query.message.reply_photo(photo="bini_pir2.jpg",caption=text,reply_markup=reply_markup)
  return BINI_PIR


 
async def lab(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام لب", callback_data=str(BUY_LAB))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ⬅️مباحث مهم این مدل:
.لثه
.سایه‌زنی دندان‌‌ها
.ترکیب‌رنگ لب
.بافت‌لب
...
این یه مدل ساده لبِ که با دیدنش بافت لب طبیعی رو پر کنار نحوه شایه زنی دندون ها یاد میگیری.


زمان:دو ساعت و چهل و پنج دقیقه 🕐
قیمت:150,000 تومان🔥
  '''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="lab.jpg",caption=text,reply_markup=reply_markup)
  return LAB

 
async def lab_almasi(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام لب الماسی", callback_data=str(BUY_LAB_ALMASI))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  مباحث👇🏻
آموزش بافت لب 
آموزش الماس
آموزش دندون 
آموزش ایجاد برق روی لب و تناژ رژ لب قرمز 

***


این مدل ترکیبی از کلی مباث مختلفه،الماس ،رژ لب،دندون ...هر کدوم از اینا میتونه یه جلسه مجزا باشه اما فکرشو بکن همه رو تو یه جلسه یاد میگیری😍🍓🪽

زمان آموزش : 5ساعت و 10دقیقه
قیمت : 200,000 تومان
'''
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="lab_almasi2.jpg")
  await query.message.reply_photo(photo="lab_almasi.jpg",caption=text,reply_markup=reply_markup)
  return LAB_ALMASI

 
async def lab_asali(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام لب عسلی", callback_data=str(BUY_LAB_ASALI))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
⬅️آموزش لب عسلی 
مباحث:
-جنسیت سازی عسل 
-بافت لب 
-بافت زبان 
-ایجاد روشنایی و درخشنگی 

...

این آموزش ترکیبی از چند مبحث مهمِ،جنسیت سازی عسل که خیلی پرطرفداره ، آموزش بافت لب و زبان و همینطور شفافیت و درخشندگی ⚡️





زمان : 4ساعت 34 دقیقه
قیمت :  170,000 تومان  
  '''
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="lab_asali.jpg")
  await query.message.reply_photo(photo="lab_asali2.jpg",caption=text,reply_markup=reply_markup)
  return LAB_ASALI



async def tonazh_moo_ghahvei(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton(" ثبت نام تناژ مو قهوه ای", callback_data=str(BUY_TONAZH_MOO_GHAHVEI))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
⬅️مباحث آموزش:
-ترکیب رنگ‌موی قهوه‌ای
-تقسیم‌بندی و تفکیکِ جزئیات

...
اینم آموزش مقدماتی و کاربردی برای رنگ مو با تناژ قهوه ایِ  که خیلی میتونی بهت کمک بکنه برای شروع یاد گرفتن نقاشی مو.

اندازه کار:13×16.5
رنگ‌های مورد استفاده اصلی:
199.263.283.189.187.103

زمان:دو ساعت 
قیمت:150,000 تومان🔥
  '''
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="moo_ghahvei.jpg")
  await query.message.reply_photo(photo="moo_ghahvei2.jpg",caption=text,reply_markup=reply_markup)
  return TONAZH_MOO_GHAHVEI



async def tonazh_moo_siah(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton(" ثبت نام تناژ مو سیاه", callback_data=str(BUY_TONAZH_MOO_SIAH))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ⬅️مباحث آموزش:
-ترکیب‌رنگ‌موی مشکیِ پرکلاغی
-آموزش تقسیم‌بندی دسته‌های مو
-تفکیک جزئیات
-ایجاد تار‌موهای یک سرنازک و دو سرنازک
-نحوه ایجاد تارِموهای ظریف و روشن
...
این یه آموزش کوچیک برای آشنایی تو با تناژ رنگ پر کلاغی و همینطور نحوه ایجاد دسته ها و تار موهاست که خیلی میتونه کاربردی باشه.
▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️
اندازه کار:13×13
رنگ‌های مورد استفاده:
273.199.101.247(p)or347(c)

زمان : ۱ ساعت
قیمت : 150,000 تومان🔥
  

  '''
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="moo_siah.jpg")
  await query.message.reply_photo(photo="moo_siah.jpg",caption=text,reply_markup=reply_markup)
  return TONAZH_MOO_SIAH

 
async def moo_taylor(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام موی تیلور", callback_data=str(BUY_MOO_TAYLOR))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  موی تیلور 
اندازه کار:18×18
رنگ های مورد استفاده:.283.180.132.189.263.283.271.272
.199.178.187.101.273.103.329
مباحث آموزش:
ترکیب رنگ‌موی بور
موی لخت
...
این ترکیب رنگ یکی از مهم ترین ترکیب رنگ هاست و موی لخت و مدل موی کوتاه و چتری تو این ویدئو به طور کامل آموزش داده شده🧡


زمان:3ساعت و چهل دقیقه 
قیمت :290,000 تومان
  '''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="moo_taylor.jpg")
  await query.message.reply_photo(photo="moo_taylor2.jpg",caption=text,reply_markup=reply_markup)
  return MOO_TAYLOR


async def moo_shinion(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام موی شینیون", callback_data=str(BUY_MOO_SHINION))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ⬅️مباحث آموزش:
-ترکیب رنگ موی بلوند 
-حجم دهی موی شنیون شده

...

اندازه کار: A4
رنگ های مورد نیاز: 103.271.273.178.179/380.199
...
یکی از پر طرفدار ترین آموزش ها مدل موی شینیون شده است که یاد میگیری چطوری پیچ و تاب های مو رو ایجاد کنی و یه مبحث تخصصی به حساب میاد .👀

زمان: 3ساعت
قیمت :330,000 تومان🔥
  '''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="moo_shinion.jpg")
  await query.message.reply_photo(photo="moo_shinion2.jpg",caption=text,reply_markup=reply_markup)
  return MOO_SHINION
 
async def moo_pesar(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  keyboard = [
    [InlineKeyboardButton("ثبت نام موی پسر", callback_data=str(BUY_MOO_PESAR))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    

  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = '''
  ⬅️مباحث آموزش:
-ترکیب رنگ موی بلوند 
-حجم دهی موی شنیون شده
...
اندازه کار: A4
رنگ های مورد نیاز: 103.271.273.178.179/380.199
...
خیلی از شما تو کشیدن موی کوتاه مردونه مشکل دارید که با دیدن این آموزش کاملا حل میشه،همینطور نحوه کشیدن گوش هم آموزش داده شده.👀


زمان:دو ساعت و سی و هشت
قیمت:310,000 تومان🔥
  '''

  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="moo_pesar.jpg",caption=text,reply_markup=reply_markup)
  return MOO_PESAR

async def starter_home(update:Update, context: ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))],
    [InlineKeyboardButton("خرید پکیج استارتر",callback_data=str(BUY_STARTER))]
  ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  
  text = '''
  
  تو بخش استارتر این مباحث رو یاد میگیری:✨🪄

1.آشنایی با لوازم مورد نیاز و کاربردشون
2.نحوه گرفتن مداد و حرکت دست 
3.انواع روش های رنگامیزی 
4.آشنایی با فشار دست 
5.ترکیب رنگ و ایجاد تنالیته با استفاده از دو رنگ 
6.تشخیص رنگ 
7.ترکیب رنگ پوست های مختلف (پالت رنگی) 
8.حجم دهی
9.تفکیک خط در نقاشی 
10.دید جزئی نگر 
11.روش های طراحی اولیه 
12.روش های انتقال طرح


قیمت : 890,000 تومان
  '''
  
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="Pishrafte.jpg",caption=text,reply_markup= reply_markup)
  
  return STARTER
  
async def pishrafte_home(update:Update, context: ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))],
    [InlineKeyboardButton("خرید پکیج پیشرفته",callback_data=str(BUY_PISHRAFTE))]
  ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  
  text = '''
  تو بخش پیشرفته انواع بافت های پوست رو یاد میگیری ✨🪄

شامل⬇️
1.بافت صاف و یکدست  
2.بافت کک و مکی 
3.بافت مخملی (کرک‌دار)
4.بافت خیس
5.بافت پرتقالی
6.بافت عسلی
7.بافت خاص (بافت شن روی پوست) 
8.بافت پیر
9.بافت پوست تیره 

تک تک مدلها با دقتُ وسواس انتخاب شدن تا همه نوع پوستی رو بعد از گذروندن این دوره بتونی به راحتی نقاشی کنی😍🍓✨
  

قیمت : ,1,690,000 تومان
  '''
  
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="Pishrafte.jpg",caption=text,reply_markup= reply_markup)
  
  return PISHRAFTE

  
async def show_packages(update : Update ,context : ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("پکیج صفر تا صد نقاشی چهره",callback_data=str(SEFR_TA_SAD))],
    [InlineKeyboardButton("پکیج پوست",callback_data=str(POOST))],
    [InlineKeyboardButton("پکیج تک چهره دختر",callback_data=str(TAK_CHEHRE))],
    [InlineKeyboardButton("پکیج تک چهره زین",callback_data=str(ZEIN))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    
  ]
  context.user_data[START_OVER] = True
  reply_markup = InlineKeyboardMarkup(keyboard)
  query = update.callback_query
  text = '''
  
  🍓فهرست دوره ها:
این لیست دوره های اصلیمونِ ✨

🔶 دوره صفر تا صد نقاشی چهره
(شامل ۳ ترم فشرده از مبتدی تا حرفه ای) 

🔶 پکیج تک چهره دختر
(بیش از 18  ساعت آموزش جزء به جزء یک مدل دختر)

🔶 پکیج تک چهره پسر
(آموزش جزء به جزء ریش و مو یک مدل پسر )

🔶 پکیج پوست
(شامل ۲ بخش استارتر و پیشرفته برای افراد مبتدی تا حرفه ای، مختص یادگیری انواع بافت و تناژ پوست)

برای اطلاعات بیشتر راجع به هر دوره روی اسم دوره کلیک کن✨🪄
  '''
  await query.answer()
  await query.message.reply_text(text=text,reply_markup=reply_markup)
  return SELECT_PACKAGE
  

  
   
  
async def sefr_ta_sad_home(update : Update ,context : ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("خرید پکیج صفر تا صد نقاشی چهره",callback_data=str(BUY_SEFR_TA_SAD))],
    [InlineKeyboardButton("ترم اول",callback_data=str(TERM_1)),
    InlineKeyboardButton("ترم دوم",callback_data=str(TERM_2)),
    InlineKeyboardButton("ترم سوم",callback_data=str(TERM_3))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text_main = '''
  🔥 دوره صفر تا صد نقاشی چهره 🔥

این دوره شامل 3 ترم آموزش مباحث پایه ، اجزای چهره و انواع مو هست. + یک ترم آپدیت رایگان. 
دلیل 3 ترمی بودن دوره اینه که ما مباحث رو خیلی فشرده تر و جامع تر داخل هر ترم دسته بندی کردیم☄️✨

اینجوری نیازی نیست که برای یاد گرفتن مثلا مبحث چشم دو سه ترم آموزش ثبت نام کنی!!! 

 با همین 3 ترم میتونی تمام چیز هایی که برای کشیدن چهره به صورت خیلی حرفه ای لازم هست رو یاد بگیری ، برای ثبت نام هم نیازی به پیش زمینه نیست و شما با هر سطحی میتونی ثبت نام کنی🥰🪄✨

هم میتونی ترم به ترم ثبت نام کنی هم یکجا
حتی بعضی از جلسات رو تکی هم میتونی ثبت نام کنی 😍🌱


قیمت : 2,240,000 تومان
  '''
  text_t1 = '''
  🔥ترم اول🔥

این ترم شامل ۲ بخشِ  
بخش اول برای یادگیری مباحث پایه،
و بخش دوم برای یادگیری هفت تا مدل چشم جذاب🔥

تمام مدل ها جوری انتخاب شدن که شما علاوه بر یادگیری کشیدن انواع چشم و ابرو و مژه، تناژ و بافتهای مختلف پوست رو هم از همین ترم اول کم کم یاد بگیرید.😌🪄✨ 

یکی از آیتم های این ترم( چشم سه رخ ) رو به صورت تک جلسه هم میتونید تهیه کنید🥰🍓
برای ثبت نام 👇🏻


قیمت : ,600,000 تومان

  '''
  text_t2 = '''
  🔥ترم دوم🔥
مخصوص بینی و لب
علاوه بر حجم دهی و بافت پوست و لب،
بافتهایی مثل عسل و الماس، زبان، دندانو لثه رو هم یادمیگیرید. 

حتی به تناژ پوست ها هم دقت کردیم که متنوع باشه! ✨🪄

ترم دوم رو هم میتونی یکجا و هم به صورت تک جلسه ای ثبت نام کنی 🌱✨
  

قیمت : ,680,000 تومان
  '''
  text_t3='''
  💥ترم سوم 💥

مخصوص یادگیری انواع مدل مو در رنگ ها و حالت های مختلف به همراه ریش،گوش و اکسسوری ...

این پکیج ۹ جلسه و در حال تکمیل هستش و قراره مدل های بیشتری بهش اضافه بشه

ترم سوم رو هم میتونی یکجا و هم به صورت تک جلسه ای ثبت نام کنی 🌱✨
  
  
قیمت : ,980,000 تومان
  '''
  
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="sefr_ta_sad.jpg",caption=text_main,reply_markup=reply_markup)
  await query.message.reply_photo(photo="term1.jpg",caption=text_t1,reply_markup=reply_markup)
  await query.message.reply_photo(photo="term2.jpg",caption=text_t2,reply_markup=reply_markup)
  await query.message.reply_photo(photo="term3.jpg",caption=text_t3,reply_markup=reply_markup)
  return SELECTION
  
  
   
async def tak_chehre_home(update : Update ,context : ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("ثبت نام پکیج تک چهره دختر",callback_data=str(BUY_TAK_CHEHRE))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    
  ]
  caption = '''
پکیج تکچهره دختر 
18 ساعت ویدیو آموزش صفر تا صد این مدل زیبا. 
 برای ثبت نام نیاز به پیش زمینه و سطح کارِ متوسط داره تا بتونید راحت از پس جزئیات این مدل بربیاید.
اگر مبتدی هستید و تا به حال تکنیک مدادرنگی سبک هایپررئال کار نکردید، از دوره ی صفر تا صد باید شروع کنید تا از پایه قوی پیش برید.
ارائه پکیج تو کانال تلگرام هستش که به صورت ویدیو های از قبل آماده شده همراه با توضیحات کامل آپلود شدن براتون. 
همراه با 3ماه رفع اشکال که این تایم 3ماهه از اولین تمرینی که میفرستید شروع میشه نه زمان ثبت نام. 
رفع اشکال 3روز در هفته انجام میشه. 
تایم کلاساهم کاملا دست خودتونه چون فیلمهای اموزشی به صورت یکجا در اختیارتون قرار میگیره.

🔥تخفیف ویژه پکیج تکچهره 🔥

قیمت : ,980,000 تومان
'''
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = "متن صفحه اصلی پکیج تک جهره دختر"
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="takchehre.jpg",caption=caption,reply_markup=reply_markup)
  return SELECTION
  
  
  
async def zein_home(update : Update ,context : ContextTypes.DEFAULT_TYPE) -> str :
  keyboard = [
    [InlineKeyboardButton("ثبت نام پکیج تک چهره زین",callback_data=str(BUY_ZEIN))],
    [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    
  ]
  caption = '''
   🔥 پکیج تک چهره زین 🔥
   
   
  👈🏻صفر تا صد آموزش تک‌چهره پسر خیلی کمکت میکنه که از پس ریش ،موی کوتاه و روشن ،مدل موی پسرونه و پوست گردن و صورت بر بیای و خودش میتونه برای تو که آموزش مقدماتی دیدی یه پکیج کامل باشه تا بتونی چهره کامل بکشی 🔥
تمام نکات مهم و کدهای مدادرنگی‌ها روی ویدئو نوشته شده ✨


قیمت : ,975,000 تومان
'''
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = "متن صفحه اصلی پکیج تک جهره زین"
  query = update.callback_query
  await query.answer()
  await query.message.reply_photo(photo="Zein.jpg",caption=caption,reply_markup=reply_markup)
  return SELECTION
  

async def poost_package_home(update : Update ,context : ContextTypes.DEFAULT_TYPE) -> str :
 keyboard = [
   [InlineKeyboardButton("ثبت نام پکیج پوست",callback_data=str(BUY_POOST))],
   [InlineKeyboardButton("پیشرفته",callback_data=str(PISHRAFTE))],
   [InlineKeyboardButton("استارتر",callback_data=str(STARTER))],
   [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
   

 ]
 reply_markup = InlineKeyboardMarkup(keyboard)
 text = '''
 🔥 پکیج پوست 🔥

این پکیج شامل دو بخش استارتر و پیشرفته ست. 
بخش استارتر برای یادگیری مباحث پایه نقاشی پوست مثل ترکیب رنگها و تشخیص رنگ و کلی مباحث کلیدی دیگه مثل دید جزئی نگر و... 

بخش پیشرفته هم آموزش 9 مدل پوست با بافتها و تناژ های مختلف... 😍🍓

اگه قبلا نقاشی چهره کار کردی و میخوای که کارات بافت هایپررئال تری داشته باشه 
این دوره مخصوصِ خودته✨🪄
 
قیمت : 2,580,000 تومان
 '''
 query = update.callback_query
 await query.answer()
 await query.message.reply_photo(photo="Pishrafte.jpg",caption=text,reply_markup=reply_markup)
 return SELECTION

# buy_functions :

async def buy_sefr_ta_sad(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "sefr_ta_sad"
  context.user_data[PRICE] = 2240.000
  context.user_data[URL] = ["https://t.me/+RhELuOdUW200M2U0 ","https://t.me/+OML8kGGK_xUwOGFk" ,"https://t.me/+OZLCocS5l0xjZDdk ", "https://t.me/+OldALVtZrpYzNjU0"]
  context.user_data[PRICE_T] = 0
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_tak_chehre(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "tak_chehre"
  context.user_data[PRICE] = 980.000
  context.user_data[PRICE_T] = 0
  context.user_data[URL] = ["https://t.me/+zNjvj8YebyQ5MjU0"]
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_zein(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "Zein_TakChehre"
  context.user_data[PRICE] = 975.000
  context.user_data[PRICE_T] = 0
  context.user_data[URL] = ["https://t.me/+zNjvj8YebyQ5MjU0"]
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_poost(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "poost"
  context.user_data[PRICE] = 2580.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_starter(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "starter"
  context.user_data[PRICE] = 890.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_pishrafte(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "pishrafte"
  context.user_data[PRICE] = 1690.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN




async def buy_term_2(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "term_2"
  context.user_data[PRICE] = 680.000
  context.user_data[PRICE_T] = 0

  context.user_data[URL] = ["https://t.me/+DMM_XeNZlxc1NzY0"]
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN
async def buy_term_1(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "term_1"
  context.user_data[PRICE] = 600.000
  context.user_data[PRICE_T] = 0

  context.user_data[URL] = ["https://t.me/+1buEEob9ZMZiNGY0" ,"https://t.me/+YhaxpPztbBI4MzRk"]
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN
async def buy_term_3(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "term_3"
  context.user_data[PRICE] = 980.000
  context.user_data[PRICE_T] = 0

  context.user_data[URL] = ["https://t.me/+99h5iMpcQgc4ZjE0"]
  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN
#complete forward def later

async def buy_cheshm_3rokh(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "cheshm_3rokh"
  context.user_data[PRICE] = 170.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_bini(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "bini"
  context.user_data[PRICE] = 180.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_bini_pir(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "bini_pir"
  context.user_data[PRICE] = 200.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_bini_3rokh(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "bini_3rokh"
  context.user_data[PRICE] = 170.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_lab(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "lab"
  context.user_data[PRICE] = 150.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_lab_almasi(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "lab_almasi"
  context.user_data[PRICE] = 200.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_lab_asali(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "lab_asali"
  context.user_data[PRICE] = 170.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_tonazh_moo_ghahvei(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "moo_ghahvei"
  context.user_data[PRICE] = 150.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_tonazh_moo_siah(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "moo_siah"
  context.user_data[PRICE] = 150.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_moo_taylor(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "moo_taylor"
  context.user_data[PRICE] = 290.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN

async def buy_moo_shinion(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "moo_shinion"
  context.user_data[PRICE] = 330.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

اگر کد تخفیف دارید میتوانید با ارسال کد از تخفیف بهره مند شوید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  reply_markup = InlineKeyboardMarkup(keyboard)
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


async def buy_moo_pesar(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  context.user_data[PACKAGE] = "moo_pesar"
  context.user_data[PRICE] = 310.000
  context.user_data[PRICE_T] = 0

  await query.answer()
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
   
  text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏
اگر کد تخفیف دارید آن را به صورت حروف بزرگ ارسال کنید و با قیمت تخفیف خورده خریداری کنید.

پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  await query.message.reply_photo(photo="cardnumber.jpg",caption=text,reply_markup=reply_markup)
  return FORWARD_TO_ADMIN


# forward to admin and accept payment proccess :

async def forward_to_admin(update : Update , context : ContextTypes.DEFAULT_TYPE) -> str :
  payment_image = update.message.photo[-1].file_id
  user_name = update.message.from_user.username
  user_id = update.message.from_user.id
  package = context.user_data[PACKAGE]
  price = context.user_data[PRICE]
  context.user_data[ID] = user_id
  package = context.user_data[PACKAGE]
  takhfif = context.user_data[PRICE_T]
  
  reply_text = '''
  فیش ارسالی شما برای ادمین ارسال شد.
منتظر تایید ادمین باشید.🙏
بعد از تأیید , لینک ورود به گروه ها برای شما به صورت خودکار ارسال خواهد شد.
اگر طی ۲۴ ساعت لینکی برای شما ارسال نشد عکس فیش خود را 
به همراه نام و نام خانوادگی و پکیج خریداری شده برای پشتیبانی ارسال نمایید.
از صبر و شکیبایی شما سپاسگزاریم.🧡💛
  '''
  await update.message.reply_text(text=reply_text)
  
  ACCEPT = str(f"accept {user_id} {package}")
  keyboard = [
    [InlineKeyboardButton("تایید فیش",callback_data= ACCEPT)]
  ]  
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  
  
  text = f"فیش ارسال شده از هنرجو : {user_name} \n با شماره ایدی : {user_id} \n برای پکیج : {package}\n با قیمت : {price}\nو یا با قیمت تخفیف خورده : {takhfif}"
  
  
  await bot.forward_message(chat_id = "498359484", from_chat_id=update.message.chat_id,message_id=update.message.message_id)
  
  await bot.send_photo(chat_id="498359484",photo=payment_image,reply_markup=reply_markup,caption=text)
 
  await bot.forward_message(chat_id = "510143481", from_chat_id=update.message.chat_id,message_id=update.message.message_id)
  
  await bot.send_photo(chat_id="510143481",photo=payment_image,reply_markup=reply_markup,caption=text)
  
  return SHOW_LINKS

 
async def code_takhfif(update:Update,context:ContextTypes.DEFAULT_TYPE) -> str :
  codes = ["0T100-1","0T100-2","0T100-3","POOST-1","POOST-2","POOST-3",
           "TKH-1","TKH-2","TKH-3","ZEIN-1","ZEIN-2","ZEIN-3",
           "TRM1-1","TRM1-2","TRM1-3","TRM2-1","TRM2-2","TRM2-3","TRM3-1","TRM3-2","TRM3-3",
           "STARTER-1","STARTER-2","STARTER-3","PISHRAFTE-1","PISHRAFTE-2","PISHRAFTE-3",
           ]
  message = update.message.text
  print(message)
  context.user_data[PRICE_T] = 0
  keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  if message == "0T100-1" or message == "0T100-2" or message == "0T100-3":
    context.user_data[PRICE_T]= context.user_data[PRICE] * 0.44
  elif message == "POOST-1" or message == "POOST-2" or message == "POOST-3":
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.55  
  elif message == "TKH-1" or message == "TKH-2" or message == "TKH-3":
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.70
  elif message == "ZEIN-1" or message == "ZEIN-2" or message == "ZEIN-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.50
  elif message == "TRM1-1" or message == "TRM1-2" or message == "TRM1-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.80
  elif message == "TRM2-1" or message == "TRM2-2" or message == "TRM2-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.80
  elif message == "TRM3-1" or message == "TRM3-2" or message == "TRM3-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.80
  elif message == "STARTER-1" or message == "STARTER-2" or message == "STARTER-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.60
  elif message == "PISHRAFTE-1" or message == "PISHRAFTE-2" or message == "PISHRAFTE-3": 
    context.user_data[PRICE_T] = context.user_data[PRICE] * 0.55

  if context.user_data[PRICE_T] != 0 :
    
    text = f'''
  برای خرید پکیج  » {context.user_data[PACKAGE]}
لطفا مبلغ » {context.user_data[PRICE_T]:.3f} 
به شماره کارت ارسال شده به نام سرکار خانم مریم باقری  واریز نمایید.🙏🙏🙏


پس از واریز , فیش واریزی خود را در همین قسمت بفرستید تا برای ادمین ارسال شود.
پس از تأیید فیش شما توسط ادمین لینک گروه ها به صورت خودکار برای شما ارسال خواهد شد.

از صبر و شکیبایی شما ممنونیم.🧡💛
  '''
  
    await update.message.reply_text(text=text,reply_markup=reply_markup)
    return FORWARD_TO_ADMIN
  else :
    text = "کد تفیف ارسالی مورد تأیید نمیباشد.لطفا توجه داشته باشید که کد تخفیف را با حروف بزرگ ارسال نمایید"
    await update.message.reply_text(text=text,reply_markup=reply_markup)
  
  return FORWARD_TO_ADMIN
  
  
async def button_callback(update:Update,context:ContextTypes.DEFAULT_TYPE) -> str :
  query = update.callback_query
  data = query.data.split()
  user_id = data[1]
  package = data[2]
  print(user_id,package)

  if package == "tak_chehre":
    keyboard = [
      [InlineKeyboardButton("لینک گروه تک چهره",url="https://t.me/+zNjvj8YebyQ5MjU0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "sefr_ta_sad":
    keyboard = [
      [InlineKeyboardButton("لینک گروه ترم اول ",url="https://t.me/+1buEEob9ZMZiNGY0")],
      [InlineKeyboardButton("لینک گروه آپدیت ترم اول ",url="https://t.me/+YhaxpPztbBI4MzRk")],
      [InlineKeyboardButton("لینک گروه ترم دوم ",url="https://t.me/+DMM_XeNZlxc1NzY0")],
      [InlineKeyboardButton("لینک گروه ترم سوم ",url="https://t.me/+99h5iMpcQgc4ZjE0")],
      [InlineKeyboardButton("بارگشت",callback_data=str(BACK))]
    ]
  elif package =="Zein_TakChehre":
    keyboard = [
      [InlineKeyboardButton("لینک گروه تک چهره زین ",url="https://t.me/+otiOts5uoNA5OTA8")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "term_1":
    keyboard = [
      [InlineKeyboardButton("لینک گروه آپدیت ترم اول ",url="https://t.me/+1buEEob9ZMZiNGY0")],
      [InlineKeyboardButton("لینک گروه ترم اول ",url="https://t.me/+YhaxpPztbBI4MzRk")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "term_2":
    keyboard = [
      [InlineKeyboardButton("لینک گروه ترم دوم ",url="https://t.me/+DMM_XeNZlxc1NzY0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "term_3":
    keyboard = [
      [InlineKeyboardButton("لینک گروه ترم سوم ",url="https://t.me/+99h5iMpcQgc4ZjE0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "cheshm_3rokh":
    keyboard = [
      [InlineKeyboardButton("لینک گروه جشم سه رخ ",url="https://t.me/+HdHDLoerKTZlNjg8")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "bini":
    keyboard = [
      [InlineKeyboardButton("لینک گروه بینی تمام رخ ",url="https://t.me/+eGoKoKWLsSUwYmE8")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "bini_3rokh":
    keyboard = [
      [InlineKeyboardButton("لینک گروه بینی سه رخ ",url="https://t.me/+kYwuy2X4Y185NDFk")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "bini_pir":
    keyboard = [
      [InlineKeyboardButton("لینک گروه بینی پیر ",url="https://t.me/+SGH5EQkExaliZDY0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "lab_asali":
    keyboard = [
      [InlineKeyboardButton("لینک گروه لب عسلی ",url="https://t.me/+UupKG9E-kME2OTNk")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "lab_almasi":
    keyboard = [
      [InlineKeyboardButton("لینک گروه لب الماسی ",url="https://t.me/+Ih5LQ93iofw0YjU0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "lab":
    keyboard = [
      [InlineKeyboardButton("لینک گروه لب خندان ",url="https://t.me/+SSzHyF-XdYYxMWRk")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "starter":
    keyboard = [
      [InlineKeyboardButton("لینک گروه استارتر",url="https://t.me/+fcvSvAxfGYA5ODk0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "pishrafte":
    keyboard = [
      [InlineKeyboardButton("لینک گروه پیشرفته ",url="https://t.me/+IwMGEazEyVdlNjQ0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
  elif package == "poost":
    keyboard = [
      [InlineKeyboardButton("لینک گروه استارتر",url="https://t.me/+fcvSvAxfGYA5ODk0")],
      [InlineKeyboardButton("لینک گروه پیشرفته ",url="https://t.me/+IwMGEazEyVdlNjQ0")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]  
  else:
    keyboard = [
      [InlineKeyboardButton("لینک گروه ",url="")],
      [InlineKeyboardButton("بازگشت",callback_data=str(BACK))]
    ]
          
    

    
  reply_markup = InlineKeyboardMarkup(keyboard)
  if data[0] == "accept":
    await query.answer("خرید پذیرفته شد")
    await bot.send_message(chat_id=user_id,text="فیش ارسالی شما با موفقیت توسط ادمین تأیید شد و لینک های گروه ها به صورت خودکار برای شما ارسال خواهد شد\nممنون از اعتماد و خرید شما\nدر صورتی که میخواهید دوباره از ربات استفاده کنید کلمه /start را ارسال کنید.",reply_markup=reply_markup)
    return SHOW_LINKS
  else :  
    keyboard = [[InlineKeyboardButton("بازگشت",callback_data=str(BACK))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await bot.send_message(chat_id=user_id,text="فیش ارسالی شما توسط ادمین تأیید نشد.لطفا با ارسال /start و تماس با پشتیبانی اطلاعات لازم را دریافت کنید",reply_markup=reply_markup) 
  

async def back_lo_list(update:Update , context : ContextTypes.DEFAULT_TYPE) -> str :
  
  await show_packages(update,context)
  
  return SHOW_PACKAGES


async def back_to_term_1(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer()
  await term_1_home(update,context)
  return TERM_1
async def back_to_term_2(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer()
  await term_2_home(update,context)
  return TERM_2
async def back_to_term_3(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer()
  await term_3_home(update,context)
  return TERM_3
async def back_to_poost_package(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer()
  await poost_package_home(update,context)
  return SELECTION



async def back_to_sefr_ta_sad(update:Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer()
  await sefr_ta_sad_home(update,context)
  return SELECTION


  
async def stop(update : Update,context : ContextTypes.DEFAULT_TYPE) -> str:
  query = update.callback_query
  await query.answer("restart")
  await query.message.reply_text("please send /start again to restart bot")
  return HOME

async def back_to_show_packages(update:Update ,context : ContextTypes.DEFAULT_TYPE)-> str:
  query = update.callback_query
  await query.answer()
  await show_packages(update,context)
  return SHOW_PACKAGES
    
async def about_us(update:Update , context:ContextTypes.DEFAULT_TYPE)-> str :
  query = update.callback_query
  await query.answer()
  await query.message.reply_text("FELAN HICHI")
  return HOME
  
 
  
def main() -> None:
  
  application = Application.builder().token(token).build() 
   
  #  buy functions left
  sefr_ta_sad_package_conv = ConversationHandler(entry_points=[CallbackQueryHandler(sefr_ta_sad_home, pattern= "^" + str(SEFR_TA_SAD) + "$")],
                                                  states= { SELECTION : [CallbackQueryHandler(term_1_home , pattern="^" + str(TERM_1) + "$"),
                                                                         CallbackQueryHandler(term_2_home , pattern="^" + str(TERM_2) + "$"),
                                                                         CallbackQueryHandler(term_3_home , pattern="^" + str(TERM_3) + "$"),
                                                                         CallbackQueryHandler(buy_sefr_ta_sad , pattern="^" + str(BUY_SEFR_TA_SAD) + "$"),
                                                                         CallbackQueryHandler(back_to_show_packages , pattern="^" + str(BACK) + "$")] ,
                                                            FORWARD_TO_ADMIN : [MessageHandler(filters=filters.PHOTO ,callback= forward_to_admin),
                                                                                MessageHandler(filters=filters.TEXT,callback=code_takhfif),
                                                                                CallbackQueryHandler(sefr_ta_sad_home,pattern="^" +str(BACK) + "$"),
                                                                                ],
                                                            TERM_1 : [CallbackQueryHandler(cheshm_3rokh,pattern="^"+str(CHESHM_3ROKH)+ "$"),
                                                                      CallbackQueryHandler(buy_term_1,pattern="BUY"),
                                                                      CallbackQueryHandler(back_to_sefr_ta_sad,pattern="^"+str(BACK)+ "$")
                                                                      ],
                                                            CHESHM_3ROKH : [CallbackQueryHandler(buy_cheshm_3rokh,pattern= "^" + str(BUY_CHESHM_3ROKH) + "$"),
                                                                          CallbackQueryHandler(back_to_term_1,pattern="^" + str(BACK) + "$")], 
                                                            TERM_2 : [CallbackQueryHandler(bini,pattern="^"+str(BINI)+ "$"),
                                                                      CallbackQueryHandler(lab,pattern="^"+str(LAB)+ "$"),
                                                                      CallbackQueryHandler(bini_pir,pattern="^" + str(BINI_PIR) + "$"),
                                                                      CallbackQueryHandler(bini_3rokh,pattern="^" + str(BINI_3ROKH) + "$"),
                                                                      CallbackQueryHandler(lab_almasi,pattern="^"+str(LAB_ALMASI)+ "$"),
                                                                      CallbackQueryHandler(lab_asali,pattern="^"+str(LAB_ASALI)+ "$"),
                                                                      CallbackQueryHandler(buy_term_2,pattern="^"+str(BUY_TERM2)+ "$"),
                                                                      CallbackQueryHandler(back_to_sefr_ta_sad,pattern="^"+str(BACK)+ "$")
                                                                      ],
                                                            BINI : [CallbackQueryHandler(buy_bini,pattern= "^" + str(BUY_BINI) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")], 
                                                            BINI_3ROKH : [CallbackQueryHandler(buy_bini_3rokh,pattern= "^" + str(BUY_BINI_3ROKH) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")], 
                                                            BINI_PIR : [CallbackQueryHandler(buy_bini_pir,pattern= "^" + str(BUY_BINI_PIR) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")], 
                                                            
                                                            LAB_ASALI : [CallbackQueryHandler(buy_lab_asali,pattern= "^" + str(BUY_LAB_ASALI) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")],
                                                             
                                                            LAB_ALMASI : [CallbackQueryHandler(buy_lab_almasi,pattern= "^" + str(BUY_LAB_ALMASI) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")],
                                                             
                                                            LAB : [CallbackQueryHandler(buy_lab,pattern= "^" + str(BUY_LAB) + "$"),
                                                                          CallbackQueryHandler(back_to_term_2,pattern="^" + str(BACK) + "$")],
                                                            TERM_3 : [CallbackQueryHandler(tonazh_moo_siah,pattern="^"+str(TONAZH_MOO_SIAH)+ "$"),
                                                                      CallbackQueryHandler(tonazh_moo_ghahvei,pattern="^" + str(TONAZH_MOO_GHAHVEI) + "$"),
                                                                      CallbackQueryHandler(moo_taylor,pattern="^"+str(MOO_TAYLOR)+ "$"),
                                                                      CallbackQueryHandler(moo_shinion,pattern="^"+str(MOO_SHINION)+ "$"),
                                                                      CallbackQueryHandler(moo_pesar,pattern="^"+str(MOO_PESAR)+ "$"),
                                                                      CallbackQueryHandler(buy_term_3,pattern="^"+str(BUY_TERM3)+ "$"),
                                                                      CallbackQueryHandler(back_to_sefr_ta_sad,pattern="^"+str(BACK)+ "$")
                                                                      ],
                                                           TONAZH_MOO_SIAH : [CallbackQueryHandler(buy_tonazh_moo_siah,pattern= "^" + str(BUY_TONAZH_MOO_SIAH) + "$"),
                                                                          CallbackQueryHandler(back_to_term_3,pattern="^" + str(BACK) + "$")], 
                                                           TONAZH_MOO_GHAHVEI : [CallbackQueryHandler(buy_tonazh_moo_ghahvei,pattern= "^" + str(BUY_TONAZH_MOO_GHAHVEI) + "$"),
                                                                          CallbackQueryHandler(back_to_term_3,pattern="^" + str(BACK) + "$")], 
                                                           MOO_TAYLOR : [CallbackQueryHandler(buy_moo_taylor,pattern= "^" + str(BUY_MOO_TAYLOR) + "$"),
                                                                          CallbackQueryHandler(back_to_term_3,pattern="^" + str(BACK) + "$")],
                                                           MOO_SHINION : [CallbackQueryHandler(buy_moo_shinion,pattern= "^" + str(BUY_MOO_SHINION) + "$"),
                                                                          CallbackQueryHandler(back_to_term_3,pattern="^" + str(BACK) + "$")], 
                                                           MOO_PESAR : [CallbackQueryHandler(buy_moo_pesar,pattern= "^" + str(BUY_MOO_PESAR) + "$"),
                                                                          CallbackQueryHandler(back_to_term_3,pattern="^" + str(BACK) + "$")], 
                                                           SHOW_LINKS : [CallbackQueryHandler(button_callback),
                                                                         CallbackQueryHandler(sefr_ta_sad_home,pattern="^" + str(BACK) + "$")]

                                                  },
                                                  
                                                  map_to_parent={
                                                    
                                                    STOP:STOP,
                                                    FORWARD_TO_ADMIN:FORWARD_TO_ADMIN,
                                                  },
                                                  fallbacks=[CommandHandler("start",start)],allow_reentry=True,
                                                  )

   
  tak_chehre_package_conv = ConversationHandler(entry_points=[CallbackQueryHandler(tak_chehre_home,pattern="^" + str(TAK_CHEHRE) + "$")],
                                                 states={
                                                   SELECTION : [
                                                     CallbackQueryHandler(buy_tak_chehre,pattern="^" + str(BUY_TAK_CHEHRE) + "$"),
                                                     CallbackQueryHandler(back_to_show_packages,pattern="^" + str(BACK) + "$"),
                                                   ],
                                                   FORWARD_TO_ADMIN : [MessageHandler(filters=filters.PHOTO ,callback= forward_to_admin),
                                                                       MessageHandler(filters=filters.TEXT,callback=code_takhfif),
                                                                       CallbackQueryHandler(tak_chehre_home,pattern="^"+str(BACK) + "$")],
                                                   SHOW_LINKS : [
                                                     CallbackQueryHandler(button_callback),
                                                     CallbackQueryHandler(tak_chehre_home,pattern="^" + str(BACK) + "$")
                                                   ]
                                                    
                                                 },
                                                 fallbacks=[CommandHandler("start",start)],
                                                 map_to_parent={
                                                   STOP : STOP,
                                                   FORWARD_TO_ADMIN: FORWARD_TO_ADMIN
                                                 },
                                                allow_reentry= True,
                                                 )
   
      
  zein_package_conv = ConversationHandler(entry_points=[CallbackQueryHandler(zein_home,pattern="^" + str(ZEIN) + "$")],
                                                 states={
                                                   SELECTION : [
                                                     CallbackQueryHandler(buy_zein,pattern="^" + str(BUY_ZEIN) + "$"),
                                                     CallbackQueryHandler(back_to_show_packages,pattern="^" + str(BACK) + "$"),
                                                   ],
                                                   FORWARD_TO_ADMIN : [MessageHandler(filters=filters.PHOTO ,callback= forward_to_admin),
                                                                       MessageHandler(filters=filters.TEXT,callback=code_takhfif),
                                                                       CallbackQueryHandler(zein_home,pattern="^"+str(BACK) + "$")],
                                                   SHOW_LINKS : [
                                                     CallbackQueryHandler(button_callback),
                                                     CallbackQueryHandler(zein_home,pattern="^" + str(BACK) + "$")
                                                   ]
                                                    
                                                 },
                                                 fallbacks=[CommandHandler("start",start)],
                                                 map_to_parent={
                                                   STOP : STOP,
                                                   FORWARD_TO_ADMIN: FORWARD_TO_ADMIN
                                                 },
                                                allow_reentry= True,
                                                 )
   
   
   
  poost_package_conv = ConversationHandler(entry_points=[CallbackQueryHandler(poost_package_home,pattern="^"+ str(POOST) + "$")],
                                            states={
                                              SELECTION : [
                                                     CallbackQueryHandler(starter_home,pattern="^" + str(STARTER) + "$"),
                                                     CallbackQueryHandler(pishrafte_home,pattern="^" + str(PISHRAFTE) + "$"),
                                                     CallbackQueryHandler(back_to_show_packages,pattern="^" + str(BACK) + "$"),
                                                     CallbackQueryHandler(buy_poost,pattern="^" + str(BUY_POOST) + "$")
                                                   ],
                                              STARTER:[CallbackQueryHandler(buy_starter,pattern= "^" + str(BUY_STARTER) + "$"),
                                                       CallbackQueryHandler(back_to_poost_package,pattern= "^" + str(BACK) + "$")],
                                              PISHRAFTE:[CallbackQueryHandler(buy_pishrafte,pattern= "^" + str(BUY_PISHRAFTE) + "$"),
                                                       CallbackQueryHandler(back_to_poost_package,pattern= "^" + str(BACK) + "$")],
                                              FORWARD_TO_ADMIN : [MessageHandler(filters=filters.PHOTO ,callback= forward_to_admin),
                                                                       MessageHandler(filters=filters.TEXT,callback=code_takhfif),
                                                                       CallbackQueryHandler(poost_package_home,pattern="^"+str(BACK) + "$")],
                                              SHOW_LINKS : [CallbackQueryHandler(button_callback),
                                                            CallbackQueryHandler(poost_package_home,pattern="^" + str(BACK) + "$")],
                                              
                                            },
                                            fallbacks=[CommandHandler("start",start)],
                                            allow_reentry= True,
                                            map_to_parent={
                                              FORWARD_TO_ADMIN:FORWARD_TO_ADMIN,
                                              STOP : STOP
                                            },
                                            )
   
  
  main_conv = ConversationHandler(
     entry_points= [CommandHandler("start",start),poost_package_conv,tak_chehre_package_conv,sefr_ta_sad_package_conv],
     states= {HOME: [CallbackQueryHandler(show_packages , pattern="^" + str(SHOW_PACKAGES) + "$"),
                     CallbackQueryHandler(about_us,pattern="^"+ str(ABOUT_US) + "$"),
                     CallbackQueryHandler(END,pattern="^" + str(END) + "$")
                     ],
              SELECT_PACKAGE : [
                poost_package_conv,
                tak_chehre_package_conv,
                sefr_ta_sad_package_conv,
                zein_package_conv,
                CallbackQueryHandler(start_over,pattern="^" + str(BACK) + "$")
              ],
              FORWARD_TO_ADMIN : [MessageHandler(filters=filters.PHOTO ,callback= forward_to_admin),
                                  MessageHandler(filters=filters.TEXT,callback=code_takhfif),
                                  CallbackQueryHandler(show_packages,pattern="^"+str(BACK) + "$")],
              STOP : [CommandHandler("start",start)],
              SHOW_LINKS : [
                CallbackQueryHandler(button_callback),
                CallbackQueryHandler(show_packages,pattern="^" + str(BACK) + "$")
              ],
              
              
              },
     fallbacks=[CommandHandler("start", start)],
     allow_reentry=True,
    
    
   )
   
  application.add_handler(main_conv)
  application.add_handler(CallbackQueryHandler(show_packages,pattern="^" + str(BACK) + "$"))
  application.add_handler(CallbackQueryHandler(show_packages,pattern="^" + str(SHOW_PACKAGES) + "$"))

  application.run_polling()
  
  
  
if __name__ == "__main__":
  main()
  