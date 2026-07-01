'''
Q. Chained Assignment With a Mutable Object
hard
Build three task lists to demonstrate how chained assignment shares one mutable object. Use the exact chained assignment statement `inbox = review = []` so `inbox` and `review` start as two names for the same empty list. Bind `archive` to its own separate empty list with `archive = []`.

Append "draft" through `inbox`, append "approved" through `review`, and append "saved" through `archive`. Finally, rebind `review` to a new list using the exact expression `review + ["sent"]`.

Expected Output:

inbox: ['draft', 'approved']
review: ['draft', 'approved', 'sent']
archive: ['saved']
inbox is review: False
inbox is archive: False
'''

inbox = review = []
archive = []

inbox.append("draft")
review.append("approved")
archive.append("saved")

review = review + ["sent",]

print(f"inbox: {inbox}")
print(f"review: {review}")
print(f"archive: {archive}")
print(f"inbox is review: {inbox is review}")
print(f"inbox is archive: {inbox is archive}")