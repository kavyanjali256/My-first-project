import matplotlib.pyplot as plt

metrics = [
    "Accuracy", "Precision", "Recall", "F1-Score", "FPR", "FAR",
    "Detection Rate/TPR", "FNR", "Computational Cost", "Resource Cost",
    "Generalization", "Inference Speed/Latency", "Real-time Performance", "Scalability"
]

counts = [10, 8, 8, 7, 4, 2, 3, 2, 3, 2, 1, 1, 2, 1]

plt.figure(figsize=(12,6))
plt.bar(metrics, counts)
plt.xlabel("Evaluation Criteria")
plt.ylabel("Number of Papers Using the Metric")
plt.ylim(0, 12)
plt.title("Evaluation Criteria Used Across 11 Research Papers")
plt.xticks(rotation=65, ha='right')
plt.tight_layout()
plt.show()
