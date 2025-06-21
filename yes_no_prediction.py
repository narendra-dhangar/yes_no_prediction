# yes_no_prediction.py

import random

def probability_predictor(prob_yes=0.7):
    # Generate a random float between 0 and 1
    rand_val = random.random()
    
    print(f"Random Value: {rand_val:.2f}")  # Optional: shows the random value

    if rand_val < prob_yes:
        print("Yes ✅")
    else:
        print("No ❌")

# Run the prediction multiple times
for i in range(10):
    print(f"Prediction {i+1}: ", end="")
    probability_predictor()