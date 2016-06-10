def calculate_area(width,height):
    area = width * height
    return area

print('Area calculator')
width = int(input('Enter width : '))
height = int(input('Enter height : '))
area = calculate_area(width,height)

print('Area =',area)