from flask import Flask, jsonify
from dice_roller.dice import Dice

app = Flask(__name__) #convention, name taken from the package

@app.route('/')
# home route directory
def home():
    dice = Dice()
    roll = dice.roll()
    return jsonify({'roll': roll})
