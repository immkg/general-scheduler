# Coding

## Protocol

- Create modules. Name the modules properly.
- Each of your module should contain a README.md.
- The module should be documented properly.
- Log everything :-)

## Representation

"A => B" can be represented as node "A" with a directed edge to node "B". A graph can be represented as a dictionary.

```
graph = {
"A": ["B", "C", ('or', ["E", "F"])],
"B": ["D"]
}
```

## Variable notations

`days = []`  
Set of working days.

`periods(d) = [i + 1 for i in range(8)]`  
start from 1 (not 0)  
the above code says that there are 8 periods in day "d".

`teachers = []`  
Teacher names, or unique id's

`subjects = []`  
Subject names, or unique id's

`groups = []`  
Group names, or unique id's

`(t, s, g, n)`  
Represents a lesson to be scheduled.  
teacher "t" teaches subject "s" to group for n'th time in a week

`duration(t, s, g, n) = k`  
"k" is an integer, number of periods of the lesson

`lessons_teacher(t) = [(t', s, g, n) where t' = t] `
lessons for a given teacher "t"

`lessons_group(g) = [(t, s, g', n) where g' = g]  `
lessons for a group "g"

### Basic Variables

`x'(t, s, g, n, d, p)  `  
represents that lesson (t, s, g, n) begins in day d and period p  
 p should be valid periods  
**Constraints:**  
 `min(periods(d)) <= p <= max(periods(d)) - durations(t, s, g, n) + 1`

### Implied Variables

`x(t, s, g, n, d, p)`  
 Formed for each lesson (t, s, g, n), each working day d and each working period p  
 Says that the lesson (t, s, g, n) is given in day d period p  
 Note the difference between x'(t, s, g, n, d, p)  
 See the implications and constraints in page 7

`x(t, s, g, n, d)`  
 Formed for each lesson (t, s, g, n) and each working day.  
 Represents that (t, s, g, n) is held in day d

`x(t, d, p)`  
 Formed for each teacher t, working day d and working period p  
 Represents that teacher t gives some lesson in day d and period p

`x(g, d, p)`  
 Formed for each group g, working day d and working period p  
 Represents that group g takes some lesson in day d and period p

`x(t, d)`  
 Formed for each teacher t and working day d  
 teacher t teaches during day d

`x(t, p)`  
 Formed for each teacher t and working period p  
 Represents that teacher t gives lessons in period p  
 Read page 8(end) and 9(begining) to learn why this is needed  
 _I have a doubt in this, if any one understands, please ping me!_

`x(g, p) and x(g, d)` can be used if required, but who cares about the students anyways :-P

### Idle periods

Free in those periods but not before and after.

`i(k, t, d, p)`  
 Formed for every t, d, p and valid k  
 Represents that teacher t is free in day d starting from period d for k periods.

`i(k, t, d)`  
 Formed for every t, d, and valid k  
 Represents that teacher t is free for k periods in day d.

`i(k, t)`  
 Formed for every t and valid k  
 Represents that teacher t is free for k periods.

`i(t, d, p)`  
 Formed for every t, d, p  
 Represents that teacher t in idle in day d from period p
