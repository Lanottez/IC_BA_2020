seq1 = ["a", "ab", "c", "a", "ab", "ac"]
occurrence_list_collection1 = [{'a': 1}, {'a': 2, 'b': 1}, {'c': 1}, {'a': 3}, {'a': 4, 'b': 2}, {'a': 5, 'c': 2}]
seq2 = ["b", "bc", "ab", "bc", "b", "abc", "b"]
seq3 = ["a", "b", "d", "c", "a", "ab"] 
seq4 = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'a', 'c', 'ab'] #{'a':4,'b':5,'c':9}
occurrence_list_collection4 = [{'a': 1}, {'b': 1}, {'a': 2}, {'c': 1}, {'b': 2}, {'a': 3}, {'b': 3}, {'a': 4}, {'c': 2}, {'a': 5, 'b': 4}]


import pdb
def the_teaser(n,letter_set_sorted,letters_dict):
    output_letter = ''
    for letter in letter_set_sorted:
        if n % letters_dict[letter] == 0:
            output_letter += letter
    if output_letter:
        return output_letter
def teaser_looper(n,letter_set_sorted,letters_dict):
    outbook_list = []
    for i in range(1,n):
        ou = the_teaser(i,letter_set_sorted,letters_dict)
        if ou:
             outbook_list.append(ou) 
    return outbook_list

def return_letter_occurrence(seq):
    def return_letter_set(seq):
        letters_output = []
        letters_dict = {}
        for letters in seq:
            for letter in letters:
                if letter not in letters_output:
                    letters_output.append(letter)
        for index in range(len(letters_output)):
            letters_dict[letters_output[index]] = index+1
        letters_dict_for_relationship = letters_dict.copy()
        for keys in letters_dict_for_relationship:
            letters_dict_for_relationship[keys] = {}
        return [letters_output,letters_dict,letters_dict_for_relationship]
    def find_the_index_of_smallest_element(letter_list,letters_output):
        for letter in letters_output:
            if letter in letter_list:
                return letter_list.index(letter)
    [letters_output,letters_dict,letters_dict_for_relationship] = return_letter_set(seq)
    def update_occurrence_recorder_letters_dict_for_relationship(letters_output,letters_dict,letters_dict_for_relationship):
        occurrence_recorder = {}
        for letter in letters_output:
            occurrence_recorder[letter] = 0
        occurrence_list_collection = []
        for letters_index in range(len(seq)):
            occurrence_list = {}
            letters = seq[letters_index]
            for letter in letters:
                occurrence_recorder[letter] += 1
                occurrence_list[letter] = occurrence_recorder[letter]
            if len(letters) > 1:
                letter_list = list(letters)
                smallest_element = letter_list.pop(find_the_index_of_smallest_element(letter_list,letters_output))
                relationship_dict = {}
                for relationship in letter_list:
                    letters_dict_for_relationship[smallest_element][relationship] = occurrence_recorder[relationship] / occurrence_recorder[smallest_element]
            occurrence_list_collection.append(occurrence_list.copy())
        def complete_letters_dict_for_relationship(letters_dict_for_relationship):        
            for keys in letters_dict_for_relationship:
                out_key = keys
                letter_dict_for_relationship = letters_dict_for_relationship[out_key]
                for keys in letter_dict_for_relationship:
                    in_key = keys
                    letters_dict_for_relationship[in_key][out_key] = 1/letters_dict_for_relationship[out_key][in_key] 
        complete_letters_dict_for_relationship(letters_dict_for_relationship)   
        return occurrence_list_collection,letters_dict_for_relationship
    
    occurrence_list_collection,letters_dict_for_relationship = update_occurrence_recorder_letters_dict_for_relationship(letters_output,letters_dict,letters_dict_for_relationship)
    
    return occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship

def incrementer(letters_dict,letters_output,letters_dict_for_relationship):
    def is_all_int(letters_dict):
        for keys in letters_dict:
            if int(letters_dict[keys]) != letters_dict[keys]:
                return False
        return True
    while True:
        small_letter= letters_output[0]
        letters_dict[small_letter] += 1
        for letter in letters_output:
            if letters_dict_for_relationship[letter] != {}:
                relationship_dic = letters_dict_for_relationship[letter]
                for keys in relationship_dic:
                    ratio = relationship_dic[keys]
                    letters_dict[keys] = letters_dict[letter] / ratio
        if is_all_int(letters_dict):
            break
    for index in range(1,len(letters_output)):
        while letters_dict[letters_output[index]] <= letters_dict[letters_output[index-1]]:
            letters_dict[letters_output[index]] += 1
    return letters_dict

def reverse_engineer(seq):
    def is_same_as_order(occurrence_list_collection,letters_dict):
        def return_a_key_and_its_value(input_dict):
            for keys in input_dict:
                return keys,input_dict[keys]
        for index in range(1,len(occurrence_list_collection)):
            letter,letter_occurrence = return_a_key_and_its_value(occurrence_list_collection(index))
            letter_n1,letter_occurrence_n1 = return_a_key_and_its_value(occurrence_list_collection(index-1))
            if occurrence_list_collection
        return True
        
        
        
        
        
    def return_dict(seq):
        [occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship] = return_letter_occurrence(seq)
        letter_set_sorted = sorted(letters_output)
        print(occurrence_list_collection)
        while True:
            if is_same_as_order(occurrence_list_collection,letters_dict):
                                 return [letters_dict,letter_set_sorted]
            else:
                incrementer(letters_dict,letters_output,letters_dict_for_relationship)

                
                
                
    [return_dict,letter_set_sorted] = return_dict(seq)
    return_list = []
    for letter in letter_set_sorted:
        return_list.append(int(return_dict[letter]))
    return return_list

# =============================================================================
# n=21
# letter_set_sorted = ['a','b','c']
#  #,'d','e','f']
#  #,'g','h','i','j','k','l','m','n']
# 
# letters_dict_1 = {'a':4,'b':5,'c':9}
#                ,'d':121,'e':150,'f':152}
#                ,'g':211,'h':212,'i':230,'j':254,'k':260,'l':1244,'m':1277,'n':1300}
# letters_dict_2 = {'a': 4, 'b': 5.0, 'c': 90.0, 'd': 91, 'e': 150.0, 'f': 152.0}
# seq1 = teaser_looper(n,letter_set_sorted,letters_dict_1)
# seq2 = teaser_looper(n,letter_set_sorted,letters_dict_2)
# #print(reverse_engineer(seq))
# =============================================================================