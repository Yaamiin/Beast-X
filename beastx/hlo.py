from . import *

import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from beastx import CMD_HELP, lang

@beast.on(beastx_cmd(pattern="hi ?(.*)"))
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "šŗ"
    await edit_or_reply(
        event,
        f"{ult}āØāØ{ult}āØ{ult}{ult}{ult}\n{ult}āØāØ{ult}āØāØ{ult}āØ\n{ult}{ult}{ult}{ult}āØāØ{ult}āØ\n{ult}āØāØ{ult}āØāØ{ult}āØ\n{ult}āØāØ{ult}āØ{ult}{ult}{ult}\nāļøāļøāļøāļøāļøāļøāļøāļø",
    )
    
@beast.on(beastx_cmd(pattern="hello"))
async def hello(bst):
  await bst.edit('''
āāāā¦āā¦āāāāāāā
āāāāāā£āāāāX Xā
āāāāāā£āā£āā£ā°āÆā
āāāā©āā©āā©āā©āāā
 ''')
CMD_HELP.update(
    {
        "Hello/hi": """**Plugin : **`Hello/hi`
        
**Commands in animation2 are **
  ā¢  `.hi`
  ā¢  `.hello`
  
  
**Function : **__sends animated hello/hi.__**"""
    }
