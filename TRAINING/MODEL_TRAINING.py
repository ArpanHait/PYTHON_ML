from sklearn.tree import DecisionTreeClassifier

def main():
    """
    Training a simple decision tree model to classify fruits and predicts based on user input.
   """
    # Sample dataset: [weight, sweetness]
    X = [[150, 7], [170, 6], [140, 8], [200, 4], [210, 3], [190, 5]]
    y = [
        "apple", "apple", "pineapple", "tomato", "tomato", "potato"
    ]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    print("Enter the weight and sweetness of a fruit to classify it (e.g., 160 6):")
    try:
        weight, sweetness = map(int, input("weight and sweetness:").split())
        prediction = model.predict([[weight, sweetness]])
        print(f"Ye le predict kar diya: {prediction[0]}")
        print("ab kal aiyo train karne Acche dataset ke sath")

    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")


if __name__ == "__main__":
    main()