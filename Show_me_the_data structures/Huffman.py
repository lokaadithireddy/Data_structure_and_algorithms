#!/usr/bin/env python
# coding: utf-8

# In[148]:


import sys

class Node:
    def __init__(self,ch,freq):
        self.char = ch
        self.freq = freq
        self.left = None
        self.right = None
    def is_leaf(self):
        return not (self.left or self.right)
        
def freq_sort(freq_list):
    sort_nodes_by_freq = sorted(freq_list,key=lambda x:x.freq,reverse=True)
    return sort_nodes_by_freq

def update_tree(tree,huffman_code):
    huffman_dict = {}
    if not tree:
        return huffman_dict
    if tree.is_leaf():
        huffman_dict[tree.char] = huffman_code
    if tree:
        if not (tree.left or tree.right):
            if huffman_code == '': # case of only one letter
                huffman_dict[tree.char] = '0'
            else:
                huffman_dict[tree.char] = huffman_code
        huffman_dict.update(update_tree(tree.left, huffman_code + '0'))
        huffman_dict.update(update_tree(tree.right, huffman_code + '1'))
    return huffman_dict
        

def encode(data):
    freq_dict = {}
    for c in data:
        freq_dict[c] = freq_dict.get(c,0)+1
    freq_list = [Node(ch,freq) for ch,freq in freq_dict.items()]
    sort_nodes_by_freq = freq_sort(freq_list)
    while len(sort_nodes_by_freq) > 1:
        left = sort_nodes_by_freq.pop()
        right = sort_nodes_by_freq.pop()
        freq_sum = left.freq + right.freq
        parent = Node(None, freq_sum)
        parent.left = left
        parent.right = right
        sort_nodes_by_freq.append(parent)
        sort_nodes_by_freq = freq_sort(sort_nodes_by_freq)
    if(len(sort_nodes_by_freq)==0):
        return Node('',1)
    return sort_nodes_by_freq[0]

def huffman_encoding(data):
    
    huffman_tree = encode(data)
    huffman_dict = update_tree(huffman_tree,'')
    final_encoded_data = ''
    for t in huffman_dict:
        final_encoded_data+=huffman_dict[t]
    return final_encoded_data, huffman_tree

def decode(tree , code = ""):
    encode_dict = {}
    if tree:
        if not (tree.left or tree.right):
            if code == "": 
                encode_dict.update({"0": tree.char})
            else:
                encode_dict.update({code: tree.char})
        encode_dict.update(decode(tree.left, code + "0"))
        encode_dict.update(decode(tree.right, code + "1"))
    return encode_dict


def huffman_decoding(encoded_data,huffman_tree):
    encoding = decode(huffman_tree)
    decoded_message = " "
    code = " "
    for c in encoded_data:
        code += c
        if code in encoding:
            decoded_message += encoding[code]
            code = " "
    return str(decoded_message)
    


# In[151]:


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print('------------------------------------------------------------------------')
    
    # Custom Test cases
    
    a_great_sentence = "ABBBBABBABABBBAABABABAABABA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print('------------------------------------------------------------------------')
    
    a_great_sentence = "This is from note: Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print('------------------------------------------------------------------------')
    
    a_great_sentence = '                 /'
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print('------------------------------------------------------------------------')
    

    a_great_sentence = 'aaaa'
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
# In[ ]:
    print('------------------------------------------------------------------------')
    
    a_great_sentence = ''
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))





# In[ ]:




