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
for i_episode in range(20):
    observation = env.reset()
    W1 = np.random.randn(nhiddens,ninputs) * pvariance
    W2 = np.random.randn(noutputs, nhiddens) * pvariance
    b1 = np.zeros(shape=(nhiddens, 1))
    b2 = np.zeros(shape=(noutputs, 1))


    for t in range(200):
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
        
        r = r+reward
        print("Reward = ",r)