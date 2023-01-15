N = input()
group_word_checker = 0
for _ in len(N):
    word = input()
    set_word = set(word)
    if len(word) == set(word):
        group_word_checker += 1
    else:
        for i in set_word:
            globals()[i + '_index_list'] 
            = [i for i, x in enumerate(letters) if x == 'c']
# index_list = [i for i, x in enumerate(letters) if x == 'c']