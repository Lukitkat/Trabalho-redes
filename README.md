# Trabalho-redes
Trabalho de redes sobre sockets em Python

# Requisitos:

Python3 e pygames

# Instruções de uso (Linux):

Primeiramente, é necessário criar um ambiente virtual em Python para instalar o pygames e inicializar o servidor e os 2 clientes.


```
python3 -m venv p1              # O nome p1 está relacianado ao nome do ambiente virtual, pode ser alterado.
```

```
source p1/bin/activate         # Ativa o ambiente virtual.
```

```
pip install pygame            # Instala a biblioteca responsável pelo jogo da velha
```

```
python3 player.py             # Inicializa o player (ou servidor, se for o caso)
```

Da mesma forma, é possível inicializar o servidor. Para que a conexão entre os clientes seja realizada, é possível usar o localhost ou ip da máquina servidora.

# Instruções de uso (Windows):

Os comandos a seguir são relacionados ao Windows PowerShell.

```
python -m venv p1
```

```
p1\Scripts\Activate.ps1      # Ativa o ambiente virtual.
```

```
pip install pygame
```

```
p1\Scripts\python.exe player.py   # Inicializa o player (ou servidor, se for o caso)
```

