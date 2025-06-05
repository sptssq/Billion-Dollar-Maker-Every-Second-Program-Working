import time
import random
import sys

def typewriter(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def hacking_animation():
    amount = random.randint(100_000_000, 2_000_000_000)
    amount_str = f"${amount:,}"
    realprogress = [
        "[▖         ] Initiating connection to offshore bank...",
        "[▘▖        ] Establishing encrypted tunnel...",
        "[▝▘▖       ] Bypassing firewalls...",
        "[▗▝▘▖      ] Cracking multi-factor authentication...",
        "[▖▗▝▘▖     ] Spoofing admin credentials...",
        "[▘▖▗▝▘▖    ] Planting backdoor...",
        "[▝▘▖▗▝▘▖   ] Evading Interpol...",
        "[▗▝▘▖▗▝▘▖  ] Accessing secret vault...",
        f"[▖▗▝▘▖▗▝▘▖ ] Downloading funds: {amount_str}...",
        f"[▘▖▗▝▘▖▗▝▘▖] Transferring {amount_str}...",
        "[SUCCESS!] Transfer complete! 💸💸💸"
    ]
    for line in realprogress:
        typewriter(line, speed=0.05)
        time.sleep(random.uniform(0.4, 1.1))
    return amount_str

def hacking_terminal():
    typewriter("Welcome.", speed=0.04)
    time.sleep(1)
    typewriter("Target: Offshore Bank [█████████]", speed=0.04)
    time.sleep(1)
    amount_str = hacking_animation()
    time.sleep(1)
    typewriter(f"\nNew balance: {amount_str}.00", speed=0.06)

if __name__ == "__main__":
    hacking_terminal()