import pickle


temp_dict = dict(name="John", age=25)
print(temp_dict)

# pickle

dumps = pickle.dumps(temp_dict)
print(dumps)

with open("test_pickle.txt", 'wb') as f:
    pickle.dump(temp_dict, f)

with open('test_pickle.txt', 'rb') as f:
    content = pickle.load(f)
    print(content)



