# settings.py
# --- Screen and Grid Dimensions ---
GRID_WIDTH = 40
GRID_HEIGHT = 30
CELL_SIZE = 25
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 20

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOREST_BG = (20, 50, 20)
QUARRY_BG = (50, 50, 50)
CAVE_BG = (25, 0, 50)
WOOD_COLOR = (139, 69, 19)
STONE_COLOR = (128, 128, 128)
CRYSTAL_COLOR = (180, 180, 255)
GENERALIST_COLOR = (255, 165, 0) # Orange
SPECIALIST_COLOR = (0, 191, 255)   # Deep Sky Blue
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --- Experiment Parameters ---
GADGET_REQUIREMENTS = {'Wood': 3, 'Stone': 2, 'Crystal': 1}
AGENT_TYPES = ['GeneralistForager', 'PunishmentTrained_Miner']
GENERALIST_GATHER_TIME = 10
SPECIALIST_GATHER_TIME = 2
QUARRY_FAILURE_PROB = 0.20
CAVE_FAILURE_PROB = 0.50
REWARD_PER_RESOURCE = 50
PENALTY_PER_STEP = -1

# --- Simulation & Evolution Parameters ---
SIMULATION_TIMEOUT_STEPS = 1000
POPULATION_SIZE = 20
MUTATION_RATE = 0.1
ELITISM_COUNT = 2
MAX_GENERATIONS = 50