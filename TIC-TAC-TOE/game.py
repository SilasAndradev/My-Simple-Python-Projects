def jogador1(board):
    while True:
        try:
            num = int(input('''Jogador 1:\nDigite o lugar que você quer jogar: '''))
            if board[num] == 'X' or board[num] == 'O':
                print('\033[0;33mEsse lugar está ocupado\033[0m')
                
            else:
                board[num] = 'X'
                print(f"""
                {board[0].replace("'"," ")}  |   {board[1].replace("'"," ")}  |   {board[2].replace("'"," ")}
                {board[3].replace("'"," ")}  |   {board[4].replace("'"," ")}  |   {board[5].replace("'"," ")}
                {board[6].replace("'"," ")}  |   {board[7].replace("'"," ")}  |   {board[8].replace("'"," ")}
                """ )
                break
        except Exception as e:
            print(f'Ocorreu {e}')

def jogador2(board):
    while True:
        try:
            num = int(input('''Jogador 2:\nDigite o lugar que você quer jogar: '''))
            if board[num] == 'X' or board[num] == 'O':
                print('\033[0;33mEsse lugar está ocupado\033[0m')
                
            else:
                board[num] = 'O'
                print(f"""
                {board[0].replace("'"," ")}  |   {board[1].replace("'"," ")}  |   {board[2].replace("'"," ")}
                {board[3].replace("'"," ")}  |   {board[4].replace("'"," ")}  |   {board[5].replace("'"," ")}
                {board[6].replace("'"," ")}  |   {board[7].replace("'"," ")}  |   {board[8].replace("'"," ")}
                """ )
                break
        except Exception as e:
            print(f'Ocorreu {e}')
            
def game():
    jogador1(board)
    jogador2(board)
    jogador1(board)
    jogador2(board)
    jogador1(board)
    jogador2(board)
    
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print('O jogador 1 ganhou')
        return

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print('O jogador 1 ganhou')
        return
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print('O jogador 2 ganhou')
        return
    
    jogador1(board)
    jogador2(board)
    jogador1(board)

    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print('O jogador 1 ganhou')
        return

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print('O jogador 1 ganhou')
        return
    
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print('O jogador 2 ganhou')
        return
    
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print('O jogador 1 ganhou')
        return
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print('O jogador 2 ganhou')
        return
    else:
        print('HAHAHAHAHAHAHAH Deu Velha')
        return


board = [
            '0','1','2',
            '3','4','5',
            '6','7','8'
        ]


print(f"""
{board[0].replace("'"," ")}  |   {board[1].replace("'"," ")}  |   {board[2].replace("'"," ")}
{board[3].replace("'"," ")}  |   {board[4].replace("'"," ")}  |   {board[5].replace("'"," ")}
{board[6].replace("'"," ")}  |   {board[7].replace("'"," ")}  |   {board[8].replace("'"," ")}
""" )

game()