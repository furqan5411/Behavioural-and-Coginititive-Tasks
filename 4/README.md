# Task 4: 


# How to launch model:
1. Use commands to build the net in the ./lib directory:
``` bash
python3 setupevonet.py build_ext --inplace
cp net*.so ../bin # or cp net*.dll ../bin
```
2. Launch learning process(from the model.ini directory)
``` bash
python3 ../bin/es.py -f (model name).ini -s (number of seed)
```
3. See results(behavior)
``` bash
python3 ../bin/es.py -f (model name).ini  -t (bestmodel.npy)
```
I've launched the algorithm for hopper and cheetah models. In case of original rewarding function, the robot can't move toward the target, it either falls down in hopper case or in case of cheetah(cheetah) different body parts moves and some don’t.  Modified function gave better results, and agents are able to move forward the goal. 

In evolutionary algorithms we must use the population of agents, learn them and pick only best ones, further learning is based on that ones (next generation). The whole process continues until certain moment. Original function are suitable for only reinforcement method, which is working with only one agent, so it can't produce evolutionary algorithms. 

Modified function is adapted to fit evolutionary strategies. There is some changes in alive bonus estimation, additional constraints like angle estimation and feet collision(calculating feet contacts), body_minx. Strategies of estimation were rewritten for each class of robot. That is why the robots can reach their goal.



