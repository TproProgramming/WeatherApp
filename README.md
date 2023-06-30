# Python Weather App
This is a simple Python weather application built using the Tkinter library. It allows users to enter a city name and retrieve weather information using the OpenWeatherMap API.

# Prerequisites
Before running the application, make sure you have the following prerequisites installed:

Python (version 3 or higher)
Tkinter library
Requests library

# Getting Started
Clone the repository or download the weather_app.py file.
Obtain an API key from OpenWeatherMap. You can sign up for a free account and generate an API key at OpenWeatherMap API.
Open the weather_app.py file in a text editor or integrated development environment (IDE).
Replace the placeholder value "YOUR_API_KEY" in the API_KEY variable with your actual OpenWeatherMap API key.
Save the file.
# Running the Application
To run the Python Weather App, follow these steps:

Open a terminal or command prompt.
Navigate to the directory where the weather_app.py file is located.
Run the following command:
Copy code
python weather_app.py
The Weather App window will open.
Enter the name of a city in the text field and press Enter.
The application will retrieve weather data for the specified city and display it in the window.

## Application Features
The application uses the OpenWeatherMap API to fetch weather data based on the entered city name.
The weather information displayed includes the city name, current weather condition, temperature, minimum and maximum temperatures, pressure, humidity, wind speed, sunrise time, and sunset time.
The application is built using the Tkinter library, which provides the graphical user interface components.
Customization
You can customize the appearance of the application by modifying the font_large and font_small variables to change the font and size of the text displayed in the window.
Additionally, you can modify the geometry parameter of the canvas.geometry function to change the initial size of the application window.
Troubleshooting
If you encounter any issues with the application, make sure you have a stable internet connection.
Check that you have correctly entered your OpenWeatherMap API key in the API_KEY variable.
Verify that the required Python libraries (Tkinter and Requests) are installed on your system.
License
This project is licensed under the MIT License. You can find the license information in the LICENSE file.

Acknowledgments
This application was created as a learning exercise and demonstration of using the Tkinter library and integrating with an API.
The OpenWeatherMap API was used to retrieve weather data. Visit their website at OpenWeatherMap for more information.
Feel free to modify and enhance the application according to your needs. Happy coding!
