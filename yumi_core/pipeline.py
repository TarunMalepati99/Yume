
"""
YumePipeline
------------

This module defines the end-to-end orchestration pipeline for Yume:
1. NLP scene parsing
2. Prompt generation
3. Image generation
4. Panel organization
5. Storyboard export

Every Yume UI (Colab, Streamlit, Gradio) calls this pipeline.
"""

from typing import List, Dict, Any

# Import core components
from .config import YumeConfig
from .scene_manager import SceneManager
from .panel_manager import PanelManager
from .storyboard_builder import StoryboardBuilder
from .registry import Registry

# External modules from other packages
from yume_nlp_parser.parser import SceneParser
from yume_prompt_engine.prompt_generator import PromptGenerator
from yume_image_engine.sd_engine import SDImageEngine


class YumePipeline:
    """Main orchestration class for Yume."""

    def __init__(self, config: YumeConfig | None = None):
        self.config = config or YumeConfig()

        # Load static world + character data
        self.registry = Registry(self.config)

        # Managers
        self.scene_manager = SceneManager()
        self.panel_manager = PanelManager()
        self.storyboard_builder = StoryboardBuilder()

        # NLP + Prompt + Image
        self.scene_parser = SceneParser(self.registry)
        self.prompt_generator = PromptGenerator(self.registry)
        self.image_engine = SDImageEngine(self.config)

    # -----------------------------------------------------------
    # MAIN EXECUTION
    # -----------------------------------------------------------

    def run(self, script_text: str) -> Dict[str, Any]:
        """
        Full end-to-end generation.
        Input:
            script_text (string): Multi-line script
        Returns:
            storyboard (dict): Final output containing panels + metadata
        """

        # STEP 1: Parse script text → structured scenes
        scenes = self.scene_parser.parse(script_text)
        self.scene_manager.add_scenes(scenes)

        # STEP 2: Convert each scene to a visual prompt
        prompts = []
        for scene in scenes:
            prompt = self.prompt_generator.generate(scene)
            prompts.append(prompt)

        # STEP 3: Generate images from prompts
        images = []
        for prompt in prompts:
            img = self.image_engine.generate(prompt)
            images.append(img)
            self.panel_manager.add_panel(prompt, img)

        # STEP 4: Build storyboard from panels
        storyboard = self.storyboard_builder.build(
            panels=self.panel_manager.get_panels(),
            metadata={"total_scenes": len(scenes)}
        )

        return storyboard

    # -----------------------------------------------------------
    # UTILITIES
    # -----------------------------------------------------------

    def save_storyboard(self, storyboard: Dict[str, Any], output_path: str) -> None:
        """Save storyboard JSON or export using Yume Exporter."""
        self.storyboard_builder.save(storyboard, output_path)

    def preview(self, script_text: str):
        """
        Lightweight preview (NLP + Prompts only).
        Useful for debugging in Colab/Streamlit.
        """
        scenes = self.scene_parser.parse(script_text)
        prompts = [self.prompt_generator.generate(s) for s in scenes]
        return prompts
