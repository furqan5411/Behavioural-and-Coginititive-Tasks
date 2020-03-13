#Exercise 1 

#CartPole-v0

import gym
env = gym.make('CartPole-v0')
print(env.action_space)

print(env.observation_space)

print(env.observation_space.high)

print(env.observation_space.low)




#pendulum-v1

import gym
env = gym.make('pendulum-v1')
print(env.action_space)

print(env.observation_space)

print(env.observation_space.high)

print(env.observation_space.low)
