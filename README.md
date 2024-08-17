# Timetable Scheduling

Timetable scheduling is a complex and challenging problem, especially in educational institutions where multiple constraints must be balanced. The goal is to create a timetable that assigns classes, teachers, and rooms to specific time slots, ensuring that all necessary conditions are met.

## Constraint Satisfaction Problem

The timetable scheduling problem can be viewed as a Constraint Satisfaction Problem (CSP), where the objective is to find a solution that satisfies a set of constraints. These constraints can be broadly categorized into two types:

1. **Correctness Requirements:**

   - Every lesson must be scheduled exactly once.
   - No teacher or student group should have overlapping classes.
   - Rooms must be allocated efficiently without conflicts.

2. **Comfort Requirements:**
   - Preferences for teaching hours.
   - Minimizing the number of working days for teachers.
   - Avoiding long stretches of consecutive classes.

## Approach

Approach involves converting the timetable scheduling problem into a SAT (Satisfiability) problem, which can be efficiently solved using the Z3 SMT (Satisfiability Modulo Theories) solver. Here's how it works:

1. **Custom Query Language:** We developed a user-friendly query language that allows users to define their scheduling constraints. This language serves as the interface between the user’s requirements and the underlying SAT problem.

2. **Constraint Encoding:** The user-defined constraints are translated into propositional logic, resulting in a conjunctive normal form (CNF) formula. This formula represents the scheduling problem in a form that the Z3 solver can process.

3. **Z3 Solver:** The Z3 solver is then used to find solutions that satisfy the CNF formula. These solutions correspond to valid timetables that meet all the defined constraints.

## Use Cases

1. **University Timetabling:**

   - **Scenario:** A university needs to schedule classes across different departments.
   - **Solution:** Define constraints to avoid class overlaps and generate a valid timetable.

2. **Meeting Scheduling for Corporates:**

   - **Scenario:** A corporate office needs to schedule meetings for multiple teams
   - **Solution:** Define constraints like no overlapping meetings for key participants

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write tests and ensure all existing tests pass.
4. Submit a pull request with a detailed explanation of your changes.

### Code Owners

- [immkg](https://github.com/immkg) - Project Maintainer

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please open an issue on the [GitHub repository](https://github.com/immkg/general-scheduler/issues).
