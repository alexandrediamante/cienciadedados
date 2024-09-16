import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display_nodes(self):
        """Retorna uma string com todos os nós da lista."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

# Função para adicionar um nó
def adicionar_no(event=None):
    try:
        valor = int(entry.get())  # Obtém o valor do campo de entrada
        ll.append(valor)  # Adiciona o nó à lista
        memo_text.insert(tk.END, f"Nó com valor {valor} adicionado.\n")  # Adiciona no memo
        entry.delete(0, tk.END)  # Limpa o campo de entrada
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Função para contar os nós
def contar_nos():
    count = ll.count_nodes()
    nodes_str = ll.display_nodes()  # Obtém os nós como string
    memo_text.insert(tk.END, f"Nós na lista: {nodes_str}\n")  # Mostra os nós
    memo_text.insert(tk.END, f"Total de nós: {count}\n")  # Mostra o número de nós

# Criando a interface gráfica
root = tk.Tk()
root.title("Lista Encadeada")

# Ajustar o tamanho da janela para 400x250 pixels
root.geometry("400x250")

# Criar a lista encadeada
ll = LinkedList()

# Label e campo de entrada (ajustado para o tamanho solicitado)
label = tk.Label(root, text="Insira um valor:")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack()

# Vinculando a tecla 'Enter' à função de adicionar nó
entry.bind('<Return>', adicionar_no)

# Botões ajustados
add_button = tk.Button(root, text="Adicionar Nó", command=adicionar_no)
add_button.pack(pady=2)

count_button = tk.Button(root, text="Contar Nós", command=contar_nos)
count_button.pack(pady=2)

# Frame para incluir o Text e o Scrollbar juntos
frame = tk.Frame(root)
frame.pack()

# Adicionando o campo de texto estilo memo para exibir os resultados, com scroll
memo_text = tk.Text(frame, height=8, width=44)
memo_text.pack(side=tk.LEFT)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Associando a scrollbar ao widget Text
memo_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=memo_text.yview)

# Rodando o formulário
root.mainloop()


#pyinstaller --onefile --noconsole linked_list_form.py