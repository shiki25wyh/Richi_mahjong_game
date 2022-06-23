from cmath import inf
from turtle import shape
from mahjong.hand_calculating.hand import HandCalculator 
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld
import random
import numpy as np
# import re

class Game:
    def __init__(self):
        tiles = np.zeros((136)).astype(int)
        self.tiles_dict = {}
        for i in range (136):
            tiles[i] = i
            self.tiles_dict[i] = i//4
        np.random.shuffle(tiles)
        # print(tiles)
        self.east_tiles = tiles[0:13].tolist() #0
        self.south_tiles = tiles[13:26].tolist() #1
        self.west_tiles = tiles[26:39].tolist() #2
        self.north_tiles = tiles[39:52].tolist() #3
        self.out_dora_indicators = tiles[52:57].tolist() #4
        self.in_dora_indicators = tiles[57:62].tolist() #5
        self.supplemental_tiles = tiles[62:66].tolist() #6
        self.tiles_pool = tiles[66:].tolist() #7
        self.pool_east = [] #8
        self.pool_south = [] #9
        self.pool_west = [] #10
        self.pool_north = [] #11
        self.east_append_list = [-1] #12
        self.south_append_list = [-1] #13
        self.west_append_list = [-1] #14
        self.north_append_list =[-1] #15
        self.east_meld = [] #16
        self.south_meld = [] #17
        self.west_meld = [] #18
        self.north_meld = [] #19
        
    def get_info(self):
        east_tiles = self.east_tiles
        south_tiles = self.south_tiles
        west_tiles = self.west_tiles
        north_tiles = self.north_tiles
        out_dora_indicators = self.out_dora_indicators
        in_dora_indicators = self.in_dora_indicators
        supplemental_tiles = self.supplemental_tiles
        tiles_pool = self.tiles_pool
        pool_east = self.pool_east
        pool_south = self.pool_south
        pool_west = self.pool_west
        pool_north = self.pool_north
        east_append_list = self.east_append_list
        south_append_list = self.south_append_list
        west_append_list = self.west_append_list
        north_append_list = self.north_append_list
        east_meld = self.east_meld
        south_meld = self.south_meld
        west_meld = self.west_meld
        north_meld = self.north_meld
        east_tiles.sort()
        south_tiles.sort()
        west_tiles .sort()
        north_tiles.sort()
        return (east_tiles,
                south_tiles,
                west_tiles,
                north_tiles,
                out_dora_indicators,
                in_dora_indicators,
                supplemental_tiles,
                tiles_pool,
                pool_east,
                pool_south,
                pool_west,
                pool_north,
                east_append_list,
                south_append_list,
                west_append_list,
                north_append_list,
                east_meld,
                south_meld,
                west_meld,
                north_meld)

    def player(self,player_wind,info,is_pong = -1,is_chi=-1):
        east_tiles = info[0]
        south_tiles = info[1]
        west_tiles = info[2]
        north_tiles = info[3]
        out_dora_indicators = info[4]
        in_dora_indicators = info[5]
        supplemental_tiles = info[6]
        tiles_pool = info[7]
        pool_east = info[8]
        pool_south = info[9]
        pool_west = info[10]
        pool_north = info[11]
        east_append_list = info[12]
        south_append_list = info[13]
        west_append_list = info[14]
        north_append_list = info[15]
        east_meld = info[16]
        south_meld = info[17]
        west_meld = info[18]
        north_meld = info[19]
        
        
        if len(tiles_pool)==0:
            print('Ryuukyoku')
            return 'o','v','e','r'
        
    
        if len(tiles_pool)!=0:
            match player_wind:
                case 0:
                    if is_pong == -1 and is_chi == -1:
                        east_tiles.append(tiles_pool.pop())
                    
                    south_append_list = [-1]
                    x = int(input('东choose which tile'))
                    while x not in range(len(east_tiles)):
                        x = int(input('please input correct NO.'))
                    
                    east_append_list[0] = east_tiles[x]
                    pool_east.append(east_tiles[x])
                    east_tiles.pop(x)
                    player_wind = 1
                    is_pong = -1
                    is_chi = -1

                    state_result = state(0,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles,self.tiles_dict)
                    state_result = state_result_to_string(state_result)
                    # print(state_result)
                    
                    if state_result[1] == 'pong':
                        if state_result[0] == 1:
                            is_pong = east_append_list[0]
                            player_wind = 1
                            south_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,south_tiles,south_meld)
                        if state_result[0] == 2:
                            is_pong = east_append_list[0]
                            player_wind = 2
                            west_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,west_tiles,west_meld)
                        if state_result[0] == 3:
                            is_pong = east_append_list[0]
                            player_wind = 3
                            north_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,north_tiles,north_meld)
                    elif state_result[1] == 'chi':
                        is_chi = state_result[0]
                        player_wind = 1
                        chi_tiles_meld(is_chi,south_tiles,south_meld,east_append_list)
                                        
                          
                    return player_wind,is_pong,is_chi,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)
                            
                case 1:

                    if is_pong == -1 and is_chi == -1:
                        south_tiles.append(tiles_pool.pop())
                    west_append_list = [-1]
                    x = int(input('南choose which tile'))
                    while x not in range(len(south_tiles)):
                        x = int(input('please input correct NO.'))
                    south_append_list[0] = south_tiles[x]
                    pool_south.append(south_tiles[x])
                    south_tiles.pop(x)
                    player_wind = 2
                    is_pong = -1
                    is_chi = -1


                
                    state_result = state(1,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles,self.tiles_dict)
                    state_result = state_result_to_string(state_result)
                    # print(state_result)

                    if state_result[1] == 'pong':
                        if state_result[0] == 2:
                            is_pong = south_append_list[0]
                            player_wind = 2
                            west_tiles.append(south_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)
                        if state_result[0] == 3:
                            is_pong = south_append_list[0]
                            player_wind = 3
                            north_tiles.append(south_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)
                        if state_result[0] == 0:
                            is_pong = south_append_list[0]
                            player_wind = 0
                            east_tiles.append(south_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)
                    elif state_result[1] == 'chi':
                        is_chi = state_result[0]
                        player_wind = 2
                        chi_tiles_meld(is_chi,west_tiles,west_meld,south_append_list)
                      
                    return player_wind,is_pong,is_chi,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)



                case 2:
                    if is_pong == -1 and is_chi == -1:
                        west_tiles.append(tiles_pool.pop())
                    north_append_list = [-1]
                    x = int(input('西choose which tile'))
                    while x not in range(len(west_tiles)):
                        x = int(input('please input correct NO.'))
                    west_append_list[0] = west_tiles[x]
                    pool_west.append(west_tiles[x])
                    west_tiles.pop(x)
                    player_wind = 3
                    is_pong = -1
                    is_chi = -1


                    state_result = state(2,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles,self.tiles_dict)
                    state_result = state_result_to_string(state_result)
                    # print(state_result)

                    if state_result[1] == 'pong':
                        if state_result[0] == 3:
                            is_pong = west_append_list[0]
                            player_wind = 3
                            north_tiles.append(west_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)
                        if state_result[0] == 0:
                            is_pong = west_append_list[0]
                            player_wind = 0
                            east_tiles.append(west_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)
                        if state_result[0] == 1:
                            is_pong = west_append_list[0]
                            player_wind = 1
                            south_tiles.append(west_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)
                    elif state_result[1] == 'chi':
                        is_chi = state_result[0]
                        player_wind = 3
                        
                        chi_tiles_meld(is_chi,north_tiles,north_meld,west_append_list)
    
                    return player_wind,is_pong,is_chi,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)



                case 3:
                    if is_pong == -1 and is_chi == -1:
                        north_tiles.append(tiles_pool.pop())
                    east_append_list = [-1]
                    x = int(input('北choose which tile'))
                    while x not in range(len(west_tiles)):
                        x = int(input('please input correct NO.'))
                    north_append_list[0] = north_tiles[x]
                    pool_north.append(north_tiles[x])
                    north_tiles.pop(x)
                    player_wind = 0
                    is_pong = -1
                    is_chi = -1

                    state_result = state(3,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles,self.tiles_dict)
                    state_result = state_result_to_string(state_result)
                    # print(state_result)

                    if state_result[1] == 'pong':
                        if state_result[0] == 0:
                            is_pong = north_append_list[0]
                            player_wind = 0
                            east_tiles.append(north_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)
                        if state_result[0] == 1:
                            is_pong = north_append_list[0]
                            player_wind = 1
                            south_tiles.append(north_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)
                        if state_result[0] == 2:
                            is_pong = north_append_list[0]
                            player_wind = 2
                            west_tiles.append(north_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)
                    elif state_result[1] == 'chi':
                        is_chi = state_result[0]
                        player_wind = 0
                        
                        chi_tiles_meld(is_chi,east_tiles,east_meld,north_append_list)
                      
                            
                    return player_wind,is_pong,is_chi,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)




            










    

def state(wind,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles,tiles_dict):
    pong = -1
    chi = -1
    kang = -1
    rong = -1
    state_list = []
    can_chi_result = 0
    if wind == 0:
        if can_pong(east_append_list,south_tiles):
            pong = 1
        if can_pong(east_append_list,west_tiles):
            pong = 2
        if can_pong(east_append_list,north_tiles):
            pong = 3
        can_chi_result = can_chi(east_append_list,south_tiles,tiles_dict)
        if len(can_chi_result[0])!=0:
            chi = can_chi_result

        

    if wind == 1:
        if can_pong(south_append_list,west_tiles):
            pong = 2
        if can_pong(south_append_list,north_tiles):
            pong = 3
        if can_pong(south_append_list,east_tiles):
            pong = 0
        can_chi_result = can_chi(south_append_list,west_tiles,tiles_dict)
        if len(can_chi_result[0])!=0:
            chi = can_chi_result
        

    if wind == 2:
        if can_pong(west_append_list,north_tiles):
            pong = 3
        if can_pong(west_append_list,east_tiles):
            pong = 0
        if can_pong(west_append_list,south_tiles):
            pong = 1
        can_chi_result = can_chi(west_append_list,north_tiles,tiles_dict)
        if len(can_chi_result[0])!=0:
            chi = can_chi_result
    

    if wind == 3:
        if can_pong(north_append_list,east_tiles):
            pong = 0
        if can_pong(north_append_list,south_tiles):
            pong = 1
        if can_pong(north_append_list,west_tiles):
            pong = 2
        can_chi_result = can_chi(north_append_list,east_tiles,tiles_dict)
        if len(can_chi_result[0])!=0:
            chi = can_chi_result

    state_list.append(pong)
    state_list.append(chi)
    state_list.append(kang)
    state_list.append(kang)
    return state_list




def can_pong(append_tile,list):
    if len(append_tile)>0:
        list = (np.array(list)//4).tolist() 
        tile = append_tile[0]//4
        count = list.count(tile)
        if count>=2:
            return True
        if count<2:
            return False

def pong_tiles_meld(is_pong,tile_list,meld):
    test_list=[]
    is_pong_tiles = is_pong//4
    for i in range(len(tile_list)):
        # print(list_a[i])
        k = tile_list[i]//4
        # print(k)
        if k == is_pong_tiles:
            test_list.append(tile_list[i])
        # print(test_list)
    tile_list.remove(test_list[0])
    tile_list.remove(test_list[1])
    tile_list.remove(test_list[2])
    meld.append(test_list[0])
    meld.append(test_list[1])
    meld.append(test_list[2])
    
    return tile_list,meld



def can_chi(append_tile,tiles,tiles_dict):
    append_tile = append_tile[0]
    possible_list = []
    show_list = []
    for j in tiles:
        for k in tiles:
            if j < 36 and k < 36:
                if tiles_dict[j] == (append_tile//4) - 2 and tiles_dict[k] == (append_tile//4) - 1 :
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],tiles_dict[k],append_tile//4))
                if tiles_dict[j] == (append_tile//4) - 1 and tiles_dict[k] == (append_tile//4) + 1:
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],append_tile//4,tiles_dict[k]))
                if tiles_dict[j] == (append_tile//4) + 1 and tiles_dict[k] == (append_tile//4) + 2:
                    possible_list.append((j,k))
                    show_list.append((append_tile//4,tiles_dict[j],tiles_dict[k]))

            if 36 <= j < 72 and 36 <= k < 72:
            
                if tiles_dict[j] == (append_tile//4) - 2 and tiles_dict[k] == (append_tile//4) - 1:
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],tiles_dict[k],append_tile//4))
                if tiles_dict[j] == (append_tile//4) - 1 and tiles_dict[k] == (append_tile//4) + 1:
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],append_tile//4,tiles_dict[k]))
                if tiles_dict[j] == (append_tile//4) + 1 and tiles_dict[k] == (append_tile//4) + 2:
                    possible_list.append((j,k))
                    show_list.append((append_tile//4,tiles_dict[j],tiles_dict[k]))

            if 72 <= j < 108 and 72 <= k < 108:
            
                if tiles_dict[j] == (append_tile//4) - 2 and tiles_dict[k] == (append_tile//4) - 1:
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],tiles_dict[k],append_tile//4))
                if tiles_dict[j] == (append_tile//4) - 1 and tiles_dict[k] == (append_tile//4) + 1:
                    possible_list.append((j,k))
                    show_list.append((tiles_dict[j],append_tile//4,tiles_dict[k]))
                if tiles_dict[j] == (append_tile//4) + 1 and tiles_dict[k] == (append_tile//4) + 2:
                    possible_list.append((j,k))
                    show_list.append((append_tile//4,tiles_dict[j],tiles_dict[k]))

            if len(possible_list)!=0:
                possible_list,show_list = return_chi_list(possible_list,show_list)
              
    return possible_list,show_list





def return_chi_list(possible_list,show_list):
    x=[]
    y=[]
    show_list.append('')
    for i in range(len(show_list)-1):
        if show_list[i]!=show_list[i+1]:
            x.append(possible_list[i])
            y.append(show_list[i])
    return x,y


def chi_tiles_meld(is_chi,tiles,meld,append_list):
    tiles.remove(is_chi[0])
    tiles.remove(is_chi[1])
    meld.append(append_list[0])
    meld.append(is_chi[0])
    meld.append(is_chi[1])



    

def state_result_to_string(state_list):
    state_result = []
    if state_list[0]!=-1:
        state_result.append('pong')
    if state_list[1]!=-1:
        state_result.append('chi')
    if state_list[2]!=-1:
        state_result.append('kang')
    if state_list[3]!=-1:
        state_result.append('rong')

    if len(state_result)!=0:
        state_result.append('cancel')
        x = input(state_result)
        while x not in ['pong','chi','kang','rong','cancel']:
            x = input('input correct selection')
        if x == 'pong':
            return state_list[0],'pong'
        if x == 'chi':
            print(state_list[1][1])
            y = int(input('select possible tiles to chi'))
            return state_list[1][0][y],'chi'
        if x == 'cancel':
            return 'cancel','cancel'

    elif len(state_result)==0:
        return None,None
    
    



game = Game()
info = game.get_info()
player_wind = 0
is_pong = -1
is_chi = -1
while True:

    # print(player_wind)
    if player_wind == 0:
        # print('pool\n',info[7])
        print('-----------------------')
        print('east\n',info[0],info[16])
    if player_wind == 1:
        # print('pool\n',info[7])
        print('-----------------------')
        print('south\n',info[1],info[17])
    if player_wind == 2:
        # print('pool\n',info[7])
        print('-----------------------')
        print('west\n',info[2],info[18])
    if player_wind == 3:
        # print('pool\n',info[7])
        print('-----------------------')
        print('north\n',info[3],info[19])
    if player_wind == 'o':
        break
    player_wind,is_pong,is_chi,info = game.player(player_wind=player_wind,info=info,is_pong=is_pong)
    
    
    # print(is_pong)
    # print('pool\n',info[7])
    # print('east\n',info[0])
    # print(info[8])
    # print('south',info[1])
    # print(info[9])
    # print('west\n',info[2])
    # print(info[10])
    # print('north',info[3])
    # print(info[11])
    # game.player(player_wind=player_wind,info=info,is_pong=is_pong)

# print('east_tiles',a[2][0])
# print('south_tiles',a[2][1])
# print('west_tiles',a[2][2])
# print('north_tiles',a[2][3])
# print('out_dora_indicators',a[2][4])
# print('in_dora_indicators',a[2][5])
# print('supplemental',a[2][6])
# print('tiles_pool',a[2][7])
# print('pool_east',a[2][8])
# print('pool_south',a[2][9])
# print('pool_west',a[2][10])
# print('pool_north',a[2][11])
# print('east_append_list',a[2][12])
# print('south_append_list',a[2][13])
# print('west_append_list',a[2][14])
# print('north_append_list',a[2][15])
# print('east_meld',a[2][16])
# print('south_meld',a[2][17])
# print('west_meld',a[2][18])
# print('north_meld',a[2][19])