# PlaneHelper
A program for working with planes for the game Sprocket

## Description
This program was originally developed to find the third coordinate of a point lying in a plane, given its two known coordinates — for the game Sprocket, since its current editor does not support such functions. However, it was later decided to create a structure that would allow adding other features in the future (for example, rotating the plane by a given angle around an arbitrary axis).

## How to use
The program uses a classic and straightforward method for interaction — the console and commands. When you launch the program, its console opens, and you enter the required commands there.

List of commands:
| Command | Description | Syntax |
|---------|-------------|--------|
| help | Show the list of all commands | help |
| setplane | Set a new plane | setplane [x1] [y1] [z1] [x2] [y2] [z2] [x3] [y3] [z3] |
| plane | Show current plane info (equation and normal) | plane |
| x? | Find X from Y and Z for a point in the plane | x? [Y] [Z] |
| y? | Find Y from X and Z for a point in the plane | y? [X] [Z] |
| z? | Find Z from X and Y for a point in the plane | z? [X] [Y] |

## Example of program output (console log)
In this example, we defined a plane using three points with coordinates (65, -61, 2048), (-65, -61, 2048), and (159, -149, 430), and then found the Y coordinate of a point lying in that plane, given its known X and Z coordinates.
```console
Версия программы: 0.1 Beta
Воспользуйтесь командой "help" для просмотра списка команд
setplane 65 -61 2048 -65 -61 2048 159 -149 430
Плоскость 0.00 * X + -1.00 * Y + 0.05 * Z + -172.13 = 0 успешно задана
y? -96 1304
Y = -101.46
y? 33.9 1403
Y = -96.08
```
