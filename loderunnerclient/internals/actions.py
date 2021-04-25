from enum import Enum


class LoderunnerAction(Enum):
    GO_LEFT = "left"
    GO_RIGHT = "right"
    GO_UP = "up"
    GO_DOWN = "down"    
    DO_NOTHING = "stop"
    SUICIDE = "act(0)"
    DRILL_RIGHT = "act,right"
    DRILL_LEFT = "act,left"
