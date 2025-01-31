import csv
from tkinter import Tk, Text, Label, Frame, END

# Register bank
Acc = 0  # Initialize accumulator to 0
PSW = 0  # Program Status Word to select register bank

class Instructions:
    def __init__(self):
        # Initialize 4 register banks, each with 8 registers (R0-R7)
        self.rbank = [[0] for _ in range(8)]
        #self.print_register_bank()

    def print_register_bank(self):
        """Print the current state of the register bank."""
        for row in self.rbank:
            print(row)
        print("--------")

    def put(self, rb, r_val):
        """Store a value in a register."""
        self.rbank[rb] = [r_val]

    # MOVE statement
    def toAcc(self, i):
        """Move the value from a register to the accumulator."""
        global Acc
        Acc = self.rbank[i][0]

    def toReg(self, i):
        """Move the value from the accumulator to a register."""
        global Acc
        self.rbank[i][0] = Acc

    def toAccImmediate(self, r_val):
        """Move an immediate value to the accumulator."""
        global Acc
        Acc = r_val

    # INCREMENT/Decrement statement
    def inc(self, i):
        """Increment a register or the accumulator."""
        global Acc
        if i == 'A':
            Acc += 1
        else:
            i1 = int(i[1:])
            self.rbank[i1][0] += 1

    def dec(self, i):
        """Decrement a register or the accumulator."""
        global Acc
        if i == 'A':
            Acc -= 1
        else:
            i1 = int(i[1:])
            self.rbank[i1][0] -= 1

    def set(self, i):
        """Set a register or the accumulator to 1."""
        global Acc
        if i == 'A':
            Acc = 1
        else:
            i1 = int(i[1:])
            self.rbank[i1][0] = 1

    def reset(self, i):
        """Reset a register or the accumulator to 0."""
        global Acc
        if i == 'A':
            Acc = 0
        else:
            i1 = int(i[1:])
            self.rbank[i1][0] = 0

    # ADDITION statement
    def add(self, i):
        """Add the value of a register to the accumulator."""
        global Acc
        Acc += self.rbank[i][0]

    # SUBTRACTION statement
    def sub(self, i):
        """Subtract the value of a register from the accumulator."""
        global Acc
        Acc -= self.rbank[i][0]

# Mnemonics dictionary
Mnemonics = {
    "mov": None,
    "add": None,
    "inc": None,
    "dec": None,
    "set": None,
    "reset": None,
    "sub": None,
    "jz": None,
    "jnz": None,
    "djnz": None,
}

# All Move functions for addressing modes
def MOV1(r, rb, r_val):
    """Move immediate value to a register."""
    r.put(rb, r_val)

def MOV2(i, r):
    """Move value from a register to the accumulator."""
    r.toAcc(i)

def MOV3(i, r):
    """Move value from the accumulator to a register."""
    r.toReg(i)

def MOV4(r_val):
    """Move immediate value to the accumulator."""
    global Acc
    Acc = r_val

def ADD1(i, r):
    """Add the value of a register to the accumulator."""
    global Acc
    Acc += r.rbank[i][0]

def ADD2(r_val):
    """Add an immediate value to the accumulator."""
    global Acc
    Acc += r_val

def INC(i, r):
    """Increment a register or the accumulator."""
    r.inc(i)

def DEC(i, r):
    """Decrement a register or the accumulator."""
    r.dec(i)

def SUB1(i, r):
    """Subtract the value of a register from the accumulator."""
    r.sub(i)

def JZ(label, r):
    """Jump to label if the accumulator is zero."""
    global Acc
    if Acc == 0:
        return label

def JNZ(label, r):
    """Jump to label if the accumulator is not zero."""
    global Acc
    if Acc != 0:
        return label

def DJNZ(i, label, r):
    """Decrement a register and jump to label if the register is not zero."""
    global Acc
    i1 = int(i[1:])
    r.rbank[i1][0] -= 1
    if r.rbank[i1][0] != 0:
        return label

# Assign functions to mnemonics
Mnemonics["mov"] = MOV1
Mnemonics["add"] = ADD1
Mnemonics["inc"] = INC
Mnemonics["dec"] = DEC
Mnemonics["sub"] = SUB1
Mnemonics["jz"] = JZ
Mnemonics["jnz"] = JNZ
Mnemonics["djnz"] = DJNZ

# Initialize the instruction set
x = Instructions()

def parse_value(value):
    """Parse a value, handling hexadecimal, binary, octal, and decimal values."""
    if value.startswith('#'):  # Immediate value
        value = value[1:]
    
    if value.endswith('H'):  # Hexadecimal
        return int(value[:-1], 16)
    elif value.endswith('B'):  # Binary
        return int(value[:-1], 2)
    elif value.endswith('O'):  # Octal
        return int(value[:-1], 8)
    else:  # Decimal (default)
        return int(value)

def selecting_mov(row):
    """Handle MOV instructions."""
    global x
    column1, column2, column3 = row
    if column1 == 'mov' and column2.startswith('R') and column3.startswith('#'):
        column2_int = int(column2[1:])
        column3_int = parse_value(column3)
        Mnemonics["mov"](x, column2_int, column3_int)
    elif column1 == 'mov' and column2 == 'A' and column3.startswith('R'):
        column3_int = int(column3[1:])
        Mnemonics["mov"](column3_int, x)
    elif column1 == 'mov' and column2.startswith('R') and column3 == 'A':
        column2_int = int(column2[1:])
        Mnemonics["mov"](column2_int, x)
    elif column1 == 'mov' and column2 == 'A' and column3.startswith('#'):
        column3_int = parse_value(column3)
        Mnemonics["mov"](column3_int)
    else:
        print('Invalid Syntax')

def selecting_add(row):
    """Handle ADD instructions."""
    global x
    column1, column2, column3 = row
    if column1 == 'add' and column2 == 'A' and column3.startswith('R'):
        column3_int = int(column3[1:])
        Mnemonics["add"](column3_int, x)
    elif column1 == 'add' and column2 == 'A' and column3.startswith('#'):
        column3_int = parse_value(column3)
        Mnemonics["add"](column3_int)

def selecting_sub(row):
    """Handle SUB instructions."""
    global x
    column1, column2, column3 = row
    if column1 == 'sub' and column2 == 'A' and column3.startswith('R'):
        column3_int = int(column3[1:])
        Mnemonics["sub"](column3_int, x)

def process_row(row):
    """Process a row of instructions."""
    if len(row) == 3:
        column1 = row[0]
        if column1 == 'mov':
            selecting_mov(row)
        elif column1 == 'add':
            selecting_add(row)
        elif column1 == 'sub':
            selecting_sub(row)
        elif column1 == 'inc':
            column2 = row[1]
            Mnemonics[column1](column2, x)
        elif column1 == 'dec':
            column2 = row[1]
            Mnemonics[column1](column2, x)
        elif column1 in ['jz', 'jnz', 'djnz']:
            column2 = row[1]
            label = Mnemonics[column1](column2, x)
            if label:
                return label
    else:
        print("Invalid command")

def read_csv_file(file_path):
    """Read and process instructions from a CSV file."""
    labels = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        # First pass to collect labels
        for i, row in enumerate(rows):
            if len(row) == 1 and row[0].endswith(':'):
                labels[row[0][:-1]] = i

        # Second pass to execute instructions
        i = 0
        while i < len(rows):
            row = rows[i]
            if len(row) == 1 and row[0].endswith(':'):
                i += 1
                continue
            split_val = row[0].split(',')  # Split by comma
            if len(split_val) <= 3:
                result = process_row(split_val)
                if result:
                    i = labels[result]
                else:
                    i += 1
            else:
                print(len(split_val))
                print("Invalid command")
                i += 1

# Tkinter GUI for displaying output
def display_output():
    """Display the register bank and accumulator in a Tkinter window."""
    root = Tk()
    root.title("8051 Simulator Output")
    root.geometry("400x300")

    # Frame for register bank
    frame = Frame(root)
    frame.pack(pady=10)

    # Label for register bank
    Label(frame, text="Register Bank", font=("Arial", 14)).pack()

    # Text box for register bank
    register_box = Text(frame, height=10, width=40)
    register_box.pack()

    # Insert register bank values into the text box
    for i, row in enumerate(x.rbank):
        register_box.insert(END, f"R{i}: {row[0]}\n")

    # Label for accumulator
    Label(root, text=f"Accumulator: {Acc}", font=("Arial", 14)).pack(pady=10)

    root.mainloop()

# Main execution
file_path = "D:\PySim8051\PySim8051\Command.txt"  # Replace with the actual file path
read_csv_file(file_path)

# Display output in Tkinter window
display_output()