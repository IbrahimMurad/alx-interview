def canUnlockAll(boxes):
    locks = {
        "unlocked": {0},
        "locked": set(range(1, len(boxes)))
        }
    tikked = True
    while tikked:
        locked = locks["locked"].copy()
        unlocked = locks["unlocked"].copy()
        if not locked:
            return True
        for key in unlocked:
            locks["unlocked"].update(boxes[key])
            locks["locked"].difference_update(locks["unlocked"])
        tikked = locked.difference(locks["locked"]) != set()
    return False

# Test Case 1: Simple Case
test_case_1 = [[1], [2], [3], []]  # Expected Result: True
print(f'1. True -->  {canUnlockAll(test_case_1)}')
# Test Case 2: Unreachable Box
test_case_2 = [[1, 3], [2], [], []]  # Expected Result: True
print(f'2. True -->  {canUnlockAll(test_case_2)}')
# Test Case 3: Isolated Box
test_case_3 = [[1], [2], [], [3]]  # Expected Result: False
print(f'3. False -->  {canUnlockAll(test_case_3)}')
# Test Case 4: Redundant Keys
test_case_4 = [[1, 2, 3], [2], [3], []]  # Expected Result: True
print(f'4. True -->  {canUnlockAll(test_case_4)}')
# Test Case 5: No Keys at All
test_case_5 = [[], [], [], []]  # Expected Result: False
print(f'5. False -->  {canUnlockAll(test_case_5)}')
# Test Case 6: Circular Key References
test_case_6 = [[1], [2], [0], [3]]  # Expected Result: False
print(f'6. False -->  {canUnlockAll(test_case_6)}')
# Test Case 7: All Keys in First Box
test_case_7 = [[1, 2, 3], [], [], []]  # Expected Result: True
print(f'7. True -->  {canUnlockAll(test_case_7)}')
# Test Case 8: Multiple Keys per Box
test_case_8 = [[1, 2], [3], [3], []]  # Expected Result: True
print(f'8. True -->  {canUnlockAll(test_case_8)}')
# Additional Test Case 9: Single Box
test_case_9 = [[]]  # Expected Result: True (only one box which is already open)
print(f'9. True -->  {canUnlockAll(test_case_9)}')
# Additional Test Case 10: Multiple Paths to All Boxes
test_case_10 = [[1, 2], [2, 3], [3], []]  # Expected Result: True
print(f'10. True -->  {canUnlockAll(test_case_10)}')
# Additional Test Case 11: Disconnected Boxes
test_case_11 = [[1], [2], [4], [5], [3]]  # Expected Result: False (boxes 3 and 5 cannot be opened)
print(f'11. False -->  {canUnlockAll(test_case_11)}')
# Additional Test Case 12: Empty First Box
test_case_12 = [[], [1], [2], [3]]  # Expected Result: False (cannot open any box other than box 0)
print(f'12. False -->  {canUnlockAll(test_case_12)}')
# Additional Test Case 13: Redundant Keys and Disconnected Boxes
test_case_13 = [[1, 4], [2], [3], [], [5], []]  # Expected Result: False (box 5 cannot be opened)
print(f'13. False -->  {canUnlockAll(test_case_13)}')
# Additional Test Case 14: All Boxes Accessible with Multiple Keys
test_case_14 = [[1, 2, 4], [3, 5], [4, 5], [6], [6], [6], []]  # Expected Result: True
print(f'14. True -->  {canUnlockAll(test_case_14)}')
# Additional Test Case 15: Chain of Boxes with No Cycle
test_case_15 = [[1], [2], [3], [4], []]  # Expected Result: True
print(f'15. True -->  {canUnlockAll(test_case_15)}')
# Additional Test Case 16: Multiple Independent Chains
test_case_16 = [[1], [2], [], [4], [5], []]  # Expected Result: False (cannot access boxes 3, 4, 5)
print(f'16. False -->  {canUnlockAll(test_case_16)}')
# Additional Test Case 17: Box with Itself Key Only
test_case_17 = [[0]]  # Expected Result: True (box 0 is open, no other boxes)
print(f'17. True -->  {canUnlockAll(test_case_17)}')