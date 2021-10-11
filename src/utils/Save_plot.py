import os
import matplotlib.pyplot as plt


def save_plot(df, plots_name,plots_dir):
    df.plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)


    unique_filename = plots_name

    path_to_plot = os.path.join(plots_dir, plots_name)
    os.makedirs(path_to_plot, exist_ok=True)
    plt.savefig(path_to_plot)
    plt.show()
