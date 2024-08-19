import cv2
import numpy as np
import time

classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')

amostra = 1
numero_amostra = 250
id = 1
largura, altura = 220,220

camera = cv2.VideoCapture(0)
print("Preparando para as fotos, se posicione...")
time.sleep(3)
while (True):
	conectado, imagem= camera.read()
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	#print(np.average(imagem_cinza))
	faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor = 1.5, minSize=(150,150))

	for (x,y,l,a) in faces_detectadas:
		cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)
		regiao = imagem[y : y + a, x : x + a]
		regiao_cinza = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
		# olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza)
		# for (ox,oy,ol,oa) in olhos_detectados:
			# cv2.rectangle(regiao, (ox,oy), (ox+ol, oy+oa), (0,255,0),2)

		# if cv2.waitKey(1) & 0xFF == ord("q"):
		if np.average(imagem_cinza)>70 :
			imagem_face = cv2.resize(imagem_cinza [y:y + a, x:x + l], (largura, altura))
			cv2.imwrite("Fotos/Rosto." + str(id) + "." + str(amostra) + ".jpg", imagem_face)
			print("Foto" + str(amostra) + "capturada com sucesso")
			amostra +=1

	cv2.imshow ("Face", imagem)
	key = cv2.waitKey(1)
	if amostra>= numero_amostra + 1:
		break
		print("Faces capturadas com sucesso")
	elif key == 27:
		break

camera.release()
cv2.destroyAllWindows()