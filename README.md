# 📚 Book Recommendation System

A simple and interactive **Book Recommendation System** built using **Machine Learning** and deployed with **Streamlit**.

🔗 **Live App:** https://book-recommendation-system-paxu6cwcucqbct7vq9wltb.streamlit.app/

---

## 🚀 Features

* 📖 Select a book from the dropdown
* 🤖 Get top 5 similar book recommendations
* ⚡ Fast and interactive UI using Streamlit
* 🧠 Uses collaborative filtering for recommendations

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**

---

## 🧠 How It Works

* A **pivot table** is created where:

  * Rows = Books
  * Columns = Users
  * Values = Ratings

* Missing values are filled with 0

* **Cosine Similarity** is used to measure similarity between books

* Based on similarity score, top 5 similar books are recommended

---

## 📂 Project Structure

```
book-recommendation-system/
│
├── app.py
├── pt.pkl
├── similarity_score.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/mdriyaz9540/book-recommendation-system.git
```

2. Navigate to project folder:

```
cd book-recommendation-system
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## ⚠️ Notes

* Make sure all `.pkl` files are present in the directory
* If facing errors, check dependencies in `requirements.txt`

---

## 🔥 Future Improvements

* Add book cover images
* Show author and ratings
* Improve UI design
* Add search functionality

---

## 🙌 Author

**Mohd Riyaz**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
