using Microsoft.AspNetCore.Components;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace SFS_UI.Models
{
    public class CardViews
    {
        public List<Card> Cards { get; set; }
        public List<Inventory> Inventory { get; set; }
        public List<Card> displayCards { get; set; }
        public List<Card> displayInventory { get; set; }
        public void Initialize()
        {
            displayCards = new List<Card>();
            displayInventory = new List<Card>();
        }
        public Card RefToCard(string set, string cn)
        {
            return this.Cards.Where(x =>
                x.set.ToUpper().Equals(set.ToUpper()) &&
                x.collector_number.Equals(cn)
            ).First();
        }
        public void closeNonEssential()
        {
            Cards = new List<Card>();
        }

        public List<Card> getRandomCards()
        {
            Random rand = new Random();            
            int skip = rand.Next(this.Cards.Count());            
            List<Card> sample_cards = this.Cards.Skip(skip).Take(10).ToList();
            List<string> inv_ids = this.Inventory.Select(x => x.CardId).ToList();
            foreach (var card in sample_cards)
            {
                try
                {                    
                    this.displayCards.Add(card);
                }
                catch (Exception e)
                {
                    Debug.WriteLine("Could not load card.");                    
                    this.displayCards.Add(new Card().ErrorCard(card.set, card.collector_number));
                }
            }
            return this.displayCards;
        }

        public List<Card> getRandomCardsFromInventory()
        {
            Random rand = new Random();            
            int skip_Inv = rand.Next(this.Inventory.Count());            
            List<Inventory> showInventory = this.Inventory.Skip(skip_Inv).Take(10).ToList();            

            foreach (var invcard in showInventory)
            {
                try
                {
                    var thisCard = RefToCard(invcard.Set, invcard.Collector_Number);                    
                    this.displayInventory.Add(thisCard);
                }
                catch (Exception e)
                {
                    Debug.WriteLine("Could not load card.");                    
                    this.displayInventory.Add(new Card().ErrorCard(invcard.Set, invcard.Collector_Number));
                }
            }
            return this.displayInventory;
        }
    }
}
