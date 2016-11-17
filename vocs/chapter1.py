#!/usr/bin/env python

from scene import Scene
from animation.transform import Transform
from animation.transform import FadeOut
from animation.simple_animations import Write
from animation.simple_animations import TextMobject

class TexMobjectScene(Scene):
    def construct(self):
        text1 = TextMobject("Text Can be written into to the page.")
        text2 = TextMobject("Any {\\TeX} based macros can be used.")
        text3 = TextMobject("""
          \\begin{bmatrix}
          1/2 & 1/4 \\\\
          1/8 & 1/16
          \\end{bmatrix}
          """)
        self.play(Write(text1))
        self.dither()
        self.play(Transform(text1, text2))
        self.dither()
        self.play(Transform(text1, text3))
        self.dither()

