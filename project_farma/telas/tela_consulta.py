import customtkinter as ctk
from banco import conectar


def buscar_produtos(nome=""):

    conn = conectar()
    cursor = conn.cursor()

    if nome == "":
        cursor.execute("SELECT * FROM medicamentos")
    else:
        cursor.execute(
            "SELECT * FROM medicamentos WHERE nome LIKE ?",
            (f"%{nome}%",)
        )

    produtos = cursor.fetchall()

    conn.close()

    return produtos


def atualizar_lista(frame, pesquisa=""):

    for widget in frame.winfo_children():
        widget.destroy()

    produtos = buscar_produtos(pesquisa)

    for produto in produtos:

        card = ctk.CTkFrame(frame)
        card.pack(fill="x", padx=10, pady=10)

        texto = f"""
💊 {produto[1]}

🆔 Código: {produto[2]}
💰 Preço: R${produto[3]}
📦 Estoque: {produto[4]}
📁 Categoria: {produto[5]}
"""

        label = ctk.CTkLabel(
            card,
            text=texto,
            justify="left",
            font=("Arial", 16)
        )

        label.pack(padx=20, pady=20, anchor="w")


def abrir_tela_consulta():

    tela = ctk.CTkToplevel()

    tela.title("Consulta de Produtos")
    tela.geometry("1000x700")

    titulo = ctk.CTkLabel(
        tela,
        text="📋 Consulta de Produtos",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    pesquisa_entry = ctk.CTkEntry(
        tela,
        placeholder_text="Pesquisar medicamento...",
        width=500,
        height=45
    )

    pesquisa_entry.pack(pady=10)

    frame_lista = ctk.CTkScrollableFrame(
        tela,
        width=900,
        height=500
    )

    frame_lista.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    atualizar_lista(frame_lista)

    btn_pesquisar = ctk.CTkButton(
        tela,
        text="Pesquisar",
        height=50,
        command=lambda: atualizar_lista(
            frame_lista,
            pesquisa_entry.get()
        )
    )

    btn_pesquisar.pack(pady=10)