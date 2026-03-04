ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World!"

# A tuple is a collection which is ordered and unchangeable.
# Since tuples are immutable, we need to convert it to a list first to make changes.
tmp_lst = list(ft_tuple)
tmp_lst[1] = "S. Korea!"
ft_tuple = tuple(tmp_lst)

ft_set.remove("tutu!")
ft_set.add("Seoul!")

ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
