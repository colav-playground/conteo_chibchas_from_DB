import pandas as pd

df=pd.read_json('/home/restrepo/Downloads/DB.json')

p=pd.DataFrame()
for t in df.columns:
    l=df[t].dropna()
    if isinstance( l.iloc[0],list ):
        ll=len(l.sum())
    else:
        ll=df[t].dropna().shape[0]
    print( f'{t} → {ll}' )
    p=pd.concat((p,pd.DataFrame([{'Producto':t,'Cantidad':ll}])))#p.append( {'Producto':t,'Cantidad':ll},ignore_index=True ) 
