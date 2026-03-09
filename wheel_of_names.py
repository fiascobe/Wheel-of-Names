import random
import time
import os
import platform
from datetime import datetime

# --- Configuration ---
MAX_NAMES = 20
ANIMATION_DURATION_SECONDS = 5
HISTORY_FILE = "historial_sorteos.txt"
# ---------------------

def clear_screen():
    command = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(command)

def get_names():
    names = []
    print("--- 🎡 Wheel of Names ---")
    print(f"Ingresá hasta {MAX_NAMES} nombres. Enter en blanco cuando termines.\n")

    while len(names) < MAX_NAMES:
        name = input(f"Nombre #{len(names) + 1}: ").strip()

        if not name:
            if len(names) < 2:
                print("Necesitás al menos 2 nombres.\n")
                continue
            else:
                break

        names.append(name)

    if len(names) == MAX_NAMES:
        print(f"\nMáximo de {MAX_NAMES} nombres alcanzado.")

    return names

def display_names(names, highlighted=None):
    """Muestra todos los nombres. Si se pasa uno como highlighted, lo resalta."""
    print("Participantes:\n")
    for name in names:
        if name == highlighted:
            print(f"  ▶  {name.upper()}  ◀")
        else:
            print(f"     {name}")
    print()

def run_animation(names):
    clear_screen()
    print("¡A girar la rueda!\n")
    time.sleep(1)

    winner = random.choice(names)

    start_time = time.time()
    current_time = time.time()
    spin_delay = 0.08

    while current_time - start_time < ANIMATION_DURATION_SECONDS:
        clear_screen()
        print("🎡 Girando...\n")

        # Mostrar todos los nombres, resaltando uno random
        highlighted = random.choice(names)
        display_names(names, highlighted)

        time.sleep(spin_delay)

        # Frenar en los últimos 2.5 segundos
        if current_time - start_time > (ANIMATION_DURATION_SECONDS - 2.5):
            spin_delay += 0.03

        current_time = time.time()

    return winner

def display_winner(name, all_names):
    clear_screen()
    print("Y el ganador es...\n")
    time.sleep(1.5)

    winner_text = f"🎉  {name.upper()}  🎉"
    border = "═" * (len(winner_text) + 4)

    print(f"\n  ╔{border}╗")
    print(f"  ║  {winner_text}  ║")
    print(f"  ╚{border}╝")
    print("\n  ¡Felicitaciones!\n")

    save_to_history(name, all_names)

def save_to_history(winner, all_names):
    """Guarda el resultado en el archivo de historial."""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    participants = ", ".join(all_names)

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"Participantes: {participants}\n")
        f.write(f"Ganador: {winner}\n")
        f.write("-" * 40 + "\n")

    print(f"  (Resultado guardado en '{HISTORY_FILE}')\n")

def show_history():
    """Muestra el historial de sorteos anteriores."""
    if not os.path.exists(HISTORY_FILE):
        print("Todavía no hay historial de sorteos.\n")
        return

    print("\n--- 📋 Historial de sorteos ---\n")
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def main():
    clear_screen()
    print("--- 🎡 Wheel of Names ---\n")
    print("1. Hacer un sorteo")
    print("2. Ver historial")
    print("3. Salir\n")

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        names_list = get_names()
        if names_list:
            winner = run_animation(names_list)
            display_winner(winner, names_list)
            input("Presioná Enter para volver al menú...")
            main()

    elif opcion == "2":
        show_history()
        input("Presioná Enter para volver al menú...")
        main()

    elif opcion == "3":
        print("¡Hasta la próxima!\n")

    else:
        print("Opción inválida.\n")
        main()

if __name__ == "__main__":
    main()
