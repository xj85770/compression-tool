Huffman Coding Compression Tool
This project implements a Huffman coding algorithm for file compression and decompression. Huffman coding is an efficient method of compressing data without losing any information. This tool reads a text file, compresses it using the Huffman coding technique, and then decompresses it back to its original form.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What you need to run this project:

Python 3.x
Installing
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/xj85770/huffman-coding.git
Navigate to the cloned directory:

bash
Copy code
cd huffman-coding
Usage
To use this tool, you need to have a text file that you want to compress and decompress. Once you have the text file, follow these steps:

Replace les_miserables.txt in the main_encode() function with the path to your text file.
Run the script:
Copy code
python huffman_encoder.py
This will generate two files:

encoded_output.txt: The compressed version of your text file.
decoded_output.txt: The decompressed version, which should be identical to the original text file.
Built With
Python 3 - The scripting language used.
