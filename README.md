# Calculator App
Simple calculator by use Python, Tkinter  and Figma
Overview: This calculator application, built using the tkinter module in Python, provides basic arithmetic functionalities such as addition, subtraction, multiplication, and division. The GUI features a clean and intuitive interface with buttons for digits (0-9), operations (+, -, *, /), and a special "C" button for clearing the display.

## Features

- **Numeric Buttons (0-9)**: Each number button updates the display to show the digits as they are entered. Users can construct any numerical value to participate in calculations.

- **Arithmetic Operations**: The calculator includes four basic arithmetic operations:
                              Addition (+): Adds two numbers.
                              Subtraction (-): Subtracts the second number from the first.
                              Multiplication (*): Multiplies two numbers.
                              Division (/): Divides the first number by the second, handling division by zero gracefully by displaying an error.
  
- **Clear Display ("C" Button)**:This button clears all current input and any stored operations. When pressed, it resets the display and all internal states, allowing the user to start a new calculation without 
                                 any remnants of previous ones.
- **Result Calculation ("=" Button)**:This button computes the result of the entered operation based on the current input and the chosen arithmetic function. If the calculation is successful, the result is 
                                      displayed. If there is an error (such as a syntax error or division by zero), the display shows "Error".
- **Error Handling**:The application robustly handles errors, such as invalid input sequences or mathematical errors (e.g., division by zero). In such cases, the display shows "Error", and the calculator can be 
                      reset using the "C" button.

## Technical Implementation:
1-The GUI layout is managed using tkinter frames and labels, with buttons placed in a grid layout for easy access and visibility.
2-Global variables are used to store the current number and the pending arithmetic operation to manage the flow of calculation.
3-The application handles user input through button callbacks, which update the display label dynamically.
4-The calculator's state (current operation, current number) is reset using the "C" button, ensuring a fresh start for new calculations without exiting or restarting the application.

## Usability:
1-This calculator is designed for ease of use with a straightforward interface, making it suitable for everyday arithmetic tasks.
2-The clear button enhances usability by allowing quick correction of mistakes and new calculations without manual clearing.

## Figma Design
![UI Design](UXFigma.jpg "UI Design Example")



