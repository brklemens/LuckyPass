import argparse
import getpass
from luckypass import checker

def main():

    parser = argparse.ArgumentParser(
        description='Audit password strength and security'
    )

    args = parser.parse_args()


    password = getpass.getpass('Enter the password to audit:')

    result = checker.analysis(password)
    length = result['length']
    unique_chars = result['unique_characters']
    has_special = result['special_character']
    has_capital = result['capital_character']
    has_lower = result['lower_character']
    in_rockyou = result['in_common_list']

    # Convert booleans to symbols
    special_symbol = '✓' if has_special else '✗'
    capital_symbol = '✓' if has_capital else '✗'
    lower_symbol = '✓' if has_lower else '✗'
    rockyou_symbol = '✓' if in_rockyou else '✗'

    print()
    print("╔═══════════════════════════════════╗")
    print("║       LuckyPass v0.1.3            ║")
    print("╠═══════════════════════════════════╣")
    print(f"║ Length of password: {length:<14}║")
    print(f"║ Includes special symbols: {special_symbol:<8}║")
    print(f"║ Includes capital letter: {capital_symbol:<9}║")
    print(f"║ Includes lowercase letter: {lower_symbol:<7}║")
    print(f"║ Number of unique characters: {unique_chars:<5}║")
    print(f"║ Inside of rockyou.txt: {rockyou_symbol:<11}║")
    print("╠═══════════════════════════════════╣")
    print("║       Created by brklemens        ║")
    print("╚═══════════════════════════════════╝")
    print()





if __name__ == "__main__":
    main()