# Kelas Node yang digunakan untuk menyimpan kata dalam BST
class Node:
    def __init__(self, word):
        self.word = word  # Kata yang disimpan dalam node
        self.left = None  # Subtree kiri
        self.right = None  # Subtree kanan

# Kelas BST (Binary Search Tree) untuk menyimpan dan mengelola kata
class BST:
    def __init__(self):
        self.root = None  # Root awalnya kosong

    # Menyisipkan kata ke dalam BST
    def insert(self, word):
        if self.root is None:
            self.root = Node(word)  # Jika root kosong, buat node baru
        else:
            self._insert_recursive(self.root, word)  # Jika sudah ada root, sisipkan dengan rekursif

    # Fungsi rekursif untuk menyisipkan kata
    def _insert_recursive(self, node, word):
        if word < node.word:  # Jika kata lebih kecil, masuk ke subtree kiri
            if node.left is None:  # Jika subtree kiri kosong
                node.left = Node(word)  # Buat node baru
            else:
                self._insert_recursive(node.left, word)  # Rekursif ke kiri
        elif word > node.word:  # Jika kata lebih besar, masuk ke subtree kanan
            if node.right is None:  # Jika subtree kanan kosong
                node.right = Node(word)  # Buat node baru
            else:
                self._insert_recursive(node.right, word)  # Rekursif ke kanan

    # Menampilkan BST dalam urutan inorder (terurut)
    def inorder_traversal(self):
        words = []  # List untuk menyimpan kata-kata
        self._inorder_recursive(self.root, words)  # Memulai traversal dari root
        return words

    # Fungsi rekursif untuk inorder traversal
    def _inorder_recursive(self, node, words):
        if node:
            self._inorder_recursive(node.left, words)  # Traversal ke subtree kiri
            words.append(node.word)  # Tambahkan kata ke list
            self._inorder_recursive(node.right, words)  # Traversal ke subtree kanan

    # Autocomplete berdasarkan prefix
    def autocomplete(self, prefix):
        all_words = self.inorder_traversal()  # Ambil semua kata dari BST
        suggestions = [word for word in all_words if word.startswith(prefix)]  # Cari kata yang diawali dengan prefix
        return suggestions  # Kembalikan daftar saran kata
