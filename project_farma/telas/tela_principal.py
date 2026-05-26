import customtkinter as ctk
from telas.tela_cadastro import abrir_tela_cadastro
from telas.tela_consulta import abrir_tela_consulta
from telas.tela_venda import abrir_tela_venda

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()

janela.title("PDV Farmácia")
janela.geometry("1200x700")


# TÍTULO

titulo = ctk.CTkLabel(
    janela,
    text="FARMACO POLO 💊",
    font=("Arial", 38, "bold")
)

titulo.pack(pady=30)

# FRAME PRINCIPAL

frame = ctk.CTkFrame(janela)
frame.pack(expand=True, fill="both", padx=40, pady=40)


# BOTÕES

btn_venda = ctk.CTkButton(
    frame,
    text="🛒 REALIZAR VENDA",
    width=350,
    height=100,
    font=("Arial", 24, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=abrir_tela_venda
)

btn_venda.pack(pady=20)


btn_cadastro = ctk.CTkButton(
    frame,
    text="💊 CADASTRAR MEDICAMENTO",
    width=350,
    height=100,
    font=("Arial", 24, "bold"),
    fg_color="green",
    hover_color="#006400",
    command=abrir_tela_cadastro
)

btn_cadastro.pack(pady=20)


btn_consulta = ctk.CTkButton(
    frame,
    text="📋 CONSULTAR PRODUTOS",
    width=350,
    height=100,
    font=("Arial", 24, "bold"),
    fg_color="#d97706",
    hover_color="#92400e",
    command=abrir_tela_consulta
)

btn_consulta.pack(pady=20)


janela.mainloop()