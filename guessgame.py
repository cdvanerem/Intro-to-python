import random

class Game:
    """
    Number guessing game. To run, create an instance of class and run start_game().
    """ 
    def __init__(self) -> None:
        """Initialization function."""
        self.target_num: int 

    def start_game(self) -> None:
        """Starts the game loop. Runs until the correct number has been guessed."""
        self.target_num = random.randint(0, 100)
        while True:
            guess = self._get_user_guess()
            if self._check_guess(guess):
                break

    def _get_user_guess(self) -> int:
        """
        Retrieves an integer guess from the player.
        
        Returns:
            Value of the player's guess.
        """
        while True: 
            guess = input("Please enter a positive integer between 0 and 100: ")
            try:
                if float(guess).is_integer() and 0 <= int(guess) <= 100:
                    return int(guess)
                else:
                    print("Guess was not a valid integer between 0 and 100.")
            except ValueError:
                print("Guess was not a valid integer.")

    def _check_guess(self, guess) -> bool:
        """
        Checks the provided guess against the target value. 
        Prints 'Higher' or 'Lower' if incorrect guess. Returns True if the correct guess.
        
        Returns:
            True if the correct guess, False otherwise.
        """
        if guess < self.target_num:
            print("Higher!\n")
            return False
        elif guess > self.target_num:
            print("Lower!\n")
            return False
        else:
            print(f"Correct guess! The number was {self.target_num}")
            return True

if __name__ == "__main__":
    game = Game()
    game.start_game()