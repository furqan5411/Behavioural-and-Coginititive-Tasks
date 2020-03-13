# Behavioural-and-Coginititive-Tasks

Task1:
Exercise 1. Familiarize with these commands and with the other environments available in gym. Exploit the possibility to issue the commands line by line on the python interpreter and to print variables to familiarize with the structure of the data. From the environments page of the gym.openai.com site you can also inspect the source code of the some of these environments starting from the simple classic control problems (e.g. CartPole-v0, pendulum-v1 ext.)


Task2(a,b):

a)Implement a neural network controller for a Gym problem (e.g. the CartPole-v0 problem). Initialize the network with random parameters, and evaluate the neuro-agent for 10 evaluation episodes each lasting 200 steps. You can use the following code to allocate and initialize the connection weights and the biases parameters.


b)Implement the evolutionary strategy described above and use it to train the neural network policy. You can initialize the parameters of the population with random value extracted with a normal distribution with average 0 and standard deviation. Initializing the parameters corresponding to the biases to 0.0 is usually helpful. Test your program on the CartPole-v0 problem. Does the robot manage to solve the problem? Does it solve the problem every time you run the training process? What happen by changing the parameters (e.g. size of the population, number of hidden units, the variance of the perturbation vector, the number of evaluation episodes). Test your algorithm on other simple control problem such as the Pendulum-v0.




Task3:

Run few replications of the experiment by using different seeds (integer numbers). You can use the pre-prepared acrobot.ini file included in the ./xacrobot directory. While the program is running check the source code of the environment available from the https://gym.openai.com/envs/ website to figure out the content of the observation vectors, the content of the action vector, and the way in which the reward is calculated. Plot performance across generations and then observe the behavior of evolved robots.
