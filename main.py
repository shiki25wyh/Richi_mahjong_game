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
        for i in range (136):
            tiles[i] = i
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

    def player(self,player_wind,info,is_pong = -1):
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
            print('流局')
            return 'g','g','g'
        
    
        if len(tiles_pool)!=0:
            match player_wind:
                case 0:
                    if is_pong != -1:
                        south_append_list = [-1]
                        # print info
                        # print(east_tiles)
                        x = input('东choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        east_append_list[0] = east_tiles[x]
                        pool_east.append(east_tiles[x])
                        east_tiles.pop(x)
                        player_wind = 1
                        is_pong = -1

                        pong_result = pong(0,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)

                        if pong_result == 1:
                            is_pong = east_append_list[0]
                            player_wind = 1
                            south_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,south_tiles,south_meld)

                        if pong_result == 2:
                            is_pong = east_append_list[0]
                            player_wind = 2
                            west_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,west_tiles,west_meld)

                        if pong_result == 3:
                            is_pong = east_append_list[0]
                            player_wind = 3
                            north_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,north_tiles,north_meld)


                        if pong_result == 4:
                            pass
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)

                                                    
                    
                    if is_pong == -1:
                        south_append_list = [-1]   
                        east_tiles.append(tiles_pool.pop())
                        #print info
                        # print(east_tiles)
                        x = input('东choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        east_append_list[0] = east_tiles[x]
                        pool_east.append(east_tiles[x])
                        east_tiles.pop(x)
                        player_wind = 1
                        is_pong = -1

                        pong_result = pong(0,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)
                    
                        if pong_result == 1:
                            is_pong = east_append_list[0]
                            player_wind = 1
                            south_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,south_tiles,south_meld)

                        if pong_result == 2:
                            is_pong = east_append_list[0]
                            player_wind = 2
                            west_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,west_tiles,west_meld)

                        if pong_result == 3:
                            is_pong = east_append_list[0]
                            player_wind = 3
                            north_tiles.append(east_append_list.pop())
                            pong_tiles_meld(is_pong,north_tiles,north_meld)


                        if pong_result == 4:
                            pass
                            
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)
                            
                case 1:

                    if is_pong != -1:
                        west_append_list = [-1]
                        # print info
                        # print(south_tiles)
                        x = input('南choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        south_append_list[0] = south_tiles[x]
                        pool_south.append(south_tiles[x])
                        south_tiles.pop(x)
                        player_wind = 2
                        is_pong = -1


                    
                        pong_result = pong(1,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)

                        if pong_result == 2:
                            is_pong = south_append_list[0]
                            player_wind = 2
                            west_tiles.append(south_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)

                        if pong_result == 3:
                            is_pong = south_append_list[0]
                            player_wind = 3
                            north_tiles.append(south_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)

                        if pong_result == 0:
                            is_pong = south_append_list[0]
                            player_wind = 0
                            east_tiles.append(south_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)


                        if pong_result == 4:
                            pass
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)


            
                    if is_pong == -1:
                        west_append_list = [-1]
                        south_tiles.append(tiles_pool.pop())
                        # print info
                        # print(south_tiles)
                        x = input('南choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        south_append_list[0] = south_tiles[x]
                        pool_south.append(south_tiles[x])
                        south_tiles.pop(x)
                        player_wind = 2
                        is_pong = -1


                    
                        pong_result = pong(1,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)

                        if pong_result == 2:
                            is_pong = south_append_list[0]
                            player_wind = 2
                            west_tiles.append(south_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)

                        if pong_result == 3:
                            is_pong = south_append_list[0]
                            player_wind = 3
                            north_tiles.append(south_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)

                        if pong_result == 0:
                            is_pong = south_append_list[0]
                            player_wind = 0
                            east_tiles.append(south_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)


                        if pong_result == 4:
                            pass
                            
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)



                case 2:
                    if is_pong != -1:
                        north_append_list = [-1]
                        # print info
                        # print(west_tiles)
                        x = input('西choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        west_append_list[0] = west_tiles[x]
                        pool_west.append(west_tiles[x])
                        west_tiles.pop(x)
                        player_wind = 3
                        is_pong = -1


                        pong_result = pong(2,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)

                        if pong_result == 3:
                            is_pong = west_append_list[0]
                            player_wind = 3
                            north_tiles.append(west_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)

                        if pong_result == 0:
                            is_pong = west_append_list[0]
                            player_wind = 0
                            east_tiles.append(west_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)

                        if pong_result == 1:
                            is_pong = west_append_list[0]
                            player_wind = 1
                            south_tiles.append(west_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)


                        if pong_result == 4:
                            pass
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)
    





                    if is_pong == -1:
                        north_append_list = [-1]
                        west_tiles.append(tiles_pool.pop())
                        # print info
                        # print(west_tiles)
                        x = input('西choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        west_append_list[0] = west_tiles[x]
                        pool_west.append(west_tiles[x])
                        west_tiles.pop(x)
                        player_wind = 3
                        is_pong = -1


                        pong_result = pong(2,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)

                        if pong_result == 3:
                            is_pong = west_append_list[0]
                            player_wind = 3
                            north_tiles.append(west_append_list.pop())
                            north_tiles,north_meld = pong_tiles_meld(is_pong,north_tiles,north_meld)

                        if pong_result == 0:
                            is_pong = west_append_list[0]
                            player_wind = 0
                            east_tiles.append(west_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)

                        if pong_result == 1:
                            is_pong = west_append_list[0]
                            player_wind = 1
                            south_tiles.append(west_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)


                        if pong_result == 4:
                            pass
                            
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)



                case 3:
                    if is_pong != -1:
                        east_append_list = [-1]
                        # print info 
                        # print(north_tiles)
                        x = input('北choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        north_append_list[0] = north_tiles[x]
                        pool_north.append(north_tiles[x])
                        north_tiles.pop(x)
                        player_wind = 0
                        is_pong = -1

                        pong_result = pong(3,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)
                    
                            

                        if pong_result == 0:
                            is_pong = north_append_list[0]
                            player_wind = 0
                            east_tiles.append(north_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)

                        if pong_result == 1:
                            is_pong = north_append_list[0]
                            player_wind = 1
                            south_tiles.append(north_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)

                        if pong_result == 2:
                            is_pong = north_append_list[0]
                            player_wind = 2
                            west_tiles.append(north_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)
        

                        if pong_result == 4:
                            pass
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)







                    if is_pong == -1:
                        east_append_list = [-1]
                        # print info 
                        # print(north_tiles)
                        x = input('北choose which tile')
                        while x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
                            x = input('please input correct NO.')
                        x = int(x)
                        north_tiles.append(tiles_pool.pop())
                        north_append_list[0] = north_tiles[x]
                        pool_north.append(north_tiles[x])
                        north_tiles.pop(x)
                        player_wind = 0
                        is_pong = -1

                        pong_result = pong(3,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles)
                    
                            

                        if pong_result == 0:
                            is_pong = north_append_list[0]
                            player_wind = 0
                            east_tiles.append(north_append_list.pop())
                            east_tiles,east_meld = pong_tiles_meld(is_pong,east_tiles,east_meld)

                        if pong_result == 1:
                            is_pong = north_append_list[0]
                            player_wind = 1
                            south_tiles.append(north_append_list.pop())
                            south_tiles,south_meld = pong_tiles_meld(is_pong,south_tiles,south_meld)

                        if pong_result == 2:
                            is_pong = north_append_list[0]
                            player_wind = 2
                            west_tiles.append(north_append_list.pop())
                            west_tiles,west_meld = pong_tiles_meld(is_pong,west_tiles,west_meld)
        

                        if pong_result == 4:
                            pass
                            
                        return player_wind,is_pong,(east_tiles,south_tiles,west_tiles,north_tiles,out_dora_indicators,in_dora_indicators,supplemental_tiles,tiles_pool,pool_east,pool_south,pool_west,pool_north,east_append_list,south_append_list,west_append_list,north_append_list,east_meld,south_meld,west_meld,north_meld)




            




















        





    

def pong(wind,east_append_list,south_append_list,west_append_list,north_append_list,east_tiles,south_tiles,west_tiles,north_tiles):
    if wind == 0:
        if can_pong(east_append_list,south_tiles):
            x = input('东pong南y/n')
            if x == 'y':
                return 1
            if x == 'n':
                return 4
        if can_pong(east_append_list,west_tiles):
            x = input('东pong西y/n')
            if x == 'y':
                return 2
            if x == 'n':
                return 4
        if can_pong(east_append_list,north_tiles):
            x = input('东pong北y/n')
            if x == 'y':
                return 3
            if x == 'n':
                return 4
        if (can_pong(east_append_list,south_tiles) and can_pong(east_append_list,west_tiles) and can_pong(east_append_list,north_tiles)) == 0:
            return 4

    if wind == 1:
        if can_pong(south_append_list,west_tiles):
            x = input('南pong西y/n')
            if x == 'y':
                return 2
            if x == 'n':
                return 4
        if can_pong(south_append_list,north_tiles):
            x = input('南pong北y/n')
            if x == 'y':
                return 3
            if x == 'n':
                return 4
        if can_pong(south_append_list,east_tiles):
            x = input('南pong东y/n')
            if x == 'y':
                return 0
            if x == 'n':
                return 4
        if (can_pong(south_append_list,west_tiles) and can_pong(south_append_list,north_tiles) and can_pong(south_append_list,east_tiles)) == 0:
            return 4

    if wind == 2:
        if can_pong(west_append_list,north_tiles):
            x = input('西pong北y/n')
            if x == 'y':
                return 3
            if x == 'n':
                return 4
        if can_pong(west_append_list,east_tiles):
            x = input('西pong东y/n')
            if x == 'y':
                return 0
            if x == 'n':
                return 4
        if can_pong(west_append_list,south_tiles):
            x = input('西pong南y/n')
            if x == 'y':
                return 1
            if x == 'n':
                return 4
        if (can_pong(west_append_list,north_tiles) and can_pong(west_append_list,east_tiles) and can_pong(west_append_list,south_tiles)) == 0:
            return 4

    if wind == 3:
        if can_pong(north_append_list,east_tiles):
            x = input('北pong东y/n')
            if x == 'y':
                return 0
            if x == 'n':
                return 4
        if can_pong(north_append_list,south_tiles):
            x = input('北pong南y/n')
            if x == 'y':
                return 1
            if x == 'n':
                return 4
        if can_pong(north_append_list,west_tiles):
            x = input('北pong西y/n')
            if x == 'y':
                return 2
            if x == 'n':
                return 4
        if (can_pong(north_append_list,east_tiles) and can_pong(north_append_list,south_tiles) and can_pong(north_append_list,west_tiles)) == 0:
            return 4
    

def can_pong(append_tile,list):
    if len(append_tile)>0:
        list = (np.array(list)//4).tolist() 
        num = append_tile[0]//4
        count = list.count(num)
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
    


    



game = Game()
info = game.get_info()
player_wind = 0
is_pong = -1
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
    if player_wind == 'g':
        break
    player_wind,is_pong,info = game.player(player_wind=player_wind,info=info,is_pong=is_pong)
    
    
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