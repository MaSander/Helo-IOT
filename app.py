import RPi.GPIO as GPIO
import time

GPIO.setmode(GIPO.BOARD) #Defini que os GIPOs serão referenciados pelo numero da placa
GPIO.setwaringws(False) #Não exibi na tela mensagens referente as portas e blablabla


GPIO.setup(7, GPIO.OUT) #Defini pino 7 como saida
#GPIO.setup(7, GPIO.IN) #Pino 7 definido como entrada

GPIO.output(7, GPIO.HIGH) #Liga a porta 7
time.sleep(5) #Timer de 5 segundos
GPIO.output(7, GPIO.LOW) #Desliga a porta 7



print("Hello, World!")