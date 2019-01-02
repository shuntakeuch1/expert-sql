from pathlib import Path
# txtをsqlに変換
for f in Path('./code/').rglob('*.txt'):
    if f.stem == "readme":
        f.rename('./code/'+f.stem+'.md')
    else:
        f.rename('./code/'+f.stem+'.sql')
