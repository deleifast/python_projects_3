from __future__ import print_function
from time import sleep
import tqdm

fruits = [
    "Acai", "Apple", "Apricots", "Avocado", "Banana", "Blackberry",
    "Blueberries", "Cherries", "Coconut", "Cranberry", "Cucumber",
    "Durian", "Fig", "Grapefruit", "Grapes", "Kiwi", "Lemon", "Lime",
    "Mango", "Melon", "Orange", "Papaya", "Peach", "Pear", "Pineapple",
    "Pomegranate", "Raspberries", "Strawberries", "Watermelon"]

contains_berry = 0
for fruit in tqdm.tqdm(fruits):
    if "berr" in fruit.lower():
        contains_berry += 1
    sleep(.1)

print("{} fruit names contain 'berry' or 'berries'".format(contains_berry))