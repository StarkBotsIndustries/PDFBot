from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can help you to do stuff on PDFs as well as convert images to PDF. Use /help to see features.

JUST SEND A PDF (or an image) to get started.

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
    ]

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot with PDF Tools by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/PDFBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
