scores = [90, 85, 78, 92, 88]

total = sum(scores)
avg = total / len(scores)

passed = 0
for score in scores:
    if score >= 80:
        passed += 1
        
print(f"합격자수: {passed}")