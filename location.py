# yume_prompt_engine/location_prompt.py

class LocationPromptBuilder:
    """
    Builds prompt descriptions for environments based on world settings and scene header.
    """

    def __init__(self, world_db, environment_db):
        """
        world_db: global world.json (lighting presets, style, etc.)
        environment_db: individual environment JSONs
        """
        self.world = world_db
        self.envs = environment_db

    def build(self, location_name, time_of_day=None):
        """
        Returns a detailed prompt for the scene location.
        """

        environment = self.envs.get(location_name.lower())
        if not environment:
            return f"{location_name}"

        base_desc = environment.get("description", "")
        style = environment.get("style", self.world.get("default_style", "cinematic"))
        lighting = environment.get("lighting", self.world.get("lighting", "soft light"))

        prompt = [
            f"{location_name}",
            base_desc,
            f"style: {style}",
            f"lighting: {lighting}",
        ]

        if time_of_day:
            prompt.append(f"set during {time_of_day}")

        return ", ".join([p for p in prompt if p])
