
greetings = {
    "Italian":      "Ciao mondo",
    "Irish":        "Dia duit Domhanda",
    "French":       "Bonjour le monde",
    "English":      "Hello World",
    "Australian":   "G'day World",
    "German":       "Hallo Welt",
    "Hungarian":    "Helló Világ",
    "Czech":        "Ahoj světe",
    "Dutch":        "Hallo Wereld",
    "Danish":       "Hej Verden",
    "Swedish":      "Hej världen",
    "Lithuanian":   "Labas pasauli",
    "Latin":        "salve Orbis Terrarum",
    "Spanish" :     "Hola Mundo",
    "Catalan" :     "Hola món",
    "Hawaiian":     "Aloha kākou honua",

    "Afrikaans":    "Hello Wêreld",
    "Swahili" :     "Salamu, Dunia",
    "Zulu":         "Sawubona Mhlaba",

    "Greek":        "Γειά σου Κόσμε",

    "Uyghur":       "ياخشىمۇسىز دۇنيا",
    "Urdu":         "ہیلو ورلڈ",
    "Arabic":       "مرحبا بالعالم",
    "Sindhi":       "هيلو ورلڊ",
    "Hebrew":       "שלום עולם",
    "Yiddish":      "העלא וועלט",
    "Armenian":     "Բարեւ աշխարհ",

    "Mongolian":    "Сайн уу",
    "Chinese":      "你好，世界",
    "Korean":       "안녕 세상",
    "Japanese":     "こんにちは世界",
    "Vietnamese":   "Chào thế giới",
    "Lao":          "ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ",
    "Burmese":      "မင်္ဂလာပါကမ္ဘာလောက",
    "Thai":         "สวัสดีชาวโลก",
    "Telugu":       "హలో వరల్డ్",

    "Hindi" :       "नमस्ते दुनिया",
    "Tamil":        "ஹலோ வேர்ல்ட்",
    "Gujarati":     "હેલો વર્લ્ડ",
    "Nepali":       "नमस्कार संसार",
    "Marathi":      "हॅलो वर्ल्ड",
    "Malayalam":    "ഹലോ വേൾഡ്",
    "Bangla":       "ওহে বিশ্ব",
    "Kannada":      "ಹಲೋ ವರ್ಲ್ಡ್",
    "Sinhala":      "හෙලෝ වර්ල්ඩ්",

    "Russian":      "Привет, мир",
    "Kyrgyz":       "салам дүйнө",
    "Ukranian":     "Привіт Світ",
    "Bulgarian":    "Здравей свят",
    "Macedonian":   "Здраво свету",
    "Tajik":        "Салом Ҷаҳон",
    "Tatar" :       "Сәлам, Дөнья",

    "Uzbek":        "Salom Dunyo",
    "Polish":       "Witaj świecie",
    "Georgian":     "Გამარჯობა მსოფლიო",

}

def main():
    for lang in greetings:
        message = greetings[lang]
        l = len(message)
        print("Howdy", l, lang, message)
        #for c in message:
        #    print ("character:", c)

main()
