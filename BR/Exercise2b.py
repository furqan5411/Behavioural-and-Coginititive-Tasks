#Exercise 2b

import gym
import numpy as np
env = gym.make('CartPole-v0')


pvariance = 0.1
ppvariance = 0.02
nhiddens = 5
update = []
reward_list = []

addition = lambda x : x+ppvariance



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

    vector = np.concatenate((W1.flatten(),W2.flatten(),b1.flatten(),b2.flatten()))
    #print(vector)
    update.append(vector)

    # r = 0
    
    # for t in range(200):
    #     observation.resize(ninputs,1)
    #     Z1 = np.dot(W1, observation) + b1
    #     A1 = np.tanh(Z1)
    #     Z2 = np.dot(W2, A1) + b2
    #     A2 = np.tanh(Z2)
        
    #     if (isinstance(env.action_space, gym.spaces.box.Box)):
    #         action = A2
        
    #     else:
    #         action = np.argmax(A2)
    #     env.render()
        
    #     observation, reward, done, info = env.step(action)
        
    #     r = r+reward

        
    #     # if done:
    #     #     print("Episode finished after {} timesteps".format(t+1))
            
    #     #     break
    # print("Reward = ",r) 
    # reward_list.append(r)
          
#env.close()

#...................................................
arranged = np.reshape(update, (20, 37))
#print(arranged)
#print(reward_list)
#reward_list = np.argsort(reward_list)
#print(reward_list)




#for j in range(0,10):
    #arranged[reward_list[j]]=addition(arranged[reward_list[j+10]])

for l in range(30):
    update=[]
    for m in range(20):
        W1 = np.random.randn(nhiddens,ninputs) * pvariance
        W2 = np.random.randn(noutputs, nhiddens) * pvariance
        b1 = np.zeros(shape=(nhiddens, 1))
        b2 = np.zeros(shape=(noutputs, 1))

        vector = np.concatenate((W1.flatten(),W2.flatten(),b1.flatten(),b2.flatten()))
        #print(vector)
        update.append(vector)
    arranged = np.reshape(update, (20, 37))
    for k in range(30):
        r = 0
        reward_list = []
    
        for i_episode in range(20):
            observation = env.reset()
            r = 0
    

            W1= arranged[i_episode][0:20]
            W2= arranged[i_episode][20:30]
            b1= arranged[i_episode][30:35]
            b2= arranged[i_episode][35:37]


            W1 = np.reshape(W1,(5,4))
            W2 = np.reshape(W2,(2,5))
            b1 = np.reshape(b1,(5,1))
            b2 = np.reshape(b2,(2,1))




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

            print(str(k)+" kth step and " + str(i_episode) + "th episode, Reward = ",r) 
            reward_list.append(r)
          
        env.close()


        reward_list = np.argsort(reward_list)


        for j in range(0,10):
            arranged[reward_list[j]]=addition(arranged[reward_list[j+10]])

        if sum(reward_list)==200*20:
            print('Trained Successfully')
            break
    
    if sum(reward_list)==200*20:
        print('Trained Successfully')
        break    
np.save('Furqan.npy',arranged)