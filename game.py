import random

class Rock_paper_scissors:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.choices = ['rock' ,'paper','scissors']
    
    # get_player_choice
    def get_player_choice(self):
        """Get player choice randomly from choices : Rock Paper Scissor."""
        player_choice = input(f'Hi {self.player_name} please choice {self.choices}')
        if player_choice in self.choices:
            return player_choice
        else:
            print("your choice isn't valid please try again ")
            return self.get_player_choice()
    
    
    # get_computer_choice
    def get_computer_choice(self):
        """Get computer choice randomly from choices : Rock Paper Scissor."""
        computer_choice = random.choice(self.choices)
        return computer_choice

    # find_winner
    def find_winner(self, player_choice: str, computer_choice: str)-> str:
        """Decide the winner of the game base on user and computer choices.

        :param player_choice: The choice of the user.
        :param computer_choice: the choice of the computer.
        :return: The result of the game.
        """
        if player_choice == computer_choice:
            return " eqoal"
           
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            return " you won!"
        
        else:
            return " computer won"
    
    # def play_game
    def play_game(self):
        """plat the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = str(self.get_player_choice().lower())
        print(f'{user_choice}')
        computer_choice = self.get_computer_choice()
        print('Computer chose: ', computer_choice)
        print(self.find_winner(user_choice, computer_choice))
        

# play agane
name = input(f'enter your name :')
if __name__ == '__main__':
    game = Rock_paper_scissors(name)
    play = True
    while play :
        game.play_game()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            print('Done !')
            play = False