import numpy as np

def agents_step(env, observations, info, func, limites):
    step = 0
    infos_list = []

    while env.agents:
        step += 1
        actions = func(env, observations, env.agents, limites)
        observations, rewards, terminations, truncations, infos = env.step(actions)
        info = infos['drone0']
        info['step'] = step
        infos_list.append(info)
        print(info)
    return infos_list


def split_map(env):
    observations, info = env.reset()
    matrix = observations['drone0'][1]
    matrix_shape = matrix.shape
    drones = env.agents

    if len(drones) == 1:
        size = matrix_shape
        pos = [(0, 0)]
        limites = [((0, matrix_shape[0]), (0, matrix_shape[1]))]

    if len(drones) == 2:
        size = (matrix_shape[0]//2, matrix_shape[1])
        pos = [(size[0]-1, 0), (size[0], 0)]
        limites = [((0, size[0]), (0, size[1])), ((size[0], size[0]*2), (0, size[1]))]

    if len(drones) == 4:
        size = (matrix_shape[0]//2, matrix_shape[1]//2)

        limites, pos = [], []
        for x in range(2):
            for y in range(2):
                meio_x = size[0]
                meio_y = size[1]
                limites += [(((-x+1)*meio_x, meio_x+(-x+1)*meio_x) , ((-y+1)*meio_y, meio_y+(-y+1)*meio_y))]
                pos += [(size[0]-x, size[1]-y)]

    resp = dict(zip(drones, limites))

    return pos, resp
    


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


def reduce_space(array, tresh=0):
    zero_count_rows = np.count_nonzero(array, axis=0)
    zero_count_cols = np.count_nonzero(array, axis=1)

    rows_to_remove = np.argwhere(zero_count_rows < tresh).flatten()
    cols_to_remove = np.argwhere(zero_count_cols < tresh).flatten()

    rows = np.delete(np.array(range(array.shape[0])), rows_to_remove, axis=0)
    cols = np.delete(np.array(range(array.shape[1])), cols_to_remove, axis=1)

    return rows, cols