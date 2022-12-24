# PROXY DESIGN PATTERN

class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disk(self):
        print("loading " + self.filename)

    def display_image(self):
        print("display " + self.filename)


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxystate = None


class ProxyImage(Proxy):
    def display_image(self):
        if self.proxystate is None:
            self.subject.load_image_from_disk()
            self.proxystate = 1
        else:
            self.subject.display_image()


proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
proxy_image2 = ProxyImage(Image("HiRes_10Mb_Photo2"))

proxy_image1.display_image()  # loading necessary
proxy_image1.display_image()  # loading unnecessary
proxy_image2.display_image()  # loading necessary
proxy_image2.display_image()  # loading unnecessary
proxy_image1.display_image()  # loading unnecessary
