import random

def learning():
    print("Print a random string containing 0 or 1:")
    print()
    final = ""
    while True:
        candidate = input()
        for c in candidate:
            if c == "0" or c == "1":
                final += c
        print("Current data length is {}, {} symbols left".format(len(final), 100 - len(final)))
        if len(final) >= 100:
            break
        print("Print a random string containing 0 or 1:")
        print()
    print("Final data string:")
    return final


def count_triad(triada):
    global final_string
    temp = final_string
    count_zero = 0
    count_one = 0
    for _ in final_string:
        if temp.startswith(triada + "0"):
            count_zero += 1
        if temp.startswith(triada + "1"):
            count_one += 1
        temp = temp[1:]
    if count_zero > count_one:
        return "0"
    elif count_zero < count_one:
        return "1"
    else:
        return str(random.randint(0, 1))


def compare_prediction(test, candidate):
    count = 0
    global balance
    for _ in range(3, len(test)):
        if test[_] == candidate[_]:
            count += 1
    print()
    print("Computer guessed right {} out of {} symbols ({} %)"
          .format(count, len(test) - 3, round(count * 100 / (len(test) - 3), 2)))
    balance -= count
    balance += len(test) - 3 - count


def make_prediction(test):
    candidate = ""
    for _ in range(len(test)):
        if _ < 3:
            candidate += str(random.randint(0, 1))
        else:
            candidate += propabilities[test[_ - 3:_]]
    return candidate


def check_input(test):
    for character in test:
        if character not in ["0", "1"]:
            return False
    return True


balance = 1000
random.seed(100500)
final_string = learning()
propabilities = {"000": count_triad("000"), "001": count_triad("001"), "010": count_triad("010"),
                 "011": count_triad("011"), "100": count_triad("100"), "101": count_triad("101"),
                 "110": count_triad("110"), "111": count_triad("111")}
print(final_string)
print()
while True:
    print("Print a random string containing 0 or 1:")
    print()
    test_string = input()
    if test_string == "enough":
        break
    if not check_input(test_string):
        continue
    candidate_string = ""
    print("prediction:")
    candidate_string = make_prediction(test_string)
    print(candidate_string)
    compare_prediction(test_string, candidate_string)
    print("Your capital is now ${}".format(balance))
    if balance <= 0:
        break
print("Game over!")
