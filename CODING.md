## Coding Document

### Coding env

- language = "python2.7"
- style = "PEP8"

### Protocol

- Create modules.
- Name the modules properly.
- Dont edit other modules without permission from the owner.
- Each of your module should contain a README.md for instructions of usage.
- The module should be documented properly.
- Documentation shoud be in the code, as comments. (Refer PEP8)
- For those using sublime, the Anaconda extension does autformatting of PEP8 errors
- Log everything :-)

### Comments

- Try to be as abstract as possible.
- Please review the code before commiting.
- Proper naming should be given, long variable names are fine.

### Representation

"A => B" can be representated as node "A" with a directed edge to node "B"  
A graph can be represented as a dictionary.  
eg. graph = {
"A": ["B", "C", ('or', ["E", "F"])],
"B": ["D"]
}

### Variable notations

**
We need to decide if the following should be functions are arrays, global or local, etc.
**

days = []  
 Set of working days.

periods(d) = [i + 1 for i in range(8)]  
 start from 1 (not 0)  
 the above code says that there are 8 periods in day "d".

teachers = []  
 Teacher names, or unique id's

subjects = []  
 Subject names, or unique id's

groups = []  
 Group names, or unique id's

(t, s, g, n)  
 Represents a lesson to be scheduled.  
 teacher "t" teaches subject "s" to group for n'th time in a week

duration(t, s, g, n) = k  
 "k" is an integer, number of periods of the lesson  
 refer page 6

lessons_teacher(t) = [(t', s, g, n) where t' = t]  
 lessons for a given teacher "t"

lessons_group(g) = [(t, s, g', n) where g' = g]  
 lessons for a group "g"

#### Basic Variables

x'(t, s, g, n, d, p)  
 represents that lesson (t, s, g, n) begins in day d and period p  
 p should be valid periods  
**Constraints:**  
 min(periods(d)) <= p <= max(periods(d)) - durations(t, s, g, n) + 1

#### Implied Variables

x(t, s, g, n, d, p)  
 Formed for each lesson (t, s, g, n), each working day d and each working period p  
 Says that the lesson (t, s, g, n) is given in day d period p  
 Note the difference between x'(t, s, g, n, d, p)  
 See the implications and constraints in page 7

x(t, s, g, n, d)  
 Formed for each lesson (t, s, g, n) and each working day.  
 Represents that (t, s, g, n) is held in day d

x(t, d, p)  
 Formed for each teacher t, working day d and working period p  
 Represents that teacher t gives some lesson in day d and period p

x(g, d, p)  
 Formed for each group g, working day d and working period p  
 Represents that group g takes some lesson in day d and period p

x(t, d)  
 Formed for each teacher t and working day d  
 teacher t teaches during day d

x(t, p)  
 Formed for each teacher t and working period p  
 Represents that teacher t gives lessons in period p  
 Read page 8(end) and 9(begining) to learn why this is needed  
 _I have a doubt in this, if any one understands, please ping me!_

x(g, p) and x(g, d) can be used if required, but who cares about the students anyways :-P

#### Idle periods

Free in those periods but not before and after.

i(k, t, d, p)  
 Formed for every t, d, p and valid k  
 Represents that teacher t is free in day d starting from period d for k periods.

i(k, t, d)  
 Formed for every t, d, and valid k  
 Represents that teacher t is free for k periods in day d.

i(k, t)  
 Formed for every t and valid k  
 Represents that teacher t is free for k periods.

i(t, d, p)  
 Formed for every t, d, p  
 Represents that teacher t in idle in day d from period p

### Tasks

Please write your name in the brackets provided, before the task, if you wish to take it :-).

- (Adithya) [id: 1] A function(s) that takes in a set of inputs and returns a unique variable, in string format.  
  eg.  
   var_type = x'  
   t = 1  
   g = 2  
   should return a unique id for the specific, which will be used to index into the dict.

- (Adithya) [id: 2] A task to initialize the graph by creating all the nodes and initializing all the possible variables, given a few inputs.  
  ie, all the days, periods, teachers, subjects, groups, lessons given.

- () [id: 3] Formalise input processing and representation

- () [id: 4] Formalise conversion to implications based on input-representation (as strings ?)

- () [id: 5] Creating all the basic implications (implications that define correctness)  
  Make some edges :-)  
  All implications till page 10.  
  Not the requirement implications.

- () [id: 6] Creating correctness implications  
  Make some edges :-)

- () [id: 7] Creating requirement implications  
  Make some edges :-)

- (Mayank) [id: 8] Convert string to graphs ?

- (Mayank) [id: 9] Graph to Z3 input

#Indpendently

- () [id: 10] decode Z3 output

- () [id: 11] Gui front-end to receive input and to display output

#NOTE  
This is still incomplete.  
Additions to this are encouraged :-)
