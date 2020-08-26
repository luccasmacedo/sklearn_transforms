from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class Categoric(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        
        data.loc[((data.REPROVACOES_GO > 0) & (data['NOTA_GO'].isnull())), 'NOTA_GO'] = 0       

        data.loc[(data.REPROVACOES_DE == 0) & (data.NOTA_DE == 0), 'NOTA_DE'] = 10
        data.loc[(data.REPROVACOES_EM == 0) & (data.NOTA_EM == 0), 'NOTA_EM'] = 10
        data.loc[(data.REPROVACOES_MF == 0) & (data.NOTA_MF == 0), 'NOTA_MF'] = 10
        data.loc[(data.REPROVACOES_GO == 0) & (data.NOTA_GO == 0), 'NOTA_GO'] = 10
        
        data['NOTA_GO'].fillna(data['NOTA_GO'].mean(), inplace=True)
        return data
