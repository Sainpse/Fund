from Models.DDQNAgent import DDQNAgent
from tensorflow import keras
import numpy as np

class DDGNProcessor():

    def __init__(self) -> None:

        gamma = .9,  # discount factor
        tau = 100  # target network update frequency
        architecture = (256,256)  # units per layer
        learning_rate = 0.0001  # learning rate
        l2_reg = 1e-6  # L2 regularization
        replay_capacity = int(1e6)
        batch_size = 4096
        epsilon_start = 1.0
        epsilon_end = .01
        epsilon_decay_steps = 250
        epsilon_exponential_decay = .99

        self.num_actions = 3
        self.state_dim   = 165
        self.choice      = None

        self.observation = None

        self.brain  = DDQNAgent(state_dim=self.state_dim,
                    num_actions=self.num_actions,
                    learning_rate=learning_rate,
                    gamma=gamma,
                    epsilon_start=epsilon_start,
                    epsilon_end=epsilon_end,
                    epsilon_decay_steps=epsilon_decay_steps,
                    epsilon_exponential_decay=epsilon_exponential_decay,
                    replay_capacity=replay_capacity,
                    architecture=architecture,
                    l2_reg=l2_reg,
                    tau=tau,
                    batch_size=batch_size)
    
    def loadBrain(self) -> None:
        self.brain.online_network = keras.models.load_model("./Models/weightsDDQN/online_net_weights")
        self.brain.target_network = keras.models.load_model("./Models/weightsDDQN/target_net_weights")
        print(self.brain.online_network.summary())

    def decide(self, obs) -> str:
        obs = np.array([obs])
        decision ={0:"hold", 1:"sell", 2:"buy"}
        action   =self.brain.epsilon_greedy_policy(obs)
        self.choice =  decision[action]


        return self.choice