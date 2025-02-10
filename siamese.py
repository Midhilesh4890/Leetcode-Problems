# Siamese Network for Similarity Learning
# Introduction
# Siamese networks are a type of neural network architecture used for learning similarity between pairs of data points. In this document, we will walk through the process of utilizing a Siamese network to learn similarity between samples in a dataset containing features like Title, ProductName, Manufacture Name, and Price.

# Steps
# 1. Dataset Preparation
# Start with a dataset containing a large number of samples. Each sample should be represented by features such as Title, ProductName, Manufacture Name, and Price. Ensure that the dataset is properly cleaned and preprocessed.

# 2. Pair Generation
# From the dataset, generate pairs of samples. Each pair consists of two samples: one considered similar to the other (positive pair) and one considered dissimilar (negative pair). Define similarity/dissimilarity based on the task at hand. For example:

# Positive pairs: Samples with similar titles or from the same manufacturer.
# Negative pairs: Samples with different titles or from different manufacturers.
# 3. Labeling
# Label the generated pairs accordingly. Assign a label of 1 to positive pairs (similar) and a label of 0 to negative pairs (dissimilar).

# 4. Training and Validation Split
# Split the labeled pairs into training and validation sets. Ensure that both sets have a balanced distribution of positive and negative pairs.

# 5. Siamese Network Architecture
# Define the architecture of the Siamese network. This typically involves:

# Defining the input dimensions based on the number of features and the desired embedding dimension.
# Implementing the Siamese network model, which usually consists of an embedding layer followed by fully connected layers.
# 6. Training
# Train the Siamese network using the training set. Use a suitable loss function (e.g., Binary Cross-Entropy Loss) and optimizer (e.g., Adam) for training. Monitor the training process for convergence and adjust hyperparameters as needed.

# 7. Evaluation
# Evaluate the performance of the trained Siamese network on the validation set. Calculate metrics such as accuracy, precision, recall, or F1 score to assess the model's performance in capturing similarity.

# 8. Embedding Extraction
# After training, use the trained Siamese network to extract embeddings for individual samples in the dataset. These embeddings capture the learned similarity information and can be used for downstream tasks such as clustering, classification, or recommendation.

# Conclusion
# Utilizing a Siamese network for similarity learning enables the capture of complex relationships between data samples. By following the outlined steps, one can effectively train a Siamese network on a dataset containing various features and leverage the learned embeddings for various applications.


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import numpy as np

# Step 1: Dataset Preparation
# Assume data is loaded into X (features) and y (labels) from your dataset

# Step 2: Pair Generation
# Assume a function generate_pairs(X, y) is defined to generate pairs of samples based on similarity/dissimilarity

# Step 3: Labeling
# Assume positive pairs are labeled as 1 and negative pairs as 0

# Step 4: Training and Validation Split
X_train_pairs, X_val_pairs, y_train, y_val = train_test_split(X_pairs, y, test_size=0.2, random_state=42)

# Step 5: Text Embedding
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

def get_text_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = torch.mean(outputs.last_hidden_state, dim=1)
    return embeddings

# Step 6: Calculate Cosine Similarity
def calculate_cosine_similarity(pair1, pair2):
    embedding1 = get_text_embedding(pair1)
    embedding2 = get_text_embedding(pair2)
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity

# Step 7: Siamese Network Architecture
class SiameseNetwork(nn.Module):
    def __init__(self, input_dim, embedding_dim):
        super(SiameseNetwork, self).__init__()
        self.embedding = nn.Embedding(input_dim, embedding_dim)
        self.fc = nn.Sequential(
            nn.Linear(embedding_dim, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, embedding_dim)
        )

    def forward_once(self, x):
        x = self.embedding(x)
        x = torch.mean(x, dim=1)  # Average pooling over the sequence length
        x = self.fc(x)
        return x

# Step 8: Training and Evaluation Functions
def train_siamese_network(model, criterion, optimizer, train_loader, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model.forward_once(inputs)
            loss = criterion(outputs.squeeze(), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss / len(train_loader)}")

def evaluate_siamese_network(model, criterion, val_loader):
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model.forward_once(inputs)
            loss = criterion(outputs.squeeze(), labels)
            running_loss += loss.item()
    print(f"Validation Loss: {running_loss / len(val_loader)}")

# Step 9: Create DataLoader, criterion, optimizer, and other hyperparameters

# Define batch size
batch_size = 32

# Create DataLoader for training data
train_data = TensorDataset(torch.tensor(X_train_pairs), torch.tensor(y_train))
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)

# Define criterion (loss function)
criterion = nn.BCEWithLogitsLoss()

# Define optimizer
siamese_net = SiameseNetwork(input_dim, embedding_dim)
optimizer = optim.Adam(siamese_net.parameters(), lr=0.001)

# Step 10: Train Siamese network
num_epochs = 10
train_siamese_network(siamese_net, criterion, optimizer, train_loader, num_epochs)

# Step 11: Evaluate Siamese network
# Assuming X_val_pairs and y_val are the validation pairs and labels
val_data = TensorDataset(torch.tensor(X_val_pairs), torch.tensor(y_val))
val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)
evaluate_siamese_network(siamese_net, criterion, val_loader)

# Step 12: Extract embeddings for the entire dataset
def extract_embeddings(data):
    embeddings = []
    for pair in data:
        embeddings.append(get_text_embedding(pair))
    return torch.cat(embeddings, dim=0)

# Extract embeddings for the entire dataset
embeddings = extract_embeddings(dataset)
print("Embeddings Shape:", embeddings.shape)

################################################################################
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, Model

# Step 1: Dataset Preparation
# Assuming you have your dataset ready in a pandas DataFrame format
# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Perform preprocessing like handling missing values, encoding categorical variables, etc.
data['Price'] = StandardScaler().fit_transform(data['Price'].values.reshape(-1, 1))

# Split data into features and labels
X = data[['Title', 'ProductName', 'Manufacturer', 'Price']].values
y = data['Label'].values  # Assuming 'Label' is the target variable indicating similarity

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Pair Generation
def generate_pairs(X, y, num_pairs, positive_ratio=0.5):
    pairs = []
    labels = []
    for _ in range(num_pairs):
        idx1, idx2 = np.random.choice(len(X), 2, replace=False)
        if y[idx1] == y[idx2]:
            if np.random.rand() < positive_ratio:
                pairs.append((X[idx1], X[idx2]))
                labels.append(1)
            else:
                idx_diff = np.random.choice(np.where(y != y[idx1])[0])
                pairs.append((X[idx1], X[idx_diff]))
                labels.append(0)
        else:
            pairs.append((X[idx1], X[idx2]))
            labels.append(0)
    return np.array(pairs), np.array(labels)

# Generate pairs for training
X_train_pairs, y_train_pairs = generate_pairs(X_train, y_train, num_pairs=10000)

# Generate pairs for validation
X_val_pairs, y_val_pairs = generate_pairs(X_val, y_val, num_pairs=2000)

# Step 5: Siamese Network Architecture
def siamese_network(input_shape):
    input_1 = layers.Input(shape=input_shape)
    input_2 = layers.Input(shape=input_shape)

    # Base network
    base_network = tf.keras.Sequential([
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(32, activation='relu')
    ])

    # Encode each input using the base network
    encoded_1 = base_network(input_1)
    encoded_2 = base_network(input_2)

    # Euclidean distance between the encoded outputs
    distance = tf.reduce_sum(tf.square(tf.subtract(encoded_1, encoded_2)), axis=1)

    # Final output layer
    output = layers.Dense(1, activation='sigmoid')(distance)

    # Siamese network model
    model = Model(inputs=[input_1, input_2], outputs=output)
    return model

# Define input shape based on the number of features
input_shape = X_train_pairs.shape[1]

# Create an instance of the Siamese network model
model = siamese_network(input_shape)

# Step 6: Training
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit([X_train_pairs[:, 0], X_train_pairs[:, 1]], y_train_pairs, 
          validation_data=([X_val_pairs[:, 0], X_val_pairs[:, 1]], y_val_pairs), 
          epochs=10, batch_size=32)

# Step 7: Evaluation
# Evaluate the model
loss, accuracy = model.evaluate([X_val_pairs[:, 0], X_val_pairs[:, 1]], y_val_pairs)
print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')

# Step 8: Embedding Extraction
# Extract embeddings for individual samples
embedding_model = Model(inputs=model.input[0], outputs=model.layers[-2].output)
embeddings = embedding_model.predict(X)
