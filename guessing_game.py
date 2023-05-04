print('Name country who won CWC in 1992')
secret_word = 'Pakistan'
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guesses:
    print("Out of guess, YOU LOOSE!")
else:
    print('you win')