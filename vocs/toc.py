#!/usr/bin/env python

from constants import *
from animation.simple_animations import Write
from animation.simple_animations import TextMobject
from scene import Scene

class TableOfContents(Scene):
    def construct(self):
        self.play(Write(TextMobject("Chapter 1 -- Text and {\\TeX}").to_edge(UP + LEFT)))


