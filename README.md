### 8051 Simulator - User Guide

Welcome to the **8051 Simulator**! This tool allows you to simulate the behavior of an 8051 microcontroller using a set of assembly-like instructions. Below is a simple guide to help you get started and understand how to use the simulator effectively.

---

### **Key Features**
- **Register Banks**: The simulator supports 4 register banks, each with 8 registers (R0-R7). You can switch between register banks using the PSW (Program Status Word).
- **Accumulator (A)**: The accumulator is used for arithmetic and logical operations.
- **B Register**: The B register is used for multiplication and other operations.
- **Supported Instructions**: The simulator supports common 8051 instructions like `MOV`, `ADD`, `SUB`, `INC`, `DEC`, `JZ`, `JNZ`, `DJNZ`, and `MUL`.
- **Input File**: You can write your 8051 assembly code in a text file (e.g., `Input.txt`) and load it into the simulator.
- **Output Display**: The results (register values and accumulator) are displayed in a user-friendly Tkinter window.

---

### **How to Use the Simulator**

#### 1. **Write Your Code**
   - Create a text file (e.g., `Input.txt`) and write your 8051 assembly code in it.
   - Each line should contain one instruction.
   - Example:
     ```
     mov A #5
     mov R0 #3
     add A R0
     jz end
     inc R0
     end:
     ```

#### 2. **Supported Instructions**
   - **MOV**: Move data between registers, accumulator, and immediate values.
     - Example: `mov A #5` (Move 5 into the accumulator).
   - **ADD**: Add a value to the accumulator.
     - Example: `add A R0` (Add the value in R0 to the accumulator).
   - **SUB**: Subtract a value from the accumulator.
     - Example: `sub A R0` (Subtract the value in R0 from the accumulator).
   - **INC**: Increment a register or the accumulator.
     - Example: `inc R0` (Increment R0 by 1).
   - **DEC**: Decrement a register or the accumulator.
     - Example: `dec R0` (Decrement R0 by 1).
   - **JZ**: Jump to a label if the accumulator is zero.
     - Example: `jz end` (Jump to the label `end` if A == 0).
   - **JNZ**: Jump to a label if the accumulator is not zero.
     - Example: `jnz loop` (Jump to the label `loop` if A != 0).
   - **DJNZ**: Decrement a register and jump to a label if the register is not zero.
     - Example: `djnz R0 loop` (Decrement R0 and jump to `loop` if R0 != 0).
   - **MUL**: Multiply the accumulator by the B register.
     - Example: `mul` (Multiply A by B, result in A and B).

#### 3. **Run the Simulator**
   - Save your code in a text file (e.g., `Input.txt`).
   - Update the `file_path` variable in the Python script to point to your input file.
   - Run the Python script. The simulator will execute your code and display the results in a Tkinter window.

#### 4. **View Results**
   - The Tkinter window will display:
     - The current state of the register bank (R0-R7).
     - The value of the accumulator (A).
   - Example Output:
     ```
     Register Bank:
     R0: 5
     R1: 0
     R2: 0
     R3: 0
     R4: 0
     R5: 0
     R6: 0
     R7: 0

     Accumulator: 8
     ```

---

### **Example Programs**

#### 1. **Factorial Calculation**
   - Calculate the factorial of a number using multiplication.
   - Code:
     ```
       mov A #5
       mov R0 A
       dec R0
       Here:
       mov B R0
       loop1:
       mul AB
       djnz R0 Here
       END:
       ```

#### 2. **Simple Addition**
   - Add two numbers and store the result in the accumulator.
   - Code:
     ```
     mov A #10
     mov R0 #20
     add A R0
     end:
     ```

---

### **Tips for Writing Code**
- Use labels (e.g., `loop:`, `end:`) for jumps and loops.
- Ensure that each instruction is on a new line.
- Use `#` for immediate values (e.g., `#5` for the number 5).
- Use `R0-R7` for registers and `A` for the accumulator.
- Don't use comma
- No space should be given in between consecutive two lines

---

### **Troubleshooting**
- **Invalid Command**: If you see this error, check the syntax of your instructions. Ensure that each instruction is valid and properly formatted.
- **Infinite Loop**: If your program gets stuck in a loop, double-check your jump and loop conditions (e.g., `JZ`, `JNZ`, `DJNZ`).

---

### **Next Steps**
- Try writing your own programs using the supported instructions.
- Experiment with different operations like multiplication, division (if implemented), and conditional jumps. (UPCOMING)
- Share your feedback or report issues to improve the simulator!

---

Enjoy using the **8051 Simulator**! If you have any questions or need further assistance, feel free to reach out. Happy coding! 🚀
