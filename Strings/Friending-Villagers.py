"""
You want to increase the friendship level with your favorite 
villager so everytime someone mentions the villager’s name 
you want to pay attention to the in-game text in case it's 
a task you can do to increase your friendship level with the 
villager. Given a string and a villager’s name(case insensitive), 
return whether or not the villager’s name appears in the text. 
"""


def containsName(text, name):
    text = text.lower()
    name = name.lower()
    return name in text


def main():
    print(containsName(“Help Champ get 4 apples.”, “Champ”))
    print(containsName(“That bird pecked me.”, “Peck”))
    print(containsName(“I like dogs”, “Kitty”))
    print("The booleans above should be True, True, and False.")
