import bot
import commands
import calculator

def main():
    calculator.calculator_prompt()
    print(calculator.calculate_tax(200))
    print(calculator.calculate_tax(200,100))
    print(calculator.calculate_wage(80,'h'))
    print(calculator.calculate_interest(2000,15,30))
    print(calculator.calculate_inverse_interest(1000,1.5,2000))


if __name__ == '__main__':
    commands.run_discord_bot()
    #main()


