import random

options = ["pedra","papel","tesoura"]
score = 0;
rounds_played = 0; #quantas vezes foi jogado

while True:
    #inicializando o adversario
    random_choice = random.choice(options);
    player_choice = input("Escolha pedra, papel ou tesoura: ");

    if(player_choice=="pedra"):
        rounds_played +=1;
        if random_choice=="pedra":
            print("Empate")
        elif random_choice =="papel":
            print("Você perdeu!")
        elif random_choice == "tesoura":
            print("Você Ganhou!")
            score +=1;

    elif player_choice == "papel":
        rounds_played +=1;
        if random_choice=="papel":
            print("Empate")
        elif random_choice =="tesoura":
            print("Você perdeu!")
        elif random_choice == "pedra":
            print("Você Ganhou!")
            score +=1;

    elif player_choice == "tesoura":
        rounds_played +=1;
        if random_choice=="tesoura":
            print("Empate")
        elif random_choice =="pedra":
            print("Você perdeu!")
        elif random_choice == "papel":
            print("Você Ganhou!")
            score +=1;

    else:
        play_again = input("Deseja jogar novamente? (s/n):")
        if play_again == "s":
            continue
        elif play_again == "n":
            print("Você ganhou :", score, " vezes!", rounds_played, " rodadas jogadas")
            break
        else:
            print("Escolha inválida!")
