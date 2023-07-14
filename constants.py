ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia',\
                    'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana',\
                          'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

#facciamo dei raggruppamenti per simulare un comportamento umano durante il training
ingredient_groups = [
    ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango'],
    ['ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'limone', 'lime', 'mandarino', 'caviale'],
    ['salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori'],
    ['mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline']
]
#questi ingredienti li aggiungiamo casualmente per dare più casualità
other_ingredients = [ 'cipolla', 'arancia', 'pompelmo', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

poke_incomplete = ['cipolla', 'arancia', 'pompelmo', 'peperoncino', 'aglio', 'mirin', 'sake', 'mela']
#poke_incomplete = ['carote', 'anacardi', 'rucola', 'peperone', 'cipolla', 'arancia', 'mela', 'caviale', 'mirin']
#poke_incomplete = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'cipolla', 'arancia', 'pompelmo','peperoncino']
#poke_incomplete = ['ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'limone', 'lime', 'mandarino']
#poke_incomplete = ['salmone', 'gamberi', 'avocado', 'fragola', 'peperone', 'lattuga', 'wasabi', 'zenzero', 'maionese']


num_inc = 8 #lunghezza dell'array esclusi gli ingredienti mancanti
num_com = 10 #lunghezza dell'array compresi gli ingredienti mancanti
num_row = 100 #lunghezza del dataset (numero righe) utilizzato per il training