# Zig-Zag-Sort-
This project is a Python-based visualization tool for the Zig-Zag (Wave) Sort algorithm using Matplotlib. It animates the sorting process step-by-step, highlighting the logic and comparisons at each stage with interactive controls.

🔍 What is Zig-Zag Sort?
Zig-Zag Sort arranges elements in an alternating fashion such that:

css
Copy
Edit
a[0] < a[1] > a[2] < a[3] > a[4] ...
This is done by comparing adjacent elements and swapping them based on a flag that alternates between < and > conditions.

🎥 Features
Dynamic bar chart animation of the sorting process

Highlights current elements being compared and swapped

Displays corresponding pseudo-code with real-time line highlighting

Buttons for:

▶️ Play

⏹️ Stop

🔁 Reset

🔄 (Optional) Randomize data (you can add this feature)

🛠️ Tech Stack
Python 3

Matplotlib

NumPy

📁 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/zigzag-sort-visualization.git
cd zigzag-sort-visualization
Install required packages:

bash
Copy
Edit
pip install matplotlib numpy
Run the script:

bash
Copy
Edit
python zigzag_sort_visualization.py
📸 Preview
(Add a GIF or screenshot of the visualization here)

📚 Educational Purpose
This project is great for students and educators who want to learn or teach sorting algorithms through visual demonstration and pseudo-code tracing.

✅ Future Improvements
Add support for other sorting algorithms

Allow manual stepping through each sort stage

Add color legend for better clarity

Export animations as videos or GIFs
