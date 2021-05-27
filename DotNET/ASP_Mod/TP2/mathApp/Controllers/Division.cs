using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace mathApp.Controllers
{
    public class Division : Controller
    {
        public IActionResult Index(float num1, float num2)
        {
            ViewBag.Div = $"Divisão: {num1 / num2}";
            return View();
        }
    }
}
