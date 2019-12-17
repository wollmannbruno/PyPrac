# Lesson2 / Numbers, Files, Lists, and Linters

- [x] Numbers
Video https://vimeo.com/244128549
Length is 9 minutes
 
- [x] Files
Video https://vimeo.com/244127459
Length is 10 minutes
 
- [x] Lists
Video https://vimeo.com/244257596
Length is 6 minutes
 
- [x] List Slices
Video https://vimeo.com/244259492
Length is 4 minutes  
 
- [x] Lists are Mutable
Video https://vimeo.com/244287000
Length is 5 minutes
 
- [x] Tuples
Video https://vimeo.com/244153105
Length is 3 minutes
 
- [x] Using .join()
​Video https://vimeo.com/245464488
Length is 3 minutes
 
- [x] sys.argv
Video https://vimeo.com/245464766
Length is 2 minutes
 
- [x] Linters
Video https://vimeo.com/245102246
Length is 6 minutes


# Additional Content:

- [x] [Automate the Boring Stuff with Python (Chapter 4 on Strings)](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiY3k3eThpZGRsNmQ1OTFnbXg0cG4iLCJ1cmwiOiJodHRwczovL2F1dG9tYXRldGhlYm9yaW5nc3R1ZmYuY29tL2NoYXB0ZXI0Lz9fX3M9OGN2cHNtd2pwc3ZuZjI4eXR3Z2EifQ)

*Up through the section named "Removing Values from Lists with del Statements"*

- [x] [Dive Into Python, Lists](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiY3k3eThpZGRsNmQ1OTFnbXg0cG4iLCJ1cmwiOiJodHRwczovL3d3dy5kaXZlaW50by5vcmcvcHl0aG9uMy9uYXRpdmUtZGF0YXR5cGVzLmh0bWw_X19zPThjdnBzbXdqcHN2bmYyOHl0d2dhI2xpc3RzIn0)


# Exercises

Reference code for these exercises is posted on GitHub at:
(https://github.com/ktbyers/pynet/tree/master/learning_python/lesson2)



- [x] 1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).


- [ ] 2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.


- [ ] 3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".


- [ ] 4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.


- [ ] 5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.


# CLASS OUTLINE

1. Numbers (VIDEO1)
   1. Creating an integer type  [0:10]
   2. Arithmetic Operators [0:23]
      1. Modulo Operator [0:59]
      2. Raise to the power [1:19]
      3. Division behavior and Python2 [1:31]
         1. from \_\_future\_\_ import division [2:44]
      4. Whitespace in Python [3:32]
   3. Type float [4:00]
   4. Type casting an integer to a float [4:50]
   5. Strange math behavior of .1 + .2 [5:53]
   6. Increment by one [8:00]
 
2. Files (VIDEO2)
   1. Open a file for reading [0:26]
      1. f.read() [0:58]
      2. f.seek(0) [1:43]
      3. f.close() [2:22]
   2. f.readline() [3:23]
   3. f.readlines() [3:56]
   4. Context manager [5:04]
      1. Automatic close [5:56]
   5. Writing a file [6:30]
      1. f.flush() [7:30]
      2. Destructive operation [7:43]
   6. Append a file [8:12]
 
3. Lists (VIDEO3)
   1. Data that is inherently sequential [0:06]
   2. Examples [0:19]
   3. Creating a list [0:56]
      1. Creating a list with existing values [1:16]
      2. Lists can store different types of data [1:39]
      3. Accessing element 0, 1, 2, 3 [1:56]
      4. Changing the value of an element [2:23]
   4. List methods [2:53]
      1. append() [2:57]
      2. list concatenation [3:13]
      3. list.extend() [3:48]
      4. removing elements [4:14]
         1. my_list.pop() [4:22]
         2. my_list.pop(0) [4:37]
         3. del my_list\[0] [4:58]
 
4. List slices (VIDEO4)
   1. Read from show_version.txt [0:12]
   2. Creating new lists from an existing list [0:47]
   3. First index is included [1:07]
   4. Last index is excluded [1:14]
   5. First number is excluded (go to beginning) [1:39]
   6. Last number is excluded (go to end) [2:02]
   7. Can use negative indices [3:21]
 
5. Lists are Mutable (VIDEO5)
   1. What does mutable mean [0:14]
   2. Mutable data types (lists, dictionaries) [2:13]
   3. Immutable data types (strings, numbers) [3:03]
   4. Be careful with copying lists [4:48]
 
6. Tuples (VIDEO6)
   1. Use parenthesis and not brackets [0:19]
   2. Why use tuples? [0:34]
   3. Behaves like a list, but can't modify it [0:48]
   4. Tuples use less memory [2:07]
   5. Type cast as a list [2:21]
 
7. Using .join() (VIDEO7)
   1. Review of using .split()   [0:11]
      1. Split returns a list   [0:34]
   2. .join() reunites the parts   [0:59]
      1. String separator, pass in a list   [1:06]
      2. Separator between each element   [1:30] 
      3. .join() is a string method   [1:35]
   3. Example using an IP address   [2:26]

8. sys.argv (VIDEO8)
   1. Behavior of sys.argv   [0:25]
      1. Returns a list, element1 is the program name   [0:31]
      2. Additional args are remaining elements   [0:54]

9. Linters (VIDEO9)
   1. Advantages of using linters [0:04]
      1. Improve readability [0:23]
      2. Flag obvious errors and save debugging time [0:40]
      3. Flag potential problems [0:50]
   2. Two most common linters: pylint and pycodestyle [1:01]
      1. Installing pylint and pycodestyle linters [1:20]
      2. Example using pylint and pycodestyle [1:35]
      3. Example using pylint and pycodestyle [2:08]
   3. Using pylama and a setup.cfg file [3:35]
   4. You decide what characteristics matters [4:07]
   5. Zero errors [5:03]
   6. Integrate with CI [5:16]
