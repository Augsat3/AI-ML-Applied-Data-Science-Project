"""
Simple number guessing game for the Python refresher class.
Run it with: python guessing_game.py
"""

from __future__ import annotations

import random

# How good the score is based on number of tries
THRESHOLD_EXCELLENT = 3  # 1-3 tries
THRESHOLD_GOOD = 6       # 4-6 tries
# anything above that = keep practicing

MIN_NUMBER = 1
MAX_NUMBER = 100


def pick_secret(low: int = MIN_NUMBER, high: int = MAX_NUMBER) -> int:
    """Pick the number the player has to guess."""
    return random.randint(low, high)


def read_guess(low: int, high: int) -> int | None:
    """Get a guess from the player. Returns None if they type q."""
    while True:
        raw = input(f"Enter a number between {low} and {high} (or q to quit): ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            return None
        if raw == "":
            print("Please enter a number (or q to quit).")
            continue
        try:
            value = int(raw)
        except ValueError:
            print("That is not a whole number. Try again.")
            continue
        if value < low or value > high:
            print(f"Stay between {low} and {high}.")
            continue
        return value


def rate_performance(attempts: int) -> str:
    """Label the score using the thresholds above."""
    if attempts <= THRESHOLD_EXCELLENT:
        return "Excellent"
    if attempts <= THRESHOLD_GOOD:
        return "Good"
    return "Keep practicing"


def play_round(low: int = MIN_NUMBER, high: int = MAX_NUMBER) -> bool:
    """One round of the game. True if they got it, False if they quit."""
    secret = pick_secret(low, high)
    attempts = 0

    print()
    print("=" * 40)
    print("  Number Guessing Game")
    print("=" * 40)
    print(f"I am thinking of a number from {low} to {high}.")
    print("Type q anytime to quit this round.")
    print()

    while True:
        guess = read_guess(low, high)
        if guess is None:
            print(f"You quit after {attempts} guess(es). The number was {secret}.")
            return False

        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            label = rate_performance(attempts)
            print(f"Correct! You got it in {attempts} guess(es). -> {label}")
            return True


def main() -> None:
    """Start the game and keep going until they say no."""
    print("Welcome to the Guessing Game.")
    print("Tip: run with  python guessing_game.py")

    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
