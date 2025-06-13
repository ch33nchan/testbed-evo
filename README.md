

# Evolving a Project Manager AI

This project is a simulation testbed designed to explore a hierarchical AI control system. The core idea is to evolve a high-level "Project Manager" AI that learns how to effectively manage a team of specialized "worker" agents to complete a complex task in a risky environment.

This testbed serves as a proof of concept for a larger project intended for the Minecraft environment, demonstrating that this hierarchical approach—separating high-level strategy from low-level skills—is a viable and powerful method for creating intelligent, autonomous agents.

## The Task

The goal within the simulation is to **"build a Gadget."** This requires collecting a specific set of resources:
* **3 Wood** (from a safe "Forest" zone)
* **2 Stone** (from a medium-risk "Quarry" zone)
* **1 Crystal** (from a high-risk "Cave" zone)

The challenge is not just to collect the items, but to do so with the highest possible "fitness score." The score is based on the rewards for collecting items minus penalties for the time taken (steps) and any catastrophic failures by the agents. The `ProjectManager` must evolve a policy that intelligently balances the speed of its specialist worker against the reliability of its generalist worker to maximize this score.

## File Structure

The project is organized into several Python modules:

* `main.py`: The main entry point to start the simulation.
* `settings.py`: Contains all global constants and simulation parameters, such as risk probabilities, agent speeds, and colors.
* `environment.py`: Defines the `GridWorld` class, including the layout of the different risk zones.
* `agents.py`: Defines the behavior and attributes of the two worker agents: the `GeneralistForager` and the `PunishmentTrained_Miner`.
* `project_manager.py`: Defines the `ProjectManager` class, which holds the "policy" or strategy being evolved.
* `evolution.py`: Contains the `EvolutionaryAlgorithm` class, which handles the core logic of selection, crossover, and mutation to create new generations of managers.

## How to Run

1.  Ensure you have Python 3 and Pygame installed (`pip install pygame`).
2.  Place all `.py` files in the same directory.
3.  Open a terminal or command prompt, navigate to that directory, and run the command:
    ```bash
    python main.py
    ```

## Understanding the Output

After each generation, the program will print a summary line to the console. Here is a breakdown of a sample line from your `output.txt` file:

**Sample Output:** `Best Policy of Gen 1: [W: G | S: P | C: G] | Fitness: 185`

* **`Best Policy of Gen 1`**: This indicates that this is the summary for the single most successful `ProjectManager` found in **Generation 1**.
* **`[W: G | S: P | C: G]`**: This is the "policy" or strategy that the best manager used. It's a set of rules for assigning tasks:
    * **`W: G`**: For the **W**ood task, it assigns the **G**eneralist agent.
    * **`S: P`**: For the **S**tone task, it assigns the **P**unishment-Trained specialist agent.
    * **`C: G`**: For the **C**rystal task, it assigns the **G**eneralist agent.
* **`Fitness: 185`**: This is the final score this winning policy achieved. A higher fitness score means the manager was more efficient at completing the task, balancing speed against safety to minimize penalties.
