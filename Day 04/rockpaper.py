import random

print("Welcome to Rock Paper Scissor Game!!")
print("You have 10 rounds to play")
print("Type 'quit' anytime to exit the game.\n")

options = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0
tie_score = 0

for round_number in range(1, 11):
    print(f"--- Round {round_number} ---")
    
    user_choice = input("Please enter Rock, Paper, or Scissor: ").lower()
    
    if user_choice == "quit":
        print("Game ended early. Thanks for playing!\n")
        break
    
    elif user_choice not in options:
        print("❌ Invalid Option! Please enter Rock, Paper, or Scissor.\n")
        continue
    
    computer_choice = random.choice(options)
    
    print(f"User Choice: {user_choice.capitalize()}")
    print(f"Computer Choice: {computer_choice.capitalize()}")
    
    if user_choice == computer_choice:
        print("This round is a TIE!\n")
        tie_score += 1
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("🎉 You win this round!\n")
        user_score += 1
    else:
        print("😢 Computer wins this round!\n")
        computer_score += 1

print("========== Final Score ==========")
print(f"Your Wins     : {user_score}")
print(f"Computer Wins : {computer_score}")
print(f"Ties          : {tie_score}")

if user_score > computer_score:
    print("\n🏆 Congratulations, You are the Winner!")
elif user_score < computer_score:
    print("\n💻 Computer wins the Game!")
else:
    print("\n🤝 It's a Draw!")

print("Thank You for Playing the game 🎮")
