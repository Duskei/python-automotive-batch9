def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] 
        max_area = max(max_area, height * width)

    return max_area


# USER INPUT
n = int(input("Enter number of bars: "))
heights = list(map(int, input("Enter bar heights: ").split()))

print("Largest Rectangle Area:", largestRectangleArea(heights))