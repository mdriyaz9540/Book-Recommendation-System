import streamlit as st 
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl','rb'))
similarity_score= pickle.load(open('similarity_score.pkl','rb'))

def recommend(book_name):
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    recommendation = []
    for i in similar_items:
        recommendation.append(pt.index[i[0]])
    return recommendation

st.title("📚 Book Recommendation System")
selected_box= st.selectbox("Choose a Book",
                          pt.index.values)
if st.button("Recommend"):
    recommendations = recommend(selected_box)
    
    st.write("### Recommended Books:")
    for book in recommendations:
        st.write(book)
        