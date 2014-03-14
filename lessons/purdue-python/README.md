![Python logo](http://www.python.org/static/community_logos/python-logo.png)

[Python](http://www.python.org) is a programming language gaining popularity in the sciences. It's open source, free, and has an array of existing libraries. There's a large, global community of Python users across many disciplines, making it a useful language when your work  starts intersecting with that of other professionals situated outside of your lab, campus, or research field.

###### &nbsp;

### Why Python?

Time to solution is determined by "human time" and "machine time." Every language makes a tradeoff.

* Python
* Perl
* Matlab
* Java
* Fortran
* C++
* C

Software Carpentry uses Python because it is:

* free
* cross-platform
* widely used
* well documented
* easier to learn

In addition to being widely accepted in the scientific community, Python has been used to create some notable web applications:

* YouTube
* DropBox
* Instagram
* Spotify
* Reddit

###### &nbsp;

### Purpose?

* Point 1: Teaching you Python is **not** the point of this course  
* Point 2: Making you a more effective scientist or engineer **is the point**
* Point 3: Build your programs slowly and thoughtfully, using the proper tools

###### &nbsp;

### Useful Python Links

#####	Python Website: [python.org](http://docs.python.org)

#####   Built-in Functions: [doc.python.org/2/library/functions.html](http://docs.python.org/2/library/functions.html)
* Functions (such as open, range, enumerate, etc.) that are always available without having to import a supporting library.

#####   Global Module Index: [docs.python.org/2/py-modindex.html](http://docs.python.org/2/py-modindex.html)
* Libraries that are part of the standard Python distribution, including built-in modules like os, sys, datetime, math, random...

#####   Google's Python Course: [code.google.com/edu/languages/google-python-class/](http://code.google.com/edu/languages/google-python-class/)

    
###### &nbsp;

### Python in Science

#####   [NumPy](http://numpy.scipy.org/)
* Fast arrays, used by almost every scientific Python package

#####   [SciPy](http://www.scipy.org/)
* Minimization, fitting, solvers, statistics, and more

#####   [matplotlib](http://matplotlib.sourceforge.net/)
* 2D and 3D plotting, maps

#####   [AstroPy](http://astropy.org) for astronomy
#####   [Biopython](http://biopython.org/wiki/Biopython) for bioinformatics
#####   [Sage](http://www.sagemath.org/) for mathematic analysis
#####   [SymPy](http://sympy.org/en/index.html) for symbolic mathematics
#####   [pandas](http://pandas.pydata.org/) data analysis and stats for categorical and time series data
				          
##### &nbsp;

### Schedule <font color="red">(REVISIT, JEFF!!!!!!!!!!)</font>

* Basics
* IPython Notebook
* Flow Control

	**Break**
* Lists
* matplotlib
* Input and Output

	**Break**
* Functions
* Tuples, Sets, and Dictionaries

###### &nbsp;

### Python Basics

From your terminal, type in "python" to launch the Python interpreter: 

	swc@swc:~$ python
	Python 2.7.4 (default, Sep 26 2013, 03:20:56)
	[GCC 4.7.3] on linux 2
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	
Python is an interpreted language, so there is no separate compilation step. Try typing in "1 + 2" and hitting Enter:

	>>> 1 + 2
	3

Try entering "Nikola" + "Tesla":

	>>> "Nikola" + "Tesla"
	'NikolaTesla'
	
Unlike Matlab, Python doesn't care whether strings are denoted with a single or double quote. However, you'll need to be careful with nested quotes!

Also note that Python uses the "+" operator for both numbers and strings. It tries to make sense of how such operators should act on whatever type of parameters it encounters. 

Try typing in '3 * "Tesla"':

	>>> 3 * "Tesla"
	'TeslaTeslaTesla'
	
Okay, now try '3 + "Tesla"':

	>>> 3 + "Tesla"
	Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	
Oops! Sometimes Python finds no good reason for handling certain operand combinations. (This is because Python is a strongly-typed language. However, if you become a Python guru, you can override these limitations!)

Let's try entering Python commands into a file, so that we don't have to continuously work from the command line. First exit the Python shell by entering CTRL-D. Next, create a new Python program named "easyas.py" using the "nano" editor:

	swc@swc:~$ nano -ET4 easyas.py
	
Once the editor opens up, enter the following, preferably using 4 spaces for each level of indentation. Python will recognize consistent use of tabs **or** spaces, but it will choke on a mix of tabs and spaces! By using the option -ET4 in the previous command, we are telling the nano editor to convert tabs to 4 spaces.

	for i in range(10):
		if i % 2 == 0:
		    print i, "Thomas",
		else:
		    print "Edison"
	
To save your work within nano,

1. Ctrl + O to output the file
2. Press 'Enter' to confirm file name
3. Ctrl + X to exit the editor

Now run the program:

	swc@swc:~$ python easyas.py
	
Was the output what you expected? 

To keep from having to add the -ET4 option everytime we run nano, let's make a bash shell alias:

    swc@swc:~$ alias nano="nano -ET4"
	
You can review all your current alias settings by entering 'alias' at the prompt.
	
Let's extend the capabilities of our program by importing a "built-in" Python module called "time." To see all 303 modules in the Python Standard Library, search the web for "[Python Standard Library](http://docs.python.org/2/library/)." If you don't find what you need in the standard library, there are an additional 40,974 packages in the [Python Package Index](https://pypi.python.org/pypi) (PyPI).

	import time          # This is a new line
	print time.asctime() # This is another line that changed

	for i in range(10):
		if i % 2 == 0:
		    print i, "Thomas",
		else:
		    print "Edison"
			
Note the use of the pound symbol to add comments. Try running your program again. Any surprises?

What if you wanted to know what other functions might be available from the time module? You might look it up online, of course, at: [http://docs.python.org/2/library/time.html](http://docs.python.org/2/library/time.html)
	
Might there be better way?

Get out of the Python shell (CTRL+D) and try starting up a program called [IPython](http://ipython.org/), which is an "enhanced" Python shell:

	swc@swc:~$ ipython
	
	In  [1]:
	
Type in the following Python code:

	In  [1]: for letter in "George Westinghouse": 
	    ...:     print letter,
		...:
	G e o r g e  W e s t i n g h o u s e
	
	In  [2]:
	
Note that the string "George Westinghouse" is an iterable object; that is, it allows us to loop over its constituent elements, one at a time, without having to create an explicit indexing framework. We will later return to this concept.

What do you think this command will accomplish?

	In  [2]: %run easyas.py
	
Now remember that we launched into IPython because we wanted to know more about the "time" module. So type in:

	In  [3]: time?
	
We can now see the documentation for the "time" module. You can use the down arrow or "space" bar to move through the text; you are in the less pager. (If we had not already run the easyas.py program, we would have needed to "import time" within IPython, or we would have gotten information about IPython's "magic" command called "time.")

Use "q" to exit the documentation. Since IPython knows about the "time" module, it will gladly help us out with tab completion. So type in the following, and then hit the "tab" key after entering the period...

	In  [4]: time.
	
What happened? Now type an "a" and hit tab. Then type an "s" and hit tab. Finally, add closed parentheses to call the function, and hit "Enter".

	In  [4]: time.asctime()
	Out [4]: 'Mon Mar 17 14:08:44 2014'

Any command starting with "%" is considered a "magic" command in IPython. Now try

	In  [5]: %edit easyas.py
	
You are now in the 'vi' editor, which is the default editor for IPython. This can be changed to the editor of your preference, but we're not going to worry about that now. Exit out of the vi editor by typing ":", then "q", then "ENTER."

Now try:

	In  [6]: !ls
	
By putting an exclamation mark (bang) in front of a command, you tell IPython to issue the command to the bash shell. So IPython allows you to experiment with Python code, easily jumping back and forth between an "enhanced" Python shell, your text editor, and the file system.

To see **all** the "magic" commands that IPython knows about, type in:

	In [7]: %lsmagic
	
As you are reminded each time you start IPython, its four most useful commands are:

* ? -- Provides an overview of IPython's features
* %quickref -- Quick reference
* help -- Python's own help system
* object? -- Details about 'object'; use 'object??' for extra details

As in the bash shell, you can use the up and down arrow keys to move through your input history. Your inputs and outputs are stored in variables In and Out. Try this:

	In  [8]: Out[4]
	Out [8]: 'Mon Mar 17 14:08:44 2014'
	
Want to know how fast your program is executing? Try

	In  [9]: %timeit %run easyas.py
	
Finally, let visit the "Zen of Python," by entering:

	In  [10]: import this
	
To summarize, we know that:

* Python is a widely used language
* Python programs consist of indented text that can be modified in any text editor
* The Python shell is interactive
* IPython provides an "enhanced" shell for exploration of Python programs

Next, we're going to look at IPython notebooks, which combine the power of IPython with the flexibility of web pages. It's something less that a full blown IDE (interactive development environment), but much better for mixing code with text.

Here is an example of a Python IDE:

<img style="width:600px;" src="http://software-carpentry.org/v5/novice/extras/img/debugger-screenshot.png">

To open up an IPython notebook, go to the bash shell prompt and type

	In  [11]: ipython notebook
	


<ol>
  <li><a href="python-00-resize-image.ipynb">Resizing an Image</a></li>
  <li><a href="python-01-functions.ipynb">Creating Functions</a></li>
  <li><a href="python-02-loops-indexing.ipynb">Repeating Things</a></li>
  <li><a href="python-03-conditionals-defensive.ipynb">Making Decisions and Programming Defensively</a></li>
  <li><a href="python-04-files-lists.ipynb">Files and Lists</a></li>
  <li><a href="python-05-errors.ipynb">Handling Errors</a></li>
  <li><a href="python-06-testing.ipynb">Testing</a></li>
  <li><a href="python-07-dla.ipynb">Growing a Program</a></li>
  <li><a href="python-08-numpy.ipynb">Number Crunching</a></li>
  <li><a href="python-09-cmdline.ipynb">Back to the Command Line</a></li>
 </ol>



	

	
	




	
	
	
