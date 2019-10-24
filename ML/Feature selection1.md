# Brief Filter, Wrapper, Embedded  

## import  
```
from sklearn.datasets import load_boston  
import pandas as pd  
import numpy as np  
import matplotlib  
import matplotlib.pyplot as plt  
import seaborn as sns  
import statsmodels.api as sm  
%matplotlib inline  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.feature_selection import RFE  
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso  

```  

## Filter method  
  ```  
  # See the overall correlation on the heapmap
  plt.figure(figsize=(12, 10))  
  cor = data.corr()  
  sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)  
  plt.show()  
  
  # Get the features satisfying threshold  
  cor_target = abs(cor['output'])  
  relevant_features = cor_target[cor_taret>0.5]  
  relevant_features  
  
  # Multicollinearity ?  
  data[['x1', 'x2']].corr() and so on ...  
  ```

## Wrapper method  

  ex1) Backward Elimination in OLS model
  ```  
  design_mat = sm.add_constant(X)  # X: matrix without output  
  
  model = sm.OLS(y, design_mat).fit()  
  model.pvalues  # -> Determine whether to remove one or not  
  
  # Iteration above  process
  
  # In a more organized manner  
  cols = list(X.columns)  
  pmax = 1  
  while (len(cols) > 0):  
    p_values = []  
    X_for_update = X[cols]  
    design_mat = sm.add_constant(X_for_update)  
    model = sm.OLS(y, X_for_update).fit()  
    p_values = pd.Series(model.pvalues.values[1:], index=cols) # Except constant terms  
    pmax = max(p_values)  
    pmax_feature = p_values.idxmax()  
    if(pmax > .05):  
      cols.remove(pmax_feautre)
    else:
      break  
      
   alived_features = cols; print(alived_features)  
  
  ```  
  
  ex2) RFE model  
  ```  
  # In a organized manner  
  
  nof_list = np.arange(1, len(list(X.columns))+1)  
  score = 0  
  
  nof = 0  
  score_list = []  
  
  for n in range(len(nof_list)):  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)  
    model = LinearREgression()  
    rfe = RFE(model, nof_list[n])  
    X_train_rfe = rfe.fit_transform(X_train, y_train)  
    X_test_rfe = rfe.transform(X_test)  
    model.fit(X_train_rfe, y_train)  
    score = model.score(X_test_rfe, y_test)  
    score_list.append(score)  
    if(score > high_score):  
      high_score = score  
      nof = nof_list[n]  
      
  print('The optimum number of features: %d' %nof)  
  print('Score with %d features: %f' %(nof, high_score))  
   
  # Using the optimum number above(ex. 10), make model again  
  
  cols = list(X.columns)  
  model = LinearRegression()  
  
  rfe = RFE(model, 10)  
  X_rfe = rfe.fit_transform(X,y)  
  
  model.fit(X_rfe, y)  
  temp = pd.Series(rfe.support_, index=cols)  
  selected_features_rfe = temp[temp==True].index  
  print(selected_features_rfe)  
  ```

## Embedded Method  
    ```  
    LC = LassoCV()  
    LC.fit(X,y)  

    coef = pd.Series(LC.coef_, index = X.columns)  
    
    print('Lasso picked ' + str(sum(coef != 0)) + 'variables among ' + str(len(coef)) + 'variables')  
    
    selected_coef = coef.sort_values()  
    
    matplotlib.rcParams['figure.figsize'] = (8.0, 10.0)  
    imp_coef.plot(kind = 'barh')  
    plt.title('Feature importance in Lasso Model')  
    ```
