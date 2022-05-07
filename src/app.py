<<<<<<< HEAD

# I have creat a test case for read and added some notes for create and update
# this should be the starting point of you project.   create a function  that takes in all request
# this function will then pull the action out of the request and determine which handler to user
# should look something like this
# def handler(request)
# if request["commonParams"]["action"] == read:
# read_request = userProfile.processReadRequest(request)
def start(int):
    if int > 1:
        print("hello world")


def complex(number):
    index = 2
    dividerNumber = 1
    prime_number = 1
    while index < number:
        while dividerNumber < index:
            if index % dividerNumber == 0:
                break
            dividerNumber += 1
        else:
            prime_number = index

        index += 1
    return prime_number
=======
>>>>>>> 5b6b689 (Making some progress.  It's not exactly what the project asks for, but I had to get something and it's evolving with the functionality requested.)
