class Settings:
    """a class to store all settings"""

    def __init__(self):
        """initialize game  settings"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.0
        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)

        #alien speed
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        self.fleet_direction = 1
