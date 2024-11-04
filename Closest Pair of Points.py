def merge_sort(points):
    if len(points) <= 1:
        return points
    mid = len(points) // 2
    left = merge_sort(points[:mid])
    right = merge_sort(points[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

import sys
import math

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points) // 2
    left_closest = closest_pair(points[:mid])
    right_closest = closest_pair(points[mid:])
    min_distance = min(left_closest[0], right_closest[0])
    strip_closest = closest_strip(points, mid, min_distance)
    if strip_closest[0] < min_distance:
        return strip_closest
    return left_closest if left_closest[0] < right_closest[0] else right_closest

def brute_force(points):
    min_distance = sys.maxsize
    closest_pair = (min_distance, None, None)
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (min_distance, points[i], points[j])
    return closest_pair

def closest_strip(points, mid, min_distance):
    strip_points = []

    for point in points:
        if abs(point[0] - points[mid][0]) < min_distance:
            strip_points.append(point)

    strip_points.sort(key=lambda p: p[1])
    n = len(strip_points)
    closest_pair = (min_distance, None, None)
    for i in range(n):
        j = i + 1

        while j < n and (strip_points[j][1] - strip_points[i][1]) < closest_pair[0]:
            distance = euclidean_distance(strip_points[i], strip_points[j])
            if distance < closest_pair[0]:
                closest_pair = (distance, strip_points[i], strip_points[j])
            j += 1
    return closest_pair

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Usage
import random

def generate_unique_points(num_points, max_coordinate=1000):
    points = set()
    while len(points) < num_points:
        x, y = random.randint(0, max_coordinate), random.randint(0, max_coordinate)
        points.add((x, y))
    return list(points)

def test_case():
    points = generate_unique_points(1000)
    print("Original Points Sample (10 points):", points[:10])

    sorted_points = merge_sort(points)
    print("Sorted Points Sample (10 points):", sorted_points[:10])

    closest = closest_pair(sorted_points)
    print("Closest Pair:", closest)


test_case()