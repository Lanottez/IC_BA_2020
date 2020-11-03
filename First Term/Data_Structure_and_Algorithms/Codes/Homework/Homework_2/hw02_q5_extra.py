seq1 = ["a", "ab", "c", "a", "ab", "ac"]
# seq1 =     [2, 4, 5]
occurrence_list_collection1 = [{'a': 1}, {'a': 2, 'b': 1}, {'c': 1}, {'a': 3}, {'a': 4, 'b': 2}, {'a': 5, 'c': 2}]

seq2 = ["b", "bc", "ab", "bc", "b", "abc", "b"]
# seq2 =     [3, 1, 2]

seq3 = ["a", "b", "d", "c", "a", "ab"] 
# seq 3 =    [6, 9, 11, 10]

seq4 = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'a', 'c', 'ab'] 
occurrence_list_collection4 = [{'a': 1}, {'b': 1}, {'a': 2}, {'c': 1}, {'b': 2}, {'a': 3}, {'b': 3}, {'a': 4}, {'c': 2}, {'a': 5, 'b': 4}]
# seq 4=     [4,5,9]


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


n=3000
letter_set_sorted = ['a','b','c','d','e','f','g','h','i','j','k','l']
letters_dict_2 = {'a':4,'b':5,'c':9,'d':121,'e':150,'f':1502,'g':2110,'h':2129,'i':2301,'j':2549,'k':2608,'l':3000}
seq5 = teaser_looper(n,letter_set_sorted,letters_dict_2)


letters_dict_3 = {'a':4,'b':5,'c':9,'d':121,'e':150,'f':1501,'g':2110,'h':2129,'i':2301,'j':2549,'k':2608,'l':3000}
seq6 = teaser_looper(n,letter_set_sorted,letters_dict_2)

import pdb
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
        
def reverse_engineer(seq):
    def return_one_key(input_dict):
        for keys in input_dict:
            return keys,input_dict[keys]
        
    def verify_relationship_and_update(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
        def is_int(input_num):
            if max(input_num, round(input_num)) - min(input_num, round(input_num)) < 0.000001:
                return True
            return False
        
        def verify_relationship_and_update_inner(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
            for letter in letters_output:
                relationships = letters_dict_for_relationship[letter]
                letters_modified = list(relationships.keys())
                for letter_modified in letters_modified:
                    value_modified = letters_dict[letter] / relationships[letter_modified]
                    if not is_int(value_modified):
                        letters_dict[letter] += 1
                        return False
                    else:
                        letters_dict[letter_modified] = round(value_modified)
            if letters_dict['f'] == 1501:
                pdb.set_trace()
            return True
        
        while True:
            if verify_relationship_and_update_inner(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
                break
            
    occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship = return_letter_occurrence(seq)
    def verify_size_relationship(occurrence_list_collection,letters_dict):
        for index in range(1,len(occurrence_list_collection)):
            occurrence_list_n = occurrence_list_collection[index]
            occurrence_list_n_1 = occurrence_list_collection[index-1]
            letter,letter_occurrence = return_one_key(occurrence_list_n_1)
            for keys in occurrence_list_n:
                if round(occurrence_list_n[keys] * letters_dict[keys]) <= round(letters_dict[letter] * letter_occurrence):
                    letters_dict[keys] += 1  
     
                    verify_relationship_and_update(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship)
                    return False
        return True
    
    
    
    while True:
        if verify_size_relationship(occurrence_list_collection,letters_dict):
            return_list = []
            for letter in sorted(letters_output):
                return_list.append(round(letters_dict[letter]))
            return return_list

        
        

