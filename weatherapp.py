import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter city name",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Submit",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(500,250,700,700)
        self.setStyleSheet("background:#1BC2E1")
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""QLabel, QPushButton{
                           font-family:Arial;}
                           
                           QLabel#city_label{
                           font-size:50px;
                           font-styel:italic;
                           }

                           QLineEdit#city_input{
                           font-size:50px;
                           }
                           QPushButton#get_weather_button{
                           font-size:40px;
                           font-style:bold
                           }
                           QLabel#temperature_label{
                           font-size:85px;
                           }
                           QLabel#emoji_label{
                           font-size:110px;
                           font-family:Segoe UI emoji;
                           }
                           QLabel#description_label{
                           font-size:60px;}

                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self): 
        api_key = "a7f8257f34ae72a971e5772682898ed0"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") == 200:
                self.display_weather(data)
            else:
                self.display_error(f"Error: {data.get('message', 'Unknown error')}")
        
        except requests.exceptions.HTTPError as http_error:
            status_code = response.status_code
            match status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error("Internal server error\nPlease try again")
                case 502:
                    self.display_error("Bad gateway\nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway timeout\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred\n{http_error}")
        
        except requests.exceptions.RequestException as e:
            self.display_error(f"Request failed\n{e}")
    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k-273.15
        self.temperature_label.setText(f"{temperature_c:.02f}°С")
        self.temperature_label.setStyleSheet("font-size:85px")
        weaather_description=data["weather"][0]["description"]
        self.description_label.setText(weaather_description)
        weather_id=data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200<= weather_id <=235:
            return "⛈"
        elif 300<= weather_id <=321:
            return "🌦"
        elif 500<= weather_id <=531:
            return "🌧"
        elif 600<= weather_id <=622:
            return "❄"
        elif 701<= weather_id <=741:
            return "🌫"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==781:
            return "🌪"
        elif weather_id==800:
            return "☀"
        elif 801<= weather_id <=804:
            return "☁"
        else: 
            return ""
        


 




def main():
    app=QApplication(sys.argv)
    weather=weather_app()
    weather.show()
    sys.exit(app.exec_())

main()