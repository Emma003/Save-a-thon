import random

def get_response(message):
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '$help':
        return "`list of commands: change later`"


    #TODO: add invalid input
    # return "default response"

