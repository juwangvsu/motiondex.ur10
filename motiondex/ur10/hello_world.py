# SPDX-FileCopyrightText: Copyright (c) 2020-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.utils.stage import add_reference_to_stage
# Note: checkout the required tutorials at https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html

from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.prims import XFormPrim
import carb
from isaacsim.core.api.objects.capsule import VisualCapsule
from isaacsim.core.api.objects.sphere import VisualSphere


class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        #await self.load_world_async()
        return

    def setup_scene(self):

        world = self.get_world()
        world.scene.add_default_ground_plane()

        assets_root_path = get_assets_root_path()
        if assets_root_path is None:
            carb.log_error("Could not find Isaac Sim assets folder")
        print("asset root path ", assets_root_path)
        #usd_path = assets_root_path + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd" #work

        #if load usd fail, open the usd file, select a prim, make it default prim
        usd_path2="/isaac-sim/exts/motiondex.ur10/target_follow_flat.usd"
        add_reference_to_stage(usd_path=usd_path2,prim_path="/World/tracking")

        #usd_path="/isaac-sim/test1.usd" 
        #add_reference_to_stage(usd_path=usd_path,prim_path="/World/robot1")
        world.scene.add(
            VisualSphere(
                "/World/NavigationDome",
                name="navigation_dome_obs",
                position=[0.31, -0.018, 0.086],
                radius=0.2,
                visible=True,
            )
        )

        #add_reference_to_stage(usd_path="/isaac-sim/target_follow_flat.usd")#, prim_path="/World/dex")

        return

    async def setup_post_load(self):
        return

    async def setup_pre_reset(self):
        return

    async def setup_post_reset(self):
        return

    def world_cleanup(self):
        return
