# Day_25-US-States-quiz-game 🦅
The project combines Python, the turtle module, and the pandas library to create an interactive and data-driven quiz game.

This project was inspired by a U.S States quiz game on sporcle. The goal is for the user to guess all 50 states, each correct guess is displayed on a blank map of the United States.

## How the code works:
- Using the 'turtle' module the program loads a blank U.S map image (blank_states_img)
- It reads a CSV files (50_states.csv) using pandas containing the state names and x,y coordinates for placement on the map
- The user is repeatedly prompted to guess a state name
- If the guess is correct:
    The state name is added to a list of guessed states
    The name is displayed on the map at the correct coordinates
- The game continues until:
    All 50 states are guessed, or
    The user types "Exit"
- If the user exits early:
    A new CSV file (states_to_learn.csv) is created
    It contains all the states the user did not guess

## What I learned:
- Using the pandas library
- Reading CSV files with read_csv()
- Converting data into lists
- Filtering data using conditions
- Working with the turtle module to display images and text on screen & position elements using coordinates
- Creating interactive programs using while loops
- Handling user input dynamically
- Comparing user input with stored data
- Tracking progress using lists
- List comprehension

  🚀This project introduced data analysis concepts using pandas and showed how to combine them with interactive graphics using turtle. It demonstrated how Python can be used to build engaging, data-driven applications.
