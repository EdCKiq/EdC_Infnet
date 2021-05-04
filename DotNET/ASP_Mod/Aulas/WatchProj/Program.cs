using System;

namespace WatchProj
{
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Olá Mundo!");
            Console.WriteLine("Testando o \'dotnet watch run\'");
            var nome = "Kaique";
            Console.WriteLine(nome);
            Console.WriteLine("Hora e data atuais: " + DateTime.Now);

            string greeting = "Hello";
            string firstName = "Bob";
            //string message = $"{greeting} {firstName}!";
            Console.WriteLine($@"{greeting} {firstName}!
                        na parte de baixo!");

            // $ -> Interpolação
            // @ -> Abolição dos escapes (\)
        }
    }
}
