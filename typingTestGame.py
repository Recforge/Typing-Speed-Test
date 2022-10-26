# Let's create a typing test game in Python
from time import time

# Calculating the accuracy of input prompt
def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        for i in(0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# Calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

# Calculate total time Elapsed
def timeElapsed(stime, etime):
    time = stime - etime

    return time

if __name__ == '__main__':
    prompt = "Hi, my name is Imtiyaz Mukhtar, I am a junior software engineer"
    print("Type this:- '", prompt, "'")

    # listening to input Enter
    input("press ENTER when you are ready!")

    # recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # Gather all the information returned from functions
    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    # Printing all the required data
    print("Total time elapsed : ", time, "s")
    print("You average Typing Speed was: ", speed, "words/second")
    print("With a total of: ", errors, "errors")

