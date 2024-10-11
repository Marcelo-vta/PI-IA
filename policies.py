def random_policy(env, obs, agents):
    actions = {}
    for agent in agents:
        actions[agent] = env.action_space(agent).sample()
    return actions

def trad_policy(env, obs, agents):
    return