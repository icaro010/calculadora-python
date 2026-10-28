import tkinter as tk

def clique_botao(valor):
    """Adiciona o número ou operador clicado ao visor."""
    texto_atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(tk.END, texto_atual + str(valor))

def limpar_visor():
    """Limpa todo o conteúdo do visor."""
    visor.delete(0, tk.END)

def calcular_resultado():
    """Avalia a expressão matemática no visor e exibe o resultado."""
    try:
        expressao = visor.get()
        # Subsitui o símbolo visual de multiplicação pelo operador real do Python
        expressao = expressao.replace('x', '*')
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro: Divisão por 0")
    except Exception:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("320x450")
janela.configure(bg="#202020")
janela.resizable(False, False)

# Configuração do Visor (Display)
visor = tk.Entry(janela, font=("Arial", 24), bg="#202020", fg="#ffffff", bd=0, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=15, pady=25, ipady=10, sticky="nsew")

# Layout e Design dos Botões
botoes = [
    ('C', 1, 0, '#d32f2f'), ('(', 1, 1, '#3b3b3b'), (')', 1, 2, '#3b3b3b'), ('/', 1, 3, '#f57c00'),
    ('7', 2, 0, '#333333'), ('8', 2, 1, '#333333'), ('9', 2, 2, '#333333'), ('x', 2, 3, '#f57c00'),
    ('4', 3, 0, '#333333'), ('5', 3, 1, '#333333'), ('6', 3, 2, '#333333'), ('-', 3, 3, '#f57c00'),
    ('1', 4, 0, '#333333'), ('2', 4, 1, '#333333'), ('3', 4, 2, '#333333'), ('+', 4, 3, '#f57c00'),
    ('0', 5, 0, '#333333'), ('.', 5, 1, '#333333'), ('=', 5, 2, '#388e3c')
]

# Configuração do peso das linhas e colunas para layout responsivo
for i in range(6):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

# Criação dinâmica dos botões na tela
for (texto, linha, coluna, cor_fundo) in botoes:
    # Caso especial para o botão de '=' que ocupa duas colunas
    if texto == '=':
        btn = tk.Button(janela, text=texto, font=("Arial", 14, "bold"), bg=cor_fundo, fg="#ffffff", bd=0,
                        command=calcular_resultado)
        btn.grid(row=linha, column=coluna, columnspan=2, padx=2, pady=2, sticky="nsew")
    # Caso especial para o botão de limpar (C)
    elif texto == 'C':
        btn = tk.Button(janela, text=texto, font=("Arial", 14, "bold"), bg=cor_fundo, fg="#ffffff", bd=0,
                        command=limpar_visor)
        btn.grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")
    # Botões numéricos e de operadores normais
    else:
        btn = tk.Button(janela, text=texto, font=("Arial", 14), bg=cor_fundo, fg="#ffffff", bd=0,
                        command=lambda v=texto: clique_botao(v))
        btn.grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")

# Inicia o loop da aplicação gráfica
janela.mainloop()

