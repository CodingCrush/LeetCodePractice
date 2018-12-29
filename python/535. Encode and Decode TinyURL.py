class Codec:
    def __init__(self):
        self.store = {}
        self.allowed = 'abcdefghijklmnopqrstuvwxyz'
        self.allowed += self.allowed.upper()
        self.allowed += '0123456789'

    def generate_codec(self):
        ret = ''
        for _ in xrange(6):
            ret += random.choice(self.allowed)
        return ret

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        ret = self.generate_codec()
        while ret in self.store:
            ret = self.generate_codec()
        self.store[ret] = longUrl
        return 'http://tinyurl.com/' + ret

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.store[shortUrl.split('/')[-1]]


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))