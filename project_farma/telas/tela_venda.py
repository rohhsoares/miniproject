import customtkinter as ctk
from banco import conectar
from tkinter import messagebox

carrinho = []


def buscar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicamentos")
    produtos = cursor.fetchall()

    conn.close()

    return produtos


def adicionar_carrinho(produto):
    carrinho.append(produto)
    atualizar_carrinho()


def remover_carrinho(index):
    carrinho.pop(index)
    atualizar_carrinho()


def atualizar_carrinho():
    for widget in frame_carrinho.winfo_children():
        widget.destroy()

    total = 0

    for i, produto in enumerate(carrinho):

        texto = f"""
{produto[1]}
Preço: R${produto[3]}
"""

        item = ctk.CTkFrame(frame_carrinho)
        item.pack(fill="x", pady=5, padx=5)

        label = ctk.CTkLabel(
            item,
            text=texto,
            justify="left",
            font=("Arial", 14)
        )

        label.pack(side="left", padx=10)

        btn_remover = ctk.CTkButton(
            item,
            text="X",
            width=40,
            fg_color="red",
            command=lambda i=i: remover_carrinho(i)
        )

        btn_remover.pack(side="right", padx=10)

        total += float(produto[3])

    total_label.configure(text=f"Total: R${total:.2f}")


def finalizar_venda():

    if len(carrinho) == 0:
        messagebox.showwarning(
            "Aviso",
            "Carrinho vazio!"
        )
        return

    total = 0

    for produto in carrinho:
        total += float(produto[3])

    messagebox.showinfo(
        "Venda Finalizada",
        f"Compra finalizada!\n\nTotal: R${total:.2f}"
    )

    carrinho.clear()
    atualizar_carrinho()


def abrir_tela_venda():

    global frame_carrinho
    global total_label

    tela = ctk.CTkToplevel()

    tela.title("PDV Farmácia")
    tela.geometry("1200x700")

    # TÍTULO

    titulo = ctk.CTkLabel(
        tela,
        text="💊 PDV FARMÁCIA",
        font=("Arial", 32, "bold")
    )

    titulo.pack(pady=20)

    # FRAME PRINCIPAL

    principal = ctk.CTkFrame(tela)
    principal.pack(fill="both", expand=True, padx=20, pady=20)

    # ESQUERDA PRODUTOS

    frame_produtos = ctk.CTkScrollableFrame(
        principal,
        width=700,
        height=500
    )

    frame_produtos.pack(side="left", fill="both", expand=True, padx=10)

    # DIREITA CARRINHO

    frame_direita = ctk.CTkFrame(
        principal,
        width=350
    )

    frame_direita.pack(side="right", fill="y", padx=10)

    titulo_carrinho = ctk.CTkLabel(
        frame_direita,
        text="🛒 Carrinho",
        font=("Arial", 24, "bold")
    )

    titulo_carrinho.pack(pady=20)

    frame_carrinho = ctk.CTkScrollableFrame(
        frame_direita,
        width=300,
        height=400
    )

    frame_carrinho.pack(padx=10, pady=10)

    total_label = ctk.CTkLabel(
        frame_direita,
        text="Total: R$0.00",
        font=("Arial", 24, "bold"),
        text_color="green"
    )

    total_label.pack(pady=20)

    btn_finalizar = ctk.CTkButton(
        frame_direita,
        text="Finalizar Venda",
        height=60,
        font=("Arial", 18, "bold"),
        fg_color="green",
        hover_color="#006400",
        command=finalizar_venda
    )

    btn_finalizar.pack(
        fill="x",
        padx=20,
        pady=20
    )

    # MOSTRAR PRODUTOS

    produtos = buscar_produtos()

    for produto in produtos:

        card = ctk.CTkFrame(
            frame_produtos,
            width=200,
            height=180
        )

        card.pack(padx=10, pady=10, fill="x")

        nome = ctk.CTkLabel(
            card,
            text=produto[1],
            font=("Arial", 20, "bold")
        )

        nome.pack(pady=10)

        preco = ctk.CTkLabel(
            card,
            text=f"Preço: R${produto[3]}",
            font=("Arial", 16)
        )

        preco.pack()

        estoque = ctk.CTkLabel(
            card,
            text=f"Estoque: {produto[4]}",
            font=("Arial", 16)
        )

        estoque.pack(pady=5)

        btn_add = ctk.CTkButton(
            card,
            text="Adicionar ao Carrinho",
            command=lambda p=produto: adicionar_carrinho(p)
        )

        btn_add.pack(pady=10, padx=10, fill="x")