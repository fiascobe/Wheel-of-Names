import random
import time
import os
import platform

# --- Configuration ---
MAX_NAMES = 20
ANIMATION_DURATION_SECONDS = 5 # How long the "spin" should last
# ---------------------

def clear_screen():
    """Clears the terminal screen. Works on Windows, macOS, and Linux."""
    command = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(command)

def get_names():
    """
    Prompts the user to enter a list of names.
    Returns a list of names.
    """
    names = []
    print(f"--- Welcome to the Wheel of Names! ---")
    print(f"Enter up to {MAX_NAMES} names. Press Enter on an empty line when you're done.")
    
    while len(names) < MAX_NAMES:
        prompt = f"Enter name #{len(names) + 1}: "
        name = input(prompt).strip()
        
        if not name:
            if len(names) < 2:
                print("\nPlease enter at least two names to spin the wheel.")
                continue
            else:
                break # Exit loop if input is empty and we have enough names
        
        names.append(name)
        
    if len(names) == MAX_NAMES:
        print(f"\nYou have reached the maximum of {MAX_NAMES} names.")
        
    return names

def run_animation(names):
    """
    Displays the spinning animation and returns the chosen winner.
    """
    clear_screen()
    print("Ready to spin? Let's go!")
    time.sleep(1.5)

    # Choose the winner beforehand so the animation can build up to it
    winner = random.choice(names)
    
    print("Spinning the wheel...")
    time.sleep(1)

    start_time = time.time()
    current_time = time.time()
    spin_delay = 0.05 # Initial delay between names (fast)

    # The main animation loop runs for a set duration
    while current_time - start_time < ANIMATION_DURATION_SECONDS:
        clear_screen()
        
        # Display a random name from the list
        display_name = random.choice(names)
        
        print("Choosing a name...\n")
        print(f"\t\t+--------------------+")
        print(f"\t\t|   {display_name:<18} |")
        print(f"\t\t+--------------------+")

        time.sleep(spin_delay)

        # Slow down the animation in the last 2.5 seconds for suspense
        if current_time - start_time > (ANIMATION_DURATION_SECONDS - 2.5):
            spin_delay += 0.025 # Gradually increase the delay

        current_time = time.time()

    return winner

def display_winner(name):
    """
    Clears the screen and dramatically displays the winning name.
    """
    clear_screen()
    print("And the winner is...")
    time.sleep(1.5) # Dramatic pause

    winner_text = f"🎉 {name.upper()} 🎉"
    border = "*" * (len(winner_text) + 4)
    
    print("\n\n")
    print(f"\t\t{border}")
    print(f"\t\t* {winner_text} *")
    print(f"\t\t{border}")
    print("\n\nCongratulations!\n")


def main():
    """Main function to run the program."""
    names_list = get_names()
    
    if names_list:
        winner = run_animation(names_list)
        display_winner(winner)

if __name__ == "__main__":
    main()