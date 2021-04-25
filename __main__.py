import logging
import random
import math
from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
from loderunnerclient.game_client import GameClient
from loderunnerclient.internals.element import Element

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

i = 0
max_lenght = 100
result = []
paths = {}
path = ""
prev_mov = "KK"


def turn(gcb: Board):
    Person = gcb.get_my_position()
    global i
    global max_lenght
    global path
    global prev_mov
    result.clear()
    paths.clear()
    i = 0

    if gcb.is_game_over():
        return list(LoderunnerAction)[4]

    def createPath(x, y, prevPath):
        global max_lenght
        print(prevPath)

        def CreateNewPath(path):
            global i
            paths[i] = path
            i += 1

        def Up():
            global max_lenght
            if gcb.has_ladder_at(x, y) and prevPath[-1] != "v":
                if gcb.get_at(x, y)._name == "LADDER":
                    if gcb.has_gold_at(x+1, y):
                        CreateNewPath(prevPath+">G")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x+1, y)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+">T")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x+1, y)._name == "PORTAL":
                        CreateNewPath(prevPath+">O")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.has_gold_at(x-1, y):
                        CreateNewPath(prevPath+"<G")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x-1, y)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+"<T")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y-1)._name == "PORTAL":
                        CreateNewPath(prevPath+"<O")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                else:
                    if gcb.get_at(x, y-1)._name == "NONE":
                        createPath(x, y-1, prevPath+"^")
                    if gcb.get_at(x, y-1)._name == "LADDER":
                        createPath(x, y-1, prevPath+"^")
                    if gcb.get_at(x, y-1)._name == "PIPE":
                        createPath(x, y-1, prevPath+"^")
                    if gcb.has_gold_at(x, y-1):
                        CreateNewPath(prevPath+"^G")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y-1)._name == "PORTAL":
                        CreateNewPath(prevPath+"^O")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y-1)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+"^T")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2

        def Down():
            global max_lenght
            if prevPath[-1] != "^":
                if gcb.get_at(x, y)._name == "LADDER":
                    if gcb.has_gold_at(x+1, y):
                        CreateNewPath(prevPath+">G")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x+1, y)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+">T")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x+1, y)._name == "PORTAL":
                        CreateNewPath(prevPath+">O")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.has_gold_at(x-1, y):
                        CreateNewPath(prevPath+"<G")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x-1, y)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+"<T")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y-1)._name == "PORTAL":
                        CreateNewPath(prevPath+"<O")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                else:
                    if gcb.get_at(x, y+1)._name == "NONE":
                        createPath(x, y+1, prevPath+"v")
                    if gcb.get_at(x, y+1)._name == "LADDER":
                        createPath(x, y+1, prevPath+"v")
                    if gcb.get_at(x, y+1)._name == "PIPE":
                        createPath(x, y+1, prevPath+"v")
                    if gcb.has_gold_at(x, y+1):
                        CreateNewPath(prevPath+"vG")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y+1)._name == "PORTAL":
                        CreateNewPath(prevPath+"vO")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2
                    if gcb.get_at(x, y+1)._name == "THE_SHADOW_PILL":
                        CreateNewPath(prevPath+"vT")
                        if max_lenght >= len(prevPath)-2:
                            max_lenght = len(prevPath)-2

        def Right():
            global max_lenght
            if prevPath[-1] != "<":
                if (gcb.get_at(x, y+1)._name != "NONE" or gcb.get_at(x, y)._name == "PIPE") and gcb.get_at(x, y+1)._name != "PIPE" and gcb.get_at(x, y+1)._name != "THE_SHADOW_PILL" and gcb.get_at(x, y+1)._name != "PORTAL":
                    if gcb.get_at(x, y)._name == "PIPE" or gcb.get_at(x, y)._name == "LADDER":
                        if gcb.has_gold_at(x, y+1):
                            CreateNewPath(prevPath+"vG")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x, y+1)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+"vT")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x, y+1)._name == "PORTAL":
                            CreateNewPath(prevPath+"vO")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.has_gold_at(x-1, y):
                            CreateNewPath(prevPath+"<G")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x-1, y)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+"<T")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x-1, y)._name == "PORTAL":
                            CreateNewPath(prevPath+"<O")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                    if gcb.has_gold_at(Person._x+1, Person._y+3) and not gcb.has_wall_at(Person._x+1, Person._y+2) and gcb.get_at(Person._x+1, Person._y+1)._name == "BRICK" and not gcb.get_at(Person._x+1, Person._y)._name == "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y) and not gcb.has_enemy_at(Person._x+1, Person._y):
                        createPath(x+1, y, prevPath+"p")
                    if gcb.has_gold_at(Person._x+1, Person._y+2) and not gcb.has_wall_at(Person._x+1, Person._y) and gcb.get_at(Person._x+1, Person._y+1)._name == "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y) and not gcb.has_enemy_at(Person._x+1, Person._y):
                        createPath(x+1, y, prevPath+"p")
                    else:
                        if gcb.get_at(x+1, y)._name == "NONE":
                            createPath(x+1, y, prevPath+">")
                        if gcb.get_at(x+1, y)._name == "LADDER":
                            createPath(x+1, y, prevPath+">")
                        if gcb.get_at(x+1, y)._name == "PIPE":
                            createPath(x+1, y, prevPath+">")
                        if gcb.has_gold_at(x+1, y):
                            CreateNewPath(prevPath+">G")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x+1, y)._name == "PORTAL":
                            CreateNewPath(prevPath+">O")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x+1, y)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+">T")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2

        def Left():
            global max_lenght
            if prevPath[-1] != ">":
                if (gcb.get_at(x, y+1)._name != "NONE" or gcb.get_at(x, y)._name == "PIPE") and gcb.get_at(x, y+1)._name != "PIPE" and gcb.get_at(x, y+1)._name != "THE_SHADOW_PILL" and gcb.get_at(x, y+1)._name != "PORTAL":
                    if gcb.get_at(x, y)._name == "PIPE" or gcb.get_at(x, y)._name == "LADDER":
                        if gcb.has_gold_at(x, y+1):
                            CreateNewPath(prevPath+"vG")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x, y+1)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+"vT")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x, y+1)._name == "PORTAL":
                            CreateNewPath(prevPath+"vO")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.has_gold_at(x+1, y):
                            CreateNewPath(prevPath+">G")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x+1, y)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+">T")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x+1, y)._name == "PORTAL":
                            CreateNewPath(prevPath+">O")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                    if gcb.has_gold_at(Person._x-1, Person._y+3) and not gcb.has_wall_at(Person._x-1, Person._y+2) and gcb.get_at(Person._x-1, Person._y+1)._name == "BRICK" and not gcb.get_at(Person._x-1, Person._y)._name == "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y) and not gcb.has_enemy_at(Person._x-1, Person._y):
                        createPath(x-1, y, prevPath+"l")
                    if gcb.has_gold_at(Person._x-1, Person._y+2) and  gcb.get_at(Person._x-1, Person._y-1)._name == "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y) and not gcb.has_enemy_at(Person._x-1, Person._y):
                        createPath(x-1, y, prevPath+"l")
                    else:
                        if gcb.get_at(x-1, y)._name == "NONE":
                            createPath(x-1, y, prevPath+"<")
                        if gcb.get_at(x-1, y)._name == "LADDER":
                            createPath(x-1, y, prevPath+"<")
                        if gcb.get_at(x-1, y)._name == "PIPE":
                            createPath(x-1, y, prevPath+"<")
                        if gcb.has_gold_at(x-1, y):
                            CreateNewPath(prevPath+"<G")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x-1, y)._name == "PORTAL":
                            CreateNewPath(prevPath+"<O")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2
                        if gcb.get_at(x-1, y)._name == "THE_SHADOW_PILL":
                            CreateNewPath(prevPath+"<T")
                            if max_lenght >= len(prevPath)-2:
                                max_lenght = len(prevPath)-2

        if max_lenght >= len(prevPath)-5 and len(prevPath)-2 < 15:
            Left()
            Down()
            Up()
            Right()

    def filter():
        print(paths)
        if len(paths) > 0:
            for key in paths:
                if paths[key][-1] == 'G':
                    if len(paths[key]) > 2 and paths[key][:2] == "KK":
                        result.append(paths[key][2:][:-1])
                    else:
                        result.append(paths[key][1:][:-1])
                    if len(result) > 0:
                        return min(result)
                elif paths[key][-1] == 'T':
                    if len(paths[key]) > 2 and paths[key][:2] == "KK":
                        result.append(paths[key][2:][:-1])
                    else:
                        result.append(paths[key][1:][:-1])
                    if len(result) > 0:
                        return min(result)
                elif paths[key][-1] == 'O':
                    if len(paths[key]) > 2 and paths[key][:2] == "KK":
                        result.append(paths[key][2:][:-1])
                    else:
                        result.append(paths[key][1:][:-1])
                    if len(result) > 0:
                        return min(result)

        else:
            print('paths пустой')
            return "0"

    createPath(Person._x, Person._y, prev_mov)
    path = filter()
    max_lenght = 100

    def DRILL():
        if gcb.has_pipe_at(Person._x, Person._y):
            return 3
        if gcb.get_at(Person._x+1, Person._y+1)._name == "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y) and not gcb.has_enemy_at(Person._x+1, Person._y):
            return 6
        if gcb.has_gold_at(Person._x+1, Person._y+2) and not gcb.has_wall_at(Person._x+1, Person._y+1) and not gcb.get_at(Person._x+1, Person._y)._name == "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y) and not gcb.has_enemy_at(Person._x+1, Person._y):
            return 6
        if gcb.get_at(Person._x-1, Person._y+1)._name == "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y) and not gcb.has_enemy_at(Person._x-1, Person._y):
            return 7
        if gcb.has_gold_at(Person._x-1, Person._y+2) and not gcb.has_wall_at(Person._x-1, Person._y+1) and not gcb.get_at(Person._x-1, Person._y)._name == "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y) and not gcb.has_enemy_at(Person._x-1, Person._y):
            return 7
        if gcb.has_gold_at(Person._x+1, Person._y+3) and not gcb.has_wall_at(Person._x+1, Person._y+2) and gcb.get_at(Person._x+1, Person._y+1)._name == "BRICK" and not gcb.get_at(Person._x+1, Person._y)._name == "BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y):
            return 6
        if gcb.has_gold_at(Person._x-1, Person._y+3) and not gcb.has_wall_at(Person._x-1, Person._y+2) and gcb.get_at(Person._x-1, Person._y+1)._name == "BRICK" and not gcb.get_at(Person._x-1, Person._y)._name == "BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y):
            return 7
        if (gcb.get_at(Person._x+1, Person._y+1)._name == 'BRICK' or gcb.get_at(Person._x+2, Person._y+1)._name == 'BRICK') and ("BRICK" and gcb.get_at(Person._x+1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x+1, Person._y)):
            return 1
        if (gcb.get_at(Person._x-1, Person._y+1)._name == 'BRICK' or gcb.get_at(Person._x-2, Person._y+1)._name == 'BRICK') and ("BRICK" and gcb.get_at(Person._x-1, Person._y)._name != "LADDER" and not gcb.has_other_hero_at(Person._x-1, Person._y)):
            return 0
        if gcb.has_ladder_at(Person._x, Person._y) and not gcb.has_other_hero_at(Person._x+1, Person._y) and gcb.has_wall_at(Person._x, Person._y-1):
            return 2
        else:
            if gcb.has_wall_at(Person._x-1, Person._y) or gcb.has_other_hero_at(Person._x-1, Person._y) or gcb.has_enemy_at(Person._x-1, Person._y):
                return 1
            if gcb.has_wall_at(Person._x+1, Person._y) or gcb.has_other_hero_at(Person._x+1, Person._y) or gcb.has_enemy_at(Person._x+1, Person._y):
                return 0
            else:
                return random.randint(0, len(LoderunnerAction) - 6)

    def Moving():
        global path
        global prev_mov
        if path[0] == "<":
            prev_mov = "<"
            a = path[0]
            return 0
        if path[0] == ">":
            prev_mov = ">"
            return 1
        if path[0] == "^":
            prev_mov = "^"
            return 2
        if path[0] == "v":
            prev_mov = "v"
            return 3
        if path[0] == "r":
            prev_mov = "r"
            return 6
        if path[0] == "l":
            prev_mov = "l"
            return 7
        if path[0] == "0":
            prev_mov = "0"
            return DRILL()

    action_id = 4

    action_id = Moving()

    return list(LoderunnerAction)[action_id]


def main():
    gcb = GameClient(
        "https://dojorena.io/codenjoy-contest/board/player/dojorena426?code=8792369014937308148")
    gcb.run(turn)


if __name__ == "__main__":
    main()
