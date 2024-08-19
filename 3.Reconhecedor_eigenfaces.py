import cv2

detector_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read("classificadorEigen.yml")
largura, altura = 220, 220
fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while (True):
	conectado, imagem = camera.read()
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	faces_detectadas = detector_face.detectMultiScale(imagem_cinza, scaleFactor = 1.5, minSize=(150,150))

	for (x,y,a,l) in faces_detectadas:
		imagem_face = cv2.resize(imagem_cinza[x:x+l, y:y+a], (largura, altura))
		cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)
		id, confianca = reconhecedor.predict(imagem_face)

		if id == 1:
			nome="Andre"
		elif id == 2:
			nome="Leonardo"
		elif id == 3:
			nome="Matheus"
		else:
			nome="Desconhecido"

		confianca = confianca/10000
		if confianca < 1.2:
			cv2.putText(imagem, nome, (x, y+(a+30)), fonte, 2, (0,0,255))
		cv2.putText(imagem, str(round(confianca, 2)), (x,y + (a+50)), fonte, 1, (0,0,255))

	cv2.imshow("Detector de face", imagem)
	key=cv2.waitKey(1)
	if  key ==27:
		break

camera.release()
cv2.destroyAllWindows()
