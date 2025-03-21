#  Content-Based Music Recommendation System  

A **content-based recommendation system** that uses **cosine similarity** to recommend the **top 5 songs** based on user preferences. The model is deployed using **FastAPI**, returning results as a **JSON object**, making it ideal for integration into a music app.  

---

##  Features  

✅ **Content-Based Filtering** - Recommends songs based on user preferences  
✅ **Cosine Similarity** - Measures song similarity for accurate recommendations  
✅ **FastAPI Integration** - Exposes recommendations via API endpoints  
✅ **Lightweight & Fast** - Efficient and scalable model for real-time predictions  
✅ **JSON Output** - Returns recommendations in an easy-to-use format  

---

## Project Preview  

 **Example JSON Response:**  
```json
{
  "user": "example_user",
  "recommendations": [
    {"song": "Blinding Lights", "artist": "The Weeknd"},
    {"song": "Levitating", "artist": "Dua Lipa"},
    {"song": "Save Your Tears", "artist": "The Weeknd"},
    {"song": "Watermelon Sugar", "artist": "Harry Styles"},
    {"song": "Circles", "artist": "Post Malone"}
  ]
}
