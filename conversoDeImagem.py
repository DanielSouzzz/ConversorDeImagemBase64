import base64

# Caminho para o arquivo de imagem
image_path = "teste-checkin/amor/imagemteste.jpeg"

# Nome do arquivo para salvar o código base64
output_file = "base64_encoded.txt"

with open(image_path, "rb") as image_file:
    # Codificar a imagem em base64
    encoded_string = base64.b64encode(image_file.read())

# Caminho completo para o arquivo de saída
output_path = output_file

# Escrever o código base64 no arquivo de saída
with open(output_path, "wb") as output:
    output.write(encoded_string)

print(f"Código base64 da imagem foi salvo em {output_path}")
