import PySimpleGUI as sg

lista = ['administradores', 'alunos']

def get_layout():
    layout =[
        [
            sg.Text('Selecione seu código'),
            sg.In(),
            sg.FileBrowse('Selecione', file_types=(('Codigos Python', '*.py')
                ,)
            ),
        ],
        [
            sg.Text('Selecione a lista de Destinatarios'),
            sg.Combo(lista, default_value=lista[1]),
        ],
        [
            sg.Text('Insira o Título'), 
            sg.In(key='-Title'),
        ],
        [
            sg.Text('Insira o Conteúdo do E-mail:'),
            sg.MLine(key='-Content-'),
        ],
        [
            sg.Button('Enviar',key='-Send-'),
            sg.Button('Gerenciar Listas',key='-ListEditor-'),
        ],
    ]
    return layout

def get_window():
    return sg.Window('Teste de Janela',get_layout())