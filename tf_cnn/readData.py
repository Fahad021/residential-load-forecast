import pandas as pd

def loadResidentialData():
    data = pd.read_csv('F:/OneDrive/Load Forecast/residential/data/15min_load.csv')
    #data = pd.read_csv('F:/SkyDrive/Load Forecast/residential/data/15min_load.csv')
    data = data.as_matrix()
    return data


def getUserData(data, column):
    return data[:, column]


if __name__ == "__main__":
    data = loadResidentialData()
    
    userNo = 10
    user_load = getUserData(data, userNo)