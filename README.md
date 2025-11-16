# Heart Disease Prediction - ML Project

Проект машинного навчання для передбачення серцевої недостатності за допомогою PyCaret.

## 📋 Вимоги

- Python 3.11 (рекомендовано 3.11.14)
- pip

## 🚀 Встановлення

1. **Клонуйте репозиторій:**
```bash
git clone <your-repo-url>
cd lab_ml
```

2. **Створіть віртуальне середовище:**
```bash
python3.11 -m venv venv
```

3. **Активуйте віртуальне середовище:**
```bash
# На macOS/Linux:
source venv/bin/activate

# На Windows:
venv\Scripts\activate
```

4. **Встановіть залежності:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📊 Використання

### Варіант 1: Тренування моделі

Запустіть основний скрипт:
```bash
python main.py
```

Скрипт виконає:
- Завантаження даних з `heart.csv`
- Налаштування експерименту PyCaret
- Порівняння моделей ML
- Тюнінг найкращої моделі
- Збереження моделі у `heart_failure_model.pkl`

### Варіант 2: 🌐 Веб-застосунок

Запустіть Flask застосунок:
```bash
python app.py
```

Потім відкрийте у браузері: `http://localhost:8080`

Веб-застосунок дозволяє:
- ✅ Ввести дані пацієнта через зручну форму
- ✅ Отримати миттєве передбачення ризику
- ✅ Побачити рекомендації
- ✅ Використовувати з будь-якого пристрою

Детальніше: [WEB_APP_README.md](WEB_APP_README.md)

## 📁 Структура проекту

```
lab_ml/
├── app.py                             # 🌐 Flask веб-застосунок
├── main.py                            # 🔧 Скрипт тренування моделі
├── heart.csv                          # 📊 Набір даних
├── requirements.txt                   # 📦 Python залежності
├── .tool-versions                     # 🐍 Версія Python (asdf)
├── heart_disease_prediction.ipynb     # 📓 Jupyter notebook
├── templates/
│   └── index.html                     # 🎨 HTML інтерфейс
├── heart_failure_model.pkl            # 🤖 Збережена модель (не в git)
├── heart_failure_experiment           # 🔬 Експеримент PyCaret (не в git)
├── WEB_APP_README.md                  # 📖 Документація веб-застосунку
└── logs.log                           # 📝 Лог файли (не в git)
```

## 🔧 Основні бібліотеки

- **PyCaret** - AutoML бібліотека
- **Flask** - Веб-фреймворк для застосунку
- **Pandas** - Обробка даних
- **Scikit-learn** - ML алгоритми
- **Jupyter** - Інтерактивна розробка

## ⚠️ Важливо

- Використовуйте Python 3.11 (PyCaret не підтримує 3.12+)
- Всі залежності встановлюються через `requirements.txt`
- Модель та експеримент можна перегенерувати запуском `main.py`

## 🚀 Деплой у продакшн

Хочете зробити застосунок доступним для всіх через інтернет?

### Швидкий старт:
```bash
# 1. Завантажте на GitHub
git add .
git commit -m "Ready for deployment"
git push

# 2. Деплойте на Render (безкоштовно)
# Детальна інструкція: QUICK_DEPLOY.md
```

**Платформи для деплою:**
- ⭐ [Render](https://render.com) - Рекомендовано (безкоштовно)
- 🚂 [Railway](https://railway.app) - Швидкий (безкоштовно)
- 🐍 [PythonAnywhere](https://pythonanywhere.com) - Простий

**Документація:**
- 📖 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Повна інструкція
- ⚡ [QUICK_DEPLOY.md](QUICK_DEPLOY.md) - Швидкий деплой за 5 хвилин

**Приклад готового URL:**
```
https://heart-disease-prediction.onrender.com
```

---

## 📝 Ліцензія

MIT
