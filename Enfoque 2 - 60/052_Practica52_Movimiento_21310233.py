# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Movimiento
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import cv2

# Función para detectar movimiento en un video
def detect_motion(video_path):
    # Capturar el video
    cap = cv2.VideoCapture(video_path)
    
    # Leer el primer frame
    ret, frame1 = cap.read()
    if not ret:
        print("Error verifique su video")
        return
    
    # Convertir el frame a escala de grises
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    while cap.isOpened():
        # Leer el siguiente frame
        ret, frame2 = cap.read()
        if not ret:
            break
        
        # Convertir el frame a escala de grises
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        # Calcular la diferencia entre los dos frames
        diff = cv2.absdiff(gray1, gray2)
        
        # Aplicar un umbral para resaltar las áreas con movimiento
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        
        # Dilatar el umbral para eliminar pequeños ruidos
        dilated = cv2.dilate(thresh, None, iterations=2)
        
        # Encontrar contornos de las áreas con movimiento
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Dibujar rectángulos alrededor de los objetos en movimiento
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Mostrar el frame con el movimiento detectado
        cv2.imshow('Motion Detection', frame2)
        
        # Actualizar el frame anterior
        gray1 = gray2
        
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar los recursos y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Ruta del video a procesar
video_path = 'Porsche.mp4'

# Llamar a la función para detectar movimiento en el video
detect_motion(video_path)