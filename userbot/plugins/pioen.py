import asyncio
import random

TOSHA = [
    """
༆

𝙸ғ ᴜ ᴅᴏɴᴛ sᴀᴄʀɪғɪᴄᴇ FᴏR 𝚆𝚑𝚊𝚝 𝚄 𝚠𝙰𝚗𝚝,
"ᴡʜAᴛ U ᴡAɴᴛ" ʙᴇCᴏᴍᴇS ᴛʜE Sᴀᴄʀɪғɪᴄᴇ.
""",
    """
༆

Tʜᴇʀᴇ ɪS Nᴏ Dᴏᴜʙᴛ, 
EᴠᴇʀʏOɴᴇ ɪs Dᴇᴠɪʟ...


ᴀɴᴅ TʜᴇRᴇ  ɪS Nᴏ Dᴏᴜʙᴛ,
Wᴇ ᴀRᴇ Dᴇʟᴠɪʟ ᴏᴜʀSᴇʟᴠᴇS..𓁹𓁹
""",
    """
༒︎

𝐼 𝑆ℎ𝑜𝑢𝑙𝑑 𝐻𝑎𝑣𝑒...⌫
𝐼 𝐶𝑜𝑢𝑙𝑑 𝐻𝑎𝑣𝑒...⌫
𝐼 𝑊𝑖𝑠ℎ 𝐼 𝐻𝑎𝑑...⌫
𝐼𝑓 𝑂𝑛𝑙𝑦 𝐼 𝐻𝑎𝑑...⌫

߷𝔻𝕠𝕟𝕥 𝕋𝕙𝕚𝕟𝕜߷

❥︎𝙅𝙪𝙨𝙩 𝘿𝙤 𝙞𝙩 𝙉𝙤𝙬
""",
    """
༆

𝑻𝒉𝒆 𝒐𝒏𝒍𝒚 𝒕𝒉𝒊𝒏𝒈 𝒘𝒆 𝒂𝒓𝒆 𝒂𝒍𝒍𝒐𝒘𝒆𝒅 𝒕𝒐 𝒅𝒐 𝒊𝒔 𝒕𝒐 𝔹𝕖𝕝𝕚𝕖𝕧𝕖 𝒕𝒉𝒂𝒕 𝒘𝒆 𝒘𝒐𝒏'𝒕 𝙍𝙚𝙜𝙧𝙚𝙩 𝒕𝒉𝒆 𝒄𝒉𝒐𝒊𝒄𝒆𝒔 𝒘𝒆 𝒎𝒂𝒅𝒆.


❥︎ ʟᵉᵛⁱ ᴀᶜᵏᵉʳᵐᵃⁿ
""",
    """
༒︎

ℝ𝕖𝕘𝕣𝕖𝕥𝕤...

𝑾𝒆 𝒂𝒍𝒍 𝒂𝒓𝒆 𝒇𝒖𝒍𝒍 𝒐𝒇 𝒓𝒆𝒈𝒓𝒆𝒕𝒔,
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝐶ℎ𝑎𝑛𝑔𝑒 𝒊𝒕.
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝑆𝑢𝑝𝑝𝑟𝑒𝑠𝑠 𝒊𝒕.
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝐸𝑥𝑝𝑟𝑒𝑠𝑠 𝒊𝒕.
𝑰𝒕 𝒑𝒊𝒏𝒄𝒉 𝒖𝒔 𝒂𝒍𝒍 𝒐𝒗𝒆𝒓 𝒐𝒖𝒓 ᒪIᖴᗴ,
𝚃𝚒𝚕𝚕 𝙳𝚎𝚊𝚝𝚑 .

𝔒ℜ

𝑨𝒇𝒕𝒆𝒓 𝑳𝒊𝒇𝒆 ??  𝑊ℎ𝑜 𝐾𝑛𝑜𝑤𝑠¯\_(ツ)_/¯
""",
    """
༒︎

ℕ𝕠𝕥𝕙𝕚𝕟𝕘 𝚒𝚗 𝚝𝚑𝚒𝚜 𝚏𝚞𝚔𝚒𝚗𝚐 𝚠𝚘𝚛𝚕𝚍 𝚒𝚜 𝐂𝐨𝐧𝐬𝐭𝐚𝐧𝐭...

𝑨𝒍𝒍 𝒂𝒓𝒆 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞 𝒘𝒊𝒕𝒉 𝒓𝒆𝒔𝒑𝒆𝒄𝒕 𝒕𝒐 𝑺𝒐𝒎𝒆𝒐𝒏𝒆 / 𝑺𝒐𝒎𝒆𝒕𝒉𝒊𝒏𝒈.""",
    """
༒︎

𝙷𝚊𝚟𝚎 𝚞 𝙴𝚟𝚎𝚛 𝕀𝕞𝕒𝕘𝕚𝕟𝕖....

This "𝕀𝕞𝕒𝕘𝕚𝕟𝕖" word Is itself a 𝐋𝐢𝐞

Which 𝒅𝒐𝒏'𝒕 𝑬𝒙𝒊𝒔𝒕.
""",
]




@icssbot.on(admin_cmd(pattern="انكلش"))
async def ics(kimo):
    await kimo.edit("**⌔∮ اهلا عزيزي يتم تجهيز نبذه لاجلك.**")
    await asyncio.sleep(2)
    tosh = random.choice(TOSHA)
    return await kimo.edit(f"{tosh}")
