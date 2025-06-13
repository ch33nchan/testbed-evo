# project_manager.py

class ProjectManager:

    def __init__(self, policy=None):
        self.policy = policy if policy is not None else {}
        self.fitness = 0