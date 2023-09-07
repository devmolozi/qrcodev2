import qrcode
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

qrcode_gen_path = os.path.join(desktop_path, "qrcode")
if not os.path.exists(qrcode_gen_path):
    os.mkdir(qrcode_gen_path)

contador = 1
while True:
    entrada = input('Link ou Palavra (Digite "sair" para Sair): ')
    
    if entrada.lower() == "sair":
        break
    
    image = qrcode.make(entrada)
    image_path = os.path.join(qrcode_gen_path, input('escolha o nome do arquivo: ') + '.png')
    image.save(image_path)
    print(f"QR Code {contador} gerado e salvo em {image_path}")
    
    contador += 1

print("Programa encerrado.")

