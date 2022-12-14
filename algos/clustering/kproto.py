from sklearn.preprocessing import StandardScaler
from kmodes.kprototypes import KPrototypes
from kmodes.kprototypes import euclidean_dissim
import streamlit as st
import algos.clustering.kmeans

def process(data):


    """Process K-prototype"""
    df = data[0]
    if 'object' not in list(df.dtypes):
        return algos.clustering.kmeans.process(data)

    k = st.slider('Number of Clusters :',2,9)

    numerical_columns = df.select_dtypes('number').columns
    categorical_columns = df.select_dtypes('object').columns
    categorical_indexes = []

    # Scaling
    scaler = StandardScaler()
    for c in categorical_columns:
        categorical_indexes.append(df.columns.get_loc(c))
    if len(numerical_columns) == 0 or len(categorical_columns) == 0:
        return
    # create a copy of our data to be scaled
    df_scale = df.copy()
    # standard scale numerical features
    for c in numerical_columns:
        df_scale[c] = scaler.fit_transform(df[[c]])

    # Process Data
    kproto = KPrototypes(n_clusters=k,
                        num_dissim=euclidean_dissim,
                        random_state=0)

    kproto.fit_predict(df_scale, categorical= categorical_indexes)

    # add clusters to dataframe
    df = data[0]
    df["cluster"] = kproto.labels_

    return df