import Function as f;

const posX1 = PVariable();
const posX2 = PVariable();

const posY1 = PVariable();
const posY2 = PVariable();

var n = 0;
var max_n = 5;

function savePosRoutine(cp)
{
   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");

   var i = n;

   for (; i > 0; i--)
   {
      posX1[i] = posX1[i - 1];
      posX2[i] = posX2[i - 1];
      posY1[i] = posY1[i - 1];
      posY2[i] = posY2[i - 1];
   }

   posX1[0] = dwread_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20));
   posX2[0] = dwread_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 8));
   posY1[0] = dwread_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 4));
   posY2[0] = dwread_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 12));

   if (n < max_n) n++;
}

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("Recall - Oda", Set);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }

         if (f.loop[cp] == 1)
         {
            if (n == max_n)
            {
               dwwrite_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20), posX1[max_n]);
               dwwrite_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 8), posX2[max_n]);
               dwwrite_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 4), posY1[max_n]);
               dwwrite_epd(EPD(0x58DC60 + (f.location[cp] - 1) * 20 + 12), posY2[max_n]);

               MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);
               CenterView(f.location[cp]);
            }
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 2)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         SetSwitch("Recall - Oda", Clear);
         SetDeaths(cp, SetTo, 2160, " `UniqueCoolTime");
         f.SkillEnd(cp);
      }
   }
   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");

}