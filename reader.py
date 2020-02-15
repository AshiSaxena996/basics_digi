def read_file(filepath):
    f= open(filepath, errors= 'ignore')
    data= f.read()
    f.close()
    return data



def vowel_counter(file):
    data= read_file(file).lower()
    vowels= 'aeiou'
    total_vowels= 0
    for item in vowels:
        total_vowels+= data.count(item)
    return total_vowels

def count_each_vowel(file):
    results={}
    data= read_file(file).lower()
    vowels= 'aeiou'
    total_vowels= 0
    for item in vowels:
        total_vowels= 0
        total_vowels+= data.count(item)
        results[item]= total_vowels
    return results

file='data/Richardson_Clarissa.txt'
content= read_file(file)
print("total chars: ", len(content))
print('total number of vowels: ', vowel_counter(file))
print('total number of each vowel: ', count_each_vowel(file))

# content= read_file('data/Sterne_Sentimental.txt')
# print("total chars in file 2: ", len(content))