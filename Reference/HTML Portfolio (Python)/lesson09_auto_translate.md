# Lesson 9: Automatic Traditional Chinese Translation

## 🎯 Learning Objectives:
- Install deep-translator library
- Use automatic translation
- Add Traditional Chinese (繁體中文)
- Create bilingual website

## 📝 What Students Do:

### Step 1: Install Library
```bash
pip install deep-translator
```

### Step 2: Import and Setup
```python
from deep_translator import GoogleTranslator

def translate(text):
    try:
        translator = GoogleTranslator(source='en', target='zh-TW')
        return translator.translate(text)
    except:
        return text
```

### Step 3: Translation Functions
```python
def t(text):
    """Translate English to Traditional Chinese"""
    return translate(text)

def b(text):
    """Bilingual: Chinese + English"""
    chinese = translate(text)
    return f"{chinese} {text}"
```

### Step 4: Use in HTML
```python
<h1>{t("Welcome to My Portfolio")}</h1>
<h1>Welcome to My Portfolio</h1>

<a href="/">{b("Home")}</a>
# Displays: "主頁 Home"
```

## 🌐 Language Codes:
- **zh-TW**: Traditional Chinese (繁體中文) ✅ Use this!
- **zh-CN**: Simplified Chinese (简体中文)
- **en**: English

## ✅ Deliverable:
- Bilingual website (繁體中文 + English)
- Automatic translation working
- No manual Chinese typing needed!

## 💡 Key Benefits:
- ✅ No need to type Chinese characters
- ✅ Any English text auto-translates
- ✅ Consistent translations
- ✅ Easy to update content

## 🔗 Leads to:
Lesson 10 - About Me page with bilingual content
