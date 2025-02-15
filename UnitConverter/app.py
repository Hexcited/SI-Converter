from flask import Flask, render_template, request


app = Flask(__name__)


# Conversion functions
def kilowatts_to_megawatts(kW):
    return kW * 0.001

def megawatts_to_gigawatts(MW):
    return MW * 0.001

def gigawatts_to_terawatts(GW):
    return GW * 0.001


# Route for the home page (main form)
@app.route('/')
def home():
    return render_template('index.html')    # Render the main HTML page


# Route to handle the form submission and conversion
@app.route('/convert', methods=['POST'])
def convert():
    choice = request.form['choice']         # Get the user's choice from the form
    value = float(request.form['value'])    # Get the value entered by the user

    # Call the appropriate conversion function
    if choice == '1':
        result = kilowatts_to_megawatts(value)
        unit = 'MW'
    elif choice == '2':
        result = megawatts_to_gigawatts(value)
        unit = 'GW'
    elif choice == '3':
        result = gigawatts_to_terawatts(value)
        unit = 'TW'
    else:
        result = None
        unit = ''

    # Return the result to the user
    return render_template('index.html', result=result, unit=unit)

if __name__ == '__main__':
    app.run(debug=True)