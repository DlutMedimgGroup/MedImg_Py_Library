## The Zen of Python

### Beautiful is better than ugly.

### Explicit is better than implicit.

### Simple is better than complex.

### Complex is better than complicated.

### Flat is better than nested.

### Sparse is better than dense.

### Readability counts.

## Code layout and writing standard

### Tabs or Spaces

We suggest that spaces are the preferred indentation method.

Python 3 disallows mixing the use of tabs and spaces for indentation.

Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.

When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using -tt these warnings become errors. 

These options above are highly recommended to check whether mixing tabs and spaces or not when programming.

### Line feed
 
Generally, one statement per line.

In consideration of aesthetics as well as the convenience for testing, use blank lines to deal with long statements.

### Three ways to change line

> First, three single quotes

```python
print (''' I'm a programmer,
           I just started learning Python''')
```

> Second, Three double quotes

```python
print (""" I'm a programmer,
           I just started learning Python""")
```

> Third, end with a backslash

```python
print ("I'm a programmer,\
        I just started learning Python")
```

> Use ( ), { }, [ ]，long lines can be broken over multiple lines by wrapping expressions in parentheses

```python
test2 = ('csdn '
'cssdn')
```

#### If the conditional block is too long, write in multiple lines

It is noteworthy that some keywords consisting of two characters which are followed by a space and a left parenthese are indented 4 spaces. And there would be a visual clutter in case the characters inside would also be indented 4 spaces.

#### Line feed in multiple lines

In multiple lines blocks, the right parentheses, brackets and braces which as the end of the blocks on the continued line, should be aligned with the first character inside the blocks.
```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```
### Maximum line length

We suggest that make sure all lines to a maximum of 80 characters.

### Space in expression statements

#### Don't use spaces inside parentheses, brackets or braces

>Yes: spam(ham[1], {eggs: 2})

>No:  spam( ham[ 1 ], { eggs: 2 } )

#### Don't use spaces before Comma, colon or semicolon. Spaces can be added after them

>Yes: if x == 4: print x, y; x, y = y, x

>No:  if x == 4 : print x , y ; x , y = y , x

#### Don't use spaces before the left parentheses

>Yes: spam(1)

>No:  spam (1)

#### Don't use spaces before the open parenthesis that starts the argument list of a function call

> Yes: dict['key'] = list[index]

> No:  dict ['key'] = list [index]

#### Add a single space around an assignment operator, and no more than one space for aligning it with others
> Yes: x = 1

> No:  x=1

#### Don't use spaces around a default parameter operator.
> Yes: def complex(real, imag=0.0):

> No:  def complex(real, imag = 0.0):

### Blank lines 
1. Separate top-level function and class definitions with two blank lines.
2. Method definitions inside a class are separated by a single blank line.
3. Use blank lines in functions, sparingly, to indicate logical sections.

## Comments
### Comments for the code’s overall function
The direction of the code’s overall function,which aims at explaining what function can the whole code implement, is always put at the very beginning for others to read and understand.

Pay attention that your direction is not expected to be long and complicated,just let others know why you create the code.As to the function that some specific parts implement,you can document them in your code as block comments.

The overall function comment is always presented in the form of a multiline comment.In order to make it different from single-line comment,the following example is recommended:

```python
"""
Script Name 	: 
Author		: 
Created		: 
Last Modified   : 
Version		:  
Modifications   :
Description	:  
"""
```
### Block Comments
The most needed parts you should explain in your comments are those skillful or difficult to understand.

If you are going to make an explanation when you check your code next time,you’d better comment it right when you finished.

You’d better add several lines of comments before complicated operation or parts in your code.

Here is an example:
```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.
# param para1: meaning of the first parameter
# param para2: meaning of the second parameter
# param para3: meaning of the third parameter
# rtype:
# return:
# func:
```
What else,do not describe all your code,just explain what you think needed,such as function,special names and so on,so that others can read or modify or use your code faster.

More over,it is better for block comments lined up with class and function,to make the code terse and beautiful.
### Single-line comments (inline comments)

We recommend you to comment just at the end of the same line,if the code on the line is not so conspicuous.
```python
NULL_BALLOT = Ballot(-1, -1)  # sorts before all real ballots
```
## Naming Conventions
### The abbreviations of the names

1. Frequently-used abbreviations,such as XML ID and so on,should be capitalized only the first letter, like XmlParser.

2. If there are long words in the names,abbreviate them in the form accepted through common practice.

>E.g.

- func is short for function
- txt is short for text
- obj is short for object 
- cnt is short for count
- num is short for number

### Variable names
#### Names of global variable
Use '_' to divide two capitalized words name,e.g.
> NUMBER 

>COLOR_WRITE 

If the variable is an internal variable,add a '_' at the beginning of its name,e.g.

> _COLOR_WRITE

"Internal" means that the variable is available just in the module,or it is protected or private in the class.

#### Other variable names

Other variable can include local variable,instance variable,static variable.

When naming them,use lower-case letters ,and use a '_' to divide two words,e.g.

> this_is_a_var 

Similarly,If the variable is an internal variable,add a '_' at the beginning of its name,e.g.
> _this_is_a_var

### Class names

Class names should normally use the CapWords convention,e.g.
> AdStats 

> ConfigUtil 

If the class is an internal class,add a '_' at the beginning of its name.

e.g.
> _ConfigUtil

### Function names

Function names should be lowercase, with words separated by underscores as necessary to improve readability,
e.g.

> get_name() 

> count_number() 

Similarly,If the function is an internal function,add a '_' at the beginning of its name,e.g.

> _get_name()

### Common abbreviations appendix

> E.g.

- dst = destination 
- src = source
- (to be continued)

## Other suggestions
### Something about the use of function main()
Even a file that you crate it as a script,should be imported,at the same time just import it should not make its main function operate,for it is a kind of side effect.Its main function should be packaged in a main() function.

Before the main function operate,your code always check if``__name__=='__main__'``,so that the function will not operate when you import the module.

E.g.
```python
def main()：
    ...
if __name__ == '__main__':
    main()
```
