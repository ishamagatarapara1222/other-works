#9. Implement a Printer class with a print_data() method that handles strings, integers, or both based on type
#verification.

class Printer:
    def print_data(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                print(f"Printing String Data: '{arg}'")
            elif isinstance(arg, int):
                print(f"Printing Integer Data: {arg}")
        elif len(args) == 2:
            print(f"Printing Combined Data -> String: '{args[0]}', Integer: {args[1]}")
        else:
            print("Unsupported arguments.")

# Testing
printer = Printer()
printer.print_data("Hello AI")
printer.print_data(2026)
printer.print_data("Lab Work", 5)
