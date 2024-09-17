# IV Calculator
# Tesla Battery Improvement Value (IV) Calculator
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

def ask_sub_questions(prompt, sub_questions):
    total_score = 0
    for question in sub_questions:
        score = get_user_rating(question)
        total_score += score
    return total_score / len(sub_questions)

def get_user_rating(prompt):
    while True:
        try:
            rating = int(input(prompt))
            if rating < 1 or rating > 10:
                raise ValueError("Rating must be between 1 and 10.")
            return rating
        except ValueError as e:
            print(e)

def calculate_iv_score(usability, efficiency, satisfaction, impact):
    return (usability + efficiency + satisfaction + impact) / 4

def provide_feedback(iv_score):
    if iv_score >= 9:
        return "Excellent Improvement Value!"
    elif iv_score >= 7:
        return "Good Improvement Value."
    elif iv_score >= 5:
        return "Moderate Improvement Value. Consider further improvements."
    else:
        return "Low Improvement Value. Significant improvements may be needed."

def iv_calculator():
    print("Welcome to the Tesla Battery Technology Improvement Value (IV) Calculator!")
    print("Please answer the following questions to evaluate the battery improvements across models.")

    # Usability questions
    usability_questions = [
        "How easy is it to monitor battery performance (1-10)? ",
        "Did the battery improvements enhance driving range (1-10)? ",
        "How intuitive is the battery management system (1-10)? ",
        "Is it easy to find battery-related information (1-10)? "
    ]
    usability = ask_sub_questions("Usability", usability_questions)
    
    # Efficiency questions
    efficiency_questions = [
        "Has the battery technology improved charging times (1-10)? ",
        "Is energy consumption reduced with the new battery (1-10)? ",
        "Has the battery lifecycle improved (1-10)? ",
        "Are thermal management systems more effective (1-10)? "
    ]
    efficiency = ask_sub_questions("Efficiency", efficiency_questions)
    
    # Satisfaction questions
    satisfaction_questions = [
        "How satisfied are you with the battery's performance (1-10)? ",
        "Do you feel confident in the battery's reliability (1-10)? ",
        "Would you recommend Tesla vehicles based on battery performance (1-10)? ",
        "Do you feel the battery technology has improved your driving experience (1-10)? "
    ]
    satisfaction = ask_sub_questions("Satisfaction", satisfaction_questions)
    
    # Impact questions
    impact_questions = [
        "Has the battery improvement increased the vehicle's market appeal (1-10)? ",
        "Has there been a positive impact on sales since the battery upgrade (1-10)? ",
        "Did the battery innovation contribute to sustainability goals (1-10)? ",
        "Has the new battery technology positioned Tesla better in the market (1-10)? "
    ]
    impact = ask_sub_questions("Impact", impact_questions)
    
    # Calculate the IV score
    iv_score = calculate_iv_score(usability, efficiency, satisfaction, impact)
    
    # Display the result
    print(f"\nYour calculated Improvement Value score is: {iv_score:.2f}")
    print(provide_feedback(iv_score))

# Run the IV Calculator
if __name__ == "__main__":
    iv_calculator()
