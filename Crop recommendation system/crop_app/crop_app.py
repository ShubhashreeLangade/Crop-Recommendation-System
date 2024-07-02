import joblib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])
         
        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
        
        if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
            model = joblib.load('crop_app.pkl')  # Update the model filename and extension
            arr = [values]
            acc = model.predict(arr)
            return render_template('prediction.html', prediction=str(acc[0]))
        else:
            return "Sorry... Error in entered values in the form. Please check the values and fill it again."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
