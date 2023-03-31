from browser import document, window, alert


def sketch(p):
  # this p is needed. it will be the processing sketch itself.
  # to do thinks like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(401, 301)
        p.background(255)
        p.rectMode(p.CORNER)

    def draw():
        p.fill(0, 87, 183)
        p.rect(0, 0, 400, 300)
        p.fill(255, 215, 0)
        p.rect(0, 150, 400, 150)

    p.setup = setup
    p.draw = draw


myp5 = window.p5.new(sketch)
