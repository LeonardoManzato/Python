import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def get_imagem_id():
	caminhos = [os.path.join('Fotos', f) for f in os.listdir('Fotos')]
	#print(caminhos)
	faces = []
	ids = []
	for caminho_imagem in caminhos:
		imagem_face = cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2GRAY)
		id = int(os.path.split(caminho_imagem)[-1].split('.')[1])
		print(id)
		ids.append(id)
		faces.append(imagem_face)
		#cv2.imshow("Face", imagem_face)
		#cv2.waitKey(10)
	return np.array(ids), faces

ids, faces = get_imagem_id()
#print(faces)

print("Treinando...")
eigenface.train(faces, ids)
eigenface.write('classificadorEigen.yml')

# fisherface.train(faces,ids)
# fisherface.write('classificadorFisher.yml')

# lbph.train(faces, ids)
# lbph.write('classificadorLBPH.yml')

print("Treinamento finalizado")