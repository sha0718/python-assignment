from collections import defaultdict, Counter
import heapq
import re

# Define common stop words to ignore
STOP_WORDS = set([
    'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'for', 'with', 'by', 'this', 'that', 'it', 'as', 'are'
])

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()  # Set of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insert a word into the Trie, storing it in all prefixes.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.add(word)

    def search_prefix(self, prefix):
        """
        Return all words starting with a given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.words

def clean_text(text):
    """
    Cleans the input text: removes punctuation and lowercases everything.
    """
    return re.findall(r'\b[a-z]+\b', text.lower())

def analyze_text(text):
    """
    Analyzes the text to build a word frequency counter and a Trie for fast prefix queries.
    """
    words = clean_text(text)
    filtered_words = [word for word in words if word not in STOP_WORDS]

    # Count word frequencies
    freq_counter = Counter(filtered_words)

    # Insert words into Trie
    trie = Trie()
    for word in freq_counter:
        trie.insert(word)

    return freq_counter, trie

def query_top_k_with_prefix(freq_counter, trie, prefix, k):
    """
    Returns the top K most frequent words starting with the given prefix.
    """
    candidates = trie.search_prefix(prefix)
    top_k = heapq.nlargest(k, candidates, key=lambda word: freq_counter[word])
    return top_k

# Example usage
text = """
The quick brown fox jumps over the lazy dog. This is a test of the text analysis tool.
The text contains words like the, this, and that, which should be ignored.
"""

# Analyze the text
freq_counter, trie = analyze_text(text)

# Query example: top 3 words starting with "th"
result = query_top_k_with_prefix(freq_counter, trie, 'th', 3)
print("Top 3 words starting with 'th':", result)
