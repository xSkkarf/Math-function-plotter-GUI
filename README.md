# Math Function Plotter GUI

## Overview

The Math Function Plotter GUI is a desktop application designed to plot mathematical functions. Built using PySide2 for the GUI and Matplotlib for plotting, this application allows users to input mathematical expressions, specify the range for the x-axis, and view the resulting plot.

## Features

- **Function Input**: Users can enter mathematical functions with support for various operators and functions.
- **Range Specification**: Define the x-axis range with minimum and maximum values.
- **Step Size**: Set the interval between plotted points.
- **Plotting**: Generate and display the graph based on user input.
- **Error Handling**: Real-time validation of inputs with error messages.
- **Instructions**: Access detailed instructions on how to use the application.

## Supported Mathematical Functions

- **Operators**: `+`, `-`, `/`, `*`, `^` (exponentiation)
- **Trigonometric Functions**: `sin(x)`, `cos(x)`, `tan(x)`, etc.
- **Square Root**: `sqrt(x)`
- **Logarithms**: `log(x)`, `log10(x)`, `log2(x)`
- **Constants**: `pi`, `e^x` (as `exp(x)`)


## Program Interface
![Screenshot from 2024-07-21 18-40-20](https://github.com/user-attachments/assets/bc56d134-aba1-4d34-8310-790904e65379)

## Instructions
![Screenshot from 2024-07-21 18-06-00](https://github.com/user-attachments/assets/aecd0c4f-98b6-4ca6-bb1b-9626582df849)

## Error Messages

The application provides feedback on input errors through visual cues. Below are descriptions of the various error states and corresponding images.

### 1. Plot Function is an Empty String

- **Description**: This error occurs when the plot function input field is left empty.
![Screenshot from 2024-07-21 18-06-16](https://github.com/user-attachments/assets/b57208ca-206f-4ecd-ba75-966a4c2b072a)

### 2. Plot Function is Not a Valid Mathematical Function

- **Description**: This error indicates that the input provided for the plot function is not a valid mathematical expression.
![Screenshot from 2024-07-21 18-06-40](https://github.com/user-attachments/assets/aa711f6e-eeff-4e70-b6df-a8778a9ce5c3)

### 3. X Min is an Empty String

- **Description**: This error is shown when the minimum x value input field is left empty.
![Screenshot from 2024-07-21 18-07-47](https://github.com/user-attachments/assets/752d9df1-b26a-47c9-b7f8-e8204e70ff21)

### 4. X Min is Not a Valid Number

- **Description**: This error occurs when the minimum x value input is not a valid number.
![Screenshot from 2024-07-21 18-07-59](https://github.com/user-attachments/assets/85887b5b-f623-42c0-957c-c72d23a2b56c)

### 5. X Max is an Empty String

- **Description**: This error appears when the maximum x value input field is left empty.
![Screenshot from 2024-07-21 18-08-11](https://github.com/user-attachments/assets/fc7ed852-e914-44e9-bf88-146d227b3f30)

### 6. X Max is Not a Valid Number

- **Description**: This error is displayed when the maximum x value input is not a valid number.
![Screenshot from 2024-07-21 18-08-31](https://github.com/user-attachments/assets/d3c34c1d-0ce4-4414-a931-c8fd5f2b06ec)

### 7. X Max is Not Greater Than X Min

- **Description**: This error indicates that the maximum x value is not greater than the minimum x value.
![Screenshot from 2024-07-21 18-08-44](https://github.com/user-attachments/assets/6ea1eac9-0ca8-40fe-95a7-cf8f9800d0a0)

### 8. Step is an Empty String

- **Description**: This error is shown when the step size input field is left empty.
![Screenshot from 2024-07-21 18-08-57](https://github.com/user-attachments/assets/8f421139-9401-4a41-ae79-dbb7453039b2)

### 9. Step is Not a Valid Number

- **Description**: This error appears when the step size input is not a valid number.
![Screenshot from 2024-07-21 18-09-13](https://github.com/user-attachments/assets/77d5c337-deb7-4270-a5d4-6474bcfe20d4)

### 10. Step is Zero

- **Description**: This error occurs when the step size is set to zero.
![Screenshot from 2024-07-21 18-09-25](https://github.com/user-attachments/assets/4ccb55b3-e678-4338-8749-94612e21658f)

## Successful plots:
- f(x) = sin(x)
![Screenshot from 2024-07-21 18-09-43](https://github.com/user-attachments/assets/ee9cd393-2d0e-472f-84ef-f2f281e7a31b)

- f(x) = x^3 + 6\*x^2 - 3\*x + 6
![image](https://github.com/user-attachments/assets/b2d15717-aa2f-4041-bb40-5abd45ec37c7)

## Resources:
1. [Pyside2 documentation](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html)
2. [Parwiz Forogh - YouTube - Pyside2 playlist](https://www.youtube.com/watch?v=oQTxJrDRCxg&list=PL1FgJUcJJ03tiCC6a7sF8NKLBPY4jRjmS&index=1)
3. [Geeks for geeks - Python Regex](https://www.geeksforgeeks.org/python-regex/)
4. [Corey Schafer - YouTube - Python Regex tutorial](https://www.youtube.com/watch?v=K8L6KVGG-7o)
5. [PythonGUIs - Matplotlib with Pyside2](https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/)
