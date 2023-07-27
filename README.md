# Project Description
This project allows the use of machine learning to predict the ingredients of a recipe. In particular, it has been implemented on a poke recipe in which a series of ingredients (for example 8) are passed as input and the software returns 2 missing (for example the topping and the sauce).
The model used is the Multi Target Forest and the Scikit Learn library.
The project can also be executed via flask POST api, for example from a remote frontend, or by launching the Train and Predict files in sequence locally or on a cloud server.

## Commands

To install project launch the following instructions:

```
git clone https://github.com/ettorecar/ml_ingredient_prediction.git
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
* [Github wiki](https://github.com/ettorecar/ml_ingredient_prediction/wiki)

## License
This project is licensed under the [MIT license](LICENSE.md).

## Deployment
The project is successfully deployed on Python Anywhere Platform. Contact Authors for further info.
It runs correctly on Python 3.8, 3.9, 3.10 (previous versions not verified)

## Technical Details
This project is implemented in Python, a general-purpose programming language that is popular for machine learning. The project uses a random forest classifier to predict the two missing ingredients in a recipe. The random forest classifier is a type of machine learning algorithm that is known for its accuracy and robustness. It works by creating several decision trees, and then combining the predictions of the decision trees to make a final prediction.
The project is still under development, but it has already shown to be able to predict the two missing ingredients in a recipe with high accuracy. The project has the potential to revolutionize the way people order food and could be used by restaurants, online stores, and others.
The project code is hosted on GitHub and is available for anyone to use or modify under MIT License. The code is well-documented and easy to understand and use.
See project WIKI  section for additional information.
## Mission
This project is a proof-of-concept that shows how machine learning can be used to predict missing ingredients in recipes. The project has the potential to revolutionize the way that people order food. The project is open source, and it is available for anyone to use or modify.

## Authors

Tis project has been created and coded by [ettorecar] Ettore Carpinella, [Raffaella94] Raffaella Tuozzolo, [LoritoMariaRosaria] Maria Rosaria Lorito.

