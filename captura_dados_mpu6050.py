import serial
import csv
import time
from datetime import datetime

# Configuração da porta serial
porta_serial = "COM3"  # Altere para a porta correta do seu Arduino
baud_rate = 115200

# Gera um nome de arquivo com data e hora
nome_arquivo = f"mpu6050_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

# Conectar à porta serial
ser = serial.Serial(porta_serial, baud_rate)
time.sleep(2)  # Aguarda a conexão com a Serial

# Criar e escrever o cabeçalho do CSV
with open(nome_arquivo, mode="w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Tempo(ms)", "Acel_X", "Acel_Y", "Acel_Z", "Giro_X", "Giro_Y", "Giro_Z"])

    print(f"Capturando dados... Salvando em {nome_arquivo}")
    
    try:
        while True:
            linha = ser.readline().decode().strip()
            if linha:
                print(linha)  # Exibe os dados no terminal
                escritor.writerow(linha.split(","))  # Salva no CSV
    except KeyboardInterrupt:
        print("\nCaptura encerrada.")
        ser.close()
