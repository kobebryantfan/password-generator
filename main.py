import PySimpleGUI as sg
import random
import string

palavras = ['bosozoku', 'riders', 'vao', 'descendo', 'rua', 'tirando', 'giro', 'moto',
            'kaneda', 'maltrata', 'falante', 'novo', 'yung', 'buda', 'bota', 'pra', 'tocar',
            'se', 'sua', 'mae', 'escutar', 'ela', 'chora', 'garota', 'agora', 'cena', 'muda'
            'tentou', 'me', 'pegar', 'esfregou', 'na', 'minha', 'perna']


def sortear_letras(numeros):
    if numeros:
        return random.choice(palavras[random.randint(0, 32)] + string.ascii_letters + string.digits)
    return random.choice(palavras[random.randint(0, 32)] + string.ascii_letters)


def gerar_arquivos(destino, nome, senha):
    txt = open(destino + "/" + "Senha" + ".txt", "a")
    txt.write("\n"+"Senha " + nome + ": " + senha +"\n")
    print(f'Senha {nome} criada no destino {destino}.')
    txt.close()


def gerar_senha(usa_letras, tamanho):
    if usa_letras:
        senha = ''.join(sortear_letras(True) for i in range(tamanho))
        return senha
    senha = ''.join(sortear_letras(False) for i in range(tamanho))
    return senha


sg.theme('Reddit')
layout = [
    [sg.Text('Escolha o tamanho máximo da senha. Saiba que o limite mínimo são de 8 caracteres.', size=(68, 1))],
    [sg.Text('As opções para salvar em arquivo .txt são opcionais.', size=(38, 1))],
    [sg.Slider(
        range=(8, 16),
        default_value=16,
        size=(24, 12),
        orientation='horizontal',
        key='-TAMANHO-',
        font=('Verdana', 12)
    )],
    [sg.Text('', size=(2, 1))],
    [sg.Text('Escolha onde salvar o arquivo txt: ', size=(24, 1)),
     sg.InputText(key='-PASTA-'), sg.FolderBrowse(button_text='Procurar')],
    [sg.Text('Insira o nome da senha (opcional):', size=(24, 1)), sg.InputText(key='-NOME-')],
    [sg.Checkbox('Salvar senha em arquivo de texto', size=(30, 1), key='-TEXTO-', default=False)],
    [sg.Checkbox('Senha possui letras e números', size=(30, 1), key='-STATUS-', default=True)],
    [sg.Submit(button_text='Gerar senha.'), sg.Exit(button_text='Cancelar.')],
]

window = sg.Window('Gerador de senhas', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar.':
        print('Aplicação encerrada!')
        break

    elif values['-TEXTO-'] and not values['-PASTA-']:
        sg.Popup('Para salvar a senha em arquivo de texto é necessário\nescolher o local onde será salvo o arquivo!')

    elif values['-PASTA-'] and values['-TEXTO-']:
        if values['-NOME-']:
            gerar_arquivos(values['-PASTA-'], values['-NOME-'], gerar_senha(values['-STATUS-'], int(values['-TAMANHO-'])))
            sg.popup_ok('Arquivo criado com sucesso!\nDestino: ' + values['-PASTA-'])
        else:
            gerar_arquivos(values['-PASTA-'], 'senha_sem_nome', gerar_senha(values['-STATUS-'], int(values['-TAMANHO-'])))
            sg.popup_ok('Arquivo criado com sucesso!\nDestino: ' + values['-PASTA-'])
    else:
        sg.popup_get_text(message='Senha gerada com sucesso!\nUse CTRL + C para copiar!', size=30,
                          default_text=gerar_senha(values['-STATUS-'], int(values['-TAMANHO-'])))

window.close()
