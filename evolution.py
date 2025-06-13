# evolution.py
import random
from project_manager import ProjectManager
from settings import *

class EvolutionaryAlgorithm:
    def __init__(self):
        self.population = [ProjectManager(self._create_random_policy()) for _ in range(POPULATION_SIZE)]

    def _create_random_policy(self):
        policy = {}
        for resource in GADGET_REQUIREMENTS:
            policy[resource] = random.choice(AGENT_TYPES)
        return policy

    def evolve_new_generation(self):
        self.population.sort(key=lambda mgr: mgr.fitness, reverse=True)
        new_population = []
        for i in range(ELITISM_COUNT): new_population.append(self.population[i])
        while len(new_population) < POPULATION_SIZE:
            parent1 = self._tournament_selection()
            parent2 = self._tournament_selection()
            child_policy = self._crossover(parent1.policy, parent2.policy)
            self._mutate(child_policy)
            new_population.append(ProjectManager(child_policy))
        self.population = new_population

    def _tournament_selection(self):
        participants = random.sample(self.population, 5)
        participants.sort(key=lambda mgr: mgr.fitness, reverse=True)
        return participants[0]
        
    def _crossover(self, policy1, policy2):
        child_policy = {}
        for resource in GADGET_REQUIREMENTS:
            child_policy[resource] = random.choice([policy1[resource], policy2[resource]])
        return child_policy

    def _mutate(self, policy):
        if random.random() < MUTATION_RATE:
            resource_to_mutate = random.choice(list(GADGET_REQUIREMENTS.keys()))
            policy[resource_to_mutate] = random.choice(AGENT_TYPES)