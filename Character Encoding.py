input_data = "Hello, my name is jo"

def Character_Encoding(input_data):
  vocab = set()
  input_data = list(input_data)
  for i in range(len(input_data)):
    vocab.add(i)

  return vocab, input_data

vocab, data = Character_Encoding(input_data)

vocab = sorted(list(vocab))

char2idx = {c : i for i, c in enumerate(vocab)}
idx2char = {i : c for i, c in enumerate(vocab)}

def char_2_idx(data, char2idx):
  out = [char2idx[data[i]] for i in range(len(data))]
  return out

def idx_2_char(data, idx2char):
  out = [idx2char[data[i]] for i in range(len(data))]
  return out

print("This is Original Data : ", input_data)
print("This is Character Encoded Data : ", char_2_idx(data, char2idx))
print("This is Index to Character Encoded Data : ", idx_2_char(char_2_idx(data, char2idx), idx2char))
