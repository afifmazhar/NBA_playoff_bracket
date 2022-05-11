import os
import pandas as pd
from glob2 import glob

if __name__ == "__main__":
    # read csv loop and create row replacement list
    dfs = []
    names = glob('*.csv')

    path = r"C:\Users\madwo\pclass\NBA_playoff_bracket\data\team_vs_team"
    os.chdir(path)

    old_names = ["Charlotte Bobcats", "New Jersey Nets", "New Orleans/Oklahoma City Hornets", "New Orleans Hornets","Seattle SuperSonics"]
    current_names = ["Charlotte Hornets", "Brooklyn Nets", "New Orleans Pelicans", "New Orleans Pelicans", "Oklahoma City Thunder"]

    for file in glob('*.csv'):
        df = pd.read_csv(file)
        # rename header to current abbreviation
        if 'CHA' in df.columns:
            df.rename(columns={'CHA' : 'CHO'}, inplace=True)
        if 'NJN' in df.columns:
            df.rename(columns={'NJN' : 'BRK'}, inplace=True)
        if 'NOK' in df.columns:
            df.rename(columns={'NOK' : 'NLP'}, inplace=True)
        if 'NOH' in df.columns:
            df.rename(columns={'NOH' : 'NLP'}, inplace=True)
        if 'SEA' in df.columns:
            df.rename(columns={'SEA' : 'OKC'}, inplace=True)

        # rename team name to current name
        for old in old_names:
            df.loc[file["Team"] == old, "Team"] = current_names[old_names.index(old)]

        # replace vs record into %
        for col in df.columns:
            for i, c in enumerate(df[col]):
                try:
                    if str(c).strip()[1] == "-" and str(c).strip()[0].isdigit():
                        record = str(cell).strip().split("-")
                        record_l = int(record[0])
                        record_r = int(record[1])
                        percent = str(round(record_l/sum([record_l, record_r]), 4))
                        df[col][i] = percent
                except:
                    continue
        dfs.append(df)

    os.chdir(r"C:\Users\madwo\pclass\NBA_playoff_bracket\data\clean\Team vs Team")
    for i in range(len(dfs)):
        new_df = dfs[i]
        filename = names[i]
        new_df.to_csv(str(filename), index=False)
