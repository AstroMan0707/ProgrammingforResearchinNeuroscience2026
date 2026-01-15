def mu_email(first: str, last: str) -> str:
    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    return f"{first.lower()}.{last.lower()}@marquette.edu"


if __name__ == "__main__":
    print(mu_email("John","Doe"))