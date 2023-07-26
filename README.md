# Project Description
This project allows the use of machine learning to predict the ingredients of a recipe. In particular, it has been implemented on a poke recipe in which a series of ingredients (for example 8) are passed as input and the software returns 2 missing (for example the topping and the sauce).
The model used is the Multi Target Forest and the Scikit Learn library.
The project can also be executed via flask POST api, for example from a remote frontend, or by launching the Train and Predict files in sequence locally or on a cloud server.

## Commands

To install project launch the following instructions:

```
git clone https://github.com/[username]/[project-name].git
```


To install the libraries and dependecies, first install the requirements.txt 
optional: install a virtualenv
```
(optional)python3 -m virtualenv virtualenv
(optional) source virtualenv/bin/activate
pip install -r requirements.txt
```

To execute the project, launch the training process before every other action:
```
cd [project-name]
python train.py
```
Relaunch the training process only if you change the dataset or you change other parameters in the model

After the training process, launch the prediction 
```
cd [project-name]
python predict.py
```
If you want to launch the prediction as flask services in post, do the following steps:
```
cd [project-name]
python app.py  #must be running until you need to run the flask services
```
open the index.html on server (for example in visual studio code use Live Server function)
verify the cors in the app.py code
if you need to execute the service from another front end, copy and adapt the code available in index.html

## Useful resources
Here are some links to useful resources for the project:

* [GitHub guide](https://guides.github.com/)
* [Python documentation](https://docs.python.org/3/)
* [Github link](https://github.com/ettorecar/ml_ingredient_prediction)


## Authors

Tis project has been created and coded by [ettorecar] Ettore Carpinella, [Raffaella94] Raffaella Tuozzolo, [LoritoMariaRosaria] Maria Rosaria Lorito.

