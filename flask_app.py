import random
from flask import Flask, request, render_template
app = Flask(__name__)

def select_house(favorite_spell, favorite_potion, favorite_flavor):
    # create dictionary mapping house names to point values
    houses = { "Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0 }

    # add points to each house based on how their favorite spell aligns
    if favorite_spell == "Wingardium Leviosa":
        houses["Hufflepuff"] += 2
    elif favorite_spell == "Expecto Patronum":
        houses["Gryffindor"] += 2
    elif favorite_spell == "Stupefy":
        houses["Slytherin"] += 2
    elif favorite_spell == "Aguamenti":
        houses["Ravenclaw"] += 2

    # add points to each house based on how their potion aligns
    if favorite_potion == "Amortentia":
        houses["Hufflepuff"] += 2
    elif favorite_potion == "Polyjuice":
        houses["Slytherin"] += 2
    elif favorite_potion == "Veritaserum":
        houses["Ravenclaw"] += 2
    elif favorite_potion == "Felix Felicis":
        houses["Gryffindor"] += 2

    # add random point values based on their favorite jelly bean flavor
    random.seed(favorite_flavor)
    for house in houses.keys():
        houses[house] += random.random()

    # choose the house with the highest value
    selected_house = None
    for house, points in houses.items():
        if selected_house is None or houses[selected_house] < points:
            selected_house = house

    # return the selected house
    return selected_house

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    favorite_spell = request.form.get('input_dropdown', '')
    favorite_potion = request.form.get('input_select', '')
    favorite_flavor = request.form.get('input_freeform', '')

    selected_house = select_house(favorite_spell, favorite_potion, favorite_flavor)

    return render_template("main_page.html", input_data=favorite_spell,
                           output= "Hm, {0}...{1}!".format(name, selected_house.upper()))
