# Questions the chatbot will ask the user
questions = [
    "What is the location of your land? (e.g., 'Rio Gallegos')",
    "What type of soil does your land have? (e.g., fertile, poor, sandy)",
    "What is the availability and quality of water? (e.g., groundwater, saline water, etc.)",
    "What type of climate predominates in your land? (e.g., arid, cold, temperate)",
    "What is the topography of your land? (e.g., flat, sloped, mountainous)",
    "What is the accessibility and mobility of the land? (e.g., easy access, paved roads)",
    "What nearby exploitations are in the region? (e.g., grazing, agriculture, industry)"
]

# Store user responses
user_data = {}

# Function that asks the user for necessary data
def ask_user_data():
    print("=" * 50)
    print("Hello! I need some data about your land to provide you with an agricultural analysis.")
    print("=" * 50)

    for question in questions:
        user_input = input(f"{question}: ")
        user_data[question] = user_input

# Function that offers a complete analysis with recommendations
def analyze_data():
    print("\n" + "=" * 50)
    print("Chatbot: Here is the complete analysis of your land:")
    print("=" * 50)
    
    # Summary based on user responses
    print(f"1. Location: {user_data[questions[0]]}")
    print(f"2. Soil type: {user_data[questions[1]]}")
    print(f"3. Water availability and quality: {user_data[questions[2]]}")
    print(f"4. Climate: {user_data[questions[3]]}")
    print(f"5. Topography: {user_data[questions[4]]}")
    print(f"6. Accessibility and mobility: {user_data[questions[5]]}")
    print(f"7. Nearby exploitations: {user_data[questions[6]]}")
    
    # Recommendations based on some simple examples
    print("\nRecommendations:")
    
    if "poor" in user_data[questions[1]].lower() or "sandy" in user_data[questions[1]].lower():
        print("→ The soil appears to have low fertility. I recommend using compost or organic fertilizers to improve it.")
    if "groundwater" in user_data[questions[2]].lower():
        print("→ Groundwater is a good source, but I suggest a drip irrigation system to optimize water use.")
    if "arid" in user_data[questions[3]].lower() or "dry" in user_data[questions[3]].lower():
        print("→ The arid climate suggests that drought-resistant crops like barley or rye could be viable.")
    if "flat" in user_data[questions[4]].lower():
        print("→ Flat topography facilitates agricultural machinery and the implementation of irrigation systems.")
    
    # Closing the chatbot
    print("\n" + "=" * 50)
    print("Thank you for using the agricultural chatbot. Goodbye!")
    print("=" * 50)

# Main function that controls the flow
def chatbot():
    ask_user_data()  # First, we ask for the data
    analyze_data()    # Then we provide the analysis based on that data

# Run the chatbot
if __name__ == "__main__":
    chatbot()
