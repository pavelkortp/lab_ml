# ✅ Чеклист перед деплоєм

Перевірте що все готово перед деплоєм:

## 📦 Файли для деплою

- [x] `app.py` - Flask застосунок
- [x] `requirements.txt` - Всі залежності (включно з gunicorn)
- [x] `Procfile` - Команда запуску
- [x] `render.yaml` - Конфігурація Render
- [x] `runtime.txt` - Версія Python
- [x] `heart_failure_model.pkl` - Натренована модель
- [x] `templates/index.html` - HTML інтерфейс
- [x] `.gitignore` - Правильно налаштований

## 🔍 Перевірка перед деплоєм

### 1. Локальне тестування

```bash
# Запустіть локально
python app.py

# Відкрийте http://localhost:8080
# Перевірте що все працює
```

**Що перевірити:**
- [ ] Сторінка відкривається
- [ ] Форма відображається коректно
- [ ] Можна ввести дані
- [ ] Передбачення працює (спробуйте QUICK_DEMO.txt)
- [ ] Результат відображається правильно

### 2. Перевірка файлів

```bash
# Перевірте чи є всі файли
ls -la | grep -E "(app.py|requirements|Procfile|render.yaml|model.pkl)"

# Перевірте розмір моделі (має бути ~13 KB)
ls -lh heart_failure_model.pkl
```

### 3. Git репозиторій

```bash
# Перевірте статус
git status

# Переконайтесь що модель НЕ в .gitignore
cat .gitignore | grep model
# Має бути закоментовано: # heart_failure_model.pkl

# Перевірте що модель буде додана
git add heart_failure_model.pkl
git status
```

## 🚀 Готовність до деплою

### Базові вимоги:
- [ ] Python 3.11 у `runtime.txt`
- [ ] Flask + gunicorn у `requirements.txt`
- [ ] `app.py` працює локально
- [ ] Модель завантажується без помилок
- [ ] HTML інтерфейс відображається

### Git:
- [ ] Репозиторій створено на GitHub
- [ ] Всі файли закоммічено
- [ ] Модель включена в репозиторій
- [ ] `.gitignore` правильно налаштований

### Render конфігурація:
- [ ] `render.yaml` створено
- [ ] `Procfile` створено
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app`

## 📋 Команди для деплою

```bash
# 1. Фінальна перевірка
python app.py  # Має працювати локально

# 2. Комміт всіх змін
git add .
git status  # Перевірте що все включено
git commit -m "🚀 Ready for production deployment"

# 3. Пуш на GitHub
git push origin main

# 4. Деплой на Render
# Перейдіть на render.com і слідуйте QUICK_DEPLOY.md
```

## 🎯 Після деплою

### Перевірте на продакшні:
- [ ] Сайт відкривається за URL
- [ ] Інтерфейс відображається коректно
- [ ] Форма працює
- [ ] Передбачення працює правильно
- [ ] Немає помилок у логах Render

### Тестові дані:
```bash
# Використайте дані з QUICK_DEMO.txt
cat QUICK_DEMO.txt

# Спробуйте обидва сценарії:
# 1. Низький ризик
# 2. Високий ризик
```

## 🐛 Якщо щось не працює

### Перевірте логи на Render:
1. Відкрийте Dashboard на render.com
2. Знайдіть ваш сервіс
3. Перейдіть у "Logs"
4. Шукайте червоні повідомлення про помилки

### Типові проблеми:

**"ModuleNotFoundError"**
```bash
# Оновіть requirements.txt
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

**"Model not found"**
```bash
# Переконайтесь що модель у репозиторії
git add heart_failure_model.pkl -f
git commit -m "Add model file"
git push
```

**"Application error"**
```bash
# Перевірте app.py локально
python app.py
# Якщо працює локально - перевірте логи на Render
```

## 📱 Поширення

Коли все працює:

```
🫀 Перевірте ризик серцевих захворювань:
https://ваш-сервіс.onrender.com

🤖 ML модель з точністю 87%
⚡ Миттєві результати
🔒 Безпечно і конфіденційно
```

---

## ✅ Фінальний чеклист

Перед тим як поділитися з іншими:

- [ ] ✅ Сайт відкривається
- [ ] ✅ Форма працює
- [ ] ✅ Передбачення точні
- [ ] ✅ Дизайн виглядає добре
- [ ] ✅ Працює на мобільних
- [ ] ✅ Немає помилок у логах
- [ ] ✅ URL легко запам'ятовується

---

**Готово! 🎉 Ваш ML застосунок у продакшні!**

*Детальніше: [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)*

