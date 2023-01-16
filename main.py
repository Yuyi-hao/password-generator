import string
import random
import traceback

# characters
lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)


characters_lst = [lower_case, upper_case, digits, punctuation]


def get_pass(length:int, password_type:int) -> str:
    pass_type = ""
    match password_type:
        case 1:
            pass_type = "pin"
        case 2:
            pass_type = "memorable"
        case 3:
            pass_type = "strong"

    password = ""
    match pass_type:
        case "pin":
            password = "".join(random.choices(digits, k=length))
        case "memorable":
            for i in range(length):
                random_weight = random.randint(0, 100)
                lst = random.choices(
                    characters_lst[:2],
                    cum_weights=(random_weight, 100-random_weight),
                    k=1
                )[0]
                password += random.choice(lst)
        case "medium":
            for i in range(length):
                random_weight = random.randint(0, 50)
                lst = random.choices(
                    characters_lst[:3],
                    cum_weights=(random_weight, 75-random_weight, random_weight*0.4),
                    k=1
                )[0]
                password += random.choice(lst)
        case "strong":
            for i in range(length):
                random_weight = random.randint(0, 100)
                lst = random.choices(
                    characters_lst,
                    weights=(random_weight, random_weight, random_weight/2, random_weight*2),
                    k=1
                )[0]
                password += random.choice(lst)
        case other:
            for i in range(length):
                random_weight = random.randint(0, 100)
                lst = random.choices(
                    characters_lst,
                    weights=(random_weight, random_weight, random_weight/2, random_weight*2),
                    k=1
                )[0]
                password += random.choice(lst)
    return password

if __name__ == "__main__":
    length = input("Enter the length of the password: ")
    try:
        length = int(length)
    except Exception:
        traceback.print_exc()

    password_type = input("""
Enter password type:
1. Pin, 
2. Medium(includes only letter) 
3. Strong(includes special character) 
4. Default
 :  """)
    try:
        password_type = int(password_type)
    except Exception:
        traceback.print_exc()

    print(get_pass(length, password_type))
