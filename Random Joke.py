import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
    QButtonGroup, QPushButton, QTextEdit
)
from PyQt5.QtCore import Qt

class RandomJoke(QWidget):
    def __init__(self):
        super().__init__()

        self.text_label = QLabel("Select the type of joke", self)
        self.radio_button1 = QRadioButton("Family Jokes", self)
        self.radio_button2 = QRadioButton("Dad Jokes", self)
        self.radio_button3 = QRadioButton("Dark Jokes", self)
        self.button_group = QButtonGroup(self)
        self.get_joke_button = QPushButton("Get Joke", self)
        self.joke_display = QTextEdit(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Random Joke Generator")
        self.setGeometry(500, 250, 700, 500)

        self.button_group.addButton(self.radio_button1)
        self.button_group.addButton(self.radio_button2)
        self.button_group.addButton(self.radio_button3)

        layout = QVBoxLayout()
        layout.addWidget(self.text_label)
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)
        layout.addWidget(self.get_joke_button)
        layout.addWidget(self.joke_display)

        self.text_label.setStyleSheet("font-size: 30px; font-family: Arial")
        self.joke_display.setReadOnly(True)
        self.joke_display.setStyleSheet("font-size: 20px;")
        self.setStyleSheet("QRadioButton { font-size: 24px; padding: 5px } QPushButton { font-size: 20px }")

        self.setLayout(layout)

        
        self.get_joke_button.clicked.connect(self.display_joke)

    def display_joke(self):
        if self.radio_button1.isChecked():
            joke = self.get_family_joke()
        elif self.radio_button2.isChecked():
            joke = self.get_dad_joke()
        elif self.radio_button3.isChecked():
            joke = self.get_dark_joke()
        else:
            joke = "Please select a joke category first!"
        self.joke_display.setText(joke)

    def get_dad_joke(self):
        try:
            response = requests.get("https://icanhazdadjoke.com/")
            response.raise_for_status()
            data = response.json()["joke"]
            return data.get("joke")
        except requests.exceptions.RequestException as e:
            return f"Error fetching dad joke: {e}"

    def get_dark_joke(self):
        try:
            response = requests.get("https://v2.jokeapi.dev/joke/Dark?type=single")
            response.raise_for_status()
            data = response.json()
            return data.get("joke")
        except requests.exceptions.RequestException as e:
            return f"Error fetching dark joke: {e}"

    def get_family_joke(self):
        try:
            response = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous?type=twopart")
            response.raise_for_status()
            data = response.json()
            setup = data.get("setup", "")
            delivery = data.get("delivery", "")
            return f"{setup}\n\n{delivery}" if setup and delivery else "No joke found."
        except requests.exceptions.RequestException as e:
            return f"Error fetching family joke: {e}"

def main():
    app = QApplication(sys.argv)
    window = RandomJoke()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
