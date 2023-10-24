import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order']
    }


def random_stat():
    random_number = random.randint(1, 4)
    if random_number == 1:
        stat = 'id'
    elif random_number == 2:
        stat = 'height'
    elif random_number == 3:
        stat = 'weight'
    else:
        stat = 'order'
    return stat


def run():
    player_score = 0
    opponent_score = 0

    play = 'yes'
    round_count = 1
    while play == 'yes' or play == 'y':
        print("Welcome to Round {}!".format(round_count))

        pokemon_choice_1 = random_pokemon()
        pokemon_choice_2 = random_pokemon()
        pokemon_choice_3 = random_pokemon()

        print(
            f"Three wild pokemon appeared! {pokemon_choice_1['name']}, {pokemon_choice_2['name']}, {pokemon_choice_3['name']}")
        pokemon_choice = input("Which pokemon do you want to choose? ").lower()
        pokemon_choices = [pokemon_choice_1["name"], pokemon_choice_2["name"], pokemon_choice_3["name"]]
        while pokemon_choice not in pokemon_choices:
            print("Unrecognised response. The pokemon got away! Please try again.")
            pokemon_choice = input("Which pokemon do you want to choose? ").lower()

        if pokemon_choice == pokemon_choice_1['name']:
            chosen_pokemon = pokemon_choice_1
        elif pokemon_choice == pokemon_choice_2['name']:
            chosen_pokemon = pokemon_choice_2
        elif pokemon_choice == pokemon_choice_3['name']:
            chosen_pokemon = pokemon_choice_3


        print(f"Great choice, you caught {chosen_pokemon['name']}!")
        stat_random = input("Would you like to choose a stat or have a random stat? (Choose or Random) ").lower()
        if stat_random == "choose":
            chosen_stat = input(
                f"Please choose a characteristic for your battle: \nid: {chosen_pokemon['id']} \nheight: {chosen_pokemon['height']} \nweight: {chosen_pokemon['weight']} \norder: {chosen_pokemon['order']}\n").lower()
            stats = ["id", "height", "weight", "order"]
            while chosen_stat not in stats:
                print("Stat not recognised, please try again.")
                chosen_stat = input(
                    f"Please choose a characteristic for your battle: \nid: {chosen_pokemon['id']} \nheight: {chosen_pokemon['height']} \nweight: {chosen_pokemon['weight']} \norder: {chosen_pokemon['order']}\n").lower()
        else:
            chosen_stat = random_stat()

        print("You chose {} : {}".format(chosen_stat, chosen_pokemon[chosen_stat]))

        opponent_pokemon = random_pokemon()
        print(f"Your opponent caught {opponent_pokemon['name']}")
        print("Their stat score is {} : {}".format(chosen_stat, opponent_pokemon[chosen_stat]))

        player_stat = chosen_pokemon[chosen_stat]
        opponent_stat = opponent_pokemon[chosen_stat]
        if player_stat > opponent_stat:
            print("Congratulations! You defeated your opponent and won the battle")
            player_score += 1
        elif opponent_stat > player_stat:
            print("Better luck next time! Your opponent beat you and you lost the battle")
            opponent_score += 1
        else:
            print("So close! The battle was a draw this time.")
            player_score += 1
            opponent_score += 1

        print(f"Your scores are: \nYou: {player_score}\nYour opponent: {opponent_score}")
        play = input("Would you like to play again? ")
        round_count += 1

    print(f"Your scores are: \nYou: {player_score}\nYour opponent: {opponent_score}")


    with open('pokemonscores.txt', 'w+') as score_file:
        score_file.write(f"Final Scores: \nYour Score: {player_score} \nOpponent Score: {opponent_score}")

    if player_score > opponent_score:
        print("Congratulations, you are the Pokemon Champion!")
    elif opponent_score > player_score:
        print("Your opponent won the championship.")
    else:
        print("It's a draw!")


run()