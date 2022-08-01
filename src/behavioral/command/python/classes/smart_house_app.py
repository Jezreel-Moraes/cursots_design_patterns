from classes.interfaces.smart_command_protocol import LightCommand


class SmartHouseApp:
    def __init__(self) -> None:
        self.commands: dict[str, LightCommand] = {}

    def add_command(self, id: str, command: LightCommand) -> None:
        if id in self.commands.keys():
            return
        self.commands[id] = command

    def execute_command(self, id: str) -> None:
        if id not in self.commands.keys():
            return
        self.commands[id].execute()

    def undo_command(self, id: str) -> None:
        if id not in self.commands.keys():
            return
        self.commands[id].undo()
