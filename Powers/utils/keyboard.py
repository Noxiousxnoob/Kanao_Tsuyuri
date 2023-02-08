from pykeyboard import InlineButton as ib
from pykeyboard import InlineKeyboard as ikb
from pyrogram.types import InlineKeyboardButton as KB

from Chimku.database.stuffs import STUFF

stuff = STUFF()

initial = [
    [
        KB("Flamingo", "flamingo"),
        KB("Vistas", "vistas")
    ],
    [
        KB("Grammar", "grammar"),
        KB("Others", "other")
    ]
]

def stuff_kb(needed: str):
    req = needed.lower()
    media_kb = ikb(3)
    x = STUFF.get_files(req)
    if x:
        for i in x:
            media_kb.add(
                ib(str(i), f"call_{str(i).replace(' ', '_')}")
            )
        media_kb.add(
            ib("Back", "back"),
            ib("Close", "close")
        )
        return True, media_kb
    else:
        media_kb.add( 
            ib("Back", "back"),
            ib("Close", "close") 
            )
        return False, media_kb

def purchase_kb():
    purchase = ikb()
    purchase.row(
        ib("Purchase", "purchase")
    )
    purchase.row(
        ib("Close", "close"),
        ib("Back", "bback")
    )
    return purchase

purchased = [
    [
        KB("Back", "bback")
    ],
    [
        KB("Close", "close")
    ]
]