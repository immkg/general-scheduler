# README

# Team MORAGS

* Adithya
* Rohith
* Mayank
* Gayathri
* Sooraj
* Jude

# Installing dependencies

* `sudo apt-get python-setuptools`
* `pip install tabulate`
* `pip install numpy`

# Installing Z3

`mkdir -p ~/capp; cd ~/capp`  
`git clone https://github.com/Z3Prover/z3.git`  
`cd z3`  
`python scripts/mk_make.py`  
`cd build`  
`make`  
`sudo make install`  
`cd ~`  
`cp .bashrc .bashrc_bkp`  
`echo "export LD_LIBRARY_PATH=~/capp/z3/build" >> .bashrc`  
`echo "export PYTHONPATH=~/capp/z3/build/python" >> .bashrc`  
`source .bashrc`  

# USAGE

* Make sure you have installed all the dependencies and built z3 successfully
* Change current working directory to src/
* Edit duration dict in var.py as per your requirements
* run `python ttablemaker.py` to see time-table in terminal
* run `python ttablemaker.py > table.data` to store the time-table in file

# CONTACT
* Mayank <131501018@smail.iitpkd.ac.in> 
