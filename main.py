#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def owner():
    if os.path.exists("owner.txt"):
        with open("owner.txt", "r") as f:
            data = f.read()
            return data
    else:
        pass
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def malek():
    if os.path.exists("malek.txt"):
        with open("malek.txt", "r") as f:
            data = f.read()
            return data
    else:
        pass
 #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
on_off = ["off"]
hame = ["n"]
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
hijau  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
kuning ="\x1b[1;93m"
ungu   ="\x1b[1;95m"
putih  ="\x1b[1;97m"
biru   ="\x1b[1;94m"
merah  ="\x1b[1;91m"
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
import sys,time,os
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
from os import system, name
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(00.01)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
try:import aiohttp
except ImportError:
    system("pip install aiohttp")
    clear_console()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
try:import requests
except ImportError:
    system("pip install requests")
    clear_console()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
try:from rubpy import Client
except ImportError:
    system("pip install rubpy")
    clear_console()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
try:
    from rubpy.types import Updates
    from rubpy import filters
except ImportError:
    system("pip install -U rubpy")
    system("pip install rubpy")
    clear_console()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
try:
    import aiortc
except ImportError:
    system("pip install rubpy[rtc]")
    clear_console()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
ketik(f"{hijau}» Free Version\n» Py-Bot\n» https://pybot.info{cyan}")
time.sleep(1)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
bot = Client(name="musicbot",display_welcome=False)#.rp
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def restart_program():
    print("Restarting the program...")
    python = sys.executable
    os.execl(python, python, *sys.argv)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def on_bot(message:Updates):
    if message.text == "روشن":
        o = owner()
        if message.author_guid in o:
            if "off" in on_off:
                on_off.clear()
                on_off.append("on")
                await message.reply("**ربات روشن شد**")
            else:
                await message.reply("**ربات از قبل روشن بود**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def off_bot(message:Updates):
    if message.text == "خاموش":
        o = owner()
        if message.author_guid in o:
            if "on" in on_off:
                on_off.clear()
                on_off.append("off")
                await message.reply("**ربات خاموش شد**")
            else:
                await message.reply("**ربات از قبل خاموش بود**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def send_hello(message:Updates):
    if message.text == "مالک":
        if message.object_guid.startswith("u0"):
            if os.path.exists("owner.txt"):
                pass
            else:
                guid = message.author_guid
                name = "owner.txt"
                with open(name, "w") as f:
                    f.write(guid + "\n")
                    f.write("u0Bzjsc0c52bcf1a391ef738c9bd1db5")
                    with open("malek.txt", "w") as k:
                        k.write(guid)
                        await message.reply("**⚡ سلام مالک من !**\nمن از الان فعال شدم فقط کافیه تو گروهت بنویسی فعال تا کار کنم ✔️\nچنل ربات ᯒ 𝗦𝗢𝗥𝗘𝗡n\⩥ @soren_bot ")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def group():
    if os.path.exists("group.txt"):
        with open("group.txt", "r") as f:
            data = f.read()
            return data
    else:
        pass
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def group(message:Updates):
    if message.text == "فعال":
        if "on" in on_off:
            data = owner()
            if message.author_guid in data:
                if os.path.exists("group.txt"):
                    with open("group.txt", "r") as f:
                        data_group = f.read()
                        guid = message.object_guid
                        if guid in data_group:
                            name = await bot.get_group_info(guid)
                            group_name = name["group"]["group_title"]
                            await message.reply(f"**ربات از قبل تو گروه {group_name} فعال بود ♬ **")
                        else:
                            guid = message.object_guid
                            with open("group.txt", "w") as f:
                                f.write(guid + "\n")
                                name = await bot.get_group_info(guid)
                                group_name = name["group"]["group_title"]
                                await message.reply(f"**ربات با موفقیت تو گروه {group_name} فعال شد♬n\𝐒𝐎𝐑𝐄𝐍 **")
                                text = """
سلام! 🎉  
ربات موزیکال پایتون با موفقیت در گروه شما فعال شد! 🎶  
این ربات به دو روش رایگان و اشتراکی ارائه میشود\n𝗦𝗢𝗥𝗘𝗡▷ @soren_bot """
                                await message.reply(text)
                else:
                    guid = message.object_guid
                    with open("group.txt", "w") as f:
                        f.write(guid + "\n")
                        name = await bot.get_group_info(guid)
                        group_name = name["group"]["group_title"]
                        await message.reply(f"**ربات با موفقیت تو گروه {group_name} فعال شد♬ 𝐒𝐎𝐑𝐄𝐍⇨ @soren_bot **")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def guid(message:Updates):
    if message.text == "گویدم":
        if "on" in on_off:
            await message.reply(message.author_guid)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def guidsh(message:Updates):
    if message.text.startswith("گوید"):
        o = owner()
        if message.author_guid in o:
            if "on" in on_off:
                text = message.text.split("گوید")[1].strip()
                info = await bot.get_object_by_username(text)
                name = info["user"]["user_guid"]
                await message.reply(name)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def restart(message:Updates):
    if message.text == 'ریستارت':
        o = owner()
        if message.author_guid in o:
            if "on" in on_off:
                data = owner()
                if message.author_guid in data:
                    await message.reply('» ریستارت شدم')
                    restart_program()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def vip(message:Updates):
    if message.text.startswith("ارتقا"):
        o = owner()
        if message.author_guid in o:
            if "on" in on_off:
                text = message.text.split("ارتقا")[1].strip()
                info = await bot.get_object_by_username(text)
                guid = info["user"]["user_guid"]
                nam = await bot.get_user_info(guid)
                name = nam["user"]["first_name"]
                with open("vip.txt", "w") as f:
                    f.write(guid + "\n")
                    await message.reply(f"**کاربر {name} ادمین ویژه شد ♬\n𝚂𝙾𝚁𝙴𝙽 ")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def ban_vip(message:Updates):
    if message.text.startswith("برکنار"):
        o = owner()
        if message.author_guid in o:
            if "on" in on_off:
                text = message.text.split("برکنار")[1].strip()
                info = await bot.get_object_by_username(text)
                guid = info["user"]["user_guid"]
                nam = await bot.get_user_info(guid)
                name = nam["user"]["first_name"]
                filename = 'vip.txt'
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    new_lines = [line.replace(guid, '') for line in lines]
                    with open(filename, 'w') as file:
                        file.writelines(new_lines)
                        await message.reply(f"کاربر {name} از لیست ویژه برکنار شد")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
async def fetch_url(url):
    async with aiohttp.ClientSession() as session, session.get(url) as response:
        return await response.json()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
def viip():
    if os.path.exists("vip.txt"):
        with open("vip.txt", "r") as f:
            data = f.read()
            return data
    else:
        pass
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def on_hame(message:Updates):
    if message.text == "دسترسی باز":
        o = owner()
        if "n" in hame:
            hame.clear()
            hame.append("y")
            await message.reply("**دسترسی به همه کاربران داده شد**")
        else:
            await message.reply("قبلا فعال بود")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def on_hame(message:Updates):
    if message.text == "دسترسی بسته":
        o = owner()
        if "y" in hame:
            hame.clear()
            hame.append("n")
            await message.reply("**دسترسی به همه کاربران داده نشد**")
        else:
            await message.reply("قبلا غیرفعال بود")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def random_music(message:Updates):
    if message.text == "موزیک رندوم":
        if "on" in on_off:
            o,v = owner(),viip()
            if message.author_guid in o or message.author_guid in v or "y" in hame:
                kir = (await fetch_url("https://api-free.ir/api/music"))
                name,link = kir["result"]["title"], kir["result"]["song"]
                await bot.voice_chat_player(message.object_guid,link)
                await message.reply(f"""
موزیک رندوم پیدا و درحال پخش در ویسکال است

نام موزیک : {name}

لینک دانلود موزیک : {link}

↻ㅤ  ◁ㅤㅤ❚❚       ▷       ⇆      ‌◉━━━━━━───────

𝐒𝐎𝐑𝐄𝐍 ␥ @SOREN_BOT """)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def search_music(message:Updates):
    if message.text.startswith("سرچ موزیک"):
        if "on" in on_off:
            o,v = owner(),viip()
            if message.author_guid in o or message.author_guid in v or "y" in hame:
                text = message.text.split("سرچ موزیک")[1].strip()
                kir = (await fetch_url(f"https://api-free.ir/api/sr-music/?text={text}"))
                name,link = kir["result"]["title"], kir["result"]["song"]
                await bot.voice_chat_player(message.object_guid,link)
                await message.reply(f"""
موزیک درحال پخش در ویسکال است

نام موزیک : {name}

لینک دانلود موزیک : {link}

↻ㅤ  ◁ㅤㅤ❚❚       ▷       ⇆      ‌◉━━━━━━───────
𝐒𝐎𝐑𝐄𝐍 ␥ @SOREN_BOT  """)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def stop_music(message):
    if message.text == "متوقف":
        if "on" in on_off:
            o,v = owner(),viip()
            if message.author_guid in o or message.author_guid in v or "y" in hame:
                await bot.voice_chat_player(message.object_guid, 'https://sedatoseda.com/wp-content/uploads/Absolute-Silence-Sound.mp3')
                await message.reply("**پخش موزیک در ویسکال متوقف شد**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def reply_music(message:Updates):
    if message.text == "پخش":
        if "on" in on_off:
            o,v = owner(),viip()
            if message.author_guid in o or message.author_guid in v or "y" in hame:
                send_msg = (await message.reply('درحال دانلود...'))['message_update']['message_id']
            file_inline = await bot.get_messages_by_id(message.object_guid, message.reply_message_id)
            await bot.download(save_as='music.mp3', file_inline=file_inline['messages'][0]['file_inline'])
            await bot.voice_chat_player(message.object_guid, 'music.mp3')
            await message.reply(f"""
موزیک درحال پخش در ویسکال است

↻ㅤ  ◁ㅤㅤ❚❚       ▷       ⇆      ‌◉━━━━━━───────
𝐒𝐎𝐑𝐄𝐍 ␥ @SOREN_BOT  """)
            await bot.delete_messages(message.object_guid, [send_msg])
            os.remove('music.mp3')
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def clear_vip(message:Updates):
    if message.text == "پاکسازی لیست ویژه":
        if "on" in on_off:
            o = owner()
            if message.author_guid in o:
                if os.path.exists("vip.txt"):
                    os.remove("vip.txt")
                    await message.reply("**کلیه افراد در لیست ویژه پاک شدند**")
                else:
                    await message.reply("**هیچ کس در لیست ویژه وجود ندارد**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def left(message:Updates):
    if message.text == "لفت":
        o = owner()
        if message.author_guid in o:
            if message.object_guid.startswith("g0"):
                await bot.leave_group(message.object_guid)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def voice(message:Updates):
    if message.text == "کال":
        o,v=owner(),viip()
        if message.author_guid in o or message.author_guid in v or "y" in hame:
            await bot.create_group_voice_chat(message.object_guid)
            await message.reply("**ویسکال با موفقیت ایجاد شد**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def enteghal(message:Updates):
    if message.text.startswith("انتقال مالکیت"):
        if "on" in on_off:
            o = owner()
            if message.author_guid in o:
                text = message.text.split("انتقال مالکیت")[1].strip()
                info = await bot.get_object_by_username(text)
                guid = info["user"]["user_guid"]
                os.remove("malek.txt")
                os.remove("owner.txt")
                with open("malek.txt", "w") as f:
                    f.write(guid)
                    with open("owner.txt", "w") as file:
                        file.write(guid + "\n")
                        file.write("u0Bzjsc0c52bcf1a391ef738c9bd1db5")
                        await message.reply("**مالک جدید انتخاب شد و از الان به بعد شما مالک ربات نیستید**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def fal(message:Updates):
    if message.text == "فال":
        if "on" in on_off:
            o,v=owner(),viip()
            if message.author_guid in o or message.author_guid in v or "y" in hame:
                kir = (await fetch_url("https://api.api-code.ir/fallhafez2/index.php"))
                link = kir["result"]["voice"]
                await bot.voice_chat_player(message.object_guid,link)
                await message.reply(f"""
فال درحال پخش در ویسکال است

↻ㅤ  ◁ㅤㅤ❚❚       ▷       ⇆      ‌◉━━━━━━───────
𝐒𝐎𝐑𝐄𝐍 ␥ @SOREN_BOT """)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def place(message:Updates):
    if message.text == "مقامم":
        if "on" in on_off:
            o,v=owner(),viip()
            if message.author_guid in o:
                await message.reply("**⚜️ مالک**")
            elif message.author_guid in v:
                await message.reply("**⚡ ادمین ویژه**")
            else:
                await message.reply("**👤 کاربر عادی**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def join(message):
    if message.text.startswith("https://rubika.ir/joing/"):
        if message.object_guid.startswith("u0"):
            o = owner()
            if message.author_guid in o:
                text = message.text
                await bot.join_group(text)
                await message.reply("**عضو گروه شدم**")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
@bot.on_message_updates()
async def help(message):
    if message.text == "دستورات":
        if "on" in on_off:
            help_message = """
دستورات ربات موزیکال سورن بات 
• مالک
¹ هرکی اول بعد روشن شدن ربات بره پیویش و اینو بنویسه مالک ربات میشه.
² برای عضو شدن تو گروه کافیه تنها لینک گروه و بدون هیچ متن دیگه ای براش بفرستید.

• روشن/خاموش ◁ بعد مالک شدن باید بنویسید روشن تا روشن بشه.

• ارتقا ◁ جلوش ایدی هرکی و بزارید به ربات شما دسترسی پیدا میکنه.

• برکنار ◁ جلوش ایدی هرکی و بزارید از لیست ویژه درمیاره.

•لفت ◁ از گروه لفت میده.

• مقامم ◁ مقام تونو نشون میده.

•انتقال مالکیت ◁ جلوش ایدی هرکی و بزارید اون مالک ربات میشه.

• کال

•خروج ◁ از ویسکال لفت میده

•دسترسی باز ◁ اینجوری همه کاربران میتونند از ربات استفاده کنند.

•دسترسی بسته ◁ اینجوری فقط مالک و افراد ویژه میتونند به ربات دستور بدهند.

•گوید ◁ جلوش ایدی هرکی بزارید گویدشو بهتون میده.

•گویدم

•فعال ◁برای اینکه تو گروه کار کنه مالک ربات باید حتما تو گروه بنویسه فعال.

•پاکسازی لیست ویژه

•موزیک رندوم

•سرچ موزیک ◁جلوش تیکه ای از اهنگ یا اسم خواننده رو بنویسید میاره(فقط خواننده های مجاز)

•متوقف 

•پخش ◁ رو هر اهنگی ریپلای بزنید و این دستور رو بنویسید ربات اون اهنگ و دانلود و پخش میکنه.

•فال ◁ فال میگیره و اونو تو ویسکال پخش میکنه """
            await message.reply(help_message)
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
bot.run()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#