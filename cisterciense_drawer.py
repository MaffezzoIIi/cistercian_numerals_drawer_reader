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
def unidade_1(img, cor=(0, 0, 0)):
    cv2.line(img, START_POSITION, (143, 25), cor, THICKNESS)

# Q1
def unidade_10(img, cor=(0, 0, 0)):
    cv2.line(img, START_POSITION, (57, 25), cor, THICKNESS)

# Q3
def unidade_100(img, cor=(0, 0, 0)):
    cv2.line(img, END_POSITION, (143, 170), cor, THICKNESS)

# Q4
def unidade_1000(img, cor=(0, 0, 0)):
    cv2.line(img, END_POSITION, (57, 170), cor, THICKNESS)

# Q2
def unidade_2(img, cor=(0, 0, 0)):
    cv2.line(img, (100, 65), (143, 65), cor, THICKNESS)

# Q1
def unidade_20(img, cor=(0, 0, 0)):
    cv2.line(img, (100, 65), (57, 65), cor, THICKNESS)

# Q3
def unidade_200(img, cor=(0, 0, 0)):
    cv2.line(img, (100, 130), (143, 130), cor, THICKNESS)

# Q4
def unidade_2000(img, cor=(0, 0, 0)):
    cv2.line(img, (100, 130), (57, 130), cor, THICKNESS)


def unidade_3(img, cor=(0, 0, 0)):
    cv2.line(img, (101, 25), (135, 63), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_30(img, cor=(0, 0, 0)):
    cv2.line(img, (99, 25), (65, 63), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_300(img, cor=(0, 0, 0)):
    cv2.line(img, (101, 170), (135, 135), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_3000(img, cor=(0, 0, 0)):
    cv2.line(img, (99, 170), (65, 135), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_4(img, cor=(0, 0, 0)):
    cv2.line(img, (101, 63), (135, 25), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_40(img, cor=(0, 0, 0)):
    cv2.line(img, (99, 63), (65, 25), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_400(img, cor=(0, 0, 0)):
    cv2.line(img, (101, 130), (135, 170), cor, THICKNESS, lineType=cv2.LINE_AA)

def unidade_4000(img, cor=(0, 0, 0)):
    cv2.line(img, (99, 130), (65, 170), cor, THICKNESS, lineType=cv2.LINE_AA)
  
def unidade_5(img, cor=(0, 0, 0)):
    unidade_4(img, cor)
    cv2.line(img, START_POSITION, (135, 25), cor, THICKNESS)

def unidade_50(img, cor=(0, 0, 0)):
    unidade_40(img, cor)
    cv2.line(img, START_POSITION, (65, 25), cor, THICKNESS)

def unidade_500(img, cor=(0, 0, 0)):
    unidade_400(img, cor)
    cv2.line(img, END_POSITION, (135, 170), cor, THICKNESS)

def unidade_5000(img, cor=(0, 0, 0)):
    unidade_4000(img, cor)
    cv2.line(img, END_POSITION, (65, 170), cor, THICKNESS)

def unidade_6(img, cor=(0, 0, 0)):
    cv2.line(img, (143, 25), (143, 65), cor, THICKNESS)

def unidade_60(img, cor=(0, 0, 0)):
    cv2.line(img, (57, 25), (57, 65), cor, THICKNESS)

def unidade_600(img, cor=(0, 0, 0)):
    cv2.line(img, (143, 170), (143, 130), cor, THICKNESS)

def unidade_6000(img, cor=(0, 0, 0)):
    cv2.line(img, (57, 170), (57, 130), cor, THICKNESS)

def unidade_7(img, cor=(0, 0, 0)):
    unidade_1(img, cor)
    unidade_6(img, cor)

def unidade_70(img, cor=(0, 0, 0)):
    unidade_10(img, cor)
    unidade_60(img, cor)

def unidade_700(img, cor=(0, 0, 0)):
    unidade_100(img, cor)
    unidade_600(img, cor)

def unidade_7000(img, cor=(0, 0, 0)):
    unidade_1000(img, cor)
    unidade_6000(img, cor)

def unidade_8(img, cor=(0, 0, 0)):
    unidade_2(img, cor)
    unidade_6(img, cor)

def unidade_80(img, cor=(0, 0, 0)):
    unidade_20(img, cor)
    unidade_60(img, cor)

def unidade_800(img, cor=(0, 0, 0)):
    unidade_200(img, cor)
    unidade_600(img, cor)

def unidade_8000(img, cor=(0, 0, 0)):
    unidade_2000(img, cor)
    unidade_6000(img, cor)

def unidade_9(img, cor=(0, 0, 0)):
    unidade_1(img, cor)
    unidade_8(img, cor)

def unidade_90(img, cor=(0, 0, 0)):
    unidade_10(img, cor)
    unidade_80(img, cor)

def unidade_900(img, cor=(0, 0, 0)):
    unidade_100(img, cor)
    unidade_800(img, cor)

def unidade_9000(img, cor=(0, 0, 0)):
    unidade_1000(img, cor)
    unidade_8000(img, cor)

def desenhar_cisterciense(numero: int, cor=(0, 0, 0)):
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
            func(img, cor)

    if dezenas > 0:
        func = globals().get(f"unidade_{dezenas * 10}")
        if func:
            func(img, cor)

    if centenas > 0:
        func = globals().get(f"unidade_{centenas * 100}")
        if func:
            func(img, cor)

    if milhares > 0:
        func = globals().get(f"unidade_{milhares * 1000}")
        if func:
            func(img, cor)

    return img

def mostrar_numero_gerado(numero):
    img = desenhar_cisterciense(numero)
    cv2.imshow(f"Cisterciense {numero}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"output/{numero}_cisterciense.png", img)