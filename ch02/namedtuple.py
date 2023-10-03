# namedtuple.py
from collections import namedtuple

# the problem
vision = (9.5, 8.8)
print(vision)

print(vision[0])  # left eye (implicit positional reference)
print(vision[1])  # right eye (implicit positional reference)

# the solution
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0])
print(vision.left)  # same as vision[0], but explicit
print(vision.right)  # same as vision[1], but explicit

# the change
Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
print(vision.left)  # still correct
print(vision.right)  # still correct (though now is vision[2])
print(vision.combined)  # the new vision[1]
