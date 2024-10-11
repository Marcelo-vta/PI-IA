from DSSE import CoverageDroneSwarmSearch
import pandas as pd
import numpy as np
from policies import random_policy
from utils import agents_step, reduce_space, best_pos

env = CoverageDroneSwarmSearch(
    drone_amount=3,
    render_mode="human",
    prob_matrix_path='config_01.npy',
    timestep_limit=200
)
# print(env.get_agents())

observations, info = env.reset()
prob_matrix = observations['drone0'][1]
# print(prob_matrix[18:33, 18:33])
max_prob = best_pos(env)

opt = {
    "drones_positions": max_prob,
}

observations, info = env.reset(options=opt)
space = reduce_space(observations['drone0'][1], 10)
print(space)
for drone in env.get_agents():
    observations[drone] = (observations[drone][0], space)
# infos_list = agents_step(env, observations, info, random_policy)

# df = pd.DataFrame(infos_list)
# df.to_csv('data_drone_1_config_1.csv', index=False)