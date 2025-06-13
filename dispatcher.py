# project_manager.py

class ProjectManager:
    """Represents a management strategy. Its 'gene' is a policy dictionary."""
    def __init__(self, policy=None):
        # The gene is a dictionary mapping a resource to an agent type
        # e.g., {'Wood': 'GeneralistForager', 'Stone': 'PunishmentTrained_Miner', ...}
        self.policy = policy if policy is not None else {}
        self.fitness = 0