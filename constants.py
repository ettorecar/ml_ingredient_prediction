
num_inc = 8 #lunghezza dell'array esclusi gli ingredienti mancanti
num_com = 10 #lunghezza dell'array compresi gli ingredienti mancanti
num_row = 5000 #lunghezza del dataset (numero righe) utilizzato per il training


ing_basi = ['riso bianco', 'riso rosso', 'insalata']
ing_princ = ['salmone crudo', 'tonno crudo','gamberi', 'pollo arrostito', 'tofu' ]
ing_altri = ['avocado', 'cetriolo','funghi al vapore', 'uovo marinato', 'cipollotto','pomodorini', 'daikon', 'cipolla rossa caramellata', 'cavolo viola', 'zenzero marinato', 'zenzero marinato rosa', 'edamame', 'gomawakame','ananas','carote','zucchine','tobiko', 'mela verde', 'ravanello', 'spinacino', 'mango']
ing_semi = ['misto di semi', 'sesamo bianco', 'sesamo nero', 'semi di chia', 'semi di lino', 'semi di girasole', 'semi di zucca', 'erba cipollina']
ing_salsa = ['soia classica', 'teriyaki','salsa ponzu', 'salsa agrodolce','salsa rosa Worcestershire', 'maionese', 'wasabi mayo', 'spicy mayo']
ing_topping = ['furikake', 'wasabipeas', 'mais tostato', 'cipolla crispy', 'alghe nori', 'cocco chips', 'melograno', 'bacche di goji', 'mandorle']

#composizione. 1 base, 2 principali, 4 altri, 1 semi, 1 salsa, 1 topping. Label: salsa e topping.


ingredient_list = ing_basi + ing_princ + ing_altri + ing_semi + ing_salsa + ing_topping

#poke_incomplete = ['insalata', 'gamberi', 'tofu', 'avocado', 'cetriolo', 'cipollotto', 'pomodorini', 'sesamo bianco']
poke_incomplete = ['riso bianco', 'salmone crudo', 'tonno crudo', 'daikon', 'zenzero marinato', 'uovo marinato', 'edamame', 'semi di lino']
