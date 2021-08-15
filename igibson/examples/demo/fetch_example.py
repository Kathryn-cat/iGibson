import os

import numpy as np

import igibson
from igibson.objects.ycb_object import YCBObject
from igibson.render.mesh_renderer.mesh_renderer_settings import MeshRendererSettings
from igibson.render.profiler import Profiler
from igibson.robots.fetch_robot import Fetch
from igibson.scenes.igibson_indoor_scene import InteractiveIndoorScene
from igibson.simulator import Simulator
from igibson.utils.utils import parse_config


def main():
    config = parse_config(os.path.join(igibson.example_config_path, "fetch_reaching.yaml"))
    s = Simulator(mode="headless", image_width=512, image_height=512, device_idx=2)
    scene = InteractiveIndoorScene("Rs_int", texture_randomization=False, object_randomization=False)
    s.import_ig_scene(scene)

    fetch = Fetch(config)
    s.import_robot(fetch)
    import pdb; pdb.set_trace()

    for _ in range(10):
        obj = YCBObject("003_cracker_box")
        s.import_object(obj)
        obj.set_position_orientation(np.random.uniform(low=0, high=2, size=3), [0, 0, 0, 1])

    print(s.renderer.instances)

    for i in range(10000):
        with Profiler("Simulator step"):
            turtlebot.apply_action([0.1, 0.1])
            s.step()
            rgb = s.renderer.render_robot_cameras(modes=("rgb"))
    s.disconnect()


if __name__ == "__main__":
    main()
