


my_dictionary_of_famous_aqua_song = {
"title" : "Barbie Girl",
"total_sales" : 57000000,
"language" : "english"
}


def get_title(a_dictionary):
    return a_dictionary["title"]

print(get_title(my_dictionary_of_famous_aqua_song))


def get_total_sales(a_dictionary):
    return a_dictionary["total_sales"]

my_dictionary_of_famous_aqua_song["band_members"] = 4
print(my_dictionary_of_famous_aqua_song)
print(get_total_sales(my_dictionary_of_famous_aqua_song))
