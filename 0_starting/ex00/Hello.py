ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

ft_tuple_as_list = list(ft_tuple)
ft_tuple_as_list[1] = "France!"
ft_tuple = tuple(ft_tuple_as_list)

ft_set.remove("tutu!")
ft_set.update({"Paris!"})

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)