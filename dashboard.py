# dashboard.py
import multiprocessing
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_dashboard(queue):
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('Evolutionary Progress Dashboard')
    
    x_data, y_best, y_avg = [], [], []
    line_best, = ax.plot([], [], 'o-', label='Best Fitness', color='cyan')
    line_avg, = ax.plot([], [], 'o-', label='Average Fitness', color='orange', alpha=0.7)
    
    ax.set_title("Fitness Score per Generation")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness Score")
    ax.legend()
    ax.grid(True, alpha=0.3)

    def update(frame):
        while not queue.empty():
            generation, best_fitness, avg_fitness = queue.get()
            if best_fitness > -1000:
                x_data.append(generation)
                y_best.append(best_fitness)
                y_avg.append(avg_fitness)
        if not x_data: return line_best, line_avg,
        line_best.set_data(x_data, y_best)
        line_avg.set_data(x_data, y_avg)
        ax.relim()
        ax.autoscale_view()
        fig.tight_layout()
        return line_best, line_avg,


    ani = FuncAnimation(fig, update, interval=500, blit=True, cache_frame_data=False)
    plt.show()