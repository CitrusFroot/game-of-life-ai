import pandas as pd
import Cell

class GameBoard:
    _dimX = None
    _dimY = None
    board_state = None
    _init_file = None

    def __init__(self, init_file:str):
        self._init_file = init_file #input csv file to load in the board state
        self.board_state = pd.read_csv(filepath_or_buffer=self._init_file, delimiter=',') #creates pd.DataFrame
        convert_to_cells()

        #gets the dimensions TODO
        self._dimX = np.shape(self.board_state)[0]
        self._dimY = np.shape(self.board_state)[1]

    '''
    creates a cell at a specific position in the board_state
    posX: the x coordinate of the cell
    posY: the y coordinate of the cell
    '''
    def birth_cell(posX:int, posY:int):
        pass

    '''
    deletes a cell from a specific position in the board_state
    Cell: a Cell object
    '''
    def kill_cell(cell:Cell):
        pass

    '''
    converts all instances of 1 to a Cell object
    '''
    def convert_to_cells():
        pass