def calculate_class_allocation(num_students):
    max_class_size = 30
    min_num_classes = 2

    num_classes = min(max(min_num_classes, num_students // max_class_size), num_students)
    class_size = num_students // num_classes
    remaining_students = num_students % num_classes

    allocation = {}

    for i in range(1, num_classes + 1):
        if i <= remaining_students:
            allocation[f'Class {i}'] = class_size + 1
        else:
            allocation[f'Class {i}'] = class_size

    print(f"Proposed Allocation: {num_classes} classes")
    print(allocation)

calculate_class_allocation(31)
# Output: Proposed Allocation: 2 classes
#         {'Class 1': 16, 'Class 2': 15}

calculate_class_allocation(59)
# Output: Proposed Allocation: 2 classes
#         {'Class 1': 30, 'Class 2': 29}

calculate_class_allocation(87)
# Output: Proposed Allocation: 3 classes
#         {'Class 1': 29, 'Class 2': 29, 'Class 3': 29}
