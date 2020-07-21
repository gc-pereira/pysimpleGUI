"""Crie um algoritmo em Python que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.<br>"""

import PySimpleGUI as sg

sg.theme('BluePurple')   # Tema da tela
# Layout da tela, os botoes e os campos para digitação
layout = [  [sg.Text('Usuário'), sg.Input()],
            [sg.Text('Senha'), sg.Input()],
            [sg.Button('Entrar'), sg.Button('Cancel')] ]

layout_2 = [    [sg.Text("Você inseriu usuário e senha iguais, tente novamente")],
                [sg.Button("OK")] ]

# Criando janela
window = sg.Window('Validação de usuário', layout)
window_2 = sg.Window("Erro", layout_2)
# Como foi inserido dois inputs, será criada um dicionário nomeado como values e a variável event receberá o nome dos campos.
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # Para fechar a janela clicar em cancel.
        break
    if values[1] == values[0]:
        event2, values2 = window_2.read() # Abrindo janela 2 se as senhas e usuário forem iguais
    window_2.close() #Clicando em ok a janela é fechada
window.close()

"""Crie um algoritmo em Python que leia e valide as seguintes informações:
* Nome: maior que 3 caracteres;
* Idade: entre 0 e 150;
* Salário: maior que zero;
* Sexo: 'f' ou 'm';
* Estado Civil: 's', 'c', 'v', 'd';
"""
import PySimpleGUI as sg

sg.theme('BluePurple')   # Tema da tela
# Layout da tela, os botoes e os campos para digitação
layout_tela1 = [ [sg.Text("Nome"), sg.Input(key="nome")],
                 [sg.Text("Idade"), sg.Input(key= "idade")],
                 [sg.Text("Salário"), sg.Input(key = "salario")],
                 [sg.Text("Sexo")],
                 [sg.Radio("Masculino", "sexo",key = "masculino"), sg.Radio("Feminino","sexo", key = "feminino")],
                 [sg.Text("Estado Civil")],
                 [sg.Checkbox("Solteiro", key = "solteiro"),sg.Checkbox("Casado", key = "casado"),sg.Checkbox("Viuvo(a)",key = "v"),sg.Checkbox("Divorciado", key = "divorcio")],
                 [sg.Button("Submeter"),sg.Button("Cancel")]
                 ]

layout_tela2 = [[sg.Text("Houve um erro, coloque as informações certas.")],
               [sg.Button("Ok")],
               ]

layout_tela3 = [[sg.Text("Informações Salvas com sucesso!")]]

janela1 = sg.Window("Validação").layout(layout_tela1)
janela2 = sg.Window("Erro", layout=layout_tela2)
janela3 = sg.Window("Fim do programa").layout(layout_tela3)

while True:
    try:
        texto, entradas = janela1.read()
        print(layout_tela1)
        print(layout_tela2)
        if texto in (None,"Cancel"):
            break
        else:
            if float(entradas["idade"]) == str or float(entradas["salario"]) == str or entradas["nome"] == float:
                janela2.read()
                janela2.close()
            else:
                janela3.read()
                janela3.close()
                break
    except ValueError:
        janela2.read()
        janela2.close()

janela1.close()
