def solve():
    full_name = input().strip()
    # split into words, capitalize each, then join back
    capitalized_name = " ".join(word.capitalize() for word in full_name.split())
    print(capitalized_name)
