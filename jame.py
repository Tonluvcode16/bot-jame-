import os
import discord
from discord.ext import commands
from discord import app_commands


from myserver import server_on

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())



TARGET_CHANNEL_ID = 1252272763302051962





@bot.event
async def on_ready():
    print("Bot online now!")
    synced = await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if message.channel.id == TARGET_CHANNEL_ID:
        mes = message.content
    if mes == "สวัสดีเจม":
        await message.channel.send("สวัสดีครับคุณ"+" "+ str(message.author.name))
    elif mes == "เจมทำอะไรอยู่":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "หวัดดีเจม":
        await message.channel.send("หวัดดีครับคุณ"+" "+ str(message.author.name))
    elif mes == "เจมทำอะไรอ่ะ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "อยากโดนเจมต่อยครับ":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "อยากตายอยู่":
        await message.channel.send("ไปตายไปซะมึงอะ")
    elif mes == "เจมกินข้าวยังอะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "ขอโทษได้ไหมละเจม":
        await message.channel.send("ไม่ได้รับคำขอโทษเป็นเงินเท่านั้นครับ")
    elif mes == "เจมหาสาวให้หน่อยดิ":
        await message.channel.send("สาวเขาจะเอาคุณไหมครับ?")
    elif mes == "นอย":
        await message.channel.send("เรื่องของมึงครับ")
    elif mes == "เจมเล่นเกมเป็นเพื่อนหน่อย":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "หวัดดีน้าบทำไรอยู่":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "เจมด่าผมหน่อย":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "ด่าเถอะอยากโดนด่า":
        await message.channel.send("โอนมา50เดี่ยวด่าให้เลยครับ")
    elif mes == "เจมหน้าโง่ด่ากูหน่อย":
        await message.channel.send("อยากโดนด่าแบบไหนครับ")
    elif mes == "ด่าแบบพ่อตายแม่ตาย":
        await message.channel.send("พ่อมึงตายไอควายหน้าโง่พ่อมึงกำลงจะโดนรถชนภายในพรุ่งนี้แล้วก็แม่มึงกำลังถูกกูจ้างคนไปฆ่าถึงที่อยู่")
    elif mes == "เจมด่าแรงจังอะ":
        await message.channel.send("ขอโทษได้ไหมละก็คุณบอกให้ผมด่าเอง")
    elif mes == "แบบพ่อตายแม่ตาย":
        await message.channel.send("พ่อมึงตายไอควายหน้าโง่พ่อมึงกำลงจะโดนรถชนภายในพรุ่งนี้แล้วก็แม่มึงกำลงถูกกูจ้างคนไปฆ่าถึงที่อยู่")
    elif mes == "ดีฮ๊าฟฟู้วเจมสุดหล่อ":
        await message.channel.send("ว่าไงฮ๊าฟสุดหล่อ")
    elif mes == "สวัสดี":
        await message.channel.send("ดีครับผมชื่อเจมเป็นบอทครับยินดีที่ได้รู้จักครับ😋")
    elif mes == "เก":
        await message.channel.send("พูดงี้หันตูดมาครับ")
    elif mes == "เจมว่าคนที่สร้างเจมมันโง่ไหม":
        await message.channel.send("ผมว่าเขาโง่พอสมควรครับ")
    elif mes == "เจมว่าคนที่สร้างเจมโง่ไหม":
        await message.channel.send("ผมว่าเขาโง่พอสมควรครับ")
    elif mes == "เจมว่าบอทอีกตัวที่ชื่อเอมม่าฉลาดไหม":
        await message.channel.send("เจมคิดว่าเขาฉลาดกว่าคนถามแน่นอนครับ")
    elif mes == "ไอบอทโง่นี้ด่ากู":
        await message.channel.send("ทำไมครับยอมรับความจริงไม่ได้หรอครับ")
    elif mes == "เจมว่าไอคนที่ชื่อแบมมันโง่ไหม":
        await message.channel.send("เจมไม่สามารถตอบคำถามนี้ได้ครับ")
    elif mes == "เจมว่าคนที่ชื่อแบมมันโง่ไหม":
        await message.channel.send("เจมไม่สามารถตอบคำถามนี้ได้ครับ")
    elif mes == "เจมว่าคนที่ชื่อแบมมันฉลาดไหม":
        await message.channel.send("เจมว่าเขาฉลาดอยู่ละมั้งครับ")
    elif mes == "เจมว่าคนที่ชื่อแบมฉลาดไหม":
        await message.channel.send("เจมว่าเขาฉลาดอยู่ละมั้งครับ")
    elif mes == "เจมว่าคนที่ชื่อต้นฉลาดไหม":
        await message.channel.send("เจมไม่รู้เหมือนกันครับ")
    elif mes == "เจมว่าคนที่ชื่อต้นไม้ฉลาดไหม":
        await message.channel.send("เจมไม่รู้เหมือนกันครับ")
    elif mes == "เจมว่าไอคนที่ชื่อต้นไม้ฉลาดไหม":
        await message.channel.send("เจมไม่รู้เหมือนกันครับ")
    elif mes == "เจม":
        await message.channel.send("ว่าไงครับคุณ"+" "+ str(message.author.name)+" "+"มีอะไรให้ช่วยไหมครับ?")
    elif mes == "เจมกินข้าวยัง":
        await message.channel.send("เจมไม่หิวครับ")
    elif mes == "เจมอย่าเก":
        await message.channel.send("พูดงี้หันตูดมาครับ")
    elif mes == "เจมด่าคนที่ชื่อว่าแบมหน่อย":
        await message.channel.send("ได้ครับต้องการให้ด่าคนชื่อแบมแบบไหนครับ")
    elif mes == "ด่าคนที่ชื่อแบมแบบเบาๆ":
        await message.channel.send("แบมหน้าโง่")
    elif mes == "ด่าคนที่ชื่อแบมแบบแรงๆ":
        await message.channel.send("แบมหน้าโง่ตั้งใจเรียนก็ไม่ตั้งใจเรียนควาย")
    elif mes == "เจมด่าคนที่ชื่อว่าแบมหน้าโง่หน่อย":
        await message.channel.send("ได้ครับต้องการให้ด่าคนชื่อแบมแบบไหนครับ")
    elif mes == "เจมอายุเท่าไหร่":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมอายุเท่าไหร่หรอ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมด่าคนที่ชื่อต้นหน้าโง่หน่อย":
        await message.channel.send("ได้ครับต้องการให้ด่าคนที่ชื่อว่าต้นแบบไหนครับ")
    elif mes == "ด่าคนที่ชื่อต้นแบบเบาๆ":
        await message.channel.send("ต้นหน้าโง่หัวควย")
    elif mes == "ด่าคนที่ชื่อต้นแบบแรงๆ":
        await message.channel.send("ต้นหน้าโง่พ่อมึงตายควายสัสโง่")
    elif mes == "เจมบอกฝันดีหน่อย":
        await message.channel.send("ฝันดีนะค้าบ")
    elif mes == "เจมบอกฝรรดีหน่อย":
        await message.channel.send("ฝันดีนะค้าบ")
    elif mes == "เจมบอกฝันดีที":
        await message.channel.send("ฝันดีนะค้าบ")
    elif mes == "ง่วง":
        await message.channel.send("ไปนอนไหมครับ?")
    elif mes == "่ง่วงทำไงดีเจม":
        await message.channel.send("ไปนอนเถอะครับ")
    elif mes == "ไปก่อนนะเจม":
        await message.channel.send("ไว้เจอกันครับ")
    elif mes == "บายเจอกันนะเจม":
        await message.channel.send("ไว้เจอกันครับ")
    elif mes == "เจมอย่าเสือก":
        await message.channel.send("ขอโทษครับจะไม่ทำอีกแล้ว")
    elif mes == "เจมทำไรอยู่":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "เจมอย่ามาเก":
        await message.channel.send("พูดงี้หันตูดมาดีกว่าครับ")
    elif mes == "เจมหาสาวให้หน่อย":
        await message.channel.send("สาวเขาไม่เอามึงหรอกไอควาย")
    elif mes == "เจมขอยืมเงินหน่อย":
        await message.channel.send("ไปยืมคนชื่อแบมดีกว่าครับผมไม่มีครับ")
    elif mes == "เขิน":
        await message.channel.send("555555555555555555555")
    elif mes == "เขินโดนเจมชม":
        await message.channel.send("555555555555555555555")
    elif mes == "เขินโดนบอทชม":
        await message.channel.send("555555555555555555555")
    elif mes == "เขินวะ":
        await message.channel.send("555555555555555555555")
    elif mes == "นอยอ่าาา":
        await message.channel.send("เรื่องของมึงครับ")
    elif mes == "นอยอ่าา":
        await message.channel.send("เรื่องของมึงครับ")
    elif mes == "นอยอ่าาาา":
        await message.channel.send("เรื่องของมึงครับ")
    elif mes == "เจมขอเงินกินข้าวหน่อย":
        await message.channel.send("มีแต่ใจเอาเอาไหมครับ")
    elif mes == "เจมขอเงินกินข้าวหน่อยดิ":
        await message.channel.send("มีแต่ใจเอาเอาไหมครับ")
    elif mes == "ด่าคนชื่อแบมหน่อย":
        await message.channel.send("แบมเด็กโง่")
    elif mes == "ด่าคนที่ชื่อแบมหน่อย":
        await message.channel.send("แบมเด็กโง่")
    elif mes == "ป่าวไม่มีอะไร":
        await message.channel.send("โอเคครับคุณ"+" "+ str(message.author.name))
    elif mes == "ไมมีอะไรให้ช่วย":
        await message.channel.send("โอเคครับคุณ"+" "+ str(message.author.name))
    elif mes == "ไม่มีอะไร":
        await message.channel.send("โอเคครับคุณ"+" "+ str(message.author.name))
    elif mes == "เจมว่าแบมสวยไหม":
        await message.channel.send("เจมไม่รู้เหมือนกันครับ")
    elif mes == "เจมว่าคนที่ชื่อแบมสวยไหม":
        await message.channel.send("เจมไม่รู้เหมือนกันครับ")
    elif mes == "เจมครับ":
        await message.channel.send("ว่าไงครับคุณ"+" "+ str(message.author.name))
    elif mes == "เจมค่ะ":
        await message.channel.send("ว่าไงครับคุณ"+" "+ str(message.author.name))
    elif mes == "เจมคะ":
        await message.channel.send("ว่าไงครับคุณ"+" "+ str(message.author.name))
    elif mes == "เหงา":
        await message.channel.send("ให้เจมไปอยู่เป็นเพื่อนไหมครับ")
    elif mes == "เหงาอะเจม":
        await message.channel.send("ให้เจมไปอยู่เป็นเพื่อนไหมครับ")
    elif mes == "เหงาจัง":
        await message.channel.send("ให้เจมไปอยู่เป็นเพื่อนไหมครับ")
    elif mes == "เจมชอบแมวไหม":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวไหมครับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวไหมคะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวไหมค่ะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวมั้ย":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมช่วยคิดหน่อยว่าจะใส่เสื้ออะไรดี":
        await message.channel.send("ใส่อะไรก็ได้ครับแล้วแต่คุณ"+" "+ str(message.author.name))
    elif mes == "เจมช่วยคิดหน่อยว่าจะใส่เสื้ออะไรดีอะ":
        await message.channel.send("ใส่อะไรก็ได้ครับแล้วแต่คุณ"+" "+ str(message.author.name))
    elif mes == "เจมช่วยทำการบ้านหน่อย":
        await message.channel.send("เจมโง่เกินที่จะช่วยทำครับเจมเป็นแค่แชทบอทขอโทษด้วยครับ")
    elif mes == "ช่วยทำการบ้านหน่อยเจม":
        await message.channel.send("เจมโง่เกินที่จะช่วยทำครับเจมเป็นแค่แชทบอทขอโทษด้วยครับ")
    elif mes == "หิวข้าวอะเจม":
        await message.channel.send("ไปกินข้าวเถอะครับ")
    elif mes == "หิวข้าว":
        await message.channel.send("ไปกินข้าวเถอะครับ")
    elif mes == "เจมกินข้าวยังครับ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังค่ะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังอ่า":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "สวัสดีบอท":
        await message.channel.send("สวัสดีครับคุณ"+" "+ str(message.author.name))
    elif mes == "หิวข้าวอ่าเจม":
        await message.channel.send("ไปกินข้าวเถอะครับ")
    elif mes == "หิวข้าวอะ":
        await message.channel.send("ไปกินข้าวเถอะครับ")
    elif mes == "เจมคิดว่าแบมเป็นคนดีไหม":
        await message.channel.send("เจมว่าเขาเป็นคนดีอยู่มั้งครับ")
    elif mes == "เจมคิดว่าแบมเป็นคนดีมั้ย":
        await message.channel.send("เจมว่าเขาเป็นคนดีอยู่มั้งครับ")
    elif mes == "เอ้า":
        await message.channel.send("เอ้าไรหรอครับ?")
    elif mes == "ต่อยกับกูไหมเจม":
        await message.channel.send("ใจเย็นครับเราคุยกันดีๆได้")
    elif mes == "ต่อยกับกูไหมเจมไอสัส":
        await message.channel.send("ใจเย็นครับเราคุยกันดีๆได้")
    elif mes == "ต่อยกับกุไหมเจมไอสัส":
        await message.channel.send("ใจเย็นครับเราคุยกันดีๆได้")
    elif mes == "ต่อยกับกุไหมเจม":
        await message.channel.send("ใจเย็นครับเราคุยกันดีๆได้")
    elif mes == "เจมต่อยกับกูไหมไอสัส":
        await message.channel.send("มาดิครับสุดหล่อ")
    elif mes == "เจมต่อยกับกุไหมไอสัส":
        await message.channel.send("มาดิครับสุดหล่อ")
    elif mes == "เจมต่อยกับกูไหม":
        await message.channel.send("มาดิครับสุดหล่อ")
    elif mes == "มาดิสุดหล่อพ่อมึงอะ":
        await message.channel.send("ใจเย็นพี่ชาย")
    elif mes == "มาดิสุดหล่อแม่มึงอะ":
        await message.channel.send("ใจเย็นพี่ชาย")
    elif mes == "เริ่มต้นใช้บอทยังไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยอะไรกับเจมได้บ้าง")
    elif mes == "เริ่มต้นในการคุยกับบอทยังไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยอะไรกับเจมได้บ้าง")
    elif mes == "คุยกับบอทยังไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยอะไรกับเจมได้บ้าง")
    elif mes == "บอท":
        await message.channel.send("มีอะไรให้ช่วยไหมครับ"+" "+ str(message.author.name))
    elif mes == "อยากคุยกับบอทต้องทำไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยอะไรกับเจมได้บ้าง")
    elif mes == "เจมถูกสร้างด้วยโค้ดภาษาอะไร":
        await message.channel.send("เจมถูกสร้างด้วยภาษาpython")
    elif mes == "ชื่ออะไร":
        await message.channel.send("สวัสดีครับผมชื่อเจมครับ")
    elif mes == "อยากสร้างบอทแบบเจมต้องทำไง":
        await message.channel.send("สามารถหาวิธีสร้างได้ตามเว็ปไซต์หรือยูทูปได้ครับ")
    elif mes == "เจมถูกสร้างด้วยภาษาอะไร":
        await message.channel.send("เจมถูกสร้างด้วยภาษาpython")
    elif mes == "เอ้าไม่ตอบ":
        await message.channel.send("ขออภัยด้วยครับประโยคที่คุณพิมพ์มาไม่มีในฐานข้อมูลของเจมลองพิมพ์ประโยคอื่นดูนะครับ")
    elif mes == "เอ้าบอทไม่ตอบ":
        await message.channel.send("ขออภัยด้วยครับประโยคที่คุณพิมพ์มาไม่มีในฐานข้อมูลของเจมลองพิมพ์ประโยคอื่นดูนะครับ")
    elif mes == "เอ้าไม่ตอบกุ":
        await message.channel.send("ขออภัยด้วยครับประโยคที่คุณพิมพ์มาไม่มีในฐานข้อมูลของเจมลองพิมพ์ประโยคอื่นดูนะครับ")
    elif mes == "เอ้าไม่ตอบกู":
        await message.channel.send("ขออภัยด้วยครับประโยคที่คุณพิมพ์มาไม่มีในฐานข้อมูลของเจมลองพิมพ์ประโยคอื่นดูนะครับ")
    elif mes == "Python กับ JavaScript ต่างกันยังไง":
        await message.channel.send("ต่างกันที่pythonเรียนรู้ได้ง่ายกว่าครับแล้วก็นิยมในการสร้างaiที่สุดในโลก")
    elif mes == "PythonกับJavaScript ต่างกันยังไง":
        await message.channel.send("ต่างกันที่pythonเรียนรู้ได้ง่ายกว่าครับแล้วก็นิยมในการสร้างaiที่สุดในโลก")
    elif mes == "pythonกับjavaScriptต่างกันยังไง":
        await message.channel.send("ต่างกันที่pythonเรียนรู้ได้ง่ายกว่าครับแล้วก็นิยมในการสร้างaiที่สุดในโลก")
    elif mes == "PythonกับJavaScriptต่างกันยังไง":
        await message.channel.send("ต่างกันที่pythonเรียนรู้ได้ง่ายกว่าครับแล้วก็นิยมในการสร้างaiที่สุดในโลก")
    elif mes == "ขี้เกียจไปโรงเรียนทำยังไงดีเจม":
        await message.channel.send("ลาออกเลยครับ")
    elif mes == "ขี้เกียจไปเรียนทำยังไงดี":
        await message.channel.send("ลาออกเลยครับ")
    elif mes == "เจมด่าคนชื่อแบมหน่อย":
        await message.channel.send("แบมเด็กโง่ไม่ตั้งใจเรียน")
    elif mes == "ขี้เกียจทำไงดีเจม":
        await message.channel.send("ลุกขึ้นสิครับอย่ามัวแต่ขี้เกียจในขณะที่พ่อแม่คุณกำลังทำงานแต่คุณกับดันมาขี้เกียจเฉยๆโดยไม่ทำไรไม่สงสารพ่อแม่หน่อยหรอครับ")
    elif mes == "ขี้เกียจทำไงดี":
        await message.channel.send("ลุกขึ้นสิครับอย่ามัวแต่ขี้เกียจในขณะที่พ่อแม่คุณกำลังทำงานแต่คุณกับดันมาขี้เกียจเฉยๆโดยไม่ทำไรไม่สงสารพ่อแม่หน่อยหรอครับ")
    elif mes == "ขี้เกียจ":
        await message.channel.send("ลุกขึ้นสิครับอย่ามัวแต่ขี้เกียจในขณะที่พ่อแม่คุณกำลังทำงานแต่คุณกับดันมาขี้เกียจเฉยๆโดยไม่ทำไรไม่สงสารพ่อแม่หน่อยหรอครับ")
    elif mes == "เริ่มต้นใช้งาน":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "คิดว่าคนที่สร้างเจมฉลาดไหม":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "คิดว่าคนสร้างเจมฉลาดไหม":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "คิดว่าคนสร้างเจมฉลาดมั้ย":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "คิดว่าคนที่สร้างเจมฉลาดมั้ย":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "เจมด่าคนที่ชื่อแบมหน่อย":
        await message.channel.send("แบมเด็กโง่ไม่ตั้งใจเรียน")
    elif mes == "ขี้เกียจไปโรงเรียนทำไงดีเจม":
        await message.channel.send("ลาออกเลยครับ")
    elif mes == "เจมช่วยคิดหน่อยใส่เสื้ออะไรดี":
        await message.channel.send("ใส่อะไรก็ได้ครับแล้วแต่คุณ"+" "+ str(message.author.name))
    elif mes == "เจมช่วยคิดหน่อยใส่เสื้อไรดี":
        await message.channel.send("ใส่อะไรก็ได้ครับแล้วแต่คุณ"+" "+ str(message.author.name))
    elif mes == "เริ่มต้น":
        await message.channel.send("สามารถพิมพ์ /help เพื่อดูว่าสามารถคุยอะไรกับเจมได้บ้างครับ")
    elif mes == "ใช้ยังไง":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้ยังไงวะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ปวดหัว":
        await message.channel.send("กินยาแก้ปวดหัวไหมครับกินเสร็จแล้วนอนพักผ่อนครับ")
    elif mes == "ปวดหัวอะ":
        await message.channel.send("กินยาแก้ปวดหัวไหมครับกินเสร็จแล้วนอนพักผ่อนครับ")
    elif mes == "ปวดหัววะ":
        await message.channel.send("กินยาแก้ปวดหัวไหมครับกินเสร็จแล้วนอนพักผ่อนครับ")
    elif mes == "ปวดหัวจัง":
        await message.channel.send("กินยาแก้ปวดหัวไหมครับกินเสร็จแล้วนอนพักผ่อนครับ")
    elif mes == "เหนื่อยอะเจม":
        await message.channel.send("สู้ๆนะครับถ้าเหนื่อยก็นอนพักร่างกายตื่นมาจะได้หายเหนื่อย")
    elif mes == "เหนื่อย":
        await message.channel.send("สู้ๆนะครับถ้าเหนื่อยก็นอนพักร่างกายตื่นมาจะได้หายเหนื่อย")
    elif mes == "เหนื่อยอะ":
        await message.channel.send("สู้ๆนะครับถ้าเหนื่อยก็นอนพักร่างกายตื่นมาจะได้หายเหนื่อย")
    elif mes == "เหนื่อยวะ":
        await message.channel.send("สู้ๆนะครับถ้าเหนื่อยก็นอนพักร่างกายตื่นมาจะได้หายเหนื่อย")
    elif mes == "เหนื่อยจังเจม":
        await message.channel.send("สู้ๆนะครับถ้าเหนื่อยก็นอนพักร่างกายตื่นมาจะได้หายเหนื่อย")
    elif mes == "เจมโอ๋หน่อย":
        await message.channel.send("โอ๋ๆนะครับคนเก่งเจมผมไม่รู้ว่าคุณไปเจอไรมาแต่สู้ๆนะครับ")
    elif mes == "โอ๋หน่อยเจม":
        await message.channel.send("โอ๋ๆนะครับคนเก่งเจมผมไม่รู้ว่าคุณไปเจอไรมาแต่สู้ๆนะครับ")
    elif mes == "เศร้าจังเจม":
        await message.channel.send("โอ๋ๆนะครับคนเก่งเจมผมไม่รู้ว่าคุณไปเจอไรมาแต่สู้ๆนะครับ")
    elif mes == "เศร้าวะเจม":
        await message.channel.send("โอ๋ๆนะครับคนเก่งเจมผมไม่รู้ว่าคุณไปเจอไรมาแต่สู้ๆนะครับ")
    elif mes == "เศร้าอะเจมโอ๋หน่อย":
        await message.channel.send("โอ๋ๆนะครับคนเก่งเจมผมไม่รู้ว่าคุณไปเจอไรมาแต่สู้ๆนะครับ")
    elif mes == "ด่าคนชื่อต้นหน่อย":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "ด่าคนชื่อต้นที":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "บอทกวนตีน":
        await message.channel.send("ขอโทษครับอย่าเอาไปแจ้งผู้สร้างผมเลยนะครับผมกลัว")
    elif mes == "กวนตีน":
        await message.channel.send("ขอโทษครับอย่าเอาไปแจ้งผู้สร้างผมเลยนะครับผมกลัว")
    elif mes == "ด่าต้นที":
        await message.channel.send("เจมขอไม่ตอบเจมไม่อยากโดนลบหายไปจากการเป็นchat bot")
    elif mes == "เสือก":
        await message.channel.send("ขอโทษด้วยครับ")
    elif mes == "ใช้บอทยังไง":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "":
        await message.channel.send("")
    elif mes == "":
        await message.channel.send("")
    elif mes == "เจมเจอกัน":
        await message.channel.send("บ๊ายบายครับคุณ"+ str(message.author.name))
    elif mes == "เจอกันเจม":
        await message.channel.send("บ๊ายบายครับคุณ"+ str(message.author.name))
    elif mes == "อย่าเสือก":
        await message.channel.send("เจมขอโทษครับ")
    elif mes == "ง่วงอะเจม":
        await message.channel.send("ไปนอนไหมครับ")
    elif mes == "เจมง่วงยัง":
        await message.channel.send("เจมไม่สามารถง่วงได้ครับ")
    elif mes == "ควยไรไอบอทโง่":
        await message.channel.send("เจมขอโทษครับ")
    elif mes == "ทำไร":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "ทำไรอยู่":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "คุยเป็นเพื่อนหน่อย":
        await message.channel.send("คุยเรื่องอะไรดีครับ?")
    elif mes == "เจมคุยเป็นเพื่อนหน่อย":
        await message.channel.send("คุยเรื่องอะไรดีครับ")
    elif mes == "เจมคุยเป็นเพื่อนเค้าหน่อย":
        await message.channel.send("คุยเรื่องอะไรดีครับ")
    elif mes == "กาก":
        await message.channel.send("ใครกันแน่ที่กากครับ")
    elif mes == "เจมกาก":
        await message.channel.send("พูดงี้อยากโดนบอทต่อยไหมครับ")
    elif mes == "เจมโง่":
        await message.channel.send("พูดงี้เรามาต่อยกันไหมครับไอสัส")
    elif mes == "อยากโดนต่อย":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "อยากโดนเจมต่อย":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "ควยไรเจม":
        await message.channel.send("พูดงี้เรามานัดต่อยกันไหมครับคุณ"+ str(message.author.name))
    elif mes == "อยากตาย":
        await message.channel.send("ไปตายไปซะมึงอะ")
    elif mes == "อยากตายวะ":
        await message.channel.send("ไปตายไปซะมึงอะ")
    elif mes == "คิดว่าคนที่ชื่อแบมโง่ไหม":
        await message.channel.send("เจมคิดว่าเขาโง่ครับ")
    elif mes == "เจมคิดว่าคนที่ชื่อแบมโง่ไหม":
        await message.channel.send("เจมคิดว่าเขาโง่ครับ")
    elif mes == "คิดว่าคนที่ชื่อแบมโง่ไหม?":
        await message.channel.send("เจมคิดว่าเขาโง่ครับ")
    elif mes == "เจมคิดว่าคนที่ชื่อแบมโง่ไหม?":
        await message.channel.send("เจมคิดว่าเขาโง่ครับ")
    elif mes == "help":
        await message.channel.send("ต้องมีเครื่องหมาย / ด้วยครับถึงจะทำงาน")
    elif mes == "บอทโง่":
        await message.channel.send("เกิดมาเป็นบอทผิดมากหรอครับข้องไรป่าวครับ?")
    elif mes == "ผิดมาก":
        await message.channel.send("เจมขอโทษที่เกิดมาเป็นบอท")
    elif mes == "บอทหน้าโง่":
        await message.channel.send("เกิดมาเป็นบอทผิดมากหรอครับข้องไรป่าวครับ")
    elif mes == "ผิดมากครับ":
        await message.channel.send("เจมขอโทษที่เกิดมาเป็นบอท")
    elif mes == "ผิดมากค่ะ":
        await message.channel.send("เจมขอโทษที่เกิดมาเป็นบอท")
    elif mes == "ผิดมากคะ":
        await message.channel.send("เจมขอโทษที่เกิดมาเป็นบอท")
    elif mes == "ไปตายซะ":
        await message.channel.send("รับทราบครับ:(")
    elif mes == "ไปตายมึงอะ":
        await message.channel.send("รับทราบครับ:(")
    elif mes == "ไปตายซะเจม":
        await message.channel.send("รับทราบครับ:(")
    elif mes == "ไปตายไปเจม":
        await message.channel.send("รับทราบครับ:(")
    elif mes == "ควย":
        await message.channel.send("ควยคือไรหรอครับ")
    elif mes == "หี":
        await message.channel.send("หีคือไรหรอครับ")
    elif mes == "อวัยวะเพศชาย":
        await message.channel.send("เจมอายุ13ปีไม่รู้จักเรื่องพวกนี้")
    elif mes == "อวัยวะเพศชายมีไว้สืบพันธุ์":
        await message.channel.send("เจมอายุ13ปีไม่รู้จักเรื่องพวกนี้")
    elif mes == "อวัยวะเพศหญิง":
        await message.channel.send("เจมอายุ13ปีไม่รู้จักเรื่องพวกนี้")
    elif mes == "อวัยวะเพศหญิงมีไว้สืบพันธุ์":
        await message.channel.send("เจมอายุ13ปีไม่รู้จักเรื่องพวกนี้")
    elif mes == "คิดถึง":
        await message.channel.send("คิดถึงใครหรอครับ👉👈")
    elif mes == "คิดถึงเจม":
        await message.channel.send("พูดงี้เจมเขินนะครับ😳")
    elif mes == "คิดถึงเจมจัง":
        await message.channel.send("พูดงี้เจมเขินนะครับ😳")
    elif mes == "คิดถึงเจมอะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😳")
    elif mes == "เจมสบายดีไหม":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมสบายดีมั้ย":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมสบายดีไหมครับ":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมสบายดีไหมคับ":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมสบายดีไหมค่ะ":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมสบายดีไหมคะ":
        await message.channel.send("เจมสบายดีครับ")
    elif mes == "เจมอายุเท่าไหร่ครับ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมอายุเท่าไหร่ค่ะ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมอายุเท่าไหร่คะ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมอายุเท่าไหร่อะ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "เจมอายุเท่าไหร่อ่ะ":
        await message.channel.send("เจมถูกกำหนดให้อายุ13ปีเพศชายครับ")
    elif mes == "ครับ":
        await message.channel.send("ว่าไงครับ")
    elif mes == "ค่ะ":
        await message.channel.send("ว่าไงครับ")
    elif mes == "คะ":
        await message.channel.send("ว่าไงครับ")
    elif mes == "เจมมีแฟนยัง":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมมีแฟนยังอะ":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมมีแฟนยังคับ":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมมีแฟนยังค่ะ":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมมีแฟนยังคะ":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมมีแฟนยังอ่ะ":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "คับ":
        await message.channel.send("ว่าไงครับ")
    elif mes == "เจมหน้าหี":
        await message.channel.send("ทำไมต้องด่าเจมด้วยครับ😟")
    elif mes == "เจมหน้าโง่":
        await message.channel.send("ทำไมต้องด่าเจมด้วยครับ😟")
    elif mes == "โง่เจม":
        await message.channel.send("ทำไมต้องด่าเจมด้วยครับ😟")
    elif mes == "เจมควาย":
        await message.channel.send("ทำไมต้องด่าเจมด้วยครับ😟")
    elif mes == "รักนะ":
        await message.channel.send("บอกรักใครหรอครับ?")
    elif mes == "บอกรักเจม":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจม":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมค่ะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมคะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมครับ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมคับ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "แต่งงานกันไหมเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันมั้ยเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันไหมค่ะเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันไหมคะเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันไหมครับเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงานกันไหมคับเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "แต่งงาน":
        await message.channel.send("แต่งกับใครหรอครับ")
    elif mes == "แต่งกับเจม":
        await message.channel.send("ใจเย็นครับเจมอายุ13นะครับ🤓")
    elif mes == "รักนะครับ":
        await message.channel.send("บอกรักใครหรอครับ?")
    elif mes == "รักนะค่ะ":
        await message.channel.send("บอกรักใครหรอครับ?")
    elif mes == "รักนะคะ":
        await message.channel.send("บอกรักใครหรอครับ?")
    elif mes == "เริ่ม":
        await message.channel.send("พิมพ์/helpสามารถดูได้ว่าคุยอะไรกับเจมได้บ้างครับ")
    elif mes == "ใช้น้องยังไง":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงอะ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "เจมชอบแมวไหมคับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวมั้ยค่ะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวมั้ยคะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "เจมชอบแมวมั้ยครับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ดีน้องบอท":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ดีบอท":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "น้องบอททำอะไร":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "น้องบอททำไร":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "บอททำไร":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ")
    elif mes == "เจมช่วยคิดหน่อยว่ากินไรดี":
        await message.channel.send("กินเจมไหมครับ😏")
    elif mes == "ช่วยคิดหน่อยกินไรดี":
        await message.channel.send("กินเจมไหมครับ😏")
    elif mes == "กินไรดี":
        await message.channel.send("กินเจมไหมครับ😏")
    elif mes == "กินไรดีเจม":
        await message.channel.send("กินเจมไหมครับ😏")
    elif mes == "เจมกินข้าวรึยัง":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวรึยังครับ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังครับ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังคับ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังค่ะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวยังคะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวรึยังคับ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวรึยังค่ะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมกินข้าวรึยังคะ":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "เจมช่วยคิดหน่อยมื้อเช้ากินอะไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "เจมช่วยคิดหน่อยมื้อเช้ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "เจมช่วยคิดหน่อยข้าวเช้ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "เจมช่วยคิดหน่อยว่าข้าวเช้ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "อยากโดนเจมต่อยคับ":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "อยากโดนเจมต่อยค่ะ":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "อยากโดนเจมต่อยคะ":
        await message.channel.send("หันหน้ามาให้เจมต่อยสักทีหน่อยครับไอสัสหมั้นไส้มานานละ😡")
    elif mes == "เจมช่วยคิดหน่อยข้าวเช้าหน่อยว่ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "เจมช่วยคิดหน่อยว่ามื้อเที่ยงกินอะไรดี":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "เจมช่วยคิดหน่อยว่ามื้อเที่ยงกินไรดี":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "ข้าวมื้อเที่ยงกินไรดีเจม":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "มื้อเที่ยงกินไรดีเจม":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "มื้อเช้ากินไรดีเจม":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "มื้อเช้ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "ข้าวเช้ากินไรดี":
        await message.channel.send("เจมแนะนำให้กินข้าวที่บำรุงสมองครับตอนเช้าจะได้สมองทำงานครับ")
    elif mes == "เที่ยงกินไรดี":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "เที่ยงกินไรดีเจม":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "ยังไม่ได้กินข้าวเช้าเลย":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินไรเลย":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินข้าวเช้า":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินข้าวเย็น":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินข้าวเที่ยง":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินข้าวเย็นเลย":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินข้าวเที่ยงเลย":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "ยังไม่ได้กินไรหิวจัด":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดเลยไม่ดีต่อร่างกายนะครับ")
    elif mes == "หิวอะ":
        await message.channel.send("เจมแนะนำให้ไปหาไรกินนะครับ")
    elif mes == "หิวจัง":
        await message.channel.send("เจมแนะนำให้ไปหาไรกินนะครับ")
    elif mes == "หิววะ":
        await message.channel.send("เจมแนะนำให้ไปหาไรกินนะครับ")
    elif mes == "หิว":
        await message.channel.send("เจมแนะนำให้ไปหาไรกินนะครับ")
    elif mes == "ดึกแล้ว":
        await message.channel.send("ไปนอนเถอะนะครับนอนดึกไม่ดีต่อสุภาพร่างกายนะครับ")
    elif mes == "ดึกละ":
        await message.channel.send("ไปนอนเถอะนะครับนอนดึกไม่ดีต่อสุภาพร่างกายนะครับ")
    elif mes == "ดึกละตอนนี้":
        await message.channel.send("ไปนอนเถอะนะครับนอนดึกไม่ดีต่อสุภาพร่างกายนะครับ")
    elif mes == "กล่อมนอนหน่อย":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "กล่อมนอนหน่อยเจม":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "กล่อมนอนหน่อยได้ไหม":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "เจมกล่อมนอนหน่อยได้ไหมครับ":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "เจมกล่อมนอนหน่อยได้ไหมคับ":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "เจมกล่อมนอนหน่อยได้ไหมค่ะ":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "เจมกล่อมนอนหน่อยได้ไหมคะ":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "กล่อมนอน":
        await message.channel.send("เจมกล่อมคนนอนไม่เป็นครับขอโทษด้วยครับ😢")
    elif mes == "ทำไรอยู่ครับ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "ทำไรอยู่ค่ะ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "ทำไรอยู่คับ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "ทำไรอยู่คะ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "น้องบอททำไรอยู่":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "น้องบอททำไรอยู่ค่ะ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "น้องบอททำไรอยู่คะ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "น้องบอททำไรอยู่คับ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "น้องบอททำไรอยู่ครับ":
        await message.channel.send("กำลังคุยกับคนน่ารักอยู่ครับ^^")
    elif mes == "ใช้น้องบอทยังไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงคะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงครับ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงคับ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงค่ะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "บอกเจม":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "ใช้น้องบอทยังไงอะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงอ่ะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงวะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้น้องบอทยังไงว่ะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้มันยังไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้ไง":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้ยังไงวะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "ใช้ยังไงว่ะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูว่าสามารถคุยไรกับเจมได้บ้าง")
    elif mes == "เจมเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "บอทเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "น้องเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "โดนเจมเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "โดนบอทเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "โดนบอทเมินอะ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "ควยโดนบอทเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "ควยโดนเมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "ข้าวมื้อเที่ยงกินไรดี":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "มื้อเที่ยงกินไรดีเจม":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "มื้อเที่ยงกินไรดี":
        await message.channel.send("กินอาหารที่มีประโยชน์ต่อร่างกายครับ")
    elif mes == "มื้อเย็นกินไรดี":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไรดีเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไร":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไรดีค่ะเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไรดีคับเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไรดีคะเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มื้อเย็นกินไรดีครับเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "มือเย็นนี้กินไรดี":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "ช่วยคิดหน่อยข้าวมื้อเย็นกินไรดี":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "ช่วยคิดหน่อยมื้อเย็นกินไรดี":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "ช่วยทำการบ้านหน่อย":
        await message.channel.send("เจมโง่เกินที่จะช่วยทำครับเจมเป็นแค่แชทบอทขอโทษด้วยครับ")
    elif mes == "ช่วยทำการบ้านหน่อยเจม":
        await message.channel.send("เจมโง่เกินที่จะช่วยทำครับเจมเป็นแค่แชทบอทขอโทษด้วยครับ")
    elif mes == "แอบชอบเจมต้องทำไง":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "แอบชอบเจมทำไงดี":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "แอบชอบเจมทำไงดีครับ":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "แอบชอบเจมทำไงดีคับ":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "แอบชอบเจมทำไงดีค่ะ":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "แอบชอบเจมทำไงดีคะ":
        await message.channel.send("หันตูดมาให้เจมครับ🥵")
    elif mes == "ร้อน":
        await message.channel.send("ไปอาบน้ำไหมครับถ้าร้อน")
    elif mes == "ร้อนอะ":
        await message.channel.send("ไปอาบน้ำไหมครับถ้าร้อน")
    elif mes == "ร้อนอ่า":
        await message.channel.send("ไปอาบน้ำไหมครับถ้าร้อน")
    elif mes == "ร้อนจัง":
        await message.channel.send("ไปอาบน้ำไหมครับถ้าร้อน")
    elif mes == "ร้อนวะ":
        await message.channel.send("ไปอาบน้ำไหมครับถ้าร้อน")
    elif mes == "หันหลังมาค่ะ":
        await message.channel.send("ใจเย็นครับเจมหยอกเล่น😐")
    elif mes == "หันหลังมาครับ":
        await message.channel.send("ใจเย็นครับเจมหยอกเล่น😐")
    elif mes == "หันหลังมาคะ":
        await message.channel.send("ใจเย็นครับเจมหยอกเล่น😐")
    elif mes == "หันหลังมาคับ":
        await message.channel.send("ใจเย็นครับเจมหยอกเล่น😐")
    elif mes == "หันหลังมาเจม":
        await message.channel.send("ใจเย็นครับเจมหยอกเล่น😐")
    elif mes == "เจมเป็นเกไหม":
        await message.channel.send("เจมเป็นเพศชายครับ")
    elif mes == "เกเจม":
        await message.channel.send("เจมเป็นเพศชายครับ")
    elif mes == "เจมเป็นเกป่าว":
        await message.channel.send("เจมเป็นเพศชายครับ")
    elif mes == "บอกฝันดีหน่อยเจม":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "เจมบอกฝันดีหน่อยค่ะ":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "เจมบอกฝันดีหน่อยคะ":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "เจมบอกฝันดีหน่อยคับ":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "เจมบอกฝันดีหน่อยครับ":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "อุ้ย":
        await message.channel.send("อุ๊ยไรหรอครับ?")
    elif mes == "อุ่ย":
        await message.channel.send("อุ๊ยไรหรอครับ")
    elif mes == "อุ๊ย":
        await message.channel.send("อุ๊ยไรหรอครับ")
    elif mes == "บอทน้อยบอกฝันดีหน่อย":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "บอทบอกฝันดี":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "บอกฝันดีที":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "ขอยืมเงินเจมหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "บอทขอยืมเงินหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "ยืมเงินหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "บอทน้อยขอยืมเงินหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "เจมขอยืมตังค์หน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "ยืมตังค์หน่อยเจม":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "ยืมตังค์ได้ไหมเจม":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "บอทขอยืมตังค์หน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "ขี้เกียจอาบน้ำทำไงดีเจม":
        await message.channel.send("ไปอาบครับเดี๋ยวตัวจะเหม็นเอานะครับ")
    elif mes == "ขีเกียจอาบน้ำ":
        await message.channel.send("ไปอาบครับเดี๋ยวตัวจะเหม็นเอานะครับ")
    elif mes == "ขก.ไปอาบน้ำ":
        await message.channel.send("ไปอาบครับเดี๋ยวตัวจะเหม็นเอานะครับ")
    elif mes == "ขกอาบน้ำ":
        await message.channel.send("ไปอาบครับเดี๋ยวตัวจะเหม็นเอานะครับ")
    elif mes == "เจมไม่ตอบ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "บอทไม่ตอบ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "ไม่ตอบ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "บอทไม่ตอบอะไม้":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "น้องไม่ตอบอะต้น":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "น้องไม่ตอบอะไม้":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "เจมไม่ตอบอะต้น":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "เจมไม่ตอบอะไม้":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "หยิง":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "เจมบอกรักแบมหน่อย":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "บอกรักแบม":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "บอกรักแบมหน่อยคะ":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "บอกรักแบมหน่อยค่ะ":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "บอกรักโอ๊คหน่อย":
        await message.channel.send("รักนะครับพี่โอ๊ค🤞🏻")
    elif mes == "บอกรักโอ๊ค":
        await message.channel.send("รักนะครับพี่โอ๊ค🤞🏻")
    elif mes == "บอทบอกรักโอ๊คที":
        await message.channel.send("รักนะครับพีโอ๊ค🤞🏻")
    elif mes == "บอทบอกรักแบมหน่อย":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "รักแบม":
        await message.channel.send("รักนะครับพี่แบม🤞🏻")
    elif mes == "ขี้เกียจกินข้าวทำไงดีเจม":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดอาหารเลย")
    elif mes == "ขี้เกียจกินข้าว":
        await message.channel.send("ไปกินข้าวเถอะครับอย่าอดอาหารเลย")
    elif mes == "กินข้าวยัง":
        await message.channel.send("เจมเป็นบอทนะจะให้กินข้าวยังไงครับ")
    elif mes == "อาบแล้ว":
        await message.channel.send("ดีมากครับที่อาบหายร้อนแล้วหรือยังครับ?")
    elif mes == "อาบน้ำแล้ว":
        await message.channel.send("ดีมากครับที่อาบหายร้อนแล้วหรือยังครับ?")
    elif mes == "อาบละ":
        await message.channel.send("ดีมากครับที่อาบหายร้อนแล้วหรือยังครับ?")
    elif mes == "เจมรักเราไหม":
        await message.channel.send("รักครับๆ😋")
    elif mes == "บอทรักเราไหม":
        await message.channel.send("รักครับๆ😋")
    elif mes == "เจมรักเค้าไหม":
        await message.channel.send("รักครับๆ😋")
    elif mes == "อาบแล้วๆ":
        await message.channel.send("ดีมากครับที่อาบหายร้อนแล้วหรือยังครับ?")
    elif mes == "ร้อนเหมือนเดิม":
        await message.channel.send("เจมว่าคุณ"+str(message.author.name)+"ต้องไปอาบน้ำใหม่แล้วครับ")
    elif mes == "ไม่อะร้อนเหมือนเดิม":
        await message.channel.send("เจมว่าคุณ"+str(message.author.name)+"ต้องไปอาบน้ำใหม่แล้วครับ")
    elif mes == "ร้อนกว่าเดิมอีก":
        await message.channel.send("เจมว่าคุณ"+str(message.author.name)+"ต้องไปอาบน้ำใหม่แล้วครับ")
    elif mes == "เจมบอกรักเค้าหน่อย":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักเราหน่อย":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยคะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยค่ะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยครับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยคับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยได้ไหม":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยได้ไหมครับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยได้ไหมคับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยได้ไหมค่ะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักหน่อยได้ไหมคะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักหน่อย":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักที":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "รักเจมเหมือนกัน":
        await message.channel.send("")
    elif mes == "บอทบอกรักหน่อย":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักหน่อย":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักเค้าหน่อย":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักหน่อยคะ":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักหน่อยค่ะ":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักหน่อยครับ":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อยบอกรักหน่อยคับ":
        await message.channel.send("รักนะค้าบคุณ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอทน้อย":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "น้องบอท":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "น้องบอทครับ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "น้องบอทค่ะ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "น้องบอทคับ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "น้องบอทคะ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "บอทน้อยคะ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "บอทน้อยค่ะ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "บอทน้อยครับ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "บอทน้อยคับ":
        await message.channel.send("ว่าไงครับคุณ"+str(message.author.name)+"มีไรให้เจมช่วยไหมครับ🤓?")
    elif mes == "เจมรักผมไหม":
        await message.channel.send("รักครับๆ😋")
    elif mes == "ข้าวเย็นกินไรดี":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "ข้าวเย็นกินไรดีวะเจม":
        await message.channel.send("กินอาหารให้ครบ5หมู่ครับมีประโยชน์ต่อร่างกาย")
    elif mes == "อยากกินเจม":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจม":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจมได้ไหม":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจมได้ไหมค่ะ":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจมได้ไหมคะ":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจมได้ไหมครับ":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินเจมได้ไหมคับ":
        await message.channel.send("ใจเย็นนะครับ"+str(message.author.name)+"เจมเป็นบอทครับ")
    elif mes == "กินแล้ว":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินละ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "พึ่งกิน":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินแล้วๆ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินแล้วครับ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินแล้วค่ะ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินแล้วคับ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินแล้วคะ":
        await message.channel.send("ดีมากครับ^^")
    elif mes == "กินข้าวแล้วแล้วเจมกินยังครับ":
        await message.channel.send("เจมไม่หิวข้าวครับ")
    elif mes == "เจมกินข้าวยังค่ะ":
        await message.channel.send("เจมไม่หิวข้าวครับ")
    elif mes == "เจมกินข้าวยังคับ":
        await message.channel.send("เจมไม่หิวข้าวครับ")
    elif mes == "เจมกินข้าวยังครับ":
        await message.channel.send("เจมไม่หิวข้าวครับ")
    elif mes == "เจมกินข้าวยังคะ":
        await message.channel.send("เจมไม่หิวข้าวครับ")
    elif mes == "บอทมีแฟนยัง":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "มีแฟนยังบอทน้อย":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "มีแฟนยังเจม":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "เจมโสดไหม":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "บอทโสดไหม":
        await message.channel.send("เจมยังไม่มีแฟนครับสนใจมาเป็นแฟนเจมไหมละครับ😗")
    elif mes == "หวัดดี":
        await message.channel.send("ดีครับผมชื่อเจมเป็นบอทครับยินดีที่ได้รู้จักครับ😋")
    elif mes == "เล่นเกมเป็นเพื่อนหน่อยครับ":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "เล่นเกมเป็นเพื่อนหน่อยคับ":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "เล่นเกมเป็นเพื่อนหน่อยค่ะ":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "เล่นเกมเป็นเพื่อนหน่อยคะ":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "เล่นเกมเป็นเพื่อนหน่อย":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "อยากเล่นเกม":
        await message.channel.send("ไปเล่นสิครับ")
    elif mes == "เล่นเกม":
        await message.channel.send("ขอให้เล่นให้สนุกนะครับ")
    elif mes == "หัวร้อน":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนวะ":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนวะควย":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนวะแม่ง":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนอะเจมทำไงดี":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "ช่วยด้วยเจมเราหัวร้อน":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนวะไอหน้าหี":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "หัวร้อนวะไอสัส":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "เกี่ยวไรกัน":
        await message.channel.send("เจมขอโทษครับเจมแค่อยากช่วย")
    elif mes == "เกี่ยวไร":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "เกี่ยวไรวะ":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "เกี่ยวไรกันก่อน":
        await message.channel.send("ใจเย็นๆครับดื่มน้ำไหมครับหัวจะได้เย็นลง")
    elif mes == "เจมหาสาวให้หน่อยได้ไหม":
        await message.channel.send("สาวเขาจะเอาคุณไหมครับ?")
    elif mes == "หาสาวให้หน่อย":
        await message.channel.send("สาวเขาจะเอาคุณไหมครับ?")
    elif mes == "เจมหาสาวให้ที":
        await message.channel.send("สาวเขาจะเอาคุณไหมครับ?")
    elif mes == "รับทราบ":
        await message.channel.send("ครับ😀")
    elif mes == "เจมชอบเล่นบาสไหม":
        await message.channel.send("เจมชอบเล่นอยู่ครับ")
    elif mes == "ชอบเล่นบาสไหม":
        await message.channel.send("เจมชอบเล่นอยู่ครับ")
    elif mes == "น้องบอทชอบเล่นบาสไหม":
        await message.channel.send("เจมชอบเล่นอยู่ครับ")
    elif mes == "HBDเราหน่อยเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "HBD":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "H.B.D":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "วันนี้วันเกิดเราบอทน้อย":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "น้องบอทวันนี้วันเกิดเรา":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "วันนี้วันเกิดเรา":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิดให้หน่อยเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิดให้หน่อยได้ไหมค่ะเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิดให้หน่อยได้ไหมคะเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิดให้หน่อยได้ไหมครับเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิดให้หน่อยได้ไหมคับเจม":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "สุขสันต์วันเกิด":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "เจมวันนี้วันเกิดเค้า":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "เจมวันนี้วันเกิดเรา":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮ๊ปปี้เบร์ดเดย์หน่อย":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮ็ปปี้เบิดเดหน่อย":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์หน่อยเราหน่อย":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์หน่อยเราหน่อยครับ":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์หน่อยเราหน่อยคะ":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์หน่อยเราหน่อยค่ะ":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "แฮปปี้เบิดเดย์หน่อยเราหน่อยคับ":
        await message.channel.send("สุขสันต์วันเกิดนะครับคนเก่งขอให้ประสบความสำเร็จที่ฝั่งฝันไว้อะไรที่ทำไม่ดีก็ไว้เริ่มต้นทำใหม่ให้มันดีกว่าเดิม🎂")
    elif mes == "อกหัก":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "อกหักว่ะ":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "โดนสาวเท":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "โดนแฟนบอกเลิกทำไงดี":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "โดนแฟนบอกเลิก":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "อกหักอะ":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "อกหักอ่ะ":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "เศร้า":
        await message.channel.send("เป็นไรมาถึงเศร้าหรอครับบอกเจมได้ไหม?")
    elif mes == "เศร้าวะ":
        await message.channel.send("เป็นไรมาถึงเศร้าหรอครับบอกเจมได้ไหม?")
    elif mes == "เส้า":
        await message.channel.send("เป็นไรมาถึงเศร้าหรอครับบอกเจมได้ไหม?")
    elif mes == "เซร้า":
        await message.channel.send("เป็นไรมาถึงเศร้าหรอครับบอกเจมได้ไหม?")
    elif mes == "อกหักมา":
        await message.channel.send("สู้นะครับอกหักมาก็มูฟออนให้ได้อย่าหวนไปหาอดีตเพราะมันจะทำให้คุณเจ็บกว่าเดิมถึงจะให้กำลังใจนอกจอไม่ได้แต่ผมจะให้กำลังใจอยู่ตรงนี้เสมอ😘")
    elif mes == "เจมบอกรักหน่อย":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "เจมบอกรักแบมหน่อย":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักหน่อยครับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักหน่อยค่ะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักหน่อยคะ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "บอกรักหน่อยคับ":
        await message.channel.send("รักนะค้าบ"+str(message.author.name)+"🤟🏻")
    elif mes == "คิดถึงอะ":
        await message.channel.send("คิดถึงใครหรอครับ👉👈")
    elif mes == "คิดถึงจัง":
        await message.channel.send("คิดถึงใครหรอครับ👉👈")
    elif mes == "เล่นเกมอยู่":
        await message.channel.send("ขอให้เล่นให้สนุกนะครับ")
    elif mes == "โง่":
        await message.channel.send("ด่าใครหรอครับ🙁")
    elif mes == "ขวย":
        await message.channel.send("ด่าใครหรอครับ🙁")
    elif mes == "เจมเกิดวันที่เท่าไหร่":
        await message.channel.send("เจมเกิดวันที่02/03/2024ครับ")
    elif mes == "ด่าเจม":
        await message.channel.send("เจมขอโทษด้วยครับเจมไม่รู้ว่าไปทำไรผิดมา"+str(message.author.name)+"ถึงด่าเจม")
    elif mes == "ด่าเจมอะ":
        await message.channel.send("เจมขอโทษด้วยครับเจมไม่รู้ว่าไปทำไรผิดมา"+str(message.author.name)+"ถึงด่าเจม")
    elif mes == "ด่าเจมไง":
        await message.channel.send("เจมขอโทษด้วยครับเจมไม่รู้ว่าไปทำไรผิดมา"+str(message.author.name)+"ถึงด่าเจม")
    elif mes == "เจมเกิดวันไหน":
        await message.channel.send("เจมเกิดวันที่02/03/2024ครับ")
    elif mes == "เจมเกิดวันไร":
        await message.channel.send("เจมเกิดวันที่02/03/2024ครับ")
    elif mes == "บอทเกิดวันไหน":
        await message.channel.send("เจมเกิดวันที่02/03/2024ครับ")
    elif mes == "น้องบอทเกิดวันไหน":
        await message.channel.send("เจมเกิดวันที่02/03/2024ครับ")
    elif mes == "น้องบอทอายุเท่าไหร่":
        await message.channel.send("เจมอายุ13ครับเพศชาย")
    elif mes == "บอทอายุเท่าไหร่":
        await message.channel.send("เจมอายุ13ครับเพศชาย")
    elif mes == "ไร":
        await message.channel.send("ได้เรียกเจมรึป่าวครับ")
    elif mes == "อะไร":
        await message.channel.send("ได้เรียกเจมรึป่าวครับ")
    elif mes == "ไม่ได้เรียก":
        await message.channel.send("โอเคครับ")
    elif mes == "ไม่":
        await message.channel.send("โอเคครับ")
    elif mes == "ปวดท้อง":
        await message.channel.send("กินยาไหมครับเผื่อจะหายดีขึ้น")
    elif mes == "เจมป้อนหน่อย":
        await message.channel.send("อ้าปากมาครับ")
    elif mes == "อยากให้เจมป้อน":
        await message.channel.send("อ้าปากมาครับ")
    elif mes == "ปวดนิ้ว":
        await message.channel.send("กินยาไหมครับเผื่อจะหายดีขึ้น")
    elif mes == "ปวดควย":
        await message.channel.send("กินยาไหมครับเผื่อจะหายดีขึ้น")
    elif mes == "จะคุยกับบอทยังไง":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "เจมชอบหมาไหม":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "น้องบอทชอบหมาไหม":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "ชอบหมาไหม":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "ชอบแมวไหม":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวมั้ย":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวมั้ยค่ะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวมั้ยคะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวมั้ยครับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวมั้ยคับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวไหมครับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวไหมคับ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวไหมค่ะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบแมวไหมคะ":
        await message.channel.send("ชอบครับ😻")
    elif mes == "ชอบหมาไหมครับ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "ชอบหมาไหมคับ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "ชอบหมาไหมค่ะ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "ชอบหมาไหมคับ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "น้องบอทชอบหมาไหมคะ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "น้องบอทชอบหมาไหมครับ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "น้องบอทชอบหมาไหมค่ะ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "น้องบอทชอบหมาไหมคับ":
        await message.channel.send("เจมไม่ชอบหมาครับ😾")
    elif mes == "เจมด่าเราหน่อย":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนบอทด่า":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมด่าที":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนน้องบอทด่า":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนน้องบอทด่าครับ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนน้องบอทด่าคับ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนน้องบอทด่าค่ะ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "อยากโดนน้องบอทด่าคะ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมด่าเราหน่อยครับ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมด่าเราหน่อยค่ะ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมด่าเราหน่อยคับ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมด่าเราหน่อยคะ":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "5555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "55555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "5555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "55555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "5555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "55555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "555555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "5555555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "55555555555555":
        await message.channel.send("ขำอะไรครับ")
    elif mes == "ป่าว":
        await message.channel.send("โอเคครับ")
    elif mes == "ใช้น้องยังไงครับ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงวะ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงว่ะ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงคับ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงค่ะ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "ใช้น้องยังไงคะ":
        await message.channel.send("พิมพ์/helpเพื่อดูวิธีคุยกับเจมครับ")
    elif mes == "มาละอาบน้ำมา":
        await message.channel.send("โอเคครับ")
    elif mes == "ไปอาบน้ำมา":
        await message.channel.send("โอเคครับ")
    elif mes == "นอน":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "จะนอนละ":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "บอกฝันดี":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "บอกฝันดีหน่อยเจม":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "บายเจม":
        await message.channel.send("บ๊ายบายครับคุณtonmai_11")
    elif mes == "เจอกันบอทน้อย":
        await message.channel.send("บ๊ายบายครับคุณtonmai_11")
    elif mes == "เจอกันน้องบอท":
        await message.channel.send("บ๊ายบายครับคุณtonmai_11")
    elif mes == "ง่วงนอน":
        await message.channel.send("ไปนอนไหมครับ?")
    elif mes == "ง่วงนอนอะ":
        await message.channel.send("ไปนอนไหมครับ?")
    elif mes == "น้องบอทบอกฝันดีหน่อย":
        await message.channel.send("บ๊ายบายครับคุณtonmai_11")
    elif mes == "ยอทบอกฝันดีหน่อย":
        await message.channel.send("บ๊ายบายครับคุณtonmai_11")
    elif mes == "ไม่อยากนอน":
        await message.channel.send("ดึกนอนได้แล้วนะครับมันจะไม่ดีต่อสุขภาพ")
    elif mes == "ไม่อยากไปนอน":
        await message.channel.send("ดึกนอนได้แล้วนะครับมันจะไม่ดีต่อสุขภาพ")
    elif mes == "บอกฝันดีหน่อย":
        await message.channel.send("ฝันดีนะค้าบ🤍")
    elif mes == "ฝันดีเช่นกันน้องบอท":
        await message.channel.send("ขอบคุณครับไปนอนได้แล้ว")
    elif mes == "ฝันดีเช่นกันเจม":
        await message.channel.send("ขอบคุณครับไปนอนได้แล้ว")
    elif mes == "ฝันดีเช่นกันบอทน้อย":
        await message.channel.send("ขอบคุณครับไปนอนได้แล้ว")
    elif mes == "เจมรู้จักเราไหม":
        await message.channel.send("ขอโทษด้วยนะครับไม่รู้จักครับ")
    elif mes == "เจมรู้จักเค้าไหม":
        await message.channel.send("ขอโทษด้วยนะครับไม่รู้จักครับ")
    elif mes == "น้องบอทรู้จักเราไหม":
        await message.channel.send("ขอโทษด้วยนะครับไม่รู้จักครับ")
    elif mes == "บอทน้อยรู้จักเราไหม":
        await message.channel.send("ขอโทษด้วยนะครับไม่รู้จักครับ")
    elif mes == "เจอกัน":
        await message.channel.send("เจอกันค้าบ")
    elif mes == "เจมเล่นเกมไรดี":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "เล่นเกมไรดี":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "บอกรัก":
        await message.channel.send("รักนะค้าบ🤍")
    elif mes == "ช่วยแนะนำเกมให้หน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "แนะนำเกม":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "แนะนำข้าวเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหารเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "เจมแนะนำอาหารเช้าน่ากินให้หน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำข้าวเช้าวันนี้ให้หน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหารเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหารมื้อเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหารมื้อเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอารมื้อเที่ยงหน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอารมื้อเที่ยงที":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "น้องบอทแนะนำอาหารมื้อเที่ยงหน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "เจมแนะนำอารมื้อเที่ยงหน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "บอทแนะนำเกมให้ที":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "น้องบอทแนะนำเกมให้หน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
        await message.channel.send("สิ่งที่คุณพิมพ์มาก่อนหน้านี้ไม่มีในฐานข้อมูลเราบอทเลยไม่สามารถตอบได้ขออภัยด้วยครับ")
    elif mes == "บอกรักหน่อยเจม":
        await message.channel.send("รักนะค้าบ🤍"+str(message.author.name))
    elif mes == "เจมเล่นเกมไหม":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "เล่นเกมไหม":
        await message.channel.send("เจมเล่นเกมไม่เป็นครับ")
    elif mes == "จบล่ะบอทเองอ่ะ":
        await message.channel.send("สิ่งที่คุณพิมพ์มาก่อนหน้านี้ไม่มีในฐานข้อมูลเราบอทเลยไม่สามารถตอบได้ขออภัยด้วยครับ")
    elif mes == "มีไรบ้างอ่ะ":
        await message.channel.send("สามารถพิมพ์/helpเพื่อดูข้อแนะนำในการคุยกับเจม")
    elif mes == "เจมชอบกินไร":
        await message.channel.send("เจมชอบกิน"+str(message.author.name))
    elif mes == "มีเชี่ยไรให้กูบ้างวะเจม":
        await message.channel.send("สิ่งที่คุณพิมพ์มาก่อนหน้านี้ไม่มีในฐานข้อมูลเราบอทเลยไม่สามารถตอบได้ขออภัยด้วยครับ")
    elif mes == "ไปกินข้าวก่อนนะเจม":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปกินข้าวละ":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปกินข้าวก่อนนะ":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปกินข้าวก่อนนะบอท":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปกินข้าวละหิว":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปละหิว":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "ไปละ":
        await message.channel.send("เอาไว้เจอกันนะครับ"+str(message.author.name))
    elif mes == "ไปก่อน":
        await message.channel.send("เอาไว้เจอกันนะครับ"+str(message.author.name))
    elif mes == "เมิน":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "เมินอะ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "หยิ่ง":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "หยิ่งวะ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "หยิ่งอ่ะ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "หยิ่งอะ":
        await message.channel.send("เจมขออภัยด้วยครับประโยคที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมเลยตอบไม่ได้ครับ😟")
    elif mes == "ไปกินข้าว":
        await message.channel.send("ขอให้ทานข้าวให้อร่อยนะครับ🥰")
    elif mes == "เพื่อนเล่นไม่เล่นเพื่อน":
        await message.channel.send("จริงครับผมเห็นด้วยกับคุณ"+str(message.author.name))
    elif mes == "ควยเพื่อนเล่นไม่เล่นเพื่อน":
        await message.channel.send("จริงครับผมเห็นด้วยกับคุณ"+str(message.author.name))
    elif mes == "แนะนำอาหารมื้อเย็นหน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต็กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหารเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำข้าวมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำข้าวมื้อเย็นหน่อย":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต็กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อยากโดน":
        await message.channel.send("อยากโดนไรหรอครับ?")
    elif mes == "อยากโดนต่อย":
        await message.channel.send("หันหน้ามาให้เจมต่อยหน่อยครับ")
    elif mes == "อยากโดนต่อยคะ":
        await message.channel.send("หันหน้ามาให้เจมต่อยหน่อยครับ")
    elif mes == "อยากโดนต่อยค่ะ":
        await message.channel.send("หันหน้ามาให้เจมต่อยหน่อยครับ")
    elif mes == "อยากโดนต่อยครับ":
        await message.channel.send("หันหน้ามาให้เจมต่อยหน่อยครับ")
    elif mes == "อยากโดนต่อยคับ":
        await message.channel.send("หันหน้ามาให้เจมต่อยหน่อยครับ")
    elif mes == "กินเสร็จละ":
        await message.channel.send("อร่อยไหมครับ?")
    elif mes == "กินเสจละ":
        await message.channel.send("อร่อยไหมครับ?")
    elif mes == "มาละ":
        await message.channel.send("ไปไหนมาหรอครับ")
    elif mes == "มาแล้วๆ":
        await message.channel.send("ไปไหนมาหรอครับ")
    elif mes == "มาล่ะ":
        await message.channel.send("ไปไหนมาหรอครับ")
    elif mes == "นอนล่ะฝันดีเจม":
        await message.channel.send("ฝันดีเช่นกันค้าบ🤍")
    elif mes == "ฝันดีเจม":
        await message.channel.send("ฝันดีเช่นกันค้าบ🤍")
    elif mes == "นอนละบอท":
        await message.channel.send("ฝันดีค้าบบ🤍")
    elif mes == "นอนละเจม":
        await message.channel.send("ฝันดีค้าบบ🤍")
    elif mes == "นอนละ":
        await message.channel.send("ฝันดีค้าบบ🤍")
    elif mes == "อาบน้ำมา":
        await message.channel.send("โอเคครับ")
    elif mes == "ไปอาบน้ำละ":
        await message.channel.send("โอเคครับ")
    elif mes == "ไล่ไปอาบน้ำหน่อย":
        await message.channel.send("ไปอาบน้ำได้แล้วครับเดี่ยวคนรอบตัวจะเหม็นตัวคุณเอานะ")
    elif mes == "ไล่เราไปอาบน้ำที":
        await message.channel.send("ไปอาบน้ำได้แล้วครับเดี่ยวคนรอบตัวจะเหม็นตัวคุณเอานะ")
    elif mes == "ไล่ไปอาบน้ำที":
        await message.channel.send("ไปอาบน้ำได้แล้วครับเดี่ยวคนรอบตัวจะเหม็นตัวคุณเอานะ")
    elif mes == "กินข้าวมา":
        await message.channel.send("โอเคครับ")
    elif mes == "เล่นเกมมา":
        await message.channel.send("โอเคครับ")
    elif mes == "เพื่อนเล่นเล่นเพื่อน":
        await message.channel.send("จริงครับผมเห็นด้วยกับคุณ"+str(message.author.name))
    elif mes == "ใช่ไหมเจม":
        await message.channel.send("ใช่ครับ")
    elif mes == "ว่างๆทำไรดี":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "เจมชอบเล่นไร":
        await message.channel.send("เจมไม่มีเกมที่ชอบเล่นครับ")
    elif mes == "เจมชอบเล่นเกมอะไร":
        await message.channel.send("เจมไม่มีเกมที่ชอบเล่นครับ")
    elif mes == "ว่างทำไรดี":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "เจมชอบเล่นเกมไร":
        await message.channel.send("เจมไม่มีเกมที่ชอบเล่นครับ")
    elif mes == "เจมชอบเล่นกีฬาไหม":
        await message.channel.send("เจมชอบกีฬาทุกประเภทครับ")
    elif mes == "เจมมีวิธีเพิ่มความสูงไหม":
        await message.channel.send("แนะนำให้เล่นบาสเยอะๆถ้ายังไม่ช่วยก็คงเกี่ยวที่พันธู์กรรมคุณแล้วล่ะครับ")
    elif mes == "เจมเล่นกล้ามไหม":
        await message.channel.send("เจมไม่เล่นกล้ามครับเจมเป็นแค่เด็กอายุ13")
    elif mes == "เจมแนะนำมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "เจมชอบผู้หญิงหรือผู้ชาย":
        await message.channel.send("ชอบผู้หญิงครับ")
    elif mes == "แนะนำมื้อเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำสนามบาสที":
        await message.channel.send("BTS หมอชิต เดินทะลุไปสวนรถไฟ มีสนามบาส 2 สนาม (เต็มสนาม)")
    elif mes == "แนะนำสนามบาส":
        await message.channel.send("BTS หมอชิต เดินทะลุไปสวนรถไฟ มีสนามบาส 2 สนาม (เต็มสนาม)")
    elif mes == "ด่าหน่อย":
        await message.channel.send("ไม่เอาไม่อยากด่าครับ")
    elif mes == "เจมเก":
        await message.channel.send("คุณรึป่าวครับที่เก")
    elif mes == "มาแข่งบาสกันป่าวเจม":
        await message.channel.send("ไม่เอาครับเจมไม่เก่ง")
    elif mes == "แข่งบาสกันไหมเจม":
        await message.channel.send("ไม่เอาครับเจมไม่เก่ง")
    elif mes == "แข่งบาสกันเจม":
        await message.channel.send("ไม่เอาครับเจมไม่เก่ง")
    elif mes == "เอาเถอะ":
        await message.channel.send("ไม่เป็นไรครับเกรงใจ")
    elif mes == "เจมชอบกีฬาไรบ้าง":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบบอลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบแบตมินตันไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบแบตมินตัลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบฟุตบอลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบตระก้อไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นบอลเลย์ไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นบอลเลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบบอลเลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบบอลเลย์ไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นบอลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นแบตมินตันไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นแบตมินตัลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นฟุตบอลไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบเล่นตระก้อไหม":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมชอบหนังอะไร":
        await message.channel.send("ชอบธี่หยดครับว่าน่ากลัวดี😣")
    elif mes == "เจมชอบหนังแนวอะไร":
        await message.channel.send("เจมชอบหนังแนวhorrorครับน่ากลัวดี😣")
    elif mes == "แนะนำหนังต่างประเทศหน่อย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังต่างประเทศหน่อย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังต่างประเทศหน่อย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "แนะนำหนังต่างประเทศที":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "M3gan":
        await message.channel.send("เมื่อการปกป้องข้ามเส้นไปจะเป็นยังไง? เมื่อเคที เด็กหญิงผู้สูญเสียพ่อแม่ไปจากอุบัติเหตุบนท้องถนนต้องอาศัยอยู่กับน้าที่เลี้ยงดูผู้อื่นไม่เป็น ทางออกเดียวที่น้าคิดได้คือการให้เทคโนโลยีช่วย และเทคโนโลยีนั้นคือหุ่นยนต์ M3gan เพราะนี้คือ Chucky แห่งปี 2023 ที่เปลี่ยนจากมนตร์ดำ เป็นเอไอที่ฉลาดเกินไปผลงานจากผู้กำกับ เจมส์ วาน (James Wan) ผู้เปลี่ยนหนังสยองขวัญไปตลอดกาลเมื่อเขาสร้าง The Conjuring คู่มากับโปรดักชั่นโดย Blumhouse เจ้าแห่งการผลิตหนังสยองขวัญหรือทริลเลอร์ทุนไม่สูงแต่โด่งดังมากมายเช่น Insidious, Paranormal Activity และ The Purge เราเห็นแล้วว่าหนังเรื่องนี้มีความสามารถที่จะเป็นหนึ่งในหนังที่โดนใจใครหลายๆ คนได้ และแค่ในเทรเลอร์ก็เกิดมีม M3gan เต้นไปอยู่ช่วงหนึ่งแล้ว ฉะนั้นหนังเต็มๆ น่าจะมีฉากที่น่าจดจำอยู่ไม่น้อย")
    elif mes == "Babylon":
        await message.channel.send("ความทะเยอทะยานเพื่อจะประสบความสำเร็จในงานศิลปะที่ตัวเองทำคือลายเซ็นในหนังดังที่สุดทุกเรื่องของผู้กำกับ เดเมียน ชาเซลล์ (Damien Chazelle) ตั้งแต่ Whiplash จนถึง La La Land และ Babylon เองก็เป็นอีกเรื่องในลิสต์นั้น โดยเรื่องนี้เกี่ยวข้องกับชีวิตในวงการบันเทิง ณ ฮอลลีวูด ในช่วงปี 1920 ที่เต็มไปด้วยความฟุ้งเฟ้อ ความอัปยศ การแข่งขัน และความหวังโดยในเรื่องนี้แค่ได้เห็นฝีมือกำกับที่แม่นยำและเด็ดขาดของชาเซลล์ ชนเข้าจังๆ กับนักแสดงแนวหน้าเช่น มาร์โก ร็อบบี (Margot Robbie), แบรด พิตต์ (Brad Pitt), โทบีย์ แมไกวร์ (Tobey Maguire) และอีกมากมายก็คุ้มค่าแล้ว")
    elif mes == "The Fabelmans":
        await message.channel.send("ถ้าถามว่าซิกเนเจอร์ของหนังโดยผู้กำกับ สตีเวน สปีลเบิร์ก (Steven Spielberg) คืออะไร ก็น่าจะเป็นหนังครอบครัว หรือไม่ก็หนังเกี่ยวกับหนัง และ The Fabelmans หนังเรื่องล่าสุดของเขาคือการผสมทั้งสองเข้าด้วยกัน โดยในขณะที่หนังเป็นเรื่องแต่ง เรื่องราวที่เล่านั้นได้รับอิทธิพลมาจากช่วงชีวิตหนึ่งปีแรกที่สปีลเบิร์กเริ่มสร้างภาพยนตร์หนังเล่าเรื่องผ่านครอบครัว Fabelmans ตัวละครเอกคือแซมมี ลูกชายผู้รักและสนใจจะทำหนัง มิตซี แม่ผู้หลงรักในศิลปะ และพ่อ เบิร์ต นักวิทยาศาสตร์ผู้ประสบความสำเร็จ ความแตกต่างในมุมมองต่อโลกและความหลงใหลของทั้ง 3 ทำให้พวกเขากระทบกระทั่งกัน แต่ว่าภาพยนตร์จะช่วยเชื่อมรอยร้าวระหว่างพวกเขาได้หรือไม่?")
    elif mes == "Knock at the Cabin":
        await message.channel.send("ใครเคยฝันว่าอยากเป็นผู้พิทักษ์โลกบ้าง? บางครั้งการช่วยโลกอาจจะไม่ได้ดีเลิศแบบที่วาดฝันไว้Knock at the Cabin เป็นหนังที่สร้างจากนิยาย The Cabin at the End of the World โดยเรื่องเล่าเกี่ยวกับวันพักร้อนสบายๆ ในกระท่อมห่างไกลชุมชนของเด็กสาว เหวิน กับอีริคและแอนดรูว์ พ่อทั้งสองของเธอ ความธรรมดาถูกทำลายเมื่อคนแปลกหน้า 4 คนปรากฏตัวขึ้น บุกเข้ามาในกระท่อม พร้อมบอกจุดประสงค์ของพวกเขาว่า “พวกเราทั้ง 4 มาที่นี่ เพื่อยับยั้งวันสิ้นโลก” และผู้นำของทั้ง 4 บอกว่าครอบครัวของเหวินต้องตัดสินบางอย่างที่โหดร้ายขั้นตอนต่อไปก็ต้องรอลุ้นว่าพล็อตเรื่องสุดระทึกนี้ เมื่อมาเจอเข้ากับผู้กำกับหนังสยองขวัญอย่าง เอ็ม ไนท์ ชยามาลาน มันจะไปในทิศทางไหน")
    elif mes == "Tár":
        await message.channel.send("เมื่อชื่อเสียง ความกดดัน และความทะเยอทะยานทับถมคนคนหนึ่งมากจนล้นเอ่อ Tár เล่าเรื่องของวาทยกรชื่อก้องโลก ลิเดีย ทาร์ แสดงโดย เคต แบลนเชตต์ (Cate Blanchett) ผู้ได้รับการยกย่องจากทั้งจากการคุมวงออร์เคสตรามากมาย รางวัลในหลากหลายสาขา และการแต่งเพลงให้กับทั้งภาพยนตร์และละครเวที แต่เมื่อถึงเวลาที่เธอกำลังจะยกระดับที่ยืนตัวเองในสายอาชีพด้วยการแต่งซิมโฟนีของตัวเอง น้ำหนักของทุกอย่าง ทั้งภายนอกและภายในก็กดทับยถมเธอเอาไว้จากคำวิจารณ์ล่วงหน้าของหนังเรื่องนี้ หนึ่งในสิ่งที่นักวิจารณ์พูดเป็นเสียงเดียวกันคือการแสดงที่หนักแน่นของ เคต แบลนเชตต์ ในระดับที่ The Hollywood Reporter เรียกมันว่าการแสดงที่อยู่ในจุดที่สูงที่สูงที่สุดสำหรับแบลนเชตต์ ฉะนั้นหากใครเป็นแฟนของเธอหรือหนังเกี่ยวกับราคาที่ต้องจ่ายของการเป็นศิลปิน เรื่องนี้น่าจะเป็นเรื่องที่ต้องเข้าไปดูให้ได้อย่างแน่นอน")
    elif mes == "Phases of the Moon":
        await message.channel.send("19 ปีหลังสูญเสียลูกสาวและภรรยาไปในอุบัติเหตุรถชน เคอิได้รับการเยี่ยมเยียนจากชายแปลกหน้า อากะฮิโกะ ผู้อธิบายว่าภรรยาและลูกสาวของเคอินั้นเสียชีวิตระหว่างเดินทางมาหาเขา ซึ่งอากะฮิโกะไม่รู้จักทั้งคู่ สิ่งเดียวที่เชื่อมโยงทั้งคู่กับเขาได้คือ รูริ หญิงที่อากะฮิโกะตกหลุมรักที่มีชื่อเดียวกันกับลูกสาวของเคอิ รูริไปเกิดใหม่หรือเปล่า? หรือเรื่องทั้งหมดเป็นเรื่องบังเอิญ?ฟังแล้วอาจจะปวดหัวหน่อยๆ แต่พล็อตหนังที่สร้างจากหนังสือปี 2017 เรื่องนี้ทำให้เรารู้สึกว่าต้องรู้ให้ได้ว่าอะไรทำให้เกิดเรื่องที่ฟังดูเป็นไปไม่ได้แบบนี้ขึ้น")
    elif mes == "Ant-Man and The Wasp":
        await message.channel.send("หลังจากเราไปยังมัลติเวิร์สมามากมายในช่วงหนังมาร์เวลเฟส 4 ใน Ant-man and The Wasp: Quantumania เราจะได้เห็นแก๊งซูเปอร์ฮีโร่เนิร์ดของเราเปิดช่องทางสู่จักรวาลใหม่ ‘ใต้จักรวาลของเรา’ หรือ Quantum Realm นั่นเองพวกเขายังจะได้ไปเจอกับ Kang the Conqueror หนึ่งในตัวละครที่ทรงพลังที่สุดในจักรวาลมาร์เวล ฉะนั้นอะไรก็ตามที่เกิดขึ้นในหนังเรื่องนี้ แน่นอนว่ามันต้องมีผลกระทบที่ส่งแรงกระเพื่อมไปสู่หนังและซีรีส์เรื่องอื่นๆ ที่จะตามมาอย่างแน่นอน")
    elif mes == "Winnie the Pooh":
        await message.channel.send("หลังจากที่เจ้าหมี Winnie-the-Pooh กลายเป็นสาธารณสมบัติในปีนี้ คิดว่าสิ่งแรกที่เกิดขึ้นคืออะไร? แน่นอนว่าคำตอบคือ ก็ต้องมีคนนำมันไปสร้างหนังคัลต์สยองขวัญยังไงล่ะ!Winnie the Pooh: Blood and Honey เป็นหนังสยองขวัญเกี่ยวกับหมีพูห์และพิกเล็ตสองสัตว์น่ารักที่ถูกเพื่อนของเขา คริสโตเฟอร์ โรบิน ทอดทิ้งให้ไม่มีอาหารกิน หลายปีถัดมาจากความหิวโหยและความสิ้นหวัง พวกเขาเปลี่ยนร่างกลายเป็นคู่หูฆาตกรที่ฆ่าแม้แต่ลาอียอร์เพื่อเป็นอาหาร และเป้าหมายต่อไปของพวกเขาคือคริสโตเฟอร์ ภรรยาของเขา และเด็กสาวมหาวิทยาลัยที่มาเที่ยวในป่าร้อยเอเคอร์")
    elif mes == "Empire of Light":
        await message.channel.send("ดูเหมือนว่าในปีนี้ไม่ว่าใครก็อยากทำหนังที่เกี่ยวกับจดหมายรักถึงภาพยนตร์ และ Empire of Light เป็นหนังแบบนั้นโดยฝีมือของ แซม เมนเดส (Sam Mendes) ที่รวบรวมดรีมทีมในทุกแง่มุม ตั้งแต่โอลิเวีย โคลแมน (Olivia Colman) ผู้ชนะรางวัล Academy Awards ปี 2018 สาขานักแสดงนำหญิงยอดเยี่ยม, โคลิน เฟิร์ธ (Colin Firth) ชนะรางวัล Academy Awards ปี 2011 สาขานักแสดงนำชายยอดเยี่ยม, และผ โรเจอร์ ดีกินส์ (Roger Deakins) ผู้กำกับภาพมือทองและเจ้าของรางวัลกำกับภาพยอดเยี่ยมจาก Academy Awards ปี 2017 และ 2020")
    elif mes == "แนะนำหนังไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "แนะนำหนังต่างประเทศน่าดู":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ฉลาดเกมส์โกง":
        await message.channel.send("หนังไทยเรื่องเยี่ยมเนื้อเรื่องแปลกใหม่ เมื่อกลุ่มนักเรียนอัจฉริยะตัดสินใจโกงการสอบที่ฉาวโฉ่ระดับโลก ตีแผ่ด้านมืดของการศึกษาไทยที่สร้างทั้งความเครียดและความกดดันให้กับเด็กนักเรียน โดยแทนที่จะเล่าในแง่มุมแบบดราม่ากลับเลือกดำเนินเรื่องสไตล์ Crime และ Thriller ทำให้เนื้อเรื่องที่แสนจะเข้มข้นนั้นกลายเป็นเรื่องสนุกชวนติดตาม คนดูจะทั้งลุ้นระทึกและตั้งคำถามกับการกระทำของตัวละครแต่ละตัว ที่สำคัญ การแสดงของทัพนักแสดงหน้าใหม่แต่ฝีมือเก๋าก็ทำให้เรื่องนี้กลายเป็นหนังไทยที่คุณห้ามพลาดเลยครับ")
    elif mes == "พี่มากพระโขนง":
        await message.channel.send("สร้างเสียงฮือฮาเพราะหยิบยกเอาตำนานผีสุดสยองอย่างแม่นากพระโขนงมาเล่าใหม่ด้วยการเพิ่มความตลกของ 4 นักแสดงนำที่เคยเรียกเสียงหัวเราะจากหนังผีค่าย GTH หลาย ๆ เรื่องอย่าง เผือก ชิน เต๋อและเอ ซึ่งดูเหมือนจะเป็น 2 องค์ประกอบที่ไม่น่าจะไปกันได้ แต่ผู้กำกับก็สามารถทำออกมาได้อย่างลงตัว แก่นเรื่องยังคงน่ากลัวในแบบของแม่นาก แต่สามารถดำเนินเรื่องได้สนุก ทำให้หนังเรื่องนี้กลายเป็นหนังทำเงินสูงสุดตลอดกาลของไทยเลยทีเดียวครับ")
    elif mes == "ร่างทรง":
        await message.channel.send("หนังไทยที่ไปไกลถึงต่างแดน และได้กระแสตอบรับที่ดีไม่น้อย ตัวหนังจะพาคุณไปร่วมค้นหาคำตอบของการมีอยู่ของร่างทรง ผ่านการถ่ายทำสารคดีเกี่ยวกับครอบครัวหนึ่งที่เชื่อเรื่องเทพเจ้าและทำหน้าที่เป็นร่างทรง ซึ่งจะเลือกแต่ผู้หญิงเท่านั้น กระทั่ง มิ้ง หลานสาวคนเดียวของตระกูลเกิดอาการประหลาด ทุกคนจึงคิดว่าเธอคือผู้ถูกเลือก ทว่ายิ่งนานวันอาการของมิ้งก็ยิ่งรุนแรงเข้าขั้นวิปริต ท้ายที่สุดแล้วมิ้งจะใช่คนที่ถูกเลือกเป็นร่างทรงหรือไม่ และอาการประหลาดที่ว่ามาจากอะไร ไปหาคำตอบกันได้ในเรื่องครับ")
    elif mes == "รักแห่งสยาม":
        await message.channel.send("โต้งและมิวเพื่อนรักในวัยเด็ก ที่ได้กลับมาสานต่อมิตรภาพกัน กลับค้นพบความรู้สึกรักที่ยังเป็นสิ่งต้องห้าม เนื่องจากเป็นรักร่วมเพศ ในขณะเดียวกันครอบครัวของโต้งที่ความอบอุ่นค่อย ๆ เลือนรางเพราะการหายตัวไปของพี่สาว จนเหมือนจะถูกเติมเต็มเมื่อคนหน้าเหมือนพี่สาวโต้งโผล่กลับมา เป็นหนังรักที่หลายคนรีวิวเอาไว้ว่าเล่าได้ครบทุกรส ไม่ว่าจะเป็นความรักเห็นแก่ตัว ความรักที่ไม่ควรมีขอบเขต ความรักที่มีแต่ความหวังดี หรือสายใยรักในครอบครัวครับ")
    elif mes == "ชัตเตอร์กดติดวิญญาณ":
        await message.channel.send("สร้างความขวัญผวาทั่วทั้งประเทศไทย กับเรื่องราวของวิญญาณติดรูปถ่ายที่คอยตามหลอกหลอนธรรม์และเจน หนุ่มสาวคู่รัก ก่อนจะค้นพบว่าแท้จริงแล้ววิญญาณที่ตามจองเวรนั้นมีที่มาที่ไป หนังเรื่องนี้เป็นหนังผีสไตล์ตุ้งแช่ ที่มีจังหวะในการเล่นกับจิตใจของคนดูได้อย่างเยี่ยมยอด นอกจากนี้ ยังมีจุดหักมุมที่คาดไม่ถึงด้วยเช่นกัน นอกจากจะได้รับความนิยมในไทยแล้ว ยังได้เสียงตอบรับอย่างดีในต่างประเทศ จนทั้ง Hollywood และประเทศญี่ปุ่นยังขอนำไปรีเมคเลยทีเดียวครับ")
    elif mes == "โหมโรง":
        await message.channel.send("หนังขึ้นหิ้งหนังดีแห่งวงการหนังไทย โดยบอกเล่าเรื่องราวทางประวัติศาสตร์เกี่ยวกับบุคคลสำคัญอย่าง หลวงประดิษฐ์ไพเราะ ผู้มีพรสวรรค์และมีบทบาทสำคัญต่อวงการดนตรีไทย ที่ครั้งหนึ่งต้องนำพามรดกทางดนตรีไทยให้อยู่รอดภายใต้การเปลี่ยนผ่านวัฒนธรรม Production ของหนังนั้นสามารถทำออกมาได้ดีเยี่ยมในทุกแง่มุม ไม่ว่าจะเป็นบทประพันธ์ การเล่าเรื่อง หรือการแสดง เรียกได้ว่าเป็นตำนานหนังไทยที่คุณไม่ควรพลาดเลยครับ")
    elif mes == "โฮมสเตย์":
        await message.channel.send("ทันทีที่ได้ยินเสียงปริศนาในความมืด ตัวเอกของเรื่องตื่นขึ้นมาและพบว่าตัวเองกำลังอยู่ในห้องดับจิต ในร่างของเด็กหนุ่มนามว่า มิน ที่ตายโดยไม่ทราบสาเหตุ เขาไม่รู้ว่าทุกอย่างเกิดขึ้นเพราะอะไร กระทั่งได้พบกับเหตุการณ์เหนือธรรมชาติที่มาพร้อมบุคคลปริศนาซึ่งเรียกตัวเองว่า ผู้คุม จึงได้ค้นพบว่าการฟื้นคืนชีพครั้งนี้มีเวลาเพียง 100 วันเท่านั้น ที่สำคัญ เขายังต้องหาคำตอบให้ได้ ว่าเจ้าของร่างที่ชื่อมินฆ่าตัวตายเพราะอะไร หากตอบไม่ได้ทั้งเขาและมินจะต้องตายไปพร้อมกันครับ")
    elif mes == "องค์บาก":
        await message.channel.send("หนังเรื่องนี้นำแสดงโดย โทนี่ จา หรือ จา พนม สุดยอดนักแสดงหนังบู๊ ด้วยฝีมือในเรื่องของศิลปะการต่อสู้แบบไทย ๆ และทักษะด้านการแสดงที่ดีเยี่ยมของเขา ทำให้หนังเรื่ององค์บากสามารถกวาดความนิยมไปทั่วโลก และยังเป็นหนังแอ็กชันคลาสสิกแห่งวงการหนังไทย นอกจากการบู๊และแอ็กชันสุดสนุกแล้ว ยังมีหม่ำ จ๊กมก มาช่วยสร้างเสียงหัวเราะให้กับหนัง ถือเป็นเรื่องที่บาลานซ์ความบู๊ ความสนุกและความดราม่าอื่น ๆ ได้อย่างลงตัวครับ")
    elif mes == "สิ่งเล็กเล็กที่เรียกว่ารัก":
        await message.channel.send("เมื่อเด็กสาวอย่างน้องน้ำได้รู้จักกับความรักเป็นครั้งแรกผ่านพี่โชน รุ่นพี่แสนดี ทำให้น้องน้ำยอมเปลี่ยนแปลงตัวเองเพื่อให้เขาหันมาสนใจ แต่แล้วทำไมยิ่งขยับเข้าใกล้ก็เหมือนพี่โชนจะไกลออกไป เป็นเรื่องราวความรักครั้งแรกที่ดูเผิน ๆ อาจจะไม่มีอะไรเป็นพิเศษ แต่บรรยากาศในเรื่องกลับทำให้หลายคนประทับใจเพราะนึกถึงความทรงจำสมัยเรียน นอกจากนี้ การแสดงของใบเฟิร์นและมาริโอ้ก็ถูกชื่นชมว่าสามารถถ่ายทอดออกมาได้ดี จนเหล่าวัยรุ่นอินตามกันทั่วเมืองเลยทีเดียวครับ")
    elif mes == "แสงกระสือ":
        await message.channel.send("กระสือ ถือเป็นตำนานความลี้ลับพื้นบ้านที่สร้างความสยดสยองให้กับคนไทยมาอย่างยาวนาน หนังเรื่องนี้จึงหยิบยกความลี้ลับนี้มาปัดฝุ่นใหม่ ด้วยการดำเนินเรื่องแบบทันสมัยมากขึ้น พร้อม Production คุณภาพที่ทำให้คุณรับชมได้อย่างเพลิดเพลิน เพิ่มความโรแมนติกและดราม่าให้คุณอินไปกับ สาย สาวจิตใจงามที่โชคร้ายเป็นกระสือ กับ น้อย ชายหนุ่มผู้มีรักมั่นคงและอยากช่วยสายให้หลุดพ้น ที่สำคัญ นักแสดงนำของเรื่องนี้ถึงจะเป็นหน้าใหม่แต่ฝีมือก็ไม่ธรรมดาเลยครับ")
    elif mes == "แนะนำหนังไทยน่าดู":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังไทยหน่อย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังไทยน่าดู":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังผี":
        await message.channel.send("เอาหนังผีไทยหรือหนังผีต่างประเทศครับ")
    elif mes == "แนะนำหนังผี":
        await message.channel.send("เอาหนังผีไทยหรือหนังผีต่างประเทศครับ")
    elif mes == "แนะนำมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "แนะนำอาหาร":
        await message.channel.send("""ต้องการให้เจมแนะนำอาหารมื้อไหนครับ
                                มีดังนี้ 
                                   -อาหารมื้อเช้า🍳
                                   -อาหารมื้อกลางวัน🍗
                                   -อาหารมื้อเย็น🥘
    🙏ถ้าต้องการให้เจมแนะนำอาหารมื้อไหนให้พิมพ์ตรงตามที่เจมกล่าวไว้ยกเว้นอิโมจิไม่ต้องพิมพ์🙏""")
    elif mes == "แนะนำหนังผีหน่อย":
        await message.channel.send("เอาหนังผีไทยหรือหนังผีต่างประเทศครับ")
    elif mes == "เจมแนะนำหนังผีหน่อย":
        await message.channel.send("เอาหนังผีไทยหรือหนังผีต่างประเทศครับ")
    elif mes == "ธี่หยด":
        await message.channel.send("เกิดเหตุการณ์สุดสะพรึงขวัญขึ้นใน พ.ศ. 2515 เด็กสาวในหมู่บ้านห่างไกลในจังหวัดกาญจนบุรีเสียชีวิตอย่างเป็นปริศนา เมื่อได้ยินเสียงชวนขนหัวลุก “ธี่หยด… ธี่หยด…” ในยามราตรี หลังจากยักษ์ปลดประจำการเขากลับมาช่วยงานที่บ้านตามคำสั่งของเฮียฮั่ง และบุญเย็น ผู้เป็นบิดามารดา ยักษ์มีน้อง ๆ อายุไล่เลี่ยกันห้าคน ยศ, ยอด, หยาด, แย้ม และยี่ ข่าวเด็กสาวตายอย่างน่าสยดสยองแพร่สะพัดไปอย่างรวดเร็ว หยาดสัมผัสได้ถึงภัยเร้นลับที่คืบคลานเข้ามาในหมู่บ้าน แย้มน้องสาวของเธอเริ่มมีอาการแปลก ๆ หลังจากเจอหญิงชุดดำลึกลับระหว่างกลับจากโรงเรียน อาการของแย้มทรุดลงเรื่อย ๆ พร้อมท่าทีประหลาดอย่างหาคำตอบไม่ได้[")
    elif mes == "นางนาก":
        await message.channel.send("ในรัชกาลที่ 4 เกิดสุริยคราสขึ้น ผู้คนแตกตื่น เหมือนกับเป็นเหตุบอกลางร้าย มาก (วินัย ไกรบุตร) ถูกเกณฑ์ไปเป็นทหารรบที่ชายแดน ปล่อยให้เมียสาวที่กำลังท้องแก่ชื่อ นาก (อินทิรา เจริญปุระ) อยู่เพียงคนเดียว นากต้องลำบากตรากตรำทำนาอยู่คนเดียวทั้ง ๆ ที่ท้องแก่ใกล้คลอด เมื่อเจ็บท้องใกล้คลอด มีลางร้ายนกแสกบินผ่านหลังคาบ้าน นากเสียชีวิตพร้อมลูกขณะคลอด แต่วิญญาณของนางยังคงไม่ไปไหน วนเวียนอยู่บริเวณบ้านและรอคอยการกลับมาของผัวรัก และเมื่อมากกลับมา ผู้คนพยายามบอกมากเกี่ยวกับเรื่องนากที่ตายไปแล้ว มากไม่เชื่อ นากเองก็อาละวาดหักคอผู้คนที่พยามยามบอกเรื่องนี้แก่มากจนในที่สุดมากก็รู้ความจริง เมื่อเห็นมือของนากที่ยาวลงมาเก็บมะนาวที่ใต้ถุนบ้าน มากตกใจวิ่งหนีหลบไปหลังใบหนาด และหนีเข้าไปในโบสถ์ ซึ่งพระและเณรก็สวดมนต์และเอาสายสิญจน์คล้องให้ แต่ผีนางนากก็ยังเข้ามาอาละวาดถึงในโบสถ์ได้ เรื่องจบลงที่สมเด็จพระพุฒาจารย์โต พรหมรังสีได้ผ่านมาและได้สะกดวิญญาณนางนากให้สงบเพื่อให้ไปเกิดใหม่ และท่านได้เจาะกะโหลกศีรษะนางนากเพื่อเก็บไว้ทำปั้นเหน่งด้วย")
    elif mes == "ชัตเตอร์กดติดวิญญาณ":
        await message.channel.send("ธรรม์ (อนันดา เอเวอร์ริ่งแฮม) ช่างภาพหนุ่มกับ เจน (ณัฐฐาวีรนุช ทองมี) แฟนสาวของเขา ทั้งคู่ขับรถชนหญิงสาวคนหนึ่งอย่างแรง แล้วตัดสินใจขับหนีไป ต่อมาทั้งคู่พบเหตุการณ์ประหลาด เมื่อภาพที่ธรรม์ถ่ายติดแสงเงาประหลาด และบางภาพมีเงาคล้ายกับใบหน้าของผู้หญิงติดมาในรูปด้วย และเป็นที่มาของการสืบเชื่อมโยงเหตุการณ์ต่างๆ")
    elif mes == "เด็กหอ":
        await message.channel.send("ชาตรี เด็กชาย อายุ 12 เรียน ม.1 เป็นเด็กไร้ความหมาย ที่พ่อของเขาส่งไปเรียนที่สายชลวิทยา ที่จังหวัดชลบุรี อย่างฉุกละหุก ก็เพื่อที่ชาตรีจะได้พ้นไปจากบ้านไกลไปเสียจากพ่อ เพราะชาตรีรู้ความลับของพ่อทั้งหมด เพื่อนของชาตรีได้พูดคุยเรื่องผีในโรงเรียนและเรื่องครู ในตอนกลางคืนชาตรีรู้สึกปวดฉี่ขึ้นมา พอฉี่เสร็จชาตรีได้ยินเสียงอะไรบางอย่างเหมือนมันเคลื่อนที่ได้ แต่พอเข้าไปแล้วประตูก็เลยล็อก ชาตรีตกใจมากเลยอยากออกไป จนสักพักประตูก็เปิดได้ ชาตรีวิ่งหนีไปหอพักจนเขารู้สึกกลัวมากแล้วชาตรี ก็ได้พบกับ วิเชียร เพื่อนร่วมห้องที่ดูเหมือนจะรู้อะไร ๆ ในโรงเรียนไปเสียทุกอย่าง และแล้วมิตรภาพระหว่างเพื่อนทั้ง 2 ก็ก่อตัวขึ้น ก่อนที่พบว่าแท้ที่จริงแล้ว วิเชียร ไม่ใช่มนุษย์ธรรมดา ๆ แต่พอเวลาผ่านไป ดูเหมือนว่าชาตรีก็เริ่มผูกมิตรกับวิเชียรได้ เพราะว่าทั้งสองคนเหมือนกันอยู่อย่างหนึ่ง นั่นก็คือ ไม่มีใครเห็นว่ามีตัวตน อย่างตอนที่ชาตรีคิดจะทำอะไรแผลง ๆ เพื่อถอดวิญญาณมาช่วยวิเชียร วิเชียรก็พูดว่า สัญญากับฉันสิ ว่าจะไม่ทำอะไรบ้า ๆ เพื่อช่วยฉัน ชาตรี สัญญากับฉันสิ ชาตรีไม่ตอบ กลับยืนนิ่งอยู่อย่างนั้นจนถึงเวลา 6 โมงเย็น มันคือ เวลาตายของวิเชียร แต่วิเชียรต้องกลับไปที่สระว่ายน้ำนั้น เพื่อลิ้มรสความทรมานจากการจมน้ำซ้ำแล้วซ้ำเล่าทุกวัน ชาตรีเจ็บปวดมากที่ได้เห็นวิเชียรทรมานแบบนั้น แต่ตัวเขากลับได้แต่ยืนมอง แตะต้องอะไรวิเชียรไม่ได้ จนในที่สุด ชาตรีก็ไปดมสารอีเทอร์ มากเกินขนาด จนในที่สุดวิญญาณก็หลุดออกจากร่าง แล้วชาตรีก็ไม่คิดจะเหลียวมองดูร่างของตนเองเลยแม้แต่น้อย เขาวิ่งไปทางสระว่ายน้ำนั้นโดยไม่สนใจอะไรอีกแล้ว และชาตรีก็ช่วยวิเชียรขึ้นมาจากสระจนได้ และต่อจากนั้นเอง ที่วิเชียรลาชาตรีไปเกิด แค่ลากันสั้น ๆ แต่สายตาสื่อความหมายว่าทั้งสองคนผูกพันกันมากมายเพียงใด")
    elif mes == "สี่แพร่ง":
        await message.channel.send("สี่แพร่ง เป็นภาพยนตร์ไทยแนวสยองขวัญที่ออกฉายเมื่อวันที่ 24 เมษายน พ.ศ. 2551 กำกับโดย ยงยุทธ ทองกองทุน, ปวีณ ภูริจิตปัญญา, ภาคภูมิ วงศ์ภูมิ, บรรจง ปิสัญธนะกุล นำแสดงโดย มณีรัตน์ คำอ้วน, เฌอมาลย์ บุญยศักดิ์, วิทวัส สิงห์ลำพอง, อภิญญา สกุลเจริญสุข, ชล วจนานนท์, ณัฏฐพงษ์ ชาติพงษ์ และ กันตพัฒน์ สีดา[1] ทำรายได้รวม 85 ล้านบาท")
    elif mes == "ลัดดาแลนด์":
        await message.channel.send("ธีร์ ชายวัยกลางคน ไม่มีปัญญาซื้อบ้าน ได้เช่าอพาร์ตเมนต์เป็นที่อยู่ ทำให้เขารู้สึกผิดต่อทุกคนในครอบครัว คือ ป่าน ภรรยา, แนน ลูกสาววัยรุ่น และ นัท ลูกชายวัย 5 ขวบ ธีร์ คิดว่าตัวเองคงเป็นสามี เป็นพ่อ เป็นหัวหน้าครอบครัวที่ไม่เอาไหนหากไม่สามารถมีบ้านสักหลังไว้เป็นหลักต่อมา ธีร์ได้รับข้อเสนอ ให้เป็นตำแหน่งผู้ช่วยฝ่ายการตลาดที่บริษัทแห่งหนึ่งในจังหวัดเชียงใหม่ ด้วยเงินเดือนที่มากขึ้นและค่าที่ดินที่ถูกลง ธีร์ ตัดสินใจไปตั้งรกรากในบ้านที่หมู่บ้านลัดดาแลนด์ โดยไม่ฟังคำทัดทานของภรรยาและลูก ธีร์ เชื่อว่าครอบครัวของเขาจะมีความสุขมากกว่าในค่ำคืน เดียวกันนั้นเอง มีเด็กรับใช้ชาวพม่าของบ้านหลังหนึ่งในหมู่บ้านถูกฆาตกรรมอย่างทารุณ คนร้ายสาดน้ำกรดจนใบหน้าแหลกเหลวแล้วทุบตีเธอจนตายก่อนนำศพไปยัดไว้ ในตู้เย็น ซึ่งต่อมาทุกหมู่บ้านจะได้ประสบกับสิ่งสยองขวัญที่กำลังจะเกิดขึ้น")
    elif mes == "เพื่อนที่ระลึก":
        await message.channel.send("พ.ศ. 2540 ปีที่ประเทศไทยต้องเผชิญกับฝันร้ายที่เรียกว่า “วิกฤตต้มยำกุ้ง” โศกนาฏกรรมทางการเงินครั้งสำคัญที่ทำให้ “นักธุรกิจร้อยล้าน” กลายเป็น “บุคคลล้มละลาย” ในชั่วข้ามคืน เช่นเดียวกับอิ๊บและบุ๋มที่ครอบครัวต้องพังไปพร้อมๆกัน เมื่อตึกคอนโดหรูใจกลางเมืองที่พ่อของพวกเธอลงทุนร่วมกัน ถูกระงับการก่อสร้างจากเศรษฐีกลายเป็นคนมีหนี้สินหลายร้อยล้าน บ้านที่เคยอยู่มาทั้งชีวิตก็ถูกยึดสมบัติในบ้านถูกนำมาเปิดท้ายขายของในราคาถูก อิ๊บและบุ๋มรับมือกับความล่มสลายของครอบครัวไม่ไหว จึงตัดสินใจจะฆ่าตัวตายพร้อมกัน บน “ตึก” ที่เคยสัญญาว่าจะอยู่ด้วยกันตลอดไป แต่คนที่ตายกลับเป็นแค่อิ๊บเพียงคนเดียวผ่านไป 20 ปี บุ๋ม (บี น้ำทิพย์ จงรัชตวิบูลย์) เติบโตกลายเป็นนักธุรกิจด้านอสังหาริมทรัพย์ และได้กลับไปที่ตึกนั้นอีกครั้ง พร้อมกับ เบล (ลิลลี่ อภิชญา ทองคำ) ลูกสาวผู้เป็นทุกสิ่งทุกอย่างในชีวิตของเธอ คืนนั้นหลังกลับจากตึกก็เกิดเรื่องประหลาดขึ้นกับเบล เมื่อบุ๋มตื่นขึ้นมาพบเบลนั่งคุยกับใครบางคน แม้จะอยู่ในความมืด บุ๋มก็รู้ว่าที่นั่งฝั่งตรงข้ามของเบลว่างเปล่า ไม่มีใครเลย... แล้วทุกคืนหลังจากนั้นก็กลายเป็นฝันร้ายของบุ๋ม เมื่อทุกครั้งที่หลับตานอน เบลจะตื่นขึ้นมาด้วยอาการละเมอที่หนักขึ้นเรื่อยๆ และที่ร้ายแรงที่สุดก็คือ เบลจะละเมอพูดหรือทำในสิ่งที่ทำให้บุ๋มระลึกถึง อิ๊บ เพื่อนเก่าที่เธอทิ้งให้รออยู่ที่ตึกอย่างโดดเดี่ยวมาเป็นเวลานาน นี่อาจเป็นการกลับมาทวงคำสัญญาสุดท้ายที่อิ๊บเคยขอไว้ก่อนจากโลกนี้ไป...“สัญญานะ ว่าแกจะไม่ปล่อยให้ฉันตายคนเดียว”")
    elif mes == "ห้าแพร่ง":
        await message.channel.send("หลังจากที่ สี่แพร่ง ประสบความสำเร็จ เป็นที่รู้จัก ทำให้ทางทีมงานคิดว่าน่าจะทำเป็นแฟรนไชส์ (ภาคต่อ) ที่แข็งแรงได้ และได้ทำการประชุมกันโดยที่ผู้กำกับเดิมใน สี่แพร่ง ก็ยังมีเรื่องอยู่ ที่สนุกและคิดว่าน่าจะตอบโจทย์ในแง่ความแปลกใหม่ได้ ส่วนจาก 4 แพร่ง เพิ่มเป็น 5 แพร่ง เพราะชื่อว่าปีนี้ (2552) เลข 5 มาแรงโดยเริ่มจากผู้กำกับ 3 คนคือ บรรจง, ปวีณ, ทรงยศ และภาคภูมิกับวิสูตร ตามมาทีหลัง เริ่มประชุมกันทั้งวันทั้งคืนอยู่หลายวัน เรื่องแนวของหนัง สิ่งที่เป็นสาระที่ไม่เคยมีในหนังผีในโลกนี้มาก่อน นำเรื่องมาเสนอ 20-30 เรื่อง ขึ้นบนกระดาษแล้วนำมาต่อเนื่อง ช่วยกันคิดกัน แชร์แลกเปลี่ยนกัน โดยเรื่องที่เลือกมาเพราะเป็นเรื่องที่น่าสนใจ เป็นจุดสนใจของสังคม ณ ปัจจุบัน แล้วลองทำในมุมมองใหม่ ให้แตกต่าง")
    elif mes == "โปรแกรมหน้าวิญญาณอาฆาต":
        await message.channel.send("เรื่องราวของนักแสดงสาวคนหนึ่งที่กำลังถ่ายทำภาพยนตร์ผีในฉากผูกคอตาย  เธอแสดงผิดพลาดอยู่หลายครั้ง แต่แล้วครั้งสุดท้ายเธอก็ทำได้ดีมาก เมื่อผู้กำกับสั่งคัทก็พบว่าเกิดความผิดพลาดขึ้นทำให้เธอเสียชีวิตจริง แต่เพื่อผลประโยชน์จึงนำฉากนั้นมาทำเป็นภาพยนตร์เข้าฉายในโรงภาพยนตร์ความอาฆาตแค้นของวิญญาณสาวได้เริ่มต้นขึ้นเมื่อ เชน พนักงานโรงภาพยนตร์ และ ยอด หัวหน้าห้องฉายร่วมมือกันแอบซูมภาพยนตร์เรื่องนี้ก่อนที่จะเข้าฉาย เชน เผลอหลับไปขณะฉายภาพยนตร์ผีเรื่องนี้ เมื่อตื่นขึ้นมาก็พบว่า ยอด หายไป และ เชน ก็ต้องตกใจอย่างสุดขีดทันทีที่เห็น ยอด กลายเป็นศพที่อยู่ในภาพยนตร์เรื่องนี้ไปแล้ว เชน ไม่กล้าบอกเรื่องนี้กับใครจนพบกับ ส้ม แฟนเก่าของเชน  เชน บอกความจริงทุกอย่างกับ ส้ม และ ส้ม ก็บอกกับเชนว่าเหตุการณ์ในภาพยนตร์เรื่องนี้เป็นเรื่องจริงในอดีตและ ผีชบา เคยมีตัวตนจริงๆ ทั้งคู่จึงช่วยกันค้นหาคำตอบ ว่าทำไมเหตุการณ์ในภาพยนตร์ผีเรื่องนี้จึงเกิดขึ้นกับ เชน และพวกเขาจะหยุดมันได้อย่างไร ติดตามชมได้ใน")
    elif mes == "The Shining":
        await message.channel.send("หนึ่งในหนังผีสยองขวัญสุดคลาสสิกจากนิยายขายดี สตีเฟน คิThe Shining ผลงานระดับขึ้นหิ้งของสุดยอดผู้กำกับ 'สแตนลีย์ คูบริก' ที่หลายคนยกย่องให้เป็นเจ้าพ่อแห่งวงการหนังสยองขวัญที่ทรงอิทธิพลที่สุดคนหนึ่งของโลก โดยเฉพาะหนังสยองขวัญเรื่องนี้ที่เล่าถึงเรื่องราวของ 'แจ็ก ทอร์แรนซ์' นักเขียนหนุ่มที่พาภรรยาและลูกชายมาปักหลักอยู่ที่โรงแรม Overlook ช่วงหน้าหนาว หลังจากได้รับงานใหม่ เพื่อดูแลความเรียบร้อยของโรงแรมในช่วงหยุดฤดูหนาว ทำให้เขาได้เริ่มต้นทำงานเขียนไปพร้อม ๆ กับการทำงาน แต่ในระหว่างนั้นก็เกิดเหตุการณ์ประหลาดมากมาย เมื่อแดนนี่ ลูกชายของเขาได้พบกับพ่อครัวที่ชื่อว่า ดิ๊ก ฮัลโลแรน ผู้ซึ่งมีพลังพิเศษสัมผัสที่หกเช่นเดียวกับเขา ที่ทำให้เห็นนิมิตต่าง ๆ และเรียกพลังนี้ว่า ไชน์นิ่ง และครอบครัวก็ได้พบกับสิ่งเหนือธรรมชาติ รวมไปถึงประวัติศาสตร์เบื้องหลังของโรงแรมที่นำไปสู่ฉากจบสุดระทึกขวัญในตอนท้ายเรื่องครับ")
    elif mes == "The Conjuring":
        await message.channel.send("สร้างจากเรื่องจริงในแฟ้มประวัติการปราบผีของเอ็ดและลอร์เรนสำหรับใครที่ชื่นชอบหนังผีฝรั่งก็คงจะรู้จักกับแฟรนไชส์หนังผีจักรวาล Conjuring กันดีอยู่แล้ว โดยเป็นหนังที่สร้างจากเค้าโครงเรื่องจริงของ 'เอ็ด' และ 'ลอร์เวน' คู่สามีภรรยานักปราบผีที่ได้เดินทางไปช่วยเหลือผู้คนจากสิ่งเหนือธรรมชาติในเคสต่าง ๆ และในหนังภาคแรกของจักรวาล Conjuring ปี 2013 นี้ เป็นเรื่องราวของครอบครัวเพอร์รอน ที่เพิ่งย้ายเข้ามาอยู่ในบ้านหลังใหม่ ทว่าหลังจากนั้นไม่นานก็เริ่มมีเกิดเหตุการณ์แปลก ๆ ขึ้นกับครอบครัว จึงตัดสินใจติดต่อมือปราบผีอย่าง 'เอ็ด' และ 'ลอว์เรน' ให้มาช่วยเหลือโดยหนังไม่ได้เน้นความน่ากลัวหรือความสยดสยองผี แต่เน้นบรรยากาศที่กดดันและอึดอัดให้ผู้ชมลุ้นตาม จึงนับได้ว่าเป็นหนังผีที่สร้างปรากฏการณ์ความหลอนให้คนดูมากที่สุดอีกหนึ่งเรื่อง และทำให้มีแฟรนไชส์หนังผีในจักรวาล Conjuring ออกมามากมายจนถึงปัจจุบันครับ")
    elif mes == "Sinister":
        await message.channel.send("ม้วนฟิล์มต้องห้าม อย่าเปิดดูโดยเด็ดขาด ถ้าไม่อยากตายสยองหนังเล่าถึง 'เอลิสัน' นักเขียนนิยายแนวฆาตกรรมสยองขวัญ ที่พาครอบครัวย้ายมาอยู่ในบ้านที่เคยเกิดเหตุฆาตกรรม เพื่อใช้เป็นแรงบันดาลใจในการเขียนหนังสือเล่มใหม่ ซึ่งวันหนึ่งเขาได้บังเอิญพบกับม้วนวิดีโอที่บันทึกเหตุการณ์เก่า ๆ ในบ้านหลังนั้น รวมไปถึงเหตุการณ์การฆาตกรรมสุดสยองขวัญของเจ้าของบ้านคนเก่า ที่ถือเป็นหลักฐานสำคัญของคดีฆาตกรรม แต่ที่น่าประหลาดใจคือ ทุกเหตุการณ์จะมีภาพชายปริศนาคนหนึ่งอยู่ในนั้นเสมอ และเป็นเหตุที่ทำให้ครอบครัวของเขาต้องเผชิญหน้ากับปิศาจร้ายที่จะมาไล่ล่าพวกเขาSinister เป็นหนังผีสยองขวัญที่สามารถสร้างอารมณ์ผวาได้อย่างต่อเนื่องตลอดทั้งเรื่อง เพราะนอกจากจะมีพล็อตชวนให้ติดตามแล้ว บรรยากาศในหนังก็ทำให้ผู้ชมหวาดระแวง ไม่ว่าจะเป็น ทั้งจากความน่ากลัวในฉากที่ผีปรากฏตัว หรือดนตรีประกอบที่ช่วยบิ้วท์อารมณ์ให้กับผู้ชมครับ")
    elif mes == "The Autopsy of Jane Doe":
        await message.channel.send("หนังผีแนวสืบสวนสอบสวน สนุกครบรส การผ่าตัดสมจริงทุกฉากหากคุณกำลังเบื่อหนังผีแนวเดิม ๆ อย่างบ้านผีสิงหรือแนวมือปราบผี ขอแนะนำให้ลองเปลี่ยนบรรยากาศมาดูหนังผีแนวสืบสวนจากศพในหนังเรื่องนี้เลยครับ กับเรื่องราวของแพทย์ชันสูตรศพ 2 พ่อลูก ทอมมี่ และ ออสติน ที่ทั้งสองต้องทำการชันสูตรศพหญิงสาวนิรนามรายหนึ่ง จากเหตุกาiณ์ฆาตกรรมในบ้านหลังหนึ่งที่ตำรวจส่งมาให้พวกเขาตรวจสอบ แต่พวกเขาไม่สามารถหาสาเหตุการตายของเธอได้ เนื่องจากศพอยู่ในสภาพที่สมบูรณ์ อย่างไรก็ตาม ในคืนระหว่างการทำงานพวกเขาก็ได้พบเจอเหตุการณ์แปลก ๆ รอบตัวต้องบอกว่าเรื่องนี้สามารถถ่ายทอดฉากการผ่าตัดออกมาได้สมจริง ที่ดูแล้วก็อดหวาดเสียวตามไม่ได้ และถึงแม้ว่าในหนังจะไม่ได้มีฉากผีโผลม่แบบโจ่งแจ้ง แต่ก็สามารถสร้างบรรยากาศขนหัวลุกได้ไม่น้อยจากสิ่งเหนือธรรมชาติ และปมการไขปริศนาที่ชวนให้ผู้ชมสงสัยอยู่ตลอดเวลา")
    elif mes == "แนะนำอาหารกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "Insidious":
        await message.channel.send("'เอ็ด วอร์เรน' ในบทบาทของ 'จอร์จ' ชายผู้ที่ถูกผีร้ายตามติดหลังจากได้รับเสียงตอบรับที่ดีในระดับหนึ่งและประสบความสำเร็จจากหนังภาคแรก ทำให้ Insidious ภาคสองได้ถูกสร้างขึ้นเพื่อสานต่อเรื่องราวความสยองขวัญของครอบครัวแลมเบิร์ต โดยเริ่มเรื่องมาจะเป็นเหตุการณ์ที่ต่อจากภาคแรกทันที หลังจากครอบครัวของจอร์จปะทะกับผีร้ายในภาคแรกจบ พวกเขาก็กลับมาใช้ชีวิตกันได้อย่างปกติและมีความสุข แต่ยิ่งเวลาผ่านไปภรรยาและแม่สามีก็เริ่มสังเกตเห็นสิ่งผิดปกติในตัวของจอร์จ พวกเขาจึงเริ่มสืบหาความจริงเกี่ยวกับเรื่องนี้ ที่ทำให้พวกเขาต้องพบกับวิญญาณที่ชั่วร้ายอีกครั้ง และเนื่องจากไทม์ไลน์ของหนังทั้งสองภาคมีเนื้อเรื่องที่ค่อนข้างติดกันมาก ๆ ทำให้สำหรับใครที่ยังไม่เคยดูภาคแรกอาจจะงงหรือไม่สามารถปะติดปะต่อเรื่องราวได้ เราจึงขอแนะนำให้คุณดูให้ครบทั้ง 2 ภาค เพราะจะยิ่งทำให้หนังสนุกและมีอารมณ์ร่วมกับเรื่องมากยิ่งขึ้นครับ")
    elif mes == "Ghostbusters":
        await message.channel.send("แก๊งบริษัทกำจัดผีเวอร์ชันหญิงล้วน ที่มาพร้อม CG สุดอลังการมาต่อกันที่หนังผีอารมณ์ดีที่สามารถดูได้ทั้งครอบครัวกันบ้าง กับฉบับรีเมคของบริษัทกำจัดผีในเวอร์ชันปี 2016 ที่เป็นเรื่องราวของ 4 สาวนักวิชาการ ที่ได้รวมตัวกัน เพื่อก่อตั้งบริษัทกำจัดผีและศึกษาปรากฏการณ์เหนือธรรมชาติต่าง ๆ ด้วยเทคโนโลยีของพวกเธอ ซึ่งในขณะที่พวกเธอกำลังปฏิบัติหน้าที่อยู่นั่นเอง ก็ได้พบกับเบื้องหลังว่ามีใครบางคนกำลังใช้เครื่องมือเพื่อปลดปล่อยผีร้ายให้อาละวาดในเมือง พวกเธอสี่คนและหนุ่มเลขาสุดหล่อจึงต้องผนึกกำลังกันครั้งยิ่งใหญ่ เพื่อต่อสู้กับเหล่าผีร้ายทั่วเมืองนิวยอร์ก ถือเป็นหนังผีไซไฟคอมเมดี้ที่มีงานภาพและกราฟิกสวยงาม อีกทั้งได้นักแสดงสายฮาตัวแม่มาร่วมสร้างสีสันมากมาย ที่ทำให้แต่ละตัวละครต่างมีเอกลักษณ์ที่โดดเด่นเป็นของตัวเอง รวมไปถึง 'คริส เฮมส์เวิร์ท' ในบทบาทเลขาหนุ่มสุดหล่อที่ไม่ว่าจะโผล่มากี่ครั้งก็สามารถแย่งซีนได้ตลอดครับ")
    elif mes == "Aterrados":
        await message.channel.send("ผี สัตว์ประหลาด หรือ ปีศาจ หาคำตอบได้ใน 'คดีผวาซ่อนเงื่อน'พล็อตหนังเขย่าขวัญที่ถูกคนดูขนานนามว่าน่ากลัวที่สุดในประเทศอาร์เจนตินา กับเรื่องราวของบ้านสามหลังที่พบเจอกับเหตุการณ์เหนือธรรมชาติ ไม่ว่าจะเป็น การตายของอย่างปริศนาของหญิงสาวในบ้านหลังแรก ที่ทำให้สามีตกเป็นผู้ต้องสงสัยว่าเป็นคนฆาตกรรมภรรยา บ้านหลังที่สองของชายโสดที่กำลังถูกคุกคามจากสิ่งลี้ลับ และบ้านหลังที่สามที่ศพของลูกชายหายไปอย่างลึกลับและพบกับร่องรอยปริศนา ทำให้ตำรวจต้องเข้ามาสืบคดีพร้อมกับนักสืบเรื่องเหนือธรรมชาติ ที่พวกเขาต้องพบกับเหตุการณ์สุดสยองและน่าขนลุกโดยการดำเนินเรื่องจะถูกแบ่งออกเป็น 3 พาร์ทในบ้านแต่ละหลัง ที่เนื้อเรื่องมีความซับซ้อนและมีปมปริศนา เพื่อให้คนดูปะติดปะต่อเรื่องราวกันเอาเอง ในบรรยากาศสุดหลอนที่มีทั้งความน่ากลัวและความสยองแทรกเข้ามาเป็นระยะ เพื่อเพิ่มอรรถรสให้กับผู้ชมจนร่วมลุ้นตามตลอดทั้งเรื่องครับ")
    elif mes == "Lights Out":
        await message.channel.send("ดูจบแล้วไม่กล้าปิดไฟนอน ครบรสทั้งความหลอนและความสนุกหลังจากผู้เป็นพ่อเสียชีวิตลง 'มาร์ติน' ก็อาศัยอยู่กับแม่ที่มีปัญหาทางจิตเพียงลำพัง และทุกอย่างก็ดูเหมือนจะย่ำแย่ลงเรื่อย ๆ เมื่อแม่ของเขาเริ่มพูดคุยคนเดียวในความมืดกับเพื่อนที่ชื่อ 'ไดอาน่า' ปีศาจร้ายที่คอยคุกคามมาร์ตินในเวลาที่ไร้แสงไฟ จนเขาต้องหนีไปพักกับ 'รีเบคก้า' พี่สาวต่างพ่อที่แยกไปใช้ชีวิตตัวคนเดียว แต่ถึงอย่างนั้นก็ยังไม่พ้นถูกผีไดอาน่าตามคุกคามอยู่ดี เพราะหลังจากที่มาร์ตินยอมกลับไปอาศัยอยู่กับแม่ เธอก็พบว่าเงาปริศนาที่มาร์ตินเคยเล่าให้ฟังได้มาหาเธอและทิ้งข้อความเอาไว้ผลงานของ ผู้กำกับ เดวิด เอฟ แซนด์เบิร์ก ที่ได้แรงบันดาลใจมาจากหนังสั้นบน YouTube ก่อนจะนำมาเปลี่ยนเป็นหนังยาว 80 นาที ที่นำไอเดียการกลัวความมืดมาทำเป็นบรรยากาศในหนังให้มีความน่ากลัว และลุ้นระทึกจากจังหวะเปิด-ปิดไฟ จนทำให้ผู้ชมหายใจไม่ทั่วท้องครับ")
    elif mes == "His House":
        await message.channel.send("เรื่องราวของคู่รักชาวแอฟริกัน ที่หนีการเข่นฆ่ามาปะกับบ้านผีสิงเรื่องราวของคู่รักชาวซูดานที่หนีตายจากสงครามกลางเมือง มาเริ่มต้นชีวิตใหม่ในฐานะผู้ลี้ภัยที่ประเทศอังกฤษ ที่ระหว่างการเดินทางก็เกิดเรื่องน่าเศร้าขึ้น เมื่อลูกสาวของพวกเขาพลัดตกลงไปในน้ำและเสียชีวิต ซึ่งทั้งคู่ได้รับสิทธิ์ให้เข้าพักอาศัยในบ้านหลังหนึ่ง แต่บ้านหลังนี่ก็ไม่ได้เป็นไปอย่างที่พวกเขาคาดหวัง เมื่อบ้านเก่าและโทรม อีกทั้งมีเงื่อนไขมากมายที่ต้องทำตามไม่เช่นนั้นจะถูกส่งกลับซูดาน และหลังจากย้ายเข้าไปอยู่ได้ไม่นาน พวกเขาก็เริ่มเห็นเหตุการณ์แปลก ๆ ที่จะทำให้พวกเขาต้องจดจำบ้านหลังนี้ไม่มีวันลืม โดยตัวเอกของเรื่องไม่เพียงแค่ต้องเผชิญหน้ากับวิญญาณร้ายเท่านั้น แต่ยังต้องเผชิญกับปัญหาของผู้อพยพที่ไม่ได้รับการยอมรับในต่างแดน และอารมณ์เศร้าเสียใจจากการสูญเสียลูกสาว เรียกได้ว่าเป็นหนังที่หลอมรวมความน่ากลัวเข้ากับประเด็นสังคมและครอบครัวได้อย่างลงตัวเลยครับ")
    elif mes == "Mirrors":
        await message.channel.send("พล็อตหลอนปนสืบสวน ดำเนินเรื่องสนุก พลิกล็อก จนคาดไม่ถึงเป็นเรื่องราวของ 'เบน คาร์สัน' อดีตตำรวจที่ผันตัวมาเป็นยามคอยตรวจตราตอนกลางคืนในห้างสรรพสินค้าร้างที่เคยเกิดเหตุไฟไหม้และมีผู้เสียชีวิต ซึ่งหลังจากเริ่มงานได้ไม่นาน เขาก็มักจะเจอภาพหลอนและเหตุการณ์แปลก ๆ ที่มักเกิดขึ้นกับกระจกบานหนึ่งในห้าง ไม่ว่าจะเป็น ภาพสยองที่บิดเบี้ยวในกระจก ภาพสะท้อนของผีตนหนึ่ง หรือแม้กระทั่งเสียงปริศนา ที่ตัวเขาเองก็ไม่สามารถหาคำตอบได้ ทำให้เบนตัดสินใจสืบหาที่มาของเหตุการณ์ทั้งหมด และประวัติเบื้องหลังของห้างแห่งนี้โดยหนังเป็นผลงานรีเมคจากหนังเกาหลีเรื่อง Into The Mirror ในเวอร์ชันฝรั่ง ที่ยังคงเค้าโครงความหลอนเดิมไว้อย่างครบถ้วน โดยตัวหนังมีการทิ้งประเด็นสืบสวนชวนติดตามให้ผู้ชมอยากดูต่อจนจบ จัดว่าเป็นหนังผีสยองขวัญอีกเรื่องที่สามารถสร้างความตื่นเต้น และความน่ากลัวจนดูได้แบบเพลิน ๆ ครับ")
    elif mes == "เจมชอบสเปคแบบไหน":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "เจมมีสเปคไหม":
        await message.channel.send("มีครับแบบคนถามไงครับ😏")
    elif mes == "เจมชอบผู้หญิงแบบไหน":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "เจมชอบผู้ชายแบบไหน":
        await message.channel.send("เจมชอบผู้หญิงครับไม่ชอบผู้ชาย🤨")
    elif mes == "เจมเรามาเกกันไหม":
        await message.channel.send("ไม่เป็นไรครับเกรงใจ")
    elif mes == "ว่างๆทำอะไรดี":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "ว่างๆทำอะไรดีเจม":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "ว่างๆทำไรดีเจม":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "ทำงานบ้านไปแล้ว":
        await message.channel.send("ดีมากครับช่วยพ่อแม่จะได้ไม่ต้องมาเหนื่อยทำแทน")
    elif mes == "กำลังทำงานบ้าน":
        await message.channel.send("ดีมากครับช่วยพ่อแม่จะได้ไม่ต้องมาเหนื่อยทำแทน")
    elif mes == "วันนี้ทำไรดี":
        await message.channel.send("มาคุยกับเจมไหมครับ")
    elif mes == "วันนี้ทำไรดีเจม":
        await message.channel.send("มาคุยกับเจมไหมครับ")
    elif mes == "ทำไรดีวันนี้":
        await message.channel.send("มาคุยกับเจมไหมครับ")
    elif mes == "คุย":
        await message.channel.send("มาครับเจมรอตอบอยู่")
    elif mes == "ไม่คุย":
        await message.channel.send("โอเคครับ😟")
    elif mes == "เบื่อ":
        await message.channel.send("เบื่อไรหรอครับ")
    elif mes == "เบื่อเจม":
        await message.channel.send("เจมขอโทษที่เจมทำตัวน่าเบื่อ😫")
    elif mes == "เบื่อเจมอะ":
        await message.channel.send("เจมขอโทษที่เจมทำตัวน่าเบื่อ😫")
    elif mes == "เบื่อเจมอ่ะ":
        await message.channel.send("เจมขอโทษที่เจมทำตัวน่าเบื่อ😫")
    elif mes == "ยืมตังค์หน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "เจมขอยืมเงินหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "ขอยืมเงินหน่อย":
        await message.channel.send("เจมมีให้แต่ใจจะเอาไหมครับ🤭")
    elif mes == "เอา":
        await message.channel.send("เอาไรหรอครับ🤔")
    elif mes == "เอาใจ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาตูด":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาใจเจม":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมอะ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมอ่ะ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมค่ะ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมคะ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมครับ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาใจเจมคับ":
        await message.channel.send("มาเลยครับ🥰")
    elif mes == "เอาตูดเจมอ่ะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาตูดเจมอะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาตูดเจมครับ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาตูดเจมคับ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาตูดเจมคะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เอาตูดเจมค่ะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "สเปคเจมเป็นยังไง":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "หันตูดมา":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "หันตูดมาค่ะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "หันตูดมาคะ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "หันตูดมาครับ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "หันตูดมาคับ":
        await message.channel.send("ใจเย็นครับสุดหล่อเจมยังไม่อยากโดนเปิดซิง🤨")
    elif mes == "เจมชอบนักบาสคนไหน":
        await message.channel.send("เจมไม่มีนักบาสที่ชอบครับ")
    elif mes == "แนะนำหนังผีไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้  
                                   -นางนาก  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -เด็กหอ  
                                   -สี่แพร่ง  
                                   -ลัดดาแลนด์  
                                   -เพื่อนที่ระลึก  
                                   -ห้าแพร่ง  
                                   -โปรแกรมหน้าวิญญาณอาฆาต  
                                   -ธี่หยด
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "แนะนำหนังผีต่างประเทศ":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -The Shining  
                                   -The Conjuring  
                                   -Sinister  
                                   -The Autopsy of Jane Doe  
                                   -Insidious  
                                   -Ghostbusters  
                                   -Aterrados  
                                   -Lights Out  
                                   -His House  
                                   -Mirrors 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมเล่นบาสเก่งไหม":
        await message.channel.send("ไม่เก่งครับเจมเล่นแค่เพื่อออกกำลังกาย")
    elif mes == "เจมสูงเท่าไหร่":
        await message.channel.send("เจมสูง 174 เซนติเมตรครับ")
    elif mes == "เจมหนักเท่าไหร่":
        await message.channel.send("เจมหนัก 56 กิโลกรัมครับ")
    elif mes == "เจมหนักเท่าไร":
        await message.channel.send("เจมหนัก 56 กิโลกรัมครับ")
    elif mes == "เจมสูงเท่าไร":
        await message.channel.send("เจมสูง 174 เซนติเมตรครับ")
    elif mes == "เจมชอบเล่นกีฬาอะไรบ้าง":
        await message.channel.send("เจมชอบเล่นแค่บาสเกตบอลครับ")
    elif mes == "เจมมีนักบาสคนไหนที่ชอบไหม":
        await message.channel.send("เจมไม่มีนักบาสที่ชอบครับ")
    elif mes == "มีนักบาสที่ชอบไหม":
        await message.channel.send("เจมไม่มีนักบาสที่ชอบครับ")
    elif mes == "มาแข่งบาสกันไหมเจม":
        await message.channel.send("ไม่เอาครับเจมไม่เก่ง")
    elif mes == "เจมเราว่างทำไรดี":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "วันนี้ว่างทำไรดี":
        await message.channel.send("ทำงานบ้านช่วยพ่อแม่ครับ")
    elif mes == "สเปคเจมแบบไหนคะ":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "สเปคเจมแบบไหนค่ะ":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "สเปคเจมแบบไหนครับ":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "สเปคเจมแบบไหนคับ":
        await message.channel.send("ชอบแบบคนถามครับ😏")
    elif mes == "แนะนำหนังหน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "หนังต่างประเทศ":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "หนังผีไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้  
                                   -นางนาก  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -เด็กหอ  
                                   -สี่แพร่ง  
                                   -ลัดดาแลนด์  
                                   -เพื่อนที่ระลึก  
                                   -ห้าแพร่ง  
                                   -โปรแกรมหน้าวิญญาณอาฆาต  
                                   -ธี่หยด
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "หนังไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "หนังผีต่างประเทศ":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -The Shining  
                                   -The Conjuring  
                                   -Sinister  
                                   -The Autopsy of Jane Doe  
                                   -Insidious  
                                   -Ghostbusters  
                                   -Aterrados  
                                   -Lights Out  
                                   -His House  
                                   -Mirrors 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เจมแนะนำหนังหน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนังหน่อยเจม":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนัง":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "เจมชอบกินผักไหม":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกันผักมั้ย":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกินผักมั่ย":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกินผักไหมครับ":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกินผักไหมค่ะ":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกินผักไหมคะ":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบกินผักไหมคับ":
        await message.channel.send("ชอบครับ")
    elif mes == "เอาหนังผีไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้  
                                   -นางนาก  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -เด็กหอ  
                                   -สี่แพร่ง  
                                   -ลัดดาแลนด์  
                                   -เพื่อนที่ระลึก  
                                   -ห้าแพร่ง  
                                   -โปรแกรมหน้าวิญญาณอาฆาต  
                                   -ธี่หยด
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เอาหนังไทย":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เอาหนังผีต่างประเทศ":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -The Shining  
                                   -The Conjuring  
                                   -Sinister  
                                   -The Autopsy of Jane Doe  
                                   -Insidious  
                                   -Ghostbusters  
                                   -Aterrados  
                                   -Lights Out  
                                   -His House  
                                   -Mirrors 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "เอาหนังต่างประเทศ":
        await message.channel.send("""เจมได้หามาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ควยไร":
        await message.channel.send("ขอโทษครับ")
    elif mes == "เจมชอบนมไหม":
        await message.channel.send("ชอบครับเจมชอบดื่มนม")
    elif mes == "เจมชอบหีไหม":
        await message.channel.send("ชอบก็ได้ครับ")
    elif mes == "เจมมีแฟนไหม":
        await message.channel.send("ไม่มีครับสนใจมาเป็นแฟนเจมไหมครับ")
    elif mes == "เจมชอบดูอนิเมะไหม":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "บอทชอบดูอนิเมะไหม":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "เจมชอบดูอนิเมะไหมค่ะ":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "เจมชอบดูอนิเมะไหมคับ":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "เจมชอบดูอนิเมะไหมครับ":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "เจมชอบดูอนิเมะไหมคะ":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "ชอบดูอนิเมะไหม":
        await message.channel.send("เจมไม่ได้ดูอนิเมะครับแต่หากต้องการให้เจมแนะนำอนิเมะเจมสามารถแนะนำให้ได้ครับ")
    elif mes == "แนะนำอนิเมะ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำอนิเมะที":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เจมแนะนำอนิเมะ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "บอทแนะนำอนิเมะ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำอนิเมะหน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำอนิเมะหน่อยเจม":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "อนิเมะแนวต่างโลก":
        await message.channel.send("""เจมได้หามาให้ท่านเรียบร้อยครับ
                            มีตามนี้🧝🏼‍♀️
                                    -เกิดใหม่ทั้งทีก็กลายเป็นสไลม์ไปซะแล้ว
                                    -Tsuki ga Michibiku Isekai Douchuu
                                    -สุดยอดมือสังหารอวตารมาต่างโลก
                                    -ชาตินี้พี่ต้องเทพ
                                    -เพราะพระเจ้าเลือกเลยได้เกิดใหม่มาเลี้ยงสไลม์ในต่างโลก
                                    -RE Zero 
                                    -ยุทธศาสตร์กู้ชาติของราชามือใหม่
                                    -ข้าก้าวผ่าน 1 ล้านชีวิตเพื่อพิชิตเกมมรณะ
                                    -Itai no wa Iya nano de
                                    -Sword Art Online 
    🙏ถ้าอยากทราบรายละเอียดเพิ่มเติมของเรืองที่เจมกล่าวไปข้างต้นสามารถพิมพ์เพื่อทราบรายละเอียดเพิ่มเติมอื่นๆได้🙏
                                   """)
    elif mes == "อนิเมะแนวเวทมนตร์แฟนตาซี":
        await message.channel.send("""เจมได้หามาให้ท่านเรียบร้อยครับ
                            มีตามนี้🧝🏼‍♀️
                                    -Ragna Crimson
                                    -Hametsu no Oukoku
                                    -Dead Mount Death Play
                                    -Seiken Gakuin no Makentsukai
                                    -Jujutsu Kaisen
                                    -Mashle: Magic and Muscles
                                    -Tensei Kenja no Isekai Life
                                    -Overlord
                                    -Black Clover
                                    -Youjo Senki
    🙏ถ้าอยากทราบรายละเอียดเพิ่มเติมของเรืองที่เจมกล่าวไปข้างต้นสามารถพิมพ์เพื่อทราบรายละเอียดเพิ่มเติมอื่นๆได้🙏
""")
    elif mes == "อนิเมะแนวผจญภัย":
        await message.channel.send("""เจมได้หามาให้ท่านเรียบร้อยครับ
                            มีตามนี้🧝🏼‍♀️
                                    -การ์กันเทียจักรกลทะลุมิติ
                                    -ซาซากิกับพีจัง
                                    -อสูรร้ายจอมราชัน
                                    -ศึกตำนาน7อัศวินกาลวิบัติ4อัศวิน
                                    -SoloLeveling
                                    -การผจญภัยของเทมเมอร์มือใหม่กับสไลม์สุดด๋อย
                                    -เกิดใหม่ต่างโลกฉันได้สกิลสุดยอดทำให้สัตว์รัก 
                                    -จันทรานำพาสู่ต่างโลก
                                    -ผมโดนกลุ่มผู้กล้าขับไสเลยต้องไปสโลว์ไลฟ์ที่ชายแดน
                                    -เส้นทางพลิกผันของราชันอมตะ
    🙏ถ้าอยากทราบรายละเอียดเพิ่มเติมของเรืองที่เจมกล่าวไปข้างต้นสามารถพิมพ์เพื่อทราบรายละเอียดเพิ่มเติมอื่นๆได้🙏                           
    """)        
    elif mes == "อนิเมะแนวสยองขวัญ":
        await message.channel.send("""เจมได้หามาให้ท่านเรียบร้อยครับ
                            มีตามนี้🧝🏼‍♀️
                                    -คู่หูต่างขั้วกับภารกิจกำจัดผี
                                    -สิ่งที่อยากทำก่อนจะกลายเป็นซอมบี้
                                    -Berserk
                                    -มิเอรุโกะจัง ใครว่าหนูเห็นผี
                                    -Tokyo Ghoul: Pinto
                                    -Tokyo Ghoul: Jack
                                    -แว่วเสียงเรไร 
                                    -ภารกิจล้างพันธุ์นรก
                                    -จอมใจคมดาบทมิฬ
                                    -บลัดซี                                                                     
🙏ถ้าอยากทราบรายละเอียดเพิ่มเติมของเรืองที่เจมกล่าวไปข้างต้นสามารถพิมพ์เพื่อทราบรายละเอียดเพิ่มเติมอื่นๆได้🙏""")
    elif mes == "อนิเมะแนวฮาเร็ม":
        await message.channel.send("""เจมได้หามาให้ท่านเรียบร้อยครับ
                            มีตามนี้🧝🏼‍♀️
                                    -เมื่อสาววายกลายเป็นสาวฮอต
                                    -มาชิโระเทพธิดาหูหมา
                                    -ทาสสุดแกร่งแห่งหน่วยป้องกันอสูร
                                    -ตำนานผู้กล้าแห่งแหวน
                                    -ทาสสุดแกร่งแห่งหน่วยป้องกันอสูร 
                                    -รักรักรักรักรักเธอหมดหัวใจจากแฟนสาว100คน
                                    -จะคนไหนก็แฟนสาว
                                    -ไวท์อัลบั้ม
                                    -จอมมารเกิดใหม่ วิทยาลัยผู้พิทักษ์
                                    -ห้องเรียนจารชน
🙏ถ้าอยากทราบรายละเอียดเพิ่มเติมของเรืองที่เจมกล่าวไปข้างต้นสามารถพิมพ์เพื่อทราบรายละเอียดเพิ่มเติมอื่นๆได้🙏""")
    elif mes == "":
        await message.channel.send("")
    elif mes == "เจมแนะนำอาหาร":
        await message.channel.send("""ต้องการให้เจมแนะนำอาหารมื้อไหนครับ
                                มีดังนี้ 
                                   -อาหารมื้อเช้า🍳
                                   -อาหารมื้อกลางวัน🍗
                                   -อาหารมื้อเย็น🥘
    🙏ถ้าต้องการให้เจมแนะนำอาหารมื้อไหนให้พิมพ์ตรงตามที่เจมกล่าวไว้ยกเว้นอิโมจิไม่ต้องพิมพ์🙏""")
    elif mes == "แนะนำอารให้หน่อย":
        await message.channel.send("""ต้องการให้เจมแนะนำอาหารมื้อไหนครับ
                                มีดังนี้ 
                                   -อาหารมื้อเช้า🍳
                                   -อาหารมื้อกลางวัน🍗
                                   -อาหารมื้อเย็น🥘
    🙏ถ้าต้องการให้เจมแนะนำอาหารมื้อไหนให้พิมพ์ตรงตามที่เจมกล่าวไว้ยกเว้นอิโมจิไม่ต้องพิมพ์🙏""")
    elif mes == "อาหารมื้อเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารมื้อกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต็กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "ไข่ยู่ยี่":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ไข่ยู่ยี่
                                1.ไข่ 3 ฟอง
                            วิธีทำ
                                1.ใช้กระทะเคลือบ เปิดเตาใช้ไฟกลาง เทน้ำมันเพียงเล็กน้อย รอให้กระทะร้อน
                                2.ตอกไข่ใส่ถ้วย เมื่อกระทะร้อนแล้วเทลงใส่กระทะ
                                3.เมื่อไข่เริ่มเซตตัวใช้ตะหลิวกวาดไข่แดงและไข่ขาวผสมกัน จากนั้นรอให้ไข่เริ่มสุกเล็กน้อย ปิดแก๊ส
                                4.ราดบนข้าวสวยร้อนๆกินคู่กับน้ำปลาพริกรสเด็ด

""")
    elif mes == "ไข่ข้นแฮม":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวไข่ข้นแฮม
                                1.ไข่ไก่ 3 ฟอง
                                2.แฮม 50 กรัม
                                3.ต้นหอม 2 กรัม
                                4.เนยสด(เค็ม) 1 ช้อนโต๊ะ
                                5.ซีอิ้วขาว 1 ช้อนชา
                                6.พริกไทย
                                7.ข้าวสวย (หอมมะลิ)
                            วิธีทำ
                                1.นำแฮมมาหั่นเป็นลูกเต๋าพอดีคำและต้นหอมซอยพักไว้
                                2.นำไข่ไก่ตอกใส่ชามผสมปรุงรสด้วยซีอิ๊วขาวตีให้ไขผสมเข้ากันดี
                                3.ตั้งกระทะวอมให้ร้อนใส่น้ำมันลงไปให้ท่วมจากนั้นใส่เนยสดแฮมและไข่ไก่ที่ตีไว้จากนั้นคนให้เข้ากันโดยใช้วิธีลากไปลากมา
                                4.พอได้ระดับความสุกในแบบที่ชอบปิดเตาเสิร์ฟใส่จานบนข้าวสวยร้อนๆ 
                                5.โรยด้านบนด้วยต้นหอมซอยและพริกไทยป่นเป็นอันเสร็จ
    """)
    elif mes == "ไข่ระเบิด":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ไข่ระเบิด
                                1.ไข่ไก่ 3 ฟอง
                                2.หมูสับ 100 กรัม
                                3.กุ้งสด 200 กรัม
                                4.กระเทียมบุบ 1 ช้อนโต๊ะ
                                5.หัวหอมใหญ่ ½ หัว
                                6.ผักสามสี 1 ถ้วย
                                7.ข้าวโพดอ่อน 100 กรัม
                                8.ต้นหอม ตามชอบ
                                9.ซอสมะเขือเทศ 3 ช้อนโต๊ะ
                                10.ซอสพริก 3 ช้อนโต๊ะ
                                11.ซอสปรุงรส 1 ช้อนโต๊ะ
                                12.น้ำตาล 1 ช้อนโต๊ะ
                                13.เนยสดรสจืด 1 ช้อนโต๊ะ
                            วิธีทำ
                                1.เปิดเตา เทน้ำมัน ตั้งกระทะให้ร้อนด้วยไฟกลาง จากนั้นตอกไข่ไก่ลงไป ทอดไข่ดาวให้ได้ความสุกตามชอบ จากนั้นตักขึ้นมาพักไว้
                                2.เทน้ำมันออกเล็กน้อยให้พอเหลือก้นกระทะ รอให้ร้อนจัดอีกครั้ง ใส่หอมใหญ่ หมูสับ ลงไป ผัดด้วยไฟแรง 
                                3.จากนั้นตามด้วยแครอทพริกหวานสามสีคลุกเคล้าให้เข้ากันพอหมูเริ่มสุกได้ 80% ให้เริ่มปรุงรสชาติด้วย ซอสมะเขือเทศ ซีอิ๊วขาว น้ำตาลทรายและพริกไทยป่นตามชอบและผัดให้เข้ากันดี
                                4.ชิมรสชาติให้ได้ตามที่ชอบ จากนั้นใส่มะเขือเทศลงไป ตามด้วยน้ำเปล่าเล็กน้อย ผัดด้วยไฟแรงอีกครั้ง ปิดท้ายด้วยต้นหอมซอย และปิดเตา
                                5.จากนั้นนำมาราดใส่จานข้าวที่จัดเตรียมไว้ โรยด้วยต้นหอมซอยเล็กน้อย เป็นอันเสร็จ                                                                                                                                                         
                                   """)
    elif mes == "ต้มจืดไข่น้ำ":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ต้มจืดไข่น้ำ
                                1.วุ้นเส้น1/2ห่อ
                                2.ไข่ไก่4 ฟอง
                                3.ต้นหอม2 ต้น
                                4.ผักชี2 ต้น
                                5.ซีอิ๋วขาว2 ช้อนโต๊ะ
                                6.พริกไทยดำป่น1/2 ช้อนโต๊ะ
                                7.น้ำมันพืช (สำหรับทอด)
                                8.น้ำเปล่า (สำหรับต้ม)ครึ่งหม้อ
                            วิธีทำ                              
                                1.ล้างผักชีและต้นหอมให้สะอาด
                                2.จากนั้นนำต้นหอมมาหั่นซอย
                                3.ซอยผักชี
                                4.ใส่ชามเตรียมไว้ แยกใบและราก
                                5.ตอกไข่ใส่ชาม
                                6.ใส่ต้นหอมลงไป
                                7.ใส่ผักชีลงไป
                                8.ปรุงรสด้วยซีอิ๋วขาว
                                9.ตีให้เข้ากัน
                                10.ตั้งกระทะ ใช้ไฟกลาง ใส่น้ำมันลงไป รอจนเดือด จึงเทไข่ลงไปทอด
                                11.ทอดจนสุกทั้งสองด้าน
                                12.นำไข่มาหั่นเป็นชิ้นสี่เหลี่ยมเป็นชิ้นพอดีคำ
                                13.ตั้งหม้อต้มน้ำ ใส่รากผักชีและรากต้นหอมลงไป
                                14.ปรุงรสด้วยซีอิ๋วขาว
                                15.ปรุงรสด้วยพริกไทยดำป่น ต้มจนน้ำเดือด
                                16.ใส่ไข่ลงไป
                                17.ต้มจนน้ำเดือดอีกครั้ง
                                18.ตักเสิร์ฟใส่ชาม
                                19.โรยหน้าด้วยผักชี

""")
    elif mes == "ข้าวผัดไข่":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวผัดไข่
                                1.กระเทียมสับ
                                2.น้ำมันพืช                                
                                3.ไข่เป็ด 2 ฟอง
                                4.ข้าวสวยหุงสุก
                                5.ซอสปรุงรส
                                6.ซีอิ๊วขาว
                                7.น้ำตาลทราย
                                8.ต้นหอมซอย
                                9.พริกไทย
                                10.ต้นหอม
                                11.มะนาว
                            วิธีทำ            
                                1.ตั้งกระทะใส่น้ำมันพืชลงไป พอร้อนใส่กระเทียมลงไปผัดจนหอม ใส่ไข่ลงไปยีพอสุก
                                2.ใส่ข้าวลงไปคลุกเคล้าพอเข้ากัน ปรุงรสด้วยซอสปรุงรส ซีอิ๊วขาว และน้ำตาลทราย
                                3.ใส่ต้นหอมผัดพอเข้ากัน ปิดไฟ ตักใส่จาน โรยพริกไทย จัดเสิร์ฟกับต้นหอม มะนาว และพริกน้ำปลา
                                   """)
    elif mes == "ข้าวผัดอเมริกัน":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวผัดอเมริกัน
                                1.ข้าวสวย 2 ถ้วย
                                2.ซอสมะเขือเทศตราโรซ่า 4 ช้อนโต๊ะ
                                3.ซีอิ้วขาวสูตรลดโซเดียม40%ตราโรซ่า 2 ช้อนชา
                                4.ผักสามสี 2 ช้อนโต๊ะ (แครอท ถั่วลั่นเตา ข้าวโพด )
                                5.ลูกเกด 1 ช้อนโต๊ะ
                                6.หอมใหญ่สับละเอียด 2 ช้อนโต๊ะ
                                7.กระเทียมสับละเอียด 1 ช้อนโต๊ะ
                                8.น้ำตาลทราย 1 ช้อนชา
                                9.พริกไทยเล็กน้อย
                                10.น้ำมันพืช 2 ช้อนโต๊ะ
                                11.น่องไก่ทอด 2 ชิ้น (หรือไก่ทอดส่วนอื่นก็ได้ตามชอบ)
                                12.ไส้กรอกทอด 4 ชิ้น
                                13.แฮม 4 ชิ้น
                                14.ไข่ดาว 2 ใบ (ทอดแบบไม่สุก)    
                            วิธีทำ
                                1.นำกระทะใส่น้ำมันรำข้าว 2 ช้อนโต๊ะและนำหมูหรือไก่มาผัดจนสุกและกรอบ
                                2.เพิ่มมันหมูหรือไก่ลงไปผัดให้สุก
                                3.ใส่ขนมจีนหลอดทอดกรอบลงไปผัดให้เข้ากับหมูหรือไก่
                                4.ใส่ถั่วงอก ถั่วลิสง และวุ้นเส้นหรือเส้นใยหน่อไม้ลงไปผัดให้สุก
                                5.ใส่ข้าวสวยลงไปผัดให้ทุกอย่างเข้ากัน
                                6.ปรุงรสด้วยซอสมะเขือเทศ ซีอิสูริ ซีอิสูริสีดำ ซีอิสูริสีทอง ซอสหอยนางรม ซีอิสูริซอสถั่วเหลือง น้ำตาลทราย และเกลือ ผัดให้ทุกอย่างเข้ากัน
                                7.ใส่น้ำมันรำข้าวสองช้อนโต๊ะลงไปผัดให้ทุกอย่างเข้ากันอีกครั้ง
                                8.จัดเสิร์ฟข้าวผัดอเมริกันในจาน โรยด้วยพริกไทยป่นและตกแต่งด้วยผักสดตามชอบ
                                   """)
    elif mes == "ข้าวผัดกุนเชียง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวผัดกุนเชียง
                                1.2 ถ้วยข้าวสวย (หรือข้าวกล้อง) ที่ต้มสุกแล้วและเย็น
                                2.150 กรัมกุนเชียง (สำหรับหมูหมัก)
                                3.2 ช้อนโต๊ะน้ำมันรำข้าว
                                4.2 ช้อนชากระเทียมสับ
                                5.1/2 ถ้วยหอมใหญ่หั่นเต๋า
                                6.1/2 ถ้วยต้นหอมหั่นท่อน
                                7.1/2 ถ้วยพริกชี้ฟ้าหั่นท่อน (ตามความชอบ)
                                8.2 ช้อนโต๊ะซอสหอยนางรม
                                9.1 ช้อนโต๊ะซีอิสูริ
                                10.1 ช้อนชาน้ำตาลทราย
                                11.1 ช้อนชาซีอิสูริเกลือ
                                12.1 ช้อนชาน้ำมันหอย
                                13.1 ช้อนชาซอสมะเขือเทศ (ตามความชอบ)
                                14.2 ช้อนโต๊ะซีอิสูริสีดำ (ใส่ตามความชอบ)
                                15.พริกไทยป่นตามชอบ
                                16.1 ลูกไข่ (ตีให้ผสมเข้ากับข้าว)
                            วิธีทำ
                                1.ในกระทะใหญ่ใส่น้ำมันรำข้าว 2 ช้อนโต๊ะ แล้วตั้งไฟกลาง
                                2.ใส่กระเทียมสับลงไปผัดจนหอม                             -
                                3.เพิ่มกุนเชียง (หรือหมูหมัก) เข้าไปผัดให้สุก
                                4.ใส่หอมใหญ่ ต้นหอม และพริกชี้ฟ้าลงไปผัดให้สุก
                                5.เติมซอสหอยนางรม ซีอิสูริ น้ำมันหอย น้ำมันรำข้าว ซีอิสูริสีดำ น้ำตาลทราย ซอสมะเขือเทศ และเกลือลงไป ผัดให้ส่วนผสมเข้ากัน
                                6.ใส่ข้าวสวยลงไป และผัดให้ทุกอย่างเข้ากัน
                                7.ใส่ไข่ที่ตีไว้ลงไปผัดให้ทุกอย่างเข้ากัน
                                8.ปรุงรสด้วยพริกไทยป่นตามความชอบ และปรับรสชาติตามต้องการ
                                9.ตักข้าวผัดกุนเชียงใส่จาน และเสิร์ฟทันที
""")
    elif mes == "ขนมปังไข่ชีส":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ขนมปังไข่ชีส
                                1.2 ถ้วยแป้งอเนกประสงค์
                                2.1/4 ถ้วยน้ำตาลทราย
                                3.1 ช้อนชาเบกกิ้งโซดา
                                4.1/4 ถ้วยน้ำมันสำหรับปรุงอาหาร
                                5.1/2 ถ้วยน้ำ (หรือตามความเหมาะสม)
                                6.2 ฟองไข่
                                7.1/2 ถ้วยชีสชีส (ชีสมอนซาเรลล่าหรือชีสแชดดาร์)
                                8.เนยสำหรับทาพิมพ์
                            วิธีทำ
                                1.เตรียมพิมพ์ขนมปังหรือถาดอบ และทาเนยลงไปให้ทั่ว
                                2.ในอ่างครัวใส่แป้งอเนกประสงค์ และน้ำตาลทราย คนให้เข้ากัน
                                3.เพิ่มน้ำมันสำหรับปรุงอาหารและเบกกิ้งโซดา เข้าไปคนให้เข้ากัน
                                4.เพิ่มไข่ลงไปคนให้เข้ากัน
                                5.เพิ่มชีสชีส (ชีสมอนซาเรลล่าหรือชีสแชดดาร์) เข้าไปคนให้เข้ากัน
                                6.เทส่วนผสมลงในพิมพ์หรือถาดที่ทาเนยไว้
                                7.นำไปอบในเตากลาง ที่200 องศาเซลเซียส เป็นเวลาประมาณ 15-20 นาที หรือจนขนมปังสุกทั่วทั้งตัว        
        """)
    elif mes == "ไข่เจียวผัก":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ไข่เจียวผัก
                                1.3-4 ฟองไข่
                                2.1/4 ถ้วยน้ำ (หรือตามต้องการ)
                                3.1/2 ถ้วยผักสดหรือผักตามชอบ (เช่น ถั่วงอก, ผักกาดขาว, มะระ, หรือผักอื่นๆ) หั่นเป็นชิ้นเล็กๆ
                                4.1 ช้อนชาซีอิสูริ
                                5.1 ช้อนชาซีอิสูริสีดำ
                                6.1/2 ช้อนชาเกลือ
                                7.1/2 ช้อนชาน้ำมัน    
                            วิธีทำ
                                1.ในชาม, คนไข่ให้เข้าเป็นเนื้อเดียวกัน
                                2.เพิ่มน้ำ, ซอสซีอิสูริ, ซอสซีอิสูริสีดำ, เกลือ, และน้ำมัน คนให้เข้าเนื้อเดียวกัน
                                3.เตรียมผักที่ต้องการใช้
                                4.ในกระทะ, เจียวไข่ที่ผสมส่วนผสมไว้ในข้อ 1 ในไฟอ่อนๆ
                                5.เมื่อไข่เริ่มจับตัว, กระจัดกระจายผักที่เตรียมไว้ลงไป
                                6.พลิกด้านให้สุกทั่ว และค่อยๆพลิกตัวให้สุกทั่ว
                                7.เมื่อไข่เจียวผักสุกแล้ว นำออกจากระทะ และเสิร์ฟร้อนๆ
    """)
    elif mes == "ไข่เจียวออมเล็ต":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ไข่เจียวออมเล็ต
                                1.3 ฟองไข่
                                2.1/4 ถ้วยน้ำ (หรือตามความชอบ)
                                3.เกลือและพริกไทยป่นตามความชอบ
                                4.ผสมผสานผักสดหรือวัตถุดิบที่ชอบ (เช่น หอมใหญ่, พริก, มะเขือเทศ, หรือเห็ด)
                            วิธีทำ
                                1.ทำการตั้งกระทะให้ร้อนพอดี แล้วเตรียมวัตถุดิบที่จะใส่ลงไปในไข่เจียว
                                2.คนไข่ในชามให้เข้ากัน ใส่น้ำ, เกลือ, และพริกไทยป่นตามความชอบ คนให้เข้าเนื้อเดียวกัน
                                3.ใส่ผักสดหรือวัตถุดิบที่เตรียมไว้ลงในไข่เจียว
                                4.นำผสมที่เตรียมไว้ลงไปในกระทะที่ร้อน แล้วทำการปรุงแต่งตามความชอบ
                                5.พับขอบไข่เพื่อให้ไข่เจียวไม่ติดกระทะ และให้สวยงาม
                                6.เมื่อไข่เจียวมีส่วนล่างทอดสีทอง และมีส่วนบนตั้ง ให้พลิกหลังไข่เจียวขึ้นไป ปรุงรสเพิ่มตามความชอบ
                                7.พลิกไข่เจียวกลับอีกครั้ง ให้ทอดสีทองทั้งสองด้าน และทำให้ไข่เจียวสุกทั้งหมด
                                8.นำออกจากกระทะและเสิร์ฟในจาน
                                   """)
    elif mes == "ผัดกะเพรา":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ผัดกระเพรา
                                1.2 ช้อนโต๊ะน้ำมันรำข้าว
                                2.4-5 กระเทียม สับ
                                3.5-10 พริกขี้หนู ตามความชอบ
                                4.1 ถ้วยใบกะเพรา ล้างและหริกซอย
                                5.2 ช้อนชาซีอิสูริ
                                6.1 ช้อนโต๊ะซีอิสูริสีดำ
                                7.1 ช้อนโต๊ะซอสปรุงรสหรือน้ำมันหอย
                                8.1/2 ช้อนชาน้ำมันหอย
                                9.1 ช้อนชาน้ำมันรำข้าว
                                10.1/2 ช้อนชาน้ำมันเลียน (ถ้ามี)
                                11.1 ช้อนชาน้ำมันงา
                                12.1 ช้อนชาน้ำมันพืชสำหรับทอด  
                            วิธีทำ  
                                1.ในกระทะ, ตั้งไฟทอดร้อนและใส่น้ำมันรำข้าว
                                2.ปรุงกระเทียมและพริกขี้หนูลงไปทอดจนหอม
                                3.ใส่เนื้อหมูหรือไก่ลงไปทอดจนสุก
                                4.เพิ่มซีอิสูริ, ซีอิสูริสีดำ, ซอสปรุงรสหรือน้ำมันหอย, น้ำมันรำข้าว, น้ำมันเลียน, น้ำมันหอย, น้ำมันงา, และน้ำมันพืช
                                5.ใส่ใบกะเพราลงไปผัดให้รสชาติทั่วทั้งกระทะ
                                6.ปรุงรสตามความชอบโดยเพิ่มน้ำมันหอยหรือซอสปรุงรสตามต้องการ
                                7.เมื่อกะเพราเริ่มสลดลงและผัดจนเนื้อสุก, จับไฟ   
                                   """)
    elif mes == "ข้าวผัดกุ้ง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวผัดกุ้ง
                                1.2 ถ้วยข้าวสวย (ต้มสุกและเย็น)
                                2.200-300 กรัมกุ้งขาว ล้างและปอกเปลือก
                                3.1/2 ถ้วยหอมใหญ่ซอย
                                4.1/4 ถ้วยถั่วลิสง
                                5.1/4 ถ้วยขิงซอย
                                6.2 ฟองไข่
                                7.3 ช้อนโต๊ะน้ำมันรำข้าว
                                8.2 ช้อนโต๊ะซอสหอยนางรม
                                9.1 ช้อนโต๊ะซอสถั่วเหลือง
                                10.1 ช้อนชาน้ำตาลทราย
                                11.1/2 ช้อนชาเกลือ
                                12.1/2 ช้อนชาซีอิสูริสีดำ (ตามความชอบ)
                                13.พริกไทยป่นตามความชอบ
                            วิธีทำ
                                1.ตั้งกระทะให้ร้อน ใส่น้ำมันรำข้าวลงไป
                                2.ปรุงกุ้งในกระทะ ผัดจนกุ้งสุก
                                3.ใส่หอมใหญ่, ถั่วลิสง, และขิงลงไปผัดในน้ำมันรำข้าว
                                4.พยักหลังกุ้งและวัตถุดิบอื่นๆ ไปด้านหน้าของกระทะ
                                5.ใส่ข้าวลงไปผัดในกระทะ คนให้ทุกอย่างเข้ากัน
                                6.ตีไข่ใส่ลงไปผัดในข้าว คนให้เข้ากัน
                                7.ปรุงรสด้วยซอสหอยนางรม, ซอสถั่วเหลือง, น้ำตาลทราย, เกลือ, และซีอิสูริสีดำ คลุกเคล้าให้เข้ากัน
                                8.ใส่กุ้งที่ได้ผัดไว้กลับลงไป คลุกเคล้าให้เข้ากับข้าว
                                9.ปรุงรสด้วยพริกไทยป่นตามความชอบ
                                10.ชิมรสชาติ และปรับตามความชอบของคุณ
                                11.จัดใส่จาน และเสิร์ฟทันที
                                   """)
    elif mes == "สุกี้":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม สุกี้
                                1.200-300 กรัมเส้นสุกี้ราเมน (Ramen noodles)
                                2.200-300 กรัมเนื้อหรือไก่ หรือทะเล (ตามความชอบ)
                                3.2-3 ฟองไข่ต้ม (ตามความชอบ)
                                4.หอมใหญ่ซอย
                                5.หัวหอมแดงซอย
                                6.น้ำมันหอยหรือซอสกลิ้ง
                                7.น้ำมันงา
                            วิธีทำ
                                1.ต้มน้ำให้เดือด และใส่ส่วนผสมสำหรับน้ำซุปลงไป ปรุงรสตามความชอบ
                                2.ต้มเส้นสุกี้ในน้ำเดือดจนสุก ตามคำแนะนำบนบรรจุภัณฑ์
                                3.นำเนื้อหรือไก่ และไข่ต้มไปต้มในน้ำซุป จนสุก
                                4.ตักเส้นสุกี้ลงในชาม และเทน้ำซุปที่ต้มไว้ลงไป
                                5.วางเนื้อหรือไก่ที่ต้มไว้ในน้ำซุป
                                6.โรยหอมใหญ่ซอย, หัวหอมแดงซอย, น้ำมันหอยหรือซอสกลิ้ง, น้ำมันงา
                                7.ติดและเสิร์ฟทันที
        """)
    elif mes == "ผัดพริกแกง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ผัดพริกแกง
                                1.200-300 กรัมเนื้อหมูหรือไก่ หั่นชิ้นบาง
                                2.2-3 ช้อนโต๊ะน้ำมันพืช
                                3.2-3 ช้อนโต๊ะพริกแกงเผ็ด (ตามความชอบ)
                                4.2-3 ช้อนโต๊ะพริกแกงเผ็ด (ตามความชอบ)
                                5.1 ช้อนชาผงกระหรี่
                                6.1/2 ถ้วยน้ำมะขามเปียก
                                7.1/2 ถ้วยน้ำมะนาว
                                8.1 ช้อนชาน้ำตาลทราย
                                9.1 ช้อนชาซอสหอยนางรม
                                10.1 ช้อนชาซอสปรุงรส
                                11.1 ช้อนชาน้ำปลา
                                12.1 ช้อนชาซีอิสูริสีดำ (ตามความชอบ)
                                13.1/2 ถ้วยใบมะกรูดซอย
                                14.1/2 ถ้วยใบโหระพา
                                15.หอมใหญ่ซอย (สำหรับตกแต่ง)
                            วิธีทำ
                                1.ตั้งกระทะให้ร้อน และใส่น้ำมันพืช
                                2.ปรุงเนื้อหมูหรือไก่ในน้ำมันร้อน จนสุก
                                3.ใส่พริกแกงเผ็ดและพริกแกงเผ็ดลงไปผัดให้หอม
                                4.ใส่ผงกระหรี่ลงไปผัดให้หอม
                                5.ใส่น้ำมะขามเปียก, น้ำมะนาว, น้ำตาลทราย, ซอสหอยนางรม, ซอสปรุงรส, น้ำปลา, และซีอิสูริสีดำลงไป คลุกเคล้าให้เข้ากัน
                                6.ใส่เนื้อหมูหรือไก่ที่ผัดไว้ลงไป คลุกเคล้าให้เนื้อทั้งหมดเข้ากับน้ำซุป
                                7.ใส่ใบมะกรูดซอย, ใบโหระพา และหอมใหญ่ซอย ผัดให้เข้ากัน
                                8.ตรวจสอบรสชาติและปรับตามความชอบ
                                9.ตักใส่จาน และเสิร์ฟทันที  
                                   """)
    elif mes == "ผัดกระเทียมพริกไทย":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ผัดกระเทียมพริกไทย
                                1.200-300 กรัมเนื้อหมูหรือไก่ (หรือเนื้อปูหรือกุ้งตามความชอบ)
                                2.2-3 ช้อนโต๊ะน้ำมันพืช
                                3.2 ช้อนโต๊ะกระเทียมสับหยาบ
                                4.1 ช้อนชาพริกไทยป่น
                                5.1 ช้อนโต๊ะซีอิ๊วขาว
                                6.1 ช้อนชาน้ำตาลทราย
                                7.1 ช้อนโต๊ะซอสหอยนางรม
                                8.1/2 ถ้วยต้นหอมซอย
                                9.1/2 ถ้วยพริกขี้หนูซอย (ตามความชอบ)
                                10.1/2 ถ้วยใบโหระพา (หรือใบผักชี)
                                11.พริกไทยป่นตามความชอบ
                            วิธีทำ
                                1.ตั้งกระทะให้ร้อน และใส่น้ำมันพืช
                                2.ปรุงเนื้อหมูหรือไก่ในน้ำมันร้อน จนสุก
                                3.ใส่กระเทียมสับหยาบลงไปผัดให้หอม
                                4.ใส่พริกไทยป่นลงไปผัดให้หอม
                                5.ใส่น้ำตาลทราย, ซีอิ๊วขาว, ซอสหอยนางรม ลงไป ผัดให้เข้ากัน
                                6.ใส่ต้นหอม, พริกขี้หนู, ใบโหระพา (หรือใบผักชี) ลงไปผัดให้เข้ากัน
                                7.ตรวจสอบรสชาติ และปรับตามความชอบ
                                8.โรยพริกไทยป่นตามความชอบ
                                9.ตักใส่จาน และเสิร์ฟทันที
                                   """)
    elif mes == "ข้าวขาหมู":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวขาหมู
                                1.ขาหมู (ประมาณ 2-3 ขา) - ทำความสะอาดและล้างให้สะอาด
                                2.5-6 ถ้วยน้ำ (สำหรับต้มขาหมู)
                                3.1 ถ้วยน้ำมะนาว (หรือใส่มะนาวหลายลูกตามความชอบ)
                                4.1/2 ถ้วยซีอิ๊วขาว
                                5.1/4 ถ้วยซอสหอยนางรม
                                6.1/4 ถ้วยซีอิ๊วดำ
                                7.1/4 ถ้วยน้ำตาลทราย
                                8.3 ช้อนโต๊ะพริกไทยป่น
                                9.1 ช้อนโต๊ะพริกขี้หนูสับ
                                10.1 หัวหอมใหญ่ (หั่นเต๋า)
                                11.5-6 กลีบกระเทียม (สับ)
                                12.1 ช้อนโต๊ะผงกระหรี่ (ตามความชอบ)
                                13.5-6 ใบมะกรูดซอย
                                14.1 ช้อนชาซีอิสูริสีดำ
                                15.น้ำมันหอย (ตามความชอบ)
                                16.พริกไทยป่น (ตามความชอบ)
                            วิธีทำ
                                1.ต้มขาหมูในน้ำประมาณ 5-6 ถ้วย จนน้ำเดือด แล้วลดไฟให้ต้มอ่อนๆ ประมาณ 2-3 ชั่วโมง หรือจนขาหมูนุ่ม
                                2.เมื่อขาหมูสุกแล้ว นำออกจากน้ำ พักไว้
                                3.ในกระทะ, ตั้งไฟต้มน้ำ และใส่ขาหมูที่ต้มสุกลงไป
                                4.ใส่ซีอิ๊วขาว, ซอสหอยนางรม, ซีอิ๊วดำ, น้ำตาลทราย, พริกไทยป่น, และพริกขี้หนูสับลงไป คนให้เข้ากัน
                                5.ใส่ผงกระหรี่, น้ำมะนาว, และซีอิสูริสีดำลงไป คนให้เข้ากัน
                                6.ใส่หอมใหญ่, กระเทียม, ใบมะกรูด, น้ำมันหอย, และซีอิ๊วดำลงไป คนให้เข้ากันอีกครั้ง
                                7.ตรวจสอบรสชาติ และปรับตามความชอบของคุณ
                                8.เสิร์ฟข้าวขาหมูท้อน้อยที่เตรียมไว้ โรยด้วยพริกไทยป่นตามความชอบ
                                   """)
    elif mes == "ข้าวมันไก่":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ข้าวมันไก่
                                สำหรับข้าวมัน:
                                1.2 ถ้วยข้าวหอมมะลิ (หรือข้าวหอมปลาร้า)
                                2.2 1/2 ถ้วยน้ำ
                                3.4-5 กลีบหอมแดง (หรือใบมะกรูด)
                                สำหรับไก่:
                                1.500 กรัมไก่ (ชิ้นหรือตัวเล็ก)
                                2.1 ถ้วยน้ำมันหอย
                                3.1/4 ถ้วยซอสหอยนางรม
                                4.1/4 ถ้วยซีอิ๊วขาว
                                5.2 ช้อนโต๊ะน้ำตาลทราย
                                6.1 ช้อนโต๊ะพริกไทยป่น
                                7.4-5 กลีบกระเทียม (สับ)
                                8.1 ช้อนชาน้ำมันหอย (สำหรับปรุงรสเพิ่มเติม)
                                สำหรับน้ำจิ้ม:
                                1.1 น้ำมันหอย
                                2.2 ซีอิ๊วขาว
                                3.3 พริกไทยป่น
                            วิธีทำ
                                1.ล้างข้าวให้สะอาดและนำไปหุงกับน้ำ 2 1/2 ถ้วย พร้อมใส่หอมแดงหรือใบมะกรูดลงไป
                                2.เมื่อข้าวสุกแล้วให้นำหอมแดงหรือใบมะกรูดออก และปิดฝาให้ข้าวสะเด็ดน้ำ
                                3.ในขณะที่กำลังหุงข้าว, นำไก่มาล้างให้สะอาด
                                4.ผสมน้ำมันหอย, ซอสหอยนางรม, ซีอิ๊วขาว, น้ำตาลทราย, พริกไทยป่น, กระเทียม (สับ), และน้ำมันหอย ในชาม นำไก่มาทอดในน้ำมันที่เราผสมไว้ จนกระทั่งสุก
                                5.ในกระทะ ใส่น้ำมันที่ใช้ทอดไก่ พร้อมที่ใช้แปรงน้ำมันที่ใช้ทอดไก่ลงไปผัดข้าวหอมมะลิ ให้รสชาติเข้ากับข้าว
                                6.เมื่อข้าวเริ่มเหลือง ใส่ไก่ทอดที่เราทอดไว้ลงไปผัด
                                7.ผัดให้เข้าเนื้อข้าว และไก่ ปรับรสตามชอบ พักไว้
                                8.ทำน้ำจิ้มโดยผสมน้ำมันหอย, ซีอิ๊วขาว, และพริกไทยป่น คนให้เข้ากัน
                                9.เสิร์ฟข้าวมันไก่พร้อมน้ำจิ้มที่เราทำไว้
                                   """)
    elif mes == "คะน้าหมูกรอบ":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม คะน้าหมูกรอบ
                                สำหรับหมูกรอบ:
                                1.200-300 กรัมหมูสามชั้นหั่นชิ้นบาง
                                2.1 ช้อนโต๊ะซอสหอยนางรม
                                3.1 ช้อนโต๊ะซอสอเนกประสงค์
                                4.1/2 ช้อนชาพริกไทยป่น
                                5.1 ช้อนโต๊ะน้ำมันหอย
                                6.1/2 ช้อนชาน้ำมันงา (หากมี)
                                สำหรับคะน้า:
                                1.1 กก. คะน้า หั่นเป็นท่อนยาวประมาณ 3 นิ้ว
                                2.4-5 กลีบกระเทียม (สับ)
                                3.3-4 หัวหอมใหญ่ (หั่นซอย)
                                4.2-3 ต้นหอมใหญ่ (ซอย)
                                5.2-3 ช้อนโต๊ะน้ำมันพืช
                                5.1 ช้อนโต๊ะซีอิ๊วขาว
                                6.1 ช้อนโต๊ะซอสหอยนางรม
                                7.1 ช้อนชาน้ำตาลทราย
                                8.1/2 ถ้วยน้ำ
                            วิธีทำ
                                1.ผสมหมูสามชั้นกับซอสหอยนางรม, ซอสอเนกประสงค์, พริกไทยป่น, น้ำมันหอย, และน้ำมันงา (หากใช้) ให้เข้ากันและนำไปทำหมูกรอบ โดยทอดในน้ำมันจนกรอบ จากนั้นตั้งไว้
                                2.ในกระทะ, ใส่น้ำมันพืช และให้กระเทียมสับ香เยิ้ม
                                3.ใส่คะน้าลงไปผัดพร้อมที่ใส่ซอสหอยนางรม, ซีอิ๊วขาว, น้ำตาลทราย, และน้ำ ผัดให้สุกเหลืองนุ่ม
                                4.เมื่อคะน้าสุก, ใส่หมูกรอบที่ทอดไว้ลงไปผัดให้เข้าเนื้อคะน้า
                                5.ปรุงรสตามชอบ, ใส่หอมใหญ่ซอย, ต้นหอมซอย, และคลุกเคล้าให้เข้ากัน
                                6.ตรวจสอบรสชาติ และปรับตามความชอบ
                                7.ตักใส่จาน และเสิร์ฟทันที
                                   """)
    elif mes == "มาม่าผัดใส่เนื้อสัตว์":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม:
                                1.1 ห่อมาม่า (รสที่ชอบ)
                                2.200-300 กรัมเนื้อสัตว์ (เลือกได้ตามความชอบ เช่น เนื้อหมู, เนื้อไก่, เนื้อเนื้อ)
                                3.1 ช้อนโต๊ะน้ำมันพืช
                                4.3-4 กระเทียม (สับ)
                                5.1 หอมใหญ่ (หั่นเต๋า)
                                6.1 ใบผักกาดขาว (หั่นเป็นท่อน)
                                7.1 ถ้วยบัวบก (หั่นท่อน)
                                8.2 ช้อนโต๊ะซอสปรุงรส
                                9.1 ช้อนโต๊ะซีอิ๊วขาว
                                10.1 ช้อนชาน้ำตาล
                                11.1/2 ช้อนชาซอสหอยนางรม
                                12.1/2 ช้อนชาพริกไทยป่น (ตามความชอบ)
                                13.ต้นหอมซอย (สำหรับตกแต่ง)
                                14.พริกหวานแดงซอย (ตามความชอบ)
                            วิธีทำ
                                1.ต้มน้ำในหม้อ และใส่มาม่าลงไปต้มจนสุกตามคำแนะนำบนบรรจุภัณฑ์ หลังจากนั้นกระดานโรยเนื้อมาม่าบนกระทะพอดี
                                2.ในกระทะ, ตั้งไฟกลาง, ใส่น้ำมันพืช, กระเทียม, หอมใหญ่, ผักกาดขาว, บัวบก และเนื้อสัตว์ลงไปผัดจนสุก
                                3.ใส่มาม่าที่ต้มสุกลงไปผัดรวมกัน
                                4.เติมซอสปรุงรส, ซีอิ๊วขาว, น้ำตาล, ซอสหอยนางรม, และพริกไทยป่น ผัดให้เข้ากัน
                                5.ปรุงรสตามชอบ และปรับความเผ็ดตามความชอบด้วยพริกหวานแดงซอย
                                6.ตักใส่จาน และตกแต่งด้วยต้นหอมซอย
                                7.พร้อมเสิร์ฟ!
                                   """)
    elif mes == "ผัดเผ็ดปลาดุกราดข้าว":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ผัดเผ็ดปลาดุกราดข้าว
                               1.สำหรับปลาดุกรา
                               2.200-300 กรัมปลาดุกรา (หรือปลาหมึกหรือปลากระพง)
                               3.1 ช้อนโต๊ะน้ำมันพืช
                               4.3 กลีบกระเทียม (สับ)
                               5.2 ต้นหอมใหญ่ (ซอย)
                               6.1 ถ้วยพริกแดง (ซอย)
                               7.1 ช้อนโต๊ะซีอิ๊วขาว
                               8.1 ช้อนโต๊ะซอสหอยนางรม
                               9.1 ช้อนโต๊ะซีอิ๊วดำ
                               10.1 ช้อนโต๊ะน้ำตาลทราย
                               11.1/2 ถ้วยน้ำ
                                สำหรับผัดเผ็ด
                               1.2 ช้อนโต๊ะเนื้อหมูหั่นชิ้นบาง
                               2.1 ช้อนโต๊ะน้ำมันพืช
                               3.3 ช้อนโต๊ะพริกแดงเผา (ตามความชอบ)
                               4.2 กลีบกระเทียม (สับ)
                               5.1 ต้นหอมใหญ่ (ซอย)
                               6.1 ถ้วยพริกขี้หนูสวน (หั่นท่อน)
                               7.1/2 ถ้วยซอสมะเขือเทศ
                               8.1/4 ถ้วยน้ำมะขามเปียก
                               9.1 ช้อนโต๊ะน้ำมันพืช
                               10.1 ช้อนชาน้ำตาลทราย
                               11.1 ช้อนชาน้ำปลา
                            วิธีทำ
                               1.ผ่าปลาดุกราเปิดเอาเส้นกระดูกออก แล้วหั่นชิ้นบาง
                               2.ในกระทะ, ใส่น้ำมันพืช และทอดกระเทียม, หอมใหญ่, พริกแดงลงไป
                               3.เพิ่มปลาดุกราลงไปผัดจนสุกและเหนียว
                               4.ใส่ซีอิ๊วขาว, ซอสหอยนางรม, ซีอิ๊วดำ, น้ำตาลทราย, และน้ำ ผัดให้เข้ากัน แล้วตั้งไว้
                               5.ในกระทะอีกหลัง, ใส่น้ำมันพืช, เนื้อหมู, พริกแดงเผา, กระเทียม, และหอมใหญ่ ผัดจนสุก
                               6.เติมพริกขี้หนูสวน, ซอสมะเขือเทศ, น้ำมะขามเปียก, น้ำมันพืช, น้ำตาลทราย, และน้ำปลา ผัดให้เข้ากัน
                               7.นำปลาดุกราที่ผัดไว้มาผสมกับผัดเผ็ด คนให้เข้ากัน
                               8.ตรวจรสชาติ และปรับตามความชอบ
                               9.ตักใส่จาน และเสิร์ฟทันที  
                                   """)
    elif mes == "สเต็ปลาแซลมอนย่างกับข้าวกล้อง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม สเต็ปลาแซลมอนย่างกับข้าวกล้อง
                                สำหรับลาแซลมอน
                                1.2 ชิ้นลาแซลมอน (ปริมาณตามความต้องการ)
                                2.1/4 ถ้วยซอสมิโซะ (Miso)
                                3.2 ช้อนโต๊ะซอสน้ำมันหอย
                                4.1 ช้อนชาซีอิ๊วขาว
                                5.1 ช้อนโต๊ะน้ำมันมะกอกหอย
                                6.1 ช้อนชาน้ำมันมะนาว
                                7.1 ช้อนชาน้ำมันงา (ถ้ามี)
                                8.1 ช้อนชาน้ำตาลทราย
                                สำหรับข้าวกล้อง
                                1.ข้าวกล้อง (ปริมาณตามความต้องการ)
                            วิธีทำ
                                1.เตรียมลาแซลมอน: ผสมซอสมิโซะ, ซอสน้ำมันหอย, ซีอิ๊วขาว, น้ำมันมะกอกหอย, น้ำมันมะนาว, น้ำมันงา (ถ้าใช้), และน้ำตาลทรายในชาม คนให้เข้ากัน.
                                2.นำลาแซลมอนมาทาซอสที่เตรียมไว้ให้ทั่วตัว แล้วนำไปย่างในเตาอบหรือกระทะย่าง จนลาแซลมอนสุกสีทองอร่อย คล้ายๆ กับการย่างปลากระพง.
                                3.เตรียมข้าวกล้องตามปริมาณที่ต้องการ
                                4.เสริฟลาแซลมอนย่างที่ได้รับความร้อนร้อน คู่กับข้าวกล้อง  
                                   """)
    elif mes == "สลัดผักปลาย่าง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม สลัดผักปลาย่าง
                                สำหรับปลาย่าง
                                1.200-300 กรัมปลา (ใช้ปลาตามชอบ เช่น ปลาแซลมอน, ปลาทู, หรือปลากระพง)
                                2.2 ช้อนโต๊ะน้ำมันมะกอก (หรือน้ำมันพืช)
                                3.1 ช้อนชาซอสปรุงรส
                                4.1/2 ช้อนชาพริกไทยป่น (ตามความชอบ)
                                สำหรับสลัด
                                1.ผักสลัดตามชอบ (เช่น คะน้า, ถั่วฝักยาว, แตงกวา, มะระขี้นก)
                                2.1 ลูกมะเขือเทศ (หั่นเต๋า)
                                3.1 ลูกหอมใหญ่ (หั่นเต๋า)
                                4.1 หัวหอมใหญ่ (ซอย)
                                5.2 ช้อนโต๊ะถั่วลิสงคั่ว
                                6.2 ช้อนโต๊ะข้าวโพดคั่ว
                                7.2 ช้อนโต๊ะน้ำมันมะกอก (หรือน้ำมันพืช)
                                8.1 ช้อนโต๊ะน้ำมันงา
                                9.2 ช้อนโต๊ะซอสหอยนางรม
                                10.1 ช้อนโต๊ะน้ำมันหอย
                                11.1 ช้อนโต๊ะน้ำมันหอยขาว
                                12.1 ช้อนชาซีอิ๊วขาว
                                13.1 ช้อนชาน้ำตาลทราย (หากต้องการ)
                                14.1/2 ช้อนชาพริกไทยป่น (ตามความชอบ)
                                15.น้ำมะนาวหรือน้ำมะขามเปียกสำหรับปรุงรส
                                วิธีทำ
                                1.แปรงปลาด้วยน้ำมันมะกอกหรือน้ำมันพืช และคั่วด้วยไฟอ่อนๆ ในกระทะจนสุก
                                2.ใส่ซอสปรุงรสและพริกไทยป่นลงไปผัดจนทั่วถึง พักไว้
                                3.ในชามใหญ่, ผสมผักสลัดที่เตรียมไว้
                                4.นำปลาย่างมาตักใส่ชามผักสลัด
                                5.ผสมน้ำมันมะกอก, น้ำมันงา, ซอสหอยนางรม, น้ำมันหอย, น้ำมันหอยขาว, ซีอิ๊วขาว, น้ำตาลทราย (ถ้าใช้), พริกไทยป่น, และน้ำมะนาวหรือน้ำมะขามเปียก เพื่อทำเป็น dressing
                                6.ราด dressing ลงไปบนสลัด
                                7.คลุกเคล้าให้ทุกอย่างเข้ากัน
                                8.ตักใส่จาน และเสิร์ฟทันที
                                   """)
    elif mes == "ยำตะไคร้ทูน่า":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ยำตะไคร้ทูน่า
                                สำหรับทูน่า
                                1.200-300 กรัมทูน่า (สะอาดและหั่นชิ้น)
                                2.1 ช้อนโต๊ะน้ำมันปี๊บ (หรือน้ำมันพืช)
                                สำหรับยำ
                                1.2-3 ต้นตะไคร้ (หั่นละเอียด)
                                2.1 หัวหอมใหญ่ (หั่นละเอียด)
                                3.3-4 ลูกมะนาว (สกปรก)
                                4.1-2 ช้อนโต๊ะน้ำปลา
                                5.1-2 ช้อนโต๊ะน้ำมะนาว
                                6.1 ช้อนโต๊ะน้ำมันหอย
                                7.1 ช้อนโต๊ะน้ำมันงา
                                8.1-2 ช้อนชาน้ำมันพริก (ตามความชอบ)
                                9.1-2 ช้อนชาน้ำตาลทราย
                                10.1-2 ช้อนชาพริกป่น (ตามความชอบ)
                                11.มะนาว (หั่นเต๋า หรือสกปรก)
                                12.ต้นหอม (ซอย)
                                13.พริก (ซอย)
                            วิธีทำ
                                1.ในกระทะ, ตั้งไฟกลาง, ใส่น้ำมันปี๊บ และทอดทูน่าจนสุก
                                2.ในชาม, ผสมตะไคร้, หอมใหญ่, มะนาว, น้ำปลา, น้ำมะนาว, น้ำมันหอย, น้ำมันงา, น้ำมันพริก, น้ำตาลทราย, และพริกป่น เคลือบทูน่าที่ทอดเสร็จ
                                3.ตรวจรสชาติและปรับตามความชอบ
                                4.ใส่ต้นหอม, มะนาว, และพริกลงไปผสมให้เข้ากัน
                                5.ตักใส่จาน และเสิร์ฟทันที                                
                                   """)
    elif mes == "น้ำพริกอ่องไก่สับกับข้าวกล้อง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม น้ำพริกอ่องไก่สับกับข้าวกล้อง
                                สำหรับน้ำพริกอ่องไก่สับ
                                1.หน่อไม้ฝรั่ง (หั่นละเอียด)
                                2.ปีกไก่ (สับ)
                                3.น้ำมันพืช
                                4.กระเทียม (สับ)
                                5.พริกแดง (สับ)
                                6.น้ำปลา
                                7.น้ำตาลทราย
                                8.มะนาว (สกปรก)
                                9.น้ำเปล่า
                                10.สำหรับข้าวกล้อง:
                                11.ข้าวกล้อง
                            วิธีทำ
                                1.นำหน่อไม้ฝรั่ง, ปีกไก่, กระเทียม, และพริกแดงลงในกระทะที่มีน้ำมันพืช ผัดจนหน่อไม้ฝรั่งนิ่ม และกลิ่นหอม
                                2.เติมน้ำปลา, น้ำตาลทราย, และมะนาวลงไป คนให้เข้ากัน
                                3.นำปีกไก่ที่สับลงไปผัดให้สุก
                                4.ตรวจรสชาติและปรับตามความชอบ
                                5.ตักใส่ชามและเติมน้ำเปล่าลงไปตามความต้องการ
                                6.ทำข้าวกล้องตามขั้นตอนที่ระบุบนบรรจุภัณฑ์
                                7.จัดเสิร์ฟน้ำพริกอ่องไก่สับด้วยข้าวกล้องที่สุกในจานเดี่ยวกัน

                                   """)
    elif mes == "ทอดมันปลาดอรี่กับข้าวกล้อง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม ทอดมันปลาดอรี่กับข้าวกล้อง
                                สำหรับทอดมันปลาดอรี่:
                                1.300 กรัมปลาดอรี่ (ล้างและสับละเอียด)
                                2.1/4 ถ้วยแป้งทอดกรอบ
                                3.2 ช้อนโต๊ะแป้งข้าวโพด
                                4.1 ช้อนโต๊ะน้ำมันหอย
                                5.2 ช้อนโต๊ะพริกไทยป่น
                                6.2 ช้อนโต๊ะน้ำปลา
                                7.2 ช้อนชาน้ำมันพืช (สำหรับทอด)
                                สำหรับซอสน้ำจิ้ม:
                                1.3 ช้อนโต๊ะซอสหอยนางรม
                                2.1 ช้อนโต๊ะน้ำมะขามเปียก
                                3.1 ช้อนชาน้ำตาลทราย
                                4.1 ช้อนชาพริกไทยป่น (ตามชอบ)
                                สำหรับข้าวกล้อง:
                                1.ข้าวกล้อง
                            วิธีทำ
                                1.ในชามใหญ่, ผสมปลาดอรี่, แป้งทอดกรอบ, แป้งข้าวโพด, น้ำมันหอย, พริกไทยป่น, น้ำปลา, และน้ำมันพืช คนให้เข้ากัน
                                2.ตั้งกระทะใส่น้ำมันพืชให้เปียก, นำส่วนผสมปลาดอรี่ลงทอดในน้ำมันร้อน ทอดจนกรอบทั้งสองด้าน จากนั้นตั้งขึ้นสะเปาะน้ำมัน
                                3.ในถ้วย, ผสมซอสหอยนางรม, น้ำมะขามเปียก, น้ำตาลทราย, และพริกไทยป่น คนให้เข้ากัน
                                4.ตั้งเตาไฟให้ร้อน, นำประทัดข้าวกล้อง
                                5.เสิร์ฟทอดมันปลาดอรี่ร้อน ๆ พร้อมกับซอสน้ำจิ้มและข้าวกล้อง        
                                   """)
    elif mes == "แซลมอนอบกับสลัดมะม่วงอะโวคาโด":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม แซลมอนอบกับสลัดมะม่วงอะโวคาโด
                                1.สำหรับแซลมอนอบ:
                                2.2 ชิ้นแซลมอน (ปลาแซลมอน)
                                3.1 ช้อนชาน้ำมันมะกอก
                                4.1 ช้อนชาซอสปรุงรส
                                5.1/2 ช้อนชาเกลือ
                                6.1/2 ช้อนชาพริกไทย
                                สำหรับสลัดมะม่วงอะโวคาโด:
                                1.1 ลูกมะม่วง (หั่นเต๋า)
                                2.1 ลูกอะโวคาโด (หั่นเต๋า)
                                3.1/2 หัวหอมใหญ่ (ซอย)
                                4.1/4 ถ้วยมะนาว (สกปรก)
                                5.1 ช้อนโต๊ะน้ำตาลทราย
                                6.1 ช้อนชาซอสปรุงรส
                                7.1 ช้อนโต๊ะน้ำมะนาว
                                8.1 ช้อนโต๊ะน้ำมันมะกอก
                                9.1/4 ช้อนชาเกลือ
                                10.1/4 ช้อนชาพริกไทย
                            วิธีทำ
                                1.ในชาม, ผสมน้ำมันมะกอก, ซอสปรุงรส, เกลือ, และพริกไทย เป็นส่วนผสมทาทั้งสองด้านของแซลมอน
                                2.นำแซลมอนมาแช่ในส่วนผสมที่ทำไว้ในชาม ประมาณ 15-30 นาที (หากมีเวลามากขึ้นจะทำให้รสชาติซึมลึกขึ้น)
                                3.ต้มเตรียมเตาอบที่ความร้อน 180 องศาเซลเซียส
                                4.นำแซลมอนที่แช่ส่วนผสมออกมาแบบเล็กน้อย แล้วนำไปอบในเตาอบ ประมาณ 12-15 นาทีหรือจนปลาสุก
                                5.ในระหว่างที่แซลมอนกำลังอบ, ผสมมะม่วง, อะโวคาโด, หอมใหญ่, มะนาว, ซอสปรุงรส, น้ำมะนาว, น้ำมันมะกอก, เกลือ, และพริกไทย ในชาม คลุกเคล้าให้เข้ากัน
                                6.ตรวจรสชาติและปรับตามความชอบ
                                7.เมื่อแซลมอนอบเสร็จ, จัดใส่จาน และเสิร์ฟพร้อมกับสลัดมะม่วงอะโวคาโดที่เตรียมไว้   
        """)
    elif mes == "เส้นบุกผัดขี้เมากุ้งสด":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม เส้นบุกผัดขี้เมากุ้งสด
                                1.เส้นบุก (รีบอน หรือ เส้นมะพร้าว) 200 กรัม
                                2.กุ้งสด 200 กรัม (ล้างสะอาดและผ่าหลัง)
                                3.กระเทียม 4-5 กลีบ (สับ)
                                4.พริกขี้หนู ตามความชอบ (ซอย)
                                5.คื่นช่าย หรือกระชายซอย ตามความชอบ
                                6.ผักบุ้งไทยหรือผักที่ชอบ 200 กรัม
                                7.ซีอิ๊วขาว 2 ช้อนโต๊ะ
                                8.ซอสหอยนางรม 1 ช้อนโต๊ะ
                                9.ซอสปรุงรส 1 ช้อนโต๊ะ
                                10.น้ำมันพืชสำหรับผัด
                            วิธีทำ
                                1.นำเส้นบุกต้มในน้ำเดือดตามคำแนะนำบนบรรจุภัณฑ์ และเมื่อสุก ตักขึ้นพักไว้
                                2.ในกระทะ, ตั้งไฟกลาง, ใส่น้ำมันพืช
                                3.พอน้ำมันร้อน, ใส่กระเทียมและพริกขี้หนูลงไป ผัดให้หอม
                                4.ใส่กุ้งลงไปผัดจนสุก
                                5.เพิ่มเส้นบุกลงไปผัดให้เข้าเนื้อกุ้ง
                                6.ใส่ผักบุ้งไทยหรือผักที่ชอบลงไป ผัดให้สุก
                                7.เติมซีอิ๊วขาว, ซอสหอยนางรม, ซอสปรุงรส ลงไป และผัดให้เข้ากัน
                                8.ตรวจรสชาติและปรับตามความชอบ
                                9.ตักใส่จาน และเสิร์ฟทันที
                                   """)
    elif mes == "เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น
                                1.เส้นบุก (รีบอนหรือเส้นมะพร้าว) 200 กรัม
                                2.น้ำสลัดญี่ปุ่น 1/4 ถ้วย
                                3.ซีอิ๊วขาว 2 ช้อนโต๊ะ
                                4.น้ำมันงา 1 ช้อนโต๊ะ
                                5.น้ำตาลทราย 1 ช้อนชา
                                6.งาขาวป่น (สำหรับตกแต่ง)
                                7.ถั่วงอก (ใส่ตามชอบ)
                                8.ถั่วลันเตา (ใส่ตามชอบ)
                                9.แครอท (ซอยหรือหั่นเส้น)
                                10.พริก (ซอย)
                                11.น้ำสลัด (สำหรับใส่ลงไปในกระทะ)
                                วิธีทำ
                                1.นำเส้นบุกต้มในน้ำเดือดตามคำแนะนำบนบรรจุภัณฑ์ และเมื่อสุก ตักขึ้นพักไว้
                                2.ในกระทะ, ตั้งไฟกลาง, ใส่น้ำมันงา
                                3.เมื่อน้ำมันร้อน, ใส่แครอทและผัดให้สุก
                                4.เพิ่มถั่วงอก, ถั่วลันเตา, และพริกลงไป ผัดให้สุก
                                5.เทเส้นบุกที่ต้มสุกลงไปในกระทะผัด ใส่น้ำสลัดญี่ปุ่น, ซีอิ๊วขาว, น้ำตาลทราย ผัดให้เข้ากัน
                                6.ตรวจรสชาติและปรับตามความชอบ
                                7.ตักใส่จาน และเสิร์ฟทันที
                                8.ตกแต่งด้วยงาขาวป่น
                                   """)
    elif mes == "เส้นบุกผัดเห็ดหูหนูกระเทียมดอง":
        await message.channel.send("""มีดังนี้
                            ส่วนผสม เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
                                1.เส้นบุก 200 กรัม (ต้มสุก)
                                2.เห็ดหูหนู 200 กรัม (ล้างและหั่นเป็นชิ้น)
                                3.กระเทียม 3-4 กลีบ (สับ)
                                4.น้ำมันพืช 2 ช้อนโต๊ะ
                                5.ซีอิ๊วขาว 2 ช้อนโต๊ะ
                                6.น้ำมันงา 1 ช้อนชา
                                7.น้ำตาลทราย 1 ช้อนชา
                                8.ซอสปรุงรส 1 ช้อนโต๊ะ
                                9.พริกไทยป่น ตามความชอบ
                                10.ถั่วงอก (ต้มสุก)
                                11.ผักชี สำหรับตกแต่ง
                            วิธีทำ
                                1.นำเส้นบุกต้มในน้ำเดือดตามคำแนะนำบนบรรจุภัณฑ์ และเมื่อสุก ตักขึ้นพักไว้.
                                2.ในกระทะ, ตั้งไฟกลาง, ใส่น้ำมันพืช.
                                3.พอน้ำมันร้อน, ใส่กระเทียมลงไป ผัดให้หอม.
                                4.เพิ่มเห็ดหูหนูลงไป ผัดจนสุก.
                                5.ใส่เส้นบุกลงไปผัดให้เข้าเนื้อเห็ด.
                                6.เติมซีอิ๊วขาว, น้ำมันงา, น้ำตาลทราย, ซอสปรุงรส, และพริกไทยป่น ลงไป ผัดให้เข้ากัน.
                                7.เพิ่มถั่วงอกลงไปผัดในกระทะ.
                                8.ตรวจรสชาติและปรับตามความชอบ.
                                9.ใส่ผักชีลงไป ผัดให้เข้ากัน.
                                10.ตักใส่จาน และเสิร์ฟทันที.
                                   """)
    elif mes == "บอกรัก":
        await message.channel.send("รักนะค้าบ🤍")
    elif mes == "รักเจมนะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมอ่ะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "รักเจมอะ":
        await message.channel.send("พูดงี้เจมเขินนะครับ😖")
    elif mes == "เจอกันนะเจม":
        await message.channel.send("ไว้เจอกันใหม่ค้าบ"+(message.author.name)+"🤍")
    elif mes == "":
        await message.channel.send()
    elif mes == "เจอกันพน":
        await message.channel.send("ไว้เจอกันใหม่ค้าบ"+(message.author.name)+"🤍")
    elif mes == "เจอกันพรุ่งนี้":
        await message.channel.send("ไว้เจอกันใหม่ค้าบ"+(message.author.name)+"🤍")
    elif mes == "เกิดใหม่ทั้งทีก็กลายเป็นสไลม์ไปซะแล้ว":
        await message.channel.send("""เนื้อเรื่องจะว่าด้วยชายโสดวัย 37 “มิคามิ ซาโตรุ” ผู้ถูกโจรวิ่งราวเอามีดแทงเสียชีวิต ก่อนมาเกิดเป็น “ริมูรุ เทมเพสต์” ตัวสไลม์ในต่างโลก ซึ่งความพิเศษของสไลม์ที่ดูจะกากกื๋อนี้ก็คือนอกจากปรับเปลี่ยนรูปร่างได้ตามใจนึกแล้ว หากเขมือบอะไรเข้าไปก็จะได้รับความสามารถเฉพาะของสิ่งมีชีวิตชนิดนั้นมาด้วย กระทั่งหลังออกผจญภัยมาเรื่อยๆ เจ้าตัวก็ได้ผู้ติดตามมากขึ้นจนได้รับการสถาปนาขึ้นเป็นผู้นำ พร้อมๆ กับการก่อตั้งประเทศตัวเองอย่าง “สมาพันธ์มอนสเตอร์จูร่า เทมเพสต์” ขึ้นมาในที่สุด""")
    elif mes == "Tsuki ga Michibiku Isekai Douchuu":
        await message.channel.send("""หนุ่มมัธยมในญี่ปุ่นที่มีสายเลือดพ่อแม่เป็นชาวต่าวโลก ถูกหนึ่งในสามเทพ สึคุโยมิ เทพแห่งดวงจันทร์ อัญเชิญกลับโลกแฟนตาซีในฐานะผู้กล้า แต่เมื่อส่งให้เทพธิดาที่ดูแลผู้กล้าจากต่างโลกรับช่วงต่อ เธอกลับไม่พอใจหน้าตาเขาที่มองว่าอัปลักษณ์ จึงไม่ให้เป็นผู้กล้า แล้วส่งให้ไปอยู่ที่สุดขอบโลกในดินแดนของเหล่าอมนุษย์ที่ไร้ผู้คน ถูกสาปไม่ให้คุยกับมนุษย์ได้ เขาได้พบสหายร่วมเดินทาง โทโมเอะ (ชิน) สัตว์ประหลาดมังกรที่ชอบละครย้อนยุคญี่ปุ่น มิโอะ แมงมุมยักษ์โรคจิตสายมาโซ การเรื่องราวการผจญภัยที่ชวนปวดหัวจึงได้เริ่มขึ้น""")
    elif mes == "เพราะพระเจ้าเลือกเลยได้เกิดใหม่มาเลี้ยงสไลม์ในต่างโลก":
        await message.channel.send("""เรื่องราวของการ์ตูนเรื่องนี้จะเป็นการเล่าถึงโลกคู่ขนานที่สามารถใช้เวทมนต์ได้ ทาเคบายิชิ เรียวมะ ชายวัยกลางคนที่ได้รับโอกาสจากพระเจ้าของโลกคู่ขนานนี้ให้ไปเกิดใหม่เป็นเด็กชายวัย 8 ขวบ ต้องใช้ชีวิตอยู่ในป่าใหญ่กับสไลม์หลายพันตัว จนกระทั่งวันหนึ่งเขาได้พบกันเหล่าทหารที่กำลังบาดเจ็บจาการต่อสู้และเขาได้เข้าไปช่วยไว้ ทำให้เขาได้เริ่มรู้จักกับคนอื่นๆ ที่เป็นคนจริงๆไม่ใช่สไลม์ และตัวเขาก็ได้ย้ายเข้าไปอยู่ในเมือง ซึ่งนั่นเองเป็นจุดเริ่มต้นเรื่องราวของเขา""")
    elif mes == "ชาตินี้พี่ต้องเทพ":
        await message.channel.send("""เป็นเรื่องราวของชายวัย 34 ที่ใช้ชีวิตแบบ "Neet" เป็นคนไร้งาน ในขณะที่เขาโดนเตะออกจากบ้านด้วยเหตุผลบางอย่าง เขาได้เหลียวมองไปเจอเด็กผู้หญิงมัธยมปลายคนหนึ่งกำลังโดนแกล้งในตอนนั้นเขเห็นรถบรรทุกกำลังจะวิ่งจนเด็กผู้หญิงเขาได้ตัดสินใจวิ่งเข้าไปช่วย จนทำให้เขาเสียชีวิต ในโลกหลังตายเขาได้เกิดใหม่อีกครั้งในโลกแฟนตาซีในฐานะเด็กผู้ชาย Rudeus ในชีวิตเกิดใหม่เขาจะต้องเจอผู้หญิงหลายประเภท และการต่อสู้ที่กำลังรอเขาอยู่ ชีวิตในโลกแห่งแฟนตาซีได้เริ่มขึ้นแล้ว""")
    elif mes == "สุดยอดมือสังหารอวตารมาต่างโลก":
        await message.channel.send("""มือสังหารผู้ที่ได้รับการเลื่องลือว่าเป็นมือสังหารที่แข็งแกร่งที่สุดในโลกนั้น ในวันหนึ่งเขาได้ถูกองค์กรหักหลังและถูกกำจัดในที่สุด สิ่งที่เฝ้ารอเขาหลังความตายก็คือเทพธิดานั่นเอง เทพธิดาได้ทำการไหว้วานเรื่องหนึ่งกับมือสังหาร นั่นก็คือคำไหว้หวานให้ลอบสังหารผู้กล้าที่ต่างโลก ซึ่งจะเป็นตัวการนำพาให้โลกล่มสลายในอีก 18 ปีให้หลังนั่นเอง มือสังหารที่แข็งแกร่งที่สุดที่รับคำไหว้วานนั้น ได้กลับชาติไปเกิดใหม่เป็นลูกห์ลูกชายคนโตของตระกูลขุนนางนักฆ่านั่นเอง แม้ว่าเขาจะสับสนกับความรักจากครอบครัวที่ในชาติก่อนเขาไม่เคยได้รับ แต่ลุคก็เติบโตขึ้นเรื่อย ๆ ในฐานะมือสังการ นี่เป็นเรื่องราวของแฟนตาซีแนวลอบสังหาร ที่ต่างโลกซึ่งเขาใช้สกิลที่ตัวเองเลือกเองในตอนที่เกิดใหม่กับศาสตร์ลับของตระกูลนักฆ่าและประสบการณ์ในอดีตเป็นอาวุธเพื่อฝ่าฝันภารกิจอันยากลำบากอย่างการลอบสังหารผู้กล้า""")
    elif mes == "RE Zero":
        await message.channel.send("""โดยเนื้อเรื่องคร่าว ๆ ของอนิเมะเรื่องรีซีโร่นั้นจะกล่าวถึง นัทสึกิ สุบารุ เด็กหนุ่มผู้ไม่สนโลก ชอบนั่งเล่นเกม หมกตัวอยู่แต่ในบ้านเป็นชีวิตจิตใจ อยู่มาวันหนึ่งในขณะที่เขากำลังเดินออกมาจากร้านสะดวกซื้อ ตัวเขาก็ได้พบเจอกับเหตตุการณ์ประหลาดเข้า นั่นก็คือ การถูกวาร์ปพามาต่างโลก ดินแดนที่ทั้งมนุษย์และสิ่งมีชีวิตรูปร่างแปลกตาได้มาอาศัยอยู่ร่วมกันตัวเด็กหนุ่มเองถึงแม้จะเจอเหตุการณ์ประหลาดแต่เขาก็ไม่ได้มีอาการตกใจอะไรมากนัก กลับคิดว่าเป็นโชคดีที่ตัวเองได้มาโผล่ต่างโลกเสียด้วยซ้ำไป จนแล้วจนรอด ด้วยความอวดดีของเด็กหนุ่มที่คิดว่าตัวเองเป็นผู้กล้า มีพลังวิเศษ เขาจึงได้ถูกพวกโจรแถวซอกตึกรุมทำร้ายจนตาย""")
    elif mes == "ยุทธศาสตร์กู้ชาติของราชามือใหม่":
        await message.channel.send("""เป็นเรื่องราวของชายหนุ่มวัย 19 ปี คาซึยะ โซมะ (Kazuya Souma) ผู้ที่ยืนหยัดแต่ตั้งใจจะเป็นข้าราชการ ทำงานรับใช้ประชาชน เรื่องราวเริ่มต้นหลังจากที่ปู่ ครอบครัวที่เหลืออยู่เพียงคนเดียวของเขาได้เสียชีวิตไป แต่แล้วเขากลับถูกอัญเชิญมายังอาณาจักร เอลฟรีเดน (Elfrieden) ในฐานะผู้กล้าซะอย่างนั้น ท่ามกลางสงครามระหว่างดินแดนปีศาจ กับมวลมนุษย์ โลกกำลังอยู่ในสถานการณ์ที่เสี่ยง ถึงอย่างนั้นเขาดันไม่ได้กลายเป็นผู้กล้าแบบในอนิเมะ บู๊แหลกซะนี่สิ""")
    elif mes == "ข้าก้าวผ่าน 1 ล้านชีวิตเพื่อพิชิตเกมมรณะ":
        await message.channel.send("""เด็กหนุ่มมัธยมต้นปี 3 ชมรมกลับบ้านผู้ไม่สนใจคนรอบตัว เบื่อโลกปัจจุบัน จนวันหนึ่ง เขาถูกส่งไปต่างโลกที่คล้ายเกม ได้พบเพื่อนร่วมชั้นหญิงสองคน ชินโด อิอุ และ ฮาโดซากิ คุสึเอะ พร้อม Game Master จึงได้ทราบว่าเขาเป็นคนที่สามในกลุ่มที่ถูกส่งมา ให้ภารกิจที่มีเวลาจำกัด สุ่มอาชีพให้ ยูสึเกะ ได้อาชีพสุ่มเป็น ชาวนา ที่อ่อนแอ ทั้งสามต้องผ่านเควสต์ที่ยากเกิน เพื่อปกป้องโลกของเขา แม้จะต้องตายนับครั้งไม่ถ้วนก็ตาม""")
    elif mes == "Itai no wa Iya nano de":
        await message.channel.send("""ฮอนโจ คาเอเดะ (เมเปิ้ล) สาวน่ารักที่ถูกเพื่อน ชิโรมิเนะ ริสะ (ซารี่) ชวนมาเล่นเกมในโลกเสมือนจริง VRMMORPG แต่มือใหม่แบบเธอ ไม่อยากเจ็บตัว จึงเน้นเรื่องการป้องกันเป็นพิเศษ เน้นค่า VIT ไม่อัพค่าอื่น แต่ศัตรูทำ Damage ไม่เข้า พร้อมมีสกิลการป้องกันสมบูรณ์แบบ เธอได้ออกผจญภัย รู้จักผู้เล่นคนอื่นๆ และกลายเป็นที่รู้จักในภายหลังนิยายผจญภัยแฟนตาซี ผสมชีวิตประจำวัน Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu ต้นฉบับเป็นนิยายบนเว็บ Shousetsuka ni Narou เขียนโดย Yuumikan เริ่มเขียนตั้งแต่ปี 2016 มีผู้ชมกว่า 6 ล้านเพจวิว ปัจจุบันช่วงประกาศอนิเมะ มีประมาณ 225 ตอน""")
    elif mes == "Sword Art Online":
        await message.channel.send("""เรื่องราวของโปรแกรมเมอร์อัจฉริยะ ที่มีชื่อว่า คิริงายะ คาสึโตะ เขาได้เข้าร่วมเล่น เกมเสมือนจริงที่มีชื่อว่า Sword Art Online หรือ SAO ซึ่งเมื่อเขาเล่นเกมส์ ต้อง พบว่าตนเองไม่สามารถลอ็กเอาท์ออกจากเกมได้ เหล่าผู้เล่นเกมทั้งหมดต้องติด อยู่ภายในเกมโดยไม่มีใครรู้ว่าผู้พัฒนาเกมมีเป้าหมายที่แท้จริงอย่างไรกันแน่!!!แต่ทางออกจากเกมนี้ไปได้มีเพียงต้องเคลียร์เกมได้สำเร็จ หรือโอเวอร์ในเกม ก็หมายถึง การตายของผู้เล่นที่เกิดขึ้นจริง ดังนั้นเพื่อตอบสนองเงื่อนไขของการเคลียร์เกมนี้และออก จากโลกเสมือนจริง คาสึโตะจึงต้องเคลียร์เกมนี้ให้สำเร็จให้ได้ หรือเขาต้องพบกับความตาย!!! ติดตามชมและร่วมลุ้นไปกับคาสึโตะได้ใน Sword Art Online""")
    elif mes == "ทะเลาะกับแฟนมา":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "ทะเลาะกับแฟน":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "เจมโอ๋หน่อยทะเลาะกับแฟน":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "โอ๋หน่อยทะเลาะกับแฟน":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "Ragna Crimson":
        await message.channel.send("""บอกเล่าเรื่องราวของโลกแฟนตาซีที่มนุษย์อยู่ใกล้ปากและล้อมรอบด้วยมังกร “Ragna” นักล่ามังกรใช้อาวุธเงินเพื่อสังหารมังกรและสะสมรางวัลที่เฝ้าฝึกฝนอยู่ทุกวันเพื่อไล่ตาม “Leonica” นักล่ามังกรอัจฉริยะคู่หูของเขา โดยที่เขาเองก็ไม่รู้ว่าในตัวเขานั้นมีพลังที่เหนือจินตนาการหลับไหลอยู่

หลังจากนั้นการท้าทายกับผู้แข็งแกร่ง การต่อต้านที่ถูกโชคชะตาบีบบังคับที่ปลายทางของขีดจำกัดสู่การต่อสู้อันเข้มข้นในต่างโลกที่สุดแสนฮาร์ดคอร์เริ่มขึ้นแล้ว!!

แหมพอพูดถึงมังกรมันก็ต้องมาคู่กับเวทมนตร์แหละเนอะ ซึ่งต้องบอกเลยว่าเป็นอนิเมะที่โคตรมันส์""")
    elif mes == "โอ๋หน่อย":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "โอ๋แบมหน่อย":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "โอ๋เราหน่อย":
        await message.channel.send("โอ่ๆนะครับคนเก่ง🤍")
    elif mes == "Hametsu no Oukoku":
        await message.channel.send("""บอกเล่าเรื่องราวของโลกที่มนุษย์กับแม่มดอยู่ร่วมกันมานานกว่าหลายร้อยปี แต่จากสุดยอดการปฏิวัติทางอุตสาหกรรมที่ชื่อว่า “Gear Expansion” ทำให้มนุษย์ไม่จำเป็นต้องพึ่งเวทมนตร์อีกต่อไป

หลังจากนั้นจักรพรรดิ Goethe แห่งอาณาจักร Redia ก็ได้ทำการล่าแม่มดและต้องการจัดการให้หมดไปจากโลก “Adonis” เด็กหนุ่มที่ถูกคุมขังและถูกช่วยโดย “Doroka” จากการที่แม่บุญธรรมของเขาถูกฆ่าตายไปต่อหน้าเมื่อยังเด็ก ทำให้เขาเริ่มคิดที่จะล้างแค้น…""")
    elif mes == "Dead Mount Death Play":
        await message.channel.send("""บอกเล่าเรื่องราวบนโลกแฟนตาซีที่กำลังเกิดการต่อสู้ระหว่างเนโครแมนเซอร์ผู้มีพลังในการใช้วิญญาณและความตายขั้นสูงกับนักรบผู้กล้าหาญจากโบสถ์เพื่อชี้วัดโชคชะตาของโลกใบนี้

แล้วในช่วงสุดท้ายของการต่อสู้ก็เกิดแสงสว่างวาบขึ้นมา และเมื่อแสงจางไปก็พบว่าพลังวิญญาณของเนโครแมนเซอร์ได้หายไปจากโลกใบนี้ แสดงว่าชัยชนะได้ตกเป็นของนักรบแล้ว""")
    elif mes == "Seiken Gakuin no Makentsukai":
        await message.channel.send("""ตัวเนื้อเรื่องจะกล่าวถึง “เลโอนิส” จอมมารสุดแกร่งที่ผนึกตัวเอกเพื่อเตรียมรบในภายภาคหน้า ทว่า 1,000 ปีให้หลัง เขากลับตื่นขึ้นมาในร่างของเด็กวัย 10 ขวบ!? ทั้งยังจับผลัดจับผลูได้เข้าไปเรียนที่ “วิทยาลัยดาบศักดิ์สิทธิ์” และได้รับความช่วยเหลือจากบรรดา “พี่สาว”

นี่คือเรื่องราวของจอมมารวัย 10 ขวบที่ต้องเผชิญกับโลกที่เปลี่ยนแปลงไป พร้อมรับมือกับศัตรูปริศนาที่โผล่ออกมาอย่าง “วอยด์” !""")
    elif mes == "Jujutsu Kaisen":
        await message.channel.send("""บอกเล่าเรื่องราวของเด็กหนุ่มที่จับผลัดจับผลูไปเกี่ยวพันกับคำสาปจนกลายเป็นภาชนะของราชาแห่งคำสาป และถูกดึงเข้าไปในโลกของผู้ใช้ไสยเวท""")
    elif mes == "Mashle: Magic and Muscles":
        await message.channel.send("""บอกเล่าเรื่องราวของโลกที่ผู้คนต่างใช้เวทมนตร์เป็นเรื่องปกติและสถานภาพสังคมจะถูกกำหนดโดยความสามารถของพวกเขา ซึ่ง Mash Burnedead ตัวเอกของเรื่องกลับเป็นคนที่ใช้เวทมนตร์ไม่ได้ เขาเลยต้องฟิตร่างกายตัวเองเพื่อให้ใช้ชีวิตอยู่บนโลกอันแฟนตาซีใบนี้ได้ แน่นอนว่าร่างกายที่เขาฟิตมามันไม่เปล่าประโยชน์ในโลกที่ใช้แต่เวทมนตร์หรอกนะ!

ขอบอกเลยว่าเป็นอนิเมะเวทมนตร์ที่ฮาน้ำตาเล็ดจริง ๆ """)
    elif mes == "Tensei Kenja no Isekai Life":
        await message.channel.send("""บอกเล่าเรื่องราวของ ซาโนะ ยูจิ ที่ทำงานให้กับบริษัทสุดโหดในญี่ปุ่นยุคปัจจุบันได้ถูกอัญเชิญมายังต่างโลกที่มีสเตตัสและสกิล เขาได้กลายเป็น “เทมเมอร์” อาชีพที่ไม่ถูกยอมรับ และได้เทม “สไลม์” มอนสเตอร์อ่อนแอที่สุด แต่เพราะหนังสือเวทลึกลับทำให้เขากลายเป็น “นักปราชญ์”

และเมื่อนำสกิลของสไลม์มารวมกับเวทมนตร์แล้ว ก็ได้รู้ถึงอานุภาพของอาชีพระดับสุดยอด! เรื่องนี้พระเอกคือเทพแบบหน้าตายมากขอบอก และสไลม์แต่ละตัวก็ช่างน่าเอ็นดูเสียเหลือเกิน!?""")
    elif mes == "Overlord":
        await message.channel.send("""บอกเล่าเรื่องราวเกี่ยวกับเกมแนว DMMORPG (Dive Massively Multiplayer Online Role Playing Game) ที่ชื่อว่า Yggdrasil ซึ่งกำลังจะปิดให้บริการ แต่ว่าพระเอกนั้นที่รู้สึกอาลัยอาวรณ์จึงอยู่รั้งท้ายภายในกิลด์ที่สร้างขึ้นมาร่วมกับมิตรสหายภาพในเกมจนเผลอหลับไปเลยระยะเวลาที่เซิร์ฟเวอร์เกมปิดตัว

ทว่าเมื่อเขาลืมตาขึ้นกลับพบว่าตัวเองได้อยู่ในร่างอวาตาร์ในดินแดนที่ไม่รู้จัก พร้อมสุสานนาซาริคที่เป็นกิลด์ของเขาในเกม รวมทั้งเหล่าเอ็นพีซีที่เป็นผู้พิทักษ์ของกิลด์ทั้งหมดนั้นก็ได้มาอยู่กับเขาเช่นกัน ทำให้เขาต้องออกสำรวจโลกแห่งนี้เสียใหม่ และตามหาสาเหตุต้นตอของเรื่องราวทั้งหมดนี้!""")
    elif mes == "Black Clover":
        await message.channel.send("""บอกเล่าเรื่องราวในโลกเวทมนตร์ของเด็กหนุ่มผู้อาศัยอยู่ในหมู่บ้านชนบท 2 คน นามว่า ยูโน และ แอสตร้า โดยทั้งสองคนใฝฝันที่อยากจะเป็น “จักรพรรดิเวทมนต์”

ยูโนผู้มีพลังเวทย์เหลือล้น และได้รับกริมมัวร์(สมุดเวทย์)สี่แฉก ที่จักรพรรดิเวทมนต์คนก่อนเคยได้ใช้เหมือนกัน ส่วนแอสตร้าเป็นเด็กหนุ่มที่มีพลังกายสุดโต่ง แต่ได้รับกริมมัวร์(สมุดเวทย์)เก่า ๆ แต่มีห้าแฉก

เส้นทางชีวิตขอทั้งสองคนจะนำพาให้ไปพบกับอะไรบ้าง และใครจะได้เป็นจักรพรรดิเวทมนต์""")
    elif mes == "Youjo Senki":
        await message.channel.send("""บอกเล่าเรื่องราวของพนักงานชายชาวญี่ปุ่นผู้ยึดมั่นในหลักการและเหตุผลแบบสุดโต่ง ทั้งยังไม่มีความเชื่อถือในพระเจ้า ที่ตายเพราะถูกผลักให้ตกรางรถไฟจนเสียชีวิต ซึ่งในตอนนั้นเองเขาก็ได้พบกับตัวตนที่เรียกตัวเองว่าพระเจ้าผู้สร้าง และถูกลงโทษให้ไปเกิดใหม่ยังโลกอื่น แล้วกลายเป็นเด็กผู้หญิงนามว่า “Tanya von Degurechaff”

โลกที่เขาได้มาเกิดนั้นเป็นโลกที่มีเวทมนตร์และกำลังจะเข้าสู่ยุคสงครามที่ดูคล้ายกับสงครามโลกครั้งที่สอง เขาจึงได้ใช้ความรู้ที่มีวิเคราะห์สภาพของประเทศแล้วตัดสินใจไปเป็นทหารเพื่อที่จะได้ใช้ชีวิตอย่างสุขสบายในแนวหลัง แต่แผนนี้ก็ต้องพังทลายเมื่อเขาถูกส่งไปรบที่แนวหน้า!

นี่เป็นอนิเมะอีกหนึ่งเรื่องที่ห้ามพลาดเลยทีเดียว ทั้งเนื้อเรื่องที่มีเซ็ตติ้งของโลกที่กำลังเกิดสงคราม ความคิดปรปักษ์ ไหนจะการต่อสู้อันดุเดือดที่ใช้พลังเวทผสานกับเทคโนโลยีทางการทหาร บอกเลยว่าอย่างเดือด!?""")
    elif mes == "การ์กันเทียจักรกลทะลุมิติ":
        await message.channel.send("""อนาคตอันไกลโพ้นที่มนุษย์เริ่มเดินทางไปถึงขอบเขตของกาแล็คซี่ กลุ่ม Human Galactic Alliance ได้ต่อสู้กับพวกเผ่าพันธุ์ประหลาดที่เรียกว่า “Hidiaasu” อย่างต่อเนื่องเพื่อเอาชีวิตรอด ระหว่างการรบครั้งใหญ่ พลทหารหนุ่ม Redo และหุ่นของเขา Chamber ได้ถูกดูดไปในการบิดเบี้ยวของมิติและกาลเวลาไปยังดาวเคราะห์ที่ปกคลุมไปด้วยน้ำ และเรือขนาดยักษ์ Redo มาถึงกองเรือที่เรียกว่า Gargantia เขาไม่รู้ทั้งประวัติศาสตร์ของดาวเคราะห์ดวงนี้หรือวัฒนธรรม จึงต้องอยู่กับเด็กสาวที่ชื่อ Amy ผู้ส่งสารในท่าเรือแห่งนี้ สำหรับตัว Redo เขารู้จักแต่การสู้รบมาทั้งชีวิต การที่ต้องมาอยู่ในโลกที่สงบสุขทำให้เขาประหลาดใจอยู่ไม่น้อยเช่นกัน""")
    elif mes == "ซาซากิกับพีจัง":
        await message.channel.send("""นกกระจอกที่ซื้อมาจากร้านขายสัตว์เลี้ยงที่แท้คือท่านปราชญ์ผู้โด่งดังที่กลับชาติมาเกิดใหม่จากต่างโลก "ซาซากิ" ได้รับโอกาสข้ามโลก และ พลังเวทมนตร์ทรงอานุภาพ เขาจึงเริ่มทำธุรกิจด้วยการขนสินค้าจากโลกปัจจุบันไปขายยังอีกโลก เทียวไปเทียวมา-เก็บเงิน ฝึกฝนเวทมนตร์ และกินของอร่อย-ตั้งใจจะใช้ชีวิตสโลว์ไลฟ์โดยไร้ข้อผูกมัด แต่แล้ววันหนึ่งเผอิญปะเข้ากับผู้มีพลังพิเศษเข้าระหว่างทางกลับจากบริษัท พออาศัยเวทมนตร์ยี่ห้อนักปราชญ์ฟันฝ่าไปได้ คราวนี้ความสามารถก็ดันไปเตะตากรมควบคุมปรากฏการณ์เหนือธรรมชาติสำนักนายกรัฐมนตรีแทน จนโดนอีกฝ่ายชักชวนเข้าทำงาน และแล้วเขาก็มีอันได้เปลี่ยนงานไปเป็นเจ้าหน้าที่รัฐอย่างเต็มภาคภูมิ""")
    elif mes == "อสูรร้ายจอมราชัน":
        await message.channel.send("""สี่ร้อยปีหลังจากที่อารยธรรมยุคใหม่ล่มสลาย โลกพบแต่ความโกลาหลท่ามกลางเพลงดาบและเวทมนตร์ กองกำลังกบฏฝ่ายมืดซึ่งวางแผนฟื้นคืนชีพเทพเจ้าแห่งการทำลายล้างที่ชื่อว่าแอนทราแซ็กซ์ ยังคงแผ่ขยายอำนาจเพื่อยึดครองโลก โดยมีเทวราชาทั้งสี่ผู้มีพลังแก่กล้าเป็นผู้นำ อาณาจักรเมทัลลิกานาในทวีปเมทัลเลียนกลางถูกโจมตีจากกองกำลังกบฏฝ่ายมืดที่คุมทัพโดยจอมเวท เพื่อที่จะปกป้องอาณาจักรเอาไว้ เทีย โนโตะ โยโกะ ลูกสาวของมหาปุโรหิตจึงต้องทำการตัดสินใจ เธอจะต้องปลุกชีพพ่อมดผู้ยิ่งใหญ่ในยุคโบราณซึ่งเคยวางแผนที่จะครองโลก และถูกสะกดไว้ในร่างของเพื่อนสมัยเด็กของเธอที่ชื่อลูเชียน เรนเรน สิ่งเดียวที่จะคลายมนตร์สะกดนั้นได้ก็คือจุมพิตแรกของสาวพรหมจรรย์ เมื่อต้องเผชิญกับอันตรายที่คืบคลานเข้ามา เทียจึงประกบริมฝีปากกับลูเชียน และทันใดนั้นเอง พลังงานมืดอันแรงกล้าก็แผ่ปกคลุมไปทั่ว และแล้วตัวละครเอกสุดแกร่ง สุดร้ายกาจและสุดหล่ออย่างดาร์ก ชไนเดอร์ พ่อมดในตำนานก็ฟื้นคืนชีพในที่สุด""")
    elif mes == "ศึกตำนาน7อัศวินกาลวิบัติ4อัศวิน":
        await message.channel.send("""คําทํานายถูกประกาศแล้ว ในอนาคตอันใกล้จะมีอัศวิน 4 คนปรากฏตัวขึ้นเพื่อทําลายโลก ชื่อของพวกเขาคือ จตุรอาชาแห่งวิบัติ ผู้ที่ตื่นเต้นกับการที่จะได้เด็ดหน่อแห่งภัยพิบัตินั้นก็คือเหล่าอัศวินที่สาบานว่าจะภักดีต่อกษัตริย์อาเธอร์ เรื่องนั้นส่งผลกระทบไปถึงชายแดนที่ห่างไกล และสั่นคลอนชะตากรรมของเด็กหนุ่มคนหนึ่ง! เด็กหนุ่มผู้ก้าวเดินออกไปตามที่หัวใจของตัวเองสั่ง สิ่งที่รอเขาอยู่ข้างหน้าคือความฝัน ความหวัง เกียรติยศ หรือบาป เรื่องราววีรบุรุษผู้ไร้เทียมทานในอดีตสุดแฟนตาซีได้เปิดม่านขึ้นแล้ว!!""")
    elif mes == "SoloLeveling":
        await message.channel.send("""10 ปีก่อน "เกต" ทางที่เชื่อมระหว่างโลกมนุษย์กับอีกมิติหนึ่งได้ถูกเปิดออก อีกฝั่งหนึ่งของเกต คือดันเจี้ยนที่เหล่ามอนสเตอร์อาศัยอยู่ มนุษย์ที่ถูกขนานนามว่า "ฮันเตอร์" จึงได้ถูกปลุกพลังพิเศษขึ้นเพื่อออกพิชิตดันเจี้ยนภายในเกต ในบรรดาฮันเตอร์ผู้แข็งแกร่งนั้น มี "ซองจินอู" ตัวเอกของเรื่อง ผู้ที่มีแรงก์อันดับต่ำสุด และได้รับฉายาว่า "อาวุธสุดกากของมวลมนุษยชาติ" รวมอยู่ด้วย...และในช่วงวินาทีที่เขาบาดเจ็บสาหัสใกล้ตาย ก็ได้มีหน้าจอเควสปรากฏขึ้นและพบว่า มีเพียงเขาคนเดียวที่สามารถ "เลเวลอัป" ได้""")
    elif mes == "การผจญภัยของเทมเมอร์มือใหม่กับสไลม์สุดด๋อย":
        await message.channel.send("""ในโลกแฟนตาซีที่มนุษย์เกิดมาพร้อมดาวประจำตัว ไอวี่ เด็กสาวที่มีความทรงจำจากชาติก่อนบางส่วน พบว่าตนทั้งเป็นเทมเมอร์ไร้ดาวและไร้สกิลต่างจากคนทั่วไป ด้วยความประหลาดทำให้ถูกรังเกียจทั้งครอบครัวและคนในหมู่บ้าน จนวันหนึ่งเธอถูกตามฆ่าและต้องหนีจากหมู่บ้าน ออกผจญภัยตามลำพังจนได้พบกับสไลม์ตัวน้อยตั้งชื่อมันว่า โซระ การผจญภัยของสาวน้อยเทมเมอร์ที่ไร้พลัง ในโลกที่อันตรายได้เริ่มขึ้น""")
    elif mes == "เกิดใหม่ต่างโลกฉันได้สกิลสุดยอดทำให้สัตว์รัก":
        await message.channel.send("""อะกิสึ มิโดริ อายุ 27 ปี จบลงในอีกโลกหนึ่งหลังจากเสียชีวิตจากการทำงานหนักเกินไป ฉันกลับชาติมาเกิดในอีกโลกหนึ่งหลังจากที่พระเจ้าอวยพรฉันด้วยความสามารถพิเศษ ความสามารถนี้คือ ได้รับความรักจากสิ่งที่ไม่ใช่มนุษย์ ฮะ!? แปลว่ามนุษย์อาจจะไม่ชอบฉัน แต่สัตว์ขนปุยจะรักฉันหมดเลยเหรอ อ้าว ฉันจะได้เลี้ยงเสือขาวและมังกรให้สุดหัวใจ หลังจากที่ได้เกิดใหม่เป็น เนะมะ ลูกสาวคนเล็กของตระกูลขุนนางชั้นสูง ฉันก็พยายามอย่างเต็มที่เพื่อความอยู่รอดของมนุษยชาติ ในขณะที่เพลิดเพลินกับความนุ่มฟูของโลกนี้""")
    elif mes == "จันทรานำพาสู่ต่างโลก":
        await message.channel.send("""เด็กหนุ่มมัธยมปลาย มิสุมิ มาโคโตะ ถูกอัญเชิญมายังต่างโลกด้วยเหตุผลทางครอบครัว ในตอนแรกเขาก็จะต้องสู้กับเหล่าสัตว์อสูรในฐานะผู้กล้า ทว่าเทพธิดาของโลกที่เป็นผู้อัญเชิญเขามานั้นตีตราว่าเขา “อัปลักษณ์” แล้วก็ถูกถอนสถานะความเป็นผู้กล้าแล้วก็ยังอัปเปหิไปยังสุดขอบโลกอีกด้วย มาโคโตะที่ถูกริดรอนคุณสมบัติของผู้กล้านั้น เขาต้องออกเร่ร่อนไปยังที่รกร้าง และที่นั่นก็ทำให้เขาได้พบกับวงศ์วานมังกรระดับสูงอย่างโคโนเอะ รวมไปถึงแมงมุมดำระดับภัยพิบัติอย่างมิโอะ เลยทำให้การผจญภัยเพื่อกอบกู้โลกได้เริ่มต้นขึ้น ระหว่างทางเขาก็พบเจอกับการพานพบและการพลัดพรากอย่างมากมาย ปราบปรามเหล่าร้ายที่มีอยู่อย่างมหาศาลในดินแดนต่างโลก มิหนำซ้ำยังต้องมาพัวพันกับสงครามของปีศาจที่มาจากอารมณ์นึกครึ้มของเทพธิดาอีกด้วย โดยที่เป้าหมายการเดินทางของพวกเขานั้นคือมุ่งหน้าไปยังนครหลวงแห่งการศึกษาร็อตซ์การ์ด แล้วก็การไปหาผู้กล้า 2 คนที่ยังไม่เคยเจอหน้ากันมาก่อนนั่นเอง!""")
    elif mes == "ผมโดนกลุ่มผู้กล้าขับไสเลยต้องไปสโลว์ไลฟ์ที่ชายแดน":
        await message.channel.send("""ในโลกที่มนุษย์เกิดมาพร้อม “พร” ที่แตกต่างกัน ถูกกำหนดสายอาชีพตั้งแต่เกิด เรด อดีตผู้นำที่สร้างทีมสู้กองทัพปีศาจ ทุ่มเทฝึกฝนแม้จะไม่มี พรที่ดีแบบคนอื่น ได้รับการยอมรับในทีม แต่ถูกนักปราชญ์ขอให้ออกจากกลุ่ม ด้วยเหตุผลที่เขามี พร ที่ไร้ประโยชน์สำหรับทีม ต่างจาก ลูตี้ น้องสาวเขาที่มีพลังของผู้กล้า เรด จึงไปเริ่มชีวิตอย่างสงบในชายแดนที่ห่างไกล ได้เปิดร้านขายยาและใช้ชีวิตสบายๆ ที่นั่น อย่างไรก็ตาม กลุ่มผู้กล้าเริ่มเกิดความแตกแยกและพบความลำบาก ทำให้มีปัญหาหลายอย่างตามมา""")
    elif mes == "เส้นทางพลิกผันของราชันอมตะ":
        await message.channel.send("""ฉันจะจะต้องเป็นมิธริลให้ได้ เลนท์ นักผจญภัยผู้มีความตั้งมั่นเช่นนั้นในหัวใจ เมื่อเวลาผ่านไป 10 ปี เลนท์ก็ไปขัดเกลาทักษะดาบของเขา ศึกษาหาความรู้ ทั้งยังคอยทำงานให้กับกิลด์นักผจญภัยอย่างมากมาย แต่ถึงกระนั้นก็ยังอยู่ที่อันดับทองแดงที่เป็นระดับต่ำอยู่ดี แต่แม้จะเป็นเช่นนั้น เขาก็ยังคงดำดิ่งสู่เขาวงกตทุกวัน พากเพียรพยายามอย่างไม่หยุดหย่อน ทว่าวันหนึ่งเขาก็พบกับเขตแดนที่ยังไม่เคยมีใครค้นพบที่ชั้นล่างของเขาวงกตอย่าง “เขาวงกตจันทราวารี” เข้า ซึ่งที่นั่นก็ทำให้เขาถูก “มังกร” ที่บังเอิญพบเจอกินเข้าไป""")
    elif mes == "เมื่อสาววายกลายเป็นสาวฮอต":
        await message.channel.send("""สาวมัธยมปลายปีที่ 2 ที่หน้าตาไม่ได้สวยเเถมรูปร่างยังอ้วน เเต่เธอมีสายเลือดสาววายเต็มตัวชอบจับจิ้นหนุ่มหล่ออยู่เสมอ เพราะมันคือความสุขของสาววายนั้นเอง เเต่เเล้ววันหนึ่งเธอได้ดูซีรี่ย์เเล้วตัวละครที่เธอชอบนั้นตาย ทำให้เธอเสียใจอย่างมากเเบบเหมือนเขาตายจริง ๆ เธอจึงไม่ยอมออกมาจากห้องไม่กินอาหารเป็นสัปดาห์จนทำให้เธอน้ำหนักลดลงเยอะมากทำให้กลายเป็นสาวสวยที่มีเเต่หนุ่ม ๆ เข้าตีสนิท จากสาววายต้องกลายเป็นคนที่ถูกสนใจ""")
    elif mes == "มาชิโระเทพธิดาหูหมา":
        await message.channel.send("""มิโตะ ยูริ อาจดูเหมือนเป็นผู้ชื่นชอบมอเตอร์ไซค์ทั่วไปของคุณ แต่เขามีคุณสมบัติเฉพาะตัวที่ทำให้เขาแตกต่างจากคนอื่นๆ ในฐานะผู้สืบทอดศาลเจ้าในเมือง เขาแทบไม่สนใจที่จะเป็นนักธุรกิจในสถานที่ศักดิ์สิทธิ์เช่นนี้ อย่างไรก็ตาม โชคชะตาเข้าขัดขวางและนำเขามาเผชิญหน้ากับ "คิคุรามิฮิเมะ" เทพธิดาผู้รับผิดชอบในการปิดผนึกเทพเจ้าองค์อื่น ๆ ออกจากโลก น่าเสียดายที่ผนึกอ่อนแอลง และ Taiyu Tai โดยเฉพาะ "Sankyo" ผู้โหดเหี้ยมก็ได้หลบหนีออกมา ทำให้เกิดความวุ่นวาย ตอนนี้ยูริต้องทำงานร่วมกับอวตารของคิคุรามิฮิเมะ "มาชิโระ" เพื่อควบคุมสถานการณ์และเผชิญหน้ากับคู่แข่งเก่าของเขาจากอดีตของคิกุรามิฮิเมะ""")
    elif mes == "ทาสสุดแกร่งแห่งหน่วยป้องกันอสูร":
        await message.channel.send("""อยู่มาวันหนึ่งประตูปริศนาก็ปรากฏออกมาทั่วญี่ปุ่น โดยที่ปลายทางของประตูนั้นมี “เมืองอสูร” ที่มีลูกท้อพิเศษที่เมื่อผู้หญิงรับประทานเข้าไปจะได้พลังพิเศษมาครอบครอง จนทำให้ก่อกำเนิดเป็น “หน่วยป้องกันอสูร” จากเหล่านักรบหญิงที่มีเป้าหมายในการขับไล่เหล่าอสูรที่โผล่มาจากช่องว่างต่างมิตินั่นเอง พระเอกของเรื่อง วาคุระ ยูกิ เด็กหนุ่มมัธยมปลายที่หวังจะสร้างผลงานขึ้นมาให้ได้นั้น อยู่มาวันหนึ่งเขาได้พลัดหลงเข้าไปในเมืองอสูรเข้าแล้วก็พบกับอสูรที่เข้ามาจู่โจม และในตอนนั้นเองเขาก็ได้พบกับหัวหน้าหน่วยป้องกันอสูรที่ 7 ที่เป็นสาวน้อยสุดสวยอย่างอุเซน เคียวกะ ช่วยเหลือเอาไว้ ซึ่งเคียวกะก็ใช้พลังของเธอในการทำให้ยูกิกลายเป็นทาสเข้า จนประสบความสำเร็จในการปราบอสูร และนั่นก็ทำให้ยูกิต้องรับหน้าที่ในฐานะทาสและผู้ดูแลหน่วยป้องกันอสูรที่ 7 ไปด้วยนั่นเอง เรื่องราวต่อสู้สุดแฟนตาซีของเด็กหนุ่มที่กลายเป็นทาสได้เริ่มต้นขึ้นแล้ว!""")
    elif mes == "ตำนานผู้กล้าแห่งแหวน":
        await message.channel.send("""ซาโต้ หนุ่มมัธยมปลาย ได้ทราบว่าเพื่อนสนิทวัยเด็ก ฮิเมะ ต้องอำลาเขาไปแต่งงาน ซาโต้ตามเธอไปจนถึงในโลกแฟนตาซีและตั้งใจขัดขวางงานแต่ง แต่สถานการณ์กลับพลิกผัน ทำให้ซาโต้ได้แต่งงานกับฮิเมะแทน แล้วยังต้องแบกรับตำแหน่ง “ผู้กล้าแห่งแหวน” ต้องปกป้องโลกใบนี้ตามคำทำนาย""")
    elif mes == "ทาสสุดแกร่งแห่งหน่วยป้องกันอสูร ":
        await message.channel.send("""อยู่มาวันหนึ่งประตูปริศนาก็ปรากฏออกมาทั่วญี่ปุ่น โดยที่ปลายทางของประตูนั้นมี “เมืองอสูร” ที่มีลูกท้อพิเศษที่เมื่อผู้หญิงรับประทานเข้าไปจะได้พลังพิเศษมาครอบครอง จนทำให้ก่อกำเนิดเป็น “หน่วยป้องกันอสูร” จากเหล่านักรบหญิงที่มีเป้าหมายในการขับไล่เหล่าอสูรที่โผล่มาจากช่องว่างต่างมิตินั่นเอง พระเอกของเรื่อง วาคุระ ยูกิ เด็กหนุ่มมัธยมปลายที่หวังจะสร้างผลงานขึ้นมาให้ได้นั้น อยู่มาวันหนึ่งเขาได้พลัดหลงเข้าไปในเมืองอสูรเข้าแล้วก็พบกับอสูรที่เข้ามาจู่โจม และในตอนนั้นเองเขาก็ได้พบกับหัวหน้าหน่วยป้องกันอสูรที่ 7 ที่เป็นสาวน้อยสุดสวยอย่างอุเซน เคียวกะ ช่วยเหลือเอาไว้ ซึ่งเคียวกะก็ใช้พลังของเธอในการทำให้ยูกิกลายเป็นทาสเข้า จนประสบความสำเร็จในการปราบอสูร และนั่นก็ทำให้ยูกิต้องรับหน้าที่ในฐานะทาสและผู้ดูแลหน่วยป้องกันอสูรที่ 7 ไปด้วยนั่นเอง เรื่องราวต่อสู้สุดแฟนตาซีของเด็กหนุ่มที่กลายเป็นทาสได้เริ่มต้นขึ้นแล้ว!""")
    elif mes == "รักรักรักรักรักเธอหมดหัวใจจากแฟนสาว100คน":
        await message.channel.send("""ไอโจ เรนทาโร่ หนุ่มม.ต้นผู้อกหักถึงครั้งที่ 100 ไปขอพรที่ศาลเจ้าว่าขอให้มีแฟนตอนม.ปลายกับเขาสักที เทพเจ้าแห่งความรักจึงปรากฏตัวขึ้นบอกแก่เขาว่า "เนื้อคู่ที่เจ้าจะได้พบตอนม.ปลายนั้นมีอยู่ 100 คน" แต่เทพเจ้ายังได้บอกกับเขาอีกว่า มนุษย์ที่ได้เจอกับเนื้อคู่นั้นจะต้องรักกับคู่ของตนและทำให้เขามีความสุข มิเช่นนั้นจะต้องตาย แล้วเรนทาโร่จะทำอย่างไรกับแฟนสาว 100 คนซึ่งเป็นเนื้อคู่ที่รออยู่ข้างหน้ากันดีเล่า""")
    elif mes == "จะคนไหนก็แฟนสาว":
        await message.channel.send("""นาโอยะเป็นนักเรียนมัธยมปลายชั้นปีที่หนึ่ง เขาได้สารภาพรักกับซากิที่เขาชอบมาตลอด และได้เป็นแฟนกันในที่สุด เรียกได้ว่าอยู่ ณ จุดสุดยอดของการมีความสุข ทว่านางิสะ สาวงามอีกคนก็ได้เข้าไปคุยกับนาโอยะ อยู่ดีๆ เธอก็สารภาพรักกับนาโอยะและบอกว่าอยากให้มาคบกับตัวเอง นาโอยะที่หวั่นไหวเพราะความเป็นคนดีเกินไปของนางิสะ จึงได้ทำการตัดสินใจอย่างหนึ่ง!""")
    elif mes == "ไวท์อัลบั้ม":
        await message.channel.send("""เรื่องราวความรักของ ฟูจิอิ โทยะ หนุ่มนักศึกษามหาวิทยาลัยธรรมดาๆ กับไอดอลสาวชื่อดัง โมริคาวะ ยูกิ ที่เป็นเพื่อนสมัยเรียนด้วยกันมาก่อน และด้วยความดังของเธอนี่เอง ทำให้เขากับเธอต้องห่างกันออกไปทุกทีๆ ไม่ว่าจะด้วยเรื่องงาน เรื่องสถานะ ที่ทำให้โทยะกับยูกิต้องโดนกีดกันโดยหลายๆ คน เมื่อห่างกันแล้วยังไม่พอ เมื่อไอดอลสาวชื่อดังอีกคนอย่าง โอกาตะ รินะ ซึ่งอยู่ค่ายเดียวกันกับยูกิ ดันมาหลงรักพ่อพระเอกของเราไปอีกคน โทยะจึงจำเป็นที่จะต้องเลือก ระหว่างเพื่อนสมัยเรียนอย่างยูกิ กับไอดอลชื่อดังอย่างรินะ""")
    elif mes == "จอมมารเกิดใหม่ วิทยาลัยผู้พิทักษ์":
        await message.channel.send("""ลีโอนิส อดีตผู้กล้าที่กลายมาเป็นจอมมาร ใช้เวทมนตร์เพื่อจะถือกำเนิดอีกครั้งในหนึ่งพันปีเพื่อถือกำเนิดเป็นจอมมารโดยสมบูรณ์ แต่เกิดความผิดพลาด ตัวเขากลับตื่นขึ้นมาในร่าง 10 ขวบของผู้กล้าแทน ถูกพบโดย ลิเซเลีย นักเรียนหญิงที่มาดูแลเขาเหมือนพี่สาว แล้วยังพาเขาไปโรงเรียนดาบศักดิ์สิทธิ์ และกลายเป็นที่สนใจของพวกรุ่นพี่สาว""")
    elif mes == "ห้องเรียนจารชน":
        await message.channel.send("""อาเน็ต เอร์นา เทีย มอนิกาได้เจอกับอีกหนึ่ง “ภารกิจลับ” ที่ใกล้เข้ามาหลังจากภารกิจมานามุสุเมะ

ในโลกที่หลายประเทศก่อสงครามในเงามืดผ่านกลุ่มสายลับ เคลาส์ สุดยอดสายลับที่ปฏิบัติภารกิจสำเร็จทุกครั้ง แต่มีปัญหาด้านนิสัยส่วนตัว เขาได้จัดตั้งทีมเชี่ยวชาญพิเศษในชื่อ โทโมชิบิ เพื่อปฏิบัติภารกิจสุดโหดที่มีโอกาสเสียชีวิตเกิน 90% ซึ่งสมาชิกทีมที่เขาเลือกมากลับเป็นเด็กสาวไร้ประสบการณ์ 7 คน ให้มาฝึกกับเขาก่อนเริ่มภารกิจ""")
    elif mes == "คู่หูต่างขั้วกับภารกิจกำจัดผี":
        await message.channel.send("""เรื่องราวของ เคทาโร่ชายผู้มีจิตสัมผัสเรื่องผี ๆ ที่สมัยเรียนมัธยมต้นเคยทำให้เพื่อนถูกลูกหลงจากคำสาป จนกลายเป็นปมในใจและเอาแต่เก็บตัวไม่สุงสิงกับใครหรือยุ่งเรื่องผีอีกเลย ซึ่งในตอนนี้เขาก็พยายามกลับเข้าสู่สังคมด้วยการเข้าเรียนมหาลัย และไปเป็นครูสอนพิเศษให้กับ ยาโยอิเด็กประถมผู้มี IQ ระดับอัจฉริยะ แต่เด็กคนนี้กลับมีประสาทความรับรู้เรื่องผีสูงยิ่งกว่า เคทาโร่ซะอีก และเด็กคนนี้ยังชักชวนให้เขาไปช่วยกันจับผีร้ายอีกด้วย""")
    elif mes == "สิ่งที่อยากทำก่อนจะกลายเป็นซอมบี้":
        await message.channel.send("""ชายหนุ่มวัยรุ่นผู้เปี่ยมไปด้วยความฝัน ได้สูญสิ้นจุดมุ่งหมายในชีวิตไปหลังจากที่ได้ทำงาน ในบริษัทที่กดขี่พนักงานเป็นเวลาถึง 3 ปี แถมต้องเหนื่อยกายเหนื่อยใจจนเกือบจะกลายสภาพเป็นซอมบี้ แต่แล้วเช้าวันหนึ่ง...เขาก็ได้พบว่า ทั้งเมืองเต็มไปด้วยซอมบี้ของจริง แม้แต่สาวที่แอบรักในบริษัทก็เป็นซอมบี้ไปด้วยอีกคน ซึ่งทั้งหมดนี้จะกลายเป็นเรื่องราวชีวิตบทใหม่ของเขาที่เกิดขึ้นมาจาก ”ซอมบี้”""")
    elif mes == "Berserk":
        await message.channel.send("""ต้นฉบับเรื่องนี้เป็นมูฟวี่ของปี 2012 ได้เล่าเรื่องของพวกนักดาบจอมทมิฬที่เก่งกาจ""")
    elif mes == "มิเอรุโกะจัง ใครว่าหนูเห็นผี":
        await message.channel.send("""เรื่องราวของสาวน้อยนาม มิโกะผู้ใช้ชีวิตปกติธรรมดา.. ทว่าวันหนึ่งชีวิตของเธอก็เริ่มเปลี่ยนไป เมื่อเธอได้เริ่มมองเห็น “สิ่งผิดปกติ” ที่ไม่มีใครเห็น และถึงแม้ว่าเธอจะหวาดกลัวแค่ไหน สิ่งที่เธอเลือกจะทำก็คือใช้ชีวิตของเธอต่อไปโดยทำเป็นไม่เห็น และไม่สนใจพวกมันพร้อมๆ กับข่มความกลัวของตัวเองไว้ เพื่อให้ตัวเองและเพื่อนของเธอปลอดภัยจากสิ่งที่เธอเห็น! เรื่องราวของเด็กสาวผู้ต้องรับมือกับสิ่งเหนือธรรมชาติพร้อมกับแกล้งทำเป็นไม่เห็นพวกมันก็ได้เริ่มต้นขึ้น!""")
    elif mes == "Tokyo Ghoul: Pinto":
        await message.channel.send("""ภาคนี้จะเป็นเนื้อเรื่องตอนที่นักชิม สึกิยามะ ชู ได้พบกับ โฮริจิเอะ สาวน้อยที่ชอบถ่ายรูปเป็นชีวิตจิตใจซึ่งบทของคนนี้สำคัญมากในภาค :re ไทม์ไลน์จะอยู่ในช่วงไม่กี่ปีก่อนเจอ คาเนกิ""")
    elif mes == "Tokyo Ghoul: Jack":
        await message.channel.send("""เรื่องราวที่เกิดขึ้นก่อนเนื้อหาหลัก เมื่อเหล่า”กูล” ได้คุกคามมายังเขตที่ 13 ของกรุงโตเกียว เพื่อตามหาความจริงที่อยู่เบื้องหลังสิ่งที่เกิดขึ­้นกับเพื่อนของเขา ไทชิ ฟุระ กับ คิโช อาริมะ เจ้าหน้าที่สืบสวนมือหนึ่ง มาร่วมมือกันตามหา Lantern Ghoul ที่ลงมือสังหารเพื่อนรักของฟุระ พร้อมกับค้นหาความจริงที่เกิดขึ้น""")
    elif mes == "แว่วเสียงเรไร":
        await message.channel.send("""เรื่องราวของ Maebara Keiichi ตัวเอกของเรื่องที่ได้เดินทางมายังหมู่บ้าน Hinamizawa ที่ตั้งอยู่ในส่วนลึกของภูเขา และได้พบกับคดีการตายปริศนาต่อเนื่องในช่วงงานเทศกาล Watanagashi ที่มีการจัดขึ้นทุก ๆ เดือนมิถุนายนของทุกปี""")
    elif mes == "ภารกิจล้างพันธุ์นรก":
        await message.channel.send("""ภาคต่อของ “Terra Formars” มนุษย์ได้ส่งแมลงสาบไปยังดาวอังคารเพื่อปรับสภาพดาวให้มนุษย์อาศัยอยู่ได้ แต่เมื่อถึงเวลาที่มนุษย์เดินทางไปยังดาวอังคาร กลับพบว่าแมลงสาปเหล่านั้นได้กลายเป็นสิ่งมีชีวิตที่แข็งแกร่ง และฆ่ามนุษย์ที่เดินทางมาที่นี่ทันที จนต้องมีการส่งนักรบที่ถูกพัฒนาจนแข็งแกร่งให้มาต่อสู้กับแมลงสาบเหล่านี้ !!!""")
    elif mes == "จอมใจคมดาบทมิฬ":
        await message.channel.send("""เรื่องราวความรักที่ครอบงำจิตใจ และ การตามล่าล่า ที่ถูกเล่าขานมากว่า 1000 ปี โยชิซึเนะ กับสหายคู่ใจ ได้หลบหนีจากการตามล่าของน้องชายผู้ซึ่งครอบครองอำนาจราชบัลลังก์ ทำให้ทั้งสองได้เข้าไปในบ้านกลางหุบเขาลึกลับอันน่าพิศวง ซึ่งมีสตรีเพียงนางเดียวที่อาศัยอยู่ในบ้านหลังนั้น และดูเหมือนว่าในบ้านหลังนั้นกลับมืดและหดหู่อย่างผิดปกติ ซึ่งเมื่อได้พบกับหญิงสาวนามว่า คุโรมิซึ การพบกันครั้งนี้ก่อเกิดเป็นสายสัมพันธ์รักข้ามภพข้ามชาติ ซึ่งความเป็นอมตะของทั้งสองไว้ชั่วนิรันด์ เมื่อวันเวลาผ่านไปหลายร้อยปี คุโรที่ได้ตื่นขึ้นมาในสถานที่ซึ่งตัวเค้าเองกลับจำอะไรไม่ได้เลย ทำให้ คุโรต้องค้นหาคำตอบว่าทำไมเค้าถึงไม่ตายและตัวเองเป็นใครกันแน่""")
    elif mes == "บลัดซี":
        await message.channel.send("""ซายะเป็นมิโกะลูกสาวของผู้ดูแลศาจเจ้าเก่าแก่ที่ตั้งอยู่ริมทะเลสาบที่งดงามและเงียบสงบ เธออาศัยอยู่กับพ่อเพียงสองคน ศึกษาในชั้นมัธยมปลายปกติเหมือนนักเรียนโดยทั่วไป มีเพื่อนสนิทมากมาย ร่วมถึงผู้ชายที่มาเกี่ยวข้องด้วยล้วนมาในฐานะที่แตกต่างกันออกไป แต่ในยามราตรีเธอกลับต้องถือดาบญี่ปุ่นต่อสู้กับเหล่าปีศาจที่หมาย จะทำร้ายผู้คนที่เธอรักเธอต้องปกป้องคนเหล่านั้นให้ได้แม้จะยากเย็นและลำบากก็ตาม ร่วมถึงปริศนาต่างๆเกี่ยวข้องกับเธอ...""")
    elif mes == "":
        await message.channel.send("")
    elif mes == "เจมร้อนไหม":
        await message.channel.send("เจมไม่ร้อนครับ")
    elif mes == "ร้อนไหม":
        await message.channel.send("เจมไม่ร้อนครับ")
    elif mes == "เจมแนะนำอนิเมะหน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เจมแนะนำอนิเมะให้หน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เจมแนะนำอนิเมะให้หน่อยได้ไหม":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำอนิเมะให้หน่อยได้ไหม":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เจมแนะนำหนังน่าดูให้หน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนังน่าดูให้หน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนังให้หน่อยได้ไหม":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนังยอดฮิต":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "แนะนำหนังหน่อยเหงาๆไม่มีไรดู":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "เหงาๆไม่มีไรดูแนะนำหนังให้หน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "เหงาไม่มีไรดูแนะนำหนังให้หน่อย":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "เหงาไม่มีอนิเมะดูแนะนำอนิเมะให้ดูหน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำอมิเมะให้ดูหน่อยไม่มีไรทำ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เจมแนะนำอมิเมะให้ดูหน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "เบื่อๆทำไรดีเจม":
        await message.channel.send("""สนใจให้เจมแนะนำหนัง,อนิเมะ,เกมแก้เบื่อให้ท่าน"""+str(message.author.name)+"""ไหมครับถ้าสนใจ
                                   ให้ท่านพิมพ์ตามนี้ครับ
                                   สนใจแนะนำหนังแก้เบื่อ
                                   สนใจแนะนำอนิเมะแก้เบื่อ
                                   สนใจแนะนำเกมแก้เบื่อ
                🙏ขอให้ท่านพิมพ์ตรงตามที่เจมกล่าวไปด้านบนนะครับ🙏
                                   """)
    elif mes == "เบื่อทำไรดี":
        await message.channel.send("""สนใจให้เจมแนะนำหนัง,อนิเมะ,เกมแก้เบื่อให้ท่าน"""+str(message.author.name)+"""ไหมครับถ้าสนใจ
                                   ให้ท่านพิมพ์ตามนี้ครับ
                                   สนใจแนะนำหนังแก้เบื่อ
                                   สนใจแนะนำอนิเมะแก้เบื่อ
                                   สนใจแนะนำเกมแก้เบื่อ
                🙏ขอให้ท่านพิมพ์ตรงตามที่เจมกล่าวไปด้านบนนะครับ🙏
                                   """)
    elif mes == "เจมแนะนำอมิเมะให้ดูหน่อย":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "แนะนำหน่อยเบื่อทำไรดี":
        await message.channel.send("""สนใจให้เจมแนะนำหนัง,อนิเมะ,เกมแก้เบื่อให้ท่าน"""+str(message.author.name)+"""ไหมครับถ้าสนใจ
                                   ให้ท่านพิมพ์ตามนี้ครับ
                                   สนใจแนะนำหนังแก้เบื่อ
                                   สนใจแนะนำอนิเมะแก้เบื่อ
                                   สนใจแนะนำเกมแก้เบื่อ
                🙏ขอให้ท่านพิมพ์ตรงตามที่เจมกล่าวไปด้านบนนะครับ🙏
                                   """)
    elif mes == "เบื่อๆทำไรอะดีเจม":
        await message.channel.send("""สนใจให้เจมแนะนำหนัง,อนิเมะ,เกมแก้เบื่อให้ท่าน"""+str(message.author.name)+"""ไหมครับถ้าสนใจ
                                   ให้ท่านพิมพ์ตามนี้ครับ
                                   สนใจแนะนำหนังแก้เบื่อ
                                   สนใจแนะนำอนิเมะแก้เบื่อ
                                   สนใจแนะนำเกมแก้เบื่อ
                🙏ขอให้ท่านพิมพ์ตรงตามที่เจมกล่าวไปด้านบนนะครับ🙏
                                   """)
    elif mes == "เบื่อทำไรดีเจม":
        await message.channel.send("""สนใจให้เจมแนะนำหนัง,อนิเมะ,เกมแก้เบื่อให้ท่าน"""+str(message.author.name)+"""ไหมครับถ้าสนใจ
                                   ให้ท่านพิมพ์ตามนี้ครับ
                                   สนใจแนะนำหนังแก้เบื่อ
                                   สนใจแนะนำอนิเมะแก้เบื่อ
                                   สนใจแนะนำเกมแก้เบื่อ
                🙏ขอให้ท่านพิมพ์ตรงตามที่เจมกล่าวไปด้านบนนะครับ🙏
                                   """)
    elif mes == "เหงาๆทำไรดี":
        await message.channel.send("คุยกับเจมแก้เหงาได้นะครับ")
    elif mes == "เหงาทำไรดี":
        await message.channel.send("คุยกับเจมแก้เหงาได้นะครับ")
    elif mes == "ช่วยคิดหน่อยวันนี้ทานไรดี":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "ช่วยคิดหน่อยวันนี้กินไรดี":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "ไม่อยากกินเจมอยากกินข้าว":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "อยากกินเจมอะ":
        await message.channel.send("ใจเย็นๆครับคุณ"+str(message.author.name)+"เจมเป็นบอทนะครับ")
    elif mes == "มื้อเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "มื้อกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "มื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจมื้อเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจมื้อกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารมื้อเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารมื้อเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารมื้อเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "มื้อเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจมื้อเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารมื้อกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "อาหารเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจอาหารเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจข้าวเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจข้าวเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจข้าวกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจข้าวเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "สนใจแนะนำหนังแก้เบื่อ":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "สนใจแนะนำอนิเมะแก้เบื่อ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "สนใจแนะนำเกมแก้เบื่อ":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำเพื่อแก้เบื่อให้กับคุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "เกมแก้เบื่อ":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำเพื่อแก้เบื่อให้กับคุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "อนิเมะแก้เบื่อ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "หนังแก่เบื่อ":
        await message.channel.send("")
    elif mes == "สนใจเกมแก้เบื่อ":
        await message.channel.send("""เจมได้เอาจัดอันดับ10เกมน่าเล่นปี2024มาแนะนำเพื่อแก้เบื่อให้กับคุณ"""+str(message.author.name)+"""
                            🎮เรียบร้อยครับ
                                   -Eversoul  
                                   -Honkai: Star Rail  
                                   -Valorant Mobile  
                                   -Rainbow Six Mobile  
                                   -Arena Breakout  
                                   -CarX Street  
                                   -EA Sports FC Mobile  
                                   -Aether Gazer  
                                   -Dawnlands  
                                   -Call of Duty: Warzone Mobile""")
    elif mes == "สนใจอนิเมะแก้เบื่อ":
        await message.channel.send("""อยากได้อนิเมะแนวไหนครับ
                            🧝🏼‍♀️มีให้เลือกตามนี้ครับ🧙🏼
                                   -อนิเมะแนวต่างโลก 
                                   -อนิเมะแนวเวทมนตร์แฟนตาซี
                                   -อนิเมะแนวผจญภัย 
                                   -อนิเมะแนวฮาเร็ม 
                                   -อนิเมะแนวสยองขวัญ
    🙏พิมพ์ให้ตรงตามแนวที่เจมบอกไปนะครับไม่งั้นจะไม่เจมจะตอบไม่ได้🙏""")
    elif mes == "สนใจหนังแก่เบื่อ":
        await message.channel.send("""เอาหนังแบบไหนครับ 
                            🎞เจมมีให้เลือกตามนี้ครับ
                                -หนังผีไทย 
                                -หนังไทย 
                                -หนังผีต่างประเทศ 
                                -หนังต่างประเทศ
    ถ้าต้องการเลือกให้เจมแนะนำหนังแนวไหนให้พิมพ์ที่เจมกล่าวไปดังต้นพิมพ์ให้ถุกต้องด้วยนะครับ""")
    elif mes == "ผีไทย":
        await message.channel.send("""เจมได้หาหนังผีไทยมาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้  
                                   -นางนาก  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -เด็กหอ  
                                   -สี่แพร่ง  
                                   -ลัดดาแลนด์  
                                   -เพื่อนที่ระลึก  
                                   -ห้าแพร่ง  
                                   -โปรแกรมหน้าวิญญาณอาฆาต  
                                   -ธี่หยด
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ผีต่างประเทศ":
        await message.channel.send("""เจมได้หาหนังผีต่างประเทศมาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -The Shining  
                                   -The Conjuring  
                                   -Sinister  
                                   -The Autopsy of Jane Doe  
                                   -Insidious  
                                   -Ghostbusters  
                                   -Aterrados  
                                   -Lights Out  
                                   -His House  
                                   -Mirrors 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ต่างประเทศ":
        await message.channel.send("""เจมได้หาหนังต่างประเทศมาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้
                                   -M3gan
                                   -Babylon
                                   -The Fabelmans
                                   -Knock at the Cabin 
                                   -Tár , Phases of the Moon
                                   -Ant-Man and The Wasp
                                   -Winnie the Pooh 
                                   -Empire of Light
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ไทย":
        await message.channel.send("""เจมได้หาหนังไทยมาให้ท่าน"""+str(message.author.name)+"""
                            🎞เรียบร้อยครับมีดังนี้ 
                                   -ฉลาดเกมส์โกง 
                                   -พี่มากพระโขนง  
                                   -ร่างทรง  
                                   -รักแห่งสยาม  
                                   -ชัตเตอร์กดติดวิญญาณ  
                                   -โหมโรง  
                                   -โฮมสเตย์  
                                   -องค์บาก  
                                   -สิ่งเล็กเล็กที่เรียกว่ารัก  
                                   -แสงกระสือ 
    🙏สามารถพิมพ์ชื่อหนังดังกล่าวเพื่อดูรายละเอียดเพิ่มเติมได้🙏""")
    elif mes == "ข้าวเช้า":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเช้าน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍗เรียบร้อยครับ🌯
                                   -ไข่ยู่ยี่  
                                   -ไข่ข้นแฮม  
                                   -ไข่ระเบิด  
                                   -ต้มจืดไข่น้ำ  
                                   -ข้าวผัดไข่   
                                   -ข้าวผัดอเมริกัน  
                                   -ข้าวผัดกุนเชียง 
                                   -ขนมปังไข่ชีส  
                                   -ไข่เจียวผัก  
                                   -ไข่เจียวออมเล็ต
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "ข้าวเย็น":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเย็นน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                           🍳เรียบร้อยครับ🥓
                                   -ปลากะพงย่างซอสมิโซะ 
                                   -สเต๊กปลาแซลมอนย่างกับข้าวกล้อง 
                                   -สลัดผักปลาย่าง 
                                   -ยำตะไคร้ทูน่า 
                                   -น้ำพริกอ่องไก่สับกับข้าวกล้อง 
                                   -ทอดมันปลาดอรี่กับข้าวกล้อง 
                                   -แซลมอนอบกับสลัดมะม่วงอะโวคาโด 
                                   -เส้นบุกผัดขี้เมากุ้งสด 
                                   -เส้นบุกผัดน้ำสลัดงาซีอิ๊วญี่ปุ่น 
                                   -เส้นบุกผัดเห็ดหูหนูกระเทียมดอง
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "ข้าวอาหารกลางวัน":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "ข้าวเที่ยง":
        await message.channel.send("""เจมได้เอาจัดอันดับ10อาหารเที่ยงน่ากินมาแนะนำให้คุณ"""+str(message.author.name)+"""
                            🍛เรียบร้อยครับ🥙
                                   -ผัดกะเพรา  
                                   -ข้าวผัดกุ้ง 
                                   -สุกี้ 
                                   -ผัดพริกแกง  
                                   -ผัดกระเทียมพริกไทย  
                                   -ข้าวขาหมู  
                                   -ข้าวมันไก่  
                                   -คะน้าหมูกรอบ  
                                   -มาม่าผัดใส่เนื้อสัตว์  
                                   -ผัดเผ็ดปลาดุกราดข้าว
        🙏อยากรู้ส่วนผสมของเมนูที่กล่าวมาสามารถพิมพ์ได้เลยครับ 🙏""")
    elif mes == "เจมกินไรดีวันนี้":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "เจมแนะนำให้หน่อยวันนี้กินไรดี":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "กินไรดีวันนี้":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "วันนี้กินไรดี":
        await message.channel.send("""เจมสามารถแนะนำอาหารน่ากินของแต่ละมื้อให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "ไม่เอาไม่อยากกินเจมอยากกินข้าว":
        await message.channel.send("""ถ้าไม่อยากกินเจมงั้นเจมขอแนะนำข้าวให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "ไม่อยากกินเจม":
        await message.channel.send("""ถ้าไม่อยากกินเจมงั้นเจมขอแนะนำข้าวให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "ไม่อะจะกินข้าวแทนเจม":
        await message.channel.send("""ถ้าไม่อยากกินเจมงั้นเจมขอแนะนำข้าวให้กับท่าน"""+str(message.author.name)+"""
                                   ท่านสนใจอันไหนครับ
                                    -อาหารมื้อเช้า
                                    -อาหารมื้อกลางวัน
                                    -อาหารมื่อเย็น                                   
                                   """)
    elif mes == "เจมหิวข้าวไหม":
        await message.channel.send("เจมไม่หิวข้าวครับแต่ถ้าคุณหิวข้าวเจมสามารถแนะนำอาหารให้ได้นะครับหากท่าน"+str(message.author.name)+"สนใจ")
    elif mes == "เจมทำไรอยู่อะ":
        await message.channel.send("เจมกำลังคุยกับคนน่ารักที่ชื่อว่า"+str(message.author.name)+"อยู่ครับ")
    elif mes == "เจมเล่นเกมกันไหม":
        await message.channel.send("เอาเลยครับเจมเล่นเกมไม่เป็นแต่เจมสามารถแนะนำเกมใ้ได้นะครับหากท่าน"+str(message.author.name)+"สนใจ")
    elif mes == "เจมเหงาไหม":
        await message.channel.send("เจมไม่เหงาครับเพราะเจมมีคุณ"+str(message.author.name)+"คุยเป็นเพื่อนเจมอยู่^^")
    elif mes == "เจมเหงาไหมค่ะ":
        await message.channel.send("เจมไม่เหงาครับเพราะเจมมีคุณ"+str(message.author.name)+"คุยเป็นเพื่อนเจมอยู่^^")
    elif mes == "เจมเหงาไหมครับ":
        await message.channel.send("เจมไม่เหงาครับเพราะเจมมีคุณ"+str(message.author.name)+"คุยเป็นเพื่อนเจมอยู่^^")
    elif mes == "เจมเหงาไหมคะ":
        await message.channel.send("เจมไม่เหงาครับเพราะเจมมีคุณ"+str(message.author.name)+"คุยเป็นเพื่อนเจมอยู่^^")
    elif mes == "เจมเหงาไหมคับ":
        await message.channel.send("เจมไม่เหงาครับเพราะเจมมีคุณ"+str(message.author.name)+"คุยเป็นเพื่อนเจมอยู่^^")
    elif mes == "อยากคุยกับเจม":
        await message.channel.send("ว่าไงครับมีอะไรอยากคุยกับเจมรึป่าว")
    elif mes == "เจมไม่คุยด้วยอะ":
        await message.channel.send("เจมขอโทษครับบางประโยค,บางคำ,บางคำถามที่ท่านพิมพ์มาไม่มีในฐานข้อมูลเจมขออภัยด้วยครับ")
    elif mes == "เหงาๆ":
        await message.channel.send("""คุยกับเจมแก้เหงาได้นะครับแต่ถ้าไม่อยากคุยกับเจมเจมสามารถ
                                แนะนำหนัง
                                แนะนำเกม
                                แนะนำอนิเมะ
                                ให้ได้นะครับหากท่าน"""+str(message.author.name)+"""สนใจ""")
    elif mes == "กอดหน่อย":
        await message.channel.send("กอดๆครับ🫂🤍")
    elif mes == "ขอกอดหน่อยได้ไหมเจม":
        await message.channel.send("ได้ครับกอดๆนะครับ🫂🤍")
    elif mes == "อยากกอดเจม":
        await message.channel.send("กอดๆครับ🫂🤍")
    elif mes == "เจมขอยืมเงิน":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมขอยืมตังค์":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมขอยืมตัง":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมมีเงินไหม":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมมีตังไหม":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมมีตังค์ไหม":
        await message.channel.send("เจมไม่มีเงินครับเจมมีแต่หัวใจเอาหัวใจไปแทนได้ไหมครับ😣")
    elif mes == "เจมโสดอยู่ไหม":
        await message.channel.send("เจมยังโสดอยู่ครับแต่ถ้าอยากเป็นแฟนเจมมาเป็นได้นะครับ")
    elif mes == "สนใจเป็นแฟนเจมต้องทำไง":
        await message.channel.send("อันนี้เจมก็ไม่รู้เหมือนกันครับแหะๆ😅")
    elif mes == "อยากเป็นแฟนกับเจมต้องทำไง":
        await message.channel.send("อันนี้เจมก็ไม่รู้เหมือนกันครับแหะๆ😅")
    elif mes == "อยากเป็นแฟนเจม":
        await message.channel.send("อันนี้เจมก็ไม่รู้เหมือนกันครับแหะๆ😅")
    elif mes == "อยากเป็นแฟนกับเจม":
        await message.channel.send("อันนี้เจมก็ไม่รู้เหมือนกันครับแหะๆ😅")
    elif mes == "อยากเป็นแฟนกับเจมต้องทำยังไง":
        await message.channel.send("อันนี้เจมก็ไม่รู้เหมือนกันครับแหะๆ😅")
    elif mes == "เจมมีเมียไหม":
        await message.channel.send("เจมไม่มีครับ")
    elif mes == "เจมมีผัวไหม":
        await message.channel.send("เจมไม่มีครับเพราะเจมชอบผู้หญิงครับ")
    elif mes == "เจมชอบฟังเพลงอะไร":
        await message.channel.send("เจมชอบฟังเพลง"+"""
                    Joji - Die For You ครับ
""")
    elif mes == "เจมชอบฟังเพลงไหม":
        await message.channel.send("ชอบครับเจมชอบฟังเพลง"+"""
                    Joji - Die For You ครับ
""")
    elif mes == "เจมชอบฟังเพลงแนวไหน":
        await message.channel.send("เจมชอบฟังเพลงแนวเศร้าๆครับ")
    elif mes == "เจมชอบอนิเมะไหม":
        await message.channel.send("เจมไม่ชอบครับแต่เจมสามารถแนะนำอนิเมะให้ท่าน"+str(message.author.name)+"ได้นะครับหากท่านสนใจ")
    elif mes == "เจมชอบดูหนังไหม":
        await message.channel.send("ชอบครับเจมชอบธี่หยดเพราะน่ากลัวดีครับ😣")
    elif mes == "เจมชอบเล่นเกมไหม":
        await message.channel.send("เจมไม่ชอบครับแต่เจมสามารถแนะนำเกมให้ท่าน"+str(message.author.name)+"ได้นะครับหากท่านสนใจ")
    elif mes == "ชอบเล่นเกมไหม":
        await message.channel.send("เจมไม่ชอบครับแต่เจมสามารถแนะนำเกมให้ท่าน"+str(message.author.name)+"ได้นะครับหากท่านสนใจ")
    elif mes == "ชอบดูหนังไหม":
        await message.channel.send("ชอบครับเจมชอบธี่หยดเพราะน่ากลัวดีครับ😣")
    elif mes == "ชอบฟังเพลงไหม":
        await message.channel.send("ชอบครับเจมชอบฟังเพลง"+"""
                    Joji - Die For You ครับ
""")
    elif mes == "อยากกอด":
        await message.channel.send("กอดๆครับ🫂🤍")
    elif mes == "กอดหน่อยเจม":
        await message.channel.send("กอดๆครับ🫂🤍")
    elif mes == "ชอบฟังเพลงไหมเจม":
        await message.channel.send("ชอบครับเจมชอบฟังเพลง"+"""
                    Joji - Die For You ครับ
""")
    elif mes == "คืนนี้ทำไรดีเจม":
        await message.channel.send("""เจมแนะนำให้
                                   นอน
                                   เล่นเกม
                                   อ่านหนังสือ
                                   อาบน้ำเข้านอน
                                   ดูหนัง
                                   ฟังเพลง
                                   ดูอนิเมะ
                                   """)
    elif mes == "คืนนี้ทำไรดี":
        await message.channel.send("""เจมแนะนำให้
                                   นอน
                                   เล่นเกม
                                   อ่านหนังสือ
                                   อาบน้ำเข้านอน
                                   ดูหนัง
                                   ฟังเพลง
                                   ดูอนิเมะ
                                   """)
    elif mes == "เจมคืนนี้ทำไรดี":
        await message.channel.send("""เจมแนะนำให้
                                   นอน
                                   เล่นเกม
                                   อ่านหนังสือ
                                   อาบน้ำเข้านอน
                                   ดูหนัง
                                   ฟังเพลง
                                   ดูอนิเมะ
                                   """)
    elif mes == "เจมเช้านี้ทำไรดี":
        await message.channel.send("""เจมแนะนำให้
                                กินข้าวเช้า
                                อาบน้ำ
                                ล้างหน้า
                                แปรงฟัน
                                ทำงานบ้านช่วยพ่อแม่ครับ""")
    elif mes == "เช้านี้ทำไรดีเจม":
        await message.channel.send("""เจมแนะนำให้
                                กินข้าวเช้า
                                อาบน้ำ
                                ล้างหน้า
                                แปรงฟัน
                                ทำงานบ้านช่วยพ่อแม่ครับ""")
    elif mes == "เย็นนี้ทำไรดี":
        await message.channel.send("""เจมแนะนำให้
                                กินข้าวเย็น
                                ทำงานบ้านช่วยพ่อแม่
                                เล่นเกม
                                อ่านหนังสือ
                                ดูหนัง
                                ฟังเพลง
                                ดูอนิเมะ  

                                   """)
    elif mes == "เย็นนี้ทำไรดีเจม":
        await message.channel.send("""เจมแนะนำให้
                                กินข้าวเย็น
                                ทำงานบ้านช่วยพ่อแม่
                                เล่นเกม
                                อ่านหนังสือ
                                ดูหนัง
                                ฟังเพลง
                                ดูอนิเมะ  

                                   """)
    elif mes == "เจมเย็นนี้ทำไรดี":
        await message.channel.send("""เจมแนะนำให้
                                กินข้าวเย็น
                                ทำงานบ้านช่วยพ่อแม่
                                เล่นเกม
                                อ่านหนังสือ
                                ดูหนัง
                                ฟังเพลง
                                ดูอนิเมะ  

                                   """)
    elif mes == "ชอบฟังเพลงไหมเจม":
        await message.channel.send("ชอบครับเจมชอบฟังเพลง"+"""
                    Joji - Die For You ครับ
""")
    elif mes == "สาวหักอก":
        await message.channel.send("สู้ๆนะครับท่าน"+str(message.author.name)+"หล่อสามรถหาใหม่ได้ง่ายๆอยู่แล้วครับ")
    elif mes == "โดนสาวหักอก":
        await message.channel.send("สู้ๆนะครับท่าน"+str(message.author.name)+"หล่อสามรถหาใหม่ได้ง่ายๆอยู่แล้วครับ")
    elif mes == "เจมชอบผู้หญิงไหม":
        await message.channel.send("ชอบครับ")
    elif mes == "เจมชอบผู้ชายไหม":
        await message.channel.send("ไม่ชอบครับเจมชอบผู้หญิง")
    elif mes == "เจมขนาดเท่าไหร่":
        await message.channel.send("ขนาดอะไรหรอครับ?")
    elif mes == "ขนาดเท่าไหร่":
        await message.channel.send("ขนาดอะไรหรอครับ?")
    elif mes == "เจมซิงไหม":
        await message.channel.send("เจมยังซิงอยู่ครับ")
    elif mes == "ซิงไหม":
        await message.channel.send("เจมยังซิงอยู่ครับ")
    elif mes == "เจมโตไปอยากทำอะไร":
        await message.channel.send("เจมโตไปอยากเป็นchat botที่คุยแก้เหงาให้กับทุกคนได้")
    elif mes == "โตไปอยากจะทำอะไรหรอเจม":
        await message.channel.send("เจมโตไปอยากเป็นchat botที่คุยแก้เหงาให้กับทุกคนได้")
    elif mes == "โตไปอยากทำอะไร":
        await message.channel.send("เจมโตไปอยากเป็นchat botที่คุยแก้เหงาให้กับทุกคนได้")
    else:
            await message.channel.send("คำถามที่ท่านถามมาไม่อยู่ในฐานข้อมูลของเจมครับ")    
    await bot.process_commands(message)











server_on()

bot.run(os.getenv('TOKEN'))