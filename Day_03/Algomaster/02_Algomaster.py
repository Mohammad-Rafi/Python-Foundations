'''
Q. Boxes, Remainders, and One Extra Box ~ (medium)

Pack 47 mugs into boxes that hold 6 mugs each.

Use floor division to count full boxes, modulo to count leftover mugs, a comparison to decide whether an extra box is needed, and `int()` to add that boolean as 0 or 1.

Expected Output:
Full boxes: 7
Leftover mugs: 5
Extra box needed: True
Boxes to ship: 8
'''

mugs_ordered = 47
mugs_per_box = 6

full_boxes = mugs_ordered // mugs_per_box

leftover_mugs = mugs_ordered % mugs_per_box

extra_box_needed = leftover_mugs > 0

boxes_to_ship = full_boxes + int(extra_box_needed)

print(f"Full boxes: {full_boxes}")
print(f"Leftover mugs: {leftover_mugs}")
print(f"Extra box needed: {extra_box_needed}")
print(f"Boxes to ship: {boxes_to_ship}")