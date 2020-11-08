def caesar_cipher_encrypt(str_to_encrypt, n):
    """
    Encrypt string using Caesar cipher by n positions
    
    This function builds one of the most widely known encryption 
    techniques, _Caesar's cipher_. This works as follows: 
    you should be given a string str_to_encrypt and an encoding 
    integer n, which then be used to replace each initial letter 
    to the encrypted one by simply shifting the letter by n positions.
    
    Parameters:
        str_to_encrypt: string
        n: shift parameter
        
    Returns:
        n-encrypted string
    
    Examples:
    >>> caesar_cipher_encrypt('a', 1)
    'b'
    >>> caesar_cipher_encrypt('abc', 1)
    'bcd'
    >>> caesar_cipher_encrypt('abc', 4)
    'efg'
    >>> caesar_cipher_encrypt('thisistherealdeal', 6)
    'znoyoyznkxkgrjkgr'
    """
    

        
        
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    def encrypter(letter,n):
         alphabet = 'abcdefghijklmnopqrstuvwxyz'
         alphabet_list = list(alphabet)
         new_letter_pos = alphabet_list.index(letter) + n
         
         try:
             return alphabet_list[new_letter_pos]
         except IndexError:
             return alphabet_list[new_letter_pos-26]
         
    str_list = list(str_to_encrypt)
    
    output = ''
    for _str_ in str_to_encrypt:
        output += encrypter(_str_,n)
    return output
        
   
    

def caesar_cipher_decrypt(str_to_decrypt, n):
    """
    Decrypt Caesar cipher by n positions
    
        
    Parameters:
        str_to_decrypt: string
        n: shift parameter
        
    Returns:
        n-decrypted string
    
    Examples:
    >>> caesar_cipher_decrypt('b', 1)
    'a'
    >>> caesar_cipher_decrypt('bcd', 1)
    'abc'
    >>> caesar_cipher_decrypt('efg', 4)
    'abc'
    >>> caesar_cipher_decrypt('znoyoyznkxkgrjkgr', 6)
    'thisistherealdeal'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    
    def decrypter(letter,n):
         alphabet = 'abcdefghijklmnopqrstuvwxyz'
         alphabet_list = list(alphabet)
         new_letter_pos = alphabet_list.index(letter) - n
         
         try:
             return alphabet_list[new_letter_pos]
         except IndexError:
             return alphabet_list[new_letter_pos+26]
         
    str_list = list(str_to_decrypt)
    
    output = ''
    for _str_ in str_to_decrypt:
        output += decrypter(_str_,n)
    return output
    

