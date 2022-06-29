from telethon import TelegramClient, events
import asyncio
from  telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import FloodWaitError
api_id = 12821795
api_hash = "11302a8e320a6774bebc5800f05092c8"

client = TelegramClient("ersalPv" , api_id , api_hash)

admin= 5458929761
@client.on(events.NewMessage(pattern="/Run"))
async def started(event):
	await event.reply( "𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ʕ •́؈•̀ ₎")
@client.on(events.NewMessage(from_users=admin,pattern='/join'))
async def join(event):
	global x
	try:
		admin= 925761076
		chat_id = event.chat_id
		async with client.conversation(chat_id) as conv:
				await conv.send_message("""**سلام و درود ادمین عزیز♥️
به بخش جوین خوش امدید😁
🛑لطفا لینک خود را ارسال کنید🛑

🔴لینک پرایوت🔴**""")
		    
				daryaft_link = await conv.get_response()
				x = daryaft_link.raw_text
				await client(ImportChatInviteRequest(x))
				await event.reply("**با موفقیت جوین شد✅")
	
	except FloodWaitError as e:
		await client.send_message(event.chat_id,f"""**اکانت شما فلود شده است🔴
و یا مشکلات دیگر لطفا صبر کنید✅
و یا اگر حل نشد مشکل شما با پشتیبانی گفتگو کنید🔥
زمان ریپ اکانت شما {e.seconds}
👨‍💻 @MAVAD_GIR
🤖
📣 https://t.me/+kyY5vZY0O6lkM2Nk**""",link_preview=False)

@client.on(events.NewMessage(from_users=admin,pattern='/send'))
async def send(event):
	global x
	chat_id = event.chat_id
	async with client.conversation(chat_id) as conv:
		await conv.send_message("""
			**☣سلام به بخش اد بنر خوش امدید☣
㊗️بنر را فوروارد کنید تا ست شود㊗️

👨‍💻 @Mavad_Gir
🤖
📣 https://t.me/+kyY5vZY0O6lkM2Nk**""",link_preview=False)
		daryaft_baner = await conv.get_response()
		await event.reply("""**بنر با موفقیت ست شد✅

👨‍💻 @Mavad_Gir
🤖
📣 https://t.me/+kyY5vZY0O6lkM2Nk**""",link_preview=False)
		inviteLink = "https://t.me/+" + x
		if inviteLink.find("+") > -1:
			inviteLink = inviteLink.replace("+", "joinchat/")
		Enti = await client.get_entity(inviteLink)
		Enid = Enti.id
		async for user in client.iter_participants(Enid):
			await client.send_message(user.id, """
			**سلام♥️
این ربات ساخته شده توسط👇
👨‍💻 @Mavad_Gir
🤖
📣 https://t.me/+kyY5vZY0O6lkM2Nk**
			""",link_preview=False)
			await daryaft_baner.forward_to(user.id)
			
	
	
@client.on(events.NewMessage(pattern='/help' , from_users=admin))
async def help(event):
			await event.reply("""
			**سلام و وقت بخیر ادمین عزیز 😁♥️

لیست دستورات👇👌

/help
با این دستور میتونید به بخش هلپ یا همون کمک دسترسی داشته باشید✅
و بفهمید که امکانات و کارایی های دستورات چیست😻

/Run
با این دستور میفهمید که رباتتون ران هست یا نه !!🔌

/send

میتونید پروسه جوین،ست بنر،و ارسال رو انجام بدید و ربات کار اصلی خودشو بکنه💣💰


👨‍💻 @Mavad_Gir
🤖
📣 https://t.me/+kyY5vZY0O6lkM2Nk**""")
					
			
			
			
		
print("runed")			
client.start()
client.run_until_disconnected()
