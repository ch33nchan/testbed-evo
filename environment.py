# environment.py
import pygame
import random
from settings import *

class GridWorld:
    def __init__(self):
        self.forest_zone = pygame.Rect(0, 0, GRID_WIDTH, GRID_HEIGHT // 2)
        self.quarry_zone = pygame.Rect(0, GRID_HEIGHT // 2, GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.cave_zone = pygame.Rect(GRID_WIDTH // 2, GRID_HEIGHT // 2, GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.visual_markers = {}
        self.reset_visuals()

    def reset_visuals(self):
        self.visual_markers = {'Wood': set(), 'Stone': set(), 'Crystal': set()}
        for _ in range(10):
            self.visual_markers['Wood'].add(self._get_random_pos_in_zone(self.forest_zone))
        for _ in range(5):
            self.visual_markers['Stone'].add(self._get_random_pos_in_zone(self.quarry_zone))
        for _ in range(3):
            self.visual_markers['Crystal'].add(self._get_random_pos_in_zone(self.cave_zone))

    def _get_random_pos_in_zone(self, zone_rect):
        x = random.randint(zone_rect.left, zone_rect.right - 1)
        y = random.randint(zone_rect.top, zone_rect.bottom - 1)
        return x, y

    def get_target_location(self, resource_type):
        if resource_type == 'Wood': return self._get_random_pos_in_zone(self.forest_zone)
        if resource_type == 'Stone': return self._get_random_pos_in_zone(self.quarry_zone)
        if resource_type == 'Crystal': return self._get_random_pos_in_zone(self.cave_zone)

    def get_zone_risk(self, position):
        if self.quarry_zone.collidepoint(position): return QUARRY_FAILURE_PROB
        if self.cave_zone.collidepoint(position): return CAVE_FAILURE_PROB
        return 0

    def draw(self, screen):
        pygame.draw.rect(screen, FOREST_BG, (self.forest_zone.x * CELL_SIZE, self.forest_zone.y * CELL_SIZE, self.forest_zone.width * CELL_SIZE, self.forest_zone.height * CELL_SIZE))
        pygame.draw.rect(screen, QUARRY_BG, (self.quarry_zone.x * CELL_SIZE, self.quarry_zone.y * CELL_SIZE, self.quarry_zone.width * CELL_SIZE, self.quarry_zone.height * CELL_SIZE))
        pygame.draw.rect(screen, CAVE_BG, (self.cave_zone.x * CELL_SIZE, self.cave_zone.y * CELL_SIZE, self.cave_zone.width * CELL_SIZE, self.cave_zone.height * CELL_SIZE))
        for x, y in self.visual_markers['Wood']: pygame.draw.rect(screen, WOOD_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for x, y in self.visual_markers['Stone']: pygame.draw.rect(screen, STONE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for x, y in self.visual_markers['Crystal']: pygame.draw.rect(screen, CRYSTAL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))