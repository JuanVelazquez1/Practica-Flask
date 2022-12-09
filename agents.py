import requests

NUM_AGENTS = 3
url_random = "http://127.0.0.1:5000/generateNumber"
url_numbers = "http://127.0.0.1:5000/numbers"
url_check = "http://127.0.0.1:5000/check"
consensus = False
num_tries = 0

# While there is no consensus, generate three random numbers
# and check again if there is consensus
while not consensus:
    # Generate random numbers
    for agents in range(NUM_AGENTS):
        requests.post(url_random, json={'random':'r'})
    numbers = requests.get(url_numbers).json()
    check= requests.get(url_check).json()
    print(numbers, check)
    num_tries += 1
    # If there is consensus, end the loop
    if(check != "No consensus"):
        consensus = True
        print("Percentage of majority:", 100/num_tries, "%")