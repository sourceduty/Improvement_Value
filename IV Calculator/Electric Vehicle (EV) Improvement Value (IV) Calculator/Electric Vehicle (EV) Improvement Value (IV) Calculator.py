# Tesla IV Calculator
# Electric Vehicle (EV) Improvement Value (IV) Calculator
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# Expanded data for Tesla models from 2008 to 2024
TESLA_MODELS = {
    "2008": {
        "Roadster": {"range": 244, "efficiency": 280, "charging_time": "3.5 hours", "autopilot": "None", "satisfaction": 80, "market_impact": "Low"},
    },
    "2010": {
        "Roadster": {"range": 245, "efficiency": 275, "charging_time": "3.5 hours", "autopilot": "None", "satisfaction": 85, "market_impact": "Low"},
    },
    "2012": {
        "Model S": {"range": 265, "efficiency": 300, "charging_time": "30 min", "autopilot": "None", "satisfaction": 85, "market_impact": "Medium"},
    },
    "2015": {
        "Model S": {"range": 295, "efficiency": 290, "charging_time": "30 min", "autopilot": "Basic Autopilot", "satisfaction": 88, "market_impact": "High"},
    },
    "2016": {
        "Model X": {"range": 250, "efficiency": 300, "charging_time": "30 min", "autopilot": "Basic Autopilot", "satisfaction": 87, "market_impact": "Medium"},
    },
    "2017": {
        "Model 3": {"range": 310, "efficiency": 260, "charging_time": "30 min", "autopilot": "Basic Autopilot", "satisfaction": 90, "market_impact": "High"},
        "Model X": {"range": 295, "efficiency": 270, "charging_time": "30 min", "autopilot": "Basic Autopilot", "satisfaction": 88, "market_impact": "Medium"},
    },
    "2018": {
        "Model 3": {"range": 325, "efficiency": 245, "charging_time": "30 min", "autopilot": "Enhanced Autopilot", "satisfaction": 91, "market_impact": "High"},
        "Model X": {"range": 289, "efficiency": 275, "charging_time": "30 min", "autopilot": "Enhanced Autopilot", "satisfaction": 87, "market_impact": "Medium"},
    },
    "2019": {
        "Model 3": {"range": 322, "efficiency": 240, "charging_time": "30 min", "autopilot": "Enhanced Autopilot", "satisfaction": 92, "market_impact": "High"},
        "Model X": {"range": 328, "efficiency": 270, "charging_time": "30 min", "autopilot": "Enhanced Autopilot", "satisfaction": 88, "market_impact": "Medium"},
        "Model Y": {"range": 316, "efficiency": 265, "charging_time": "30 min", "autopilot": "Basic Autopilot", "satisfaction": 89, "market_impact": "High"},
    },
    "2020": {
        "Model 3": {"range": 322, "efficiency": 240, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 92, "market_impact": "High"},
        "Model X": {"range": 351, "efficiency": 260, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 89, "market_impact": "High"},
        "Model Y": {"range": 316, "efficiency": 260, "charging_time": "30 min", "autopilot": "Enhanced Autopilot", "satisfaction": 89, "market_impact": "High"},
    },
    "2021": {
        "Model S": {"range": 390, "efficiency": 250, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 93, "market_impact": "High"},
        "Model 3": {"range": 353, "efficiency": 230, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 94, "market_impact": "High"},
        "Model X": {"range": 340, "efficiency": 270, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 90, "market_impact": "High"},
        "Model Y": {"range": 326, "efficiency": 245, "charging_time": "30 min", "autopilot": "Full Self-Driving", "satisfaction": 90, "market_impact": "High"},
    },
    "2022": {
        "Model S": {"range": 405, "efficiency": 250, "charging_time": "20-40 min", "autopilot": "Enhanced Autopilot", "satisfaction": 90, "market_impact": "High"},
        "Model 3": {"range": 358, "efficiency": 240, "charging_time": "20-40 min", "autopilot": "Basic Autopilot", "satisfaction": 92, "market_impact": "High"},
        "Model X": {"range": 348, "efficiency": 260, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 89, "market_impact": "Medium"},
        "Model Y": {"range": 330, "efficiency": 230, "charging_time": "20-40 min", "autopilot": "Enhanced Autopilot", "satisfaction": 88, "market_impact": "High"},
    },
    "2023": {
        "Model S": {"range": 420, "efficiency": 240, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 94, "market_impact": "High"},
        "Model 3": {"range": 375, "efficiency": 230, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 93, "market_impact": "High"},
        "Model X": {"range": 348, "efficiency": 260, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 89, "market_impact": "Medium"},
        "Model Y": {"range": 330, "efficiency": 230, "charging_time": "20-40 min", "autopilot": "Enhanced Autopilot", "satisfaction": 88, "market_impact": "High"},
    },
    "2024": {
        "Model S": {"range": 420, "efficiency": 240, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 94, "market_impact": "High"},
        "Model 3": {"range": 375, "efficiency": 230, "charging_time": "20-40 min", "autopilot": "Full Self-Driving", "satisfaction": 93, "market_impact": "High"},
    }
}

def calculate_iv_score(model_data):
    """
    Automatically calculate the IV score based on predefined values for the model.
    """
    usability = 8  # General usability score for Tesla models
    efficiency = 10 * (model_data['range'] / model_data['efficiency']) / 100  # Scaled efficiency based on range and efficiency (Wh/mile)
    satisfaction = model_data['satisfaction'] / 10  # Convert satisfaction to a 1-10 scale
    impact = 8 if model_data['market_impact'] == "High" else 6 if model_data['market_impact'] == "Medium" else 4  # Market impact score

    return (usability + efficiency + satisfaction + impact) / 4

def display_iv_comparison(models):
    """
    Display IV scores for selected models.
    """
    print("\nTesla Model Improvement Value Comparison:\n")
    for year, model in models:
        model_data = TESLA_MODELS[year][model]
        iv_score = calculate_iv_score(model_data)
        print(f"{model} ({year}) - IV Score: {iv_score:.2f}")
    print("\n")

def iv_comparison():
    """
    The main interactive IV comparison program where the user selects models to compare.
    """
    print("Tesla Model IV Comparison Program")
    print("Select multiple Tesla models to compare by year and model.")
    
    selected_models = []

    while True:
        year = input("Enter the year (2008, 2010, 2012, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024) or 'done' to finish: ").strip()
        if year.lower() == 'done':
            break
        if year not in TESLA_MODELS:
            print("Year not found. Please try again.")
            continue

        available_models = list(TESLA_MODELS[year].keys())
        print(f"Available models for {year}: {', '.join(available_models)}")

        model = input(f"Enter the Tesla model for the year {year}: ").strip().title()
        if model not in TESLA_MODELS[year]:
            print("Model not found for the selected year. Please try again.")
            continue

        selected_models.append((year, model))

    if not selected_models:
        print("No models selected for comparison.")
        return

    display_iv_comparison(selected_models)

# Run the IV Comparison Program
if __name__ == "__main__":
    iv_comparison()
