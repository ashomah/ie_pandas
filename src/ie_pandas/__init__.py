def sum_numbers(a,b):
    return(a + b)

def tokenize(sentence, lower=False):
    if lower == True:
        return(sentence.lower().split())
    else:
        return(sentence.split())