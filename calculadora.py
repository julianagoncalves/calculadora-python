#!/usr/bin/env python
# encoding: utf-8


class Calculadora:

    def __init__(self):
        self.menu_opcoes()

    def menu_opcoes(self):
        print("************** Calculadora **************")
        print("1 - Soma 2 - Subtracao 3 - Divisão 4 - Multiplicação")
        operacao = input("Qual operação deseja: ")
        primeiro_valor = input("Insira o primeiro valor: ")
        segundo_valor = input("Insira o segundo valor: ")

        if operacao == 1:
            print self.soma(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 2:
            print self.subtracao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 3:
            print self.divisao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 4:
            print self.multiplicacao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

    def soma(self, valor1, valor2):
        self.resultado = valor1 + valor2
        return self.resultado

    def subtracao(self, valor1, valor2):
        self.resultado = valor1 - valor2
        return self.resultado

    def divisao(self, valor1, valor2):
        self.resultado = valor1 / valor2
        return self.resultado

    def multiplicacao(self, valor1, valor2):
        self.resultado = valor1 * valor2
        return self.resultado

if __name__ == '__main__':

    try:
        Calculadora()

    except Exceptio