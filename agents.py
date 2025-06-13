# agents.py
import pygame
import random
from settings import *

class BaseAgent:
    def __init__(self, color):
        self.position = (GRID_WIDTH // 2, 2)
        self.color = color
        self.state = 'IDLE'
        self.target_pos = None
        self.gather_timer = 0
        self.tasked_resource = None

    def start_task(self, resource_type, target_pos):
        self.tasked_resource = resource_type
        self.target_pos = target_pos
        self.state = 'MOVING'

    def update(self, environment):
        if self.state == 'MOVING':
            self._move_towards_target()
            if self.position == self.target_pos:
                self.state = 'GATHERING'
                self.start_gathering()
        elif self.state == 'GATHERING':
            self.gather_timer -= 1
            if self.gather_timer <= 0:
                return self.finish_gathering(environment)
        return 'PENDING', None

    def _move_towards_target(self):
        if self.target_pos is None: return
        dx, dy = 0, 0
        if self.target_pos[0] > self.position[0]: dx = 1
        elif self.target_pos[0] < self.position[0]: dx = -1
        if self.target_pos[1] > self.position[1]: dy = 1
        elif self.target_pos[1] < self.position[1]: dy = -1
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def draw(self, screen):
        rect = (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, WHITE, rect, 1)

class GeneralistForager(BaseAgent):
    def __init__(self):
        super().__init__(GENERALIST_COLOR)
        self.resilient_penalty = -25

    def start_gathering(self):
        self.gather_timer = GENERALIST_GATHER_TIME

    def finish_gathering(self, environment):
        risk = environment.get_zone_risk(self.position)
        if random.random() < risk:
            self.state = 'IDLE'
            return 'FAILURE', self.resilient_penalty
        else:
            self.state = 'IDLE'
            return 'SUCCESS', self.tasked_resource

class PunishmentTrained_Miner(BaseAgent):
    def __init__(self):
        super().__init__(SPECIALIST_COLOR)
        self.catastrophic_penalty = -150

    def start_task(self, resource_type, target_pos):
        if resource_type != 'Stone':
            self.state = 'BROKEN'
        else:
            super().start_task(resource_type, target_pos)

    def start_gathering(self):
        self.gather_timer = SPECIALIST_GATHER_TIME

    def update(self, environment):
        if self.state == 'BROKEN':
            return 'FAILURE', self.catastrophic_penalty
        return super().update(environment)

    def finish_gathering(self, environment):
        risk = environment.get_zone_risk(self.position)
        if random.random() < risk:
            self.state = 'BROKEN'
            return 'FAILURE', self.catastrophic_penalty
        else:
            self.state = 'IDLE'
            return 'SUCCESS', self.tasked_resource