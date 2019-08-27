from tkinter import *
import tkinter as tk


class FoodOpt:
    def __init__(self, item, side, servingI, servingS):
        self.item = item
        self.side = side
        self.servingI = servingI
        self.servingS = servingS

    foodList = {
            "Chicken": 335,
            "Rice": 205,
            "Pizza": 285,
            "Fish": 150,
            "Fries": 365,
            "Beef": 215,
            "Green Beans": 30
    }

    def calCalc(food, serving):
        return foodList[food]*serving
