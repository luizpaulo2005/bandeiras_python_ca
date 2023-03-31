from browser import document, window, alert


def sketch(p):
  # this p is needed. it will be the processing sketch itself.
  # to do thinks like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(401, 301)
        p.background(255)
        p.rectMode(p.CORNER)

    def draw():
        p.fill(0, 0, 0)
        p.rect(0, 0, 400/3, 300)
        p.fill(253, 218, 36)
        p.rect(400/3, 0, 400/3, 300)
        p.fill(239, 51, 64)
        p.rect(400/3 * 2, 0, 400/3, 300)

    p.setup = setup
    p.draw = draw


myp5 = window.p5.new(sketch)
