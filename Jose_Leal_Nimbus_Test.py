import random

def multiplication_challenge():
    while True:
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        C = A * B
        print(f"A: {A}, C: {C}")
        
        if C == 4:
            print('Success!')
            break
multiplication_challenge()