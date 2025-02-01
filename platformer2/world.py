from utils import *

class World:
    def __init__(self):
        self.obstacle_list = []
    def process_data(self, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] >= 0:
                    img = image_list[data[i][j]]
                    img_rect = img.get_rect()
                    img_rect.x = j * TILE_SIZE
                    img_rect.y = i * TILE_SIZE
                    
        