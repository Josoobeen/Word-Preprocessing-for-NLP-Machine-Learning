# Word_Preprocessing
The way to process for train NLP AI Machine

## Byte Pair Encoding
This code is made for BPE. BPE is grouping character that has most repeated group.
This code separate all Character as list container. And Grouping every 2 container.
After Grouping, compare and choose most repeated group, and change all sentence.

if in container has over "max_length_limit = 3", cancel to group and try other group.

repeat until "minimum_connect_count = 200" is repeated only, or "data_limit = 20000" is repeated.



