#!/usr/bin/python3
"""
lockbox algorithm
"""


def canUnlockAll(boxes):
    """
    determines if all boxes can be opened
    :param boxes: list[list]
        the list of boxes
    :return True or False
    """
    size = len(boxes)
    if size <= 1:
        return True

    current_box = boxes[0]
    opened = open_box(0, current_box, boxes, [0])
    return len(opened) == len(boxes)


def open_box(idx, current, boxes, opened):
    """
    recursively open each box with keys
    found in the opened ones

    :param idx: current index in box
    :param current: currently opened box
    :param boxes: the list of box
    :param opened: list of opened boxes

    :return list of opened boxes
    """
    size = len(boxes)
    if len(opened) == size:
        return opened

    current = boxes[idx]
    if len(current) == 0 and len(opened) < size:
        return opened

    for _, val in enumerate(current):
        if not val or val in opened or val >= size:
            continue
        opened.append(val)
        opened = open_box(val, current, boxes, opened)

    return opened
