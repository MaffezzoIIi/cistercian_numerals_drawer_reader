import cv2
import numpy as np

def dividir_em_quadrantes(imagem_path):
    img = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)  # Carregar em escala de cinza
    altura, largura = img.shape

    # Ajustando os limites dos quadrantes para evitar sobreposição
    quadrantes = {
        "unidades": img[0:altura//2, largura//2+2:largura],  # Quadrante superior direito
        "dezenas": img[0:altura//2, 0:largura//2-1],         # Quadrante superior esquerdo
        "centenas": img[altura//2:altura, largura//2+2:largura],  # Quadrante inferior direito
        "milhares": img[altura//2:altura, 0:largura//2-1]   # Quadrante inferior esquerdo
    }

    return quadrantes

def detectar_linhas_horizontais(quadrante):
    # Suavizar a imagem para reduzir ruídos
    quadrante_suavizado = cv2.GaussianBlur(quadrante, (5, 5), 0)

    # Aplicar limiarização (binarização) para destacar as linhas
    _, binarizada = cv2.threshold(quadrante_suavizado, 128, 255, cv2.THRESH_BINARY_INV)

    # Criar um kernel horizontal para destacar linhas horizontais
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))
    linhas_horizontais = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel)

    return linhas_horizontais

def detectar_linhas_verticais(quadrante):
    # Suavizar a imagem para reduzir ruídos
    quadrante_suavizado = cv2.GaussianBlur(quadrante, (5, 5), 0)

    # Aplicar limiarização (binarização) para destacar as linhas
    _, binarizada = cv2.threshold(quadrante_suavizado, 128, 255, cv2.THRESH_BINARY_INV)

    # Criar um kernel vertical para destacar linhas verticais
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
    linhas_verticais = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel)

    return linhas_verticais

def detectar_linhas_diagonais_45(quadrante, comprimento_minimo=11):
    # Suavizar a imagem para reduzir ruídos
    quadrante_suavizado = cv2.GaussianBlur(quadrante, (5, 5), 0)

    # Aplicar limiarização (binarização) para destacar as linhas
    _, binarizada = cv2.threshold(quadrante_suavizado, 128, 255, cv2.THRESH_BINARY_INV)

    # Criar um kernel maior para detectar linhas de 45 graus
    kernel_45 = np.array([[1, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 0, 1]], dtype=np.uint8)  # Kernel maior para 45 graus

    # Aplicar morfologia para destacar linhas de 45 graus
    linhas_45 = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel_45)

    # Suavizar as linhas usando dilatação e erosão
    kernel_suavizacao = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    linhas_suavizadas = cv2.dilate(linhas_45, kernel_suavizacao, iterations=1)
    linhas_suavizadas = cv2.erode(linhas_suavizadas, kernel_suavizacao, iterations=1)

    # Encontrar contornos das linhas diagonais
    contornos, _ = cv2.findContours(linhas_suavizadas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar uma máscara para armazenar apenas as linhas que atendem ao comprimento mínimo
    linhas_filtradas = np.zeros_like(linhas_suavizadas)

    for contorno in contornos:
        if cv2.arcLength(contorno, closed=False) >= comprimento_minimo:
            cv2.drawContours(linhas_filtradas, [contorno], -1, 255, thickness=cv2.FILLED)

    return linhas_filtradas

def detectar_linhas_diagonais_135(quadrante, comprimento_minimo=15):
    # Suavizar a imagem para reduzir ruídos
    quadrante_suavizado = cv2.GaussianBlur(quadrante, (5, 5), 0)

    # Aplicar limiarização (binarização) para destacar as linhas
    _, binarizada = cv2.threshold(quadrante_suavizado, 128, 255, cv2.THRESH_BINARY_INV)

    # Criar um kernel maior para detectar linhas de 135 graus
    kernel_135 = np.array([[0, 0, 0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)  # Kernel maior para 135 graus

    # Aplicar morfologia para destacar linhas de 135 graus
    linhas_135 = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel_135)

    # Suavizar as linhas usando dilatação e erosão
    kernel_suavizacao = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    linhas_suavizadas = cv2.dilate(linhas_135, kernel_suavizacao, iterations=1)
    linhas_suavizadas = cv2.erode(linhas_suavizadas, kernel_suavizacao, iterations=1)

    # Encontrar contornos das linhas diagonais
    contornos, _ = cv2.findContours(linhas_suavizadas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar uma máscara para armazenar apenas as linhas que atendem ao comprimento mínimo
    linhas_filtradas = np.zeros_like(linhas_suavizadas)

    for contorno in contornos:
        if cv2.arcLength(contorno, closed=False) >= comprimento_minimo:
            cv2.drawContours(linhas_filtradas, [contorno], -1, 255, thickness=cv2.FILLED)

    return linhas_filtradas

def classificar_linhas_horizontais(linhas_horizontais, altura_quadrante):
    # Encontrar contornos das linhas horizontais
    contornos, _ = cv2.findContours(linhas_horizontais, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    linhas_superiores = 0
    linhas_inferiores = 0

    for contorno in contornos:
        # Obter o retângulo delimitador do contorno
        _, y, _, _ = cv2.boundingRect(contorno)

        # Classificar a linha como superior ou inferior com base na posição vertical (y)
        if y < altura_quadrante // 2:
            linhas_superiores += 1
        else:
            linhas_inferiores += 1

    return linhas_superiores, linhas_inferiores

def contar_linhas(linhas_horizontais):
    # Encontrar contornos das linhas horizontais
    contornos, _ = cv2.findContours(linhas_horizontais, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contornos)

def calculate_number_value(horizontal_top, horizontal_bottom, vertical_count, diagonal_45_count, diagonal_135_count, quadrant, total_value):
    # Define the values for each combination of lines
    line_combinations = {
        (1, 0, 0, 0, 0): 1,
        (0, 1, 0, 0, 0): 2,
        (0, 0, 0, 1, 0): 3,
        (0, 0, 0, 0, 1): 4,
        (1, 0, 0, 0, 1): 5,
        (0, 0, 1, 0, 0): 6,
        (1, 0, 1, 0, 0): 7,
        (0, 1, 1, 0, 0): 8,
        (1, 1, 1, 0, 0): 9,
    }

    # Multipliers for each quadrant
    multipliers = {
        "unidades": 1,
        "dezenas": 10,
        "centenas": 100,
        "milhares": 1000,
    }

    # Adjust the order of combinations for hundreds and thousands
    if quadrant in ["centenas", "milhares"]:
        horizontal_top, horizontal_bottom = horizontal_bottom, horizontal_top

    # Get the corresponding value and apply the multiplier
    value = line_combinations.get((horizontal_top, horizontal_bottom, vertical_count, diagonal_45_count, diagonal_135_count), 0)
    return total_value + value * multipliers[quadrant]


def processar_quadrantes(imagem_path):
    quadrantes = dividir_em_quadrantes(imagem_path)
    unit_value = 0

    for nome, quadrante in quadrantes.items():
        altura_quadrante, _ = quadrante.shape

        # Detectar e classificar linhas horizontais
        linhas_horizontais = detectar_linhas_horizontais(quadrante)
        linhas_superiores, linhas_inferiores = classificar_linhas_horizontais(linhas_horizontais, altura_quadrante)

        # Detectar e contar linhas verticais
        linhas_verticais = detectar_linhas_verticais(quadrante)
        quantidade_linhas_verticais = contar_linhas(linhas_verticais)
        # cv2.imshow(f"Linhas Verticais - {nome.upper()}", linhas_verticais)

        # Detectar e contar linhas diagonais de 45 graus
        linhas_diagonais_45 = detectar_linhas_diagonais_45(quadrante)
        quantidade_linhas_diagonais = contar_linhas(linhas_diagonais_45)
        # cv2.imshow(f"Linhas Diagonais 45 - {nome.upper()}", linhas_diagonais_45)

        # Detectar e contar linhas diagonais de 135 graus
        linhas_diagonais_135 = detectar_linhas_diagonais_135(quadrante)
        quantidade_linhas_diagonais_135 = contar_linhas(linhas_diagonais_135)
        # cv2.imshow(f"Linhas Diagonais 135 - {nome.upper()}", linhas_diagonais_135)

        # Calcular o valor do número com base nas linhas detectadas
        unit_value = calculate_number_value(
            linhas_superiores, linhas_inferiores, quantidade_linhas_verticais,
            quantidade_linhas_diagonais, quantidade_linhas_diagonais_135, nome, unit_value
        )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return unit_value
