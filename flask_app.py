from flask import Flask, request, render_template
app = Flask(__name__)

stressometer=0

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    ID = request.form.get('input_name', '')
    Time = request.form.get('input_dropdown', '')
    select = request.form.get('Happy Index', '')
    freeform = request.form.get('Destress', '')
    if dropdown ==
    return render_template("main_page.html", input_data=dropdown,
                           output="statement")
