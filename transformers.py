# Install necessary libraries (if not already installed)
# pip install transformers datasets torch

import torch
from transformers import BertTokenizer, BertForQuestionAnswering, AdamW
from datasets import load_dataset
from torch.utils.data import DataLoader

# STEP 1: Load a pre-trained BERT model and tokenizer
# BERT's tokenizer splits text into subword tokens and converts them to numerical IDs.
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Load a pre-trained BERT model for Question Answering.
model = BertForQuestionAnswering.from_pretrained("bert-base-uncased")

# STEP 2: Load the dataset
# Here, we use the SQuAD dataset (can replace with your company's dataset).
dataset = load_dataset("squad")

# Split into training and validation sets
train_data = dataset["train"]
validation_data = dataset["validation"]

# STEP 3: Preprocess the data
def preprocess_data(example):
    """
    Preprocesses a single example by tokenizing the question and context, 
    aligning the answer to the token positions, and adding labels for training.
    """
    # Tokenize question and context with truncation/padding
    inputs = tokenizer(
        example["question"],
        example["context"],
        truncation=True,
        padding="max_length",
        max_length=384,
        return_tensors="pt"
    )
    
    # Identify the start and end token positions of the answer in the context
    answer_start = example["answers"]["answer_start"][0]
    answer_text = example["answers"]["text"][0]
    
    # Convert character positions to token positions
    start_position = inputs.char_to_token(answer_start)
    end_position = start_position + len(tokenizer(answer_text)["input_ids"]) - 1

    # Add labels for training
    inputs["start_positions"] = torch.tensor(start_position, dtype=torch.long)
    inputs["end_positions"] = torch.tensor(end_position, dtype=torch.long)
    
    return inputs

# Apply preprocessing to train and validation data
train_data = train_data.map(preprocess_data)
validation_data = validation_data.map(preprocess_data)

# STEP 4: Prepare DataLoader
def collate_fn(batch):
    """
    Prepares batches of input data and labels for training and validation.
    """
    input_ids = torch.stack([item["input_ids"].squeeze(0) for item in batch])
    attention_mask = torch.stack([item["attention_mask"].squeeze(0) for item in batch])
    start_positions = torch.tensor([item["start_positions"] for item in batch])
    end_positions = torch.tensor([item["end_positions"] for item in batch])
    
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "start_positions": start_positions,
        "end_positions": end_positions,
    }

# Create DataLoaders for training and validation
train_loader = DataLoader(train_data, batch_size=8, collate_fn=collate_fn, shuffle=True)
val_loader = DataLoader(validation_data, batch_size=8, collate_fn=collate_fn)

# STEP 5: Fine-Tune the Model
# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Optimizer for updating model weights
optimizer = AdamW(model.parameters(), lr=5e-5)

# Training Loop
print("Starting Training...")
for epoch in range(3):  # Number of epochs
    model.train()
    total_loss = 0
    for batch in train_loader:
        # Move inputs to device (GPU/CPU)
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        start_positions = batch["start_positions"].to(device)
        end_positions = batch["end_positions"].to(device)

        # Forward pass
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            start_positions=start_positions,
            end_positions=end_positions,
        )
        loss = outputs.loss
        total_loss += loss.item()

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {total_loss / len(train_loader)}")

# STEP 6: Evaluate the Model
# Evaluate on the validation set
print("\nStarting Evaluation...")
model.eval()
all_start_preds, all_end_preds = [], []
all_start_labels, all_end_labels = [], []

with torch.no_grad():
    for batch in val_loader:
        # Move inputs to device
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        start_positions = batch["start_positions"].to(device)
        end_positions = batch["end_positions"].to(device)

        # Forward pass for predictions
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        start_preds = torch.argmax(outputs.start_logits, dim=1)
        end_preds = torch.argmax(outputs.end_logits, dim=1)

        # Collect predictions and labels
        all_start_preds.extend(start_preds.cpu().numpy())
        all_end_preds.extend(end_preds.cpu().numpy())
        all_start_labels.extend(start_positions.cpu().numpy())
        all_end_labels.extend(end_positions.cpu().numpy())

# Compute accuracy for start and end positions
from sklearn.metrics import accuracy_score
start_acc = accuracy_score(all_start_labels, all_start_preds)
end_acc = accuracy_score(all_end_labels, all_end_preds)

print(f"Start Position Accuracy: {start_acc:.4f}")
print(f"End Position Accuracy: {end_acc:.4f}")

# STEP 7: Save and Deploy the Model
# Save the fine-tuned model and tokenizer
model.save_pretrained("bert-fine-tuned-qa")
tokenizer.save_pretrained("bert-fine-tuned-qa")

# Reload for inference
from transformers import pipeline
qa_pipeline = pipeline("question-answering", model="bert-fine-tuned-qa", tokenizer="bert-fine-tuned-qa")

# Example inference
result = qa_pipeline({
    "question": "Who developed BERT?",
    "context": "BERT is a transformer model developed by Google in 2018."
})
print("\nInference Result:", result)




# Explanation of the Steps
# Load Pre-trained Model and Tokenizer:

# Use a pre-trained BERT model (bert-base-uncased) for extractive QA.
# Dataset Preprocessing:

# Tokenize the input (question and context).
# Align the start and end positions of the answer in the tokenized text.
# Prepare DataLoaders:

# Group inputs into batches for efficient training and validation.
# Fine-Tune the Model:

# Train the model to predict the start and end positions of the answer span in the context.
# Evaluate:

# Measure accuracy on the validation set by comparing predicted and actual positions.
# Save and Deploy:

# Save the fine-tuned model and tokenizer for reuse in inference tasks.
