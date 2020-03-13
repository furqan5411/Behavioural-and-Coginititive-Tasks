import gym
import numpy as np
env = gym.make('CartPole-v0')

pvariance = 0.1 
ppvariance = 0.02 
nhiddens = 5 

ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
 noutputs = env.action_space.shape[0]
else:
 noutputs = env.action_space.n

parameters = np.load('Furqan.npy')

W1 = parameters[0][0:20]
W2 = parameters[0][20:30]
b1 = parameters[0][30:35]
b2 = parameters[0][35:37]

W1 = np.reshape(W1,(5,4))
W2 = np.reshape(W2,(2,5))
b1 = np.reshape(b1,(5,1))
b2 = np.reshape(b2,(2,1))
r = 0


for i_episodes in range(20):
    observation = env.reset()
    W1 = parameters[0][0:20]
    W2 = parameters[0][20:30]
    b1 = parameters[0][30:35]
    b2 = parameters[0][35:37]

    W1 = np.reshape(W1,(5,4))
    W2 = np.reshape(W2,(2,5))
    b1 = np.reshape(b1,(5,1))
    b2 = np.reshape(b2,(2,1))
    print('Simulating the system for episode '+str(i_episodes)+'.')
    for j in range(200):
        observation.resize(ninputs,1)
        Z1 = np.dot(W1, observation) + b1
        A1 = np.tanh(Z1)
        Z2 = np.dot(W2, A1) + b2
        A2 = np.tanh(Z2)
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)

        env.render()
        observation, reward, done, info = env.step(action)
        if(reward==1):
            r = r+1
    env.close()
    print('Reward for epsidoe '+str(episodes)+' = ',r)
    r = 0

