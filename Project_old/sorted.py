
sort_dictionary = {'India': 91, 'UK' : 44 , 'USA' : 1,'Austria': 43,'Russia':7,'Spain': 34,'Germany': 49}

ordered_dictionary = {}
for key, value in sorted(sort_dictionary.items(), key=lambda x: x[1], reverse=True):
    ordered_dictionary[key] = value

print("unsorted dictionary:", sort_dictionary)
print("sorted dictionary:", ordered_dictionary)