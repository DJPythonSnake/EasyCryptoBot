from ast import Try
from distutils.log import error
from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

TOKEN='enter the token'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

big_text = str("Что такое криптовалюта?\n\nНачать стоит с самого главного определения, на котором и будет строиться всё дальнейшее обучение. Что же такое криптовалюта? По сути, это виртуальные деньги, которые в отличие от фиатных средств не имеют физического выражения.Грубо говоря, электронные деньги – это реальные деньги, которые вы внесли на счет и они выражаются в виде цифр на вашем кошельке. Вы можете ими расплачиваться и можете вывести их. Криптовалюта, в свою очередь, представляет собой независимую систему самостоятельных электронных денег. Эти деньги эмитируются в сети и не имеют никакой связи с привычной валютой, никак не регулируются государством или любым другим органом.")
big_text1 = str("6 фактов, почему стоит заняться криптовалютой прямо сейчас \n\n1. Развитие криптовалюты находится на таком же уровне, как уровень развития интернета в 1993 году.\n2. Рыночная капитализация всей криптовалюты превысила такие платёжные системы как Visa и MasterCard.\n3. В Китае Bitcoin защищен национальными банками и правительством.\n4. Во многих банках развитых стран криптовалюту можно купить также, как и любую фиатную валюту.\n5. Несмотря на свою распространённость, 1000 человек владеет половиной общемировых объемов криптовалюты.\n6. Все криптовалютные транзакции никак не регулируются государством или любым другим органом.")
big_text2 = str("*Bitcoin* - отец крипты, самая старая и популярная валюта. От цены биткойна зависят большинство альткойнов \n\n*Альткойны* - все криптовалюты кроме биткойна\n\n*Stable Coin* - криптовалюта, которая равна 1 доллару, в простонародье криптодоллар. Их множество, но самая популярная Tether(USDT)\n\n*Shitcoin* или мем валюты - условное название для монет, которые имеют низкую капитализацию и неясные перспективы.\n\n*Кошелек*  — приложение для хранения криптовалюты. Есть кошельки в физическом виде и браузерного расширения\n\n*Киты* - инвесторы, владеющие достаточным количеством биткоинов, чтобы влиять на рынок самостоятельно. Обычно, к ним относят кошельки, на которых размещено более $50 млн.\n\n*Быки* - те, кто искусственно поднимают цену крипты\n\n*Медведи* - те, кто искусственно понижают цену крипты\n\n*Хомяк* — начинающий трейдер, которому свойственно принимать ошибочные решения из-за паники и эмоций.\n\nНа этом базовые термины для криптовалюты закончены. Погрузись в эту сферу и начни зарабатывать в перспективе больше своего препода. 😉")
big_text3 = str('🏛Лучшие биржи и криптокошельки🏛\n\nВыделим лучшие из бирж из кошельков.\n\n[Binance](www.binance.com/ru/activity/referral/offers/claim?ref=CPA_001FQIUX7Z) - молодая и быстро развивающаяся биржа. + Наибольшее количество объема торгов за сутки\n\n[Huobi](www.huobi.co.ma/ru-ru/v/register/double-invite/?invite_code=cqz75223&name=&avatar=&inviter_id=11345710) - биржа с 7 летним опытом, с десятками млн. пользователей, множество торговых пар.\n\n[Bybit](www.bybit.com/ru-RU/invite?ref=PKGBJY) - работает с 2018 года, предназначена для трейдинга. Подойдёт для людей из РБ. \n\nПочти на каждой бирже нужно пройти верификацию 18+. Как пройти верификацию смотрите в следующей статье.\n\n\nКриптокошельки📱\n\nИх существует довольно много, но лучшие из них… они👇\n\nMetamask - надежный криптокошелек, есть как приложение, так и расширение для браузера. поддерживает не все сети, удобен для дропов\n\nPhantom Wallet - дает доступ к блокчейну Solana, надёжный,  поддерживает не все блокчейны.')

special_button = KeyboardButton('Назад')

button1 = KeyboardButton('Хочу узнать о криптовалюте')
button2 = KeyboardButton('Начать обучение')
button3 = KeyboardButton('Давно занимаюсь этим')

guide_button = KeyboardButton('1. Что такое криптовалюта?')
guide_button1 = KeyboardButton('2. Крипто-терминология')

#nfo_button1 = KeyboardButton('@easyycryptoolearn')
#info_button2 = KeyboardButton('@easyycryptoo')
info_button3 = KeyboardButton('@easyycryptoo')

inline_kb_full = InlineKeyboardMarkup(row_width=1)
inline_kb_guide = InlineKeyboardMarkup(row_width=1)
extra_inline_kb_full = InlineKeyboardMarkup(row_width=1)

inline_btn_1 = InlineKeyboardButton(text='Начать обучение', url='https://t.me/easyycryptoolearn',callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_guide_btn = InlineKeyboardButton(text='1. Что такое криптовалюта?', callback_data="print_text")
inline_guide_btn1 = InlineKeyboardButton(text='2. Интересные факты о криптовалюте', callback_data="print_text1")
inline_guide_btn2 = InlineKeyboardButton(text='3. Крипто-терминология', callback_data="print_text2")
inline_guide_btn3 = InlineKeyboardButton(text='4. Лучшие биржи и криптокошельки', callback_data="print_text3")

inline_btn_3 = InlineKeyboardButton('Основной канал', url='https://t.me/easyycryptoo', callback_data='button1')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)

inline_kb_full.add(inline_btn_1, inline_btn_3)
inline_kb_guide.add(inline_guide_btn, inline_guide_btn1, inline_guide_btn2, inline_guide_btn3)
extra_inline_kb_full.add(inline_btn_3)

#greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
#greet_kb.add(button1, button2, button3)

markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button3)
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button2).add(special_button)
guide_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(guide_button).add(guide_button1)
#info_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(info_button1).add(info_button2).add(special_button)
extra_info_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(special_button)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("💸Приветствуем вас на канале EasyCrypto!💸\nДля продолжения выберите соответствующий вам вариант:", reply_markup=markup)

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("💸Приветствуем вас на канале EasyCrypto!💸\nДля продолжения выберите соответствующий вам вариант:", reply_markup=markup)

@dp.message_handler(Text(equals="Назад"))
async def with_puree(message: types.Message):
    await message.reply("Выберите один из вариантов", reply_markup=markup)

@dp.message_handler(Text(equals="Хочу узнать о криптовалюте"))
async def with_puree(message: types.Message):
    await message.reply("Выберите один из вариантов", reply_markup=markup1)

@dp.message_handler(Text(equals="Начать обучение"))
async def with_puree(message: types.Message):
    await message.reply("Выберите одну из статей", reply_markup=inline_kb_guide)

@dp.callback_query_handler(text="print_text")
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, text=big_text)

@dp.callback_query_handler(text="print_text1")
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, text=big_text1)

@dp.callback_query_handler(text="print_text2")
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, text=big_text2, parse_mode='Markdown')

@dp.callback_query_handler(text="print_text3")
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, text=big_text3, parse_mode='Markdown', disable_web_page_preview=True)

@dp.message_handler(Text(equals="Давно занимаюсь этим"))
async def with_puree(message: types.Message):
    await message.reply("Добро пожаловать на основной канал", reply_markup=extra_inline_kb_full)


if __name__ == '__main__':
    try:
        print("Starting crypto-bot...")
    except error as e:
        print(e)
    else:
        print("Success")
 
    executor.start_polling(dp)
