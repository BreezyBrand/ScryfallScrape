using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using SFS_UI.Data;
using SFS_UI.Models;
using System.Diagnostics;

namespace SFS_UI.Controllers
{
    public class ResourceController : Controller
    {
        private readonly ApplicationDbContext _context;
        public ILogger<HomeController> _logger { get; }

        public ResourceController(ApplicationDbContext context, ILogger<HomeController> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IActionResult findCard(string set, string cn)
        {
            Card card = new Card();
            try
            {
                card = _context.Cards.Where(x => x.set.Equals(set) &&
                                                 x.collector_number.Equals(cn)
                                     ).FirstOrDefault();
            }
            catch (Exception ex)
            {

            }
            return PartialView("_DisplayCard", card);
        }

        public IActionResult searchCards(string set, string cn, string name, string type, string oracle, string format)
        {
            List<Card> cards = _context.Cards.ToList();

            //Cascade the search criteria
            if (!set.IsNullOrEmpty())
            {
                cards = cards.Where(x => x.IsInSet(set)).ToList();
            }

            if (!cn.IsNullOrEmpty())
            {
                cards = cards.Where(x => x.collector_number.Equals(cn)).ToList();
            }

            if (!name.IsNullOrEmpty())
            {
                cards = cards.Where(x => x._name.ToUpper().Contains(name.ToUpper())).ToList();
            }

            if (!type.IsNullOrEmpty())
            {
                cards = cards.Where(x => x.type_line.Contains(type)).ToList();
            }

            if (!oracle.IsNullOrEmpty())
            {
                cards = cards.Where(x => x.checkOracle(oracle)).ToList();
            }

            if (!format.IsNullOrEmpty())
            {
                //Need to check legalities
                cards = cards.Where(x => x.IsLegalIn(format)).ToList();
            }

            cards.OrderBy(x => x.set).ThenBy(x => x.collector_number).ToList();
            return PartialView("_SearchCards", cards);
        }
    }
}
