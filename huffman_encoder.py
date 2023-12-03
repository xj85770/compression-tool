import heapq
import json
import sys

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
        else:
            generate_code_table(node.left, prefix + "0", code_table)
            generate_code_table(node.right, prefix + "1", code_table)
    return code_table

def encode_text(text, code_table):
    encoded_bits = ""
    for char in text:
        encoded_bits += code_table[char]
    padding = 8 - len(encoded_bits) % 8
    encoded_bits += '0' * padding
    encoded_bytes = bytearray()
    for i in range(0, len(encoded_bits), 8):
        byte = encoded_bits[i:i+8]
        encoded_bytes.append(int(byte, 2))
    return encoded_bytes, padding

def encode_huffman_tree(node):
    if node is None:
        return "1"
    if node.char is not None:
        return '0' + node.char
    return encode_huffman_tree(node.left) + encode_huffman_tree(node.right)

def write_header(output_file, frequencies, encoded_tree, padding):
    header_content = {
        'frequencies': frequencies,
        'encoded_tree': encoded_tree,
        'padding': padding
    }
    json_header = json.dumps(header_content)
    output_file.write(json_header + "\n")

def main():
    filepath = "les_miserables.txt"
    output_filename = "encoded_output.txt"
    frequencies = calculate_frequencies(filepath)
    huffman_tree = build_huffman_tree(frequencies)
    code_table = generate_code_table(huffman_tree)
    encoded_tree = encode_huffman_tree(huffman_tree)

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        encoded_bytes, padding = encode_text(text, code_table)

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        write_header(output_file, frequencies, encoded_tree, padding)
        output_file.write(encoded_bytes.decode('latin1'))  # Write bytes as text

if __name__ == "__main__":
    main()
