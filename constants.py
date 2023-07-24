
num_inc = 8 #array's lenght without missing ingredients
num_com = 10 #array's lenght with missing ingredients
num_row = 5000 #dataset's lenght (num of rows) used for the training


ing_bases = ['riso bianco', 'riso rosso', 'insalata']
ing_princ = ['salmone crudo', 'tonno crudo','gamberi', 'pollo arrostito', 'tofu' ]
ing_others = ['avocado', 'cetriolo','funghi al vapore', 'uovo marinato', 'cipollotto','pomodorini', 'daikon', 'cipolla rossa caramellata', 'cavolo viola', 'zenzero marinato', 'zenzero marinato rosa', 'edamame', 'gomawakame','ananas','carote','zucchine','tobiko', 'mela verde', 'ravanello', 'spinacino', 'mango']
ing_seeds = ['misto di semi', 'sesamo bianco', 'sesamo nero', 'semi di chia', 'semi di lino', 'semi di girasole', 'semi di zucca', 'erba cipollina']
ing_sauce = ['soia classica', 'teriyaki','salsa ponzu', 'salsa agrodolce','salsa rosa Worcestershire', 'maionese', 'wasabi mayo', 'spicy mayo']
ing_topping = ['furikake', 'wasabipeas', 'mais tostato', 'cipolla crispy', 'alghe nori', 'cocco chips', 'melograno', 'bacche di goji', 'mandorle']

#composition. 1 base, 2 principals, 4 others, 1 seeds, 1 sauce, 1 topping. Label: sauce and topping.
ingredient_list = ing_bases + ing_princ + ing_others + ing_seeds + ing_sauce + ing_topping

#recipe_incomplete = ['insalata', 'gamberi', 'tofu', 'avocado', 'cetriolo', 'cipollotto', 'pomodorini', 'sesamo bianco']
recipe_incomplete = ['riso bianco', 'salmone crudo', 'tonno crudo', 'daikon', 'zenzero marinato', 'uovo marinato', 'edamame', 'semi di lino']