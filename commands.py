import discord
from discord.ext import commands
import calculator
import create_profile
import db

profile = {}
goal = {}
expense = {}

def run_discord_bot():
    TOKEN = 'MTA2NjM5NDM3OTAyOTMxOTY5Mw.GaD34_.C-v3YEWhZ-4h7nfdc8ddiVJIEau_1CbVZ33oiM'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='$', intents=intents)


    @bot.event
    async def on_ready():
        print("im running and im online")


    @bot.command()
    async def test (ctx, *args):
        await ctx.send(args[1])

    @bot.command()
    async def helpme(ctx, arg= " "):
        is_private = check_mute(arg)
        help_embed = discord.Embed(
            title="Here are $ave-a-thon's possible commands",
            description="How to access the different commands",
            color=discord.Color.blue())
        help_embed.set_thumbnail(
            url="https://th.bing.com/th/id/R.bd382a74a382c1a3a20cf3ffd1bfc6cd?rik=M00Efr8m1TP%2baw&riu=http%3a%2f%2fwww.moorgateacoustics.co.uk%2fwp-content%2fuploads%2f2014%2f06%2fhelp.jpg&ehk=aQLQP7HYubrfeyk9At80bMM%2brSORKn2THoreN7zZzuY%3d&risl=&pid=ImgRaw&r=0")
        help_embed.add_field(name="$calculator",
                             value="Built-in calculator functions to help you calculate (tax, interest, inverse_interest)\n",
                             inline=False)
        help_embed.add_field(name="$new_profile", value="Creating your profile \n", inline=False)
        help_embed.add_field(name="$profile", value="Allows you to view the specifics of your account \n", inline=False)
        help_embed.add_field(name="$FAQ", value="Frequently asked Questions and their answers \n", inline=False)
        if is_private:
            await ctx.author.send(embed=help_embed)
        else:
            await ctx.channel.send(embed=help_embed)

    @bot.command()
    async def calculator(ctx, arg = ""):
        print("called the calculator")
        is_private = check_mute(arg)
        calculator_embed=discord.Embed(
            title= "Calculator Prompts",
            description= "The following commands gives you access to the calculator's functionalities",
            color= discord.Color.dark_orange()
        )
        calculator_embed.add_field(name= "$tax", value= "This option will return the cost of an item with its tax included \n Please enter the information the following 2 formats: \n 1. $tax 200 (the interest will be a default value assigned) \n 2.$tax 200 22 (the interest is the specified value given, 22 in this case", inline=False)
        calculator_embed.add_field(name= "$wage", value= "This will convert your wage into a monthly salary \n Please enter information in the following format: \n $wage (amount)(hour/month/year) (optional: how many hours worked per period)", inline= False)
        calculator_embed.add_field(name= "$interest", value= "This will return the future value of a lump with compounded interest \n Please enter the information in the following format: \n $interest (amount) (interest) (time in years)",inline= False)
        calculator_embed.add_field(name= "$inverse_interest", value= "This will calculate the amount of time it will take to reach your goal with your initial investment and interest rate \n Please enter information in the following format: \n $reverse_interest(Amount)(interest rate)(goal)", inline=False)
        if is_private:
            await ctx.author.send(embed=calculator_embed)
        else:
            await ctx.channel.send(embed=calculator_embed)

    @bot.command()
    async def tax(ctx, *args):
        is_private = check_mute(*args)
        tax_value = ""
        if len(args) == 2 and not is_private or len(args) == 3:
            tax_value = calculate_tax(float(args[0]), float(args[1]))
        else:
            tax_value = calculate_tax(float(args[0]))
        tax_embed=discord.Embed(
            title="Tax calculator",
            description= "The following calculation was done in accordance with the values you have entered",
            color= discord.Color.red()
        )
        tax_embed.add_field(name="Results", value= "Your initial value was: " + str(args[0]) + "\n The total after taxes is: " + str(tax_value), inline=False)
        if is_private:
            await ctx.author.send(embed=tax_embed)
        else:
            await ctx.channel.send(embed = tax_embed)

    @bot.command()
    async def interest(ctx,*args):
        is_private = check_mute(*args)
        new_amount = calculate_interest(float(args[0]), float(args[1]), int(args[2]))
        interest_embed=discord.Embed(
            title="Interest Calculator",
            description= "This calculation will return the new value accumulated after collecting the specified interest, for the specified amount of time",
            color= discord.Color.yellow()
        )
        interest_embed.add_field(name="Results", value= "Your initial investment: " + str(args[0]) + "\n The new value is: " + str(new_amount))
        if is_private:
            await ctx.author.send(embed=interest_embed)
        else:
            await ctx.channel.send(embed=interest_embed)

    @bot.command()
    async def inverse_interest(ctx, *args):
        is_private = check_mute(*args)
        no_of_years = calculate_inverse_interest(float(args[0]), float(args[1]), int(args[2]))
        inverse_interest_embed=discord.Embed(
            title="Inverse Interest Calculator",
            description= "This calculation will return the amount of time it takes to achieve your goal based on your given rate",
            color= discord.Color.dark_gray()
        )
        inverse_interest_embed.add_field(name="Results", value="It will take you: " + str(no_of_years) + " years to achieve your goal.", inline= False)
        if is_private:
            await ctx.author.send(embed=inverse_interest_embed)
        else:
            await ctx.channel.send(embed=inverse_interest_embed)

    @bot.command()
    async def wage(ctx, *args):
        is_private = check_mute(*args)
        if len(args) == 3 and not is_private or len(args) == 4:
            monthly_salary = calculate_wage(float(args[0]), args[1], int(args[2]))
        else:
            monthly_salary = calculate_wage(float(args[0]), args[1])
        wage_embed=discord.Embed(
            title="Monthly wage calculator",
            description="This calculation will return your wage in dollars/month \n Please enter your wage in the following format: \n $wage (dollar amount)(hourly = h, or monthly = m, or yearly = y)(period ~ if you work 40h/week do not put anything, if you work 20h/week you put 20)",
            color=discord.Color.magenta()
        )
        wage_embed.add_field(name="Results", value= "Your monthly wage in dollars is: " + str(monthly_salary) + "$/month", inline=False)
        if is_private:
            await ctx.author.send(embed=wage_embed)
        else:
            await ctx.channel.send(embed=wage_embed)

    @bot.command()
    async def FAQ (ctx, arg=" "):
        is_private = check_mute(arg)
        FAQ_embed = discord.Embed(
            title="FAQ",
            description="Frequently asked questions and their answers!",
            color=discord.Color.dark_gold()
        )
        FAQ_embed.add_field(name=" What is a TFSA account", value= "A TFSA account is a Tax Free Savings Account \nFor more information please follow the following page https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account.html")
        FAQ_embed.add_field(name= "What is an RRSP acoount", value= "A RRSP is a Registered Retirement Savings Plan \nFor more information please follow the following page https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/registered-retirement-savings-plan-rrsp.html")
        FAQ_embed.add_field(name="", value= "|nepotism|", inline=False)
        FAQ_embed.add_field(name="Canada's Guide to Budgeting", value= "Check out this link for help on setting up a budget https://www.canada.ca/en/financial-consumer-agency/services/make-budget.html", inline=False)
        if is_private:
            await ctx.author.send(embed=FAQ_embed)
        else:
            await ctx.channel.send(embed=FAQ_embed)

    @bot.command()
    async def create_profile(ctx, arg = ""):
        is_private = check_mute(arg)
        create_profile_embed=discord.Embed(
            title= "Profile Prompts",
            description= "The following commands gives you access to the calculator's functionalities",
            color= discord.Color.dark_orange()
        )
        create_profile_embed.add_field(name= "$profile_income <monthly salary in CAD>", value= "This command registers your monthly salary", inline=False)
        create_profile_embed.add_field(name= "$profile_expenses <transport,utilities,housing>", value= "This command registers your monthly transportation, utilities and housing expenses", inline= False)
        create_profile_embed.add_field(name="$templates",
                                       value="See our recommended savings plans", inline=False)
        create_profile_embed.add_field(name="$add_goal <title of goal>",
                                       value="Add a savings goal", inline=False)
        profile.clear()
        profile["discord_id"] = str(ctx.author)
        profile["name"] = arg

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def profile_income(ctx, arg=""):
        is_private = check_mute(arg)

        create_profile_embed = discord.Embed(
            title="Profile creation",
            description="Your income was successfully registered",
            color=discord.Color.dark_orange()
        )

        profile["monthly_income"] = arg
        finish_profile()
        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def budget_plan(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Profile creation",
            description="Your choice was successfully registered",
            color=discord.Color.dark_orange()
        )

        profile["budget_plan"] = arg
        finish_profile()
        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def profile_expenses(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Profile creation",
            description="Your expenses were successfully registered",
            color=discord.Color.dark_orange()
        )

        expenses = arg.split(',')
        profile["utilities"] = expenses[0]
        profile["housing"] = expenses[1]
        profile["transportation"] = expenses[2]
        finish_profile()

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def add_goal(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Goal creation",
            description="Please enter the following commands to register a savings goal",
            color=discord.Color.dark_orange()
        )
        create_profile_embed.add_field(name="$goal_cost <estimated cost of your goal>",
                                       value="Enter how much your goal costs",
                                       inline=False)
        create_profile_embed.add_field(name="$goal_deadline <estimated months to achieve your goal>",
                                       value="Give an estimate of when you wish to achieve your goal's amount",
                                       inline=False)
        create_profile_embed.add_field(name="$goal_start <starting contribution towards your goal>",
                                       value="This command registers how much you've contributed to your goal so far",
                                       inline=False)
        goal.clear()
        goal["discord_id"] = str(ctx.author)
        goal["name"] = arg

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def goal_cost(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Goal creation",
            description="Cost was successfully registered",
            color=discord.Color.dark_orange()
        )
        goal["amount"] = arg
        finish_goal()

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def goal_deadline(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Goal creation",
            description="Deadline was successfully registered",
            color=discord.Color.dark_orange()
        )
        goal["deadline"] = arg
        finish_goal()
        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def goal_start(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Goal creation",
            description="Starting contribution was successfully registered",
            color=discord.Color.dark_orange()
        )
        goal["progress"] = arg
        finish_goal()

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def open_profile(ctx, arg=""):
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Your profile",
            description="See how you've been doing so far",
            color=discord.Color.dark_orange()
        )
        create_profile_embed.add_field(name="$add_expense <category, amount>",
                                       value="Log your expenses to keep track of your spending habits. \n Possible category values are: \n 1- food/drinks\n 2- leisure\n 3- school\n 4- miscellaneous",
                                       inline=False)
        create_profile_embed.add_field(name="$add_goal_contribution <goal, amount>",
                                       value="Contribute any amount into one of your goals.",
                                       inline=False)
        create_profile_embed.add_field(name="$show_profile",
                                       value="See your journey towards your saving goals!",
                                       inline=False)

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)

    @bot.command()
    async def add_expense(ctx, arg=""):
        expenses = arg.split(",")
        is_private = check_mute(arg)
        create_profile_embed = discord.Embed(
            title="Your expenses",
            description="Your " + expenses[1] + "$ " + expenses[0] + " expense has been registered",
            color=discord.Color.dark_orange()
        )

        expense["discord_id"] = str(ctx.author)
        expense["category"] = expenses[0]
        expense["amount"] = expenses[1]
        finish_expense()

        if is_private:
            await ctx.author.send(embed=create_profile_embed)
        else:
            await ctx.channel.send(embed=create_profile_embed)



    bot.run(TOKEN)




def check_mute(*args):
    last_arg_index = len(args)-1
    last_arg = args[last_arg_index]
    if last_arg == 'mute':
        return True
    else:
        return False

def calculate_tax(cost, tax_amount=0.14975):
    if tax_amount != 0.14975:
        tax_amount/=100
    return cost + (tax_amount*cost)


def calculate_interest(amount, interest, time):
    #interest in years i assume?
    interest /= 100
    yearly_return = amount
    for i in range(time):
        yearly_return += yearly_return * interest
    return yearly_return


def calculate_inverse_interest(amount, interest, goal_amount):
    interest /= 100
    i=0
    while amount<goal_amount:
        amount += amount*interest
        i+=1
    return i


def calculate_wage(amount, frequency, period="default"):
    wage = 0
    if frequency == 'h':
        if period == "default":
            period = 40
        wage = (period * 4) * amount
    if frequency == 'm':
        if period != "default":
            wage = (amount/period)
        else:
            wage = amount
    if frequency == 'y':
        if period != "default":
            wage = (amount/period)/12
        else:
            wage = amount/12
    #wage = calculate_inverse_tax(wage)
    return wage

def finish_profile():
    if len(profile) == 7:
        db.add_profile(profile)
        profile.clear()

def finish_goal():
    if len(goal) == 5:
        db.add_goal(goal)
        goal.clear()

def finish_expense():
    if len(expense) == 3:
        db.add_expense(expense)
        expense.clear()