import random
import time
import os
import platform
from datetime import datetime

# --- Configuration ---
MAX_NAMES = 20
ANIMATION_DURATION_SECONDS = 5
HISTORY_FILE = "draw_history.txt"
# ---------------------

def clear_screen():
    command = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(command)

def get_names():
    names = []
    print("--- 🎡 Wheel of Names ---")
    print(f"Enter up to {MAX_NAMES} names. Press Enter on an empty line when you're done.\n")

    while len(names) < MAX_NAMES:
        name = input(f"Name #{len(names) + 1}: ").strip()

        if not name:
            if len(names) < 2:
                print("Please enter at least 2 names.\n")
                continue
            else:
                break

        names.append(name)

    if len(names) == MAX_NAMES:
        print(f"\nMaximum of {MAX_NAMES} names reached.")

    return names

def display_names(names, highlighted=None):
    """Shows all names. Highlights the currently selected one."""
    print("Participants:\n")
    for name in names:
        if name == highlighted:
            print(f"  ▶  {name.upper()}  ◀")
        else:
            print(f"     {name}")
    print()

def run_animation(names):
    clear_screen()
    print("Let's spin the wheel!\n")
    time.sleep(1)

    winner = random.choice(names)

    start_time = time.time()
    current_time = time.time()
    spin_delay = 0.08

    while current_time - start_time < ANIMATION_DURATION_SECONDS:
        clear_screen()
        print("🎡 Spinning...\n")

        # Show all names, highlight a random one
        highlighted = random.choice(names)
        display_names(names, highlighted)

        time.sleep(spin_delay)

        # Slow down in the last 2.5 seconds
        if current_time - start_time > (ANIMATION_DURATION_SECONDS - 2.5):
            spin_delay += 0.03

        current_time = time.time()

    return winner

def display_winner(name, all_names):
    clear_screen()
    print("And the winner is...\n")
    time.sleep(1.5)

    # Fixed width to avoid emoji alignment issues in terminal
    BOX_WIDTH = 30
    name_centered = name.upper().center(BOX_WIDTH)

    print(f"\n  ╔{'═' * (BOX_WIDTH + 2)}╗")
    print(f"  ║ {name_centered} ║")
    print(f"  ╚{'═' * (BOX_WIDTH + 2)}╝")
    print("\n  🎉 Congratulations! 🎉\n")

    save_to_history(name, all_names)

def save_to_history(winner, all_names):
    """Saves the draw result to the history file."""
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
    participants = ", ".join(all_names)

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"Participants: {participants}\n")
        f.write(f"Winner: {winner}\n")
        f.write("-" * 40 + "\n")

    print(f"  (Result saved to '{HISTORY_FILE}')\n")

def show_history():
    """Displays the history of previous draws."""
    if not os.path.exists(HISTORY_FILE):
        print("No draw history yet.\n")
        return

    print("\n--- 📋 Draw History ---\n")
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def main():
    clear_screen()
    print("--- 🎡 Wheel of Names ---\n")
    print("1. Run a draw")
    print("2. View history")
    print("3. Exit\n")

    option = input("Choose an option: ").strip()

    if option == "1":
        names_list = get_names()
        if names_list:
            winner = run_animation(names_list)
            display_winner(winner, names_list)
            input("Press Enter to go back to the menu...")
            main()

    elif option == "2":
        show_history()
        input("Press Enter to go back to the menu...")
        main()

    elif option == "3":
        print("See you next time!\n")

    else:
        print("Invalid option.\n")
        main()

if __name__ == "__main__":
    main()
