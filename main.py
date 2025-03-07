import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from pathlib import Path

API_TOKEN = "7403622075:AAHDTMnilPHWk7ySa43eiMxAXjoUKTacfgk"

bot = Bot(token=API_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
mytelegramid = "5482330178"
janarteltgramid = []
usernum = 0

questions = [
    "Адам аттан неге құлайды?",
    "Өмір – бұл театр, ал адамдар оның әртістері. ? ",
    "🎩🔍 Бұл сериал менің ең сүйікті сериал десем де болады, тауып көрші?",
    "Сөзжұмбақ: Ж _ _ E_ _",
    "Сөзжұмбақ: 💮 🐁 ",
    "'Үлкен аға сені бақылап тұр' кітаптың есмін тауып көрші ?",
    "Егер спектакль жүріп жатқанда өмірді қайта бастайтындай болып егіліп жылап, сахна жабылған кезде мыжырайған бас киімін киіп алып, бұрынғы таз қалпына қайта түсетін көрермен секілді болсаң, онда сен үшін шындык өмірлік мақсат емес, анда-санда бір шарпып өтетін көңілдің серпілісі ғана.",
    "Синонимдес сөзді тап? От, көз, алтын, тау  _____"]
answers = [
    "Жерге. Қазір Жердің айналу жылдамдығы сағатына 1670 км, бірақ біз оны сезбейміз, өйткені атмосфера бізбен бірге қозғалады.",
    "Уильям Шекспирдің философиялық көзқарасын білдіреді.",
    "✅ Дұрыс! Бұл - 'Шерлок'. Артур Конан Дойл Холмстың бейнесін жасау үшін доктор Джозеф Беллден шабыт алған.",
    "✅ Дұрыс Жүрек Адам жүрегі өмір бойы 3 миллиард рет соғады! 🔄 Ал бір күнде ол 100 000 рет соғып" ,
    "Альджернонға арналған гүлдер",
    "1984",
    "Төлен Әбдік",
    "Жанар – оттай ыстық, көздей өткір, алтындай қымбат, таудай асқақ есім!"
]

jokes = [
    "Егер Жер бірден тоқтап қалса, аттан емес, тікелей орбитадан құлаймыз... 😅",
    "Егер өмір шынымен театр болса, сен ең басты рөлдегі кейіпкерсің... ал мен сенің ең адал көрерменіңмін.",
    "Мен де сенің көзқарасыңды, қимылдарыңды бақылап, сені зерттеп отырмын... (Шерлок сияқты!) 😏",
    "бірақ кейбір жағдайларда ол қалыптан тыс соғуы мүмкін…  Мысалы, біреу қызықты викторина жасап жатса... немесе бір ерекше адаммен сөйлесіп отырса.😏",
    "Егер мен Чарли сияқты бәрін жоғалтып алсам да, мен сені ұмытпас едім 🥀💖",
    "Үлкен аға емес, мен сені бақылап тұрмын... ",
    "Егер өмір шынымен спектакль болса, мен үшін ең әсерлі сахна – сенің жаныңда болған сәттер. 🎭❤️"  ,
    "Және бұл викторина – жай ғана ойын емес, сен үшін арнайы дайындалған ерекше сыйлық! 🎁✨"
]

realanswers = ["жерге", "шекспир", "шерлок", "жүрек" , "Альджернонға арналған гүлдер", "1984", "Төлен Әбдік", "жанар"]
class QuizState(StatesGroup):
    level = State()
    score = State()
    client = State()

@dp.message(Command("sendtozh"))
async def send(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Қандай хабарлама жіберу керек? (мәтін, видео, аудио, т.б.)")
    await state.set_state(QuizState.client)

@dp.message(QuizState.client)
async def handle_sendmessage(message: Message, state: FSMContext):
    if not janarteltgramid:
        await message.answer("Хабарлама жіберетін адамдар жоқ!")
    else:
        # Если сообщение содержит текст
        if message.text:
            for chat_id in janarteltgramid:
                await bot.send_message(chat_id, message.text)
            await message.answer("Хабарлама сәтті жіберілді! ✅")

        # Если сообщение содержит видео
        elif message.video:
            for chat_id in janarteltgramid:
                await bot.send_video(chat_id, message.video.file_id)
            await message.answer("Видео сәтті жіберілді! ✅")

        # Если сообщение содержит аудио
        elif message.audio:
            for chat_id in janarteltgramid:
                await bot.send_audio(chat_id, message.audio.file_id)
            await message.answer("Аудио сәтті жіберілді! ✅")

        # Если сообщение содержит голосовое сообщение
        elif message.voice:
            for chat_id in janarteltgramid:
                await bot.send_voice(chat_id, message.voice.file_id)
            await message.answer("Голосовое сообщение сәтті жіберілді! ✅")

    await state.clear()


@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    global usernum
    buttons = InlineKeyboardBuilder()
    buttons.button(text="Ойынды бастау", callback_data="startgame")



    text = """
       🌸 <b>Сәлем, Жанар!</b> 🌸\n
       Бүгін – ерекше күн, өйткені бұл сенің мейрамың! 💖\n
       <b>8 НАУРЫЗ ҚҰТТЫ БОЛСЫН!</b> 🎉\n
       ✨ Сен – әдемісің, мейірімдісің, ерекше жансың!\n
       Сен туралы қызықты викторина дайындалды! 🎁\n
       🎯 Дайын болсаң, төмендегі <b>"Ойынды бастау"</b> түймесін бас!
       """


    janarteltgramid.append(message.chat.id)
    usernum += 1

    await message.answer(text, reply_markup=buttons.as_markup() , parse_mode="HTML")




@dp.callback_query(lambda c: c.data == "startgame")
async def startgame(callbackquery: CallbackQuery, state: FSMContext):
    await callbackquery.message.answer(
        "✨ <b>Ойын шарты:</b> ✨\n"
        "✅ Әр дұрыс жауап үшін – <b>1 ұпай</b> 🎉\n"
        "❌ Қате жауап үшін – <b>-0.3 ұпай</b> 😅\n"
        "🎯 <b>Мақсат:</b> 5.5 ұпай жинау! 💪\n"
        "🎁 Егер сен жеңсең – мен сенің <b>бір қалауыңды</b> орындаймын! 😉\n"
        "😏 Бірақ егер сен жеңілсең... онда менің <b>шартымды</b> орындауың керек! 🤭\n"
        "🔥 <b>Дайынсың ба? Онда бастайық!</b> 🔥"
     , parse_mode="HTML")

    buttons = InlineKeyboardBuilder()
    buttons.button(text="Гоу", callback_data="go")
    await callbackquery.message.answer("Дайын болсаң, бастайық!", reply_markup=buttons.as_markup())





answerof4 = ["р", "ү", "к"]

@dp.message(lambda m: m.text)
async def check_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    level = data.get("level", 0)
    score = data.get("score", 0)
    count4 = data.get("count4", 0)

    if level >= len(questions):
        await message.answer(f"🎉 Ойын аяқталды! Барлық сұрақтарға дұрыс жауап бердің! Жалпы ұпай: {score} 🎉")
        return

    text = message.text.lower().strip()

    if text == realanswers[level].lower().strip():
        score += 1
        await state.update_data(score=score)
        await message.answer(f"<i>{answers[level]}</i>" , parse_mode="HTML")
        await message.answer(f"<i>{jokes[level]}</i>" , parse_mode="HTML")
        await bot.send_message(mytelegramid, f"Pass {level + 1} level ✅ \n Ұпайың {score}")

        if level + 1 < len(questions):
            await state.update_data(level=level + 1)
            await message.answer(f"<b>{questions[level + 1]}</b>" ,parse_mode="HTML")
        else:
            await message.answer(f"🎉 Ойын аяқталды! Жалпы ұпай: {score} 🎉")

            if(score > 5.5):
                await message.answer(f"🎉 Сен ұттың сенің бір шартыңды орындаймын {score} ")
                await bot.send_message( mytelegramid,f"🎉  Сен ұттың! 🏆 Сенің бір шартыңды орындаймын! ✅ {score} 🎉")

            else:
                await message.answer(f"🎉  Сен ұтылып қалдың! 😜 Сен менің бір шартымды орындайсың! ✅{score} 🎉")
                await bot.send_message(mytelegramid, f"🎉 Сен ұттың сенің бір шартыңды орындаймын {score} ")

            audio = FSInputFile("whats.ogg")  # Открытие файла для передачи
            await message.answer_audio(audio)
            await asyncio.sleep(1)
            buttons = InlineKeyboardBuilder()
            buttons.button("Иә"  , callback_data="yes")
            buttons.button("Жоқ"  , callback_data="no")
            await message.answer("Ұнады ма ?"   ,reply_markup=buttons.as_markup())



    else:
        score -= 0.3
        await state.update_data(score=score)
        await message.answer(f"Қате жауап ❌ \n Ұпайың {score}")

        if level == 3:
            if count4 < len(answerof4):
                await message.answer(f"Cөзде тағы '{answerof4[count4]}' әріпі бар")
                await state.update_data(count4=count4 + 1)
            else:
                await message.answer("Сен барлық әріптерді көрдің! Енді толық жауапты ойлан! 🤔")

        await bot.send_message(mytelegramid, f"didn't pass level {level + 1}: {text}")


@dp.callback_query(lambda c: c.data in ["yes", "no" ,"go"])
async def go_game(callbackquery: CallbackQuery, state: FSMContext):
    if(callbackquery.data.startswith("yes")):
        audio = FSInputFile("yes.ogg")  # Открытие файла для передачи
        await bot.send_message(mytelegramid, "Толығымен аяқталды yes басып аудио тындады")
        await callbackquery.message.answer_audio(audio)
    elif(callbackquery.data.startswith("no")):
        await callbackquery.message.answer("Келесі жолы бұдан да жақсырақ тырысамын! 💪😊")
        await bot.send_message(mytelegramid, "Толығымен аяқталды жок басты")
    elif(callbackquery.data.startswith("go")):
        await state.set_state(QuizState.level)
        await state.update_data(level=0, score=0)
        await callbackquery.message.answer(questions[0])



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
