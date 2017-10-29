# Data sets

Most come from [kaggle](https://www.kaggle.com/) (highly recommended).

Others are from

- [UK ONS](https://www.ons.gov.uk/)
- [data.gov.uk](https://data.gov.uk/)

## The Aim

The aim here is to get some practice with tools such as
 
- [numpy](https://docs.scipy.org/doc/numpy-dev/index.html)
- [pandas](pandas.pydata.org)
- [matplotlib](https://matplotlib.org/api/pyplot_summary.html)
- [seaborn](https://seaborn.pydata.org)
- [scipy](https://scipy.org)
- [sympy](http://www.sympy.org/en/index.html)

while still having some fun, because after all, this *IS* real data. 

Each dataset is zipped in a separate directory (becasue of space limitations on GitHub) 
so to get started simply use your favourity archiving utility.<br>
eg <br>

```sh
$ cd credit_cards/ 
$ 7z x credit_cards.zip
# cvs files unpacked in this directory
$ ipython3 # import them using pandas.read_csv(FILENAME)
```

The strucure allows you to freely create [Jupyter Notebooks](http://jupyter.org/) and store generated plots in each directory.

I will be including `requirements.txt` with all the essential packages so once you clone, simply run:

```sh
# optionally configure venv
$ python -m venv .pyvenv 
$ source .pyvenv/bin/activate # if running bash
$ pip install --user requirements.txt
``` 

----------------------------------------

## Resources

* [Machine Learning Reddit](https://www.reddit.com/r/MachineLearning/)
* [Guide to machine learning](http://yerevann.com/a-guide-to-deep-learning/?utm_campaign=Revue+newsletter&utm_medium=Newsletter&utm_source=revue)
