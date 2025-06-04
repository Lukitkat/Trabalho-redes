import socket
import pickle
import time

# Criação do socket, configuracao livre de ip host e definicao da porta
s = socket.socket()
host = ""
port = 9999
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

playerOne = 1
playerTwo = 2

# Lista de sockets e enderecos
playerConn = list()
playerAddr = list()       

# Funcao que recebe uma jogada dependendo do estado do currentplayer
def get_input(currentPlayer):
    if currentPlayer == playerOne:
        player = "Player One's Turn"
        conn = playerConn[0]
    else:
        player = "Player Two's Turn"
        conn = playerConn[1]
    print(player)
    send_common_msg(player)
    try:
        conn.send("Input".encode())
        data = conn.recv(2048 * 10)
        conn.settimeout(20)
        dataDecoded = data.decode().split(",")
        x = int(dataDecoded[0])
        y = int(dataDecoded[1])
        matrix[x][y] = currentPlayer
        send_common_msg("Matrix")
        send_common_msg(str(matrix))
    except:
        conn.send("Error".encode())
        print("Error occured! Try again..")

# Funcao que verifica vencedor 
def check_rows():
    result = 0
    for i in range(3):
        if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]:
            result = matrix[i][0]
            if result != 0:
                break
    return result

# Funcao que verifica vencedor
def check_columns():
    result = 0
    for i in range(3):
        if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]:
            result = matrix[0][i]
            if result != 0:
                break
    return result

# Funcao que verifica vencedor
def check_diagonals():
    result = 0
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        result = matrix[0][0]
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
        result = matrix[0][2]
    return result

# Funcao que define o vencedor
def check_winner():
    result = 0
    result = check_rows()
    if result == 0:
        result = check_columns()
    if result == 0:
        result = check_diagonals()
    return result

# Funcao que inicia o servidor e escuta conexoes
def start_server():
    try:
        s.bind((host, port))
        print("Server iniciado")
        s.listen(2) 
        accept_players()
    except socket.error as e:
        print("Erro de conexao:", e)
    
# Funcao de verificacao dos players e inicio do jogo
def accept_players():
    try:
        for i in range(2): # So aceita 2 players
            conn, addr = s.accept() # Aceita a conexao
            msg = "<<< You are player {} >>>".format(i+1)
            conn.send(msg.encode())

            playerConn.append(conn)
            playerAddr.append(addr)
            print("Player {} - [{}:{}]".format(i+1, addr[0], str(addr[1])))
    
        start_game()
        s.close()
    except socket.error as e:
        print("Player connection error", e)
    except KeyboardInterrupt:
            print("\nKeyboard Interrupt")
            exit()
    except Exception as e:
        print("Error occurred:", e)

# Funcao que contra os turnos, jogadas, tabuleiro, verifica o vencedor e encerra o jogo
def start_game():
    result = 0
    i = 0         # Turnos
    while result == 0 and i < 9 :
        if (i%2 == 0):
            get_input(playerOne)
        else:
            get_input(playerTwo)
        result = check_winner()
        i = i + 1
        
    send_common_msg("Over")

    if result == 1:
        lastmsg = "Player One is the winner!!"
    elif result == 2:
        lastmsg = "Player Two is the winner!!"
    else:
        lastmsg = "Draw game!! Try again later!"

    send_common_msg(lastmsg)
    time.sleep(10)
    for conn in playerConn:
        conn.close()
    

def send_common_msg(text):
    playerConn[0].send(text.encode())
    playerConn[1].send(text.encode())
    time.sleep(1)

start_server()
