# --- IMPORTS ---
from random import choice
from art import logo, vs
from game_data import data
from replit import clear


# --- FUNCTIONS ---

# Gets user answer
def get_answer(text, alt1, alt2):
    ans = input(text).lower()
    while ans != alt1 and ans != alt2:
        print("You tiped a wrong answer. Try again.")
        ans = input(text).lower()
    return ans


# Choose a person diferent than the one before
def choose_person(last_person: dict, _data: list):
    data_list = _data[:]
    data_list.remove(last_person)
    new_person = choice(data_list)
    return new_person


# Comparing samples
def compare(choise: str, person_a: dict, person_b: dict, _data: list):
    """
    Compare if followers of choise has more followers than the other, returns True if it is, False in the other case.
    """
    is_bigger = False
    followers_a = person_a["follower_count"]
    followers_b = person_b["follower_count"]
    if choise == "a":
        if followers_a > followers_b:
            is_bigger = True
    else:
        if followers_b > followers_a:
            is_bigger = True
    return is_bigger


# Starting game function
def start(last_person:dict=None, winnings=0, first_time=True):
    # Show logo
    print(logo)

    # Print The winings in case is not the first time
    if not first_time:
        print(f"You're right! Current score: {winnings}.")

    # Choose samples
    people = data[:]
    if last_person == None:
        person_a = choice(people)
    else:
        person_a = last_person
    person_b = choose_person(person_a, people)

    # Present samples
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

    # Ask the User
    question = "Who has more followers? Type 'A' or 'B': "
    answer = get_answer(question, "a", "b")

    # Compare samples
    answer_is_right = compare(answer, person_a, person_b, people)

    if answer_is_right:
        clear()
        winnings += 1
        start(person_b, winnings, False)
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {winnings}.")
        text_restart = "Do you want to play again? Type (y)es or (n)o: "
        restart = get_answer(text_restart, "y", "n")
        if restart == "y":
            start()
        else:
            return


# Aplication
start()