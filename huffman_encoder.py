import heapq
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(filepath):
    freq = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
    return freq

def build_huffman_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def generate_code_table(node, prefix="", code_table={}):
    if node is not None:
        if node.char is not None:
            code_table[node.char] = prefix
        generate_code_table(node.left, prefix + "0", code_table)
        generate_code_table(node.right, prefix + "1", code_table)
    return code_table

def encode_text(text, code_table):
    encoded_text = ""
    for char in text:
        encoded_text += code_table[char]
    return encoded_text

def encode_huffman_tree(node):
    tree_str = ""
    if node is None:
        return "1"
    if node.char is not None:
        return "0" + node.char
    tree_str += encode_huffman_tree(node.left)
    tree_str += encode_huffman_tree(node.right)
    return tree_str

def main():
    filepath = "les_miserables.txt"
    frequencies = calculate_frequencies(filepath)
    huffman_tree = build_huffman_tree(frequencies)
    code_table = generate_code_table(huffman_tree)
    
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        encoded_text = encode_text(text, code_table)
    
    encoded_tree = encode_huffman_tree(huffman_tree)

    # Output the encoded tree and text
    with open('encoded_output.txt', 'w', encoding='utf-8') as file:
        file.write(encoded_tree + '\n')
        file.write(encoded_text)

if __name__ == "__main__":
    main()
