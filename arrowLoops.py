"""
    Arrow pattern with validations
"""

arrow_base_height = int(input('Enter Base Height '))
arrow_base_width = int(input('Enter Base Width '))
arrow_head_width = int(input('Enter Head Height '))

while arrow_head_width <= arrow_base_height:
    arrow_head_width = int(input('Enter Head Height '))


for i in range(arrow_base_height):
    print('*' * arrow_base_width)

while arrow_head_width > 0:
    print('*' * arrow_head_width)
    arrow_head_width -=1