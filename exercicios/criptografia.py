class Cifrador:
    """
    Classe para simular o cifrador de César

    Exemplo de uso:
        >>> cifrador = Cifrador(1)
        >>> cifrador.cifrar('a')
        'b'
        >>> cifrador.cifrar('b')
        'c'
        >>> cifrador.cifrar('z')
        'a'
        >>> cifrador = Cifrador(2)
        >>> cifrador.cifrar('a')
        'c'
        >>> cifrador.cifrar('b')
        'd'
        >>> cifrador.cifrar('z')
        'b'
        >>> cifrador = Cifrador(1)
        >>> cifrador.decifrar('a')
        'z'
        >>> cifrador.decifrar('b')
        'a'
        >>> cifrador.decifrar('c')
        'b'
        >>> cifrador.decifrar('z')
        'y'
        >>> cifrador=Cifrador(1)
        >>> cifrador.cifrar('renzo')
        'sfoap'
        >>> cifrador.decifrar('sfoap')
        'renzo'
        >>> chave = [2, 1]
        >>> cifrador=Cifrador(chave)
        >>> cifrador.cifrar('abcd')
        'ccee'
        >>> chave = [15, 24, 19, 7, 14, 13]
        >>> cifrador=Cifrador(chave)
        >>> cifrador.cifrar('python')
        'ewmoca'
        >>> cifrador.decifrar('ewmoca')
        'python'
    """

    def __init__(self, chave):
        self.chave = [chave] if isinstance(chave, int) else chave
        self._forca = len(self.chave)
        self.dicionario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def _cript(self, texto):
        for i in enumerate(texto.upper()):
            if i[1] in self.dicionario:
                k = (self.dicionario.find(i[1]) + self.chave[i[0] % self._forca]) % 26
                yield self.dicionario[k].lower()

    def _decript(self, texto):
        for i in enumerate(texto.upper()):
            if i[1] in self.dicionario:
                k = self.dicionario.find(i[1]) - self.chave[i[0] % self._forca]
                yield self.dicionario[k].lower()

    def cifrar(self, texto):
        return ''.join(self._cript(texto))

    def decifrar(self, texto):
        return ''.join(self._decript(texto))
