def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('LISTA DE PRODUTOS')
        mostrar(txt)
    finally:
        a.close()
def mostrar(txt):