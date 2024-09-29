# Hangman-Game
For this mini-project, I developed a simple hangman game in Python, which revolves around guessing a hidden word letter by letter. The words are all dessert-themed, such as "bolo", "sorvete", and "brigadeiro", making the game fun and thematic. I used the random module to select a word from a predefined list at the start of each game.

The program allows the player to guess letters, and it keeps track of both correct and incorrect guesses. Correct guesses are displayed in the word’s respective positions, while incorrect guesses are recorded and reduce the number of remaining attempts. The game loop continues until the player either guesses the word or runs out of attempts.

I implemented logic to handle repeated guesses, ensuring the player can't reuse previously entered letters. To enhance the user experience, the game prints the current state of the word with blanks representing unguessed letters, as well as the number of remaining attempts and incorrect letters guessed so far.

The game ends with a win message if the player successfully guesses the word, or a loss message revealing the word if the player runs out of attempts. I also added basic input validation to make sure only single letters are accepted as guesses, preventing invalid entries.

This project helped me practice key Python concepts like list comprehensions, loops, and conditionals, while also improving my ability to manage game flow and user input. It was a great way to apply programming logic in a fun, interactive manner, reinforcing the skills I've been learning.
