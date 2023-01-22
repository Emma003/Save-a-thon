import random
import discord
import calculator


def get_response(message):
    p_message = message.lower()
    #split by spaces
    #look at index 0 for the method
    #look at last index for mute (private message)
    split_message = p_message.split(' ')
    method = split_message[0]
    parameters = split_message[1:]
    if method == 'tax':
        if len(parameters) == 1:
            return calculator.calculate_tax(float(parameters[0]), float(parameters[1]))
        else:
            return calculator.calculate_tax(float(parameters[0]))

    if method == 'wage':
        if len(parameters) == 3:
            return calculator.calculate_wage(float(parameters[0]),parameters[1],float(parameters[2]))
        else:
            return calculator.calculate_wage(float(parameters[0]),parameters[1])

    if method == 'interest':
        return calculator.calculate_interest(float(parameters[0]), float(parameters[1]), int(parameters[2]))

    if method == 'inverse_interest':
        return calculator.calculate_inverse_interest(float(parameters[0]), float(parameters[1]), float(parameters[2]))

    if p_message == 'FAQ':
        pass

    if p_message == 'help':
        help_embed=discord.Embed(
        title= "Here are $ave-a-thon's possible commands",
        description="How to access the different commands",
        color=discord.Color.blue())
        help_embed.set_thumbnail(url="https://th.bing.com/th/id/R.bd382a74a382c1a3a20cf3ffd1bfc6cd?rik=M00Efr8m1TP%2baw&riu=http%3a%2f%2fwww.moorgateacoustics.co.uk%2fwp-content%2fuploads%2f2014%2f06%2fhelp.jpg&ehk=aQLQP7HYubrfeyk9At80bMM%2brSORKn2THoreN7zZzuY%3d&risl=&pid=ImgRaw&r=0")
        help_embed.add_field(name="$calculator", value= "Built-in calculator functions to help you calculate (tax, interest, inverse_interest)\n", inline=False)
        help_embed.add_field(name="$new_profile", value= "Creating your profile \n", inline= False)
        help_embed.add_field(name= "$profile", value= "Allows you to view the specifics of your account \n", inline= False)
        help_embed.add_field(name= "$FAQ", value= "Frequently asked Questions and their answers \n", inline= False)
        return help_embed

        #
        # list_of_commands = "These are possible commands to type:\n " \
        #                    "$calculator: built-in calculator functions to help you calculate (tax, interest, inverse_interest)\n" \
        #                     "$new_profile: creating your profile \n" \
        #                      "$profile: allows you to view the specifics of your account \n" \
        #                     "$FAQ: frequently asked questions and their answers \n"
        #
        # return list_of_commands

    if p_message == 'calculator':
        return calculator.calculator_prompt()
    #TODO: add invalid input
    # return "default response"
