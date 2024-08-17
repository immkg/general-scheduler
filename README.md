# README

# Team MORAGS

- Adithya
- Rohith
- Mayank
- Gayathri
- Sooraj
- Juse (aka Anil)

# Concept of the Project

We know that Scheduling is a NP-hard problem. Our aim is to convert the scheduling problem into a SAT problem to use the Z3 SMT solver. We have to find out a way to set up a query language which a client can use to define their problem which should be converted to a SAT problem.

# Installing dependencies

```bash
pip install -r requirements.txt
```

# INSTALLING Z3

Create an issue and assign **immkg** if any problem occurs during installation.

- step 01: `mkdir -p ~/capp; cd ~/capp`
- step 02: `git clone https://github.com/Z3Prover/z3.git`
- step 03: `cd z3`
- step 04: `python scripts/mk_make.py`
- step 05: `cd build`
- step 06: `make`
- step 07: `sudo make install`
- step 08: `cd ~`
- step 09: `cp .bashrc .bashrc_bkp`
- step 10: `echo "export LD_LIBRARY_PATH=~/capp/z3/build" >> .bashrc`
- step 11: `echo "export PYTHONPATH=~/capp/z3/build/python" >> .bashrc`
- step 12: `source .bashrc`
