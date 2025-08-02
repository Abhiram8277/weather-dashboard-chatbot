# chatbot.py

from weather import get_weather

def respond_to_query(user_input):
    user_input = user_input.lower()
    
    if "weather" in user_input or "temperature" in user_input:
        # Extract city from input
        words = user_input.split()
        for i in range(len(words)):
            if words[i] in ["in", "at"] and i + 1 < len(words):
                city = words[i + 1].capitalize()
                weather = get_weather(city)
                if weather:
                    return (f"The current weather in {weather['city']} is {weather['description']} "
                            f"with a temperature of {weather['temperature']}°C.")
                else:
                    return "Sorry, I couldn't find weather info for that city."
        return "Please mention a city like: What's the weather in Mumbai?"
    
    return "I can help you with weather queries. Try asking: What's the temperature in Delhi?"
