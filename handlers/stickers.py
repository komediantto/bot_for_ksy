import random

from aiogram import types

from create_bot import bot

stickerpack = [
    r'CAACAgIAAxkBAAEFqQNjBh56t3WKnRJ-M_08PcQ6q1NapgACAgAD_CBIFBlTbyrmKEFvKQQ',
    r'CAACAgIAAxkBAAEFqQdjBh6HmNyHe9T8tOo5Uxl1guzWJgACAwAD_CBIFGuH3MANkGF4KQQ',
    r'CAACAgIAAxkBAAEFqQljBh6JSTIF5Ng1wOXqabEOazbn0wACBAAD_CBIFAggf9e99eExKQQ',
    r'CAACAgIAAxkBAAEFqQtjBh6MGq8ZnY0yh4WYOeYqaPvSPAACBQAD_CBIFLk-AAGnOokNECkE',
    r'CAACAgIAAxkBAAEFqQ1jBh6Oug1tKf4Ey314XjgzEULp6QACBgAD_CBIFL0kJeqMvZjyKQQ',
    r'CAACAgIAAxkBAAEFqQ9jBh6TO2NGwPURDSv1d10Z_8zANgACBwAD_CBIFElMqFCtJB3CKQQ',
    r'CAACAgIAAxkBAAEFqRFjBh6VsW96cGL7KNJD4mZkqAVpKwACCAAD_CBIFAPC---WAWuIKQQ',
    r'CAACAgIAAxkBAAEFqRVjBh6cI5VDNfxVcdQYfAvat5PLUQACCQAD_CBIFMwgFwlN3wGUKQQ',
    r'CAACAgIAAxkBAAEFqRdjBh6f7oXNM7vtE1snI_Avi0kp5gACCgAD_CBIFNmSTCTgt625KQQ',
    r'CAACAgIAAxkBAAEFqRljBh6jl3zxVKgQ4gN9OAYOHpaHIwACCwAD_CBIFLYuKyEeWDlPKQQ',
    r'CAACAgIAAxkBAAEFqRtjBh6lGZJKUEya_rFPxm-z48rbNQACDAAD_CBIFGSRcIooeXCgKQQ',
    r'CAACAgIAAxkBAAEFqR1jBh6pBUvdQLLtQC5BZBufbT1CZAACDQAD_CBIFDrX7hMHLNoEKQQ',
    r'CAACAgIAAxkBAAEFqSFjBh6z1E9OlrGyntkn3746CUc0TQACDgAD_CBIFGHLfH6ZHKssKQQ',
    r'CAACAgIAAxkBAAEFqSNjBh63HX0rnqnwxqTNE0p6U2HTHQACDwAD_CBIFCfhH-069os5KQQ',
    r'CAACAgIAAxkBAAEFqSVjBh68LYnsZl6U3-YoTpXnYgrrsAACEAAD_CBIFG5XtYu3xaASKQQ',
    r'CAACAgIAAxkBAAEFqSdjBh7APTAyNrtxQZGa1Tb0zHoVvQACEQAD_CBIFMSm0FoOBBhpKQQ',
    r'CAACAgIAAxkBAAEFqSljBh7ESGGgcPbZkPIAAU1BVtV9T4EAAhIAA_wgSBQQKeLWE0R1BCkE',
    r'CAACAgIAAxkBAAEFqStjBh7HX8fOSxmDvaCRRxGj4HQgrgACEwAD_CBIFMB-W1jVFkGtKQQ',
    r'CAACAgIAAxkBAAEFqS1jBh7LcyVrQqCu38VHUh_GDoy7IwACFAAD_CBIFClMcRWeYdHqKQQ',
    r'CAACAgIAAxkBAAEFqS9jBh7Pl_wbcUFxbIxBkW3n-uh-wAACFQAD_CBIFOvLznVPO-KbKQQ',
    r'CAACAgIAAxkBAAEFqTFjBh7TBCCCvyJI7PgdwDbNir2UVgACFgAD_CBIFDWUm86S9xYbKQQ',
    r'CAACAgIAAxkBAAEFqTNjBh7XdECldYbVyRV2zWkU8uRhigACFwAD_CBIFKutYEz0s-bPKQQ',
    r'CAACAgIAAxkBAAEFqTVjBh7bMVm8PZySZdyaHNzPuRD8-AACGAAD_CBIFPdSt6k7aMtoKQQ',
    r'CAACAgIAAxkBAAEFqTdjBh7f43NUPjk0YJAtmXDaIw64nQACGQAD_CBIFO0LEaL-VhfTKQQ',
    r'CAACAgIAAxkBAAEFqTljBh7jx06Wk5BH6tz0iOXBEZMcnwACGgAD_CBIFGk9TKVYFdm6KQQ',
    r'CAACAgIAAxkBAAEFqTtjBh7n863iZkEweAJU3iiDFtT6jAACGwAD_CBIFBSN4P4DGJhpKQQ',
    r'CAACAgIAAxkBAAEFqT1jBh7rwJHAQecWusLr8Dk7nPRpHQACHAAD_CBIFM109R0-i-LLKQQ',
]


# Функция для отправки трёх рандомных стикеров из списка
async def send_random_stickers(message: types.Message):
    await message.reply('Упс! Кажется ты переборщила, мать. '
                        'Лови мотивацию')
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(stickerpack))
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(stickerpack))
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(stickerpack))
