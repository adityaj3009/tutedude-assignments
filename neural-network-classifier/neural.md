# 🧠 Neural Network from Scratch – A, B, C Image Recognition

This project implements a basic **Feedforward Neural Network** using **NumPy only** and **mathplotlib** for ploting purpose to recognize the letters **A**, **B**, and **C** represented as binary pixel grids.

---

## 📊 Dataset

Each character (A, B, C) is represented as a **5×6 binary image** (30 pixels). The labels are one-hot encoded:

- `A = [1, 0, 0]`
- `B = [0, 1, 0]`
- `C = [0, 0, 1]`

### 🔤 Sample Characters

| Character | Image Shape | Binary Pixels |
|----------|--------------|----------------|
| A        | 5x6          | `[0, 0, 1, 1, 0, 0, ...]` |
| B        | 5x6          | `[0, 1, 1, 1, 1, 0, ...]` |
| C        | 5x6          | `[0, 1, 1, 1, 1, 0, ...]` |

---

## 🛠 Features

✅ Manual dataset of characters  
✅ One hidden layer Neural Network  
✅ Forward propagation & Backpropagation  
✅ Accuracy and Loss tracking  
✅ Visualize predictions and training graphs

---

## ⚙️ Network Architecture

- **Input Layer:** 30 neurons (5x6 image)
- **Hidden Layer:** 5 neurons
- **Output Layer:** 3 neurons (one-hot for A, B, C)
- **Activation Function:** Sigmoid
- **Loss Function:** Mean Squared Error (MSE)
- **Optimizer:** Gradient Descent

---

## 🏁 How It Works

1. **Initialize random weights** for `w1` and `w2`.
2. **Forward Pass:** Input → Hidden → Output
3. **Compute Loss:** Mean squared error
4. **Backpropagate:** Update weights using gradients
5. **Train:** Repeat for multiple epochs

---

## 🧪 Example Prediction

```python
predict(x[0], w1, w2)  # Should print: image is of letter A
predict(x[1], w1, w2)  # Should print: image is of letter B
predict(x[2], w1, w2)  # Should print: image is of letter C
