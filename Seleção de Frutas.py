import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dicionário de frutas e seus links de imagem
frutas_imagens = {
    "Uva": "https://img.freepik.com/vetores-premium/icone-de-desenho-animado-de-uva-ilustracao-de-desenho-grafico-plano_1319591-80.jpg?semt=ais_hybrid",
    "Morango": "https://i.pinimg.com/736x/2a/dc/0c/2adc0ccdcc48c2a308a71a060e486953.jpg",
    "Banana": "https://thumbs.dreamstime.com/b/bananas-dos-desenhos-animados-76537191.jpg",
    "Manga": "https://static.vecteezy.com/ti/vetor-gratis/p1/1735917-manga-fresca-madura-fruta-exotica-vetor.jpg",
    "Abacaxi": "https://thumbs.dreamstime.com/b/abacaxi-55526274.jpg",
    "Maçã": "https://i.pinimg.com/originals/e9/38/a2/e938a2a3cf6cd84e0c6b01f9689133d9.png",
    "Laranja": "https://img.freepik.com/vetores-premium/laranjas-em-um-fundo-branco-projeto-de-desenho-animado-de-frutas-maduras_530689-1117.jpg",
    "Melancia": "https://www.desenhar.org/wp-content/uploads/2023/10/Como-desenhar-melancia-Passo-8.jpg",
    "Pera": "https://img.freepik.com/vetores-gratis/desenho-de-pera-verde-isolado_1308-126377.jpg",
    "Limão": "https://i.pinimg.com/736x/5a/11/bb/5a11bb57e62d9a80198f86fe2cfc2ca3.jpg",
    "Abacate": "https://i.pinimg.com/736x/da/8a/bd/da8abdc2eccb2b9adf2ddd78cd057082.jpg",
    "Goiaba": "https://i.pinimg.com/736x/98/f8/a6/98f8a63d26ace1c95cbd0ba3247e4a1f.jpg",
    "Kiwi": "https://i.pinimg.com/736x/a1/0e/be/a10ebe094a5ddafd5abe9944aedfaf09.jpg",
    "Mamão": "https://i.pinimg.com/736x/69/86/96/69869657764d03ad16b9b4d6e63cfa04.jpg",
    "Tomate": "https://i.pinimg.com/736x/a3/11/31/a31131fc34461f5f85ab36e5861d8d33.jpg",
    "Melão": "https://img.freepik.com/vetores-premium/ilustracao-em-vetor-brilhante-de-metade-colorida-fatia-e-todo-o-melao-de-suco-vegetal-fresco-dos-desenhos-animados-isolado-no-fundo-branco_126520-732.jpg",
    "Jaca": "https://media.istockphoto.com/id/2159021731/pt/vetorial/jackfruit-flat-design-tree-fruit-illustration.jpg?s=612x612&w=0&k=20&c=_A1jGH5KEDED76z5BcW5PJxKxaedZ9KXTxWoTWSuJwo="
}

def exibir_imagem(fruta):
    """Função para buscar e exibir a imagem da fruta selecionada."""
    # Verifica se a fruta está no dicionário
    if fruta in frutas_imagens:
        url = frutas_imagens[fruta]
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica se houve erro na requisição
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = img.resize((300, 300), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            imagem_label.configure(image=img_tk)
            imagem_label.image = img_tk
        except Exception as e:
            imagem_label.configure(text="Erro ao carregar a imagem.")
    else:
        imagem_label.configure(text="Selecione uma fruta válida.")

# Configuração da janela principal
root = tk.Tk()
root.title("Seleção de Imagens de Frutas")
root.geometry("500x500")
root.configure(bg="lightblue")

# Título
titulo = tk.Label(root, text="Escolha uma fruta para ver a imagem", font=("Arial", 16), bg="lightblue")
titulo.pack(pady=10)

# Caixa de seleção de frutas
fruta_selecionada = tk.StringVar()
caixa_selecao = ttk.Combobox(root, textvariable=fruta_selecionada, state="readonly", font=("Arial", 12))
caixa_selecao['values'] = list(frutas_imagens.keys())
caixa_selecao.pack(pady=10)

# Botão para exibir a imagem
botao = tk.Button(root, text="Exibir Imagem", command=lambda: exibir_imagem(fruta_selecionada.get()), font=("Arial", 12), bg="green", fg="white")
botao.pack(pady=10)

# Label para exibir a imagem
imagem_label = tk.Label(root, text="", bg="lightblue")
imagem_label.pack(pady=20)

# Loop principal da interface
root.mainloop()
