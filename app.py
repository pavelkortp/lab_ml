from flask import Flask, render_template, request, jsonify
import pandas as pd
from pycaret.classification import load_model
import os

app = Flask(__name__)

# Завантажуємо модель при старті застосунку
model = load_model("heart_failure_model")


@app.route("/")
def home():
    """Головна сторінка"""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Обробка даних та передбачення"""
    try:
        # Отримуємо дані з форми
        data = {
            "Age": [int(request.form["age"])],
            "Sex": [request.form["sex"]],
            "ChestPainType": [request.form["chest_pain"]],
            "RestingBP": [int(request.form["resting_bp"])],
            "Cholesterol": [int(request.form["cholesterol"])],
            "FastingBS": [int(request.form["fasting_bs"])],
            "RestingECG": [request.form["resting_ecg"]],
            "MaxHR": [int(request.form["max_hr"])],
            "ExerciseAngina": [request.form["exercise_angina"]],
            "Oldpeak": [float(request.form["oldpeak"])],
            "ST_Slope": [request.form["st_slope"]],
        }

        # Створюємо DataFrame
        input_df = pd.DataFrame(data)

        # Робимо передбачення
        prediction = model.predict(input_df)
        result = int(prediction[0])

        # Формуємо відповідь
        if result == 1:
            message = "⚠️ ВИСОКИЙ РИЗИК серцевих захворювань"
            recommendation = "Рекомендується негайно звернутися до кардіолога для детального обстеження."
            risk_level = "high"
        else:
            message = "✅ НИЗЬКИЙ РИЗИК серцевих захворювань"
            recommendation = "Продовжуйте вести здоровий спосіб життя. Регулярні профілактичні огляди раз на рік."
            risk_level = "low"

        return jsonify(
            {
                "success": True,
                "prediction": result,
                "message": message,
                "recommendation": recommendation,
                "risk_level": risk_level,
            }
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    print("🚀 Запуск веб-застосунку...")
    # Для локального запуску
    port = int(os.environ.get("PORT", 8080))
    print(f"📍 Відкрийте в браузері: http://127.0.0.1:{port}")
    app.run(debug=True, host="0.0.0.0", port=port)
