using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Newtonsoft.Json;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Diagnostics;
using System.Linq.Expressions;
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.JavaScript;
using System.Text.Json;

namespace SFS_UI.Models
{
    [Table("Cards")]
    public class Card
    {
        [Key, Column("Id")]
        public string id { get; set; }
        [Column("object")]
        public string _object { get; set; }
        public string oracle_id { get; set; }
        public string multiverse_ids { get; set; }
        public string mtgo_id { get; set; }
        public string mtgo_foil_id { get; set; }
        public string tcgplayer_id { get; set; }
        public string cardmarket_id { get; set; }
        [Column("name")]
        public string _name { get; set; }
        public string lang { get; set; }
        public string released_at { get; set; }
        [Column("uri")]
        public string _uri { get; set; }
        public string scryfall_uri { get; set; }
        public string layout { get; set; }
        public string highres_image { get; set; }
        public string image_status { get; set; }
        public string image_uris { get; set; }
        public string mana_cost { get; set; }
        public string cmc { get; set; }
        public string type_line { get; set; }
        public string oracle_text { get; set; }
        public string power { get; set; }
        public string toughness { get; set; }
        public string colors { get; set; }
        public string color_identity { get; set; }
        public string keywords { get; set; }
        public string legalities { get; set; }
        public string games { get; set; }
        public string reserved { get; set; }
        public string foil { get; set; }
        public string nonfoil { get; set; }
        public string finishes { get; set; }
        public string oversized { get; set; }
        public string promo { get; set; }
        public string reprint { get; set; }
        public string variation { get; set; }
        [Column("set_id")]
        public string _set_id { get; set; }
        public string set { get; set; }
        public string set_name { get; set; }
        public string set_type { get; set; }
        public string set_uri { get; set; }
        public string set_search_uri { get; set; }
        public string scryfall_set_uri { get; set; }
        public string rulings_uri { get; set; }
        public string prints_search_uri { get; set; }
        public string collector_number { get; set; }
        public string digital { get; set; }
        public string rarity { get; set; }
        public string flavor_text { get; set; }
        public string card_back_id { get; set; }
        public string artist { get; set; }
        public string artist_ids { get; set; }
        public string illustration_id { get; set; }
        public string border_color { get; set; }
        public string frame { get; set; }
        public string full_art { get; set; }
        public string textless { get; set; }
        public string booster { get; set; }
        public string story_spotlight { get; set; }
        public string edhrec_rank { get; set; }
        public string penny_rank { get; set; }
        public string prices { get; set; }
        public string related_uris { get; set; }
        public string purchase_uris { get; set; }
        public string all_parts { get; set; }
        public string promo_types { get; set; }
        public string arena_id { get; set; }
        public string security_stamp { get; set; }
        public string card_faces { get; set; }
        public string preview { get; set; }
        public string produced_mana { get; set; }
        public string watermark { get; set; }
        public string frame_effects { get; set; }
        public string loyalty { get; set; }
        public string printed_name { get; set; }
        public string DisplayNumber()
        {
            var len = this.collector_number.Length;

            if (len.Equals(1))
            {
                return "00" + this.collector_number;
            }
            else if (len.Equals(2))
            {
                return "0" + this.collector_number;
            }
            if (len.Equals(3))
            {
                return this.collector_number;
            }
            else if (len.Equals(4))
            {
                return this.collector_number;
            }
            return this.collector_number;
        }
        public List<CardFace> splitCardFaces()
        {
            string jsonString = this.card_faces.Replace("\"","\"");
            try
            {
                var formatedFaces = new List<CardFace>();
                var faces = JsonDocument.Parse(jsonString);

                for (int i = 0; i < faces.RootElement.GetArrayLength(); i++)
                {
                    var charstring = faces.RootElement[i].ToString().Replace('[', '"').Replace(']', '"');
                    var result = JsonConvert.DeserializeObject<CardFace>(charstring);
                    formatedFaces.Add(result);
                }

                return formatedFaces;
            }
            catch (Exception e)
            {
                return new List<CardFace>();
            }
        }
        public bool IsInSet(string set)
        {
            string normalizedSetRequest = set.ToUpper();
            string normalizedSetCard = this.set.ToUpper();

            return normalizedSetCard.Equals(normalizedSetRequest);
        }
        public bool IsLegalIn(string format)
        {
            JsonDocument legalities = JsonDocument.Parse(this.legalities);
            var thisFormat = legalities.RootElement.GetProperty(format).GetString();

            switch (thisFormat)
            {
                case "Legal":
                    return true;
                case "Restricted":
                    return true;
                default:
                    // code block
                    return false;
            }
        }
        public bool checkOracle(string oracle)
        {
            string normalizedOracleRequest = oracle.ToUpper();
            string normalizedOracleCard = this.oracle_text.ToUpper();
            normalizedOracleCard = normalizedOracleCard.Replace(this._name.ToUpper(), " ~ ");

            if (normalizedOracleCard.Contains('~'))
            {
                Debug.WriteLine("This card states its own name");
            }

            return normalizedOracleCard.Contains(normalizedOracleRequest);
        }
        public Card ErrorCard(string set, string cn)
        {
            this._name = set + ":" + cn;
            return this;
        }
    }
    [Table("Inventory"), PrimaryKey(nameof(Set), nameof(Collector_Number), nameof(foiled))]
    public class Inventory
    {
        public string Set { get; set; }
        [Column("Collector Number")]
        public string Collector_Number { get; set; }
        public string foiled { get; set; }
        public int Quantity { get; set; }
        public string Proxied { get; set; }
    }

    //Non-Table Models

    public class CardFace
    {
        [JsonProperty("object")]
        public string _object { get; set; }
        [JsonProperty("name")]
        public string name { get; set; }
        [JsonProperty("mana_cost")]
        public string mana_cost { get; set; }
        [JsonProperty("type_line")]
        public string type_line { get; set; }
        [JsonProperty("oracle_text")]
        public string oracle_text { get; set; }
        [JsonProperty("colors")]
        public string colors { get; set; }
        [JsonProperty("flavor_text")]
        public string flavor_text { get; set; }
        [JsonProperty("artist")]
        public string artist { get; set; }
        [JsonProperty("artist_id")]
        public string artist_id { get; set; }
        [JsonProperty("illustration_id")]
        public string illustration_id { get; set; }
        //[JsonProperty("image_uris")]
        //public List<string> image_uris { get; set; }
        //'small':
        //'normal':
        //'large':
        //'png':
        //'art_crop':
        //'border_crop'

    }
}
