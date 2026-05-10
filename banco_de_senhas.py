from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton
from PIL import Image
import pandas as pd
import os
import menu_cadastro_2


def banco_senhas(usuario, senha, senha_repeticao):
    #criando arquivo
    arquivo = "dados_projeto/lista_de_senhas.csv"

    #cria um dataframe com os dados do novo usuário
    df = pd.DataFrame(columns=["Usuário", "Senha"])
    novo_usuario = pd.DataFrame([[usuario.get(), senha.get()]],
                                columns=["Usuário", "Senha"]
                                )

    # adiciona ao CSV — cria o cabeçalho apenas se o arquivo ainda não existir
    novo_usuario.to_csv(arquivo,
                        mode="a",
                        header=not os.path.exists(arquivo),
                        index=False
                        )

    # limpa os campos após o cadastro
    usuario.delete(0, END)
    senha.delete(0, END)
    senha_repeticao.delete(0, END)



