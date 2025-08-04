# data/machine_learning_data.py

machine_learning_data = {
    "title": "Machine Learning Roadmap",
    "youtube_playlist": "http://googleusercontent.com/ml_full_course_placeholder", # Placeholder
    "topics": [
        {
            "name": "Introduction to ML & Types (Scratch)",
            "explanation": "Understanding what Machine Learning is, its applications, and the main types: Supervised Learning (Regression, Classification), Unsupervised Learning (Clustering, Dimensionality Reduction), and Reinforcement Learning.",
            "example_code": None,
            "example_output": None,
            "youtube_link": "http://googleusercontent.com/ml_intro_video_placeholder" # Placeholder
        },
        {
            "name": "Python for ML: NumPy & Pandas (Intermediate)",
            "explanation": "Mastering essential Python libraries for data manipulation and numerical operations in ML: NumPy for arrays and mathematical functions, and Pandas for data structures (DataFrames) and analysis.",
            "example_code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df['A'].mean())",
            "example_output": "1.5",
            "youtube_link": "http://googleusercontent.com/ml_python_libs_video_placeholder" # Placeholder
        },
        {
            "name": "Supervised Learning: Regression (Intermediate)",
            "explanation": "Learning about regression algorithms (e.g., Linear Regression, Polynomial Regression) to predict continuous output variables. Covers concepts like hypothesis, cost function, and gradient descent.",
            "example_code": "from sklearn.linear_model import LinearRegression\nimport numpy as np\nX = np.array([[1], [2], [3]])\ny = np.array([2, 4, 5])\nmodel = LinearRegression().fit(X, y)\nprint(model.predict([[4]]))",
            "example_output": "[7.] (approx)",
            "youtube_link": "http://googleusercontent.com/regression_ml_video_placeholder" # Placeholder
        },
        {
            "name": "Supervised Learning: Classification (Intermediate)",
            "explanation": "Understanding classification algorithms (e.g., Logistic Regression, Decision Trees, SVM, K-Nearest Neighbors) to predict categorical output variables. Covers confusion matrix, precision, recall, F1-score.",
            "example_code": "from sklearn.linear_model import LogisticRegression\nX = [[1, 2], [2, 3], [3, 4], [4, 5]]\ny = [0, 0, 1, 1]\nmodel = LogisticRegression().fit(X, y)\nprint(model.predict([[5, 6]]))",
            "example_output": "[1]",
            "youtube_link": "http://googleusercontent.com/classification_ml_video_placeholder" # Placeholder
        },
        {
            "name": "Deep Learning & Neural Networks (Advanced)",
            "explanation": "Introduction to Deep Learning. Covers neural network architectures (perceptrons, multi-layer perceptrons), activation functions, backpropagation, and an overview of frameworks like TensorFlow/Keras or PyTorch.",
            "example_code": "# Conceptual Keras model:\n# from tensorflow import keras\n# model = keras.Sequential([\n#   keras.layers.Dense(units=1, input_shape=[1])\n# ])\n# model.compile(optimizer='sgd', loss='mean_squared_error')",
            "example_output": "A simple neural network model is defined.",
            "youtube_link": "http://googleusercontent.com/deep_learning_intro_placeholder" # Placeholder
        },
    ]
}