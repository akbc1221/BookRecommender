def recommender(df, genre):
    '''
    Recommend top rated book from same genre.
    If only single book from that genre -> return randomly from all time top 10
    
    '''
    
    top = df[df['genre'] == genre].sort_values(by='ratings', ascending=False)
    if top.shape[0] > 1:
        return dict(top.iloc[0])
    else:
        return dict(df.sort_values(by='ratings', ascending=False).iloc[:10].sample(1).squeeze())