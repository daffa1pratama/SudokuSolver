import pytesseract as tesseract
import cv2
import os
from PIL import Image

""" CHANGE THIS FILE DIRECTORY! """
tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def readTextFile(filename) :
    """
    Read sudoku matrix from txt file
    """
    # Get filepath
    cwd = os.getcwd()
    data_path = os.path.abspath(os.path.join(cwd, os.pardir, 'test'))
    filename_path = os.path.join(data_path, filename + '.txt')
    # Init
    f = open(filename_path, 'r')
    container = []
    text = f.readlines()
    # Start read textfile
    for i in range(len(text)) :
        line = text[i].strip('\n').split(' ')
        for j in range(len(line)) :
            if (line[j] == '#') :
                line[j] = 0
            else :
                line[j] = int(line[j])
        container.append(line)
    f.close()
    return container

def writeFile(filename, text) :
    """
    Write sudoku result into result file
    """
    # Get filepath
    cwd = os.getcwd()
    data_path = os.path.abspath(os.path.join(cwd, os.pardir, 'result'))
    filename_path = os.path.join(data_path, filename + '-result.txt')
    # Init
    f = open(filename_path, 'w')
    # Write textfile
    f.write(text)
    f.close()

def readImageFile(filename) :
    """
    Read sudoku image and converting into matrix
    """
    # Get filepath
    cwd = os.getcwd()
    data_path = os.path.abspath(os.path.join(cwd, os.pardir, 'test'))
    filename_path = os.path.join(data_path, filename + '.png')
    board = [[0 for i in range(9)] for j in range(9)]
    # Load image
    image = cv2.imread(filename_path)
    # Get image size and cell size
    height = image.shape[0]
    width = image.shape[1]
    h_cell = height / 9
    w_cell = width / 9
    # Starting read cell
    for i in range(9) :
        for j in range(9) :
            # Get cell coordinate
            top = int((0.1 * h_cell) + h_cell * i)
            bottom = int((-0.02 * h_cell) + h_cell * (i+1))
            left = int((0.125 * w_cell) + w_cell * j)
            right = int((-0.1 * w_cell) + w_cell * (j+1))
            # Crop cell
            cropped = image[top:bottom, left:right]
            # Get cell value
            cell = tesseract.image_to_string(cropped, config='--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789')
            if cell == '' :
                board[i][j] = 0
            else :
                board[i][j] = int(cell)
    return board