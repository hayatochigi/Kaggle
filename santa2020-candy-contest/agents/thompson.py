# Thompson Samplingによる自動販売機選択Agent
import random

''' observationとconfiguration
{'remainingOverageTime': 60, 'step': 2, 'agentIndex': 0, 'reward': 1, 'lastActions': [96, 33]}
{'episodeSteps': 2000, 'actTimeout': 0.25, 'runTimeout': 1200, 'banditCount': 100, 'decayRate': 0.97, 'sampleResolution': 100}
''' 

total_reward = 0

def agent(observation, configuration):
    global num_of_rewards_1, num_of_rewards_0, total_reward, vend_index
    # rewadsはstep0で初期化する
    if observation.step == 0:
        # 最初の選択はランダムに
        vend_index = random.randrange(configuration.banditCount)
        num_of_rewards_1 = [0] * configuration["banditCount"]
        num_of_rewards_0 = [0] * configuration["banditCount"]
    
    # observation.rewardには累積報酬が保持されているみたい
    # なので前の値から現在地を差し引いて、
    reward = observation.reward - total_reward
    # 以前選択したindexの報酬を更新する
    if reward == 1:
        num_of_rewards_1[vend_index] = num_of_rewards_1[vend_index] + 1
    else:
        num_of_rewards_0[vend_index] = num_of_rewards_0[vend_index] + 1
    total_reward = observation.reward
    
    max_random = 0
    vend_index = 0
    
    for n in range(0, configuration.banditCount):
        random_beta = random.betavariate(num_of_rewards_1[n] + 1, num_of_rewards_0[n] + 1)
        if random_beta > max_random:
            max_random = random_beta
            vend_index = n
    
    
    return vend_index
