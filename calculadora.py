#!/usr/bin/env python
# encoding: utf-8

from os import system
from os import sys


class Calculadora:

    def __init__(self):
        system("clear")
        self.menu_opcoes()

    def menu_opcoes(self):
        print("************************* Calculadora *************************\n")
        print("(1)Soma (2)Subtracao (3)Divisão (4)Multiplicação (5)Sair")
        operacao = input("\nQual operação deseja: ")

        if operacao == 1:
            primeiro_valor = input("\nInsira o primeiro valor: ")
            segundo_valor = input("Insira o segundo valor : ")

            print self.soma(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 2:
            primeiro_valor = input("\nInsira o primeiro valor: ")
            segundo_valor = input("Insira o segundo valor : ")

            print self.subtracao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 3:
            primeiro_valor = input("\nInsira o primeiro valor: ")
            segundo_valor = input("Insira o segundo valor : ")

            print self.divisao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 4:
            primeiro_valor = input("\nInsira o primeiro valor: ")
            segundo_valor = input("Insira o segundo valor : ")

            print self.multiplicacao(primeiro_valor, segundo_valor)
            self.menu_opcoes()

        if operacao == 5:
            sys.exit()

    def soma(self, valor1, valor2):
        self.resultado = valor1 + valor2
        return "\n => Resultado = " + str(self.resultado) + "\n"

    def subtracao(self, valor1, valor2):
        self.resultado = valor1 - valor2
        return "\n => Resultado = " + str(self.resultado) + "\n"

    def divisao(self, valor1, valor2):
        self.resultado = valor1 / valor2
        return "\n => Resultado = " + str(self.resultado) + "\n"

    def multiplicacao(self, valor1, valor2):
        self.resultado = valor1 * valor2
        return "\n => Resultado = " + str(self.resultado) + "\n"

if __name__ == '__main__':

    try:
        Calculadora()

    except Exception:
        print Exception
