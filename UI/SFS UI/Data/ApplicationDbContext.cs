using Microsoft.EntityFrameworkCore;
using SFS_UI.Models;

namespace SFS_UI.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Card> Cards { get; set; }
        public DbSet<Inventory> Inventory { get; set; }
    }
}
