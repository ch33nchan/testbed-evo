# main.py
import pygame
import copy
from settings import * 
from environment import GridWorld
from agents import GeneralistForager, PunishmentTrained_Miner
from evolution import EvolutionaryAlgorithm

def run_episode(policy, environment, screen=None, clock=None, font=None):
    inventory = {resource: 0 for resource in GADGET_REQUIREMENTS}
    total_score = 0
    steps = 0
    agent_pool = {'GeneralistForager': GeneralistForager, 'PunishmentTrained_Miner': PunishmentTrained_Miner}
    
    while steps < SIMULATION_TIMEOUT_STEPS:
        next_resource = next((res for res, needed in GADGET_REQUIREMENTS.items() if inventory[res] < needed), None)
        if next_resource is None: break

        agent_type_to_use = policy[next_resource]
        agent = agent_pool[agent_type_to_use]()
        
        target_pos = environment.get_target_location(next_resource)
        agent.start_task(next_resource, target_pos)

        task_in_progress = True
        while task_in_progress:
            if screen and pygame.QUIT in [event.type for event in pygame.event.get()]: return -float('inf')
            
            steps += 1
            total_score += PENALTY_PER_STEP
            status, data = agent.update(environment)
            
            if status != 'PENDING':
                task_in_progress = False
                if status == 'SUCCESS':
                    inventory[data] += 1
                    total_score += REWARD_PER_RESOURCE
                else: total_score += data

            if screen:
                screen.fill(BLACK)
                environment.draw(screen)
                agent.draw(screen)
                
                def draw_text(text, pos, color=WHITE): screen.blit(font.render(text, True, color), pos)
                
                draw_text(f"Task: Get {next_resource}", (10, 10))
                draw_text(f"Deployed: {agent_type_to_use}", (10, 35), GENERALIST_COLOR if 'Generalist' in agent_type_to_use else SPECIALIST_COLOR)
                
                inv_y = 70
                draw_text("Gadget Inventory:", (10, inv_y))
                for resource, count in inventory.items():
                    inv_y += 25
                    needed = GADGET_REQUIREMENTS[resource]
                    draw_text(f"- {resource}: {count} / {needed}", (15, inv_y), GREEN if count >= needed else WHITE)
                
                draw_text(f"Score: {int(total_score)}", (10, SCREEN_HEIGHT - 40))
                pygame.display.flip()
                clock.tick(FPS)
    
    return total_score

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project Manager Evolution")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    ea = EvolutionaryAlgorithm()
    world = GridWorld()
    generation = 0

    running = True
    while running and generation < MAX_GENERATIONS:
        if pygame.QUIT in [event.type for event in pygame.event.get()]: running = False
        
        print(f"\n--- Generation {generation} ---")
        for i, manager in enumerate(ea.population):
            eval_env = copy.deepcopy(world)
            fitness = run_episode(manager.policy, eval_env)
            manager.fitness = fitness

        ea.population.sort(key=lambda mgr: mgr.fitness, reverse=True)
        best_manager = ea.population[0]
        
        policy_str = ' | '.join([f'{k[0]}: {v[0]}' for k, v in best_manager.policy.items()])
        print(f"  Best Policy of Gen {generation}: [{policy_str}] | Fitness: {best_manager.fitness:.0f}")

        # Visualize the champion's policy
        world.reset_visuals()
        vis_score = run_episode(best_manager.policy, world, screen, clock, font)
        if vis_score == -float('inf'): running = False

        ea.evolve_new_generation()
        generation += 1

    print("Simulation finished.")
    pygame.quit()

if __name__ == '__main__':
    main()