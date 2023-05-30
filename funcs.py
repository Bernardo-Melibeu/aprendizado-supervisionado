import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import (train_test_split,StratifiedKFold)
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,confusion_matrix,roc_curve,RocCurveDisplay,auc)
import seaborn as sns
import matplotlib.pyplot as plt
VARS=["fixed acidity","volatile acidity","residual sugar","total sulfur dioxide","density","alcohol"]

def faz_logreg(x,y,model):
    model.fit(X=x,y=y)
    y_prob=model.predict_proba(x)
    y_pred=model.predict(x)
    return y_prob,y_pred,model



def faz_opinion(df):
    df["opinion"]=np.zeros(df.shape[0])
    df["opinion"].loc[df["quality"]>5]=1


def faz_prompt(y,yhat):
    print(f"acuracia: {accuracy_score(y,yhat):.2f}, precisão {precision_score(y,yhat):.2f}, recall: {recall_score(y,yhat):.2f}, f1: {f1_score(y,yhat):.2f}")


def faz_splits(x,y,random_state,stratify,test_size=0.2):
    return train_test_split(x,y,random_state=random_state,stratify=stratify,test_size=test_size)


def escala_dados(x,x_test,scaler=StandardScaler()):
    x_scaled=scaler.fit_transform(x)
    x_test_scaled = scaler.transform(x_test)
    return x_scaled,x_test_scaled,scaler



def prep_logreg(df,random_state=42,stratify=None,vars=VARS,y_name="opinion"):
    x_train,x_test,y_train,y_test=train_test_split(df[vars],df[y_name],test_size=0.2,random_state=random_state,stratify=stratify)
    x_train_scaled,x_test_scaled,_=escala_dados(x_train,x_test)
    return x_train_scaled,x_test_scaled,y_train,y_test



def prep_folds(df,random_state=42,vars=VARS,y_name="opinion"):
    x=df[vars]
    y=df[y_name]
    stratify=y
    x_train,x_test,y_train,y_test=faz_splits(x,y,random_state,stratify)
    return x_train,x_test,y_train,y_test


def faz_prompt_media(f1,acc,precision,recall): 
    print(f"Meu resultado de acuracia Médio é: {np.mean(acc):.2} +- {np.std(acc): .2}")
    print(f"Meu resultado de precisão Médio é: {np.mean(precision):.2} +- {np.std(precision): .2}")
    print(f"Meu resultado de recall   Médio é: {np.mean(recall):.2} +- {np.std(recall): .2}")
    print(f"Meu resultado de F1-Score Médio é: {np.mean(f1):.2} +- {np.std(f1): .2}")



def folding_time(x_train_white_cv,y_train_white_cv,model):
    cv=StratifiedKFold(n_splits=10)
    f1=[]
    acc=[]
    precision=[]
    recall=[]
    models=[]
    scalers=[]
    for train_idx,val_idx in cv.split(x_train_white_cv,y_train_white_cv):
        x_train_white=x_train_white_cv.values[train_idx,:]
        y_train_white=y_train_white_cv.values[train_idx]
        x_val_white=x_train_white_cv.values[val_idx,:]
        y_val_white=y_train_white_cv.values[val_idx]
        x_train_white,x_val_white,scaler=escala_dados(x_train_white,x_val_white)
        scalers.append(scaler)
        y_prob_white,y_pred_white,model=faz_logreg(x_train_white,y_train_white,model)
        y_pred_val_white=model.predict(x_val_white)
        models.append(model)
        f1.append(f1_score(y_val_white,y_pred_val_white))
        acc.append(accuracy_score(y_val_white,y_pred_val_white))
        precision.append(precision_score(y_val_white,y_pred_val_white))
        recall.append(recall_score(y_val_white,y_pred_val_white))
    faz_prompt_media(f1,acc,precision,recall)
    best_layer=np.argmax(recall)
    return best_layer,models,scalers,y_prob_white,y_pred_white


def aplica_teste(x_train_white_cv,y_train_white_cv,x_test_white,y_test_white,model):
    _,_,model=faz_logreg(x_train_white_cv,y_train_white_cv,model)
    y_pred_test_white=model.predict(x_test_white)
    print("--------TESTE---------------")
    faz_prompt(y_test_white,y_pred_test_white)


def faz_tudo(model,df_white):
    x_train_white_cv,x_test_white,y_train_white_cv,y_test_white=prep_folds(df_white)
    best_layer,tree,scale,y_prob_white,y_pred_white=folding_time(x_train_white_cv,y_train_white_cv,model)
    aplica_teste(x_train_white_cv,y_train_white_cv,x_test_white,y_test_white,tree[best_layer])
    return best_layer,tree,scale  
