ingredient_list = ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango', 'ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'salsa di soia',\
                    'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori', 'caviale', 'cipolla', 'limone', 'lime', 'mandarino', 'arancia', 'pompelmo', 'mela', 'banana',\
                          'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']

#facciamo dei raggruppamenti per simulare un comportamento umano durante il training
ingredient_groups = [
    ['tonno', 'salmone', 'gamberi', 'polpo', 'avocado', 'mango'],
    ['ananas', 'cetriolo', 'carote', 'peperone', 'rucola', 'lattuga', 'limone', 'lime', 'mandarino'],
    ['salsa di soia', 'wasabi', 'zenzero', 'maionese', 'sesamo', 'alga nori'],
    ['mela', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline']
]
#questi ingredienti li aggiungiamo casualmente per dare più casualità
other_ingredients = ['caviale', 'cipolla', 'arancia', 'pompelmo', 'peperoncino', 'aglio', 'mirin', 'sake', 'sale', 'pepe', 'curcuma', 'coriandolo', 'prezzemolo']


poke_incomplete_alt_2 = ['tonno', 'salsa di soia', 'mirin', 'mango', 'sesamo', 'ananas', 'alga nori', 'peperone', 'rucola']
poke_incomplete = ['ananas', 'cetriolo', 'banana', 'fragola', 'mirtilli', 'kiwi', 'anacardi', 'noccioline','mela']
poke_incomplete_alt = ['salmone', 'gamberi', 'avocado', 'fragola', 'peperone', 'lattuga', 'wasabi', 'zenzero', 'maionese']


num_el_incomplete = 9 #lunghezza dell'array esclusi gli ingredienti mancanti
num_el_complete = 10 #lunghezza dell'array compresi gli ingredienti mancanti
num_el_dataset_training = 5000 #lunghezza del dataset (numero righe) utilizzato per il training