from model.scrabble_points import scrabble_points

def scrabble_score(word):
    return sum(scrabble_points.get(letter, 0) for letter in word.lower())

def run():
    word = input("Enter a word: ")
    score = scrabble_score(word)
    print(f"The score for {word} is {score}.")

run()