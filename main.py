import os
import sys
import requests
import time
from config import API_KEY

BANNER1 = r"""
██╗   ██╗██╗   ██╗██╗      ██████╗ █████╗ ███╗   ██╗██╗██╗  ██╗      █████╗ ██╗
██║   ██║██║   ██║██║     ██╔════╝██╔══██╗████╗  ██║██║╚██╗██╔╝     ██╔══██╗██║
██║   ██║██║   ██║██║     ██║     ███████║██╔██╗ ██║██║ ╚███╔╝█████╗███████║██║
╚██╗ ██╔╝██║   ██║██║     ██║     ██╔══██║██║╚██╗██║██║ ██╔██╗╚════╝██╔══██║██║
 ╚████╔╝ ╚██████╔╝███████╗╚██████╗██║  ██║██║ ╚████║██║██╔╝ ██╗     ██║  ██║██║
  ╚═══╝   ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝
                                                                               
"""

BANNER2 = r"""
                             . ..
                          . :-----:-----.----..
                         .--:.........::::::::-:
                        --.....................::::::--.
                       ::......................::.....:::-
                      .-..:....................::....:::::::.
                     .-::.....................:::::......::::.
                    .-::....................:::::..........:::
                    :-::..................:::::.............::
                    .-:::................::::::.............:.
                     ..-:::.:..............................::
                        ..-:....................... .....:::
                         ::...........................::::.
                        .-:....................... .:---.
                        .-:...................... ..:.-.
                         .-::.....::...............::-..
                           .------.:::.............::-
                                   .-:............:..-
                                    -:...........:::-.
                                  .-::..........:::::.
                                   -:................:.
                                    -:................-.
                                     .:--:...:..........
                                          . .--.........::--.
                                              . .-:.........:-
                                                 .-::...... .-
                                                    -.......:.
                                                   ......:-.
                                                 ..:...:-.
                                               ..+-#+*+#-...
                                             ..:=++*******:..
                                            .:=*+++*+***+**#.
                                          .:=*=*=+#++=*+*++#*#
                                        .-=+-=*==++*==+=++++**#..
                                       ==+-=++==+*+++=*=++*++#*##
                                    .==++==**===*++++=+*=++#++*###.
                                 ..:=++**-=+===++=+++++*=+++#++*####..
                                 .-=+++*-=+====+==+++*+===*++*++**####.
                               .:=*++**==*-===++==+=+**===+++**++*#####*
                             .==++++*+=++*==+*+===+==**+==++++*****#*##%#*
                          ..=*+==+**+++++++++*====+==+++===*++**+***#*#####-
                         .=+===++**=+*+*++++*+-==+*==++#+===+++*++******####%.
                      .-=++===++*#==*++*==++*+===++===+**+==++++#++*+**#*######.
                   .:==+++==*++*#==++**===++*+==+++===+*+*++++*+*#++*++***#######.
                ..===++===+++**===*+*====++++++==++===+*++*++++++**++**+*#**#######.
              .+-=++-=+=+*++*+===++*=-==*+++++==++====+*+++#*+++++**++**+****#####%##.
        ...++++++*+==++++++*-===++++-====++++===++===++**+++**+++++**++****#**######%#%..
       #++++**#++=+++**++++====++++=====+*+++=+++++==+++*+++****#*+***+*##*****#######%%##+.
    #++++++#**##%++*#+++++====++*=+==+++*++*+++++*++++++*++*+++*##*******##******#####++++**#+*-
 .=******#############*++++++++*++*#+*+++++++++++*++++++*#++++####**#*#***##******##++++*########%
  . .
"""

ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_orange(text):
    print(f"{ORANGE}{text}{RESET}")

def loading_animation():
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(25):
        for char in spinner:
            print(f"\r{ORANGE}Vulcanix is thinking {char}{RESET}   ", end="", flush=True)
            time.sleep(0.08)

def get_response(user_input, history, model):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://github.com/vulcanix-ai",
        "X-OpenRouter-Title": "Vulcanix AI",
        "Content-Type": "application/json"
    }

    system_prompt = "You are Vulcanix AI - a powerful and helpful assistant. You are excellent at generating clean, well-commented code in any programming language. When giving code, always use markdown code blocks with the correct language."

    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": user_input}]

    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=90
        )
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    clear_screen()
    print_orange(BANNER1)
    print_orange("Welcome to Vulcanix AI!")
    print_orange("Developer: discord - artem567yt , telegram - @artem567yt2\n")

    print_orange("1. Start")
    print_orange("2. Exit")

    choice = input(f"\n{ORANGE}Choose an option: {RESET}").strip()

    if choice == "2":
        print_orange("Goodbye!")
        sys.exit(0)
    elif choice != "1":
        print_orange("Invalid choice.")
        sys.exit(0)

    clear_screen()
    print_orange(BANNER2)
    print_orange("Vulcanix AI is ready!\n")
    
    print_orange("Enter the model you want to use from OpenRouter")
    model = input(f"{ORANGE}Model: {RESET}").strip()
    if not model:
        model = "openrouter/free"

    print_orange(f"\nUsing model: {model}\n")

    history = []

    while True:
        user_input = input(f"\n{ORANGE}Enter your query: {RESET}").strip()
        
        if user_input.lower() in ["exit", "quit", "выход"]:
            print_orange("Goodbye!")
            break
        if not user_input:
            continue

        print_orange("\nVulcanix: ")
        loading_animation()

        reply = get_response(user_input, history, model)
        
        print(f"\r{ORANGE}Vulcanix: {RESET}", end="")
        print(reply)

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})

        if len(history) > 20:
            history = history[-20:]

if __name__ == "__main__":
    main()