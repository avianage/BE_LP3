import heapq

class Node:
    def __init__(self, freq, symbol, left = None,right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
        
    def __lt__(self, other):
        return self.freq < other.freq
 
def generate_huffman_codes(node, val=""):
    if not node.left and not node.right:
        return {node.symbol: val}

    huffman_codes = {}
    if node.left:
        huffman_codes.update(generate_huffman_codes(node.left, val + "0"))
    
    if node.right:
        huffman_codes.update(generate_huffman_codes(node.right, val + "1"))
    
    return huffman_codes

def encode(text, huffman_codes):
    return ''.join([huffman_codes[ch] for ch in text])

def decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
            
        if not current.left and not current.right:
            decoded_text += current.symbol
            current = root
    
    return decoded_text

def build_huffman_tree(chars, freq):
    nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]
    heapq.heapify(nodes)
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = "0"
        right.huff = "1"
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    root = nodes[0]
    huffman_codes = generate_huffman_codes(root)
    return root, huffman_codes

def huffman_coding(chars, freq, text):
    root, huffman_codes = build_huffman_tree(chars, freq)
    print("Huffman Code for Characters: ")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
        
    encoded_text = encode(text, huffman_codes)
    print("\nEncoded Text: ", encoded_text)
    
    decoded_text = decode(encoded_text, root)
    print("Decoded Text: ", decoded_text)
    
    return encoded_text, decoded_text

if __name__ == "__main__":
    chars = input("Enter characters (comma-separated): ").split(',')
    freqs = list(map(int, input("Enter frequencies (comma-separated, same order as characters): ").split(',')))
    text = input("Enter the text to encode: ")

    encoded_text, decoded_text = huffman_coding(chars, freqs, text)