# 😎 **Real-Time Face Mesh Detection using OpenCV and Mediapipe**

⚡ **A Python-based project that leverages MediaPipe's Face Mesh and OpenCV to detect facial landmarks in real-time with FPS tracking.**

---

## 🚀 **Project Highlights**

- 🎯 **Real-Time Face Mesh Detection:** Detects facial landmarks using MediaPipe's `FaceMesh` solution.
- 📷 **Live Camera Input:** Works seamlessly with your webcam.
- ⏱️ **Performance Monitoring:** Displays real-time FPS (Frames Per Second) for performance analysis.
- 🎨 **Customizable Drawing Options:** Adjust the drawing specs such as color, circle radius, and thickness for visual landmarks.
- 🧠 **Detailed Pixel Mapping:** Maps landmark points to screen coordinates and prints their pixel values.

---

## 🛠️ **Technologies Used**

- 🐍 **Python**
- 📦 **OpenCV**
- 📦 **MediaPipe**
- ⏳ **Time Library**

---

## 📸 **Demo**

🎥 **Run the code and visualize your face landmarks in real-time!**

### **Example Output:**
- Real-time FPS displayed on the screen.
- Face Mesh tessellation with landmark points rendered on your face.
- Pixel values printed for each landmark point.

---

## 🧩 **Code Overview**

```python
👨‍💻 cap = cv.VideoCapture(0)
🎨 facemesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=3)
✨ results = facemesh.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
🖍️ mpdraw.draw_landmarks(img, facelms, mpFaceMesh.FACEMESH_TESSELATION)
🕒 fps = 1 / (time.time() - ptime)
```

---

## 🖥️ **How to Run**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repository-name
   ```
2. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe
   ```
3. **Run the script:**
   ```bash
   python face_mesh_detection.py
   ```
4. **Quit the program:**
   Press `Q` to exit the window.

---

## 📂 **File Structure**
```
📁 Face-Mesh-Detection
├── face_mesh_detection.py  # Main script file
└── README.md               # Project documentation
```

---

## 🤝 **Let's Stay Connected!**

📧 [Email](mailto:nimmanirishik@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/nimmani-rishik-66b632287)  
💻 [GitHub](https://github.com/)  
📷 [Instagram](https://instagram.com/rishik_3142)  

---

## 🌟 **Contribute**

Feel free to open an issue or submit a pull request to improve this project. Your contributions are always welcome!

---

## 📜 **License**

This project is licensed under the MIT License.  

---

🧑‍💻 **Crafted with ❤️ by [Nimmani Rishik](mailto:nimmanirishik@gmail.com)**
