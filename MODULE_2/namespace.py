calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(strings):
    count_calls()
    return len(strings), strings.upper(), strings.lower()

def is_contains(strings, list_to_search):
    count_calls()
    string_lower = strings.lower()
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False

if __name__ == "__main__":
    print(string_info('Capybara'))
    print(string_info('Armageddon'))

    print(is_contains('Urban', ['ban', 'BaNan', 'urBAN']))
    print(is_contains('cycle',['recycling','cyclic']))

    print(calls)