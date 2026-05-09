import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Load and preprocess
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train.astype('float32') / 255.0, x_test.astype('float32') / 255.0
x_train, x_test = x_train.reshape(-1, 28, 28, 1), x_test.reshape(-1, 28, 28, 1)
y_train_cat, y_test_cat = keras.utils.to_categorical(y_train, 10), keras.utils.to_categorical(y_test, 10)

# Build and train
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)), layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)), layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(), layers.Dense(64, activation='relu'), layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train_cat, epochs=5, batch_size=128, validation_split=0.2, verbose=1)

# Evaluate and predict
test_loss, test_acc = model.evaluate(x_test, y_test_cat, verbose=0)
print(f"\nTest Accuracy: {test_acc:.4f}")
y_pred_classes = np.argmax(model.predict(x_test), axis=1)

# Show one example of each digit 0-9
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
for digit in range(10):
    idx = np.where(y_test == digit)[0][0]
    axes.flat[digit].imshow(x_test[idx].reshape(28, 28), cmap='gray')
    color = 'green' if y_test[idx] == y_pred_classes[idx] else 'red'
    axes.flat[digit].set_title(f'Digit: {digit}\nTrue: {y_test[idx]}\nPred: {y_pred_classes[idx]}', color=color)
    axes.flat[digit].axis('off')
plt.suptitle('One Example of Each Digit 0-9', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Show multiple examples of digits 3, 6, 8
fig, axes = plt.subplots(3, 4, figsize=(12, 9))
for row, digit in enumerate([3, 6, 8]):
    for col, idx in enumerate(np.where(y_test == digit)[0][:4]):
        axes[row, col].imshow(x_test[idx].reshape(28, 28), cmap='gray')
        color = 'green' if digit == y_pred_classes[idx] else 'red'
        axes[row, col].set_title(f'True: {digit}\nPred: {y_pred_classes[idx]}', color=color)
        axes[row, col].axis('off')
    for col in range(len(np.where(y_test == digit)[0][:4]), 4):
        axes[row, col].axis('off')
plt.suptitle('Multiple Examples of Digits 3, 6, 8', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Random examples per digit
fig, axes = plt.subplots(10, 2, figsize=(4, 20))
for digit in range(10):
    selected = np.random.choice(np.where(y_test == digit)[0], 2, replace=False)
    for col, idx in enumerate(selected):
        axes[digit, col].imshow(x_test[idx].reshape(28, 28), cmap='gray')
        color = 'green' if digit == y_pred_classes[idx] else 'red'
        axes[digit, col].set_title(f'Pred: {y_pred_classes[idx]}', color=color, fontsize=8)
        axes[digit, col].axis('off')
    axes[digit, 0].set_ylabel(f'Digit {digit}', rotation=0, size=12, labelpad=20)
plt.suptitle('Random Examples (2 per digit)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Print statistics
print("\n======= CLASSIFICATION REPORT =======\n", classification_report(y_test, y_pred_classes))

# Confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix(y_test, y_pred_classes), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted'); plt.ylabel('True')
plt.show()

# Show confusion stats for digits 3, 6, 8
print("\n======= CONFUSIONS FOR DIGITS 3, 6, 8 =======")
for digit in [3, 6, 8]:
    preds = y_pred_classes[y_test == digit]
    print(f"\nDigit {digit}: {np.mean(preds == digit)*100:.1f}% correct")
    for wrong_digit in np.unique(preds[preds != digit]):
        print(f"  → Misclassified as {wrong_digit}: {np.sum(preds == wrong_digit)} times")