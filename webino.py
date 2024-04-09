#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#https://t.me/WebinoSource
try:
    from pyrogram import Client, filters, errors
    from pyrogram.raw import functions, types
    from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    import os, random, asyncio, time
except:
    import os
    os.system('pip3 install pyrogram==2.0.41')
    os.system('pip3 install asyncio')
    import random, asyncio, time
    from pyrogram import Client, filters, errors
    from pyrogram.raw import functions, types
    from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    

#           ---         ---         ---         #
api_id = 23180943
api_hash = 'e89c763a8560766bb99cf6f342aacbef'
bot_token = '6821384034:AAHGkgDF5AvKnpmOZ4idDzWMLnmnAgqtUMw'
bot_admins = [5373443138]
#           ---         ---         ---         #
sleeping = 2 # main sleep time in sec ***[DO NOT EDIT]***
step = None # current step ***[DO NOT EDIT]***
tempClient = dict() # temporary client holder ***[DO NOT EDIT]***
isWorking = list() # Temporary Active Eval Names ***[DO NOT EDIT]***
#           ---         ---         ---         #
fosh = ['علاقه ای زیادی به کص خوری دارم شبو روز منبع تغذیم شده کوسمادرت', 'برو اونور مادر حرمله فعلا رو باید کارامو تموم کنم به وقتش به خفت گیرام دستور اجنتاب میکنم مادرتو یه جا تا سر حد مرگ کتک بزنن', 'با کون میپرم تو صورت مادرت ناموس اشپز مادرتو به بردگی گرفتم فهمیدی یا نه ناموص چایی خشک', 'گوزیدم تو بخت و آخر عاقبت مادرت', 'از روی ناموست ایهام تناسب درست میکنم توی شعرای ملک الشعرا میزارم بعد داخل تست کنکور انسانی مطرحش میکنم', 'ناموستو به عنوان یه عنصر جدید تو جدول تناوبی جایگزاری میکنم', 'برای جشن تولد مادرت دعوت شدم تا درو باز کرد دیدم ننت لخت کلاه تولد گذاشته رو سرش منم کیرمو کردم تو کیک تولد درش اوردم با فندک سر کیرمو روشن کردم مادرت یه ارزو کرد بعدش کیرمو فوت کرد بی غیرت بیا جلو مادرتو بگیر داره خودشو رو کیک تولد ارضا میکنه حرومزاده گشنمه کیک تولد از دست میره الان', 'تولد ننه ی بی غیرتت مبارک', 'از پوست ممه های مادرت اسپیکر درست میکنم فشار بخور', 'میخوام با روح و روان مادرت بازی کنم ببینم تو غیرتت میکشه روح و روان مادرتو از زیر کیر من نجات بدی یا نه', 'رو مغز مادرت تردمیل میزنم', 'ببین مادر اهریمن دست و پای مادرتو می\u200cبندم بعدش مادرتو لخت میکنم در ادامه کلی زنبور عسل رو رها میکنم تا از کص مادرت شهد بگیرن بعد از اینکه اون زنبورا کندو خودشونو درست کردن از کندوش عسل میگیرم و میرم به بابا بی غیرتت عسل میفروشم', 'به مادرت اینقدر آنتی بیوتیک میدم تا سلول های بدنش از کار بیوفتن', 'حتی یه لحظه هم جنده بودن مادرت شک نکردم', 'با پدرت تیم آپ کردم رفتیم مادرتو گاییدیم', 'کیرمو جلو چشمای مادرت تکون میدم مادرتو هیپنوتیزم می کنم', 'مادرت انمی بود و منم اسنایپ پلیر چنان مادرتو فست اسکوپ زدم که بهم گفتن چیتری', 'با چوس گرم و بو دار مادر سرطانیتو شیمی درمانی میکنم', 'تردمیل رو میذارم رو سرعت اخر با چوب ماهی گیری یه دیلدوی خیس اویزون میکنم جلوی چشای مادرت له له بزنه واسش جوری بدووه که تردمیل کم بیاره در مقابل سرعت مادرت', 'نقش هیولا مانند مادرتو به دیوار غار حکاکی میکنم تا نسل های بعدی ببینن مادرت چه هیولای زشتی بوده و از شکل شمایلش حتی وحشی ترین جانور ها هم میترسن و به صخره های بلند کص خواهرت پناه میبرن از ترس پایین نمیان', 'محکم شمشیر جواهر نشانمو فرو میکنم تو کص مادرت تا عصاره ی جاودانگی رو از تو قلبش در بیارم', 'به نام ایزد منان', 'کیر ولادمیر لنین تو کص ننت🇷🇺', 'کیر ژوزف استالین تو کص ننت🇷🇺', 'کیر ولادمیر پوتین تو کص ننت🇷🇺', 'کیر نیکلای دوم تو کص ننت🇷🇺', 'کیر پیتر کبیر تو کص ننت🇷🇺', 'کیر کمال اتاتورک تو کص ننت🇹🇷', 'کیر عبدل العزیز یکم تو کص ننت🇹🇷', 'کیر سلیم دوم تو کص ننت🇹🇷', 'کیر رجب اردوغان تو کص ننت🇹🇷', 'کیر کوروش بزرگ تو کص ننت🇮🇷', 'کیر مهرداد دوم تو کص ننت🇮🇷', 'کیر نادر شاه تو کص ننت🇮🇷', 'کیر رضا شاه پهلوی تو کص ننت🇮🇷', 'کیر ویلیهم دوم تو کص ننت🇩🇪', 'کیر فریدریش چهارم تو کص ننت🇩🇪', 'کیر ادولف هیتلر تو کص ننت🇩🇪', 'کیر فرانک والتر تو کص ننت🇩🇪', 'کیر چارلز سوم تو کص ننت🇬🇧', 'کیر ادوارد هفتم تو کص ننت🇬🇧', 'کیر جرج چهارم تو کص ننت🇬🇧', 'کیر ویلیام چهارم تو کص ننت🇬🇧', 'کیر جرج بوش تو کص ننت🇺🇸', 'کیر دونالد ترامپ تو کص ننت🇺🇸', 'کیر جو بایدن تو کص ننت🇺🇸', 'کیر جرج واشنگتون تو کص ننت🇺🇸', 'کیر ناپلئون بناپارت تو کص ننت🇫🇷', 'کیر شارل دهم تو کص ننت🇫🇷', 'کیر لوئی فیلیپ یکم تو کص ننت🇫🇷', 'کیر امانوئل مکرون تو کص ننت🇫🇷', 'کیر شی جین پینگ تو کص ننت🇨🇳', 'کیر شوان تونگ تو کص ننت🇨🇳', 'کیر چیان لونگ تو کص ننت🇨🇳', 'کیر یه جیان یینگ تو کص ننت🇨🇳', 'کیر امپراتور میجی تو کص ننت🇯🇵', 'کیر ناروهیتو تو کص ننت🇯🇵', 'کیر هیروهیتو تو کص ننت🇯🇵', 'کیر امپراتور تایشو تو کص ننت🇯🇵', 'کیر کیم جونگ اون تو کص ننت🇰🇵', 'کیر کیم ایل سونگ تو کص ننت🇰🇵', 'کیر جومونگ تو کص ننت🇰🇵', 'کیر پادشاه بوجانگ تو کص ننت🇰🇵', 'کیر امپراتور گوچونگ تو کص ننت🇰🇷', 'کیر سجونگ کبیر تو کص ننت🇰🇷', 'کیر سئونگ جونگ تو کص ننت🇰🇷', 'کیر یون سوک یول تو کص ننت🇰🇷', 'کیر همایون شاه تو کص ننت🇮🇳', 'کیر اکبر شاه تو کص ننت🇮🇳', 'کیر ابراهیم لودی تو کص ننت🇮🇳', 'کیر مهاتما گاندی تو کص ننت🇮🇳', 'کیر رام نات کوویند تو کص ننت🇮🇳', 'کیر ژولیوس سزار تو کص ننت🇮🇹', 'کیر تراژان تو کص ننت🇮🇹', 'کیر اومبرتوی دوم تو کص ننت🇮🇹', 'کیر سرجیو ماتارلا تو کص ننت🇮🇹']
#https://t.me/WebinoSource

if not os.path.isdir('sessions') :
    os.mkdir('sessions')


if not os.path.isfile('app.txt') :
    with open('app.txt', 'w', encoding='utf-8') as file:
        file.write(str(api_id) + ' ' + api_hash)


async def randomString() -> str:
    '''Return a random string'''
    size = random.randint(4, 8)
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVLXYZ') for _ in range(size))


async def randomAPP():
    with open('app.txt', 'r', encoding='utf-8') as file:
        file = file.read().split('\n')
        app_id, app_hash = random.choice(file).split()
    return app_id, app_hash


async def accountList() :
    return [myFile.split('.')[0] for myFile in os.listdir('sessions') if os.path.isfile(os.path.join('sessions', myFile))]


async def remainTime(TS):
    TS = time.time() - TS
    if TS < 60 :
        return str(int(TS)) + ' ثانیه'
    else :
        min = int(TS/60)
        sec = TS%60
        return str(int(min)) + ' دقیقه و ' + str(int(sec)) + ' ثانیه'


bot = Client(
    "WebinoSource",
    bot_token = bot_token,
    api_id = api_id,
    api_hash = api_hash
)
#https://t.me/WebinoSource


print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░███░█░▄▄█░▄▄▀██▄██░▄▄▀█▀▄▄▀███░▄▄█▀▄▄▀█░██░█░▄▄▀█▀▄▀█░▄▄
█▄▀░▀▄█░▄▄█░▄▄▀██░▄█░██░█░██░███▄▄▀█░██░█░██░█░▀▀▄█░█▀█░▄▄
██▄█▄██▄▄▄█▄▄▄▄█▄▄▄█▄██▄██▄▄████▄▄▄██▄▄███▄▄▄█▄█▄▄██▄██▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            << @WebinoSource >>
""")
print("Bot running ...")

#           StartCommand            #
@bot.on_message(filters.command(['start', 'cancel']) & filters.private & filters.user(bot_admins))
async def StartResponse(client, message):
    global step, tempClient, isWorking
    try:
        tempClient['client'].disconnect()
    except:
        pass
    tempClient = {}
    step = None
    my_keyboard = [
        [InlineKeyboardButton('افزودن اکانت ➕', callback_data='addAccount'), InlineKeyboardButton('✖️ حذف اکانت', callback_data='removeAccount')],
        [InlineKeyboardButton('عملیات عضویت ⚪️', callback_data='joinEval'), InlineKeyboardButton('⚪️ عملیات لفت', callback_data='leftEval')],
        [InlineKeyboardButton('عملیات ویو پست ⚫️', callback_data='viewEval'), InlineKeyboardButton('⚫️ عملیات ری اکشن پست', callback_data='reActionEval')],
        [InlineKeyboardButton('عملیات نظرسنجی 🔴', callback_data='voteEval') , InlineKeyboardButton('⚠️ اسپم کاربر', callback_data='Spamuser')],
        [InlineKeyboardButton('لیست اکانت ها 📊', callback_data='accountsList'), InlineKeyboardButton('♻️ بررسی اکانت ها', callback_data='checkAccounts')],
        [InlineKeyboardButton('تنظیم زمان 🕠', callback_data='setTime'), InlineKeyboardButton('📛 لغو تمام عملیات ها', callback_data='endAllEvals')],
    ]
    await message.reply('<b>> به منوی اصلی خوش آمدید :\n\n@WebinoSource</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#           StopEval            #
@bot.on_message(filters.regex('^/stop_\w+') & filters.private & filters.user(bot_admins))
async def StopEval(client, message):
    global step, isWorking
    my_keyboard = [
        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
    ]
    evalID = message.text.replace('/stop_', '')
    if evalID in isWorking:
        isWorking.remove(evalID)
        await message.reply(f'<b>عملیات با شناسه {evalID} با موفقیت خاتمه یافت ✅</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
    else:
        await message.reply(f'<b>عملیات موردنظر یافت نشد !</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)



#           callback query            #
@bot.on_callback_query()
async def callbackQueries(client, query):
    global step, bot_admins, tempClient, isWorking, sleeping
    chat_id = query.message.chat.id
    message_id = query.message.id
    data = query.data
    query_id = query.id
    if chat_id in bot_admins:
        if data == 'backToMenu':
            try:
                tempClient['client'].disconnect()
            except:
                pass
            tempClient = {}
            step = None
            my_keyboard = [
                [InlineKeyboardButton('افزودن اکانت ➕', callback_data='addAccount'), InlineKeyboardButton('✖️ حذف اکانت', callback_data='removeAccount')],
                [InlineKeyboardButton('عملیات عضویت ⚪️', callback_data='joinEval'), InlineKeyboardButton('⚪️ عملیات لفت', callback_data='leftEval')],
                [InlineKeyboardButton('عملیات ویو پست ⚫️', callback_data='viewEval'), InlineKeyboardButton('⚫️ عملیات ری اکشن پست', callback_data='reActionEval')],
                [InlineKeyboardButton('عملیات نظرسنجی 🔴', callback_data='voteEval') , InlineKeyboardButton('⚠️ اسپم کاربر', callback_data='Spamuser')],
                [InlineKeyboardButton('لیست اکانت ها 📊', callback_data='accountsList'), InlineKeyboardButton('♻️ بررسی اکانت ها', callback_data='checkAccounts')],
                [InlineKeyboardButton('تنظیم زمان 🕠', callback_data='setTime'), InlineKeyboardButton('📛 لغو تمام عملیات ها', callback_data='endAllEvals')],
            ]
            await bot.edit_message_text(chat_id, message_id, '<b>> به منوی اصلی خوش آمدید :\n\n@WebinoSource</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'endAllEvals':
            step = None
            evalsCount = len(isWorking)
            isWorking = list()
            await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message=f'تمام {evalsCount} عملیات فعال با موفقیت متوقف شدند ✅'))

        elif data == 'addAccount':
            step = 'getPhoneForLogin'
            my_keyboard = [
                [InlineKeyboardButton('🔙', callback_data='backToMenu')],
            ]
            await bot.edit_message_text(chat_id, message_id, '<b>- برای افزودن اکانت لطفا شماره مورد نظرتان را ارسال نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
        
        elif data == 'removeAccount':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'removeAccount'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- برای حذف اکانت لطفا شماره مورد نظرتان را ارسال نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'accountsList':
            if os.path.isfile(f'./accounts.txt'):
                os.unlink(f'./accounts.txt')
            myLen = len((await accountList()))
            if myLen == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد !'))
            else:
                with open(f'./accounts.txt', 'w') as my_file:
                    my_file.write("\n".join(await accountList()))
                try:
                    await bot.send_document(chat_id, f'./accounts.txt', caption=f'تعداد کل اکانت ها : {myLen}')
                    os.unlink(f'./accounts.txt')
                except:
                    pass

        elif data == 'checkAccounts':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                evalID = await randomString()
                isWorking.append(evalID)
                deleted = 0
                error = 0
                free = 0
                cli = None
                TS = time.time()
                AllCount = len(await accountList())
                await bot.edit_message_text(chat_id, message_id, '<b>عملیات بررسی اکانت ها شروع شد ...</b>')
                for session in ((await accountList())):
                    if evalID not in isWorking:
                        break
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    await asyncio.sleep(sleeping)
                    try:
                        api_id2, api_hash2 = await randomAPP()
                        cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                        await cli.connect()
                        await cli.resolve_peer("@durov")
                        await cli.disconnect()
                    except (errors.SessionRevoked, errors.UserDeactivated, errors.AuthKeyUnregistered, errors.UserDeactivatedBan, errors.Unauthorized):
                        try:
                            await cli.disconnect()
                        except:
                            pass
                        os.unlink(f'sessions/{session}.session')
                        deleted += 1
                    except Exception as e:
                        try:
                            await cli.disconnect()
                        except:
                            pass
                        error += 1
                    else:
                        free += 1
                    finally:
                        spendTime = await remainTime(TS)
                        allChecked = deleted + free + error
                        await bot.edit_message_text(chat_id, message_id, f'''♻️ عملیات بررسی اکانت های ربات ...

• کل اکانت ها : {AllCount}
• اکانت های بررسی شده : {allChecked}
• اکانت های سالم : {free}
• سشن های خراب : {deleted}
• خطاهای ناشناخته : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
                try:
                    isWorking.remove(evalID)
                except:
                    pass
                allChecked = deleted + free + error
                spendTime = await remainTime(TS)
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.send_message(chat_id, f'''عملیات بررسی اکانت ها با موفقیت به اتمام رسید ✅

• کل اکانت ها : {AllCount}
• اکانت های بررسی شده : {allChecked}
• اکانت های سالم : {free}
• سشن های خراب : {deleted}
• خطاهای ناشناخته : {error}
• زمان سپری شده : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard))


        elif data == 'setTime':
            step = 'setTime'
            my_keyboard = [
                [InlineKeyboardButton('🔙', callback_data='backToMenu')],
            ]
            await bot.edit_message_text(chat_id, message_id, f'<b>فاصله زمانی فعلی {sleeping} ثانیه میباشد\nدرصورتیکه قصد تغییر فاصله زمانی بین انجام عملیات ها را دارید عدد جدید را ارسال نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'joinEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'joinAccounts'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- برای عملیات عضویت لطفا یوزرنیم یا لینک خصوصی مورد نظرتان را ارسال کنید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'Spamuser':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'Spamuser'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- برای عملیات اسپم کاربر یوزرنیم کاربر را وارد کنید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'leftEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'leaveAccounts'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- برای عملیات لفت لطفا شناسه عددی مورد نظرتان را ارسال کنید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'viewEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'sendViewToPost'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- لطفا لینک پست مورد نظر را ارسال نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'reActionEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'reActionEval'
                my_keyboard = [
                        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                    ]
                await bot.edit_message_text(chat_id, message_id, '<b>لطفا در خط اول لینک پست موردنظر و در خط دوم ایموجی ها با فاصله و در خط سوم تعداد موردنظرتان را وارد نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
        
        elif data == 'voteEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد ❗️'))
            else:
                step = 'voteEval'
                my_keyboard = [
                        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                    ]
                await bot.edit_message_text(chat_id, message_id, '<b>لطفا در خط اول لینک پست و در خط دوم شماره گزینه موردنظرتان را وارد کنید (گزینه ها از 0 شروع میشوند) :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))


#           Text Response            #
@bot.on_message(filters.text & filters.private & filters.user(bot_admins))
async def TextResponse(client, message):
    global step, isWorking, tempClient, api_hash, api_id, sleeping
    chat_id = message.chat.id
    text = message.text
    my_keyboard = [
        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
    ]

#                       Add Account                       #
    if step == 'getPhoneForLogin' and text.replace('+', '').replace(' ', '').replace('-', '').isdigit():
        phone_number = text.replace('+', '').replace(' ', '').replace('-', '')
        if os.path.isfile(f'sessions/{phone_number}.session'):
            await message.reply('<b>این شماره از قبل در پوشه sessions سرور موجود است !</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            tempClient['number'] = phone_number
            tempClient['client'] = Client(f'sessions/{phone_number}', int(api_id), api_hash,"4.8.6","Telegram Desktop","windows")
            await tempClient['client'].connect()
            try :
                tempClient['response'] = await tempClient['client'].send_code(phone_number)
            except (errors.BadRequest, errors.PhoneNumberBanned, errors.PhoneNumberFlood, errors.PhoneNumberInvalid):
                await message.reply('<b>خطایی رخ داد !</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            else:
                step = 'get5DigitsCode'
                await message.reply(f'<b>کد 5 رقمی به شماره {phone_number} ارسال شد ✅</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

    elif step == 'get5DigitsCode' and text.replace(' ', '').isdigit():
        telegram_code = text.replace(' ', '')
        try:
            await tempClient['client'].sign_in(tempClient['number'], tempClient['response'].phone_code_hash, telegram_code)
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>اکانت با موفقیت ثبت شد ✅\nدرصورتیکه قصد افزودن شماره دارید, شماره موردنظر را ارسال کنید و یا از دستور /cancel استفاده نمایید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.PhoneCodeExpired :
            await tempClient['client'].disconnect()
            tempClient = {}
            step = None
            await message.reply('<b>کد ارسال شده منقضی شده است, لطفا عملیات را /cancel کنید و مجدد تلاش کنید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.PhoneCodeInvalid :
            await message.reply('<b>کد وارد شده اشتباه است یا منقضی شده, لطفا از دستور /cancel استفاده نمایید و یا کد درست را ارسال کنید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.BadRequest :
            await message.reply('<b>کد وارد شده اشتباه است یا منقضی شده, لطفا از دستور /cancel استفاده نمایید و یا کد درست را ارسال کنید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.AuthKeyUnregistered :
            await asyncio.sleep(3)
            name = await randomString()
            try:
                await tempClient['client'].sign_up(tempClient['number'], tempClient['response'].phone_code_hash, name)
            except Exception:
                pass
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>اکانت با موفقیت ثبت شد ✅\nدرصورتیکه قصد افزودن شماره دارید, شماره موردنظر را ارسال کنید و یا از دستور /cancel استفاده نمایید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.SessionPasswordNeeded:
            step = 'SessionPasswordNeeded'
            await message.reply('<b>لطفا رمز تایید دو مرحله ای را وارد نمایید :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

    elif step == 'SessionPasswordNeeded':
        twoFaPass = text
        try :
            await tempClient['client'].check_password(twoFaPass)
        except errors.BadRequest:
            await message.reply('<b>رمز وارد شده اشتباه میباشد, لطفا مجدد ارسال نمایید یا از دستور /cancel استفاده نمایید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>اکانت با موفقیت ثبت شد ✅\nدرصورتیکه قصد افزودن شماره دارید, شماره موردنظر را ارسال کنید و یا از دستور /cancel استفاده نمایید.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       Delete Account                       #
    if step == 'removeAccount':
        step = None
        phone_number = text.replace('+', '').replace(' ', '').replace('-', '')
        if not os.path.isfile(f'sessions/{phone_number}.session'):
            await message.reply('<b>شماره مورد نظر در سرور یافت نشد !</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            await bot.send_document(message.chat.id, f'sessions/{phone_number}.session', caption='<b>شماره مورد نظر با موفقیت حذف شد ✅\nسشن پایروگرام برای بایگانی برای شما ارسال شد.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
            os.unlink(f'sessions/{phone_number}.session')

#                       set Time                       #
    if step == 'setTime':
        step = None
        sleeping = float(text)
        await message.reply('<b>زمان جدید با موفقیت تنظیم شد ✅</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       join Accounts                       #
    if step == 'joinAccounts':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        link = text.split()[0].replace('@', '').replace('+', 'joinchat/')
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>عملیات عضویت شروع شد ...</b>')
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.join_chat(link)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات عضویت اکانت های ربات ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>عملیات عضویت با موفقیت به پایان رسید ✅

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}</b>''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)


#                       Leave Accounts                       #
    if step == 'leaveAccounts':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>عملیات خروج شروع شد ...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.leave_chat(int(text), delete=True)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات لفت اکانت های ربات ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>عملیات لفت با موفقیت به پایان رسید ✅</b>

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send view                       #
    if step == 'sendViewToPost':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        username = text.split('/')[3]
        msg_id = int(text.split('/')[4])
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>عملیات ویو پست کانال شروع شد ...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        for session in ((await accountList())):
            if evalID not in isWorking :
                break
            try:
                await cli.disconnect()
            except:
                pass
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.invoke(functions.messages.GetMessagesViews(peer = await cli.resolve_peer(username), id=[msg_id], increment=True))
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات ارسال ویو اکانت های ربات ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>عملیات بازدید پست کانال با موفقیت به پایان رسید ✅</b>

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send Post reAction                       #
    if step == 'reActionEval':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        peerID = '@' + text.split("\n")[0].split('/')[3]
        peerMessageID = int(text.split("\n")[0].split('/')[4])
        emojies = text.split("\n")[1].split()
        countOfWork = int(text.split("\n")[2])
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        if text.split("\n")[0].split('/')[3].isdigit():
            await message.reply('<b>لینکی که برام ارسال کردی مربوط به یک چت خصوصیه ❗️</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            msg = await message.reply('<b>عملیات ارسال ری اکشن شروع شد ...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            for session in ((await accountList())):
                if all >= countOfWork:
                    break
                if evalID not in isWorking:
                    break
                try:
                    await cli.disconnect()
                except:
                    pass
                all += 1
                await asyncio.sleep(sleeping)
                try:
                    api_id2, api_hash2 = await randomAPP()
                    cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                    await cli.connect()
                    await asyncio.sleep(0.2)
                    await cli.send_reaction(peerID, peerMessageID, random.choice(emojies))
                    await asyncio.sleep(0.2)
                    await cli.disconnect()
                except Exception as e:
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    error += 1
                else:
                    done += 1
                finally:
                    spendTime = await remainTime(TS)
                    await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات ارسال ری اکشن پست کانال ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
            try:
                isWorking.remove(evalID)
            except:
                pass
            spendTime = await remainTime(TS)
            await message.reply(f'''<b>عملیات ری اکشن پست با موفقیت به پایان رسید ✅</b>

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send Post vote                       #
    if step == 'voteEval':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        peerID = '@' + text.split("\n")[0].split('/')[3]
        peerMessageID = int(text.split("\n")[0].split('/')[4])
        opt = text.split("\n")[1]
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        if not opt.isdigit():
            await message.reply('<b>گزینه وارد شده صحیح نمیباشد ❗️</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            msg = await message.reply('<b>عملیات ارسال نظر سنجی شروع شد ...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            for session in ((await accountList())):
                if evalID not in isWorking:
                    break
                try:
                    await cli.disconnect()
                except:
                    pass
                all += 1
                await asyncio.sleep(sleeping)
                try:
                    api_id2, api_hash2 = await randomAPP()
                    cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                    await cli.connect()
                    await asyncio.sleep(0.2)
                    await cli.vote_poll(peerID, peerMessageID, int(opt))
                    await asyncio.sleep(0.2)
                    await cli.disconnect()
                except Exception as e:
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    error += 1
                else:
                    done += 1
                finally:
                    spendTime = await remainTime(TS)
                    await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات ارسال نظرسنجی ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
            try:
                isWorking.remove(evalID)
            except:
                pass
            spendTime = await remainTime(TS)
            await message.reply(f'''<b>عملیات نظر سنجی با موفقیت به پایان رسید ✅</b>

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       Spam user                       #
    if step == 'Spamuser':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        usernames = text
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>عملیات اسپم کاربر شروع شد ...</b>')
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2,"4.8.6","Telegram Desktop","windows")
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.send_message(usernames,random.choice(fosh))
                await cli.block_user(usernames)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات اسپم کاربر  ...

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}

برای لغو این عملیات از دستور ( /stop_{evalID} ) استفاده نمایید.''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>عملیات عضویت با موفقیت به پایان رسید ✅

• اکانت های بررسی شده : {all}/{allAcccounts}
• موفق : {done}
• خطا : {error}
• زمان سپری شده : {spendTime}</b>''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)











bot.run()