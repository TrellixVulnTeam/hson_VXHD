

import random
from ..tosh import Cmds
from telethon import events

@icss.on(
    icss_cmd(pattern="الاوامر")
)
async def cmds(icss):
    await eor(icss, Cmds)



import random

from telethon import events

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )



import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التسليه :** \n⪼ `.قمر` \n⪼ `.اقمار` \n⪼ `.قمور` \n⪼ `.قلوب` \n⪼ `.قلب ` \n⪼ `.جيم` \n⪼ `.افكر` \n⪼ `.افكرر` \n⪼ `.شنوو ` \n⪼ `.مح ` \n⪼ `.متت ` \n⪼ `.النضام الشمسي ` \n⪼ `.موسيقى ` \n⪼ `.قنبله ` \n⪼ `.مكبعات ` \n⪼ `.افعى ` \n⪼ `.طائره ` \n⪼ `.نجمه ` \n⪼ `.دائره ` \n⪼ `.شرطه ` \n⪼ `.فايروس ` \n⪼ `.غبي ` \n⪼ `.العد التنازلي`\n⪼ `.يد`\n⪼ `.تهكير`\n⪼ `.قرد `\n⪼ `.بشره `\n⪼ `.انيم `\n⪼ `.نيكول `\n⪼ `.مربع`\n⪼ `.قاتل `\n⪼ `.تحميل`\n⪼ `.رجل `\n⪼ `.شنوو `\n⪼ `.ريبي `\n⪼ `.تفريغ `\n⪼ `.حلويات `\n⪼ `.فليم`\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التسليه :** \n⪼ `.قمر` \n⪼ `.اقمار` \n⪼ `.قمور` \n⪼ `.قلوب` \n⪼ `.قلب ` \n⪼ `.جيم` \n⪼ `.افكر` \n⪼ `.افكرر` \n⪼ `.شنوو ` \n⪼ `.مح ` \n⪼ `.متت ` \n⪼ `.النضام الشمسي ` \n⪼ `.موسيقى ` \n⪼ `.قنبله ` \n⪼ `.مكبعات ` \n⪼ `.افعى ` \n⪼ `.طائره ` \n⪼ `.نجمه ` \n⪼ `.دائره ` \n⪼ `.شرطه ` \n⪼ `.فايروس ` \n⪼ `.غبي ` \n⪼ `.العد التنازلي`\n⪼ `.يد`\n⪼ `.تهكير`\n⪼ `.قرد `\n⪼ `.بشره `\n⪼ `.انيم `\n⪼ `.نيكول `\n⪼ `.مربع`\n⪼ `.قاتل `\n⪼ `.تحميل`\n⪼ `.رجل `\n⪼ `.شنوو `\n⪼ `.ريبي `\n⪼ `.تفريغ `\n⪼ `.حلويات `\n⪼ `.فليم`\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م4":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الردود :** \n⪼ `.اضف رد ` \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الردود :** \n⪼ `.اضف رد ` \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م5":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الرفع :** \n⪼ `.رفع مطي ` \n⪼ `.رفع جلب ` \n⪼ `.رفع بكلبي `\n⪼ `.رفع مرتي ` \n⪼ `.رفع تاج ` \n⪼ `.رفع جريذي `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الرفع :** \n⪼ `.رفع مطي ` \n⪼ `.رفع جلب ` \n⪼ `.رفع بكلبي `\n⪼ `.رفع مرتي ` \n⪼ `.رفع تاج ` \n⪼ `.رفع جريذي `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م6":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الحمايه :** \n⪼ `.الكل ` \n⪼ `.المسموح لهم ` \n⪼ `.سماح `\n⪼ `.رفض ` \n⪼ `.بلوك ` \n⪼ `.انبلوك `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الحمايه :** \n⪼ `.الكل ` \n⪼ `.المسموح لهم ` \n⪼ `.سماح `\n⪼ `.رفض ` \n⪼ `.بلوك ` \n⪼ `.انبلوك `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )



import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م7":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م8":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م9":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م10":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م11":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر المجموعه :** \n⪼ `.المجموعه ` \n⪼ `.رفع مشرف ` \n⪼ `.رفع مالك ` \n⪼ `.تك ` \n⪼ `.الاحصائيات ` \n⪼ `.تنظيف الحسابات ` \n⪼ `.الاعضاء ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر المجموعه :** \n⪼ `.المجموعه ` \n⪼ `.رفع مشرف ` \n⪼ `.رفع مالك ` \n⪼ `.تك ` \n⪼ `.الاحصائيات ` \n⪼ `.تنظيف الحسابات ` \n⪼ `.الاعضاء ` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )



import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م12":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الترجمه :** \n⪼ `.ترجمه ar` لترجمه من اي لغه الى العربيه \n⪼ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الترجمه :** \n⪼ `.ترجمه ar` لترجمه من اي لغه الى العربيه \n⪼ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م13":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر البحث :** \n⪼ `.بحث` للبحث عن اغنيه + .بحث عشق \n⪼ `.صوره` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر البحث :** \n⪼ `.بحث` للبحث عن اغنيه + .بحث عشق \n⪼ `.صوره` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م14":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م15":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م16":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )



import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م17":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الحساب :** \n⪼ `.اسم` لتغير اسم حسابك \n⪼ `.صوره` لتغير صوره حسابك \n⪼ `.معرف ` لتغير معرف حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.مسح الصور ` لحذف جميع صور حسابك \n⪼ `.مسح ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر الحساب :** \n⪼ `.اسم` لتغير اسم حسابك \n⪼ `.صوره` لتغير صوره حسابك \n⪼ `.معرف ` لتغير معرف حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.مسح الصور ` لحذف جميع صور حسابك \n⪼ `.مسح ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م18":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪"
            )



import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "قائمه":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n⪼ **قائمه اوامر اكسس قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆰 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪 "
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n⪼ **قائمه اوامر اكسس قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆰 𝙎𝙊𝙐𝙍𝘾𝞝 𝑮𝑷𝑻𝑯𝑶𝑵 - [𝘿𝙀𝙑](t.me/GPTHON) 𓆪 "
            )




import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "ديڤ":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n ⌔∮𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @GPTHON \n  ⌔∮𝑫𝑬𝑽 𝑰𝑫 ↬ 1707671487"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n ⌔∮𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @GPTHON \n  ⌔∮𝑫𝑬𝑽 𝑰𝑫 ↬ 1707671487"
            )




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جلب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في اكسس",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في اكسس",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مطي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مطي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تم رفعه مطي هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تم رفعه مطي هنا ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مرتي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )



from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع تاج(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه تـاج 👑🔥 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه تـاج 👑🔥 ",
        )




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بكلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه بڪلبك 🖤 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه بڪلبك 🖤 ",
        )




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جريذي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جريذي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )




from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع فرخ(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع فرخ(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تم رفعه فرخ هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تم رفعه فرخ هنا ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj




import random

from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@bot.on(admin_cmd(pattern="نسبه الانوثه(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="نسبه الانوثه(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الانوثه لـ [{custom}](tg://user?id={user.id}) هيه {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الانوثه لـ [{tag}](tg://user?id={user.id}) هيه {ioi} ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj



from . import reply_id

DEV_IMG = "https://telegra.ph/file/c80cd08e4f03c3b867cb4.jpg"
DEV_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑮𝑷𝑻𝑯𝑶𝑵 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪"
EMOJI = "  𓄂† "


@icssbot.on(icss_cmd(outgoing=True, pattern="المطور$"))
@icssbot.on(sudo_cmd(pattern="المطور$", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    reply_to_id = await reply_id(e)
    if DEV_IMG:
        dev_c = f"**{DEV_TEXT}**\n"
        dev_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝑮𝑷𝑻𝑯𝑶𝑵ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        dev_c += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @Y88YH ༗\n"
        dev_c += f"**{EMOJI}** 𝑫𝑬𝑽 𝑰𝑫 ↬ 1707671487 ༗\n"
        dev_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝑮𝑷𝑻𝑯𝑶𝑵ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await e.client.send_file(
            e.chat_id, DEV_IMG, caption=dev_c, reply_to=reply_to_id
        )
        await e.delete()
