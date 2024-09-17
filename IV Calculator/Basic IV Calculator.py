# Basic IV Calculator
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

def ask_sub_questions(prompt, sub_questions):
    """
    This function asks a series of sub-questions related to a specific dimension and calculates a suggested rating.
    """
    total_score = 0
    for question in sub_questions:
        score = get_user_rating(question)
        total_score += score
    # Average the sub-question scores
    return total_score / len(sub_questions)

def get_user_rating(prompt):
    """
    This function asks the user for a rating between 1 and 10 and validates the input.
    """
    while True:
        try:
            rating = int(input(prompt))
            if rating < 1 or rating > 10:
                raise ValueError("Rating must be between 1 and 10.")
            return rating
        except ValueError as e:
            print(e)

def calculate_iv_score(usability, efficiency, satisfaction, impact):
    """
    This function calculates the average of the four dimensions to compute the IV score.
    """
    return (usability + efficiency + satisfaction + impact) / 4

def provide_feedback(iv_score):
    """
    This function provides feedback based on the IV score.
    """
    if iv_score >= 9:
        return "Excellent Improvement Value!"
    elif iv_score >= 7:
        return "Good Improvement Value."
    elif iv_score >= 5:
        return "Moderate Improvement Value. Consider further improvements."
    else:
        return "Low Improvement Value. Significant improvements may be needed."

def iv_calculator():
    """
    This is the main IV Calculator function that interacts with the user and calculates the Improvement Value.
    """
    print("Welcome to the expanded Improvement Value (IV) Calculator!")
    print("Please answer the following questions to help us evaluate the improvement.")

    # Usability questions
    usability_questions = [
        "How easy is it to navigate through the system (1-10)? ",
        "Did the improvement reduce the number of steps required to complete tasks (1-10)? ",
        "How intuitive is the user interface (1-10)? ",
        "Is it easy to find help or guidance when needed (1-10)? "
    ]
    usability = ask_sub_questions("Usability", usability_questions)
    
    # Efficiency questions
    efficiency_questions = [
        "Has the improvement reduced the time taken to complete tasks (1-10)? ",
        "Did the change reduce the effort required to achieve your goals (1-10)? ",
        "Are resources being used more effectively after the improvement (1-10)? ",
        "Has the overall workflow become smoother (1-10)? "
    ]
    efficiency = ask_sub_questions("Efficiency", efficiency_questions)
    
    # Satisfaction questions
    satisfaction_questions = [
        "How satisfied are you with the overall improvement (1-10)? ",
        "Do you feel happier or more comfortable using the system (1-10)? ",
        "Would you recommend the product/service after the improvement (1-10)? ",
        "Do you feel more confident using the product/service (1-10)? "
    ]
    satisfaction = ask_sub_questions("Satisfaction", satisfaction_questions)
    
    # Impact questions
    impact_questions = [
        "Has the improvement helped in increasing the market competitiveness (1-10)? ",
        "Has there been a noticeable improvement in business metrics (e.g., sales, revenue) after the change (1-10)? ",
        "Did the improvement create a positive impact on the surrounding ecosystem or community (1-10)? ",
        "Has the improvement contributed to long-term goals or strategic positioning (1-10)? "
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
