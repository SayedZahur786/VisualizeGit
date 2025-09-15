import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from vgit.animations.push import PushAnimation

if __name__ == "__main__":
    anim = PushAnimation(commits=3, remote='origin', branch='main')
    anim.animate()