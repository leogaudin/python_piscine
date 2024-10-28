from ft_package import count_in_list

assert count_in_list(["toto", "tata", "toto"], "toto") == 2, 'Ay caramba'
assert count_in_list(["toto", "tata", "toto"], "tata") == 1, 'Ay caramba'
assert count_in_list(["toto", "tata", "toto"], "tutu") == 0, 'Ay caramba'
