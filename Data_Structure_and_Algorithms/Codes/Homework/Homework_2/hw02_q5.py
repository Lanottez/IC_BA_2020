def if_seq_match(seq,letter_set_sorted,letters_dict):
    while True:
            seq_copy = seq.copy()
            n_value = 1
            while seq_copy:
                output_letter = the_teaser(n_value,letter_set_sorted,letters_dict)
                n_value += 1
                if output_letter:
                    if output_letter != seq_copy.pop(0):
                        return False
                if seq_copy == []:
                    return True
                
                
seq_1 = ['a', 'b', 'a', 'c', 'a']
seq_2 = ['a', 'b', 'a', 'c', 'ab', 'a', 'b']
letter_set_sorted = ['a','b','c']
letters_dict = {'a':2,'b':3,'c':5}

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