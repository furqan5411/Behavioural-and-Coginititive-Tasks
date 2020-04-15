# Exercise 5: 
## New Gym/Bullet environment

> I followed the tutorial from given link. https://backyardrobotics.eu/2017/11/27/build-a-balancing-bot-with-openai-gym-pt-i-setting-up/. 

OpenAI Gym, Baselines and pyBullet were used in implementing this task to create the new environment balacebor-v0. It has certain structure and contains XML-file with robot description and "balancebot_env.py" script, which contains main environment methods (init(), seed(), step(), reset(), render(), methods for estimation of reward, observations, actuators and termination process).

1. Build the environment:
``` bash
cd balance-bot
pip install -e .
```
2.The environment can be used by import in the balancebot_task.py file.
```
import balance_bot.
