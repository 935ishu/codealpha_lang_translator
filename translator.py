from deep_translator import GoogleTranslator

print("🌍 Welcome to Language Translator!")
text = input("Enter text to translate: ")
target_lang = input("Enter target language (e.g., te for Telugu, hi for Hindi, fr for French): ")

try:
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    print(f"\n✅ Translated Text: {translated}")
except Exception as e:
    print("❌ Error:", e)