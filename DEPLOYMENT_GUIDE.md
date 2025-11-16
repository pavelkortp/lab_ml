# 🚀 Інструкція по деплою веб-застосунку

## 🎯 Мета
Зробити застосунок доступним для всіх через інтернет (безкоштовно!)

---

## ✅ Варіант 1: Render (РЕКОМЕНДОВАНО)

### Чому Render?
- ✅ **Безкоштовно** (з обмеженнями)
- ✅ Простий у налаштуванні
- ✅ Автоматичний деплой з GitHub
- ✅ HTTPS включено
- ⚠️ "Засинає" після 15 хв неактивності (перший запуск буде повільним)

### Крок 1: Підготовка проекту ✅

Все вже готово! У вас є:
- ✅ `requirements.txt` - залежності
- ✅ `render.yaml` - конфігурація Render
- ✅ `Procfile` - команда запуску
- ✅ `app.py` - оновлений для продакшн

### Крок 2: Завантажте код на GitHub

```bash
# Ініціалізуйте git (якщо ще не зробили)
git init

# Додайте файли
git add .

# Зробіть комміт
git commit -m "Ready for deployment"

# Створіть репозиторій на GitHub
# Потім підключіть його:
git remote add origin https://github.com/pavelkortp/lab_ml.git
git branch -M main
git push -u origin main
```

### Крок 3: Деплой на Render

1. **Зареєструйтесь на Render**
   - Перейдіть на https://render.com
   - Натисніть "Get Started for Free"
   - Увійдіть через GitHub

2. **Створіть новий Web Service**
   - Натисніть "New +" → "Web Service"
   - Оберіть ваш репозиторій `lab_ml`
   - Натисніть "Connect"

3. **Налаштуйте деплой**
   ```
   Name: heart-disease-prediction (або будь-яка назва)
   Environment: Python
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free
   ```

4. **Натисніть "Create Web Service"**

5. **Зачекайте 5-10 хвилин** 
   - Render встановить залежності
   - Запустить ваш застосунок
   - Ви побачите URL типу: `https://heart-disease-prediction.onrender.com`

### Крок 4: Готово! 🎉

Ваш застосунок доступний за адресою типу:
```
https://ваша-назва.onrender.com
```

Поділіться цим URL з ким завгодно!

---

## 🔧 Варіант 2: Railway

### Чому Railway?
- ✅ Безкоштовно (500 годин/місяць)
- ✅ Швидший за Render
- ✅ Не "засинає"
- ✅ Простий деплой

### Кроки:

1. **Зареєструйтесь на Railway**
   - https://railway.app
   - Увійдіть через GitHub

2. **Створіть новий проект**
   - "New Project" → "Deploy from GitHub repo"
   - Оберіть `lab_ml`

3. **Railway автоматично**:
   - Знайде `requirements.txt`
   - Встановить залежності
   - Запустить через `Procfile`

4. **Отримайте URL**
   - Settings → Domains → Generate Domain
   - Ваш URL: `https://ваш-проект.up.railway.app`

---

## 🌐 Варіант 3: PythonAnywhere (найпростіший!)

### Чому PythonAnywhere?
- ✅ Спеціалізований на Python
- ✅ Безкоштовний план
- ✅ Завжди активний (не засинає)
- ⚠️ Обмеження: лише HTTP (не HTTPS на безкоштовному)

### Кроки:

1. **Зареєструйтесь**
   - https://www.pythonanywhere.com
   - "Create a Beginner account" (безкоштовно)

2. **Завантажте код**
   ```bash
   # У консолі PythonAnywhere:
   git clone https://github.com/ВАШ_ЮЗЕРНЕЙМ/lab_ml.git
   cd lab_ml
   ```

3. **Встановіть залежності**
   ```bash
   pip install --user -r requirements.txt
   ```

4. **Налаштуйте Web App**
   - Web → Add a new web app
   - Manual configuration → Python 3.11
   - WSGI файл: вкажіть шлях до `app.py`

5. **URL**: `http://ваш-юзернейм.pythonanywhere.com`

---

## 🎯 Що обрати?

| Платформа | Переваги | Недоліки | Рекомендація |
|-----------|----------|----------|--------------|
| **Render** | Простий, HTTPS | Засинає | ⭐⭐⭐⭐⭐ Найкраще для початку |
| **Railway** | Швидкий, не засинає | Ліміт 500 год/міс | ⭐⭐⭐⭐ Гарна альтернатива |
| **PythonAnywhere** | Завжди активний | Тільки HTTP | ⭐⭐⭐ Для простих проектів |

---

## 📝 Після деплою

### Перевірте чи працює:

1. Відкрийте ваш URL у браузері
2. Введіть тестові дані (з `QUICK_DEMO.txt`)
3. Перевірте чи працює передбачення

### Поширіть посилання:

```
🫀 Перевірте ризик серцевих захворювань:
https://ваш-домен.onrender.com

Використовує ML з точністю 87%!
```

---

## 🐛 Можливі проблеми

### "Application failed to start"

**Проблема:** Модель не завантажується

**Рішення:** Переконайтесь що `heart_failure_model.pkl` є в репозиторії:
```bash
git add heart_failure_model.pkl
git commit -m "Add model file"
git push
```

### "ModuleNotFoundError"

**Проблема:** Не всі залежності встановлені

**Рішення:** Перевірте `requirements.txt`:
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Повільне завантаження на Render

**Це нормально!** Безкоштовний план "засинає" після 15 хв.
Перше завантаження може зайняти 30-60 секунд.

---

## 🔄 Оновлення застосунку

Після змін у коді:

```bash
git add .
git commit -m "Опис змін"
git push
```

Render автоматично передеплоїть застосунок за 2-3 хвилини!

---

## 💰 Безкоштовні обмеження

### Render Free:
- ✅ 750 годин/місяць
- ✅ 512 MB RAM
- ⚠️ Засинає після 15 хв
- ✅ HTTPS

### Railway Free:
- ✅ 500 годин/місяць
- ✅ 512 MB RAM
- ✅ $5 кредитів
- ✅ HTTPS

### PythonAnywhere Free:
- ✅ Завжди активний
- ✅ 512 MB RAM
- ⚠️ Тільки HTTP
- ⚠️ Повільніший

---

## 🎉 Готово!

Тепер ваш ML застосунок доступний всьому світу!

**Приклад готового URL:**
```
https://heart-disease-prediction.onrender.com
```

### Наступні кроки:
1. 📱 Поділіться URL з друзями/колегами
2. 📊 Збирайте фідбек
3. 🔧 Покращуйте модель
4. 🚀 Додайте нові фічі!

---

**Створено з ❤️ для доступного ML**

*Питання? Проблеми? Перевірте логи на платформі деплою!*

