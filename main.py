from DSSE import CoverageDroneSwarmSearch
import pandas as pd
import numpy as np
from policies import random_policy
from utils import agents_step, split_map, best_pos

env = CoverageDroneSwarmSearch(
    drone_amount=2,
    render_mode="human",
    prob_matrix_path='config_01.npy',
    timestep_limit=200
)

pos_inicial, limites = split_map(env)
print(limites)

opt = {
    "drones_positions": pos_inicial,
}

observations, info = env.reset(options=opt)


steps = agents_step(env, observations, info, random_policy)

# df = pd.DataFrame(steps)
# df.to_csv('data_drone_1_config_1.csv', index=False)