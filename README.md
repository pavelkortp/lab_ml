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

## 📁 Структура проекту

```
lab_ml/
├── main.py                      # Основний скрипт
├── heart.csv                    # Набір даних
├── requirements.txt             # Python залежності
├── .tool-versions              # Версія Python (asdf)
├── heart_failure_model.pkl     # Збережена модель (не в git)
├── heart_failure_experiment    # Експеримент PyCaret (не в git)
└── logs.log                    # Лог файли (не в git)
```

## 🔧 Основні бібліотеки

- **PyCaret** - AutoML бібліотека
- **Pandas** - Обробка даних
- **Scikit-learn** - ML алгоритми
- **Jupyter** - Інтерактивна розробка

## ⚠️ Важливо

- Використовуйте Python 3.11 (PyCaret не підтримує 3.12+)
- Всі залежності встановлюються через `requirements.txt`
- Модель та експеримент можна перегенерувати запуском `main.py`

## 📝 Ліцензія

MIT
