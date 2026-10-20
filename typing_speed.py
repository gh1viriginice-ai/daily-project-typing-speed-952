#!/usr/bin/env python3
import time, random

SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
    "python is a great programming language",
    "practice makes perfect every single day",
    "technology changes the way we live and work",
    "coding is fun when you solve real problems",
]

def test():
    s = random.choice(SENTENCES)
    print(f"Type this:\n\n  {s}\n")
    input("Press Enter to start...")
    start = time.time()
    typed = input(">> ")
    elapsed = time.time() - start
    words = len(typed.split())
    wpm = (words / elapsed) * 60
    accuracy = sum(a == b for a, b in zip(s, typed)) / max(len(s), len(typed)) * 100
    print(f"\nWPM: {wpm:.1f} | Accuracy: {accuracy:.1f}%")

if __name__ == "__main__":
    test()
