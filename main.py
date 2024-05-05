"""Escape Room!"""


def choices():  # Lists the possible actions that the user can take
    print('There are various items scattered around the room.\n'
          f'What will {char_name} do?\n\n'
          'A: Read the movie poster on the wall\n'  # Hint: Se7en What's in the box???
          'B: Look under the bed\n'  # Decoy
          'C: Inspect the bird cage\n'  # Codeword: PEACE
          'D: Check the bookshelf\n'  # Hint: An animal holds a key word
          'E: Pick up the teddy bear\n'  # Codeword: WAR
          'F: Grab a pillow\n'  # Decoy
          'G: Examine the dull knife\n'  # Codeword: CHAOS
          'H: Inspect the picture frame\n'  # Hint: The bird is a symbol
          'I: Check the pizza box\n'  # Decoy
          'J: Search the unopened box\n'  # Hint: Knife holds a key word
          'K: Try to unlock the door\n')  # Password: WAR CHAOS PEACE


char_name = input('Enter character name here: ')
print(f'Character name: {char_name}\n')

print(f'{char_name} wakes up in a locked bedroom.\n\n'
      'There is a note at their feet. It reads:\n'
      f'"Welcome to the escape room, {char_name}.\n'
      f'You are subject #7.\n'
      f'Your goal: find a way out."\n')

choices()  # Initial list of actions

choice = str(input('Enter choice here: '))
correct_door_code = False

while correct_door_code is False:  # Loop will run until all 3 passwords are entered correctly

    if choice.lower() == 'a':  # Points to choice J
        print(f'\n{char_name} reads the movie poster.\n'
              "It's a poster of the movie Se7en.\n"
              'Under Brad Pitt and Morgan Freeman is a caption.\n'
              "What's in the box???\n")
        choices()  # Every time an action is taken, the list of choices will show before user makes another choice
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'b':  # Decoy choice
        print(f'\n{char_name} looks under the bed.\n'
              'Nothing there besides dust.\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'c':  # Gives 3rd password
        print(f'\n{char_name} inspects the bird cage.\n'
              'Inside the nest is a note. It reads:\n'
              '"III: PEACE"\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'd':  # Hint pointing to choice E
        print(f'\n{char_name} checks the bookshelf.\n'
              'On one shelf is the book Corduroy.\n'
              'Drawn onto the cover is a yellow key symbol.\n'
              f'Nothing happens when {char_name} touches it. What could it mean?\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'e':  # Gives 1st password
        print(f'\n{char_name} picks up the raggedy teddy bear.\n'
              'It is missing an eye, and there is a note on its back.\n'
              'The note reads:\n'
              '"I: WAR"\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'f':  # Decoy choice
        print(f'\n{char_name} grabs a pillow off the bed.\n'
              "There's no note, but it's comfortable!\n")
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'g':  # Gives 2nd password
        print(f'\n{char_name} examines the dull knife.\n'
              'Carved onto both sides of the blade is a message:\n'
              '"II: CHAOS"\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'h':  # Hint pointing to choice C
        print(f'\n{char_name} inspects the framed picture on the wall.\n'
              'It depicts a parrot flying around.\n'
              'The cage in the background looks familiar...\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'i':  # Decoy choice
        print(f'\n{char_name} checks the pizza box on the bed.\n'
              "There's no hint, but the pizza is still fresh.\n"
              'It tastes really good!\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'j':  # Hint pointing to choice G
        print(f'\n{char_name} searches the unopened box on the floor.\n'
              'Inside is a decorated knife stand.\n'
              'One knife seems to be missing.\n')
        choices()
        choice = str(input('Enter choice here: '))

    elif choice.lower() == 'k':  # This section was more complicated to code since it involves 3 locks
        # So I separated it to make it easier to read
        print('\nThe door has 3 locks.\n')
        user_password1 = input('Enter first password: ')

        if user_password1.lower() == 'war':  # Checks user input is correct password
            print('\nThe first lock opened!\n')
            user_password2 = input('Enter second password: ')

            if user_password2.lower() == 'chaos':  # Checks user input is correct password
                print('\nThe second lock opened!\n')
                user_password3 = input('Enter third password: ')

                if user_password3.lower() == 'peace':  # Checks user input is correct password
                    correct_door_code = True
                    break  # Breaks the loop to jump to the ending text

                else:  # If even one entered password is wrong, the user has to redo all 3
                    print('\nIncorrect. The locks have reset.\n')
                    choices()
                    choice = str(input('Enter choice here: '))

            else:
                print('\nIncorrect. The locks have reset.\n')
                choices()
                choice = str(input('Enter choice here: '))

        else:
            print('\nIncorrect. The locks have reset.\n')
            choices()
            choice = str(input('Enter choice here: '))

    else:  # Corrector if any value besides one in the range of A and K is entered
        print('\nPlease try again. Select a letter between A and K.\n')
        choice = str(input('Enter choice here: '))

if correct_door_code is True:  # Ending text once user enters the 3 right passwords
    print('\nThe door swings open!\n'
          f'{char_name} feels a rush of freedom as they race down the hill.\n'
          f"{char_name} still doesn't know how they got in that room...\n"
          f"But for now, {char_name} is safe.\n"
          "END")
