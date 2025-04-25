import cv2
import numpy as np

X_INICIAL = 100
Y_INICIAL = 25

START_POSITION = (100, 25)
END_POSITION = (100, 170)

THICKNESS = 2

def criar_canvas():
    # Cria uma imagem branca
    img = np.ones((200, 200, 3), dtype=np.uint8) * 255

    cv2.line(img, START_POSITION, END_POSITION, (0, 0, 0), THICKNESS)

    return img

# Q2
def unidade_1(img):
    cv2.line(img, START_POSITION, (143, 25), (0, 0, 0), THICKNESS)

# Q1
def unidade_10(img):
    cv2.line(img, START_POSITION, (57, 25), (0, 0, 0), THICKNESS)

# Q3
def unidade_100(img):
    cv2.line(img, END_POSITION, (143, 170), (0, 0, 0), THICKNESS)

# Q4
def unidade_1000(img):
    cv2.line(img, END_POSITION, (57, 170), (0, 0, 0), THICKNESS)

# Q2
def unidade_2(img):
    cv2.line(img, (100, 65), (143, 65), (0, 0, 0), THICKNESS)

# Q1
def unidade_20(img):
    cv2.line(img, (100, 65), (57, 65), (0, 0, 0), THICKNESS)

# Q3
def unidade_200(img):
    cv2.line(img, (100, 130), (143, 130), (0, 0, 0), THICKNESS)

# Q4
def unidade_2000(img):
    cv2.line(img, (100, 130), (57, 130), (0, 0, 0), THICKNESS)


def unidade_3(img):
    cv2.line(img, (101, 25), (135, 63), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_30(img):
    cv2.line(img, (99, 25), (65, 63), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_300(img):
    cv2.line(img, (101, 170), (135, 135), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_3000(img):
    cv2.line(img, (99, 170), (65, 135), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_4(img):
    cv2.line(img, (101, 63), (135, 25), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_40(img):
    cv2.line(img, (99, 63), (65, 25), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_400(img):
    cv2.line(img, (101, 130), (135, 170), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)

def unidade_4000(img):
    cv2.line(img, (99, 130), (65, 170), (0, 0, 0), THICKNESS, lineType=cv2.LINE_AA)
  
def unidade_5(img):
    unidade_4(img)
    cv2.line(img, START_POSITION, (135, 25), (0, 0, 0), THICKNESS)

def unidade_50(img):
    unidade_40(img)
    cv2.line(img, START_POSITION, (65, 25), (0, 0, 0), THICKNESS)

def unidade_500(img):
    unidade_400(img)
    cv2.line(img, END_POSITION, (135, 170), (0, 0, 0), THICKNESS)

def unidade_5000(img):
    unidade_4000(img)
    cv2.line(img, END_POSITION, (65, 170), (0, 0, 0), THICKNESS)

def unidade_6(img):
    cv2.line(img, (143, 25), (143, 65), (0, 0, 0), THICKNESS)

def unidade_60(img):
    cv2.line(img, (57, 25), (57, 65), (0, 0, 0), THICKNESS)

def unidade_600(img):
    cv2.line(img, (143, 170), (143, 130), (0, 0, 0), THICKNESS)

def unidade_6000(img):
    cv2.line(img, (57, 170), (57, 130), (0, 0, 0), THICKNESS)

def unidade_7(img):
    unidade_1(img)
    unidade_6(img)

def unidade_70(img):
    unidade_10(img)
    unidade_60(img)

def unidade_700(img):
    unidade_100(img)
    unidade_600(img)

def unidade_7000(img):
    unidade_1000(img)
    unidade_6000(img)

def unidade_8(img):
    unidade_2(img)
    unidade_6(img)

def unidade_80(img):
    unidade_20(img)
    unidade_60(img)

def unidade_800(img):
    unidade_200(img)
    unidade_600(img)

def unidade_8000(img):
    unidade_2000(img)
    unidade_6000(img)

def unidade_9(img):
    unidade_1(img)
    unidade_8(img)

def unidade_90(img):
    unidade_10(img)
    unidade_80(img)

def unidade_900(img):
    unidade_100(img)
    unidade_800(img)

def unidade_9000(img):
    unidade_1000(img)
    unidade_8000(img)

def desenhar_cisterciense(numero: int):
    if not (1 <= numero <= 9999):
        raise ValueError("Número deve estar entre 1 e 9999")

    img = criar_canvas()

    unidades = numero % 10
    dezenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    milhares = numero // 1000

    if unidades > 0:
        func = globals().get(f"unidade_{unidades}")
        if func:
            func(img)

    if dezenas > 0:
        func = globals().get(f"unidade_{dezenas * 10}")
        if func:
            func(img)

    if centenas > 0:
        func = globals().get(f"unidade_{centenas * 100}")
        if func:
            func(img)

    if milhares > 0:
        func = globals().get(f"unidade_{milhares * 1000}")
        if func:
            func(img)

    return img

def mostrar_numero_gerado(numero):
    img = desenhar_cisterciense(numero)
    cv2.imshow(f"Cisterciense {numero}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"output/imagens_geradas/{numero}_cisterciense.png", img)