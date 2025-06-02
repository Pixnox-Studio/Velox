

class Scene:
    def __init__(self):
        self.engine = None

        self.game_objects = []
        self.game_objects_to_create = []

        self.shader = None
        self.camera = None

        self.initialised = False

    def on_event(self,event):
        pass

    def on_create(self):
        """
        this function is called once before any rendering or updating only called once

        :return: None
        """

        self.initialised = True


        for game_object in self.game_objects_to_create:
            self.add_game_object(game_object)

    def add_game_object(self, game_object):
        """
        this registers the game object to be used in the runtime

        :param game_object: GameObject class
        :return: None
        """
        if self.initialised:
            game_object.engine = self.engine
            game_object.scene = self
            game_object.on_create()

            self.game_objects.append(game_object)
        else:
            self.game_objects_to_create.append(game_object)

    def on_update(self):
        """
        this function is called once per frame

        :return: None
        """

        for component in self.game_objects:
            component.on_update()

    def on_render(self):
        """
        this function is called after any code updates and graphics are ready to be drawn

        :return: None
        """

        for component in self.game_objects:
            component.on_render()

    def on_close(self):
        """
        this function is called once before the application is closed

        :return: None
        """

        for component in self.game_objects:
            component.on_close()