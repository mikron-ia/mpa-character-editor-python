# Test file until some more state-of-art tests are made

from domain.character import Character

if __name__ == "__main__":
    character = Character('config/basic.json', dict())
    print(character.attributes)