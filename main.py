from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        if game.playing == False:
            game.show_menu()

    