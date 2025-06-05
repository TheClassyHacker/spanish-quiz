def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    score = 0 # keep track of the score
    total = len(translations)

    for english, spanish in translations.items():
        answer = input(f"What is the Spanish translation for {english}? ")
        if answer == spanish:
            print("That is correct!")
            score += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.")
        print() # prints a blank line
    print(f"You got {score} / {total} words correct, come study again soon!")

        
    



if __name__ == '__main__':
    main()
