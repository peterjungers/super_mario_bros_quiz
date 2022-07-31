"""
This module contains utilities used by the program.
"""


import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("- " * 30)
    print("Super Mario Bros. quiz".center(60))
    print("- " * 30)
    print()
