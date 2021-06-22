# Arrow pattern problem

arrow_head_height = int(input('Enter Head Height '))
arrow_base_height = int(input('Enter Base Height '))
arrow_base_width = int(input('Enter Base Width '))

"""
    printing the arrow
"""
while arrow_base_height > 0:
    print(arrow_base_width*'*')
    arrow_base_height -= 1
    if arrow_base_height == 0:
        for i in range(arrow_head_height,0,-1):
            print(i*'*')


