results = [
    {'Domain': 'FINANCE', 'test size': 2000, 'Router': '97.50%'},  # 54m 57s
    {'Domain': 'MEDICINE', 'test size': 2000, 'Router': '98.25%'},  # 53m 25s
    {'Domain': 'LEETCODE', 'test size': 2000, 'Router': '82.45%'},  # 56m 01s
    {'Domain': 'EXAM', 'test size': 2000, 'Router': '81.65%'},  # 55m 31s
    {'Domain': 'WEBGPT', 'test size': 2000, 'Router': '56.99%'},  # 55m 29s
    {'Domain': 'GPT4TOOLS', 'test size': 2000, 'Router': '97.00%'},  # 52m 10s
    {'Domain': 'COT', 'test size': 2000, 'Router': '84.45%'},  # 54m 06s
    {'Domain': 'STACKOWERFLOW', 'test size': 2000, 'Router': '45.45%'},  # 58m 44s
]

# Calculate average
average_size = sum([result["test size"] for result in results]) / len(results)
average_classifier_accuracy = sum(
    [float(result["Router"].strip('%')) for result in results]
) / len(results)

# Add the average row
results.append({
    "Domain": "Average",
    "test size": average_size,
    "Router": f"{average_classifier_accuracy:.2f}%",
})
