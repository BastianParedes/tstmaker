salto_automatico = False

procedimiento = r"""Los términos tienen una parte numérica y una parte literal\\
Ejemplo 1: Considera el término $\mathrm{-6{x}^{2}yz^{5}}$. La parte numérica es el número que está multiplicando a las letras, que en este caso es $-6$. La parte literal es la parte de las letras en conjunto a sus exponentes, en este caso es $\mathrm{{x}^{2}yz^{5}}$.\\
Es importante notar que hay números en la parte literal (que son sus exponentes), pero no se relacionan con la parte numérica.\\\\
Ejemplo 2: Considera el término $\mathrm{a{b}^{10}t}$. La parte numérica es el número que está multiplicando a las letras, pero en este caso no está escrito, por lo que se asume que es 1. La parte literal es la parte de las letras en conjunto a sus esponentes, en este caso es $\mathrm{a{b}^{10}t}$.\\
En este caso puede resultar extraño que la parte literal sea todo el término, pero esto ocurre ya que la parte numérica 1 no está escrita."""
