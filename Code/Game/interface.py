def turn(self) -> dict:
    '''   
    返回值：  
    {
        'Win' : True/False,
        'Choice': 'Follow' | 'Doubt' | 'Claim' | 'Pass'
        ['Cards' : list(actually_played_cards)],        
        ['Claim' : dict(claim_length:int, claim_rank:card_rank)],
        
    }
    在开始新的一轮（Claim）的情况下， Cards, Claim参数均存在
    在跟牌（Follow）的情况下，仅存在Cards参数
    其他情况下不存在任何可选参数
    '''
    pass
