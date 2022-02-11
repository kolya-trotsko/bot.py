from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '1946562538:AAFfw_CFeOcDRfoLpQdLeWc_4-Y5zvsjh3A'
price = ''
suma = 0
star = "✨"
lover = "🥰"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Прайс","Про нас","Корзина"]
    keyboard.add(*buttons)
    await message.answer("Привіт✨\nЯ допоможу тобі обрати найкращий подарунок\nдля тебе або твоїх близьких" + lover, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["Прайс","Пошукаю ще"])
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Бомбочки","Тверда піна","Морська сіль","Скраби","Бокси"]
    keyboard.add(*buttons)
    await message.answer("Обери що буде у твоєму замовленні:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Бомбочки")
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "З морською сіллю", "Бомбочка з перламутром", "Пончик", "Серце", "Бомбочка Ялинка", "Міні-чаша", "Відьмин котел", "Чаша кохання", "Хелловінська ніч"
        ]
    keyboard.add(*buttons)
    await message.answer("Ось види бомбочок які ви можете замовити", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "З морською сіллю")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/5rqh9tcrg3e0p0a/%D0%B1%D0%BE%D0%BC%D0%B1%D0%BE%D1%87%D0%BA%D0%B0%20%D0%B7%20%D0%BC%D0%BE%D1%80%D1%81%D1%8C%D0%BA%D0%BE%D1%8E%20%D1%81%D1%96%D0%BB%D0%BB%D1%8E.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку з морською сіллю)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Бомбочка з перламутром")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/z7209hdjrwbwo09/%D0%B1%D0%BE%D0%BC%D0%B1%D0%BE%D1%87%D0%BA%D0%B0%20%D0%B7%20%D0%BF%D0%B5%D1%80%D0%BB%D0%B0%D0%BC%D1%83%D1%82%D1%80%D0%BE%D0%BC%20.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку з перламутром)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Пончик")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/nvccg84puzfsqri/%D0%B1%D0%BE%D0%BC%D0%B1%D0%BE%D1%87%D0%BA%D0%B0%20%D0%BF%D0%BE%D0%BD%D1%87%D0%B8%D0%BA.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Пончик)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Серце")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/pkqa1gckuqc22xp/%D0%B1%D0%BE%D0%BC%D0%B1%D0%BE%D1%87%D0%BA%D0%B0%20%D1%81%D0%B5%D1%80%D1%86%D0%B5.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Серце)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Бомбочка ялинка")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/bceitytlbiban9x/%D0%B1%D0%BE%D0%BC%D0%B1%D0%BE%D1%87%D0%BA%D0%B0%20%D1%8F%D0%BB%D0%B8%D0%BD%D0%BA%D0%B0.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Ялинка)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Міні-чаша")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/362gqgt65jzyj06/%D0%BC%D1%96%D0%BD%D1%96-%D0%BC%D1%96%D0%BD%D1%96%20%D1%87%D0%B0%D1%88%D0%B0.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Міні-чаша)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Відьмин котел")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/hwc3z6g77fq939l/%D0%BC%D1%96%D0%BD%D1%96-%D1%87%D0%B0%D1%88%D0%B0.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Відьмин котел)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Чаша кохання")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/2p0jx0i818rp69r/%D1%87%D0%B0%D1%88%D0%B0%20%D0%BA%D0%BE%D1%85%D0%B0%D0%BD%D0%BD%D1%8F.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Чаша кохання)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Хелловінська ніч")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/zb5pnodm8v0zwcp/%D1%85%D0%B5%D0%BB%D0%BB%D0%BE%D0%B2%D1%96%D1%96%D0%BD%D1%81%D1%8C%D0%BA%D0%B0%20%D0%BD%D1%96%D1%87.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (бомбочку Хелловінська ніч)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Тверда піна")
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Зірка", "Ялинка", "Цукерка"
        ]
    keyboard.add(*buttons)
    await message.answer("Ось види твердої піни які ви можете замовити", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Зірка")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/x7681ark3k6pppf/%D0%B7%D1%96%D1%80%D0%BA%D0%B8.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (тверду піну Зірка)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Ялинка")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/x7y6szapg2l0ljt/%D1%82%D0%B2%D0%B5%D1%80%D0%B4%D0%B0%20%D0%BF%D1%96%D0%BD%D0%B0%20%D1%8F%D0%BB%D0%B8%D0%BD%D0%BA%D0%B0.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (тверду піну Ялинка)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Цукерка")
async def registration(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://www.dropbox.com/s/jznze9z082cq1y0/%D1%82%D0%B2%D0%B5%D1%80%D0%B4%D0%B0%20%D0%BF%D1%96%D0%BD%D0%B0%20%D1%86%D1%83%D0%BA%D0%B5%D1%80%D0%BA%D0%B0.jpg?dl=0")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "В корзину (тверду піну Цукерка)", "Пошукаю ще"
        ]
    keyboard.add(*buttons)
    await message.answer("Беремо?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Морська сіль")
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Стандарт", "З перламутром", "З пінорозчинником"
        ]
    keyboard.add(*buttons)
    await message.answer("Ось види морської солі які ви можете замовити:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Скраби")
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Рафаелло","Утромбований"
        ]
    keyboard.add(*buttons)
    await message.answer("Ось види скрабів які ви можете замовити", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Бокси")
async def registration(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Бокси"
    ]
    keyboard.add(*buttons)
    await message.answer("Ось види боксів які ви можете замовити", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку з морською сіллю)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 60
    price += " (бомбочка з морською сіллю) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку з перламутром)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 45
    price += " (бомбочка з перламутром) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Пончик)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 65
    price += " (бомбочка Пончик) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Серце)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 40
    price += " (бомбочка Серце) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Ялинка)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 80
    price += " (бомбочка Ялинка) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Міні-чаша)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 45
    price += " (бомбочка Міні-чаша) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Відьмин котел)")
async def registration(message: types.Message):
    global price
    global suma
    suma += 45
    price += " (бомбочка Відьмин котел) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Чаша кохання)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 90
    price += " (бомбочка Чаша кохання) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (бомбочку Хелловінська ніч)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 80
    price += " (бомбочка Хелловінська ніч) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (тверду піну Зірка)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 30
    price += " (тверда піна Зірка) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (тверду піну Ялинка)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 30
    price += " (тверда піна Ялинка) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "В корзину (тверду піну Цукерка)")
async def registration(message: types.Message):
    global suma
    global price
    suma += 40
    price += " (тверда піна Цукерка) "
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == 'Про нас')
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="instagram - Kings_Bombs", url="https://instagram.com/kings_bombs_?utm_medium=copy_link"),
        types.InlineKeyboardButton(text="tik tok - Kings_Bombs", url="https://vm.tiktok.com/ZMLFrw4j8/")
    ]
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Наші сторінки в соц. мережах", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Корзина")
async def registration(message: types.Message):
    global price
    global suma
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Очистити","Замовити"
    ]
    keyboard.add(*buttons)
    await message.answer("Ви замовили: "+price+"\nна суму: "+str(suma), reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Очистити")
async def registration(message: types.Message):
    global price
    global suma
    global many
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))
    await bot.send_message(message.from_user.id, "Очищення...")
    price = ""
    many = 0
    suma = 0
    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

@dp.message_handler(lambda message: message.text == "Замовити")
async def registration(message: types.Message):
    global price
    global suma
    await bot.send_message(337646093, "====================================")
    await bot.send_message(337646093, "замовлення: " + price)
    await bot.send_message(337646093, "ціною: "+ str(suma))
    await bot.send_message(337646093, "@"+message.from_user.username)
    await bot.send_message(337646093, "====================================")

    await bot.send_message(message.from_user.id, "Ви замовили: "+price+"\nна суму: "+str(suma))

    await bot.send_message(367471403, "====================================")
    await bot.send_message(367471403, "замовлення: " + price)
    await bot.send_message(367471403, "ціною: "+ str(suma))
    await bot.send_message(367471403, "@"+message.from_user.username)
    await bot.send_message(367471403, "====================================")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "напиши /start")

if __name__ == '__main__':
    executor.start_polling(dp)