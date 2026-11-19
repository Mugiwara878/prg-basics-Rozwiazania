###
# Identifies absent students using set difference
#
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students   # różnica: co jest w pierwszym, a nie ma w drugim
print(absent_students)