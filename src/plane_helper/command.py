# SPDX-License-Identifier: MIT
# (c) 2026 dakur6

from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, name: str, description: str, usage_message: str = ""):
        if not name:
            raise ValueError("Название команды не может быть пустым!")
        if ' ' in name:
            raise ValueError("Название команды не должно содержать пробелы")
        
        self.__name = name
        self.__description = description
        self.__usage_message = name if usage_message == "" else usage_message

    @abstractmethod
    def execute(self, args: list) -> None:
        pass

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description
    
    def get_usage_message(self) -> str:
        return self.__usage_message
    
class CommandError(Exception):
    pass

class InvalideSyntaxCommandException(CommandError):
    pass

commands = {}

def register(cmd: Command) -> None:
    name = cmd.get_name()
    
    if name in commands:
        raise CommandError("Попытка повторно зарегистрировать уже зарегистрированную команду")
    
    commands[cmd.get_name()] = cmd

def get_all() -> tuple[str, Command]:
    return commands

def read() -> None:
    data = str(input()).split()
    command_name = data[0]
    args = data[1:]

    if not (command_name in commands):
        print(f"Неизвестная команда: \"{command_name}\". Воспользуйтесь командой \"help\" для просмотра списка команд")
        return
    cmd = commands[command_name]

    try:
        cmd.execute(args)
    except InvalideSyntaxCommandException:
        print(f"Использование: {cmd.get_usage_message()}")