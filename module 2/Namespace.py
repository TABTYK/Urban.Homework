call = 0

def count_calls():
    global call
    call += 1

def string_info(string):
    tuple = {len(string), string.lower(), string.upper()}
    print(tuple)
    count_calls()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False


string_info('capybara')
string_info('HaRRInGton')
string_info('pOTTER')
print(is_contains('ban',['ban','123']))
print(is_contains('1000',['52','69','777']))
print(call)