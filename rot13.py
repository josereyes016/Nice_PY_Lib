def rot13( message, shift, format):
    '''
        Implements the rot13 alogrithm.
        Can be used to encrypt or decrypt.


        message : string to encrypt or decrypt
        shift : int to shift letters by
        format : int, 1 case sensitive or 0 for none

        return a string with character shifted as specified
    '''
    rot_mapper = 'abcdefghijklmnopqrstuvwxyz'
    try:
        n = int(shift)
    except:
        print "shift is not a number, encryption aborted"
        n = 0
    m = message.lower()
    e_m = []
    for c in m:
        if c.isalpha():
            temp =  (rot_mapper.index(c) + n) % 26
            e_m.append( rot_mapper[temp] )
        else:
            e_m.append(c)
    if format:
        for i in range(len(message)):
            if message[i].isalpha() and message[i].isupper():
                e_m[i] = e_m[i].upper()
    print ''.join(e_m)
