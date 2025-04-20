from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    message = ''
    
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            if height <= 0 or weight <= 0:
                message = 'Please enter valid positive numbers for weight and height.'
            else:
                bmi = round(weight / (height ** 2), 2)

                if bmi < 18.5:
                    message = 'You are underweight.'
                elif 18.5 <= bmi < 24.9:
                    message = 'You have a normal weight.'
                elif 25 <= bmi < 29.9:
                    message = 'You are overweight.'
                else:
                    message = 'You are obese.'
        except (ValueError, TypeError):
            message = 'Invalid input. Please enter numeric values only.'

    return render_template('bmi-calc.html', bmi=bmi, message=message)

if __name__ == '__main__':
    app.run(debug=True)
