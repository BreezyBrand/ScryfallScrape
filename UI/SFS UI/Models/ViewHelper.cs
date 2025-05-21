using Microsoft.IdentityModel.Tokens;

namespace SFS_UI.Models
{
    public class ViewHelper
    {
        public bool ban_pictures { get; set; }
        public string convertToHTML(string raw)
        {
            if (raw.IsNullOrEmpty())
            {
                return "";
            }

            string html = raw.Replace("\\n", "<br/>")
                     .Replace("\\'", "'");

            html = swapManaSymbols(html);

            return html;
        }

        public string swapManaSymbols(string text)
        {
            //Basic Mana Symbols
            text = text.Replace("{W}", "<div class='imgBlock wMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White Mana' /></div>")
                       .Replace("{U}", "<div class='imgBlock uMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Blue Mana' /></div>")
                       .Replace("{B}", "<div class='imgBlock bMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Black Mana' /></div>")
                       .Replace("{R}", "<div class='imgBlock rMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Red Mana' /></div>")
                       .Replace("{G}", "<div class='imgBlock gMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Green Mana' /></div>")
                       .Replace("{C}", "<div class='imgBlock cMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless Mana' /></div>")
                       .Replace("{X}", "<div class='imgBlock xMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='X Mana' /></div>")
                       .Replace("{S}", "<div class='imgBlock sMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Snow Mana' /></div>");

            //Action Symbols
            text = text.Replace("{T}", "<div class='imgBlock tSymb'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Tap' /></div>")
                       .Replace("{Q}", "<div class='imgBlock uSymb'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Untap' /></div>");

            //Color Hybrid Symbols
            text = text.Replace("{W/U}", "<div class='imgBlock wuMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White/Blue Hybrid Mana' /></div>")
                       .Replace("{W/B}", "<div class='imgBlock wbMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White/Black Hybrid Mana' /></div>")
                       .Replace("{R/W}", "<div class='imgBlock rwMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White/Red Hybrid Mana' /></div>")
                       .Replace("{G/W}", "<div class='imgBlock gwMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White/Green Hybrid Mana' /></div>")
                       .Replace("{U/B}", "<div class='imgBlock ubMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Blue/Black Hybrid Mana' /></div>")
                       .Replace("{U/R}", "<div class='imgBlock urMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Blue/Red Hybrid Mana' /></div>")
                       .Replace("{G/U}", "<div class='imgBlock guMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Blue/Green Hybrid Mana' /></div>")
                       .Replace("{B/R}", "<div class='imgBlock brMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Black/Red Hybrid Mana' /></div>")
                       .Replace("{B/G}", "<div class='imgBlock bgMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Black/Green Hybrid Mana' /></div>")
                       .Replace("{R/G}", "<div class='imgBlock rgMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Red/Green Hybrid Mana' /></div>");

            //Special Hybrids
            //text = text.Replace("{G/U/P}", "<div class='imgBlock gupMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Green/Blue/Phyrexian Hybrid Mana' /></div>")
            //           .Replace("{G/W/P}", "<div class='imgBlock gwpMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Green/White/Phyrexian Hybrid Mana' /></div>");

            //Phyrexian Symbols
            text = text.Replace("{W/P}", "<div class='imgBlock wpMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='White Phyrexian Mana' /></div>")
                       .Replace("{U/P}", "<div class='imgBlock upMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Blue Phyrexian Mana' /></div>")
                       .Replace("{B/P}", "<div class='imgBlock bpMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Black Phyrexian Mana' /></div>")
                       .Replace("{R/P}", "<div class='imgBlock rpMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Red Phyrexian Mana' /></div>")
                       .Replace("{G/P}", "<div class='imgBlock gpMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Green Phyrexian Mana' /></div>");

            //Hybrid/Colorless Symbols
            text = text.Replace("{C/W}", "<div class='imgBlock cwMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless/White Hybrid Mana' /></div>")
                       .Replace("{C/U}", "<div class='imgBlock cuMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless/Blue Hybrid Mana' /></div>")
                       .Replace("{C/B}", "<div class='imgBlock cbMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless/Black Hybrid Mana' /></div>")
                       .Replace("{C/R}", "<div class='imgBlock crMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless/Red Hybrid Mana' /></div>")
                       .Replace("{C/G}", "<div class='imgBlock cgMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='Colorless/Green Hybrid Mana' /></div>")
                       .Replace("{2/W}", "<div class='imgBlock c2wMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Colorless/White Hybrid Mana' /></div>")
                       .Replace("{2/U}", "<div class='imgBlock c2uMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Colorless/Blue Hybrid Mana' /></div>")
                       .Replace("{2/B}", "<div class='imgBlock c2bMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Colorless/Black Hybrid Mana' /></div>")
                       .Replace("{2/R}", "<div class='imgBlock c2rMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Colorless/Red Hybrid Mana' /></div>")
                       .Replace("{2/G}", "<div class='imgBlock c2gMana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Colorless/Green Hybrid Mana' /></div>");

            //Generic Cost
            text = text.Replace("{0}", "<div class='imgBlock c0mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='0 Generic' /></div>")
                       .Replace("{1}", "<div class='imgBlock c1mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='1 Generic' /></div>")
                       .Replace("{2}", "<div class='imgBlock c2mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='2 Generic' /></div>")
                       .Replace("{3}", "<div class='imgBlock c3mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='3 Generic' /></div>")
                       .Replace("{4}", "<div class='imgBlock c4mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='4 Generic' /></div>")
                       .Replace("{5}", "<div class='imgBlock c5mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='5 Generic' /></div>")
                       .Replace("{6}", "<div class='imgBlock c6mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='6 Generic' /></div>")
                       .Replace("{7}", "<div class='imgBlock c7mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='7 Generic' /></div>")
                       .Replace("{8}", "<div class='imgBlock c8mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='8 Generic' /></div>")
                       .Replace("{9}", "<div class='imgBlock c9mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='9 Generic' /></div>")
                       .Replace("{10}", "<div class='imgBlock c10mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='10 Generic' /></div>")
                       .Replace("{11}", "<div class='imgBlock c11mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='11 Generic' /></div>")
                       .Replace("{12}", "<div class='imgBlock c12mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='12 Generic' /></div>")
                       .Replace("{13}", "<div class='imgBlock c13mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='13 Generic' /></div>")
                       .Replace("{14}", "<div class='imgBlock c14mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='14 Generic' /></div>")
                       .Replace("{15}", "<div class='imgBlock c15mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='15 Generic' /></div>")
                       .Replace("{16}", "<div class='imgBlock c16mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='16 Generic' /></div>")
                       .Replace("{17}", "<div class='imgBlock c17mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='17 Generic' /></div>")
                       .Replace("{18}", "<div class='imgBlock c18mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='18 Generic' /></div>")
                       .Replace("{19}", "<div class='imgBlock c19mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='19 Generic' /></div>")
                       .Replace("{20}", "<div class='imgBlock c20mana'><div class='img-crop'></div><img class='collapse cardSymbol' src='/Images/Symbols/all_symbols.png' alt='20 Generic' /></div>");

            if (this.ban_pictures)
            {
                //text = text.Replace("src=''", "src='Images/filler.png'");
            }

            return text;
        }

    }
}
