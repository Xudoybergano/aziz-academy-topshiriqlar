secret_number = int(input())

k = int(input())

for _ in range(k):
    guess = int(input())
    
    if guess == secret_number:
        print("TOPDINGIZ")
    elif guess > secret_number:
        print("KATTA")
    else:
        print("KICHIK")
     