# Equation Solver

This program was made as part of my "Projet Personnel".
It allows you to find the solution to quadratic functions, absolute value functions, square root functions and rational functions.

## Dependencies

To run this program, you must first have Python installed, as well as the python library "matplotlib".
This only needs to be done once.

Get the latest Python standalone installer from https://www.python.org/downloads/ .

When installing python, make to sure to check to option *Add python.exe to PATH*

After Python is installed, open your terminal and run `pip install matplotlib` .

# How to use

Download the source code and extract the ZIP file.

To open the program, simply run the `run.bat` file.

For technical users:
Standalone solvers (in terminal) do exist but they will probably be released at a later date (if ever) if i do take the time to fix them up.

## Select an equation

When you open the program, you will be met with an introduction page telling you to "Select a tab to get started".
Tabs are located at the top of the program (Home, Quadratic, Absolute Value, Square Root, Rational).
All tabs are active at once, they do not need to be opened and closed manually for each use. They also store the values you input and answers, while you change between them (the data is only stored for as long as you keep the program open).

# Equations

This solver allows for 6 different equations:

 - Quadratic
 - Absolute Value
 - Square Root
 - Rational
 - Logarithmic
 - Exponential

In addition to this, you are able to determine how many decimal positions answers will have (significant figures).
If you chose to leave that designated field blank, the program will simply show as many decimals as the answer has.

At the top of the home tab, there is a field to select which answer format you want.
By default, the program will show answers in decimal format.

It is not recommended to request decimal numbers at more than 16 significant figures due to computer imprecision (computers cannot perfectly store decimal numbers, so small rounding errors start appearing after too many decimal positions are taken into account).

## Quadratic

The program allows you to find the solutions to a quadratic equation of the form:

$$
y=ax²+bx+c
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a, 0 for b, c and y.

## Absolute value

The program allows you to find the solutions to an absolute value equation of the form:

$$
y=a|b(x-h)|+k
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a and b, 0 for h, k and y.


## Square Root

The program allows you to find the solution to a square root equation of the form:

$$
 y=a\sqrt{b\left(x-h\right)}+k
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a and b, 0 for h, k and y.

## Rational

The program allows you to find the solution to a square root equation of the form:

$$
 y=\frac{a}{b(x-h)}+k
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a and b, 0 for h, k and y.

## Logarithmic

The program allows you to find the solution to a logarithmic equation of the form:

$$
 y=a\ \log_{c}{(b(x-h))}+k
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a and b, 10 for c, 0 for h, k and y.
For c, you can enter 'e' to use the natural logarithm function (ln).

## Exponential

The program allows you to find the solution to a logarithmic equation of the form:

$$
 y=a(c)^{b(x-h)}+k
$$

A reference image is provided to indicate the form.

To input the values of your equation, simply write them in their designated fields.
If you do not enter a value in a field, it will use its default value:
1 for a and b, 10 for c, 0 for h, k and y.

## Results box

At the bottom of each solver window, there is a box where answers will be written.

The `copy results` button will copy **all** results currently in the box.

The `clear results` button will, as it's name says, clear all results currently in the box.
‎ 
‎ 
‎ 
# ***-** 834*

## License

Code: MIT License  
Documentation and visuals: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)  
See the [LICENSE](LICENSE) file for full details.














