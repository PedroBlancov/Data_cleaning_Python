'''Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent 
a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.'''

def FindIntersection(strArr):
  import string
  arrays = [arr_string.split(', ') for arr_string in strArr]
  intersection = []
  for num in arrays[0]:
    if num in arrays[1]:
      intersection.append(int(num))
  return ','.join([str(n) for n in sorted(intersection)])


print(FindIntersection(input()))
