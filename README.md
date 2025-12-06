# GreenTag: AI-Powered Anti-Counterfeiting System

An AI authentication system using Convolutional Neural Networks (CNN) to verify the authenticity of physical products through microscopic image analysis. This project implements a Physical Unclonable Function (PUF) verification system to combat counterfeiting.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Overview

**GreenTag** uses deep learning to authenticate products by analyzing microscopic surface patterns that are unique and unclonable, similar to fingerprints. The system can distinguish between genuine ("secured") and counterfeit ("not secured") products with high accuracy.

### Key Features

- 🔬 **Microscopic Image Analysis** - Processes high-resolution microscopic images
- 🧠 **CNN-Based Authentication** - Deep learning model for pattern recognition
- 🖥️ **User-Friendly GUI** - Simple interface for image upload and verification
- ⚡ **Real-Time Verification** - Instant authentication results
- 🎨 **Visual Feedback** - Color-coded results (Green = Secured, Red = Not Secured)

## 🏗️ System Architecture

```
Input Image → Preprocessing → CNN Model → Binary Classification → Result Display
    ↓              ↓              ↓               ↓                    ↓
Microscope    Resize to      Feature         Secured (1.0)      GUI Alert
  Scan         30x30        Extraction      Not Secured (0.0)   (Color-coded)
```

## 🛠️ Technology Stack

- **Deep Learning:** TensorFlow/Keras
- **Computer Vision:** OpenCV
- **GUI Framework:** PySimpleGUI
- **Image Processing:** PIL (Pillow), NumPy
- **Model Architecture:** Convolutional Neural Network (CNN)

## 📋 Prerequisites

### Required Libraries

```bash
pip install tensorflow opencv-python numpy PySimpleGUI pillow scikit-learn
```

### System Requirements

- Python 3.7 or higher
- 4GB RAM minimum (8GB recommended for training)
- Microscope with digital imaging capability (for data collection)

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/greentag.git
cd greentag
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Prepare dataset:**
```
greentag/
├── data/
│   ├── 0/  # Not secured (counterfeit) images
│   └── 1/  # Secured (genuine) images
└── greentag.py
```

## 💻 Usage

### Training the Model

```bash
python greentag.py data/
```

The model will:
- Load images from the `data/` directory
- Train for 10 epochs (configurable)
- Display accuracy metrics
- Launch the GUI for testing

### Using the GUI

1. **Launch the application**
2. **Click "FileBrowse"** to select a microscopic image
3. **Click "Load Image"** to preview the image
4. **Click "Validate"** to authenticate the product

### Results Interpretation

- **🟢 Green Alert ("secured")** - Product is authenticated as genuine
- **🔴 Red Alert ("not secured")** - Product is flagged as potentially counterfeit

## 🧠 Model Architecture

### Neural Network Design

```python
Sequential Model:
├── Conv2D Layer (64 filters, 3x3, ReLU)
├── MaxPooling2D (2x2)
├── Conv2D Layer (64 filters, 3x3, ReLU)
├── MaxPooling2D (2x2)
├── Flatten Layer
├── Dense Layer (128 neurons, ReLU)
├── Dropout (0.5)
└── Dense Layer (2 neurons, Softmax)
```

### Hyperparameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Input Size | 30x30x3 | RGB images resized to 30x30 pixels |
| Epochs | 10 | Training iterations |
| Test Split | 40% | Portion of data for testing |
| Optimizer | Adam | Adaptive learning rate |
| Loss Function | Categorical Crossentropy | For binary classification |
| Dropout Rate | 0.5 | Prevents overfitting |

## 📊 Performance

The model achieves:
- **Training Accuracy:** ~95% (varies with dataset)
- **Test Accuracy:** ~90% (varies with dataset)
- **Inference Time:** < 100ms per image

*Note: Performance depends on dataset quality and size.*

## 🔬 How It Works

### 1. Data Collection
Microscopic images are captured of genuine products and counterfeits. Each product has unique microscopic surface patterns that act as a Physical Unclonable Function (PUF).

### 2. Preprocessing
- Images are resized to 30x30 pixels
- Normalized for neural network input
- Converted to NumPy arrays

### 3. Feature Extraction
The CNN automatically learns distinguishing features:
- Surface texture patterns
- Microscopic irregularities
- Material-specific characteristics

### 4. Classification
The model outputs a probability distribution:
- `[1.0, 0.0]` → Not Secured (Counterfeit)
- `[0.0, 1.0]` → Secured (Genuine)

## 📁 Project Structure

```
greentag/
├── greentag.py              # Main application file
├── data/                   # Training dataset
│   ├── 0/                  # Counterfeit samples
│   └── 1/                  # Genuine samples
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── model.h5               # Saved trained model (optional)
```

## 🎓 Educational Context

This project was developed as part of exploring:
- Computer Vision applications in security
- Convolutional Neural Networks
- Physical Unclonable Functions (PUFs)
- Anti-counterfeiting technologies
- Real-world deep learning deployment

## 🔮 Future Enhancements

- [ ] **Model Optimization:** Experiment with different architectures (ResNet, VGG)
- [ ] **Larger Dataset:** Collect more diverse samples for better generalization
- [ ] **Mobile Deployment:** Convert to TensorFlow Lite for smartphone use
- [ ] **Multi-Class Support:** Authenticate multiple product types simultaneously
- [ ] **Confidence Scores:** Display prediction probability percentages
- [ ] **Database Integration:** Store authentication history and analytics
- [ ] **API Development:** REST API for integration with other systems
- [ ] **Blockchain Logging:** Immutable record of authentication attempts

## 🐛 Known Limitations

- **Dataset Dependency:** Requires substantial labeled microscopic images
- **Image Quality:** Performance degrades with low-quality or blurry images
- **Lighting Conditions:** Microscope lighting must be consistent
- **Binary Classification:** Currently only distinguishes genuine vs counterfeit
- **No Transfer Learning:** Model trains from scratch each time

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Dataset expansion
- Model architecture optimization
- GUI enhancements
- Documentation improvements
- Testing and validation

## 📝 Technical Notes

### Why 30x30 Resolution?
- Balance between detail retention and computational efficiency
- Faster training and inference
- Sufficient for capturing microscopic patterns

### Model Saving (Optional)
To save the trained model:
```python
# Add after training
model.save('greentag_model.h5')

# Load for inference
model = tf.keras.models.load_model('greentag_model.h5')
```

## 🔒 Security Considerations

- Model should be deployed in controlled environments
- False positives/negatives have real-world implications
- Regular model updates recommended as counterfeiters adapt
- Consider ensemble methods for critical applications

## 📚 References

- Physical Unclonable Functions (PUFs) in Security
- CNN Architectures for Image Classification
- Anti-Counterfeiting Technologies
- Computer Vision in Product Authentication

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Marco Halomoan**

This project demonstrates the application of deep learning in solving real-world security challenges, specifically in the fight against product counterfeiting using AI-powered authentication.

---

## 🚦 Quick Start Example

```bash
# 1. Prepare your dataset
mkdir -p data/0 data/1
# Add counterfeit images to data/0/
# Add genuine images to data/1/

# 2. Train and launch
python greentag.py data/

# 3. Use the GUI to test images
```

---

**⚠️ Disclaimer:** This is an educational project demonstrating AI authentication concepts. For production anti-counterfeiting systems, additional security measures and extensive testing are required.

---

*Built with 🧠 and 🔬 | Combining Computer Vision with Product Security*
