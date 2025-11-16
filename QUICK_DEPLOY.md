# ⚡ Швидкий деплой за 5 хвилин

## 🎯 Найпростіший спосіб: Render

### Крок 1: Завантажте на GitHub (2 хв)

```bash
# Якщо ще не зробили git init:
git init
git add .
git commit -m "🚀 Ready for deployment"

# Створіть репозиторій на GitHub.com, потім:
git remote add origin https://github.com/ВАШ_ЮЗЕРНЕЙМ/lab_ml.git
git branch -M main
git push -u origin main
```

### Крок 2: Деплой на Render (3 хв)

1. 🌐 Відкрийте: https://render.com
2. 🔐 Натисніть **"Get Started for Free"** → Увійдіть через GitHub
3. ➕ Натисніть **"New +"** → **"Web Service"**
4. 🔍 Знайдіть та оберіть ваш репозиторій **`lab_ml`**
5. ⚙️ Налаштування:
   ```
   Name: heart-disease-prediction
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Plan: Free
   ```
6. ✅ Натисніть **"Create Web Service"**

### Крок 3: Зачекайте ☕

- Render встановить залежності (~5-7 хвилин)
- Після завершення отримаєте URL типу:
  ```
  https://heart-disease-prediction.onrender.com
  ```

### Крок 4: Готово! 🎉

Відкрийте URL і перевірте чи працює!

---

## 📱 Поділіться посиланням:

```
🫀 Перевірте ризик серцевих захворювань:
https://heart-disease-prediction.onrender.com

ML модель з точністю 87%!
```

---

## 🔄 Як оновити після змін:

```bash
git add .
git commit -m "Опис змін"
git push
```

Render автоматично передеплоїть! ⚡

---

## ⚠️ Важливо знати:

- Безкоштовний план "засинає" після 15 хв неактивності
- Перше завантаження буде ~30 секунд
- Це нормально! ✅

---

## 🐛 Проблеми?

1. **Модель не завантажується:**
   ```bash
   git add heart_failure_model.pkl -f
   git commit -m "Add model"
   git push
   ```

2. **Помилка залежностей:**
   ```bash
   pip freeze > requirements.txt
   git add requirements.txt
   git commit -m "Update deps"
   git push
   ```

3. **Дивіться логи на Render:**
   - Dashboard → Ваш Service → Logs

---

**Детальніше:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

