using System;

namespace mathMulti
{
    class multi
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Esta aplicação calcula a multiplicação de dois números");
            Console.WriteLine("Digite o primeiro número");
            int numOne = Int32.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Segundo Número");
            int numTwo = Int32.Parse(Console.ReadLine());

            int result = numOne * numTwo;

            Console.WriteLine($"o Resultado de {numOne} vezes {numTwo} é: {result}!");
        }
    }
}
