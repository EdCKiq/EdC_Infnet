using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace mathApp.Controllers
{
    public class Multiplication : Controller
    {
        public IActionResult Index(int num1, int num2)
        {
            ViewBag.Mul = $"Multiplicação: {num1 * num2}";
            return View();
        }
    }
}
