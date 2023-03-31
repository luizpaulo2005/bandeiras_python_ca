from browser import document, window, alert


def sketch(p):
  # this p is needed. it will be the processing sketch itself.
  # to do thinks like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(401, 301)
        p.background(255)
        p.rectMode(p.CORNER)

    def draw():
        p.fill(31, 81, 255)
        p.rect(0, 0, 100, 100)
        p.fill(255, 255, 0)
        p.rect(0, 300 / 3 * 1, 100, 100)
        p.fill(31, 81, 255)
        p.rect(0, 300 / 3 * 2, 100, 100)
        p.fill(255, 255, 0)
        p.rect(100, 0, 100, 300)
        p.fill(31, 81, 255)
        p.rect(200, 0, 300, 100)
        p.fill(255, 255, 0)
        p.rect(200, 300/3 * 1, 300, 100)
        p.fill(31, 81, 255)
        p.rect(200, 300/3 * 2, 300, 100)

    p.setup = setup
    p.draw = draw


myp5 = window.p5.new(sketch)
