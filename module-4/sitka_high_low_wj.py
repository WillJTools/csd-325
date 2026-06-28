# William Judd
# 6/28/2026
# Module 4.2 Assignment
# Purpose: Display Sitka high and low temperatures using a menu.
# Changes made:
# 1. Added a menu so the user can choose high temperatures, low temperatures, or exit.
# 2. Added support for low temperature data from the TMIN column.
# 3. Added a loop so the program continues until the user selects exit.
# 4. Added graph formatting for high temperatures in red and low temperatures in blue.
# 5. Added an exit message when the user leaves the program.

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt


FILENAME = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    """Read Sitka weather data and return dates, highs, and lows."""
    dates, highs, lows = [], [], []

    with open(FILENAME) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_temperatures(dates, temperatures, temp_type):
    """Plot either high or low temperatures based on the user's menu choice."""
    fig, ax = plt.subplots()

    if temp_type == 'highs':
        ax.plot(dates, temperatures, c='red')
        plt.title('Daily high temperatures - 2018', fontsize=24)
    else:
        ax.plot(dates, temperatures, c='blue')
        plt.title('Daily low temperatures - 2018', fontsize=24)

    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


def display_menu():
    """Display the program menu."""
    print('\nSitka Weather Menu')
    print('1. View high temperatures')
    print('2. View low temperatures')
    print('3. Exit')


def main():
    """Run the Sitka high and low temperature program."""
    dates, highs, lows = load_weather_data()

    while True:
        display_menu()
        choice = input('\nEnter your choice: ')

        if choice == '1':
            plot_temperatures(dates, highs, 'highs')
        elif choice == '2':
            plot_temperatures(dates, lows, 'lows')
        elif choice == '3':
            print('\nThank you for using the Sitka weather program. Goodbye!')
            sys.exit()
        else:
            print('\nInvalid choice. Please select 1, 2, or 3.')


if __name__ == '__main__':
    main()