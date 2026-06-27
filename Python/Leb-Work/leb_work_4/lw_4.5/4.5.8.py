#8. Write a program to demonstrate the difference between sort() (in-place) and sorted() (returns a new list) using a
#sample list

# --- Scenario A: using sorted() ---
list_A = [5, 2, 9, 1]
print("--- Using sorted() ---")
print("Original list_A before:", list_A)

new_list = sorted(list_A)  # Leaves list_A intact, returns a copy
print("Returned new_list   :", new_list)
print("Original list_A after :", list_A, "(Unchanged!)")


# --- Scenario B: using .sort() ---
list_B = [5, 2, 9, 1]
print("\n--- Using .sort() ---")
print("Original list_B before:", list_B)

return_value = list_B.sort()  # Modifies list_B directly, returns None
print("Returned value        :", return_value)
print("Original list_B after :", list_B, "(Modified in-place!)")
