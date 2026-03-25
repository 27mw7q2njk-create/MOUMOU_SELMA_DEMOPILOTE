import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent
from .steering_piste import SteeringPiste # import de la class (composition)
from omegaconf import OmegaConf #import fichier config
cfg = OmegaConf.load("../agents/team7/configDemoPilote.yaml") # on le renome cfg= plus rapide

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = " Moumou Selma" # exo 2a: affichage nom prenom a lecran
        self.steering = SteeringPiste(cfg) # initialisation de steering
    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        acceleration = 0.5 # on roule doucement 

        correction_piste = self.steering.correction_centrePiste(obs)

        action = {
            "acceleration": acceleration,
            "steer": correction_piste,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": bool(random.getrandbits(1)),
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
