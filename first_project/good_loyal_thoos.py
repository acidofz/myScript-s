import time
import sys

def slow_print(text, delay=0.035):
    """Печатает текст медленно, символ за символом"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_line(line, pause=0.6):
    slow_print(line)
    time.sleep(pause)


lyrics = [
    # Intro / Hook (повторяется несколько раз)
    "World don't revolve around you",
    "Girl, you not the only one",
    "World don't revolve around you",
    "Girl, you not the only one",
    "World don't revolve around you",
    "Girl, you not the only one",
    "World don't revolve around you",
    "Girl, you not the only one",
    "",
    # Verse
    "There's more where that came from",
    "I got me more than a couple girls",
    "It's not yours, girl, this my world",
    "I-I break her back and make her twirl",
    "I like seeing them girls on girls",
    "That's her best friend, she's bisexual",
    "I like seeing them girls on girls",
    "That's her best friend, she's bisexual",
    "",
    # Повтор хука
    "World don't revolve around you",
    "Girl, you not the only one",
    "World don't revolve around you",
    "Girl, you not the only one",
    "",
    # Outro / повторяющиеся части
    "World don't revolve around you",
    "Girl, you not the only one",
    "World don't revolve around you",
    "Girl, you not the only one"
]

# Красивый заголовок
print("\n" + "═" * 70)
print(" " * 20 + "Odetari — GOOD LOYAL THOTS")
print(" " * 25 + "(2023 • odecore vibe)")
print("═" * 70 + "\n")

time.sleep(1.5)

for line in lyrics:
    if line.strip() == "":
        print()  # пустая строка → пауза и воздух
        time.sleep(1.0)
    else:
        print_line(line, pause=0.7 if "World don't" in line else 0.9)

print("\n" + "═" * 70)
print(" " * 22 + "That's her best friend... ♡")
print("═" * 70 + "\n")