import numpy as np

def agents_step(env, observations, info, func):
    step = 0
    infos_list = []

    while env.agents:
        step += 1
        """actions = func(env, observations, env.agents)
        observations, rewards, terminations, truncations, infos = env.step(actions)
        info = infos['drone0']
        info['step'] = step
        infos_list.append(info)
        print(info)"""
    return infos_list


def reduce_space(array, tresh=0):
    zero_count_rows = np.count_nonzero(array, axis=0)
    zero_count_cols = np.count_nonzero(array, axis=1)

    rows_to_remove = np.argwhere(zero_count_rows < tresh).flatten()
    cols_to_remove = np.argwhere(zero_count_cols < tresh).flatten()

    rows = np.delete(np.array(range(array.shape[0])), rows_to_remove, axis=0)
    cols = np.delete(np.array(range(array.shape[1])), cols_to_remove, axis=1)

    return rows, cols

def best_pos(env):
    n_agents = len(env.get_agents())
    observations, _ = env.reset()
    prob_matrix = observations['drone0'][1]
    max_prob = [np.unravel_index(np.argmax(prob_matrix, axis=None), prob_matrix.shape)]

    val = []
    pos = []
    pos0 = max_prob[0]
    for i in range(pos0[0]-1, pos0[0]+2):
        for j in range(pos0[1]-1, pos0[1]+2):
            if i != pos0[0] and j != pos0[1]:
                val += [prob_matrix[i, j]]
                pos += [(i, j)]
    

    for _ in range(n_agents-1):
        idx = np.argmax(val)
        max_prob += [pos[idx]]

        val.pop(idx)
        pos.pop(idx)
    
    return max_prob