#!/bin/bash

echo "🚀 Запуск веб-застосунку для передбачення серцевих захворювань..."
echo ""

# Активуємо віртуальне середовище
source venv/bin/activate

# Перевіряємо чи є модель
if [ ! -f "heart_failure_model.pkl" ]; then
    echo "⚠️  Модель не знайдена!"
    echo "Спочатку натренуйте модель: python main.py"
    exit 1
fi

echo "✅ Модель знайдена"
echo "📍 Веб-застосунок буде доступний за адресою: http://localhost:8080"
echo ""
echo "⏹️  Для зупинки натисніть Ctrl+C"
echo ""

# Запускаємо Flask
python app.py

