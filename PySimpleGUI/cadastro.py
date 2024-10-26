from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Primeiro número'),sg.Input(key='prinum')],
    [sg.Text('Segundo número'),sg.Input(key='segnum')],
    [sg.Checkbox('Lembrar a conta?')],
    [sg.Button('Limpar campos')]
    [sg.Button('Encerrar')]
]

# Janela
janela = sg.Window('Tela de Soma', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Encerrar':
        break
    elif eventos == 'Limpar campos':
        janela['prinum'].update('')
        janela['segnum'].update('')