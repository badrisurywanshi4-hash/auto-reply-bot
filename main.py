import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "YOUR_BOT_TOKEN"

# ❤️ LOVE
love = [
"दिल की हर धड़कन में तेरा ही नाम बसता है,\nतू दूर है फिर भी हर एहसास तुझसे जुड़ता है।",
"तेरी मुस्कान ही मेरी पहचान बन गई,\nतू मिले या ना मिले, तू मेरी जान बन गई।",
"इश्क़ वो नहीं जो लफ़्ज़ों में बयान हो,\nइश्क़ वो है जो खामोशी में भी मेहरबान हो।",
"तेरे बिना ये दिल अधूरा सा लगता है,\nहर खुशी में भी एक दर्द सा लगता है।",
"तू सामने हो तो वक्त ठहर सा जाता है,\nतेरी आँखों में मेरा जहां बस जाता है।",
"तेरी यादों का सहारा ही काफी है,\nवरना ये दिल तो कब का टूट जाता है।",
"मोहब्बत नाम है तेरा हर एक सांस में,\nतू ही बसा है मेरे हर एहसास में।",
"तेरे बिना जीना अब मुमकिन नहीं लगता,\nतू ही मेरा सच, बाकी सब सपना लगता है।",
"तू मिले या ना मिले ये मुकद्दर की बात है,\nपर तुझे चाहना मेरी फितरत की बात है।",
"दिल चाहता है तुझे हर पल पास रखूं,\nतेरी हर खुशी को अपनी सांस रखूं।"
]

# 💔 SAD
sad = [
"टूट कर भी हम मुस्कुरा लेते हैं,\nदर्द दिल में छुपा कर जी लेते हैं।",
"जिसे चाहा वही बेवफा निकला,\nदिल का हर सपना अधूरा निकला।",
"आँखों में आँसू हैं पर कोई समझता नहीं,\nहम मुस्कुराते हैं पर कोई पढ़ता नहीं।",
"दर्द इतना है कि लफ़्ज़ कम पड़ जाते हैं,\nऔर हम खामोश रह जाते हैं।",
"जिसे अपना समझा वही पराया हो गया,\nदिल फिर एक बार तन्हा हो गया।",
"कभी जो अपना था अब अजनबी सा लगता है,\nदिल का हर कोना खाली सा लगता है।",
"रिश्ते भी अजीब होते हैं,\nजो दिल के करीब होते हैं वही दूर होते हैं।",
"हमने चाहा जिसे वो हमें समझ ना सका,\nऔर हम उसे कभी भूल ना सके।",
"खुश रहने की कोशिश में टूटते गए,\nऔर लोग हमें मजबूत समझते गए।",
"दिल अब किसी पर भरोसा नहीं करता,\nक्योंकि हर अपना ही दर्द देता है।"
]

# 🤝 FRIENDSHIP
friendship = [
"दोस्ती वो नहीं जो जान देती है,\nदोस्ती वो है जो हर दर्द में साथ देती है।",
"सच्चे दोस्त कभी दूर नहीं होते,\nदिल के रिश्ते कभी मजबूर नहीं होते।",
"तेरी मेरी दोस्ती सबसे खास है,\nये रिश्ता नहीं, एक एहसास है।",
"दोस्ती नाम है भरोसे का,\nजो हर हाल में साथ निभाता है।",
"हमारे जैसे दोस्त किस्मत से मिलते हैं,\nदिल से नहीं, नसीब से मिलते हैं।",
"दोस्ती में कोई शर्त नहीं होती,\nये वो मोहब्बत है जो खत्म नहीं होती।",
"तू साथ है तो सब आसान लगता है,\nवरना ये जहां सुनसान लगता है।",
"सच्चे दोस्त दर्द नहीं देखते,\nबस साथ खड़े रहते हैं।",
"दोस्ती वो है जो मुस्कान दे जाए,\nऔर आँसू को छुपा जाए।",
"हमारी दोस्ती हमेशा यूँ ही रहे,\nना कोई दूरी, ना कोई फासला रहे।"
]

# 🔥 MOTIVATION
motivation = [
"हार मत मानो अभी तो शुरुआत है,\nतेरी मेहनत में ही तेरी जीत की बात है।",
"रुकावटें सिर्फ तुम्हें मजबूत बनाने आती हैं,\nवरना रास्ते हमेशा आसान नहीं होते।",
"खुद पर भरोसा रख, तू कर सकता है,\nजो सोचा है वो तू हासिल कर सकता है।",
"अंधेरा कितना भी गहरा हो,\nसुबह जरूर आती है।",
"मेहनत करने वालों की कभी हार नहीं होती,\nकिस्मत भी उनके आगे झुकती है।",
"सपने वो नहीं जो नींद में आते हैं,\nसपने वो हैं जो नींद उड़ाते हैं।",
"रास्ते खुद बनते हैं चलने वालों के लिए,\nरुकने वालों के लिए नहीं।",
"तू कोशिश कर, मंज़िल खुद मिलेगी,\nतेरी मेहनत ही तुझे आगे ले जाएगी।",
"गिरना जरूरी है उठने के लिए,\nऔर लड़ना जरूरी है जीतने के लिए।",
"आज की मेहनत ही कल की ताकत है,\nइसलिए कभी रुकना मत।"
]

user_state = {}

def get_shayari(topic):
    return random.choice(topic)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["❤️ Love", "💔 Sad"],
        ["🤝 Friendship", "🔥 Motivation"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Aapka mood select karo 👇", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    user_id = update.message.chat_id

    if text in ["❤️ love", "💔 sad", "🤝 friendship", "🔥 motivation"]:
        user_state[user_id] = text.split()[1]

    elif text in ["next", "aur", "dobara", "another", "nhi pasand"]:
        pass

    topic = user_state.get(user_id, "love")

    if topic == "love":
        msg = get_shayari(love)
    elif topic == "sad":
        msg = get_shayari(sad)
    elif topic == "friendship":
        msg = get_shayari(friendship)
    else:
        msg = get_shayari(motivation)

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
