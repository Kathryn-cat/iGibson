import logging
import os

import igibson
from igibson.envs.igibson_env import iGibsonEnv
from igibson.render.profiler import Profiler


def main():
    config_filename = os.path.join(igibson.example_config_path, "fetch_room_rearrangement.yaml")
    env = iGibsonEnv(config_file=config_filename, device_idx=2)
    for j in range(10):
        env.reset()
        for i in range(100):
            with Profiler("Environment action step"):
                action = env.action_space.sample()
                state, reward, done, info = env.step(action)
                if done:
                    logging.info("Episode finished after {} timesteps".format(i + 1))
                    break
    env.close()


if __name__ == "__main__":
    main()
