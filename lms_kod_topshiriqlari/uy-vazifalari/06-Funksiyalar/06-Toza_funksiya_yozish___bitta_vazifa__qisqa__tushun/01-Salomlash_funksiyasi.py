import sys

def salomlash(ism):
    return f"Salom, {ism}!"

ism = sys.stdin.read().strip()

if ism:
    print(salomlash(ism))