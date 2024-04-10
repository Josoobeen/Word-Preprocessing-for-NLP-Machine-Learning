from tqdm import tqdm

max_vocab = []

def 띄어쓰기문제제거(types):
    if types[0] == ' ':
        types = types[1:]
    return types
    
def 단어사전처리(all_type):
    new_type = []
    for data in all_type:
        if data != '':
            new_type.append(data)
    all_type = new_type
    all_type = [띄어쓰기문제제거(data) for data in tqdm(all_type)]
    all_type = ['_' + data for data in tqdm(all_type)]
    return all_type

def no_tqdm_단어사전처리(all_type):
    new_type = []
    for data in all_type:
        if data != '':
            new_type.append(data)
    all_type = new_type
    all_type = [띄어쓰기문제제거(data) for data in all_type]
    all_type = [data for data in all_type]
    return all_type

def count_vocab(all_type):
    count_vocab = {}
    new_type = []
    for data in tqdm(all_type):
        if len(data) != 1:
            count_vocab[data] = count_vocab.get(data, 0) + 1
    for data in tqdm(count_vocab):
        new_type.append(list(data))
    return count_vocab, new_type


def new_byte_pair(all_2, token_vocab, max_length):
    token_vocab2 = {}
    for i in range(len(all_2)):
        for j in range(len(all_2[i]) - 1):
            pair = ''.join(all_2[i][j:j+2])
            if len(pair) <= max_length:
                token_vocab2[pair] = token_vocab2.get(pair, 0) + token_vocab[''.join(all_2[i])]
    return token_vocab2



def change_all_type(all_2, i, data): # 전체 데이터에 넣고 다시 돌릴 준비
    for j in range(1,len(all_2[i])):
        if ''.join(all_2[i][j-1:j+1]) == data:
            all_2[i][j-1:j+1] = [data]
        
    return all_2[i]

def max_finder(vocab):
    max_ = sorted(vocab.values(), reverse=True)
    newvocab = {vocab[a] : a for a in vocab}
    
    new = []
    block = set()
    maxi = 0
    stop= False
    for i in max_:
        j = newvocab[i]
        if any(a in block for a in j):
            break
        new.append(j)
        for a in j:
            if a != ' ':
                 block.add(a)
    return new, max_

def word_clean(word, len_max_vocab):
    words = list(word)
    for _ in range(len_max_vocab):
        for j in range(len(words)-1):
            data = ''.join(words[j:j+2])
            if data in max_vocab:
                words[j:j+2] = [data]
    return words

def spliter(data):
    new = []
    for data1 in data:
        if len(data1) != 1:
            for data2 in data1:
                new.append(data2)
        else:
            new.append(data1[0])
    return new

def data_preprocessing(sentence, max_vocab, len_max_vocab):
    for _ in range(10):
        sentence = sentence.replace('  ', ' ')
    if sentence[0] == ' ':
        sentence = sentence[1:]
    data = sentence.split(' ')
    
    data = no_tqdm_단어사전처리(data)
    
    total_ = [word_clean(i, len_max_vocab) for i in data]
#     total_ = [data + [' '] for data in total_]

    data = spliter(total_)
    data3 = []
    for data2 in data:
        if data2 in list(char2idx):
            data3.append(char2idx[data2])
        else:
            data3.append(char2idx[new_token[3]])
    data = data3
    
    return data









# all_data is the string data you need to encode
#반복
max_length_limit = 3
stop = False
data_limit = 20000
minimum_connect_count = 200


max_length_limit = 3
all_type2 = 단어사전처리(all_type)
count_vocab2, list_vocab = count_vocab(all_type2)

#반복
stop = False
data_limit = 20000
minimum_connect_count = 200

m = 0
whole_time = time.time()
while stop == False:
    now = time.time()
    token_vocab2 = new_byte_pair(list_vocab, count_vocab2, max_length_limit)
    max_outs, sor_out = max_finder(token_vocab2)
    meat=0
    for max_out in max_outs:
        m += 1
        max_vocab.append(max_out)
        list_vocab = [change_all_type(list_vocab, i, max_out) for i in range(len(list_vocab))]
        now2 = round(time.time() - now)
        now3 = round(time.time() - whole_time)
        print('{} 번째 : {}회전 {}초 : 전체시간 {}초 ==> {} 단어 결합 ==> {} 단어 결합==> {} 개 단어가 곂침'.format(m, meat, now2, now3, max_out, len(max_vocab), sor_out[meat]))
        if len(max_vocab) >= data_limit:
            stop = True
            break
        elif minimum_connect_count >= sor_out[meat]:
            stop = True
            break
        else:
            meat+= 1
  
