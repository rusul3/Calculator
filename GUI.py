import tkinter as tk
from calcu import add, subtract, multiply, divide

def click_button(value):
    current = display["text"]
    if current == "Error":
        display.config(text=value)
    else:
        display.config(text=f"{current}{value}")

def perform_operation(operator, symbol):
    global current_number, current_operator
    current_text = display["text"].strip()
    if current_text in ["", "Error"]:  # Handle empty or error state
        display.config(text="Error")
    else:
        try:
            current_number = float(current_text)  # converting current text to float
            current_operator = operator
            display.config(text=f"{current_text} {symbol} ")
        except ValueError:
            display.config(text="Error")
            current_number, current_operator = None, None

def calculate_result():
    global current_number, current_operator
    if current_operator is None or current_number is None:
        display.config(text="Error")
        return
    current_text = display["text"].strip()
    try:
        second_operand = current_text.split()[-1]  # Get the last element after splitting by space
        operand = float(second_operand)  # Convert the second operand to float
        result = current_operator(current_number, operand)
        display.config(text=str(result))
    except Exception as e:
        display.config(text="Error")
    finally:
        # Reset the globals after displaying the result
        current_number, current_operator = None, None

def clear_display():
    global current_number, current_operator
    display.config(text="")
    current_number = None
    current_operator = None


root = tk.Tk()
root.title('Calculter App')
root.geometry('250x300') 
root.configure(bg='#9C0707')  # Set the background color for the root window
current_number = None
current_operator = None

screen_frame = tk.Frame(root, bg='#FFFFFF', width=216, height=77)
screen_frame.place(x=19 , y=30 ) 

display = tk.Label(screen_frame, text="", bg='white', fg='black', width=25, height=2)
display.place(x=19, y=30)

no1_button = tk.Button (root, text="1", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(1) )
no1_button.place(x=19, y=124)

no2_button = tk.Button (root, text="2", bg='#000000', fg='white', width=6, height=1,command=lambda:click_button(2))
no2_button.place(x=96, y=124)

no_button = tk.Button (root, text="+", bg='#000000', fg='white', width=6, height=1,command=lambda: perform_operation(add, '+') )
no_button.place(x=174, y=124)

no3_button = tk.Button (root, text="3", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(3))
no3_button.place(x=19, y=154)

no4_button = tk.Button (root, text="4", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(4))
no4_button.place(x=96, y=154)

no11_button = tk.Button (root, text="-", bg='#000000', fg='white', width=6, height=1,command=lambda: perform_operation(subtract, ' - ') )
no11_button.place(x=174, y=154)

no5_button = tk.Button (root, text="5", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(5))
no5_button.place(x=19, y=184)

no6_button = tk.Button (root, text="6", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(6))
no6_button.place(x=96, y=184)

no12_button = tk.Button (root, text="*", bg='#000000', fg='white', width=6, height=1 ,command=lambda: perform_operation(multiply, ' * '))
no12_button.place(x=174, y=184)

no7_button = tk.Button (root, text="7", bg='#000000', fg='white', width=6, height=1 , command=lambda:click_button(7))
no7_button.place(x=19, y=214)

no8_button = tk.Button (root, text="8", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(8))
no8_button.place(x=96, y=214)

no13_button = tk.Button (root, text="/", bg='#000000', fg='white', width=6, height=1,command=lambda:perform_operation(divide, ' / ') )
no13_button.place(x=174, y=214)

no9_button = tk.Button (root, text="9", bg='#000000', fg='white', width=6, height=1 , command=lambda:click_button(9))
no9_button.place(x=19, y=244)

no0_button = tk.Button (root, text="0", bg='#000000', fg='white', width=6, height=1, command=lambda:click_button(0))
no0_button.place(x=96, y=244)

no14_button = tk.Button (root, text="=", bg='#000000', fg='white', width=6, height=1,command=calculate_result )
no14_button.place(x=174, y=244)

clear_button = tk.Button(root, text="C", bg='#000000', fg='white', width=6, height=1, command=clear_display)
clear_button.place(x=96, y=274) 

root.mainloop()

