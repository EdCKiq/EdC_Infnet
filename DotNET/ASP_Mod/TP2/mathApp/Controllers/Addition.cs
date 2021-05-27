using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace mathApp.Controllers
{
    public class Addition : Controller
    {
        public IActionResult Index(int num1,int num2)
        {
            ViewBag.Sum = $"Soma: {num1+num2}";
            return View();
        }

    }
}
