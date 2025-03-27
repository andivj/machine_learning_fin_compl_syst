import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas as pd

def simulate_hmm(T, mu, sigma, P):
    states = np.zeros(T, dtype=int)
    observations = np.zeros(T)

    states[0] = np.random.choice([0,1])
    observations[0] = np.random.normal(mu[states[0]], sigma[states[0]])
    for t in range(1, T):
        states[t] = np.random.choice([0, 1], p=P[states[t-1]])
        observations[t] = np.random.normal(mu[states[t]], sigma[states[t]])
    return states, observations



# Parameters from professor paper
# note that the parameters are built in such a way that the time series keeps the same hidden state for a llong 
# period of time, ask for confirmation
mu = [0.0006, -0.0008]
sigma = [0.0078, 0.0174]
P = np.array([[0.9979, 0.0021],
              [0.0120, 0.9880]])

df = pd.DataFrame()
sim = 1000

T = [250, 500, 1000, 2000]
for t in T:
    returns_list = []
    states_list = []
    for i in range(1000):
        states, observations = simulate_hmm(sim, mu, sigma, P)
        returns_list.append(pd.Series(observations, name=f'returns_{i}'))
        states_list.append(pd.Series(states, name=f'states_{i}'))

    df_returns = pd.concat(returns_list, axis=1)
    df_states = pd.concat(states_list, axis=1)

    df = pd.concat([df_returns, df_states], axis=1)
    df.to_csv("simulated_hmm_{}.csv".format(t), index=False)
