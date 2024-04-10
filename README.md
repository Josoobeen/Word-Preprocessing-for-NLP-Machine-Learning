# Word_Preprocessing
The way to process for train NLP AI Machine

## Byte Pair Encoding(Most best)
This code is made for BPE. BPE is grouping character that has most repeated group.
This code separate all Character as list container. And Grouping every 2 container.
After Grouping, compare and choose most repeated group, and change all sentence.

if in container has over "max_length_limit = 3", cancel to group and try other group.

repeat until "minimum_connect_count = 200" is repeated only, or "data_limit = 20000" is repeated.

"I am hungry" -> ["I"," ","am"," ","hun","gry"]


## Character Encoding(Most various data)
This code is Character Encoding, One of the most easy code for preprocessing data.
This code is Good for new words. But it is hard to train for model about recognize what is the meaning of every index.
Also Maximum word is increasing, it makes training time increase.

Character Encoding is Very OLD Technique.
"I am hungry" -> ["I"," ","a","m"," ","h","u","n","g","r","y"]
