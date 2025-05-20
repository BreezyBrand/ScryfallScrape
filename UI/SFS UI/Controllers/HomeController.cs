using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using SFS_UI.Data;
using SFS_UI.Models;
using System.Diagnostics;

namespace SFS_UI.Controllers
{
    public class HomeController : Controller
    {
        private readonly ApplicationDbContext _context;        
        public ILogger<HomeController> _logger { get; }

        public HomeController(ApplicationDbContext context, ILogger<HomeController> logger)
        {
            _context = context;            
            _logger = logger;            
        }

        public IActionResult Index()
        {
            CardViews vm = new CardViews()
            {
                Cards = _context.Cards.ToList(),
                Inventory = _context.Inventory.ToList(),                
            };
            vm.Initialize();
            vm.getRandomCardsFromInventory();
            vm.getRandomCards();
            //vm.closeNonEssential();
            return View(vm);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}
