import matplotlib.pyplot as plt
import os

def main():
    print("Welcome to the chartmaker! Please begin by choosing one of the following options:")
    print("Option 1: Manual Data Entry")
    print("Option 2: Enter Data From Text File")

    choice = get_user_choice([1, 2])

    if choice == 1:
        manual_data_entry()
    elif choice == 2:
        file_data_entry()

def get_user_choice(allowed_choices):
    """Get a valid user choice from the list of allowed choices."""
    while True:
        try:
            choice = int(input("> "))
            if choice in allowed_choices:
                return choice
            else:
                print(f"Please choose a valid option from {allowed_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def manual_data_entry():
    """Handle the manual data entry flow."""
    x_values = [float(x) for x in input("Please enter the x-axis values.\n> ").split(',')]
    y_values = [float(y) for x in input("Please enter the y-axis values.\n> ").split(',')]
    
    if len(x_values) != len(y_values):
        print("Error: X and Y axis data sets are not the same size.")
        return

    plot_title = None
    if input("Would you like a plot title? [Y/N]\n> ").lower() == 'y':
        plot_title = input("Please enter a plot title.\n> ")

    x_label = None
    if input("Would you like an x-axis label? [Y/N]\n> ").lower() == 'y':
        x_label = input("Please enter an x-axis label.\n> ")

    y_label = None
    if input("Would you like a y-axis label? [Y/N]\n> ").lower() == 'y':
        y_label = input("Please enter a y-axis label.\n> ")

    line_style = get_line_style()
    marker_style = None
    if input("Would you like to choose a custom marker style? [Y/N]\n> ").lower() == 'y':
        marker_style = input("Please choose a marker style (e.g. 'o' for circle, '.' for point, etc.):\n> ")

    plot_chart(x_values, y_values, plot_title, x_label, y_label, line_style, marker_style)

def get_line_style():
    """Allow user to choose a line style and return the corresponding matplotlib linestyle."""
    line_style_dict = {
        1: '-',
        2: ':',
        3: '--',
        4: '-.'
    }
    if input("Would you like to choose a custom line style? [Y/N]\n> ").lower() == 'y':
        print("Please choose a line style:")
        print("1. Solid Line")
        print("2. Dotted Line")
        print("3. Dashed Line")
        print("4. Dashed/Dotted Line")
        choice = get_user_choice([1, 2, 3, 4])
        return line_style_dict.get(choice, '-')
    return '-'

def file_data_entry():
    """Handle the data entry flow from a file."""
    while True:
        file_name = input("Please enter the file name\n> ")
        if os.path.exists(file_name):
            break
        print("Error: File does not exist. Please try again.")
    
    with open(file_name, 'r') as file:
        x_values = [float(x) for x in file.readline().split(',')]
        y_values = [float(y) for x in file.readline().split(',')]
        
        plot_title = file.readline().strip()
        x_label = file.readline().strip()
        y_label = file.readline().strip()
        line_style = get_line_style_from_file(int(file.readline().strip()))
        marker_style = file.readline().strip()

    plot_chart(x_values, y_values, plot_title, x_label, y_label, line_style, marker_style)

def get_line_style_from_file(choice):
    """Convert a numerical choice to a matplotlib linestyle."""
    line_style_dict = {
        1: '-',
        2: ':',
        3: '--',
        4: '-.'
    }
    return line_style_dict.get(choice, '-')

def plot_chart(x_values, y_values, title, x_label, y_label, line_style, marker_style):
    """Plot a chart with given parameters."""
    plt.plot(x_values, y_values, linestyle=line_style, marker=marker_style)
    if title:
        plt.title(title)
    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    plt.show()

if __name__ == "__main__":
    main()
