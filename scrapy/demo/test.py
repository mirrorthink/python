import pandas as pd
df_reg = {
    "user_id":[1,2,3],
    "game_id":[1,2,3],
    "reg_time":["2020-01-01 12:00:00","2020-01-06 12:00:00","2020-02-01 12:00:00"]
}
df_reg = pd.DataFrame(df_reg)
df_pay = {
    "user_id":[1,2,3,1],
    "pay_time":["2020-01-01 12:00:00","2020-01-06 12:00:00","2020-02-01 12:00:00","2020-01-01 12:00:00"],
    "pay_result":[1,0,1,1],
    "game_id":[1,2,3,1],
    "pay_money":[80,0,100,12]
}
df_pay = pd.DataFrame(df_pay)
game_config = {
    "game_name":["game1", "game2"],
    "game_id":[1,3]
}
game_config = pd.DataFrame(game_config)

user_game=pd.merge(df_reg,game_config,how='left')
user_game=user_game.fillna("未知游戏")

game_pay=pd.merge(df_pay,game_config,how='left')
game_pay=game_pay.fillna("未知游戏")

jan_user_game=user_game.loc[user_game['reg_time'].str.contains('2020-01')]
jan_game_pay=game_pay.loc[game_pay['pay_time'].str.contains('2020-01')]

num_agg = {'user_id':['count'],
           "pay_result":["sum"],
           "pay_money":["sum"]
           }
result=pd.merge(jan_user_game,jan_game_pay,how='outer').groupby('game_name').agg(num_agg)

result.columns=["game_name","reg_counts","money","pay_nums"]
result.to_csv(r"E:\python\test_data.csv")