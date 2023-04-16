# python3
B = 9
Q = 256

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    mode = input()
    if mode[0] == "I":
        return (input().rstrip(), input().rstrip())
    elif mode[0] == "F":
        file_name = input()
        if "a" in file_name:
            return
        file_name = 'tests/' + file_name
        with open(file_name, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
        return (pattern, text)
    else:
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    
def get_hash(pattern) -> int:
    global B, Q
    length = len(pattern)
    result = 0
    for i in range(length):
        result = (B*result+ord(pattern[i]))%Q
    return result

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    global B, Q
    pattern_length = len(pattern)
    
    # this function should find the occurances using Rabin Karp alghoritm 
    multiplier = 1
    for i in range(1, pattern_length):
        multiplier = (multiplier*B)%Q

    occurrences = []

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])

    for i in range(pattern_length, len(text)):
        text_hash = (B*(text_hash-ord(text[i-pattern_length])*multiplier)+ord(text[i]))%Q
        if text_hash == pattern_hash:
            if text[i-pattern_length+1:i + 1] == pattern:
                occurrences.append(i-pattern_length+1)
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

