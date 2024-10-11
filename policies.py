import random
def random_policy(env, obs, agents, limites):
    actions = {}
    for agent in agents:
        actions[agent] = env.action_space(agent).sample()
    return actions

def trad_policy(env, obs, agents, limites):
    actions = {}


    for agent in agents:
        if obs[agent][0][0] == h:
            actions[agent] = random.choice([])
        actions[agent] = env.action_space(agent).sample()
    return actions