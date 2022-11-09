
'''
Helper Functions 
'''

def array_conversation_string(array):
    new_array = []
    for i in array.split(','):
        i = int(i)
        new_array.append(i)

    new_array.sort(reverse=True)
    string_array = ','.join([str(element) for element in new_array])
    return string_array
