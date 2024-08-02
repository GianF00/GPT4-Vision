from math import ceil
from matplotlib import pyplot as plt
import cv2
import numpy as np
import sklearn.metrics
import time
import replicate

def calculate_image_tokens(width: int, height: int):
    if width > 2048 or height > 2048:
        aspect_ratio = width / height
        if aspect_ratio > 1:
            width, height = 2048, int(2048 / aspect_ratio)
        else:
            width, height = int(2048 * aspect_ratio), 2048
            
    if width >= height and height > 768:
        width, height = int((768 / height) * width), 768
    elif height > width and width > 768:
        width, height = 768, int((768 / width) * height)

    tiles_width = ceil(width / 512)
    tiles_height = ceil(height / 512)
    total_tokens = 85 + 170 * (tiles_width * tiles_height)
    
    return total_tokens

def calculate_cost(width, height):
    num_tokens = calculate_image_tokens(width, height)
    cost_per_token = 10.00 / 1_000_000  # 10 dollar per 1 million tokens
    cost = num_tokens * cost_per_token
    return cost

