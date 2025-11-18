"""
SceneManager
------------

Responsible for storing, organizing, and managing scenes parsed
from the user's script.

The SceneManager does NOT parse text — that is handled by
yume_nlp_parser. This module simply receives scene dictionaries
and keeps them in a structured, ordered form.

Expected scene format (example):
{
    "id": 1,
    "type": "INT" | "EXT",
    "location": "Hotel Lobby",
    "characters": ["Ram", "Mona"],
    "verbs": ["walks", "looks"],
    "dialogue": ["RAM: Where is she?"],
    "mood": "tense",
    "raw_text": "INT. HOTEL LOBBY - Ram looks around, tense."
}
"""

from typing import List, Dict, Any


class SceneManager:
    """Manages parsed scenes and maintains ordering."""

    def __init__(self):
        self.scenes: List[Dict[str, Any]] = []
        self.next_scene_id = 1

    # -----------------------------------------------------------
    # ADDING SCENES
    # -----------------------------------------------------------

    def add_scene(self, scene: Dict[str, Any]) -> None:
        """
        Add a single scene dictionary. Automatically assigns an ID if missing.
        """

        if "id" not in scene:
            scene["id"] = self.next_scene_id
            self.next_scene_id += 1

        self._validate_scene(scene)
        self.scenes.append(scene)

    def add_scenes(self, scenes: List[Dict[str, Any]]) -> None:
        """
        Add multiple scenes at once.
        """
        for scene in scenes:
            self.add_scene(scene)

    # -----------------------------------------------------------
    # RETRIEVAL
    # -----------------------------------------------------------

    def get_scene(self, scene_id: int) -> Dict[str, Any] | None:
        """
        Retrieve a scene by ID.
        """
        for scene in self.scenes:
            if scene["id"] == scene_id:
                return scene
        return None

    def get_all_scenes(self) -> List[Dict[str, Any]]:
        """
        Returns all scenes in the order they were added.
        """
        return self.scenes

    def get_scene_count(self) -> int:
        return len(self.scenes)

    # -----------------------------------------------------------
    # INTERNAL VALIDATION
    # -----------------------------------------------------------

    def _validate_scene(self, scene: Dict[str, Any]) -> None:
        """
        Basic validation to avoid corrupt pipeline data.
        """
        required_keys = ["id", "raw_text"]

        for key in required_keys:
            if key not in scene:
                raise ValueError(f"Scene missing required key: {key}")

        # Auto-fill missing fields for safety
        scene.setdefault("location", None)
        scene.setdefault("characters", [])
        scene.setdefault("verbs", [])
        scene.setdefault("dialogue", [])
        scene.setdefault("mood", None)
        scene.setdefault("type", None)

    # -----------------------------------------------------------
    # RESET / CLEAR
    # -----------------------------------------------------------

    def clear(self) -> None:
        """
        Reset all scenes.
        """
        self.scenes = []
        self.next_scene_id = 1

    # -----------------------------------------------------------
    # FOR DEBUGGING / LOGGING
    # -----------------------------------------------------------

    def summary(self) -> str:
        """
        Returns a readable summary of all scenes.
        """
        lines = ["Scene Summary:"]
        for s in self.scenes:
            lines.append(
                f"- Scene {s['id']}: {s.get('type', '')} {s.get('location', '')} "
                f"({len(s.get('characters', []))} characters)"
            )
        return "\n".join(lines)

