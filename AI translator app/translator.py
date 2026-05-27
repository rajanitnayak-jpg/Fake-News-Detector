from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")

target_lang = input("Enter target language code (hi, fr, es, kn): ")

translated = translator.translate(text, dest=target_lang)

print("\nTranslated Text:")
print(translated.text)