def turn(self, last_player_claim:dict) -> dict:
    ''' 
    last_player_claim = {
        ['claim_length' : int, 'claim_rank' : {card.rank\'w','W'}]
        }
    若此参数为空（{}），则认为开始一新轮
    return = {
        'Winned' : True/False,
        ['Doubt' : True/False],
        ['Claim' : *a dict same as last_player_claim*],
        ['Pass'  : None]
        }
    Doubt、Claim、Pass 必定仅出现一个， 其中开始新轮和跟牌出现Claim。
    '''
    pass
